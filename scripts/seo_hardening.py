from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")
DOMAIN = "https://deepseek-tui.app"

SECTION_LABELS_EN = {
    "guides": "Guides",
    "docs": "Docs",
    "install": "Install",
    "config": "Config",
    "modes": "Modes",
    "comparisons": "Comparisons",
    "troubleshooting": "Troubleshooting",
    "mcp": "MCP",
    "skills": "Skills",
    "news": "News",
    "about": "About",
    "contact": "Contact",
}

SECTION_LABELS_ZH = {
    "guides": "指南",
    "docs": "文档",
    "install": "安装",
    "config": "配置",
    "modes": "模式",
    "comparisons": "对比",
    "troubleshooting": "排错",
    "mcp": "MCP",
    "skills": "Skills",
    "news": "新闻",
    "about": "关于",
    "contact": "联系",
}

DOC_LABELS_EN = {
    "accessibility": "Accessibility Docs",
    "architecture": "Architecture Docs",
    "competitive-analysis": "Competitive Analysis Docs",
    "configuration": "Configuration Docs",
    "docker": "Docker Docs",
    "install": "Install Docs",
    "keybindings": "Keybindings Docs",
    "legacy-rust-audit-0-7-6": "Legacy Rust Audit 0.7.6",
    "localization": "Localization Docs",
    "mcp": "MCP Docs",
    "memory": "Memory Docs",
    "modes": "Modes Docs",
    "operations-runbook": "Operations Runbook",
    "release-runbook": "Release Runbook",
    "runtime-api": "Runtime API Docs",
    "subagents": "Subagents Docs",
    "tool-surface": "Tool Surface Docs",
    "v0-7-5-implementation-plan": "v0.7.5 Implementation Plan",
    "capacity-controller": "Capacity Controller",
    "v0-8-8-coordinator-prompt": "v0.8.8 Coordinator Prompt",
}

DOC_LABELS_ZH = {
    "accessibility": "可访问性文档",
    "architecture": "架构文档",
    "competitive-analysis": "竞争分析文档",
    "configuration": "配置文档",
    "docker": "Docker 文档",
    "install": "安装文档",
    "keybindings": "快捷键文档",
    "legacy-rust-audit-0-7-6": "旧版 Rust 审计 0.7.6",
    "localization": "本地化文档",
    "mcp": "MCP 文档",
    "memory": "记忆文档",
    "modes": "模式文档",
    "operations-runbook": "运维手册",
    "release-runbook": "发布手册",
    "runtime-api": "运行时 API 文档",
    "subagents": "子代理文档",
    "tool-surface": "工具边界文档",
    "v0-7-5-implementation-plan": "v0.7.5 实现计划",
    "capacity-controller": "容量控制器文档",
    "v0-8-8-coordinator-prompt": "v0.8.8 协调器提示词",
}


def extract(text: str, pattern: str) -> str:
    match = re.search(pattern, text, re.S)
    return match.group(1).strip() if match else ""


def replace_once(text: str, pattern: str, repl: str) -> str:
    if not re.search(pattern, text, re.S):
        return text
    return re.sub(pattern, repl, text, count=1, flags=re.S)


def prettify_slug(slug: str) -> str:
    return slug.replace("-", " ").replace("cli", "CLI").title()


def canonical_to_path(canonical: str) -> str:
    path = canonical.replace(DOMAIN, "")
    return path or "/"


def page_type(path: str) -> str:
    if path in {"/", "/index.html", "/zh/index.html"}:
        return "WebPage"
    if path.endswith("/about/index.html"):
        return "AboutPage"
    if path.endswith("/contact/index.html"):
        return "ContactPage"
    parts = [p for p in path.strip("/").split("/") if p]
    if not parts:
        return "WebPage"
    if parts[-1] == "index.html" and len(parts) <= 2:
        return "CollectionPage"
    if len(parts) >= 2 and parts[-2] == "news":
        return "NewsArticle"
    return "Article"


def breadcrumb_items(path: str, title: str, zh: bool) -> list[dict]:
    if path in {"/", "/index.html", "/zh/index.html"}:
        return []
    parts = [p for p in path.strip("/").split("/") if p]
    items = []
    if zh:
        items.append({"@type": "ListItem", "position": 1, "name": "首页", "item": f"{DOMAIN}/zh/index.html"})
    else:
        items.append({"@type": "ListItem", "position": 1, "name": "Home", "item": f"{DOMAIN}/index.html"})
    if zh and parts and parts[0] == "zh":
        parts = parts[1:]
    if parts and parts[-1] == "index.html":
        parts = parts[:-1]
    pos = 2
    current = "/zh" if zh else ""
    for idx, part in enumerate(parts):
        current += f"/{part}"
        if idx == 0:
            label = (SECTION_LABELS_ZH if zh else SECTION_LABELS_EN).get(part, DOC_LABELS_ZH.get(part, DOC_LABELS_EN.get(part, prettify_slug(part))))
        elif parts and parts[0] == "docs":
            label = (DOC_LABELS_ZH if zh else DOC_LABELS_EN).get(part, prettify_slug(part))
        else:
            label = prettify_slug(part) if not zh else DOC_LABELS_ZH.get(part, SECTION_LABELS_ZH.get(part, part.replace("-", " ")))
        items.append({"@type": "ListItem", "position": pos, "name": label, "item": f"{DOMAIN}{current}/index.html"})
        pos += 1
    if items:
        items[-1]["name"] = title
        items[-1]["item"] = f"{DOMAIN}{path}"
    return items


def ensure_og_and_twitter(text: str, title: str, desc: str, canonical: str, og_type: str) -> str:
    og_block = (
        f'\n  <meta property="og:title" content="{title}">'
        f'\n  <meta property="og:description" content="{desc}">'
        f'\n  <meta property="og:type" content="{og_type}">'
        f'\n  <meta property="og:url" content="{canonical}">'
        '\n  <meta property="og:site_name" content="DeepSeek TUI Guide">'
        f'\n  <meta name="twitter:card" content="summary_large_image">'
        f'\n  <meta name="twitter:title" content="{title}">'
        f'\n  <meta name="twitter:description" content="{desc}">'
    )
    if 'property="og:title"' not in text:
        text = text.replace('<meta name="robots" content="index, follow">', f'<meta name="robots" content="index, follow">{og_block}', 1)
    else:
        if 'name="twitter:title"' not in text:
            text = text.replace('<meta name="twitter:card" content="summary_large_image">', f'<meta name="twitter:card" content="summary_large_image">\n  <meta name="twitter:title" content="{title}">\n  <meta name="twitter:description" content="{desc}">', 1)
    return text


def build_schema(path: str, title: str, desc: str, canonical: str, zh: bool) -> str:
    ptype = page_type(path)
    if path in {"/", "/index.html"}:
        graph = [
            {"@type": "WebSite", "name": "DeepSeek TUI Guide", "url": f"{DOMAIN}/"},
            {"@type": "Organization", "name": "DeepSeek TUI Guide", "url": f"{DOMAIN}/"},
        ]
    elif path == "/zh/index.html":
        graph = [
            {"@type": "WebSite", "name": "DeepSeek TUI 中文指南", "url": f"{DOMAIN}/zh/index.html"},
            {"@type": "Organization", "name": "DeepSeek TUI 中文指南", "url": f"{DOMAIN}/zh/index.html"},
        ]
    else:
        primary = {
            "@type": ptype,
            "headline": title,
            "name": title,
            "description": desc,
            "url": canonical,
            "inLanguage": "zh-CN" if zh else "en",
        }
        graph = [primary]
        crumbs = breadcrumb_items(path, title, zh)
        if crumbs:
            graph.append({"@type": "BreadcrumbList", "itemListElement": crumbs})
    payload = {"@context": "https://schema.org", "@graph": graph}
    return '<script type="application/ld+json">\n' + json.dumps(payload, ensure_ascii=False, indent=2) + '\n  </script>'


def cleanup_docs_page(text: str, path: Path, zh: bool) -> str:
    parts = path.parts
    try:
        idx = parts.index("docs")
    except ValueError:
        return text
    slug = parts[idx + 1]
    label = (DOC_LABELS_ZH if zh else DOC_LABELS_EN).get(slug)
    if not label:
        return text
    if zh:
        title = f"DeepSeek TUI {label}"
        desc = f"围绕上游文档主题，理解 {label} 在 DeepSeek TUI 工作流里为什么值得单独阅读。"
        h1 = f"为什么 {label} 对 DeepSeek TUI 用户值得单独看"
        intro = f"{label} 这类页面的价值，在于它把仓库里的特定主题重新整理成更容易搜索和决策的入口。"
    else:
        title = f"DeepSeek TUI {label}"
        desc = f"Read the upstream docs topic in context and understand why {label.lower()} matters for DeepSeek TUI users."
        h1 = f"Why {label} matter for DeepSeek TUI users"
        intro = f"{label} pages matter because they turn a repo topic into a clearer search and workflow entry point."
    text = replace_once(text, r"<title>.*?</title>", f"<title>{title}</title>")
    text = replace_once(text, r'<meta name="description" content=".*?">', f'<meta name="description" content="{desc}">')
    text = replace_once(text, r"<h1>.*?</h1>", f"<h1>{h1}</h1>")
    text = replace_once(text, r"<p>(?!.*?Direct Answer).*?</p>", f"<p>{intro}</p>")
    return text


def process_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)
    zh = rel.parts[0] == "zh"
    if ("docs" in rel.parts) and rel.name == "index.html" and (len(rel.parts) >= 3):
        text = cleanup_docs_page(text, rel, zh)
    title = extract(text, r"<title>(.*?)</title>")
    desc = extract(text, r'<meta name="description" content="(.*?)">')
    canonical = extract(text, r'<link rel="canonical" href="(.*?)">')
    path_str = canonical_to_path(canonical)
    og_type = "website" if page_type(path_str) in {"WebPage", "CollectionPage", "AboutPage", "ContactPage"} else "article"
    text = ensure_og_and_twitter(text, title, desc, canonical, og_type)
    if 'application/ld+json' not in text:
        schema = build_schema(path_str, title, desc, canonical, zh)
        text = text.replace("</head>", f"  {schema}\n</head>", 1)
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path in ROOT.rglob("index.html"):
        process_file(path)


if __name__ == "__main__":
    main()
