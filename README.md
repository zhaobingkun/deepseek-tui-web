# DeepSeek TUI Guide

Static micro-site focused on the search intent around `DeepSeek TUI`.

Current structure:

- Homepage
- Guides hub
- Docs hub
- Install hub
- npm install page
- cargo install page
- Homebrew install page
- Config hub
- API key setup page
- Provider setup page
- Config file location page
- Environment variables page
- Modes hub
- Plan mode page
- Yolo mode page
- Plan mode vs yolo mode page
- MCP hub
- MCP setup page
- MCP servers page
- MCP server examples page
- Skills hub
- Skills examples page
- Skills vs prompts page
- Comparisons hub
- DeepSeek TUI vs Claude Code page
- DeepSeek TUI vs Codex CLI page
- Troubleshooting hub
- Command not found fix page
- Homebrew command not found page
- Release binaries page
- Provider troubleshooting page
- News hub
- What is DeepSeek TUI page
- About
- Contact

Current canonical/domain:

- `https://deepseek-tui.app/`

If you deploy to another domain, replace canonical URLs, sitemap URLs, and `robots.txt`.


Docs sync workflow:

- Upstream GitHub docs are mirrored into local cache under `upstream-docs/`
- Run `python3 scripts/sync_upstream_docs_fulltext.py` to fetch the latest `docs/*.md` from the upstream repo and rebuild `docs/*` plus `zh/docs/*`
- The English docs pages now include the full upstream article body directly
- The Chinese docs pages keep the Chinese site shell and embed the upstream English article body under `上游文档原文（英文）`


Chinese mirror now available under `/zh/` with translated hub and core guide pages.

Current page count:

- `122` HTML pages including English and Chinese mirrors

Latest added pages:

- `docs hub quick routes and docs nav cleanup`
- `deepseek tui windows install`
- `deepseek tui update or upgrade`
- `deepseek tui config reset`
- `deepseek tui provider cost`
- `deepseek tui mcp troubleshooting`
- all five English pages with Chinese mirrors

Suggested next pages:

- `deepseek tui windows install command not found`
- `deepseek tui brew upgrade`
- `deepseek tui config backup`
- `deepseek tui provider limits`
- `deepseek tui mcp timeout`
