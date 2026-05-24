from __future__ import annotations

import base64
import html
import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")
SCRIPT_DIR = ROOT / "scripts"
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from fill_docs_detail_pages import (  # type: ignore
    TOPIC_DATA,
    DOC_LABELS_EN,
    DOC_LABELS_ZH,
    build_title_desc,
    render_links,
)


API_URL = "https://api.github.com/repos/zhaobingkun/DeepSeek-TUI/contents/docs"
SYNC_DIR = ROOT / "upstream-docs"
DOMAIN = "https://deepseek-tui.app"

SLUG_TO_FILENAME = {
    "accessibility": "ACCESSIBILITY.md",
    "architecture": "ARCHITECTURE.md",
    "competitive-analysis": "COMPETITIVE_ANALYSIS.md",
    "configuration": "CONFIGURATION.md",
    "docker": "DOCKER.md",
    "install": "INSTALL.md",
    "keybindings": "KEYBINDINGS.md",
    "legacy-rust-audit-0-7-6": "LEGACY_RUST_AUDIT_0_7_6.md",
    "localization": "LOCALIZATION.md",
    "mcp": "MCP.md",
    "memory": "MEMORY.md",
    "modes": "MODES.md",
    "operations-runbook": "OPERATIONS_RUNBOOK.md",
    "release-runbook": "RELEASE_RUNBOOK.md",
    "runtime-api": "RUNTIME_API.md",
    "subagents": "SUBAGENTS.md",
    "tool-surface": "TOOL_SURFACE.md",
    "v0-7-5-implementation-plan": "V0_7_5_IMPLEMENTATION_PLAN.md",
    "capacity-controller": "capacity_controller.md",
    "v0-8-8-coordinator-prompt": "v0.8.8-coordinator-prompt.md",
}


def run_curl(url: str) -> str:
    result = subprocess.run(
        ["curl", "-Ls", "--retry", "4", "--retry-delay", "1", "--retry-all-errors", url],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout


def fetch_manifest() -> dict[str, dict]:
    data = json.loads(run_curl(API_URL))
    manifest: dict[str, dict] = {}
    for item in data:
        if item.get("type") != "file":
            continue
        manifest[item["name"]] = item
    return manifest


def fetch_blob_text(item: dict) -> str:
    blob = json.loads(run_curl(item["git_url"]))
    content = blob.get("content", "")
    encoding = blob.get("encoding")
    if encoding != "base64":
        raise RuntimeError(f"Unsupported blob encoding for {item['name']}: {encoding}")
    return base64.b64decode(content).decode("utf-8")


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def escape_inline(text: str) -> str:
    return html.escape(text, quote=False)


def render_inline(text: str, file_map: dict[str, str]) -> str:
    placeholders: list[str] = []

    def stash(match: re.Match[str]) -> str:
        placeholders.append(match.group(1))
        return f"@@CODE{len(placeholders)-1}@@"

    text = re.sub(r"`([^`]+)`", stash, text)
    text = escape_inline(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", text)

    def repl_link(match: re.Match[str]) -> str:
        label = match.group(1)
        url = match.group(2).strip()
        rewritten = file_map.get(url, url)
        return f'<a href="{html.escape(rewritten, quote=True)}">{html.escape(label)}</a>'

    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", repl_link, text)

    for index, code in enumerate(placeholders):
        text = text.replace(f"@@CODE{index}@@", f"<code>{html.escape(code)}</code>")
    return text


def parse_table(lines: list[str], start: int, file_map: dict[str, str]) -> tuple[str, int]:
    header = [cell.strip() for cell in lines[start].strip().strip("|").split("|")]
    rows = []
    i = start + 2
    while i < len(lines) and "|" in lines[i] and lines[i].strip():
        rows.append([cell.strip() for cell in lines[i].strip().strip("|").split("|")])
        i += 1
    thead = "".join(f"<th>{render_inline(cell, file_map)}</th>" for cell in header)
    tbody = "".join(
        "<tr>" + "".join(f"<td>{render_inline(cell, file_map)}</td>" for cell in row) + "</tr>"
        for row in rows
    )
    return f'<table><thead><tr>{thead}</tr></thead><tbody>{tbody}</tbody></table>', i


def parse_list(lines: list[str], start: int, file_map: dict[str, str], ordered: bool) -> tuple[str, int]:
    pattern = r"^\d+\.\s+" if ordered else r"^[-*]\s+"
    tag = "ol" if ordered else "ul"
    items: list[str] = []
    i = start

    while i < len(lines):
        stripped = lines[i].strip()
        if not re.match(pattern, stripped):
            break

        item_lines = [re.sub(pattern, "", stripped)]
        i += 1

        while i < len(lines):
            raw = lines[i]
            nxt = raw.strip()
            if not nxt:
                break
            if re.match(pattern, nxt):
                break
            if re.match(r"^(#{1,6})\s+", nxt) or nxt.startswith("```") or nxt.startswith(">") or re.match(r"^---+$", nxt):
                break
            if i + 1 < len(lines) and "|" in lines[i] and re.match(r"^\s*\|?[\s:-]+\|[\s|:-]*$", lines[i + 1]):
                break
            if raw.startswith("  ") or raw.startswith("\t"):
                item_lines.append(nxt)
                i += 1
                continue
            break

        items.append(" ".join(item_lines))

        while i < len(lines) and not lines[i].strip():
            i += 1
            if i < len(lines) and re.match(pattern, lines[i].strip()):
                break

    html_items = "".join(f"<li>{render_inline(item, file_map)}</li>" for item in items)
    return f"<{tag}>{html_items}</{tag}>", i


def render_markdown(md: str, file_map: dict[str, str]) -> tuple[str, list[tuple[int, str, str]]]:
    lines = md.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    i = 0
    parts: list[str] = []
    headings: list[tuple[int, str, str]] = []

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            i += 1
            block: list[str] = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            if i < len(lines):
                i += 1
            class_attr = f' class="language-{html.escape(lang, quote=True)}"' if lang else ""
            parts.append(f"<pre><code{class_attr}>{html.escape(chr(10).join(block))}</code></pre>")
            continue

        heading_match = re.match(r"^(#{1,6})\s+(.*)$", stripped)
        if heading_match:
            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            heading_id = slugify(heading_text)
            headings.append((level, heading_text, heading_id))
            parts.append(f'<h{level} id="{heading_id}">{render_inline(heading_text, file_map)}</h{level}>')
            i += 1
            continue

        if i + 1 < len(lines) and "|" in lines[i] and re.match(r"^\s*\|?[\s:-]+\|[\s|:-]*$", lines[i + 1]):
            table_html, i = parse_table(lines, i, file_map)
            parts.append(table_html)
            continue

        if re.match(r"^[-*]\s+", stripped):
            list_html, i = parse_list(lines, i, file_map, ordered=False)
            parts.append(list_html)
            continue

        if re.match(r"^\d+\.\s+", stripped):
            list_html, i = parse_list(lines, i, file_map, ordered=True)
            parts.append(list_html)
            continue

        if stripped.startswith(">"):
            quote_lines = []
            while i < len(lines) and lines[i].strip().startswith(">"):
                quote_lines.append(lines[i].strip()[1:].strip())
                i += 1
            parts.append("<blockquote><p>" + "<br>".join(render_inline(x, file_map) for x in quote_lines) + "</p></blockquote>")
            continue

        if re.match(r"^---+$", stripped):
            parts.append("<hr>")
            i += 1
            continue

        paragraph = [stripped]
        i += 1
        while i < len(lines):
            nxt = lines[i].strip()
            if not nxt:
                break
            if nxt.startswith("```") or re.match(r"^(#{1,6})\s+", nxt) or re.match(r"^[-*]\s+", nxt) or re.match(r"^\d+\.\s+", nxt) or nxt.startswith(">") or re.match(r"^---+$", nxt):
                break
            if i + 1 < len(lines) and "|" in lines[i] and re.match(r"^\s*\|?[\s:-]+\|[\s|:-]*$", lines[i + 1]):
                break
            paragraph.append(nxt)
            i += 1
        parts.append("<p>" + render_inline(" ".join(paragraph), file_map) + "</p>")
    return "\n".join(parts), headings


def build_file_map() -> dict[str, str]:
    file_map: dict[str, str] = {}
    for slug, filename in SLUG_TO_FILENAME.items():
        file_map[f"./{filename}"] = f"/docs/{slug}/index.html"
        file_map[filename] = f"/docs/{slug}/index.html"
        file_map[f"docs/{filename}"] = f"/docs/{slug}/index.html"
    return file_map


def toc_html(headings: Iterable[tuple[int, str, str]]) -> str:
    items = [
        (level, text, hid)
        for level, text, hid in headings
        if level <= 3
    ]
    if not items:
        return "<p>No section headings found in the upstream doc.</p>"
    return "<ul>" + "".join(
        f'<li class="toc-level-{level}"><a href="#{hid}">{html.escape(text)}</a></li>'
        for level, text, hid in items
    ) + "</ul>"


def build_main(slug: str, zh: bool, doc_html: str, toc: str, source_html_url: str, source_raw_url: str) -> str:
    topic = TOPIC_DATA[slug]
    label = DOC_LABELS_ZH[slug] if zh else DOC_LABELS_EN[slug]
    title, _ = build_title_desc(slug, zh)
    links_html = render_links(topic["related"], zh)
    if zh:
        return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">文档全文</span><h1>{html.escape(title)}</h1><p>{html.escape(topic['summary_zh'])}</p><div class="hero-points"><span>上游源文件：{html.escape(topic['upstream'])}</span><span>站内直接可读</span><span>原文保留在下方</span></div></div><aside class="answer-card"><span class="panel-kicker">本页用途</span><h2>这页现在直接承载上游文档正文，不再只是导读。</h2><p>{html.escape(topic['when_zh'])}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>这份文档真正覆盖什么</h2><p>{html.escape(topic['summary_zh'])}</p><h2>怎么用这页</h2><ul><li>先看右侧目录，直接跳到你当前最关心的小节。</li><li>如果你只是来解决具体问题，优先读正文里的相关标题，再回站内对应 hub。</li><li>如果你要核对原始来源，可以直接打开 GitHub 原文链接。</li></ul></article><aside class="panel-card"><span class="panel-kicker">快速入口</span><div class="link-stack"><a href="{html.escape(source_html_url, quote=True)}">GitHub 文档页</a><a href="{html.escape(source_raw_url, quote=True)}">Raw Markdown</a>{links_html}</div></aside></div></section><section class="section section-alt"><div class="container two-col"><article class="prose doc-article"><h2>上游文档原文（英文）</h2>{doc_html}</article><aside class="panel-card toc-card"><span class="panel-kicker">目录</span>{toc}</aside></div></section></main>"""
    return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">Full Docs Article</span><h1>{html.escape(title)}</h1><p>{html.escape(topic['summary_en'])}</p><div class="hero-points"><span>Upstream source: {html.escape(topic['upstream'])}</span><span>Readable on-site</span><span>Full article embedded below</span></div></div><aside class="answer-card"><span class="panel-kicker">What changed</span><h2>This page now carries the upstream doc body directly instead of acting as a lightweight reading map only.</h2><p>{html.escape(topic['when_en'])}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>What this document actually covers</h2><p>{html.escape(topic['summary_en'])}</p><h2>How to use this page</h2><ul><li>Use the section list on the right to jump into the exact upstream section you need.</li><li>If you came here for one problem only, read the relevant heading first and return to the matching hub afterward.</li><li>If you need source verification, open the GitHub page or raw Markdown directly.</li></ul></article><aside class="panel-card"><span class="panel-kicker">Quick links</span><div class="link-stack"><a href="{html.escape(source_html_url, quote=True)}">GitHub doc page</a><a href="{html.escape(source_raw_url, quote=True)}">Raw Markdown</a>{links_html}</div></aside></div></section><section class="section section-alt"><div class="container two-col"><article class="prose doc-article"><h2>Full upstream document</h2>{doc_html}</article><aside class="panel-card toc-card"><span class="panel-kicker">Contents</span>{toc}</aside></div></section></main>"""


def process_page(path: Path, slug: str, zh: bool, doc_html: str, toc: str, source_html_url: str, source_raw_url: str) -> None:
    text = path.read_text(encoding="utf-8")
    title, desc = build_title_desc(slug, zh)
    text = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)}</title>", text, count=1, flags=re.S)
    text = re.sub(r'<meta name="description" content=".*?">', f'<meta name="description" content="{html.escape(desc)}">', text, count=1, flags=re.S)
    text = re.sub(r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{html.escape(title)}">', text, count=1, flags=re.S)
    text = re.sub(r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{html.escape(desc)}">', text, count=1, flags=re.S)
    text = re.sub(r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{html.escape(title)}">', text, count=1, flags=re.S)
    text = re.sub(r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{html.escape(desc)}">', text, count=1, flags=re.S)
    text = re.sub(r'"headline": ".*?"', f'"headline": "{html.escape(title)}"', text, count=1)
    text = re.sub(r'"name": ".*?"', f'"name": "{html.escape(title)}"', text, count=1)
    text = re.sub(r'"description": ".*?"', f'"description": "{html.escape(desc)}"', text, count=1)
    text = re.sub(
        r"<main>.*?</main>",
        lambda _m: build_main(slug, zh, doc_html, toc, source_html_url, source_raw_url),
        text,
        count=1,
        flags=re.S,
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    manifest = fetch_manifest()
    file_map = build_file_map()
    SYNC_DIR.mkdir(parents=True, exist_ok=True)

    for slug, filename in SLUG_TO_FILENAME.items():
        item = manifest.get(filename)
        if not item:
            raise RuntimeError(f"Upstream doc not found for {slug}: {filename}")
        markdown_text = fetch_blob_text(item)
        (SYNC_DIR / filename).write_text(markdown_text, encoding="utf-8")
        rendered, headings = render_markdown(markdown_text, file_map)
        toc = toc_html(headings)
        process_page(ROOT / "docs" / slug / "index.html", slug, False, rendered, toc, item["html_url"], item["download_url"])
        process_page(ROOT / "zh" / "docs" / slug / "index.html", slug, True, rendered, toc, item["html_url"], item["download_url"])


if __name__ == "__main__":
    main()
