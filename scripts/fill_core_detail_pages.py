from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")
DOMAIN = "https://deepseek-tui.app"

SECTION_LABELS_EN = {
    "install": "Install",
    "config": "Config",
    "mcp": "MCP",
    "modes": "Modes",
}

SECTION_LABELS_ZH = {
    "install": "安装",
    "config": "配置",
    "mcp": "MCP",
    "modes": "模式",
}


PAGES = {
    ("install", "npm"): {
        "title": "Install DeepSeek TUI with npm",
        "description": "Use the npm install path for DeepSeek TUI, verify the global binary, and avoid the most common Node-based setup mistakes.",
        "eyebrow": "npm Install",
        "h1": "Install DeepSeek TUI with npm when Node is already your normal CLI toolchain",
        "intro": "The npm route is strongest when your machine already manages terminal tools through Node. It gives you a familiar global install and a straightforward update path, but only if your shell and global bin path are already in a healthy state.",
        "answer_kicker": "Best Use",
        "answer_h2": "Choose npm when you already trust global Node CLI installs and want the fastest path to a working DeepSeek TUI binary.",
        "answer_p": "If your shell is already using npm-based tools cleanly, this is usually the lowest-friction route. If your Node environment is messy, fix that first or use a different install path.",
        "questions": [
            "When is npm the right route instead of cargo or Homebrew?",
            "What should you verify right after the install finishes?",
            "Which failures are actually Node PATH problems rather than DeepSeek TUI problems?",
        ],
        "steps": [
            ("Confirm the runtime first", "Run `node --version` and `npm --version` before you install. If those basics are unstable, the DeepSeek TUI install will not be your real problem."),
            ("Install globally once", "Use a single global npm install path, not a mix of system Node, nvm shells, and copied binaries."),
            ("Check the active binary", "After install, verify that the `deepseek` command resolves to the same global route you think npm owns."),
        ],
        "checks": [
            "Run `deepseek --version` in a fresh shell, not only the one where you installed it.",
            "Confirm your API key and provider settings before assuming the install failed.",
            "If the command exists but behaves strangely, inspect config and environment variables next.",
        ],
        "mistakes": [
            "Installing with one Node version manager and testing in a shell that uses another.",
            "Treating provider auth failures as install failures.",
            "Updating npm packages but never checking which binary your shell actually calls.",
        ],
        "links": [
            ("Config hub", "/config/index.html"),
            ("API key setup", "/config/api-key/index.html"),
            ("Command not found troubleshooting", "/troubleshooting/command-not-found/index.html"),
        ],
        "examples": [
            ("Fastest npm install path", "Use one global npm route, then verify the command from a fresh shell instead of trusting the install window only.", "npm install -g deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("If you already use nvm or fnm", "Install and verify inside the same Node manager shell so package ownership does not split across different runtimes.", "node --version\nnpm --version\nnpm install -g deepseek-tui\ndeepseek --version"),
        ],
        "failure_routes": [
            ("Install command succeeded but `deepseek` is missing", "That is usually a PATH or shell-profile problem, not an npm package failure. Go to command-not-found troubleshooting before reinstalling."),
            ("`deepseek --version` works in one terminal but not another", "Your Node manager or shell startup files are inconsistent across terminal profiles. Compare the active shell first instead of changing the app."),
        ],
        "zh_title": "用 npm 安装 DeepSeek TUI",
        "zh_description": "使用 npm 安装 DeepSeek TUI，并核对全局二进制、PATH 与最常见的 Node 安装问题。",
        "zh_eyebrow": "npm 安装",
        "zh_h1": "当 Node 已经是你常用 CLI 工具链时，用 npm 安装 DeepSeek TUI 最顺",
        "zh_intro": "如果你平时就通过 Node 管理终端工具，npm 路线通常最省事。它的问题不在命令本身，而在于你的 shell、全局 bin 路径和 Node 管理方式是否已经稳定。",
        "zh_answer_kicker": "最快判断",
        "zh_answer_h2": "当你本来就习惯用 npm 管理全局 CLI，并且 PATH 健康时，npm 往往是最快的安装路径。",
        "zh_answer_p": "如果 Node 环境本身就混乱，先修 Node，再装 DeepSeek TUI；否则你会把底层问题误判成工具问题。",
        "zh_questions": [
            "什么时候该优先选 npm，而不是 cargo 或 Homebrew？",
            "安装结束后最先该核对什么？",
            "哪些失败其实是 Node PATH 问题，而不是 DeepSeek TUI 自己坏了？",
        ],
        "zh_steps": [
            ("先确认运行时", "安装前先跑 `node --version` 和 `npm --version`。如果这一步就不稳，后面装工具只是把问题往后推。"),
            ("只保留一条全局安装路径", "尽量保持一条明确的全局 npm 安装路线，不要把系统 Node、nvm 和手动拷贝二进制混在一起。"),
            ("安装后立即查当前命令", "安装完成后就核对 `deepseek` 命令到底来自哪里，确保和你认为的 npm 路径一致。"),
        ],
        "zh_checks": [
            "在新开的 shell 里跑 `deepseek --version`，不要只在当前安装窗口测试。",
            "先确认 API Key 和 provider 配置是否准备好了，再判断是不是安装失败。",
            "如果命令存在但行为异常，下一步应先查配置和环境变量。",
        ],
        "zh_mistakes": [
            "用一套 Node 管理方式安装，却在另一套 shell 环境里测试。",
            "把 provider 认证报错误判成安装失败。",
            "升级了 npm 包，却从来不核对 shell 实际调用的是哪个二进制。",
        ],
        "zh_links": [
            ("配置总页", "/zh/config/index.html"),
            ("API Key 设置", "/zh/config/api-key/index.html"),
            ("command not found 排错", "/zh/troubleshooting/command-not-found/index.html"),
        ],
        "zh_examples": [
            ("最快的 npm 安装路径", "只保留一条全局 npm 路线，然后在新 shell 里验证，不要只相信安装窗口里的结果。", "npm install -g deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("如果你本来就在用 nvm 或 fnm", "安装和验证都放在同一套 Node 管理器 shell 里完成，避免把不同运行时的包归属混在一起。", "node --version\nnpm --version\nnpm install -g deepseek-tui\ndeepseek --version"),
        ],
        "zh_failure_routes": [
            ("安装命令成功了，但 `deepseek` 不存在", "这通常是 PATH 或 shell profile 问题，不是 npm 包本身失败。先去看 command-not-found 排错，不要先重装。"),
            ("一个终端里能跑，另一个终端里不能跑", "说明 Node 管理器或 shell 启动文件在不同 terminal profile 里不一致。先比 shell，再动应用。"),
        ],
    },
    ("install", "cargo"): {
        "title": "Install DeepSeek TUI with cargo",
        "description": "Use the cargo path for DeepSeek TUI when your terminal workflow already lives in Rust tooling and source-first CLI installs.",
        "eyebrow": "Cargo Install",
        "h1": "Install DeepSeek TUI with cargo when Rust is already part of your normal terminal workflow",
        "intro": "The cargo route makes the most sense if you already use Rust-based CLIs, trust cargo for updates, and want one toolchain to own the binary. It is less attractive if you would only install Rust for this one app.",
        "answer_kicker": "Best Use",
        "answer_h2": "Choose cargo when Rust tooling is already normal on your machine and you want one package ecosystem to own the DeepSeek TUI binary.",
        "answer_p": "Cargo is not automatically better than npm; it is better when it matches the way you already maintain terminal software.",
        "questions": [
            "When does cargo reduce complexity instead of adding it?",
            "What should you check after a cargo install or update?",
            "Which problems belong to Rust toolchain setup rather than the app itself?",
        ],
        "steps": [
            ("Verify cargo first", "Check `cargo --version` before treating the cargo route as ready. Missing toolchain pieces should be fixed before the app install step."),
            ("Install through the active toolchain", "Keep your install tied to the same Rust toolchain you actually use in your shell, especially on multi-toolchain machines."),
            ("Validate the resulting binary path", "Make sure the cargo-owned binary is the one your shell sees after install and after a restart."),
        ],
        "checks": [
            "Confirm `deepseek --version` in a fresh shell.",
            "Check whether an older npm or manual binary is shadowing the cargo install.",
            "Move immediately into provider and config setup once the binary is confirmed.",
        ],
        "mistakes": [
            "Installing Rust only for one app without understanding where cargo puts binaries.",
            "Leaving an older global npm install ahead of cargo in PATH.",
            "Assuming a successful cargo build means provider configuration is also ready.",
        ],
        "links": [
            ("Install hub", "/install/index.html"),
            ("Update or upgrade", "/install/update-or-upgrade/index.html"),
            ("Provider setup", "/config/provider-setup/index.html"),
        ],
        "examples": [
            ("Verify cargo owns the binary you are about to trust", "Before you debug the app, prove that the Rust toolchain and the resolved binary path line up in the same shell.", "cargo --version\ncargo install deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("Check for a shadowed older install", "If cargo install worked but behavior did not change, inspect whether npm or a manual binary still wins PATH.", "command -v deepseek || which deepseek\ndeepseek --version\n# compare with the expected cargo bin path"),
            ("Re-check the cargo bin path after a fresh shell", "Cargo installs often look correct in the install shell. Reopen the terminal and confirm the same path still wins before you move into provider setup.", "command -v deepseek || which deepseek\ndeepseek --version\n# reopen shell and repeat"),
        ],
        "failure_routes": [
            ("Cargo finished cleanly but the command still looks old", "That usually means an older binary is still resolving first. Check PATH ownership before touching provider config."),
            ("`cargo install` fails before the app even builds", "Treat that as a Rust toolchain problem first. Fix cargo and the build environment before you debug DeepSeek TUI itself."),
            ("The command changed, but the next shell cannot find it", "That usually means cargo bin is not exported consistently across shells. Fix shell startup before you debug provider auth."),
        ],
        "zh_title": "用 cargo 安装 DeepSeek TUI",
        "zh_description": "当你的终端工具链本来就以 Rust 为主时，用 cargo 安装 DeepSeek TUI 会更合适。",
        "zh_eyebrow": "Cargo 安装",
        "zh_h1": "如果 Rust 已经是你平时的终端工具链，用 cargo 安装 DeepSeek TUI 会更自然",
        "zh_intro": "cargo 路线最适合本来就长期使用 Rust CLI、也习惯通过 cargo 更新工具的人。如果只是为了这一款工具去装整套 Rust，它就未必是最低摩擦路径。",
        "zh_answer_kicker": "最快判断",
        "zh_answer_h2": "当 Rust 工具链本来就在你的机器上长期稳定使用时，cargo 才是更合理的拥有者。",
        "zh_answer_p": "cargo 并不天然优于 npm；它只是在更符合你现有维护习惯时，才更好。",
        "zh_questions": [
            "什么时候 cargo 会降低复杂度，而不是增加复杂度？",
            "cargo 安装或升级后，最先要核对什么？",
            "哪些问题属于 Rust 工具链，而不是 DeepSeek TUI 本身？",
        ],
        "zh_steps": [
            ("先确认 cargo 自己没问题", "在进入安装之前先跑 `cargo --version`。如果工具链本身就不完整，后面所有问题都会被放大。"),
            ("只通过当前活跃工具链安装", "尤其在多 toolchain 机器上，安装时要确保 cargo 对应的是你平时真正使用的那套 Rust 环境。"),
            ("确认最终二进制路径", "安装后和重启 shell 后，都确认一下当前 `deepseek` 命令是不是 cargo 那一路。"),
        ],
        "zh_checks": [
            "在新 shell 中验证 `deepseek --version`。",
            "检查是不是旧的 npm 或手动二进制挡在 cargo 前面。",
            "确认二进制没问题后，立刻进入 provider 和配置设置。",
        ],
        "zh_mistakes": [
            "只为了这一款工具装 Rust，却不理解 cargo 二进制路径。",
            "PATH 里还残留旧的 npm 全局安装。",
            "把 cargo 编译成功误解成整套配置也已经完成。",
        ],
        "zh_links": [
            ("安装总页", "/zh/install/index.html"),
            ("更新与升级", "/zh/install/update-or-upgrade/index.html"),
            ("provider 设置", "/zh/config/provider-setup/index.html"),
        ],
        "zh_examples": [
            ("先确认 cargo 真是当前拥有者", "在排 app 之前，先证明 Rust 工具链和当前解析到的二进制路径是在同一个 shell 里对齐的。", "cargo --version\ncargo install deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("检查是不是被旧安装挡住了", "如果 cargo 安装成功但行为没变，先看是不是 npm 或手动二进制还在 PATH 前面。", "command -v deepseek || which deepseek\ndeepseek --version\n# 对照预期的 cargo bin 路径"),
            ("重开 shell 后再核对 cargo bin", "很多 cargo 安装在当前终端看起来没问题，但新 shell 里才会暴露路径没接好的问题。", "command -v deepseek || which deepseek\ndeepseek --version\n# 重开 shell 后再重复一次"),
        ],
        "zh_failure_routes": [
            ("cargo 完整装完了，但命令还是旧的", "这通常说明旧二进制还在优先解析。先查 PATH 归属，不要先动 provider 配置。"),
            ("`cargo install` 在构建前就失败", "先把它当成 Rust 工具链问题处理。cargo 和构建环境没稳定前，不要先怪 DeepSeek TUI。"),
            ("当前 shell 能用，换个 shell 就找不到", "通常不是 provider 问题，而是 cargo bin 没有稳定写进各个 shell 的启动路径。"),
        ],
    },
    ("install", "homebrew"): {
        "title": "Install DeepSeek TUI with Homebrew",
        "description": "Use Homebrew to install DeepSeek TUI when your macOS CLI workflow already relies on brew-managed tools and updates.",
        "eyebrow": "Homebrew Install",
        "h1": "Homebrew is the cleanest DeepSeek TUI install path when brew already owns most of your macOS CLI tools",
        "intro": "If your machine already treats Homebrew as the package authority for developer tools, using brew keeps updates and binary ownership clearer than introducing another package path just for one app.",
        "answer_kicker": "Best Use",
        "answer_h2": "Choose Homebrew when you want macOS CLI consistency more than the fastest copy-paste command.",
        "answer_p": "Brew is most helpful when it remains the obvious owner of the binary, not when it competes with npm or manual installs already in PATH.",
        "questions": [
            "When does Homebrew simplify the install story on macOS?",
            "How do you avoid competing binary ownership between brew and other package paths?",
            "Which checks tell you the brew route is truly active?",
        ],
        "steps": [
            ("Confirm brew health", "Make sure `brew --version` and your normal brew install flow already work before adding DeepSeek TUI to that stack."),
            ("Install through the same package owner you update with", "Do not mix a brew install with later updates from npm or cargo unless you are intentionally migrating."),
            ("Verify the active binary path", "After install, inspect which binary your shell resolves first and confirm it matches the brew-managed location."),
        ],
        "checks": [
            "Validate `deepseek --version` after reopening the terminal.",
            "Check whether `/opt/homebrew` or `/usr/local` ordering hides another binary.",
            "Continue into config only after the binary route is clear.",
        ],
        "mistakes": [
            "Using Homebrew because it looks convenient even though another package manager already owns most of your CLI tools.",
            "Updating with brew while the active binary still comes from npm or cargo.",
            "Debugging provider issues before confirming the binary path.",
        ],
        "links": [
            ("Install hub", "/install/index.html"),
            ("Update or upgrade", "/install/update-or-upgrade/index.html"),
            ("Config file location", "/config/file-location/index.html"),
        ],
        "examples": [
            ("Install and verify through brew only", "Keep package ownership obvious. Install, reopen the shell, then confirm the same brew-managed binary is active.", "brew install deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("Check which Homebrew prefix actually won", "On macOS, confusion often comes from `/opt/homebrew` versus `/usr/local` or another package path winning first.", "command -v deepseek || which deepseek\n# compare whether the resolved path matches your brew prefix"),
            ("Confirm brew health before you blame the app", "If brew itself is stale or unhealthy, fix that first so you do not turn package-manager drift into an app debugging session.", "brew --version\nbrew doctor\nbrew list | rg deepseek-tui || true"),
        ],
        "failure_routes": [
            ("Brew install succeeded but the command still points somewhere else", "That means Homebrew is not the active owner yet. Fix PATH order before you treat this as a DeepSeek TUI issue."),
            ("The brew binary is active but requests still fail", "That is usually not an install problem anymore. Move straight into provider setup or config checks."),
            ("`brew doctor` is already complaining before install", "Treat that as Homebrew environment debt first. A noisy brew base will make install verification unreliable."),
        ],
        "zh_title": "用 Homebrew 安装 DeepSeek TUI",
        "zh_description": "当你的 macOS 终端工具本来就大量依赖 Homebrew 时，用 brew 安装 DeepSeek TUI 会更整洁。",
        "zh_eyebrow": "Homebrew 安装",
        "zh_h1": "如果你的 macOS CLI 工具大多由 brew 管理，Homebrew 会是更整洁的 DeepSeek TUI 安装路线",
        "zh_intro": "当 Homebrew 已经是你机器上的主要包管理层时，用它安装 DeepSeek TUI 可以让更新路径和二进制归属更清晰，而不是为了一个工具额外引入别的生态。",
        "zh_answer_kicker": "最快判断",
        "zh_answer_h2": "如果你更在意 macOS CLI 工具统一归 Homebrew 管理，brew 往往比最短命令更重要。",
        "zh_answer_p": "只有在它真的是当前二进制拥有者时，brew 才最有价值；如果它和 npm、cargo 同时竞争 PATH，反而会更乱。",
        "zh_questions": [
            "什么时候 Homebrew 真能简化 macOS 上的安装故事？",
            "怎样避免 brew 和其他安装路径抢同一个二进制？",
            "哪些检查能说明当前真的走的是 brew 路线？",
        ],
        "zh_steps": [
            ("先确认 brew 自己稳定", "安装前先保证 `brew --version` 和你平时的 brew 安装流程本来就能正常工作。"),
            ("谁安装谁更新", "如果这次是 brew 安装，后面更新也尽量继续走 brew，不要半路改去 npm 或 cargo。"),
            ("核对当前二进制路径", "安装后马上查 shell 实际调用的是不是 brew 管理的二进制。"),
        ],
        "zh_checks": [
            "重开终端后验证 `deepseek --version`。",
            "检查 `/opt/homebrew` 或 `/usr/local` 顺序是不是把别的二进制挡住了。",
            "二进制路径没确认前，不要急着往 provider 和配置层排。",
        ],
        "zh_mistakes": [
            "只是觉得 brew 方便，就选它，但你机器上真正长期管理 CLI 的其实是别的路径。",
            "用 brew 更新，但实际生效的二进制还来自 npm 或 cargo。",
            "没核对路径，就先去排 provider 错误。",
        ],
        "zh_links": [
            ("安装总页", "/zh/install/index.html"),
            ("更新与升级", "/zh/install/update-or-upgrade/index.html"),
            ("配置文件位置", "/zh/config/file-location/index.html"),
        ],
        "zh_examples": [
            ("只通过 brew 安装并验证", "让包归属保持单一。安装、重开 shell，然后确认当前活跃二进制确实来自 brew。", "brew install deepseek-tui\ndeepseek --version\ncommand -v deepseek || which deepseek"),
            ("检查当前生效的是哪条 Homebrew 前缀", "在 macOS 上，很多混乱都来自 `/opt/homebrew`、`/usr/local` 或别的包路径先赢。", "command -v deepseek || which deepseek\n# 对照解析到的路径是不是你的 brew 前缀"),
            ("先确认 brew 自己健康，再怪应用", "如果 brew 本身就有问题，先修它，不要把包管理器漂移误判成 DeepSeek TUI 安装问题。", "brew --version\nbrew doctor\nbrew list | rg deepseek-tui || true"),
        ],
        "zh_failure_routes": [
            ("brew 安装成功了，但命令仍然指向别处", "这说明 Homebrew 还不是当前拥有者。先修 PATH 顺序，不要先把问题归到 DeepSeek TUI。"),
            ("当前已经是 brew 二进制，但请求还是失败", "那通常就不再是安装层问题了，直接去看 provider 设置或配置层。"),
            ("`brew doctor` 在安装前就已经报很多问题", "先把它当成 Homebrew 环境债务处理。brew 基线不干净，后面的安装验证就不可靠。"),
        ],
    },
    ("install", "windows"): {
        "title": "Install DeepSeek TUI on Windows",
        "description": "Choose the right Windows install path for DeepSeek TUI by matching PowerShell, Git Bash, WSL, or mixed terminal setups to the correct package route.",
        "eyebrow": "Windows Install",
        "h1": "Install DeepSeek TUI on Windows by matching the package path to the shell you actually use every day",
        "intro": "Windows is where install confusion grows fastest because the shell, PATH rules, and terminal habits vary much more than on macOS or Linux. The right route depends on whether your real workflow lives in PowerShell, Git Bash, WSL, Node, or Rust.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Pick the install path that already fits your active Windows shell instead of the shortest command from another ecosystem.",
        "answer_p": "If your real work happens in Node-style CLIs, npm is often the cleanest. If you live in Rust tooling, cargo may be more predictable. If you rely on WSL, make that boundary explicit.",
        "questions": [
            "Which Windows shell is the real owner of your CLI workflow?",
            "When should npm, cargo, or WSL be preferred on Windows?",
            "What proves the install succeeded beyond a single one-off shell session?",
        ],
        "steps": [
            ("Identify the true shell first", "Do not start from the install command. Start from whether your real sessions happen in PowerShell, Git Bash, or WSL."),
            ("Match the ecosystem to that shell", "Use the package path that already behaves normally there instead of forcing an unfamiliar toolchain."),
            ("Validate after reopening", "Windows path issues often appear only after a new shell session, so reopen the terminal and verify again."),
        ],
        "checks": [
            "Run `deepseek --version` in the shell you will actually use for work.",
            "Check whether PATH changes only exist in one terminal profile.",
            "If the binary exists but requests fail, move into provider setup next.",
        ],
        "mistakes": [
            "Testing in PowerShell but doing real work later in Git Bash or WSL.",
            "Installing through a package path that your main shell does not already trust.",
            "Assuming one successful run means the PATH is fixed for all terminal profiles.",
        ],
        "links": [
            ("Install hub", "/install/index.html"),
            ("npm install guide", "/install/npm/index.html"),
            ("Command not found troubleshooting", "/troubleshooting/command-not-found/index.html"),
        ],
        "examples": [
            ("Test in the shell you really use for work", "Windows setup only counts in the shell that will own your daily workflow, not just the shell where installation happened to succeed once.", "deepseek --version\nwhere deepseek"),
            ("Separate Windows shell paths before changing package ecosystems", "If PowerShell, Git Bash, and WSL disagree, compare their binary paths first before you reinstall through another toolchain.", "where deepseek\n# repeat in the exact shell profile you plan to use"),
            ("Check version and path together after restart", "On Windows, version success without path consistency is not enough. Reopen the exact terminal profile and verify both again.", "deepseek --version\nwhere deepseek\n# repeat after opening a new PowerShell, Git Bash, or WSL session"),
        ],
        "failure_routes": [
            ("PowerShell works but Git Bash or WSL does not", "Treat that as a shell-boundary or PATH-boundary issue first. Do not assume the package manager itself is broken."),
            ("The command exists but only inside the install shell", "That usually means PATH propagation or terminal-profile scope is incomplete. Reopen the target shell and inspect which path actually resolves."),
            ("The path looks right but requests still fail only in one shell", "That often means auth or env exports differ by shell profile. Move from install debugging into env and provider checks."),
        ],
        "zh_title": "在 Windows 上安装 DeepSeek TUI",
        "zh_description": "根据 PowerShell、Git Bash、WSL 或混合终端环境，为 DeepSeek TUI 选择正确的 Windows 安装路径。",
        "zh_eyebrow": "Windows 安装",
        "zh_h1": "在 Windows 上安装 DeepSeek TUI，先看你每天真正工作的 shell，再决定安装路径",
        "zh_intro": "Windows 安装最容易混乱，不是因为命令难，而是因为 shell、PATH 规则和终端习惯比 macOS、Linux 更分裂。正确路线取决于你真正工作的地方到底是 PowerShell、Git Bash、WSL、Node 还是 Rust 工具链。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "优先选择和你当前 Windows 主力 shell 匹配的安装路径，而不是照搬另一个生态里最短的命令。",
        "zh_answer_p": "如果你的 CLI 本来就偏 Node，npm 往往最顺；如果长期在 Rust 工具链里，cargo 会更稳定；如果主要靠 WSL，就要先把这个边界想清楚。",
        "zh_questions": [
            "到底哪个 Windows shell 才是你真实的 CLI 工作环境？",
            "什么时候 Windows 上该优先选 npm、cargo 或 WSL？",
            "除了某个终端里一次跑通，还要怎么确认安装真的完成了？",
        ],
        "zh_steps": [
            ("先识别真实 shell", "不要从安装命令开始想，而是先确认你真实工作到底在 PowerShell、Git Bash 还是 WSL。"),
            ("让工具生态去匹配 shell", "选择那条在该 shell 里本来就最自然的安装路径，而不是强行引入不熟的工具链。"),
            ("重开终端再验证", "Windows 的 PATH 问题常常只在新 shell 里出现，所以一定要重开后再查一次。"),
        ],
        "zh_checks": [
            "在你真正要工作的那个 shell 里跑 `deepseek --version`。",
            "确认 PATH 变化是不是只存在于某一个终端 profile。",
            "如果二进制存在但请求失败，下一步应转去 provider 设置。",
        ],
        "zh_mistakes": [
            "在 PowerShell 里测试，但真实工作都在 Git Bash 或 WSL。",
            "安装路径和主力 shell 平时完全不搭。",
            "只因为某一次运行成功，就以为所有终端 profile 都修好了。",
        ],
        "zh_links": [
            ("安装总页", "/zh/install/index.html"),
            ("npm 安装", "/zh/install/npm/index.html"),
            ("command not found 排错", "/zh/troubleshooting/command-not-found/index.html"),
        ],
        "zh_examples": [
            ("一定在你真实工作的 shell 里测试", "Windows 安装是否成功，只在你日常真正工作的 shell 里才算数，不是某个安装窗口里跑通一次就结束。", "deepseek --version\nwhere deepseek"),
            ("先把不同 Windows shell 的路径边界分开", "如果 PowerShell、Git Bash、WSL 结果不一致，先比二进制路径，不要先换包管理器。", "where deepseek\n# 在你真正要使用的 shell profile 里重复执行"),
            ("重开终端后同时看版本和路径", "在 Windows 上，只看一次版本成功不够，还要在新开的同一终端 profile 里再对照路径。", "deepseek --version\nwhere deepseek\n# 新开 PowerShell、Git Bash 或 WSL 后再重复"),
        ],
        "zh_failure_routes": [
            ("PowerShell 正常，但 Git Bash 或 WSL 不正常", "先把它当成 shell 边界或 PATH 边界问题，不要立刻判断包管理器坏了。"),
            ("命令只在安装那个 shell 里存在", "通常是 PATH 传播或 terminal profile 范围没打通。重开目标 shell，再查当前实际解析的路径。"),
            ("路径看起来对，但只有某个 shell 请求失败", "这往往不是安装层，而是不同 shell 的认证或环境变量导出不一致。下一步去看 env 和 provider。"),
        ],
    },
    ("install", "update-or-upgrade"): {
        "title": "How to Update or Upgrade DeepSeek TUI",
        "description": "Update or upgrade DeepSeek TUI safely by using the same package path that owns the active binary in your shell.",
        "eyebrow": "Update and Upgrade",
        "h1": "Updating DeepSeek TUI is simple only after you confirm which package path actually owns the live binary",
        "intro": "Most upgrade confusion comes from duplicate installs or forgotten PATH history. The right update command is not universal; it depends on the package ecosystem that currently owns the `deepseek` command your shell resolves first.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Update DeepSeek TUI through the same package route that currently owns the active binary in your shell.",
        "answer_p": "If you installed with npm, update with npm. If you installed with cargo or Homebrew, stay there unless you are intentionally migrating and cleaning up the old path.",
        "questions": [
            "How do you identify which package path currently owns the binary?",
            "When is an upgrade issue actually a duplicate-install issue?",
            "What should you verify immediately after upgrading?",
        ],
        "steps": [
            ("Find the active owner", "Before running any upgrade command, determine whether npm, cargo, Homebrew, or a manual binary is the actual owner of the current command."),
            ("Upgrade through one path only", "Run the update in that ecosystem first instead of shotgun-updating several package managers."),
            ("Re-verify the shell after restart", "Open a new shell and confirm the version again so you do not mistake cache or PATH order for a successful upgrade."),
        ],
        "checks": [
            "Confirm `deepseek --version` changed in a fresh shell.",
            "Check whether an older install path is still earlier in PATH.",
            "If behavior changed unexpectedly, verify config compatibility next rather than reinstalling blindly.",
        ],
        "mistakes": [
            "Updating through npm when the binary in use actually comes from cargo or brew.",
            "Running multiple upgrade commands and losing track of which one won PATH precedence.",
            "Assuming upgrade problems are package-manager issues when the real break is config drift.",
        ],
        "links": [
            ("Install hub", "/install/index.html"),
            ("Config reset", "/config/reset/index.html"),
            ("Release binaries troubleshooting", "/troubleshooting/release-binaries/index.html"),
        ],
        "examples": [
            ("Upgrade the same owner you installed with", "Do not shotgun-update every package manager. First work out which route actually owns the live binary.", "deepseek --version\ncommand -v deepseek || which deepseek\n# then update through the matching package route"),
            ("Verify after a fresh shell", "An upgrade only counts once a new terminal session resolves the same binary at the newer version.", "deepseek --version"),
        ],
        "failure_routes": [
            ("You upgraded but the version did not change", "That usually means you updated the wrong package owner or an older binary still resolves earlier in PATH."),
            ("The version changed but behavior got strange", "This is often config drift or provider mismatch after upgrade, not a broken package manager. Check config compatibility next."),
        ],
        "zh_title": "更新或升级 DeepSeek TUI",
        "zh_description": "通过当前真正拥有活跃二进制的包路径，安全地更新或升级 DeepSeek TUI。",
        "zh_eyebrow": "更新与升级",
        "zh_h1": "只有先搞清楚当前活跃二进制到底归谁管，更新 DeepSeek TUI 才会简单",
        "zh_intro": "大多数升级混乱都来自重复安装和遗留 PATH。正确的升级命令不是放之四海而皆准的，它取决于现在 shell 第一个解析到的 `deepseek` 命令到底来自哪条包管理路径。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "始终通过当前真正拥有活跃二进制的那条安装路径来更新 DeepSeek TUI。",
        "zh_answer_p": "如果最初是 npm 安装，就先继续用 npm；如果是 cargo 或 Homebrew，也优先留在原生态，除非你明确在迁移并清理旧路径。",
        "zh_questions": [
            "怎么判断当前到底是哪条包路径在拥有这个二进制？",
            "什么时候升级问题其实是重复安装问题？",
            "升级完成后第一时间该核对什么？",
        ],
        "zh_steps": [
            ("先找出当前拥有者", "任何升级命令之前，先确认现在的 `deepseek` 到底来自 npm、cargo、Homebrew 还是手动二进制。"),
            ("一次只走一条更新路径", "先在当前拥有者生态里更新，不要几个包管理器一起乱跑。"),
            ("重开 shell 再核对", "升级后重开终端，再查一次版本，避免把缓存或 PATH 顺序误判成升级成功。"),
        ],
        "zh_checks": [
            "在新 shell 中确认 `deepseek --version` 已经变化。",
            "检查旧安装路径是不是仍然排在 PATH 前面。",
            "如果升级后行为异常，下一步先看配置兼容，而不是盲目重装。",
        ],
        "zh_mistakes": [
            "当前生效的是 cargo 或 brew，却跑了 npm 更新。",
            "几个升级命令一起跑，最后自己都不清楚 PATH 是谁赢了。",
            "把升级问题都归因于包管理器，而真正坏掉的是配置漂移。",
        ],
        "zh_links": [
            ("安装总页", "/zh/install/index.html"),
            ("配置重置", "/zh/config/reset/index.html"),
            ("Release binaries 排错", "/zh/troubleshooting/release-binaries/index.html"),
        ],
        "zh_examples": [
            ("谁安装谁更新", "不要几个包管理器一起跑更新。先确认当前活跃二进制到底归谁管。", "deepseek --version\ncommand -v deepseek || which deepseek\n# 再走对应的那条更新路径"),
            ("重开 shell 以后再核对", "只有在新终端里解析到的还是同一个二进制、而且版本已经变了，这次升级才算真的完成。", "deepseek --version"),
        ],
        "zh_failure_routes": [
            ("你更新了，但版本号没变", "通常说明你更新的是错误的拥有者，或者旧二进制还排在 PATH 前面。"),
            ("版本号变了，但行为变怪了", "这往往不是包管理器坏了，而是升级后配置或 provider 预期漂移。下一步去看配置兼容。"),
        ],
    },
    ("config", "api-key"): {
        "title": "Set Up the DeepSeek TUI API Key",
        "description": "Configure the DeepSeek TUI API key correctly and separate provider auth problems from unrelated install or UI issues.",
        "eyebrow": "API Key Setup",
        "h1": "API key setup is where many DeepSeek TUI sessions succeed or fail before any mode or tool detail even matters",
        "intro": "Once the binary works, the next hard boundary is provider authentication. API key mistakes often look like install or runtime issues, but they belong to a narrower layer: whether the right credential is present in the right place for the provider you actually chose.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Treat API key setup as a provider-auth problem, not as a generic install problem.",
        "answer_p": "If the command runs but requests fail, the next question is almost always whether the credential is missing, misplaced, or tied to the wrong provider path.",
        "questions": [
            "Where should the API key live: file, environment variable, or provider block?",
            "How do you tell a missing key apart from a wrong provider selection?",
            "Which checks prove auth is the real failure layer?",
        ],
        "steps": [
            ("Confirm the provider first", "Before touching a key, verify which provider path your current config actually expects."),
            ("Place one source of truth", "Use one clear credential source first so you can test without wondering whether file and environment values disagree."),
            ("Run a minimal live request", "Validate with the simplest request path you can, before layering modes, MCP, or other advanced behavior on top."),
        ],
        "checks": [
            "Confirm the key belongs to the provider configured in DeepSeek TUI.",
            "Check for typos, empty values, and shell profile drift.",
            "If auth works but behavior is odd, move into provider setup or config file checks next.",
        ],
        "mistakes": [
            "Setting a key for one provider while the config points at another.",
            "Leaving multiple shells with different exported credentials.",
            "Assuming an auth error means the binary install is broken.",
        ],
        "links": [
            ("Provider setup", "/config/provider-setup/index.html"),
            ("Environment variables", "/config/environment-variables/index.html"),
            ("Provider troubleshooting", "/troubleshooting/provider-troubleshooting/index.html"),
        ],
        "examples": [
            ("Environment-first auth check", "Keep the first pass simple: one credential source, one shell, one live request path.", "export DEEPSEEK_API_KEY=\"your-key-here\"\ndeepseek"),
            ("Before you blame the key", "Confirm the shell really sees the value you think it sees before editing more config.", "echo \"$DEEPSEEK_API_KEY\"\ndeepseek --version"),
        ],
        "failure_routes": [
            ("The app opens but the first request fails", "That usually means the credential is missing, empty, or tied to the wrong provider path. Check provider setup before touching modes or MCP."),
            ("It works in one shell but fails in another", "You probably have shell-specific exports or stale profile values. Compare environment variables before changing the key again."),
        ],
        "zh_title": "设置 DeepSeek TUI 的 API Key",
        "zh_description": "正确配置 DeepSeek TUI 的 API Key，并把 provider 认证问题和安装、界面问题分开。",
        "zh_eyebrow": "API Key 设置",
        "zh_h1": "在模式、工具和高级功能之前，API Key 设置往往就是决定 DeepSeek TUI 能不能跑通的第一道关",
        "zh_intro": "二进制能启动以后，真正的下一道硬边界通常就是 provider 认证。很多 API Key 错误表面像安装或运行时问题，实际上只是凭据位置、提供方选择或变量来源不一致。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "把 API Key 问题当成 provider 认证问题来看，而不是笼统的安装问题。",
        "zh_answer_p": "如果命令能跑但请求失败，下一步大概率不是重装，而是确认凭据是否缺失、放错位置，或者跟当前 provider 路线不匹配。",
        "zh_questions": [
            "API Key 应该放在配置文件、环境变量还是 provider 配置块里？",
            "怎样区分“没填 key”和“provider 选错了”？",
            "哪些检查能证明失败层真的在认证，而不是别的地方？",
        ],
        "zh_steps": [
            ("先确认 provider", "动 key 之前先确认当前配置真正期待的是哪个 provider 路线。"),
            ("先保留一个可信来源", "优先让凭据只来自一个清晰来源，避免文件和环境变量互相打架。"),
            ("用最小请求路径验证", "先用最简单的请求去验证，再叠加模式、MCP 或其他高级行为。"),
        ],
        "zh_checks": [
            "确认当前 key 确实属于你在 DeepSeek TUI 里配置的那个 provider。",
            "检查拼写、空值和 shell profile 漂移。",
            "如果认证已经成功但行为仍异常，再转去 provider 设置或配置文件排查。",
        ],
        "zh_mistakes": [
            "给 A provider 配了 key，但当前 config 指向的却是 B provider。",
            "不同 shell 里残留了不同的导出凭据。",
            "把认证错误误判成二进制安装坏了。",
        ],
        "zh_links": [
            ("provider 设置", "/zh/config/provider-setup/index.html"),
            ("环境变量", "/zh/config/environment-variables/index.html"),
            ("provider 排错", "/zh/troubleshooting/provider-troubleshooting/index.html"),
        ],
        "zh_examples": [
            ("先走环境变量认证验证", "第一轮先只保留一个清楚的凭据来源，这样最容易判断失败是不是卡在认证层。", "export DEEPSEEK_API_KEY=\"your-key-here\"\ndeepseek"),
            ("先别急着怪 key", "动更多配置文件之前，先确认当前 shell 里真的有你以为的那个值。", "echo \"$DEEPSEEK_API_KEY\"\ndeepseek --version"),
        ],
        "zh_failure_routes": [
            ("程序能打开，但第一条请求失败", "通常不是安装坏了，而是凭据缺失、空值，或者 provider 路线不匹配。先去核对 provider 设置。"),
            ("一个 shell 里能用，另一个 shell 里失败", "大概率是不同 shell 的导出值不一致，或者旧 profile 还在生效。先比环境变量。"),
        ],
    },
    ("config", "environment-variables"): {
        "title": "DeepSeek TUI Environment Variables",
        "description": "Use environment variables with DeepSeek TUI without losing track of which shell value is overriding your intended config.",
        "eyebrow": "Environment Variables",
        "h1": "Environment variables help DeepSeek TUI only when you know exactly which shell values are winning",
        "intro": "Environment variables are convenient because they are fast to change, but that convenience turns into confusion when different shells, profiles, or project scripts quietly override what you thought the app would use.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Use environment variables as an explicit override layer, not as a mystery layer you forget is active.",
        "answer_p": "If behavior changes between terminals, environment variables are one of the first places to inspect.",
        "questions": [
            "Which values belong in environment variables instead of checked-in config files?",
            "How do you see whether the shell is overriding file-based config?",
            "When should you stop using environment variables and move values into a more stable config path?",
        ],
        "steps": [
            ("Decide what should stay secret or local", "Use environment variables for values that should remain machine-local or session-local, not for everything by default."),
            ("Track where they are set", "Know whether the variable comes from shell profile files, direnv-like tooling, CI, or a temporary export."),
            ("Test across shell boundaries", "If one terminal works and another does not, compare active environment state before rewriting config files."),
        ],
        "checks": [
            "List the relevant environment variables in the shell you actually use.",
            "Compare behavior with and without those exports active.",
            "If the same issue survives after clearing env overrides, return to the config file path.",
        ],
        "mistakes": [
            "Treating environment values as if they were self-documenting.",
            "Forgetting that different terminal profiles can export different values.",
            "Using env overrides permanently when a stable config file would be easier to reason about.",
        ],
        "links": [
            ("API key setup", "/config/api-key/index.html"),
            ("Config file location", "/config/file-location/index.html"),
            ("Config reset", "/config/reset/index.html"),
        ],
        "examples": [
            ("Check what the current shell really exports", "List the relevant values before you edit config files, especially if different terminals behave differently.", "echo \"$DEEPSEEK_API_KEY\"\n# inspect any provider-related exports in the current shell"),
            ("Compare with and without overrides", "The fastest way to prove the env layer is involved is to compare behavior before and after clearing the relevant export.", "unset DEEPSEEK_API_KEY\n# reopen the shell or retry the narrowest request path"),
        ],
        "failure_routes": [
            ("One terminal works and another does not", "That is usually a shell-profile difference, not a provider outage. Compare exports across the two shells before rewriting config."),
            ("You changed the config file but nothing moved", "An environment override may still be winning. Clear or inspect env values before assuming the file path is wrong."),
        ],
        "zh_title": "DeepSeek TUI 的环境变量怎么用",
        "zh_description": "在 DeepSeek TUI 中使用环境变量，同时搞清楚到底是哪一个 shell 值覆盖了你的配置。",
        "zh_eyebrow": "环境变量",
        "zh_h1": "环境变量只有在你清楚当前是哪一组 shell 值在生效时，才会真正帮助 DeepSeek TUI",
        "zh_intro": "环境变量改起来很快，但一旦多个 shell、profile 或项目脚本同时存在，它们也最容易把你原本以为会生效的配置静默覆盖掉。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "把环境变量当成显式覆盖层，而不是忘了自己开着的神秘层。",
        "zh_answer_p": "如果两个终端里行为不一样，环境变量几乎总该先查。",
        "zh_questions": [
            "哪些值更适合放环境变量，而不是写进配置文件？",
            "怎么判断 shell 是不是在覆盖文件配置？",
            "什么时候该停止依赖环境变量，转成更稳定的配置路径？",
        ],
        "zh_steps": [
            ("先决定哪些值应该本地化", "环境变量更适合机器本地或会话级的敏感值，不适合默认承载一切配置。"),
            ("记清它们从哪来", "知道变量到底来自 shell profile、direnv 类工具、CI，还是一次性的 export。"),
            ("跨 shell 比较", "如果一个终端正常、另一个不正常，先对比环境变量状态，再决定要不要改配置文件。"),
        ],
        "zh_checks": [
            "在真正工作的 shell 里列出相关环境变量。",
            "比较变量存在和移除之后的行为差异。",
            "如果清掉 env 覆盖后问题还在，再回到配置文件路径排查。",
        ],
        "zh_mistakes": [
            "把环境变量当成默认就自解释的东西。",
            "忘了不同终端 profile 可能导出不同值。",
            "长期用环境变量顶着，明明写进稳定配置文件会更好理解。",
        ],
        "zh_links": [
            ("API Key 设置", "/zh/config/api-key/index.html"),
            ("配置文件位置", "/zh/config/file-location/index.html"),
            ("配置重置", "/zh/config/reset/index.html"),
        ],
        "zh_examples": [
            ("先看当前 shell 到底导出了什么", "尤其当不同终端行为不一致时，先把相关值列出来，再动配置文件。", "echo \"$DEEPSEEK_API_KEY\"\n# 再检查当前 shell 里的 provider 相关导出"),
            ("做一次有无覆盖的对照", "想快速证明 env 层是不是在作怪，最直接的方法就是清掉相关导出后再比一次。", "unset DEEPSEEK_API_KEY\n# 重开 shell 或重试最窄请求路径"),
        ],
        "zh_failure_routes": [
            ("一个终端正常，另一个终端不正常", "这通常不是 provider 掉了，而是 shell profile 差异。先对比两个 shell 的导出值。"),
            ("你改了配置文件，但行为完全没动", "很可能环境变量覆盖还在赢。先把 env 值查清楚，再判断是不是文件路径问题。"),
        ],
    },
    ("config", "file-location"): {
        "title": "Where the DeepSeek TUI Config File Lives",
        "description": "Find the DeepSeek TUI config file, understand which file is active, and stop editing the wrong path.",
        "eyebrow": "Config File Location",
        "h1": "Most config file confusion comes from editing the wrong DeepSeek TUI path, not from the syntax itself",
        "intro": "A config file can be perfectly valid and still feel broken if the app is reading a different path than the one you edited. The first job here is not tweaking values; it is confirming which file is truly active.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Before changing any values, confirm that the file you are editing is the one the running DeepSeek TUI session actually reads.",
        "answer_p": "Many config problems disappear once you stop editing an inactive path or a stale copy from another setup route.",
        "questions": [
            "Where does DeepSeek TUI expect its config file by default?",
            "How do local overrides, copied files, and alternate setup routes create confusion?",
            "What should you do once you know which file is live?",
        ],
        "steps": [
            ("Find the active path", "Do not assume the file location. Confirm which path the current install and shell actually use."),
            ("Check for duplicate copies", "Look for old config files from earlier experiments, previous providers, or a different install route."),
            ("Only then edit values", "Once the active file is confirmed, change one thing at a time and validate it immediately."),
        ],
        "checks": [
            "Verify the file path matches the install route and user account you are actually using.",
            "Compare the active file against any older backups or copied examples.",
            "If edits change nothing, re-check environment variable overrides next.",
        ],
        "mistakes": [
            "Editing a sample file or backup file instead of the active config.",
            "Keeping multiple copies and forgetting which one belongs to the active shell.",
            "Changing many values before confirming the correct file path.",
        ],
        "links": [
            ("Environment variables", "/config/environment-variables/index.html"),
            ("Config reset", "/config/reset/index.html"),
            ("Provider setup", "/config/provider-setup/index.html"),
        ],
        "examples": [
            ("Locate the file before you edit values", "The safest first move is to prove which config file exists and which path you are about to change.", "find ~ -name '*deepseek*' 2>/dev/null | head\n# compare candidates before editing anything"),
            ("Change one value, then validate immediately", "Once the active file is confirmed, edit the smallest possible value and test that one change before touching the rest.", "# edit the confirmed active file\n# then run the narrowest possible DeepSeek TUI check"),
            ("Archive old copies once the active file is known", "You do not need several live-looking copies once the true path is confirmed. Archive the extras so the next edit does not start from confusion.", "# keep one active config path\n# move old examples or backups into a clearly named archive folder"),
        ],
        "failure_routes": [
            ("You edited the file but behavior never moved", "That usually means you changed an inactive copy or an environment override is still winning. Re-check the active path first."),
            ("You found several config files and do not know which one matters", "Stop editing all of them. Narrow the live path first, then keep one source of truth and archive the rest."),
            ("The active file is correct but the values still seem ignored", "That usually means another layer is winning, most often env overrides or provider defaults. Leave file-location debugging and check those layers next."),
        ],
        "zh_title": "DeepSeek TUI 配置文件位置",
        "zh_description": "找到 DeepSeek TUI 的配置文件，确认当前活跃文件路径，并停止编辑错误的那份文件。",
        "zh_eyebrow": "配置文件位置",
        "zh_h1": "很多配置混乱并不是语法错了，而是你编辑的根本不是 DeepSeek TUI 当前正在读取的那份文件",
        "zh_intro": "配置文件哪怕完全合法，如果程序读的不是你改的那份，它看起来也会像坏的一样。这里最先要做的不是调值，而是确认活跃路径。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "改任何值之前，先确认当前运行中的 DeepSeek TUI 真正读取的是哪一个配置文件。",
        "zh_answer_p": "很多配置问题在你停止编辑无效路径或旧副本之后，自己就消失了。",
        "zh_questions": [
            "DeepSeek TUI 默认会从哪里找配置文件？",
            "本地覆盖、复制文件和不同安装路径会怎样造成混乱？",
            "一旦确认了活跃文件，接下来该怎么改？",
        ],
        "zh_steps": [
            ("先确认活跃路径", "不要靠猜。先确认当前安装路径和 shell 真正使用的是哪一个文件。"),
            ("检查有没有重复副本", "找找之前实验留下来的旧配置、旧 provider 路线或不同安装路径产生的副本。"),
            ("确认后再改值", "只有在活跃文件确定之后，才开始一项一项改并立即验证。"),
        ],
        "zh_checks": [
            "核对文件路径和当前用户、安装路径是否匹配。",
            "把活跃文件和任何旧备份、示例文件做对比。",
            "如果改动没有任何效果，下一步先回头查环境变量覆盖。",
        ],
        "zh_mistakes": [
            "编辑的是示例文件或备份文件，而不是活跃配置。",
            "机器上留了多份文件，却忘了当前 shell 实际用哪份。",
            "在没确认路径前，一次改太多值。",
        ],
        "zh_links": [
            ("环境变量", "/zh/config/environment-variables/index.html"),
            ("配置重置", "/zh/config/reset/index.html"),
            ("provider 设置", "/zh/config/provider-setup/index.html"),
        ],
        "zh_examples": [
            ("先找文件，再改值", "最稳的第一步不是调参数，而是先证明机器上到底有哪些配置文件候选，以及你准备改的是哪一份。", "find ~ -name '*deepseek*' 2>/dev/null | head\n# 改任何值前先对照候选路径"),
            ("一次只改一个值，并立刻验证", "活跃文件确认后，每次只动最小的一项，再立刻验证这一次改动有没有生效。", "# 只编辑确认过的活跃文件\n# 然后跑一次最窄的 DeepSeek TUI 检查"),
            ("活跃文件确认后，把旧副本归档", "一旦知道哪份是真的在用，就把其他像活跃文件的旧副本收起来，不要让下一次修改又从混乱开始。", "# 只保留一份活跃配置路径\n# 旧示例或备份移动到命名清楚的归档目录"),
        ],
        "zh_failure_routes": [
            ("你改了文件，但行为完全没动", "这通常说明你改的是无效副本，或者环境变量覆盖还在赢。先重新确认活跃路径。"),
            ("你找到了好几份配置文件，不知道哪份才算数", "先停下来，不要每份都改。先缩窄出活跃路径，再保留一份真相来源，其余归档。"),
            ("活跃文件确认没错，但值看起来还是没被用到", "那通常就不是文件定位层了，而是 env 覆盖或 provider 默认值还在赢。下一步去查那些层。"),
        ],
    },
    ("config", "provider-cost"): {
        "title": "DeepSeek TUI Provider Cost",
        "description": "Understand DeepSeek TUI provider cost by separating tool usage habits from the billing model of the model provider you connect.",
        "eyebrow": "Provider Cost",
        "h1": "DeepSeek TUI cost questions usually make sense only after you map them back to the provider and the workflow",
        "intro": "People search for the tool name, but the bill usually comes from the provider and the way you use the agent. Cost changes when your provider changes, when your mode changes, and when your workflow causes longer or broader sessions.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "The practical cost question is usually not the app itself; it is which provider you connect and how your workflow drives that provider’s usage.",
        "answer_p": "That is why cost belongs next to provider setup, mode choice, and session habits, not in a vague pricing page by itself.",
        "questions": [
            "Which cost questions belong to the provider instead of the app?",
            "How do mode choice and session style affect usage patterns?",
            "What should you compare before changing providers for cost reasons?",
        ],
        "steps": [
            ("Identify the billing layer", "Confirm which provider is actually charging for the requests behind your current workflow."),
            ("Look at usage behavior", "Longer sessions, more retries, or wider tool usage can change cost even if the app itself did not change."),
            ("Compare providers with the same workflow in mind", "A provider swap only helps if you compare the same task style, not two different usage patterns."),
        ],
        "checks": [
            "Map your current mode and task style to the provider’s billing model.",
            "Check whether a config or mode change would reduce usage before changing providers.",
            "Keep provider setup docs nearby so cost and auth do not drift apart in your mental model.",
        ],
        "mistakes": [
            "Asking a generic cost question without identifying the active provider.",
            "Comparing providers while also changing workflow style at the same time.",
            "Assuming the fastest mode and the cheapest usage pattern are always the same thing.",
        ],
        "links": [
            ("Provider setup", "/config/provider-setup/index.html"),
            ("Plan vs yolo", "/modes/plan-vs-yolo/index.html"),
            ("Pricing and cost guide", "/guides/pricing-and-cost/index.html"),
        ],
        "examples": [
            ("Compare cost under the same workflow shape", "If you want a useful comparison, keep the task shape stable while you compare provider choice or mode choice.", "# run the same style of task\n# compare provider and mode decisions, not two unrelated workflows"),
            ("Reduce waste before changing providers", "Sometimes the cheaper move is narrowing the session or mode scope before you migrate the backend.", "# compare plan-style and broader yolo-style usage on the same task"),
        ],
        "failure_routes": [
            ("You changed providers and cost still feels wrong", "That may be a workflow-width problem, not a provider problem. Look at mode choice and session sprawl next."),
            ("You cannot explain which provider is billing this session", "Stop cost comparisons until provider ownership is explicit. A vague billing layer makes every pricing guess weak."),
        ],
        "zh_title": "DeepSeek TUI 的 Provider 成本",
        "zh_description": "理解 DeepSeek TUI 的 provider 成本问题，并把工具使用习惯和模型提供方计费模型分开看。",
        "zh_eyebrow": "Provider 成本",
        "zh_h1": "只有把成本问题重新映射回 provider 和工作流，DeepSeek TUI 的价格问题才说得清",
        "zh_intro": "用户搜索的是工具名，但账单通常来自 provider，以及你怎么使用代理。provider 变了、模式变了、会话长度和工具宽度变了，成本判断也会跟着变。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "真正的成本问题通常不在 app 本身，而在你接了哪个 provider、以及你的工作流怎样驱动它的使用量。",
        "zh_answer_p": "所以成本应当和 provider 设置、模式选择、会话习惯放在一起看，而不是孤立成一个模糊的 pricing 页面。",
        "zh_questions": [
            "哪些成本问题属于 provider，而不是属于 app？",
            "模式选择和会话方式会怎样改变使用量？",
            "如果要因为成本换 provider，换之前该比什么？",
        ],
        "zh_steps": [
            ("先识别计费层", "先确认当前工作流背后真正计费的是哪个 provider。"),
            ("再看使用行为", "会话更长、重试更多、工具使用更广，哪怕 app 没变，成本也可能变化。"),
            ("同一种工作流下再比较 provider", "只有在任务风格一致时，对比 provider 成本才有意义。"),
        ],
        "zh_checks": [
            "把当前模式和任务风格映射到 provider 的计费模型上。",
            "先判断是不是配置或模式变化就能减少使用量，而不是立刻换 provider。",
            "把 provider 设置文档放在旁边，避免成本理解和认证设置脱节。",
        ],
        "zh_mistakes": [
            "问成本却不先指出当前接的是哪个 provider。",
            "一边换 provider，一边还改变任务风格，最后对比失真。",
            "以为最快的模式一定也最省钱。",
        ],
        "zh_links": [
            ("provider 设置", "/zh/config/provider-setup/index.html"),
            ("plan vs yolo", "/zh/modes/plan-vs-yolo/index.html"),
            ("pricing / cost 指南", "/zh/guides/pricing-and-cost/index.html"),
        ],
        "zh_examples": [
            ("在同一种工作流形状下比较成本", "想做出有意义的成本对比，前提是任务风格不变，只比较 provider 或 mode 变化。", "# 用同一种任务类型做对照\n# 比 provider 和模式，不要比两种完全不同的工作流"),
            ("先减少浪费，再考虑换 provider", "很多时候更省钱的动作不是立刻迁移后端，而是先把会话范围和模式宽度缩窄。", "# 在同一任务上对比 plan 风格和更宽的 yolo 风格"),
        ],
        "zh_failure_routes": [
            ("换了 provider，但成本感觉还是不对", "那可能不是 provider 问题，而是工作流宽度问题。下一步先看模式选择和会话扩张。"),
            ("你说不清这次会话到底是谁在计费", "在 provider 归属没说清前，先不要做成本结论。计费层模糊，所有价格判断都会失真。"),
        ],
    },
    ("config", "provider-setup"): {
        "title": "DeepSeek TUI Provider Setup",
        "description": "Set up the right provider for DeepSeek TUI, align auth with the selected backend, and avoid cross-provider config confusion.",
        "eyebrow": "Provider Setup",
        "h1": "Provider setup is where DeepSeek TUI stops being a binary on disk and starts becoming a real working agent",
        "intro": "Once installation is complete, provider setup becomes the real activation step. The important part is not only entering credentials, but making sure the selected backend, auth values, and expected models all belong to the same path.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Treat provider setup as one aligned path: selected backend, credential source, model expectations, and config location should all agree.",
        "answer_p": "Most provider setup failures come from mixing assumptions across providers or leaving an older setup path half-active.",
        "questions": [
            "Which provider path is actually active in the current config?",
            "How do auth, model defaults, and runtime expectations have to line up?",
            "Which failures should send you back to API key, env vars, or config file location?",
        ],
        "steps": [
            ("Choose the provider explicitly", "Do not let the provider remain an implicit assumption. Name the active backend first."),
            ("Align auth and config in one place", "Make sure the credential source and provider block describe the same backend instead of mixing two routes."),
            ("Validate with a minimal live request", "Test the smallest successful provider call before you tune models, modes, or MCP."),
        ],
        "checks": [
            "Confirm the provider named in config matches the key or token you supplied.",
            "Check whether stale env vars are silently overriding the intended provider block.",
            "If auth is valid but behavior still looks wrong, inspect model defaults and mode assumptions next.",
        ],
        "mistakes": [
            "Keeping one provider in config and another in environment variables.",
            "Testing with advanced workflows before the simplest provider call is stable.",
            "Changing several provider-related defaults at once and losing a clean baseline.",
        ],
        "links": [
            ("API key setup", "/config/api-key/index.html"),
            ("Environment variables", "/config/environment-variables/index.html"),
            ("Provider troubleshooting", "/troubleshooting/provider-troubleshooting/index.html"),
        ],
        "examples": [
            ("Provider-first setup order", "Do not configure auth, model defaults, and advanced features all at once. Lock the provider path first, then verify one minimal request.", "deepseek --version\n# then start one minimal session after auth is set"),
            ("One-source-of-truth pass", "Keep provider choice, auth source, and model assumptions aligned in one pass before you add MCP or more advanced runtime behavior.", "export DEEPSEEK_API_KEY=\"your-key-here\"\n# keep env and config pointing at the same provider"),
            ("Verify the credential layer before tuning models", "A working provider path is worth more than any model tweak. First prove the key and provider route agree, then change model defaults later.", "echo \"$DEEPSEEK_API_KEY\"\n# confirm the intended provider block\n# run one minimal request before touching model defaults"),
        ],
        "failure_routes": [
            ("Provider is selected but auth still fails", "That usually means the provider name and credential source disagree. Check API key setup and env overrides before changing models."),
            ("Auth works but responses feel wrong", "This is often a model-default or mode-assumption problem, not a credential problem. Move into config and mode pages next."),
            ("You are changing provider, env vars, and model defaults in one pass", "Stop and split the work. Lock the provider and auth layer first, or you will not know which change fixed or broke the session."),
        ],
        "zh_title": "DeepSeek TUI 的 Provider 设置",
        "zh_description": "为 DeepSeek TUI 设置正确的 provider，让认证、后端选择和配置路径真正对齐。",
        "zh_eyebrow": "Provider 设置",
        "zh_h1": "provider 设置是 DeepSeek TUI 从“磁盘上的命令”变成“真正可工作的代理”的关键一步",
        "zh_intro": "安装完成以后，provider 设置才是真正的激活步骤。重点不只是填凭据，而是让选中的后端、认证值、模型预期和配置路径都属于同一条路线。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "把 provider 设置看成一条完整链路：后端选择、凭据来源、模型预期和配置位置都必须一致。",
        "zh_answer_p": "大多数 provider 设置失败都来自不同 provider 路线被混在一起，或者旧配置仍然半激活。",
        "zh_questions": [
            "当前配置里，到底是哪条 provider 路线处于激活状态？",
            "认证、模型默认值和运行时预期怎样才算真正对齐？",
            "哪些失败应该把你送回 API Key、环境变量或配置文件位置页？",
        ],
        "zh_steps": [
            ("显式选定 provider", "不要让 provider 保持隐式假设，第一步就明确当前后端是谁。"),
            ("让认证和配置来源保持一条线", "确保凭据来源和 provider 配置块描述的是同一个后端，而不是两条路线混杂。"),
            ("用最小请求先验证", "先把最简单的一次 provider 请求跑通，再去调模型、模式和 MCP。"),
        ],
        "zh_checks": [
            "确认配置里写的 provider 和你提供的 key/token 属于同一路后端。",
            "检查是不是旧环境变量在静默覆盖你想用的 provider 配置块。",
            "如果认证是通的但行为仍然不对，下一步再查模型默认值和模式假设。",
        ],
        "zh_mistakes": [
            "配置文件里是一个 provider，环境变量里又留着另一个 provider。",
            "最简单请求还没稳定，就先上复杂工作流。",
            "一次性改太多 provider 相关默认值，失去干净基线。",
        ],
        "zh_links": [
            ("API Key 设置", "/zh/config/api-key/index.html"),
            ("环境变量", "/zh/config/environment-variables/index.html"),
            ("provider 排错", "/zh/troubleshooting/provider-troubleshooting/index.html"),
        ],
        "zh_examples": [
            ("先锁 provider，再测最小请求", "不要一上来同时配认证、模型默认值和高级功能。先把 provider 路线锁定，再验证最小请求。", "deepseek --version\n# 在认证完成后再开最小会话验证"),
            ("先只保留一套真相来源", "让 provider 选择、凭据来源和模型预期先在一轮里对齐，再去加 MCP 或更多运行时行为。", "export DEEPSEEK_API_KEY=\"your-key-here\"\n# 保证环境变量和配置文件指向同一 provider"),
            ("先证明认证层是通的，再去调模型", "真正值钱的是先让 provider 路线跑通，而不是一开始就改模型默认值。", "echo \"$DEEPSEEK_API_KEY\"\n# 确认当前 provider 配置块\n# 先跑一次最小请求，再动模型默认值"),
        ],
        "zh_failure_routes": [
            ("Provider 选对了，但认证还是失败", "通常是 provider 名字和凭据来源没对齐。先查 API Key 设置和环境变量覆盖。"),
            ("认证已经通过，但返回行为不对", "这更像模型默认值或模式预期的问题，不再是凭据问题。下一步去看 config 和 modes。"),
            ("你同时在改 provider、环境变量和模型默认值", "先停下来拆层。先把 provider 和认证层锁定，否则你根本不知道是哪一项让会话变好或变坏。"),
        ],
    },
    ("config", "reset"): {
        "title": "How to Reset DeepSeek TUI Config",
        "description": "Reset DeepSeek TUI config cleanly when the active settings state has become too mixed to debug efficiently.",
        "eyebrow": "Config Reset",
        "h1": "Reset DeepSeek TUI config when the current settings state is harder to reason about than rebuilding it",
        "intro": "A reset is not a failure. It is often the fastest way back to a known-good baseline when provider values, environment overrides, and copied config changes have become too tangled to inspect with confidence.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Reset config when you no longer trust which layer is driving the current behavior.",
        "answer_p": "If you cannot clearly explain whether the active behavior comes from the config file, an environment variable, or a stale provider block, a reset is usually justified.",
        "questions": [
            "When is reset more efficient than continued patching?",
            "What should you preserve before clearing the current config state?",
            "How do you rebuild from a clean baseline without repeating the same confusion?",
        ],
        "steps": [
            ("Record what still matters", "Before resetting, keep a short list of credentials, provider choices, or defaults you know you still need later."),
            ("Remove ambiguity first", "Back up or clear the config while also checking env overrides, so you do not reset one layer and leave another stale layer active."),
            ("Rebuild in a narrow order", "Bring the setup back in this order: install confidence, provider auth, config path, then workflow tuning."),
        ],
        "checks": [
            "Keep a backup of the current file before rewriting it.",
            "Remove or inspect environment variable overrides at the same time.",
            "After reset, validate one layer at a time instead of restoring every old tweak immediately.",
        ],
        "mistakes": [
            "Resetting the file while leaving old shell exports active.",
            "Restoring all previous tweaks at once and recreating the old confusion.",
            "Using reset as a substitute for finding the active config file path.",
        ],
        "links": [
            ("Config file location", "/config/file-location/index.html"),
            ("Environment variables", "/config/environment-variables/index.html"),
            ("Provider setup", "/config/provider-setup/index.html"),
        ],
        "examples": [
            ("Back up before you wipe ambiguity", "A reset is cleaner when you preserve the old state once, then rebuild from a narrower baseline instead of half-resetting repeatedly.", "cp path/to/current-config path/to/current-config.backup\n# then clear or replace the active file on purpose"),
            ("Reset one layer and test one layer", "After reset, validate install, then provider auth, then config values. Do not restore every old tweak immediately.", "# reopen shell\n# verify deepseek --version\n# then re-add only the minimum provider settings"),
            ("Write down the minimum rebuild order first", "A reset works better when you already know the shortest order for rebuilding: binary, auth, active config, then workflow extras.", "# 1. verify binary\n# 2. verify provider auth\n# 3. confirm active config path\n# 4. add extras later"),
        ],
        "failure_routes": [
            ("You reset the file but the behavior stayed the same", "That usually means environment variables or another config copy are still active. Resetting one layer is not enough if another layer still wins."),
            ("You reset and immediately reintroduced the same mess", "If you restore every previous tweak at once, the reset bought you nothing. Rebuild from a minimal known-good path instead."),
            ("You cannot tell whether reset improved anything", "The rebuild order is too wide. Narrow it to one layer at a time so each change has a visible result."),
        ],
        "zh_title": "如何重置 DeepSeek TUI 配置",
        "zh_description": "当当前配置状态已经混乱到不值得继续修时，干净地重置 DeepSeek TUI 配置。",
        "zh_eyebrow": "配置重置",
        "zh_h1": "当当前设置状态比重新搭一遍还难理解时，就该重置 DeepSeek TUI 配置",
        "zh_intro": "重置不是失败，而是回到可解释基线最快的方式。尤其当 provider 值、环境变量覆盖和复制来的配置改动已经缠在一起时，继续补丁式排查反而更慢。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "当你已经不再信任到底是哪一层在驱动当前行为时，就应该考虑重置配置。",
        "zh_answer_p": "如果你说不清当前行为到底来自配置文件、环境变量还是旧 provider 配置块，重置往往是更合理的动作。",
        "zh_questions": [
            "什么时候重置比继续修补更高效？",
            "重置前应该保留什么？",
            "怎样从干净基线重建，而不再重复旧的混乱？",
        ],
        "zh_steps": [
            ("先记下还需要的东西", "重置前先留下你之后一定还会用到的凭据、provider 选择和关键默认值。"),
            ("先移除歧义", "备份或清理配置文件的同时，也一起检查环境变量覆盖，避免只清掉一层，另一层还在。"),
            ("按窄顺序重建", "重建顺序建议是：先确认安装、再确认 provider 认证、再确认配置路径，最后才调工作流细节。"),
        ],
        "zh_checks": [
            "重写前先备份当前文件。",
            "同时检查或移除环境变量覆盖。",
            "重置后一次只验证一层，不要立刻把旧 tweak 全部加回来。",
        ],
        "zh_mistakes": [
            "重置了配置文件，却把旧 shell export 留着不动。",
            "一次性把之前所有改动又全恢复回来，重新制造旧混乱。",
            "把重置当成替代“找活跃配置路径”的万能招。",
        ],
        "zh_links": [
            ("配置文件位置", "/zh/config/file-location/index.html"),
            ("环境变量", "/zh/config/environment-variables/index.html"),
            ("provider 设置", "/zh/config/provider-setup/index.html"),
        ],
        "zh_examples": [
            ("先备份，再一次性清掉歧义", "重置最怕半清半留。先保留旧状态一份备份，再从更窄的基线重新搭。", "cp path/to/current-config path/to/current-config.backup\n# 然后有意识地清掉或替换当前活跃文件"),
            ("一次只重建一层", "重置后先验证安装，再验证 provider 认证，最后再加配置细节。不要把所有旧 tweak 立刻恢复。", "# 重开 shell\n# 先验证 deepseek --version\n# 再只补最小 provider 设置"),
            ("先写下最小重建顺序", "重置真正有效的前提，是你知道应该按什么最短顺序重建：二进制、认证、活跃配置、最后才是额外工作流设置。", "# 1. 先验证二进制\n# 2. 再验证 provider 认证\n# 3. 确认活跃配置路径\n# 4. 其他增强最后再加"),
        ],
        "zh_failure_routes": [
            ("你重置了文件，但行为完全没变", "这通常说明环境变量或另一份配置副本还在生效。只清一层不够，另一层还在赢。"),
            ("你刚重置完，就又把旧混乱全部加回来了", "如果一次性恢复所有旧 tweak，重置就失去了意义。应该从最小可工作的基线重建。"),
            ("你甚至看不出来重置到底有没有改善", "那通常说明重建顺序太宽了。把它缩成一次只验证一层，才能看见每一步有没有效果。"),
        ],
    },
    ("mcp", "setup"): {
        "title": "Set Up MCP for DeepSeek TUI",
        "description": "Set up MCP for DeepSeek TUI in the right order so basic install and provider config are stable before server-level troubleshooting begins.",
        "eyebrow": "MCP Setup",
        "h1": "DeepSeek TUI MCP setup only feels clear when you treat it as an advanced layer on top of a stable base install",
        "intro": "MCP setup becomes confusing when users jump into servers before the underlying DeepSeek TUI install, provider auth, and config path are already reliable. The clean setup path starts lower and only climbs into MCP once the base tool is stable.",
        "answer_kicker": "Best Use",
        "answer_h2": "Set up MCP only after the base app, provider auth, and normal request flow already work without it.",
        "answer_p": "That order matters because MCP failures are much easier to isolate when the lower layers are already known-good.",
        "questions": [
            "What should already be working before you touch MCP?",
            "How do server definitions, trust, and config placement fit together?",
            "Which problems should send you back to base config instead of deeper MCP debugging?",
        ],
        "steps": [
            ("Verify the base workflow", "Make sure a normal DeepSeek TUI session already works before adding MCP servers."),
            ("Define one server path clearly", "Start with one server definition and one trust model instead of several examples at once."),
            ("Validate with narrow scope", "Test the MCP layer with one simple action before assuming the whole server toolchain is ready."),
        ],
        "checks": [
            "Confirm provider auth and config are already stable without MCP.",
            "Inspect the server definition path and expected capabilities carefully.",
            "If MCP fails early, compare the same task without MCP to isolate the layer.",
        ],
        "mistakes": [
            "Treating MCP setup as part of first install instead of an advanced second phase.",
            "Adding several servers before one simple server path is verified.",
            "Debugging servers before ruling out base config issues.",
        ],
        "links": [
            ("MCP docs", "/docs/mcp/index.html"),
            ("MCP servers", "/mcp/servers/index.html"),
            ("MCP troubleshooting", "/troubleshooting/mcp-troubleshooting/index.html"),
        ],
        "examples": [
            ("Minimal MCP bootstrap", "Start from one simple MCP config path and validate it before you add multiple servers or trust boundaries.", "deepseek-tui mcp init\ndeepseek-tui mcp list\ndeepseek-tui mcp validate"),
            ("Single-server first pass", "Add one server, validate it, and only then decide whether discovery, resources, or prompts are worth expanding.", "deepseek-tui mcp add stdio demo node ./server.js\ndeepseek-tui mcp validate"),
            ("Compare the same task with and without MCP", "The fastest way to isolate MCP is to keep the task constant and only change the MCP layer.", "# run one narrow task without MCP\n# then repeat after enabling one server"),
        ],
        "failure_routes": [
            ("Base app works but MCP tools do not appear", "That usually means server definition, config path, or discovery is wrong. Compare the same task without MCP first."),
            ("One server blocks the whole MCP layer", "Start by disabling or removing the newest server so you can isolate whether the issue is global MCP setup or one broken definition."),
            ("You added MCP before the base provider path was stable", "Roll back to the non-MCP baseline first. MCP should sit on a known-good provider path, not replace it."),
        ],
        "zh_title": "给 DeepSeek TUI 设置 MCP",
        "zh_description": "按正确顺序为 DeepSeek TUI 设置 MCP：先让基础安装和 provider 配置稳定，再进入 server 级问题。",
        "zh_eyebrow": "MCP 设置",
        "zh_h1": "只有把 MCP 当成建立在稳定基础之上的高级层，DeepSeek TUI 的 MCP 设置才会变清楚",
        "zh_intro": "如果在 DeepSeek TUI 的安装、provider 认证和配置路径都还没稳时，就直接跳进 MCP server，整个设置过程会非常混乱。干净路径一定是先把底层跑通，再上 MCP。",
        "zh_answer_kicker": "最快判断",
        "zh_answer_h2": "只有在基础 app、provider 认证和普通请求路径都已经正常时，才开始设置 MCP。",
        "zh_answer_p": "顺序很重要，因为只有底层已知没问题时，MCP 失败才更容易被隔离出来。",
        "zh_questions": [
            "动 MCP 之前，哪些东西必须已经正常工作？",
            "server 定义、信任模型和配置位置之间是什么关系？",
            "哪些问题应该让你先退回基础配置，而不是继续深挖 MCP？",
        ],
        "zh_steps": [
            ("先验证基础工作流", "在加 MCP 之前，先保证普通的 DeepSeek TUI 会话已经能跑通。"),
            ("先定义一条清晰的 server 路线", "先从一条 server 定义和一套信任模型开始，不要一上来塞多个示例。"),
            ("用最窄动作验证", "先用一个简单 MCP 动作测试，而不是直接假设整套 server 工具链都已经可用。"),
        ],
        "zh_checks": [
            "确认不带 MCP 时，provider 认证和配置已经稳定。",
            "仔细检查 server 定义路径和它声称提供的能力。",
            "如果 MCP 一开始就失败，先拿同一任务的非 MCP 路径做对比。",
        ],
        "zh_mistakes": [
            "把 MCP 设置当成首次安装的一部分，而不是第二阶段高级层。",
            "一开始就同时加多个 server。",
            "没排掉基础配置错误，就先去深挖 server 本身。",
        ],
        "zh_links": [
            ("MCP 文档", "/zh/docs/mcp/index.html"),
            ("MCP servers", "/zh/mcp/servers/index.html"),
            ("MCP 排错", "/zh/troubleshooting/mcp-troubleshooting/index.html"),
        ],
        "zh_examples": [
            ("最小 MCP 启动路径", "先只用一条简单 MCP 配置路径验证，不要一开始就同时上多个 server 和复杂信任边界。", "deepseek-tui mcp init\ndeepseek-tui mcp list\ndeepseek-tui mcp validate"),
            ("先只验证一个 server", "先加一个 server，确认能被识别，再决定要不要继续扩资源、prompts 或更多工具。", "deepseek-tui mcp add stdio demo node ./server.js\ndeepseek-tui mcp validate"),
            ("拿同一任务做有无 MCP 的对照", "隔离 MCP 最快的方法，是让任务不变，只改变 MCP 这一层。", "# 先在无 MCP 情况下跑一次窄任务\n# 再在启用单个 server 后重复同一任务"),
        ],
        "zh_failure_routes": [
            ("基础 app 能用，但 MCP 工具不出现", "通常不是 app 本体坏了，而是 server 定义、配置路径或 discovery 出了问题。先拿同一任务做一次无 MCP 对照。"),
            ("加了一个 server 以后整层都不稳定", "先禁用或移除最新 server，判断是全局 MCP 配置有问题，还是某个定义单独坏掉。"),
            ("你在基础 provider 路线还没稳时就加了 MCP", "先退回无 MCP 基线。MCP 应该建立在已知没问题的 provider 路线上，而不是拿来替代它。"),
        ],
    },
    ("mcp", "servers"): {
        "title": "DeepSeek TUI MCP Servers",
        "description": "Understand DeepSeek TUI MCP servers as workflow capability layers, not just as a list of names to copy into config.",
        "eyebrow": "MCP Servers",
        "h1": "DeepSeek TUI MCP servers are most useful when you map each server to the exact workflow gap it fills",
        "intro": "A server list is not useful by itself. The real question is what kind of context, tool access, or workflow speed each MCP server adds, and whether that gain is worth the extra trust and maintenance cost.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Judge MCP servers by the workflow they unlock, not by the novelty of their names.",
        "answer_p": "A good server choice solves a real gap in context or action. A bad one only adds complexity and another failure layer.",
        "questions": [
            "What workflow gap does a given MCP server actually close?",
            "How do you compare context servers, action servers, and convenience servers?",
            "When is a server worth the trust and maintenance overhead?",
        ],
        "steps": [
            ("Start from the task", "Pick the server from the workflow need, not the other way around."),
            ("Group servers by capability", "Separate context extension, action execution, and speed/convenience patterns when evaluating them."),
            ("Keep the trust boundary visible", "Every server adds another operational boundary, so map that cost before you scale the stack."),
        ],
        "checks": [
            "Can the same workflow be solved with normal prompts or built-in tools first?",
            "Does the server add a meaningful capability or just a fashionable extra layer?",
            "Have you documented what should happen if that server becomes unavailable?",
        ],
        "mistakes": [
            "Collecting servers because examples look interesting instead of because a workflow needs them.",
            "Treating all servers as equally trusted.",
            "Adding more capability without documenting failure expectations.",
        ],
        "links": [
            ("MCP setup", "/mcp/setup/index.html"),
            ("Server examples", "/mcp/server-examples/index.html"),
            ("Tool surface docs", "/docs/tool-surface/index.html"),
        ],
        "examples": [
            ("Group servers by job, not by hype", "Write down whether a server expands context, executes actions, or only adds convenience before you add it to the stack.", "# classify each candidate server by workflow benefit\n# keep only the ones that close a real gap"),
            ("Test one server against one real task", "A useful server should make one concrete workflow better, not just make the config look more advanced.", "# add one server\n# test one task that clearly needs that capability"),
        ],
        "failure_routes": [
            ("You keep adding servers but the workflow is not getting better", "That usually means you are collecting capability names, not solving a real task gap. Re-evaluate from the workflow backward."),
            ("You do not know which server caused the failure", "The stack is already too wide. Disable back to one server and rebuild one capability layer at a time."),
        ],
        "zh_title": "DeepSeek TUI 的 MCP Servers",
        "zh_description": "把 DeepSeek TUI 的 MCP servers 看成工作流能力层，而不是只复制进配置的一串名字。",
        "zh_eyebrow": "MCP Servers",
        "zh_h1": "只有把每个 MCP server 映射回真实工作流缺口，DeepSeek TUI 的 MCP servers 才算真正有用",
        "zh_intro": "一个 server 列表本身并不值钱。真正的问题是：它补的是哪类上下文、哪类动作能力、哪类流程速度，以及这份收益值不值得额外的信任和维护成本。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "评估 MCP server 时，先看它补上的工作流能力，而不是先看名字是否新鲜。",
        "zh_answer_p": "好的 server 能补真实缺口；不合适的 server 只会给系统加一层复杂度和失败源。",
        "zh_questions": [
            "一个 MCP server 到底补上了哪类工作流缺口？",
            "怎么区分上下文型、动作型和便利型 server？",
            "什么时候一个 server 值得承担额外的信任和维护成本？",
        ],
        "zh_steps": [
            ("从任务出发选 server", "先从工作流需求出发，再决定要不要上对应 server。"),
            ("按能力分组", "把 server 分成上下文扩展、动作执行和速度/便利三类来比较。"),
            ("把信任边界写出来", "每多一个 server，就多一层操作边界，这个代价要在一开始就看见。"),
        ],
        "zh_checks": [
            "这个工作流能不能先用普通提示词或内建工具解决？",
            "这个 server 补的是实质能力，还是只是看起来高级？",
            "它如果不可用，你是否知道系统应当如何退回？",
        ],
        "zh_mistakes": [
            "因为示例看起来有趣，就不断堆 server。",
            "默认所有 server 都同样可信。",
            "只加能力，不写失败预期和退路。",
        ],
        "zh_links": [
            ("MCP 设置", "/zh/mcp/setup/index.html"),
            ("server examples", "/zh/mcp/server-examples/index.html"),
            ("工具边界文档", "/zh/docs/tool-surface/index.html"),
        ],
        "zh_examples": [
            ("按工作职能分组，不按热度分组", "先写清楚一个 server 到底是在补上下文、执行动作，还是只是增加便利，再决定要不要接进去。", "# 先按工作流收益给每个候选 server 分类\n# 只留下真正补缺口的"),
            ("一个 server 只对照一个真实任务", "有价值的 server 应该能明确改善一类任务，而不是只让配置看起来更高级。", "# 先加一个 server\n# 用一个明确需要该能力的任务做验证"),
        ],
        "zh_failure_routes": [
            ("server 越加越多，但工作流并没有更顺", "这通常说明你在收集能力名词，而不是在解决真实任务缺口。先回到工作流本身重判。"),
            ("你已经说不清到底是哪个 server 在导致失败", "说明栈已经太宽了。先退回到单 server，再一层一层加回来。"),
        ],
    },
    ("mcp", "server-examples"): {
        "title": "DeepSeek TUI MCP Server Examples",
        "description": "Use DeepSeek TUI MCP server examples to understand which workflows each server extends before you copy a setup into config.",
        "eyebrow": "MCP Server Examples",
        "h1": "MCP server examples become useful only when they explain the workflow each example actually expands",
        "intro": "Examples are helpful when they translate abstract capability into a real task shape. Without that workflow framing, a server example becomes little more than a name, a snippet, and another chance to copy complexity without understanding it.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "A good MCP server example tells you what workflow it changes, not just what config block it uses.",
        "answer_p": "Examples should help you decide whether the server is relevant at all before you spend time wiring it into your environment.",
        "questions": [
            "What kind of task does this example improve?",
            "Does the example extend context, action, or execution speed?",
            "Could a simpler prompt or existing tool already cover most of the need?",
        ],
        "steps": [
            ("Read examples by task shape", "Group examples around the kind of work they improve instead of reading them as isolated snippets."),
            ("Compare benefit versus setup cost", "Each example should justify the extra setup, trust boundary, and maintenance it introduces."),
            ("Test one example in a narrow workflow", "Validate the example in the smallest useful real task before rolling it into a bigger stack."),
        ],
        "checks": [
            "Can you state the exact workflow benefit in one sentence?",
            "Do you know what should happen if the example server is unavailable?",
            "Have you compared it against a simpler non-MCP path first?",
        ],
        "mistakes": [
            "Copying example config before deciding whether the server solves a real problem.",
            "Treating examples as endorsements instead of illustrations.",
            "Expanding the MCP stack faster than you can verify it.",
        ],
        "links": [
            ("MCP servers", "/mcp/servers/index.html"),
            ("MCP setup", "/mcp/setup/index.html"),
            ("Skills examples", "/skills/examples/index.html"),
        ],
        "examples": [
            ("Translate the example into a workflow sentence first", "Before you copy any config, say what the example changes in plain workflow terms: more context, more action, or less manual repetition.", "# write the workflow sentence first\n# only then compare it with the example server block"),
            ("Discard examples that do not improve a live task", "If an example does not improve one real task on your machine, keep it out of the active MCP stack.", "# test one real task\n# remove the example if it adds setup cost without workflow gain"),
        ],
        "failure_routes": [
            ("The example config looks fine but the task did not improve", "Then the example may be interesting but not relevant to your workflow. Do not keep it just because it works in theory."),
            ("You copied several examples and lost the original baseline", "Reset to one example and one task. Examples are only useful when you can isolate the benefit of each one."),
        ],
        "zh_title": "DeepSeek TUI 的 MCP Server Examples",
        "zh_description": "通过 DeepSeek TUI 的 MCP server examples，先理解每个示例扩展了哪类工作流，再决定要不要接进配置。",
        "zh_eyebrow": "MCP Server Examples",
        "zh_h1": "只有当示例能说明它扩展了哪类工作流时，MCP server examples 才真正有价值",
        "zh_intro": "示例真正有帮助的地方，不是贴一段配置，而是把抽象能力翻译成真实任务形状。否则它只是一个名字、一个片段，以及另一次盲目复制复杂度的机会。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "好的 MCP server 示例，应该先告诉你它改变了哪类工作流，而不只是展示配置块长什么样。",
        "zh_answer_p": "示例的价值，在于帮助你决定这个 server 值不值得接，而不是默认你应该直接照抄。",
        "zh_questions": [
            "这个示例到底改善了什么类型的任务？",
            "它扩展的是上下文、动作，还是执行速度？",
            "更简单的提示词或现有工具能不能已经覆盖大部分需求？",
        ],
        "zh_steps": [
            ("按任务形状读示例", "不要把示例当成孤立片段，而要按它改进的工作流类型来理解。"),
            ("比较收益和接入成本", "每个示例都应该说明它值不值得那一层额外设置、信任和维护成本。"),
            ("先在小任务里验证", "先在最小有意义的真实任务里测试这个示例，再决定要不要放进更大的 MCP 栈。"),
        ],
        "zh_checks": [
            "你能不能用一句话说清楚这个示例的工作流收益？",
            "你是否知道这个 server 不可用时应该怎么退回？",
            "你有没有先拿一个更简单的非 MCP 路线做过对比？",
        ],
        "zh_mistakes": [
            "还没判断它解决的是什么问题，就先复制示例配置。",
            "把示例误解成官方背书，而不是说明用法。",
            "MCP 栈扩张速度比验证速度还快。",
        ],
        "zh_links": [
            ("MCP servers", "/zh/mcp/servers/index.html"),
            ("MCP 设置", "/zh/mcp/setup/index.html"),
            ("Skills examples", "/zh/skills/examples/index.html"),
        ],
        "zh_examples": [
            ("先把示例翻译成一句工作流描述", "复制任何配置前，先用一句人话说清楚这个示例到底改变了什么：更多上下文、更多动作，还是减少手工重复。", "# 先写出这条工作流说明\n# 再回头对照示例 server 配置"),
            ("对真实任务没帮助的示例就不要留", "如果一个示例在你机器上的真实任务里没有明显收益，就不要把它留在活跃 MCP 栈里。", "# 用一个真实任务测试\n# 没有流程收益就移除这个示例"),
        ],
        "zh_failure_routes": [
            ("示例配置看起来没问题，但任务没有变好", "那说明它可能只是有趣，不一定适合你的工作流。不要因为理论上能用就继续保留。"),
            ("你一口气复制了多个示例，最后连基线都丢了", "先退回单个示例和单个任务。示例只有在你能隔离收益时才有价值。"),
        ],
    },
    ("modes", "plan-mode"): {
        "title": "DeepSeek TUI Plan Mode",
        "description": "Understand DeepSeek TUI plan mode as the review-first workflow for higher-risk tasks, slower execution, and clearer operator control.",
        "eyebrow": "Plan Mode",
        "h1": "DeepSeek TUI plan mode is for sessions where review discipline matters more than raw momentum",
        "intro": "Plan mode slows the agent down into a more inspectable workflow. That trade-off is useful when file changes, command execution, or task ambiguity are risky enough that you want to see the shape of the work before the tool pushes further.",
        "answer_kicker": "Best For",
        "answer_h2": "Use plan mode when the cost of a bad action is higher than the cost of extra review time.",
        "answer_p": "It is not the fastest mode. It is the mode that makes intent, sequencing, and review feel more visible before action.",
        "questions": [
            "What kinds of tasks benefit most from plan mode?",
            "What do you gain in control and lose in speed?",
            "How should your review habits change when plan mode is active?",
        ],
        "steps": [
            ("Start with risk, not preference", "Choose plan mode because the task is expensive to get wrong, not because slower always feels safer."),
            ("Use it to clarify the task shape", "The main benefit is seeing the structure and intended order of work before the agent acts too far ahead."),
            ("Escalate only when confidence rises", "Once the workflow is stable and understood, decide whether this mode still matches the task or if you should switch later."),
        ],
        "checks": [
            "Use it for destructive commands, larger edits, unclear scope, or unfamiliar repos.",
            "Watch whether the extra review steps are actually reducing mistakes or just slowing down trivial work.",
            "If the task becomes straightforward, compare it with yolo mode rather than staying cautious by habit.",
        ],
        "mistakes": [
            "Using plan mode for every tiny task and then blaming the tool for being slow.",
            "Assuming plan mode removes the need for review discipline.",
            "Never re-evaluating whether the task still deserves the slower mode.",
        ],
        "links": [
            ("Modes hub", "/modes/index.html"),
            ("Plan vs yolo", "/modes/plan-vs-yolo/index.html"),
            ("Yolo mode", "/modes/yolo-mode/index.html"),
        ],
        "examples": [
            ("Good fit example", "Use plan mode when you are entering an unfamiliar repo, making broader edits, or touching commands whose downside is more expensive than extra review time.", ""),
            ("Review-first checkpoint", "If you still need to inspect intended file scope, command sequence, or task shape before action, plan mode is doing real work for you rather than adding ceremony.", ""),
            ("Escalate from discovery to action in stages", "A practical plan-mode session usually starts with repo reading, then narrows to a concrete edit plan, then only later reaches commands or file writes.", "# first inspect repo structure\n# then summarize intended file scope\n# only then move into edits or commands"),
        ],
        "failure_routes": [
            ("Plan mode feels slow on every task", "That usually means the task no longer deserves high review overhead. Compare it against yolo mode instead of blaming the mode itself."),
            ("You still skip review even in plan mode", "Then the workflow problem is operator discipline, not mode choice. Plan mode only helps if you actually use the visibility it provides."),
            ("You are using plan mode but still making huge jumps", "The issue is not the mode label; it is that the work is not being staged. Break the task into repo reading, intent check, and action steps."),
        ],
        "zh_title": "DeepSeek TUI 的 Plan Mode",
        "zh_description": "把 DeepSeek TUI 的 plan mode 理解成更偏审查优先的工作流，适合高风险任务、较慢执行和更清楚的操作者控制。",
        "zh_eyebrow": "Plan Mode",
        "zh_h1": "当审查纪律比推进速度更重要时，DeepSeek TUI 的 plan mode 才最有价值",
        "zh_intro": "plan mode 会主动把代理节奏放慢，让工作流更可检查。当文件修改、命令执行或任务边界足够敏感时，这种在行动前先看清结构和顺序的方式，往往更值得。",
        "zh_answer_kicker": "适合什么",
        "zh_answer_h2": "当一次错误动作的代价，比多花一点审查时间的代价更高时，就优先选 plan mode。",
        "zh_answer_p": "它不是最快的模式，但它能让意图、顺序和审查点在行动前更清楚。",
        "zh_questions": [
            "哪类任务最适合用 plan mode？",
            "你在控制力上获得了什么，又在速度上失去了什么？",
            "进入 plan mode 后，审查习惯应该怎样跟着调整？",
        ],
        "zh_steps": [
            ("先看任务风险，不是先看个人偏好", "选 plan mode 的理由应该是任务错不起，而不是单纯因为“慢一点看起来更安全”。"),
            ("利用它把任务形状看清楚", "plan mode 最大的价值，是让你在代理走远之前先看到工作的结构和顺序。"),
            ("信心起来后再决定要不要继续", "当任务已经变得稳定清楚时，再判断当前模式是否仍然最合适。"),
        ],
        "zh_checks": [
            "高风险命令、大改动、范围不清或陌生代码库时，更适合先开它。",
            "观察额外的审查步骤到底是在减少错误，还是只是在拖慢简单任务。",
            "如果任务已经变得直接，可以和 yolo mode 做对比，不要只是习惯性保持保守。",
        ],
        "zh_mistakes": [
            "所有小任务都用 plan mode，最后嫌工具太慢。",
            "以为开了 plan mode 就不需要自己再审查。",
            "任务都已经稳定了，却从不重新判断模式是否应该切换。",
        ],
        "zh_links": [
            ("模式总页", "/zh/modes/index.html"),
            ("plan vs yolo", "/zh/modes/plan-vs-yolo/index.html"),
            ("Yolo mode", "/zh/modes/yolo-mode/index.html"),
        ],
        "zh_examples": [
            ("适合 plan mode 的场景", "进入陌生仓库、要做范围更大的修改，或者命令一旦错了代价更高时，plan mode 才是在替你省风险。", ""),
            ("真正的 review-first 检查点", "如果你还需要看清文件范围、命令顺序和任务形状，plan mode 就不是仪式感，而是在做实事。", ""),
            ("按阶段从发现走到执行", "更实用的 plan-mode 会话，通常不是立刻动手，而是先看仓库、再缩窄文件范围、最后才进入命令和写入。", "# 先读 repo 结构\n# 再总结要动的文件范围\n# 最后才进入编辑或命令"),
        ],
        "zh_failure_routes": [
            ("你觉得每个任务都太慢", "通常不是 mode 本身有问题，而是这个任务已经不值得这么高的审查成本。应该和 yolo mode 对比。"),
            ("开了 plan mode 但你还是不看审查信息", "那问题就不是 mode 选择，而是操作者根本没利用它提供的可见性。"),
            ("你开着 plan mode，却还是在做大跳跃", "问题不在名字，而在于任务没有分阶段。先拆成看 repo、核对意图、再执行这三层。"),
        ],
    },
    ("modes", "yolo-mode"): {
        "title": "DeepSeek TUI Yolo Mode",
        "description": "Understand DeepSeek TUI yolo mode as the speed-first workflow that trades extra caution for momentum when the task is already well-bounded.",
        "eyebrow": "Yolo Mode",
        "h1": "DeepSeek TUI yolo mode is strongest when the task is already bounded and momentum matters more than extra hesitation",
        "intro": "Yolo mode exists for workflows where the operator is willing to accept more direct action in exchange for speed. That is useful only when the scope is already clear enough that extra review pauses add more friction than value.",
        "answer_kicker": "Best For",
        "answer_h2": "Use yolo mode when the task is already narrow, recoverable, and expensive to slow down unnecessarily.",
        "answer_p": "The key question is not whether speed feels good. The key question is whether the current task can afford less hesitation.",
        "questions": [
            "What kinds of tasks are bounded enough for yolo mode?",
            "What review habits should remain even when the mode is faster?",
            "When does yolo mode stop being efficient and start becoming reckless?",
        ],
        "steps": [
            ("Confirm the scope is already narrow", "Yolo mode works best when the repo, files, and action boundary are already well understood."),
            ("Keep the recovery path visible", "Faster action is only acceptable when you still know how to inspect, stop, or recover if the path drifts."),
            ("Use it where waiting is the bigger cost", "The point is to reduce unnecessary hesitation, not to remove thinking entirely."),
        ],
        "checks": [
            "Use it for repetitive, low-risk, or already-verified flows.",
            "Pause before switching to it on destructive commands or unclear repos.",
            "If you find yourself reading every step anyway, plan mode may be the better fit.",
        ],
        "mistakes": [
            "Using yolo mode because it sounds impressive instead of because the task is truly bounded.",
            "Dropping all review habits once the faster mode is active.",
            "Treating recoverability as an afterthought.",
        ],
        "links": [
            ("Modes hub", "/modes/index.html"),
            ("Plan vs yolo", "/modes/plan-vs-yolo/index.html"),
            ("Plan mode", "/modes/plan-mode/index.html"),
        ],
        "examples": [
            ("Good fit example", "Use yolo mode on tasks that are already bounded, recoverable, and cheap to correct, such as narrow repetitive edits or known-safe verification loops.", ""),
            ("Still keep a recovery path", "The mode is faster, but it still works best when you know which files, commands, or checkpoints let you stop or recover quickly.", ""),
        ],
        "failure_routes": [
            ("Yolo mode feels reckless too early", "That usually means the task boundary is still unclear. Switch back to plan mode until the repo and file scope are stable."),
            ("You are re-reading every step anyway", "Then the task is not actually yolo-ready yet, or your risk tolerance is lower than the mode assumes. Use plan mode instead of fighting the workflow."),
        ],
        "zh_title": "DeepSeek TUI 的 Yolo Mode",
        "zh_description": "把 DeepSeek TUI 的 yolo mode 理解成速度优先工作流，适合边界已经清楚、不值得再多做犹豫的任务。",
        "zh_eyebrow": "Yolo Mode",
        "zh_h1": "当任务边界已经足够清楚、继续犹豫反而更贵时，DeepSeek TUI 的 yolo mode 才最有价值",
        "zh_intro": "yolo mode 是为那些操作者愿意用更直接行动换取推进速度的场景设计的。它真正成立的前提，是当前范围已经足够清楚，额外的审查停顿带来的摩擦大于收益。",
        "zh_answer_kicker": "适合什么",
        "zh_answer_h2": "当任务已经够窄、可恢复，而且不值得被额外迟疑拖慢时，yolo mode 才是合理选择。",
        "zh_answer_p": "关键不是速度听起来爽不爽，而是这个任务是否真的承受得起更少犹豫。",
        "zh_questions": [
            "哪类任务的边界已经足够清楚，适合 yolo mode？",
            "即使模式更快，哪些审查习惯仍然不能丢？",
            "什么时候 yolo mode 从高效变成了鲁莽？",
        ],
        "zh_steps": [
            ("先确认任务边界已经够窄", "yolo mode 最适合 repo、文件范围和动作边界都已经明确的场景。"),
            ("始终保留恢复路径", "更快的行动只有在你仍然知道怎么检查、停止或回滚时才合理。"),
            ("把它用在等待成本更高的地方", "它的目标是减少无谓迟疑，而不是把思考整个拿掉。"),
        ],
        "zh_checks": [
            "重复性高、低风险、已经验证过的流程更适合它。",
            "面对破坏性命令或陌生仓库前，先停一下再决定要不要切它。",
            "如果你发现自己其实每一步都还要详细审查，那 plan mode 可能更合适。",
        ],
        "zh_mistakes": [
            "因为名字听起来猛，就默认该用它。",
            "一进更快模式，就把所有审查习惯都丢掉。",
            "把可恢复性放到最后才想。",
        ],
        "zh_links": [
            ("模式总页", "/zh/modes/index.html"),
            ("plan vs yolo", "/zh/modes/plan-vs-yolo/index.html"),
            ("Plan mode", "/zh/modes/plan-mode/index.html"),
        ],
        "zh_examples": [
            ("适合 yolo mode 的场景", "边界已经清楚、可恢复成本低、修正代价也低的任务，更适合 yolo mode，比如窄范围重复修改或已知安全的验证循环。", ""),
            ("更快不等于没有恢复路径", "它确实更快，但前提仍然是你知道哪些文件、命令或检查点能让你及时停下或回退。", ""),
        ],
        "zh_failure_routes": [
            ("你觉得它太早开始鲁莽", "通常说明任务边界还不够清楚。先切回 plan mode，把 repo 和文件范围压稳。"),
            ("你其实每一步还是要重新审", "那这个任务还没准备好进入 yolo，或者你的风险容忍本来就更低。不要硬撑。"),
        ],
    },
    ("modes", "plan-vs-yolo"): {
        "title": "DeepSeek TUI Plan Mode vs Yolo Mode",
        "description": "Compare DeepSeek TUI plan mode vs yolo mode by risk, task shape, review habits, and the real cost of slowing down or moving too fast.",
        "eyebrow": "Mode Comparison",
        "h1": "Plan mode vs yolo mode is really a question of task risk, review cost, and how bounded the workflow already is",
        "intro": "This comparison matters because the two modes are not personality labels. They are workflow shapes. The better question is not which mode is cooler, but which mode matches the current task’s risk, clarity, and cost of hesitation.",
        "answer_kicker": "Direct Answer",
        "answer_h2": "Choose plan mode when review cost is cheaper than a bad action. Choose yolo mode when hesitation cost is higher and the task is already bounded.",
        "answer_p": "The right answer can change from task to task, even for the same operator.",
        "questions": [
            "How do the two modes differ in review burden, speed, and risk tolerance?",
            "Which tasks naturally belong to one mode first?",
            "What signals tell you to switch rather than forcing one mode everywhere?",
        ],
        "steps": [
            ("Compare the downside first", "Ask whether the worse outcome is a bad action or a slow workflow. That often answers the mode question quickly."),
            ("Look at how bounded the task is", "The clearer the file scope and action boundary, the more reasonable yolo mode becomes."),
            ("Re-evaluate mid-task", "A task can start in plan mode and later become yolo-appropriate once uncertainty collapses."),
        ],
        "checks": [
            "Use plan mode for high-risk, ambiguous, or destructive work.",
            "Use yolo mode for repetitive, recoverable, and already-understood work.",
            "If you keep overriding the mode’s natural behavior, switch instead of fighting it.",
        ],
        "mistakes": [
            "Picking one mode as a permanent identity instead of a situational tool.",
            "Using yolo mode on unclear tasks because speed feels satisfying.",
            "Staying in plan mode long after the task stopped deserving it.",
        ],
        "links": [
            ("Plan mode", "/modes/plan-mode/index.html"),
            ("Yolo mode", "/modes/yolo-mode/index.html"),
            ("Modes hub", "/modes/index.html"),
        ],
        "examples": [
            ("Switch to yolo only after plan has collapsed the uncertainty", "A common good path is starting in plan mode for repo discovery, then moving to yolo once file scope and recovery paths are obvious.", "# start in plan mode for unknown scope\n# switch to yolo only after the task is narrow and recoverable"),
            ("Stay in plan when the downside is still larger than the delay", "If you still cannot comfortably name the affected files, command risk, or rollback story, the task is not ready for yolo yet.", "# if uncertainty is still high, keep plan mode active"),
        ],
        "failure_routes": [
            ("You chose a mode because it matched your identity, not the task", "That usually creates friction quickly. Re-evaluate the task boundary instead of trying to force one mode everywhere."),
            ("You keep wanting speed and safety at the same time", "That usually means the task should be staged: use plan to narrow it, then switch to yolo for the low-risk finish."),
        ],
        "zh_title": "DeepSeek TUI 的 Plan Mode vs Yolo Mode",
        "zh_description": "从风险、任务形状、审查习惯和“慢下来或冲太快”的真实代价，比较 DeepSeek TUI 的 plan mode 与 yolo mode。",
        "zh_eyebrow": "模式对比",
        "zh_h1": "Plan mode vs yolo mode，本质上比较的是任务风险、审查成本，以及当前工作流边界到底清不清楚",
        "zh_intro": "这组对比有价值，是因为两个 mode 不是性格标签，而是工作流形状。真正该问的不是哪个模式更酷，而是当前任务的风险、清晰度和迟疑成本，更匹配哪一条路线。",
        "zh_answer_kicker": "直接答案",
        "zh_answer_h2": "当审查成本低于一次错误动作的代价时选 plan mode；当迟疑成本更高且任务边界已清楚时选 yolo mode。",
        "zh_answer_p": "对同一个操作者来说，不同任务的答案也可以完全不同。",
        "zh_questions": [
            "两个模式在审查负担、速度和风险容忍上到底怎么不同？",
            "哪类任务天然更适合先用其中一个？",
            "什么信号说明你应该切模式，而不是硬撑在一个模式里？",
        ],
        "zh_steps": [
            ("先比最坏结果", "先问：更糟糕的是一次错误动作，还是被流程拖慢？这个问题往往很快就能决定模式。"),
            ("看任务边界有多清楚", "文件范围和动作边界越清晰，yolo mode 就越合理。"),
            ("允许中途重新判断", "一个任务可以先用 plan mode 起步，等不确定性收敛后再切向 yolo。"),
        ],
        "zh_checks": [
            "高风险、模糊或破坏性任务优先用 plan mode。",
            "重复、可恢复、已经理解透的任务更适合 yolo mode。",
            "如果你一直在和当前模式的自然行为对着干，不如直接切模式。",
        ],
        "zh_mistakes": [
            "把一个模式当成永久身份标签，而不是按场景选择的工具。",
            "因为喜欢快，就在边界不清时上 yolo mode。",
            "任务早就清楚了，却还在 plan mode 里机械停留。",
        ],
        "zh_links": [
            ("Plan mode", "/zh/modes/plan-mode/index.html"),
            ("Yolo mode", "/zh/modes/yolo-mode/index.html"),
            ("模式总页", "/zh/modes/index.html"),
        ],
        "zh_examples": [
            ("先用 plan 压缩不确定性，再切 yolo", "最常见的好路径不是二选一，而是先用 plan 看清仓库和文件范围，等边界清楚后再切 yolo 收尾。", "# 先用 plan mode 处理未知范围\n# 只有任务够窄、可恢复时再切 yolo"),
            ("当错误代价仍高于等待代价时，就别急着切 yolo", "如果你还说不清会动哪些文件、命令风险多大、回退路径在哪里，这个任务就还没准备好上 yolo。", "# 只要不确定性还高，就继续保留 plan mode"),
        ],
        "zh_failure_routes": [
            ("你选 mode 是因为它像一种身份标签，不是因为任务需要", "这种情况很快就会产生摩擦。先重新判断任务边界，不要硬把一个 mode 套到所有任务上。"),
            ("你同时又想要最快速度，又想要最高安全", "这通常说明任务应该分阶段：先用 plan 缩窄，再把低风险尾段切给 yolo。"),
        ],
    },
}


def replace_once(text: str, pattern: str, repl: str) -> str:
    return re.sub(pattern, repl, text, count=1, flags=re.S)


def cards_html(items: list[tuple[str, str]], zh: bool) -> str:
    label = "步骤" if zh else "Step"
    return "".join(
        f'<article class="content-card"><span class="tag">{label} {index}</span><h3>{html.escape(title)}</h3><p>{html.escape(body)}</p></article>'
        for index, (title, body) in enumerate(items, start=1)
    )


def list_html(items: list[str]) -> str:
    return "".join(f"<li>{html.escape(item)}</li>" for item in items)


def links_html(items: list[tuple[str, str]]) -> str:
    return "".join(f'<a href="{href}">{html.escape(label)}</a>' for label, href in items)


def example_blocks_html(items: list[tuple[str, str, str]]) -> str:
    blocks = []
    for title, body, code in items:
        code_html = f"<pre><code>{html.escape(code)}</code></pre>" if code else ""
        blocks.append(
            f'<article class="detail-card"><h3>{html.escape(title)}</h3><p>{html.escape(body)}</p>{code_html}</article>'
        )
    return "".join(blocks)


def route_blocks_html(items: list[tuple[str, str]]) -> str:
    return "".join(
        f'<article class="detail-card"><h3>{html.escape(title)}</h3><p>{html.escape(body)}</p></article>'
        for title, body in items
    )


def build_main(section: str, slug: str, zh: bool) -> str:
    data = PAGES[(section, slug)]
    title = data["zh_title"] if zh else data["title"]
    eyebrow = data["zh_eyebrow"] if zh else data["eyebrow"]
    h1 = data["zh_h1"] if zh else data["h1"]
    intro = data["zh_intro"] if zh else data["intro"]
    answer_kicker = data["zh_answer_kicker"] if zh else data["answer_kicker"]
    answer_h2 = data["zh_answer_h2"] if zh else data["answer_h2"]
    answer_p = data["zh_answer_p"] if zh else data["answer_p"]
    questions = data["zh_questions"] if zh else data["questions"]
    steps = data["zh_steps"] if zh else data["steps"]
    checks = data["zh_checks"] if zh else data["checks"]
    mistakes = data["zh_mistakes"] if zh else data["mistakes"]
    links = data["zh_links"] if zh else data["links"]
    examples = data.get("zh_examples" if zh else "examples", [])
    failure_routes = data.get("zh_failure_routes" if zh else "failure_routes", [])
    source_label = "本页是站内详情页" if zh else "Site detail page"
    section_label = SECTION_LABELS_ZH.get(section, section) if zh else SECTION_LABELS_EN.get(section, section.title())
    section_head = "推荐阅读顺序" if zh else "Recommended reading order"
    section_desc = "先按当前问题走，再决定要不要切去相邻详情页或 hub。" if zh else "Move through the page by workflow need first, then branch into adjacent detail pages or hubs."
    question_head = "这页能直接回答的问题" if zh else "Questions this page should answer fast"
    checks_head = "做完后该核对什么" if zh else "What to verify next"
    mistakes_head = "最常见的误区" if zh else "Common mistakes"
    where_head = "什么时候该离开这页" if zh else "When to leave this page"
    examples_head = "直接可用的示例" if zh else "Use-it-now examples"
    routes_head = "常见失败分支" if zh else "Common failure branches"
    where_text = (
        "当你已经确认当前路线没问题，就不要继续停留在这页。安装线应转去配置，配置线应转去 provider 或排错，MCP 和模式线则应该转回真实工作流页。详情页的价值是把问题缩窄，而不是长期停留在解释层。"
        if zh else
        "Once the route is clear, leave this page quickly. Install pages should hand you into config, config pages should send you into provider or troubleshooting, and MCP or mode pages should send you back into live workflow decisions. A detail page is valuable because it narrows the problem, not because you stay on it forever."
    )
    links_block = links_html(links)
    examples_section = ""
    if examples:
        examples_section = f"""<section class="section"><div class="container"><div class="section-head"><h2>{examples_head}</h2><p>{'先拿可执行例子，再回头做更细的调整。' if zh else 'Start from working examples first, then adjust the details.'}</p></div><div class="detail-grid">{example_blocks_html(examples)}</div></div></section>"""
    routes_section = ""
    if failure_routes:
        routes_section = f"""<section class="section section-alt"><div class="container"><div class="section-head"><h2>{routes_head}</h2><p>{'先判断你卡在哪一层，再去对应分支，不要把所有问题都混成一个。' if zh else 'Work out which layer failed first instead of treating every problem as the same.'}</p></div><div class="detail-grid">{route_blocks_html(failure_routes)}</div></div></section>"""
    return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">{html.escape(eyebrow)}</span><h1>{html.escape(h1)}</h1><p>{html.escape(intro)}</p><div class="hero-points"><span>{html.escape(source_label)}</span><span>{html.escape(title)}</span><span>{html.escape(section_label)}</span></div></div><aside class="answer-card"><span class="panel-kicker">{html.escape(answer_kicker)}</span><h2>{html.escape(answer_h2)}</h2><p>{html.escape(answer_p)}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>{question_head}</h2><ul>{list_html(questions)}</ul><h2>{checks_head}</h2><ul>{list_html(checks)}</ul><h2>{mistakes_head}</h2><ul>{list_html(mistakes)}</ul></article><aside class="panel-card"><span class="panel-kicker">{'下一步' if zh else 'Next pages'}</span><div class="link-stack">{links_block}</div></aside></div></section><section class="section section-alt"><div class="container"><div class="section-head"><h2>{section_head}</h2><p>{html.escape(section_desc)}</p></div><div class="card-grid card-grid-3">{cards_html(steps, zh)}</div></div></section>{examples_section}{routes_section}<section class="section"><div class="container two-col"><article class="prose"><h2>{where_head}</h2><p>{html.escape(where_text)}</p></article><aside class="panel-card"><span class="panel-kicker">{'继续看' if zh else 'Continue with'}</span><div class="link-stack">{links_block}</div></aside></div></section></main>"""


def process(path: Path) -> None:
    rel = path.relative_to(ROOT)
    zh = rel.parts[0] == "zh"
    parts = rel.parts[1:] if zh else rel.parts
    if len(parts) != 3 or parts[2] != "index.html":
        return
    section, slug = parts[0], parts[1]
    if (section, slug) not in PAGES:
        return
    data = PAGES[(section, slug)]
    title = data["zh_title"] if zh else data["title"]
    desc = data["zh_description"] if zh else data["description"]
    text = path.read_text(encoding="utf-8")
    text = replace_once(text, r"<title>.*?</title>", f"<title>{html.escape(title)}</title>")
    text = replace_once(text, r'<meta name="description" content=".*?">', f'<meta name="description" content="{html.escape(desc)}">')
    text = replace_once(text, r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{html.escape(title)}">')
    text = replace_once(text, r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{html.escape(desc)}">')
    text = replace_once(text, r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{html.escape(title)}">')
    text = replace_once(text, r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{html.escape(desc)}">')
    text = replace_once(text, r"<main>.*?</main>", build_main(section, slug, zh))
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path in ROOT.rglob("index.html"):
        process(path)


if __name__ == "__main__":
    main()
