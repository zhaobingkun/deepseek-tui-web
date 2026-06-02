from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")
DATE = "2026-05-07"
DOMAIN = "https://deepseek-tui.app"


PAGES = [
    {
        "slug": "windows",
        "section": "install",
        "section_zh": "install",
        "title": "Install DeepSeek TUI on Windows",
        "description": "Install DeepSeek TUI on Windows without guessing whether npm, cargo, or another route fits your shell setup.",
        "eyebrow": "Windows Install",
        "h1": "DeepSeek TUI on Windows usually works best when you match the install path to your shell and terminal setup",
        "intro": "Windows users often do not have the same terminal defaults as macOS and Linux users, so the best install route depends on whether your current workflow already lives in Node, Rust, WSL, or a mixed shell setup.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Use the install path that matches the shell environment you already trust on Windows, not the one that looks shortest in a README.",
        "answer_p": "If your workflow already uses Node CLIs, npm is often the cleanest start. If you live in Rust tooling, cargo may still be more predictable.",
        "sections": [
            ("Why Windows feels different", "Windows install questions usually come from shell expectations, PATH behavior, and terminal differences rather than DeepSeek TUI itself."),
            ("What to verify first", "<ul><li>Which shell are you actually using: PowerShell, Command Prompt, Git Bash, or WSL?</li><li>Do you already manage CLI tools through Node or Rust?</li><li>Will your install path stay visible after a shell restart?</li></ul>"),
        ],
        "links": [
            ("/install/", "Back to install hub"),
            ("/install/npm/", "npm install guide"),
            ("/troubleshooting/command-not-found/", "Command not found fix"),
        ],
        "zh_title": "如何在 Windows 上安装 DeepSeek TUI",
        "zh_description": "在 Windows 上安装 DeepSeek TUI，并判断 npm、cargo 或其他路径哪条更适合你的终端环境。",
        "zh_eyebrow": "Windows 安装",
        "zh_h1": "在 Windows 上安装 DeepSeek TUI，先匹配你的 shell 和终端环境，再选命令",
        "zh_intro": "Windows 用户的终端默认环境和 macOS、Linux 不一样，所以最适合的安装方式，取决于你当前更依赖 Node、Rust、WSL，还是混合 shell 组合。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "优先选择和你现在 Windows 终端环境最一致的安装路径，而不是只看 README 里最短的命令。",
        "zh_answer_p": "如果你的 CLI 工具本来就走 Node，全局 npm 往往最顺手；如果你长期用 Rust 工具链，cargo 也可能更稳。",
        "zh_sections": [
            ("为什么 Windows 安装感受会不一样", "很多 Windows 安装问题其实不是 DeepSeek TUI 独有，而是 shell、PATH 和终端差异带来的。"),
            ("先确认什么", "<ul><li>你实际在用的是 PowerShell、命令提示符、Git Bash 还是 WSL？</li><li>你的 CLI 工具平时是更依赖 Node 还是 Rust？</li><li>重启终端后，安装路径还能不能被识别？</li></ul>"),
        ],
        "zh_links": [
            ("/zh/install/", "返回安装总页"),
            ("/zh/install/npm/", "npm 安装"),
            ("/zh/troubleshooting/command-not-found/", "command not found 修复"),
        ],
    },
    {
        "slug": "update-or-upgrade",
        "section": "install",
        "section_zh": "install",
        "title": "How to Update or Upgrade DeepSeek TUI",
        "description": "Understand how to update or upgrade DeepSeek TUI depending on whether you installed it through npm, cargo, Homebrew, or binaries.",
        "eyebrow": "Update and Upgrade",
        "h1": "Updating DeepSeek TUI only feels confusing when you forget which install path owns the tool",
        "intro": "The right update route depends on the package path that installed the binary in the first place. Most upgrade confusion comes from mixing install methods or forgetting which one is active in your shell.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Update DeepSeek TUI through the same package route that currently owns the command in your shell.",
        "answer_p": "Do not mix npm, cargo, Homebrew, and manual binaries unless you are also cleaning up old copies.",
        "sections": [
            ("Why upgrades get messy", "Upgrade problems often come from duplicate installs, stale PATH entries, or switching ecosystems halfway through setup."),
            ("What to check before upgrading", "<ul><li>Which package manager installed the active `deepseek` command?</li><li>Do you have older copies from a previous npm, cargo, or binary install?</li><li>Will your shell still point to the newest version after the update finishes?</li></ul>"),
        ],
        "links": [
            ("/install/", "Back to install hub"),
            ("/troubleshooting/release-binaries/", "Release binaries guide"),
            ("/troubleshooting/command-not-found/", "Command not found fix"),
        ],
        "zh_title": "如何更新或升级 DeepSeek TUI",
        "zh_description": "根据 npm、cargo、Homebrew 或二进制安装路径，理解 DeepSeek TUI 的更新与升级方式。",
        "zh_eyebrow": "更新与升级",
        "zh_h1": "更新 DeepSeek TUI 之所以容易混乱，往往是因为忘了当前命令到底由谁管理",
        "zh_intro": "正确的更新路径，取决于最初是谁把这个命令放进你的 shell。多数升级困惑，都来自混用安装方式或忘了当前生效的是哪一路。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "始终通过当前真正管理 `deepseek` 命令的那条安装路径来更新它。",
        "zh_answer_p": "不要把 npm、cargo、Homebrew 和手动二进制混着更新，除非你也同时清理旧副本。",
        "zh_sections": [
            ("为什么升级容易变乱", "很多升级问题其实不是升级命令错了，而是有重复安装、旧 PATH 或中途换生态导致的。"),
            ("升级前先查什么", "<ul><li>当前生效的 `deepseek` 命令到底来自哪个包管理器？</li><li>你机器上有没有旧的 npm、cargo 或二进制副本？</li><li>升级后 shell 会不会仍然指向旧版本？</li></ul>"),
        ],
        "zh_links": [
            ("/zh/install/", "返回安装总页"),
            ("/zh/troubleshooting/release-binaries/", "Release binaries 页面"),
            ("/zh/troubleshooting/command-not-found/", "command not found 修复"),
        ],
    },
    {
        "slug": "reset",
        "section": "config",
        "section_zh": "config",
        "title": "How to Reset DeepSeek TUI Config",
        "description": "Reset DeepSeek TUI config when your current file, provider settings, or environment variables have become too confusing to trust.",
        "eyebrow": "Config Reset",
        "h1": "Resetting DeepSeek TUI config is often faster than debugging a setup you no longer trust",
        "intro": "Once provider values, file edits, and shell variables start conflicting, a clean reset can be more efficient than continuing to patch an unclear config state.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Reset config when you can no longer tell whether the active behavior comes from the file, the shell, or a stale provider setting.",
        "answer_p": "A reset is useful when your current setup has become harder to reason about than rebuilding it.",
        "sections": [
            ("When reset is the right move", "Resetting is justified when repeated edits no longer change behavior in predictable ways, or when you inherited an old config from a different provider path."),
            ("What to preserve before resetting", "<ul><li>Keep a backup of the current config file.</li><li>Record any custom provider values you still want later.</li><li>Check whether environment variables are overriding the file anyway.</li></ul>"),
        ],
        "links": [
            ("/config/", "Back to config hub"),
            ("/config/file-location/", "Config file location"),
            ("/config/environment-variables/", "Environment variables"),
        ],
        "zh_title": "如何重置 DeepSeek TUI 配置",
        "zh_description": "当当前配置文件、provider 设置或环境变量已经混乱到不值得继续修时，重置 DeepSeek TUI 配置会更快。",
        "zh_eyebrow": "配置重置",
        "zh_h1": "当你已经无法信任当前配置状态时，重置 DeepSeek TUI 往往比继续补丁式排查更快",
        "zh_intro": "一旦 provider、配置文件和 shell 环境变量开始互相打架，重新建立一个干净配置，通常比继续猜哪个值在生效更省时间。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "当你已经说不清当前行为到底来自配置文件、环境变量还是旧 provider 设置时，就该考虑重置。",
        "zh_answer_p": "如果现在的配置状态比重新搭一遍还难理解，重置就是更现实的路。",
        "zh_sections": [
            ("什么时候该重置", "当你已经多次修改却无法稳定改变行为，或者当前配置来自不同 provider 路线的旧遗留时，重置更合理。"),
            ("重置前保留什么", "<ul><li>先备份当前配置文件。</li><li>记下以后还想保留的 provider 值。</li><li>确认是不是环境变量其实一直在覆盖配置文件。</li></ul>"),
        ],
        "zh_links": [
            ("/zh/config/", "返回配置总页"),
            ("/zh/config/file-location/", "配置文件位置"),
            ("/zh/config/environment-variables/", "环境变量"),
        ],
    },
    {
        "slug": "provider-cost",
        "section": "config",
        "section_zh": "config",
        "title": "DeepSeek TUI Provider Cost",
        "description": "Understand provider cost questions around DeepSeek TUI and why the tool cost question usually becomes a provider usage question.",
        "eyebrow": "Provider Cost",
        "h1": "DeepSeek TUI cost questions usually turn into provider cost questions very quickly",
        "intro": "Most users asking about DeepSeek TUI cost are really trying to understand which provider they are paying, how usage is metered, and whether different setup choices change the spend profile.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "DeepSeek TUI itself is usually not the billing layer. The practical cost question is which provider you connect and how that provider meters usage.",
        "answer_p": "That is why cost decisions belong next to provider setup rather than inside a generic pricing page alone.",
        "sections": [
            ("Why provider cost matters more than tool branding", "People search for the tool name, but the actual spending risk often comes from the model provider, request volume, and workflow style behind it."),
            ("What to compare", "<ul><li>Which provider is connected?</li><li>How does that provider meter requests or tokens?</li><li>Does your current mode encourage longer sessions or broader tool use?</li></ul>"),
        ],
        "links": [
            ("/guides/pricing-and-cost/", "Pricing and cost guide"),
            ("/config/provider-setup/", "Provider setup"),
            ("/modes/plan-vs-yolo/", "Plan mode vs yolo mode"),
        ],
        "zh_title": "DeepSeek TUI 的 Provider 成本怎么理解",
        "zh_description": "理解 DeepSeek TUI 的成本问题，以及为什么它最终通常会变成 provider 计费和使用量的问题。",
        "zh_eyebrow": "Provider 成本",
        "zh_h1": "关于 DeepSeek TUI 成本的大多数问题，最后都会落到 provider 成本上",
        "zh_intro": "很多用户问的是 DeepSeek TUI 花多少钱，但真正想确认的，通常是接了哪个 provider、如何计费，以及不同工作流会不会拉高实际成本。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "DeepSeek TUI 本身通常不是主要计费层，真正需要看的是你连接的 provider 以及它的计费方式。",
        "zh_answer_p": "所以成本判断更适合放在 provider 配置旁边，而不是只停留在一个泛泛的 pricing 页面。",
        "zh_sections": [
            ("为什么 provider 成本比工具名更关键", "用户搜索的是工具名，但实际支出往往来自后面的模型 provider、请求量和工作流强度。"),
            ("该比什么", "<ul><li>当前连接的是哪个 provider？</li><li>这个 provider 怎么按请求或 token 计费？</li><li>你现在的模式会不会自然拉长会话或扩大工具使用量？</li></ul>"),
        ],
        "zh_links": [
            ("/zh/guides/pricing-and-cost/", "pricing / cost 页面"),
            ("/zh/config/provider-setup/", "provider 设置"),
            ("/zh/modes/plan-vs-yolo/", "plan vs yolo"),
        ],
    },
    {
        "slug": "mcp-troubleshooting",
        "section": "troubleshooting",
        "section_zh": "troubleshooting",
        "title": "DeepSeek TUI MCP Troubleshooting",
        "description": "Troubleshoot DeepSeek TUI MCP issues by separating basic config problems from MCP-specific server and tool-loading failures.",
        "eyebrow": "MCP Troubleshooting",
        "h1": "DeepSeek TUI MCP troubleshooting gets easier once you stop treating every failure like an MCP problem",
        "intro": "Many MCP issues are really provider, config, or path issues wearing an MCP label. You save time by isolating basic setup first and only then moving into server-level troubleshooting.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Treat MCP as the advanced layer, not the first suspect. Rule out basic config and provider errors before debugging servers and tools.",
        "answer_p": "Otherwise you may spend time debugging the wrong layer entirely.",
        "sections": [
            ("Why MCP failures are easy to misread", "MCP sits on top of a working base install and config path, so a weak foundation can easily look like an MCP-specific failure."),
            ("What to isolate first", "<ul><li>Does the base DeepSeek TUI install work without MCP?</li><li>Are provider auth and config already stable?</li><li>Is the MCP server actually reachable and described the way you expect?</li></ul>"),
        ],
        "links": [
            ("/mcp/", "Back to MCP hub"),
            ("/mcp/server-examples/", "MCP server examples"),
            ("/troubleshooting/provider-troubleshooting/", "Provider troubleshooting"),
        ],
        "zh_title": "DeepSeek TUI 的 MCP 排错",
        "zh_description": "排查 DeepSeek TUI 的 MCP 问题，先分清基础配置错误和 MCP server / tool 加载错误。",
        "zh_eyebrow": "MCP 排错",
        "zh_h1": "只要不把所有失败都当成 MCP 问题，DeepSeek TUI 的 MCP 排错就会简单很多",
        "zh_intro": "很多看起来像 MCP 的问题，其实是 provider、配置或路径基础没稳。先把底层装好，再去排 MCP server，本身就能省掉很多时间。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "先把 MCP 当成高级层，而不是第一嫌疑对象。基础配置没排干净之前，不要先钻进 server 细节。",
        "zh_answer_p": "否则你很容易把时间花在错误的层上。",
        "zh_sections": [
            ("为什么 MCP 问题很容易看错", "因为 MCP 是建立在可用的安装和配置之上的，一旦底层不稳，表面上就会像是 MCP 自己坏了。"),
            ("先隔离什么", "<ul><li>不带 MCP 时，基础 DeepSeek TUI 能不能正常工作？</li><li>provider 认证和基础配置是不是已经稳定？</li><li>MCP server 本身是否真的可达、描述也和你预期一致？</li></ul>"),
        ],
        "zh_links": [
            ("/zh/mcp/", "返回 MCP 总页"),
            ("/zh/mcp/server-examples/", "MCP server examples"),
            ("/zh/troubleshooting/provider-troubleshooting/", "provider 排错"),
        ],
    },
]


def page_html(page: dict, zh: bool = False) -> str:
    lang = "zh-CN" if zh else "en"
    prefix = "/zh" if zh else ""
    brand_home = "/zh/" if zh else "/"
    site_name = "DeepSeek TUI 中文指南" if zh else "DeepSeek TUI Guide"
    site_tag = "终端安装与使用中文站" if zh else "Terminal setup and usage hub"
    home_label = "首页" if zh else "Home"
    section_label = {
        "install": "安装" if zh else "Install",
        "config": "配置" if zh else "Config",
        "troubleshooting": "排错" if zh else "Troubleshooting",
    }[page["section"]]
    title = page["zh_title"] if zh else page["title"]
    description = page["zh_description"] if zh else page["description"]
    eyebrow = page["zh_eyebrow"] if zh else page["eyebrow"]
    h1 = page["zh_h1"] if zh else page["h1"]
    intro = page["zh_intro"] if zh else page["intro"]
    answer_kicker = page["zh_answer_kicker"] if zh else page["answer_kicker"]
    answer_h2 = page["zh_answer_h2"] if zh else page["answer_h2"]
    answer_p = page["zh_answer_p"] if zh else page["answer_p"]
    sections = page["zh_sections"] if zh else page["sections"]
    links = page["zh_links"] if zh else page["links"]
    alt_en = f"{DOMAIN}/{page['section']}/{page['slug']}/"
    alt_zh = f"{DOMAIN}/zh/{page['section']}/{page['slug']}/"
    canonical = alt_zh if zh else alt_en
    lang_switch = '<a href="/">English</a>' if zh else '<a href="/zh/">中文</a>'
    nav = (
        f'<a href="{prefix}/">{home_label}</a>'
        f'<a href="{prefix}/guides/">{"指南" if zh else "Guides"}</a>'
        f'<a href="{prefix}/docs/">{"文档" if zh else "Docs"}</a>'
        f'<a href="{prefix}/install/">{"安装" if zh else "Install"}</a>'
        f'<a href="{prefix}/config/">{"配置" if zh else "Config"}</a>'
        f'<a href="{prefix}/modes/">{"模式" if zh else "Modes"}</a>'
        f'<a href="{prefix}/comparisons/">{"对比" if zh else "Comparisons"}</a>'
        f'<a href="{prefix}/troubleshooting/">{"排错" if zh else "Troubleshooting"}</a>'
        f"{lang_switch}"
    )
    footer_desc = "独立中文指南站，聚焦安装、配置、模式、MCP 与排错。" if zh else "Independent guide site for docs, setup, modes, MCP, and troubleshooting."
    footer_links1 = (
        f'<a href="{prefix}/install/">{"安装" if zh else "Install"}</a>'
        f'<a href="{prefix}/config/">{"配置" if zh else "Config"}</a>'
        f'<a href="{prefix}/modes/">{"模式" if zh else "Modes"}</a>'
    )
    footer_links2 = (
        f'<a href="{prefix}/about/">{"关于" if zh else "About"}</a>'
        f'<a href="{prefix}/contact/">{"联系" if zh else "Contact"}</a>'
    )
    section_html = "".join(f"<h2>{heading}</h2><p>{body}</p>" if not body.startswith("<ul>") else f"<h2>{heading}</h2>{body}" for heading, body in sections)
    next_links = "".join(f'<a href="{href}">{label}</a>' for href, label in links)
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{title}</title><meta name="description" content="{description}"><link rel="canonical" href="{canonical}"><meta name="robots" content="index, follow">  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="zh-CN" href="{alt_zh}">
  <link rel="icon" type="image/svg+xml" href="/assets/images/favicon.svg"><link rel="stylesheet" href="/assets/css/site.css"></head>
<body><header class="site-header"><div class="container nav-bar"><a class="brand" href="{brand_home}"><span class="brand-mark">DT</span><span class="brand-text"><strong>{site_name}</strong><small>{site_tag}</small></span></a><nav class="nav-links" data-nav-links>{nav}</nav><button class="nav-toggle" type="button" data-nav-toggle>{"菜单" if zh else "Menu"}</button></div></header><div class="page-path"><div class="container"><a href="{brand_home}">{home_label}</a><span>/</span><a href="{prefix}/{page['section_zh' if zh else 'section']}/">{section_label}</a><span>/</span><span>{page['slug'].replace('-', ' ').title() if not zh else page['zh_eyebrow']}</span></div></div><main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">{eyebrow}</span><h1>{h1}</h1><p>{intro}</p></div><aside class="answer-card"><span class="panel-kicker">{answer_kicker}</span><h2>{answer_h2}</h2><p>{answer_p}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose">{section_html}</article><aside class="panel-card"><span class="panel-kicker">{"下一步" if zh else "Next pages"}</span><div class="link-stack">{next_links}</div></aside></div></section></main><footer class="site-footer"><div class="container footer-grid"><div><h3>{site_name}</h3><p>{footer_desc}</p><p>&copy; <span data-year></span> {site_name}</p></div><div class="footer-links">{footer_links1}</div><div class="footer-links">{footer_links2}</div></div></footer><script src="/assets/js/site.js" defer></script><script src="/assets/js/third-party-loader.js" defer></script></body></html>
"""


def write_pages() -> None:
    for page in PAGES:
        en_path = ROOT / page["section"] / page["slug"] / "index.html"
        zh_path = ROOT / "zh" / page["section"] / page["slug"] / "index.html"
        en_path.parent.mkdir(parents=True, exist_ok=True)
        zh_path.parent.mkdir(parents=True, exist_ok=True)
        en_path.write_text(page_html(page, zh=False), encoding="utf-8")
        zh_path.write_text(page_html(page, zh=True), encoding="utf-8")


def replace_once(text: str, old: str, new: str) -> str:
    if old not in text:
        raise ValueError(f"pattern not found: {old[:80]}")
    return text.replace(old, new, 1)


def update_hubs() -> None:
    install = ROOT / "install" / "index.html"
    text = install.read_text(encoding="utf-8")
    old = '</div>\n    </section>'
    new = '<article class="content-card"><span class="tag">Windows</span><h3>Install DeepSeek TUI on Windows</h3><p>Use this page when shell defaults, PowerShell, Git Bash, or WSL make the install route feel less obvious than macOS examples suggest.</p><a href="/install/windows/">Open Windows install guide</a></article>\n        <article class="content-card"><span class="tag">Update</span><h3>Update or upgrade DeepSeek TUI</h3><p>Use this page when the real issue is not first install, but how to keep the active command current without mixing package paths.</p><a href="/install/update-or-upgrade/">Open update guide</a></article>\n      </div>\n    </section>'
    install.write_text(replace_once(text, old, new), encoding="utf-8")

    zh_install = ROOT / "zh" / "install" / "index.html"
    text = zh_install.read_text(encoding="utf-8")
    old = '</div></div></section>\n  <footer'
    new = '<article class="content-card"><span class="tag">Windows</span><h3>在 Windows 上安装 DeepSeek TUI</h3><p>如果 PowerShell、Git Bash 或 WSL 让安装路线不那么直观，这页更适合先看。</p><a href="/zh/install/windows/">打开 Windows 安装</a></article>\n<article class="content-card"><span class="tag">更新</span><h3>更新或升级 DeepSeek TUI</h3><p>如果你想确认当前命令到底该通过哪条路径更新，这页更直接。</p><a href="/zh/install/update-or-upgrade/">打开更新页</a></article>\n</div></div></section>\n  <footer'
    zh_install.write_text(replace_once(text, old, new), encoding="utf-8")

    config = ROOT / "config" / "index.html"
    text = config.read_text(encoding="utf-8")
    old = '<article class="content-card"><span class="tag">Advanced</span><h3>MCP and skills build on config</h3><p>Do not jump into advanced workflows before the core auth and runtime path is stable.</p><a href="/mcp/">Open MCP guide</a></article></div></section></main>'
    new = '<article class="content-card"><span class="tag">Reset</span><h3>Reset DeepSeek TUI config</h3><p>Use this page when the current config state is so tangled that a clean reset is more efficient than more patching.</p><a href="/config/reset/">Open config reset guide</a></article><article class="content-card"><span class="tag">Cost</span><h3>Provider cost</h3><p>Use this page when your pricing question is really about which provider meters the usage behind DeepSeek TUI.</p><a href="/config/provider-cost/">Open provider cost guide</a></article><article class="content-card"><span class="tag">Advanced</span><h3>MCP and skills build on config</h3><p>Do not jump into advanced workflows before the core auth and runtime path is stable.</p><a href="/mcp/">Open MCP guide</a></article></div></section></main>'
    config.write_text(replace_once(text, old, new), encoding="utf-8")

    zh_config = ROOT / "zh" / "config" / "index.html"
    text = zh_config.read_text(encoding="utf-8")
    old = '<article class="content-card"><span class="tag">MCP</span><h3>MCP 前置理解</h3><p>很多用户会把高级能力和基础配置混在一起，先分清楚会更快。</p><a href="/zh/mcp/">打开 MCP 页</a></article>\n</div></div></section>'
    new = '<article class="content-card"><span class="tag">重置</span><h3>重置 DeepSeek TUI 配置</h3><p>如果当前配置状态已经难以信任，这页会比继续零碎排查更实用。</p><a href="/zh/config/reset/">打开配置重置</a></article>\n<article class="content-card"><span class="tag">成本</span><h3>Provider 成本</h3><p>如果你问的是 DeepSeek TUI 多少钱，这页会把问题拉回真正的 provider 计费层。</p><a href="/zh/config/provider-cost/">打开 provider 成本</a></article>\n<article class="content-card"><span class="tag">MCP</span><h3>MCP 前置理解</h3><p>很多用户会把高级能力和基础配置混在一起，先分清楚会更快。</p><a href="/zh/mcp/">打开 MCP 页</a></article>\n</div></div></section>'
    zh_config.write_text(replace_once(text, old, new), encoding="utf-8")

    troubleshooting = ROOT / "troubleshooting" / "index.html"
    text = troubleshooting.read_text(encoding="utf-8")
    old = '<article class="content-card"><span class="tag">Binaries</span><h3>Release binaries</h3><p>If package-manager friction is the issue, the release-binary route may be the cleaner path.</p><a href="/troubleshooting/release-binaries/">Open release binaries guide</a></article></div></section></main>'
    new = '<article class="content-card"><span class="tag">Binaries</span><h3>Release binaries</h3><p>If package-manager friction is the issue, the release-binary route may be the cleaner path.</p><a href="/troubleshooting/release-binaries/">Open release binaries guide</a></article><article class="content-card"><span class="tag">MCP</span><h3>MCP troubleshooting</h3><p>Use this page when MCP feels broken and you need to separate server-level failures from basic config mistakes.</p><a href="/troubleshooting/mcp-troubleshooting/">Open MCP troubleshooting</a></article></div></section></main>'
    troubleshooting.write_text(replace_once(text, old, new), encoding="utf-8")

    zh_troubleshooting = ROOT / "zh" / "troubleshooting" / "index.html"
    text = zh_troubleshooting.read_text(encoding="utf-8")
    old = '<article class="content-card"><span class="tag">API Key</span><h3>API Key 与 provider</h3><p>如果命令存在但无法使用，配置线通常比安装线更关键。</p><a href="/zh/config/api-key/">打开 API Key 页</a></article>\n</div></div></section>'
    new = '<article class="content-card"><span class="tag">API Key</span><h3>API Key 与 provider</h3><p>如果命令存在但无法使用，配置线通常比安装线更关键。</p><a href="/zh/config/api-key/">打开 API Key 页</a></article>\n<article class="content-card"><span class="tag">MCP</span><h3>MCP 排错</h3><p>如果你怀疑是 MCP 坏了，这页会先帮你分清楚是不是基础配置没稳。</p><a href="/zh/troubleshooting/mcp-troubleshooting/">打开 MCP 排错</a></article>\n</div></div></section>'
    zh_troubleshooting.write_text(replace_once(text, old, new), encoding="utf-8")


def update_nav_and_docs_hubs() -> None:
    index = ROOT / "index.html"
    text = index.read_text(encoding="utf-8")
    old_nav = '<a href="/">Home</a>\n        <a href="/guides/">Guides</a>\n        <a href="/install/">Install</a>'
    new_nav = '<a href="/">Home</a>\n        <a href="/guides/">Guides</a>\n        <a href="/docs/">Docs</a>\n        <a href="/install/">Install</a>'
    text = replace_once(text, old_nav, new_nav)
    index.write_text(text, encoding="utf-8")

    guides = ROOT / "guides" / "index.html"
    text = guides.read_text(encoding="utf-8")
    old_nav = '<a href="/">Home</a>\n        <a href="/guides/">Guides</a>\n        <a href="/install/">Install</a>'
    new_nav = '<a href="/">Home</a>\n        <a href="/guides/">Guides</a>\n        <a href="/docs/">Docs</a>\n        <a href="/install/">Install</a>'
    text = replace_once(text, old_nav, new_nav)
    guides.write_text(text, encoding="utf-8")

    docs = ROOT / "docs" / "index.html"
    text = docs.read_text(encoding="utf-8")
    if "Quick Routes" not in text:
        insert = '<section class="section section-alt"><div class="container"><div class="section-head"><h2>Quick Routes</h2><p>Start with the doc family that matches your immediate question instead of browsing the whole repo tree.</p></div><div class="card-grid card-grid-3"><article class="content-card"><span class="tag">Setup</span><h3>Install and configuration first</h3><p>If your current blocker is first-run setup, start with install docs, configuration docs, and MCP docs before you read architecture pages.</p><a href="/docs/install/">Open install docs</a></article><article class="content-card"><span class="tag">Usage</span><h3>Modes, keybindings, and tool surface</h3><p>If DeepSeek TUI is already running, move into modes, keybindings, runtime API, and tool surface docs next.</p><a href="/docs/modes/">Open usage docs</a></article><article class="content-card"><span class="tag">Maintainers</span><h3>Architecture, runbooks, and release context</h3><p>Use the architecture and runbook docs when you care about internals, release flow, or historical implementation context.</p><a href="/docs/architecture/">Open architecture docs</a></article></div></div></section>'
        text = replace_once(text, '<section class="section"><div class="container"><div class="section-head"><h2>Core Docs</h2>', insert + '<section class="section"><div class="container"><div class="section-head"><h2>Core Docs</h2>')
    docs.write_text(text, encoding="utf-8")

    zh_docs = ROOT / "zh" / "docs" / "index.html"
    text = zh_docs.read_text(encoding="utf-8")
    if "快速路线" not in text:
        insert = '<section class="section section-alt"><div class="container"><div class="section-head"><h2>快速路线</h2><p>先按当前问题进入对应文档线，而不是从头翻完整个仓库文档目录。</p></div><div class="card-grid card-grid-3"><article class="content-card"><span class="tag">上手</span><h3>先看安装与配置</h3><p>如果你现在卡在首次运行，优先看安装文档、配置文档和 MCP 文档，而不是直接跳架构页。</p><a href="/zh/docs/install/">打开安装文档</a></article><article class="content-card"><span class="tag">使用</span><h3>模式、快捷键与工具边界</h3><p>如果 DeepSeek TUI 已经能跑，下一步更值得看模式、快捷键、运行时 API 和工具边界。</p><a href="/zh/docs/modes/">打开使用文档</a></article><article class="content-card"><span class="tag">维护</span><h3>架构、runbook 与版本背景</h3><p>如果你更关心内部结构、发布流程或历史实现背景，就从架构和 runbook 线切入。</p><a href="/zh/docs/architecture/">打开架构文档</a></article></div></div></section>'
        text = replace_once(text, '<section class="section"><div class="container"><div class="section-head"><h2>核心文档</h2>', insert + '<section class="section"><div class="container"><div class="section-head"><h2>核心文档</h2>')
    zh_docs.write_text(text, encoding="utf-8")


def update_readme_and_memory() -> None:
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    text = text.replace("- `112` HTML pages including English and Chinese mirrors", "- `122` HTML pages including English and Chinese mirrors")
    old = "Latest added pages:\n\n- `docs hub and zh docs hub`\n- `accessibility docs page`\n- `architecture docs page`\n- `configuration docs page`\n- `docker docs page`\n- `install docs page`\n- `keybindings docs page`\n- `mcp docs page`\n- `runtime api docs page`\n- `tool surface docs page`\n- plus the rest of the upstream docs topics with Chinese mirrors\n\nSuggested next pages:\n\n- `deepseek tui windows install`\n- `deepseek tui update or upgrade`\n- `deepseek tui config reset`\n- `deepseek tui provider cost`\n- `deepseek tui mcp troubleshooting`\n- `deepseek tui docs overview improvements`\n# deepseek-tui-web\n"
    new = "Latest added pages:\n\n- `docs hub quick routes and docs nav cleanup`\n- `deepseek tui windows install`\n- `deepseek tui update or upgrade`\n- `deepseek tui config reset`\n- `deepseek tui provider cost`\n- `deepseek tui mcp troubleshooting`\n- all five English pages with Chinese mirrors\n\nSuggested next pages:\n\n- `deepseek tui windows install command not found`\n- `deepseek tui brew upgrade`\n- `deepseek tui config backup`\n- `deepseek tui provider limits`\n- `deepseek tui mcp timeout`\n"
    text = replace_once(text, old, new)
    readme.write_text(text, encoding="utf-8")

    memory = ROOT / "PROJECT-MEMORY.md"
    text = memory.read_text(encoding="utf-8")
    text = text.replace("- `112` HTML pages including English and Chinese mirrors", "- `122` HTML pages including English and Chinese mirrors")
    old = "## Recommended Next Batch\n\n- `windows install`\n- `update or upgrade`\n- `config reset`\n- `provider cost`\n- `mcp troubleshooting`\n"
    new = "## Latest Batch Added\n\n- `windows install`\n- `update or upgrade`\n- `config reset`\n- `provider cost`\n- `mcp troubleshooting`\n- Docs hub quick-routes section and Docs nav cleanup\n\n## Recommended Next Batch\n\n- `windows install command not found`\n- `brew upgrade`\n- `config backup`\n- `provider limits`\n- `mcp timeout troubleshooting`\n"
    text = replace_once(text, old, new)
    memory.write_text(text, encoding="utf-8")


def update_sitemap() -> None:
    sitemap = ROOT / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    additions = []
    for page in PAGES:
        additions.append(f'  <url><loc>{DOMAIN}/{page["section"]}/{page["slug"]}/</loc><lastmod>{DATE}</lastmod></url>')
        additions.append(f'  <url><loc>{DOMAIN}/zh/{page["section"]}/{page["slug"]}/</loc><lastmod>{DATE}</lastmod></url>')
    block = "\n".join(additions) + "\n"
    text = text.replace("</urlset>", block + "</urlset>")
    sitemap.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_pages()
    update_hubs()
    update_nav_and_docs_hubs()
    update_readme_and_memory()
    update_sitemap()
