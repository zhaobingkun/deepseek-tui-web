from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")
DOMAIN = "https://deepseek-tui.app"

CATEGORY_DETAILS = {
    "setup": {
        "en": {
            "concrete": [
                "Which install or configuration routes the upstream doc actually treats as official first choices.",
                "Which prerequisites, file paths, environment variables, and host assumptions must already be true.",
                "What you should validate immediately before you move from setup into provider auth or runtime usage.",
                "Which values should stay local versus which ones are safe to standardize for a team.",
            ],
            "workflow": [
                "Keep one known-good baseline before you start tuning advanced options.",
                "Record the shell, package route, and config path that really worked.",
                "Treat install, provider, and config layers as separate ownership boundaries.",
            ],
        },
        "zh": {
            "concrete": [
                "上游文档真正视为官方优先路线的安装或配置方案是哪几条。",
                "哪些前置条件、文件路径、环境变量和宿主机假设必须先成立。",
                "在进入 provider 认证或运行时使用之前，应该先完成哪些验证。",
                "哪些值应该保留在本地，哪些才适合沉淀成团队级标准。",
            ],
            "workflow": [
                "先固定一套 known-good baseline，再去调整高级选项。",
                "把真正成功的 shell、包管理路线和配置路径记下来。",
                "把安装、provider 和配置看成三层不同的拥有关系。",
            ],
        },
    },
    "usage": {
        "en": {
            "concrete": [
                "Which high-frequency actions, shortcuts, or mode differences actually change daily operator speed.",
                "Which behaviors are stable enough to internalize and which ones remain situational.",
                "What fallback paths still matter when the fast path breaks or the terminal behaves differently.",
                "How this topic changes review habits, message flow, or tool usage in practice.",
            ],
            "workflow": [
                "Start with the small set of behaviors you will use every day.",
                "Treat these docs as workflow-shape docs, not only label lists.",
                "Keep one recovery path visible even after the fast route feels comfortable.",
            ],
        },
        "zh": {
            "concrete": [
                "哪些高频动作、快捷键或模式差异，会真正改变你每天的操作速度。",
                "哪些行为足够稳定，值得内化；哪些仍然更偏场景型。",
                "当快速路径失效或终端表现不一致时，哪些回退路径仍然关键。",
                "这个主题会怎样实质影响审查习惯、消息流或工具使用。",
            ],
            "workflow": [
                "先抓住你每天都会用到的那一小组行为。",
                "把这些文档当成工作流形状文档，而不是标签清单。",
                "即使快速路线已经顺手，也保留一条恢复路径。",
            ],
        },
    },
    "architecture": {
        "en": {
            "concrete": [
                "Which subsystem boundaries are real contracts instead of just naming convenience.",
                "How prompts, state, tools, runtime hooks, and rendering hand work to one another.",
                "Which parts of the upstream doc imply cross-cutting risk if you change the boundary carelessly.",
                "Which runbooks or current setup pages should be cross-checked before implementation work.",
            ],
            "workflow": [
                "Use the doc to build a mental map before you touch prompts, tools, or runtime flow.",
                "Translate diagrams into ownership questions, not only component names.",
                "Cross-check older architecture language against newer runbooks before acting on it.",
            ],
        },
        "zh": {
            "concrete": [
                "哪些子系统边界是真正的契约，而不只是命名上的方便。",
                "提示词、状态、工具、运行时钩子和渲染层之间是怎样交接工作的。",
                "上游文档哪些地方暗示了一旦随意改边界就会产生跨层风险。",
                "在进入实现工作前，应该交叉核对哪些 runbook 或 setup 页面。",
            ],
            "workflow": [
                "先用这份文档建立脑图，再去改提示词、工具或运行时流程。",
                "把图示翻译成 ownership 问题，而不只是组件名字。",
                "根据旧架构结论采取行动前，先核对更新后的 runbook。",
            ],
        },
    },
    "history": {
        "en": {
            "concrete": [
                "Which findings are version-bound history and which ones still affect current operators or maintainers.",
                "Where an old audit or runbook note should be treated as context rather than as a live blocker list.",
                "Which risks were fixed, institutionalized, or still recur under a different name.",
                "How to keep historical notes from distorting current setup and usage guidance.",
            ],
            "workflow": [
                "Always keep the version boundary visible while reading history docs.",
                "Cross-check old findings against current code, defaults, and release notes.",
                "Use them to understand drift and debt, not to replace current runbooks.",
            ],
        },
        "zh": {
            "concrete": [
                "哪些发现只是版本阶段性的历史记录，哪些到今天仍然有现实影响。",
                "哪些旧审计或旧 runbook 更应该被当成背景，而不是当前阻塞清单。",
                "哪些风险后来被修掉、制度化，或者换了名字继续复发。",
                "怎样避免让历史记录误导今天的 setup 和 usage 判断。",
            ],
            "workflow": [
                "读历史文档时，始终把版本边界摆在前面。",
                "把旧发现和当前代码、默认值、发布说明交叉核对。",
                "它们适合帮助你理解漂移和债务，不适合替代当前 runbook。",
            ],
        },
    },
    "ops": {
        "en": {
            "concrete": [
                "Which operational checkpoints the upstream doc expects before release, incident response, or coordinated maintenance.",
                "Which steps are procedural safeguards versus which ones are direct terminal or runtime actions.",
                "Where rollback, verification, and cross-team coordination are supposed to happen.",
                "Which parts of the process should stay written down so releases and incidents are repeatable under pressure.",
            ],
            "workflow": [
                "Keep release and incident steps in a stable order instead of improvising under stress.",
                "Separate operator checkpoints from actual runtime changes so ownership stays clear.",
                "Cross-check live runbooks before using historical or planning notes as operational truth.",
            ],
        },
        "zh": {
            "concrete": [
                "上游文档在发布、事故处理或协同维护前真正要求的操作检查点有哪些。",
                "哪些步骤是流程性护栏，哪些才是直接的终端或运行时动作。",
                "回滚、验证和跨团队协调应该发生在流程的哪一段。",
                "哪些过程必须被稳定写下来，才能在压力下重复执行。",
            ],
            "workflow": [
                "发布和事故步骤要保持稳定顺序，不要到压力场景里再临场编。",
                "把操作者检查点和真实运行时改动分开，ownership 才清楚。",
                "在把历史或规划文档当作操作依据前，先核对最新 runbook。",
            ],
        },
    },
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

TOPIC_DATA = {
    "accessibility": {
        "upstream": "ACCESSIBILITY.md",
        "category": "usage",
        "summary_en": "Accessibility docs explain how a keyboard-first terminal UI stays usable for different input, output, and assistive workflows.",
        "summary_zh": "可访问性文档说明了一个键盘优先的终端界面，怎样在不同输入、输出和辅助使用场景下仍然保持可用。",
        "when_en": "Read this when navigation feels harder than it should, when contrast or focus cues are unclear, or when you need to evaluate whether a new UI change will create friction.",
        "when_zh": "当你觉得导航比预期更费劲、对比度或焦点提示不清晰，或者你要判断一次新的界面改动会不会带来额外阻力时，就该先看这页。",
        "questions_en": [
            "Which interface choices most affect screen-reader, keyboard-only, or low-vision workflows?",
            "What should stay stable when the terminal UI introduces richer panes, prompts, or overlays?",
            "How do you test accessibility regressions without turning every review into a full audit?",
        ],
        "questions_zh": [
            "哪些界面选择最影响读屏、纯键盘或低视力场景？",
            "当终端 UI 引入更多面板、提示词或浮层时，哪些交互必须保持稳定？",
            "不做完整审计的前提下，怎样快速排查可访问性回退？",
        ],
        "focus_en": [
            "Keyboard focus order, visible focus states, and escape hatches back to the main interaction loop.",
            "Color, density, and motion choices that can turn a fast TUI into a cognitively heavy one.",
            "Fallback behavior when richer rendering is unavailable or partially supported by the terminal.",
            "The difference between a merely operable flow and a comfortable, repeatable workflow.",
        ],
        "focus_zh": [
            "键盘焦点顺序、可见焦点状态，以及回到主交互循环的退出路径。",
            "颜色、密度和动效选择，如何把一个原本快速的 TUI 变成认知负担。",
            "当终端不支持完整富渲染时，降级行为该怎么做。",
            "“勉强能用”和“顺手可重复”的终端流程之间到底差在哪。",
        ],
        "pitfalls_en": [
            "Treating terminal accessibility as only a color-theme problem.",
            "Optimizing for screenshots instead of real keyboard traversal.",
            "Forgetting that faster expert flows still need predictable exits and recovery paths.",
        ],
        "pitfalls_zh": [
            "把终端可访问性只当成换配色的问题。",
            "只优化截图效果，而不去看真实键盘遍历体验。",
            "忽略了高阶快速流程同样需要稳定的退出和恢复路径。",
        ],
        "related": ["docs", "guides", "troubleshooting"],
    },
    "architecture": {
        "upstream": "ARCHITECTURE.md",
        "category": "architecture",
        "summary_en": "Architecture docs map the major subsystems so you can understand where prompts, runtime state, tools, transport, and UI boundaries actually meet.",
        "summary_zh": "架构文档用来梳理主要子系统，让你看清提示词、运行时状态、工具、传输层和 UI 边界到底在哪里交汇。",
        "when_en": "Read this when basic usage is already clear and you now need to reason about extension points, failure boundaries, or how multiple subsystems depend on one another.",
        "when_zh": "当基础使用已经清楚，而你开始需要判断扩展点、故障边界，或者多个子系统之间怎样互相依赖时，就该看这页。",
        "questions_en": [
            "Which components own orchestration, rendering, tool execution, and provider communication?",
            "Where do user settings stop and runtime coordination begin?",
            "Which parts can change independently and which parts create cross-cutting risk?",
        ],
        "questions_zh": [
            "哪些组件负责编排、渲染、工具执行和模型提供方通信？",
            "用户配置到哪里结束，运行时协调从哪里开始？",
            "哪些部分可以独立变更，哪些部分一改就会产生跨层风险？",
        ],
        "focus_en": [
            "Subsystem boundaries and the contracts that keep them from leaking concerns into one another.",
            "Data flow between prompts, messages, tools, state, and user-facing panes.",
            "Places where architecture docs should match runbooks and runtime behavior instead of drifting into diagrams-only thinking.",
            "The minimum mental model you need before changing prompts, tools, or mode behavior.",
        ],
        "focus_zh": [
            "子系统边界，以及防止它们互相渗透职责的契约。",
            "提示词、消息、工具、状态和用户可见面板之间的数据流。",
            "哪些地方架构文档必须和 runbook、运行时行为保持一致，而不是停留在图示层。",
            "在修改提示词、工具或模式行为前，你至少该建立怎样的脑图。",
        ],
        "pitfalls_en": [
            "Reading architecture notes as if they were current runtime guarantees without checking newer runbooks.",
            "Overfocusing on naming while missing ownership boundaries.",
            "Changing one subsystem in isolation when the contract actually spans prompt, state, and UI.",
        ],
        "pitfalls_zh": [
            "把架构文档直接当作当前运行时保证，而不去核对更新后的 runbook。",
            "只盯着命名，不去看职责边界。",
            "以为只改一个子系统，实际影响却跨越提示词、状态和 UI。",
        ],
        "related": ["docs", "config", "mcp"],
    },
    "competitive-analysis": {
        "upstream": "COMPETITIVE_ANALYSIS.md",
        "category": "history",
        "summary_en": "Competitive analysis docs explain how DeepSeek TUI positions itself against adjacent agent tools, not how to install or configure it.",
        "summary_zh": "竞争分析文档关注的是 DeepSeek TUI 相比相邻代理工具的定位，而不是安装或配置步骤。",
        "when_en": "Read this when your real question is product fit, trade-offs, or differentiation rather than a hands-on setup problem.",
        "when_zh": "当你的核心问题是产品适配、取舍或差异化，而不是具体上手操作时，这页更值得先看。",
        "questions_en": [
            "What does DeepSeek TUI intentionally emphasize or exclude compared with similar terminal agents?",
            "Which workflows justify using this tool instead of a general desktop assistant or IDE plugin?",
            "How should product comparisons influence docs, defaults, and roadmap language?",
        ],
        "questions_zh": [
            "和类似的终端代理相比，DeepSeek TUI 有哪些是刻意强调或刻意不做的？",
            "哪些工作流更适合它，而不是桌面助手或 IDE 插件？",
            "产品对比应当怎样反过来影响文档、默认值和路线图表达？",
        ],
        "focus_en": [
            "The comparison criteria that matter in practice: tool access, prompt orchestration, terminal fit, and operator control.",
            "Claims that should be backed by concrete workflow examples instead of abstract positioning language.",
            "Where comparison docs should stay current with modes, tools, and provider strategy changes.",
            "The gap between marketing comparisons and engineering constraints.",
        ],
        "focus_zh": [
            "真正有用的对比维度：工具能力、提示词编排、终端适配和操作者控制力。",
            "哪些结论必须用具体工作流举例支撑，而不是抽象定位话术。",
            "当模式、工具或提供方策略变化后，对比文档哪些地方要跟着更新。",
            "营销式对比和工程约束之间的落差。",
        ],
        "pitfalls_en": [
            "Using old competitive claims after core features or defaults have shifted.",
            "Comparing brand labels instead of workflow outcomes.",
            "Treating the analysis as end-user onboarding instead of positioning context.",
        ],
        "pitfalls_zh": [
            "核心功能或默认值变化了，却还在沿用旧的竞争结论。",
            "只对比品牌标签，不对比真实工作流结果。",
            "把这类分析当成新手上手文档，而不是定位背景。",
        ],
        "related": ["docs", "guides", "comparisons"],
    },
    "configuration": {
        "upstream": "CONFIGURATION.md",
        "category": "setup",
        "summary_en": "Configuration docs explain which settings change provider behavior, runtime defaults, memory, tools, and environment-specific assumptions.",
        "summary_zh": "配置文档解释了哪些设置会改变提供方行为、运行时默认值、记忆能力、工具能力以及环境相关假设。",
        "when_en": "Read this when the app starts but behaves differently from what you expect, or when you need to make settings portable across machines and providers.",
        "when_zh": "当程序已经能启动，但行为和预期不一致，或者你需要让配置在不同机器和提供方之间可迁移时，就该先看这页。",
        "questions_en": [
            "Which settings are required, optional, experimental, or provider-specific?",
            "Which values belong in config files versus environment variables?",
            "How do you change defaults without making the setup brittle for teammates or future upgrades?",
        ],
        "questions_zh": [
            "哪些设置是必需、可选、实验性，或者只对特定提供方生效？",
            "哪些值应该写进配置文件，哪些更适合环境变量？",
            "怎样修改默认值，才不会让团队协作或后续升级变脆弱？",
        ],
        "focus_en": [
            "Provider blocks, model-related defaults, and how per-provider overrides interact with global settings.",
            "Settings that affect tool permissions, memory behavior, or orchestration rather than only cosmetics.",
            "The order of precedence between checked-in config, local overrides, and shell-level environment.",
            "A minimal safe baseline before you start tuning advanced options.",
        ],
        "focus_zh": [
            "提供方配置块、模型默认值，以及提供方级覆盖和全局设置的交互关系。",
            "哪些设置会影响工具权限、记忆行为或编排，而不只是界面外观。",
            "版本库内配置、本地覆盖和 shell 环境变量之间的优先级。",
            "在调整高级选项之前，最小可用的安全基线是什么。",
        ],
        "pitfalls_en": [
            "Mixing provider-specific keys into a global mental model.",
            "Changing many defaults at once and losing a known-good baseline.",
            "Treating environment variables as documentation instead of reproducible config.",
        ],
        "pitfalls_zh": [
            "把提供方特定配置混进全局认知里。",
            "一次性改太多默认值，丢掉可回退的基线。",
            "把环境变量当作文档，而不是可复现的配置。",
        ],
        "related": ["docs", "config", "install"],
    },
    "docker": {
        "upstream": "DOCKER.md",
        "category": "setup",
        "summary_en": "Docker docs describe how to run DeepSeek TUI in a more controlled environment, especially when host dependencies or isolation matter.",
        "summary_zh": "Docker 文档说明了怎样在更可控的环境里运行 DeepSeek TUI，尤其适合依赖隔离或宿主机不稳定的场景。",
        "when_en": "Read this when package-manager installs are not enough, when host tooling is inconsistent, or when you want a more reproducible runtime envelope.",
        "when_zh": "当包管理器安装已经不够、宿主机工具链不一致，或者你需要更可复现的运行边界时，就该看 Docker 文档。",
        "questions_en": [
            "What does containerization actually solve for this CLI and what does it complicate?",
            "Which files, keys, and mounts need to remain available at runtime?",
            "How do you keep the container path usable without hiding normal local debugging steps?",
        ],
        "questions_zh": [
            "对这个 CLI 来说，容器化到底解决了什么，又会带来哪些额外复杂度？",
            "哪些文件、密钥和挂载在运行时必须可用？",
            "怎样在保留容器路线的同时，不把本地调试路径彻底遮住？",
        ],
        "focus_en": [
            "Volume mounts, config placement, and how credentials cross the host-container boundary.",
            "Terminal requirements that still matter even when packaging changes.",
            "The difference between a reproducible image and a reproducible workflow.",
            "What should stay documented outside Docker so the setup does not become opaque.",
        ],
        "focus_zh": [
            "卷挂载、配置位置，以及凭据如何跨越宿主机和容器边界。",
            "即使打包方式改变，终端层面仍然必须满足的要求。",
            "“镜像可复现”和“工作流可复现”之间的区别。",
            "哪些信息仍然应该写在 Docker 之外，避免容器方案变成黑盒。",
        ],
        "pitfalls_en": [
            "Assuming Docker removes the need to understand config and credentials.",
            "Forgetting terminal capabilities still shape the user experience.",
            "Documenting the image build but not the everyday update path.",
        ],
        "pitfalls_zh": [
            "以为用了 Docker 就不用理解配置和凭据了。",
            "忽略了终端能力依然会影响最终体验。",
            "只写镜像构建，不写日常更新和调试路径。",
        ],
        "related": ["docs", "install", "troubleshooting"],
    },
    "install": {
        "upstream": "INSTALL.md",
        "category": "setup",
        "summary_en": "Install docs cover the official setup path, prerequisites, and the differences between package, source, and environment-specific installation routes.",
        "summary_zh": "安装文档覆盖官方上手路径、前置条件，以及包管理器、源码和不同环境安装路线之间的差异。",
        "when_en": "Read this when you need the most official installation flow, when a quickstart snippet fails, or when you need to choose the right installation route for your environment.",
        "when_zh": "当你需要最官方的安装路径、快速命令失败，或者你要在不同环境之间选合适的安装方案时，就该先看这页。",
        "questions_en": [
            "What prerequisites should be true before you even choose a package manager or source build route?",
            "Which install path should you prefer for Linux, macOS, Windows, or CI-like environments?",
            "How do you confirm that an install issue is really an install issue and not a config or provider issue?",
        ],
        "questions_zh": [
            "在选择包管理器或源码构建路线之前，哪些前置条件必须先满足？",
            "在 Linux、macOS、Windows 或类似 CI 的环境里，应优先选哪条安装路径？",
            "怎样判断问题真的是安装问题，而不是配置或模型提供方问题？",
        ],
        "focus_en": [
            "Supported install routes and the assumptions each one makes about the host system.",
            "Version visibility, update strategy, and how to avoid ending up with multiple competing binaries.",
            "First-run validation after install so you can separate binary issues from provider setup issues.",
            "Where the install doc stops and the config doc should take over.",
        ],
        "focus_zh": [
            "支持的安装路线，以及每条路线对宿主机做了哪些假设。",
            "版本可见性、更新策略，以及怎样避免多个二进制互相打架。",
            "安装后的首轮验证，帮助你把二进制问题和提供方配置问题分开。",
            "安装文档的边界在哪里，什么时候应该切到配置文档。",
        ],
        "pitfalls_en": [
            "Using the fastest snippet without checking platform assumptions.",
            "Installing successfully but never validating the active binary or version path.",
            "Treating post-install provider errors as if the install itself failed.",
        ],
        "pitfalls_zh": [
            "只复制最快的命令，不核对平台前提。",
            "安装成功了，却没有验证当前激活的二进制和版本路径。",
            "把安装后的提供方报错误判成安装失败。",
        ],
        "related": ["docs", "install", "config"],
    },
    "keybindings": {
        "upstream": "KEYBINDINGS.md",
        "category": "usage",
        "summary_en": "Keybindings docs turn a working TUI into a fast one by documenting navigation, pane control, and action shortcuts.",
        "summary_zh": "快捷键文档的作用，是把“能用的 TUI”变成“顺手的 TUI”，重点在导航、面板控制和常用动作快捷方式。",
        "when_en": "Read this when you already have the app running and now want to reduce friction, memorize flows, or document overrides for your team.",
        "when_zh": "当程序已经能跑，而你想减少操作阻力、记住固定流程，或者给团队记录快捷键覆盖时，这页就有用了。",
        "questions_en": [
            "Which shortcuts matter most for message flow, navigation, pane control, and tool review?",
            "Which bindings are stable muscle-memory candidates and which are more situational?",
            "How should shortcut docs change if modes or panes change later?",
        ],
        "questions_zh": [
            "在消息流、导航、面板控制和工具审查里，哪些快捷键最关键？",
            "哪些绑定适合形成肌肉记忆，哪些更偏场景型？",
            "如果模式或面板结构变化，快捷键文档应该怎么调整？",
        ],
        "focus_en": [
            "The small set of bindings that remove the most friction first.",
            "How keybindings interact with modes, prompts, and modal states instead of existing in isolation.",
            "Fallback navigation when a shortcut conflicts with terminal or OS-level behavior.",
            "How to communicate shortcut changes without breaking experienced users.",
        ],
        "focus_zh": [
            "先记住哪一小组快捷键，最能显著降低摩擦。",
            "快捷键如何和模式、提示词、模态状态联动，而不是独立存在。",
            "当快捷键和终端或系统层冲突时，备用导航路径是什么。",
            "如何传达快捷键变更，而不打断老用户习惯。",
        ],
        "pitfalls_en": [
            "Trying to memorize everything instead of starting with high-frequency paths.",
            "Documenting shortcuts without explaining which mode or pane they belong to.",
            "Ignoring platform-specific terminal conflicts.",
        ],
        "pitfalls_zh": [
            "试图一次记住全部绑定，而不是先抓高频路径。",
            "只列快捷键，不说明它属于哪个模式或面板。",
            "忽略平台或终端层的冲突。",
        ],
        "related": ["docs", "modes", "guides"],
    },
    "legacy-rust-audit-0-7-6": {
        "upstream": "LEGACY_RUST_AUDIT_0_7_6.md",
        "category": "history",
        "summary_en": "Legacy Rust audit notes capture an earlier quality and risk snapshot, which is useful only when you explicitly need historical engineering context.",
        "summary_zh": "旧版 Rust 审计记录的是更早时期的质量和风险快照，只有在你明确需要历史工程背景时才真正有价值。",
        "when_en": "Read this when you are tracing technical debt, regressions, or previously identified implementation risks rather than trying to learn normal day-to-day usage.",
        "when_zh": "当你在追踪技术债、回归问题或历史上识别过的实现风险，而不是日常使用方法时，这页才值得打开。",
        "questions_en": [
            "Which concerns were known at that version boundary and how many are still relevant now?",
            "What did the audit treat as structural versus incidental risk?",
            "Which findings should influence current architecture or release decisions today?",
        ],
        "questions_zh": [
            "在那个版本边界上，哪些问题当时已知，如今还有多少仍然相关？",
            "审计把哪些问题视为结构性风险，哪些只是偶发实现问题？",
            "哪些发现今天仍然应该影响当前架构或发布决策？",
        ],
        "focus_en": [
            "Version context first, so you do not read an old audit as if it were a current blocker list.",
            "Risk categories that still map to live subsystems or release behavior.",
            "Signals that a historical finding became institutional knowledge, a fixed bug, or a recurring class of issue.",
            "Where to cross-check current docs before acting on old conclusions.",
        ],
        "focus_zh": [
            "先建立版本语境，避免把旧审计直接当成当前阻塞清单。",
            "哪些风险类别仍然映射到今天还活着的子系统或发布行为。",
            "如何判断一个历史发现后来变成了制度化经验、已修复 bug，还是反复出现的问题类型。",
            "在根据旧结论采取行动前，应该去哪些当前文档交叉核对。",
        ],
        "pitfalls_en": [
            "Reading historical findings without rechecking the current code or runbooks.",
            "Assuming every unresolved note is still equally important.",
            "Using audit language without the version context attached.",
        ],
        "pitfalls_zh": [
            "不看当前代码或 runbook，就直接套用历史发现。",
            "默认所有未解决记录今天仍然同样重要。",
            "引用审计结论时脱离具体版本背景。",
        ],
        "related": ["docs", "troubleshooting", "guides"],
    },
    "localization": {
        "upstream": "LOCALIZATION.md",
        "category": "usage",
        "summary_en": "Localization docs explain how docs, UI copy, and workflow expectations should stay coherent across English and non-English audiences.",
        "summary_zh": "本地化文档说明文档、界面文案和工作流预期，应该怎样在英文和非英文受众之间保持一致。",
        "when_en": "Read this when you are adding another language layer, auditing translation drift, or deciding which parts of the product can stay source-language first.",
        "when_zh": "当你在增加新的语言层、排查翻译漂移，或者判断哪些部分仍然可以保持源语言优先时，这页就会有用。",
        "questions_en": [
            "Which strings, docs, and workflows need synchronized translation and which can remain upstream-only?",
            "How do you keep terminology consistent across hub pages, guides, and detail pages?",
            "Where does localization impact navigation and workflow clarity rather than only text replacement?",
        ],
        "questions_zh": [
            "哪些字符串、文档和流程需要同步翻译，哪些可以保持只在上游维护？",
            "如何让 hub、指南和详情页之间的术语保持一致？",
            "本地化除了替换文字，还会在哪些地方影响导航和工作流理解？",
        ],
        "focus_en": [
            "Terminology consistency for modes, tools, runbooks, and multi-step workflows.",
            "What content should be mirrored, summarized, or intentionally left linked to upstream.",
            "The maintenance cost of multilingual branches and how to keep update workflows realistic.",
            "How translation choices change the usability of menus, hubs, and breadcrumb language.",
        ],
        "focus_zh": [
            "模式、工具、runbook 和多步骤流程的术语一致性。",
            "哪些内容适合镜像、摘要，哪些应该明确保留上游链接。",
            "多语言分支的维护成本，以及怎样让更新流程保持现实可执行。",
            "翻译选择如何改变菜单、hub 和面包屑语言的可用性。",
        ],
        "pitfalls_en": [
            "Translating labels but not translating workflow assumptions.",
            "Keeping two language trees alive without a practical update process.",
            "Mixing terminology across sections until navigation loses clarity.",
        ],
        "pitfalls_zh": [
            "只翻译标签，不翻译背后的工作流假设。",
            "没有更新流程却硬维持两棵语言树。",
            "各栏目术语混用，最后把导航本身搞乱。",
        ],
        "related": ["docs", "guides", "config"],
    },
    "mcp": {
        "upstream": "MCP.md",
        "category": "setup",
        "summary_en": "MCP docs explain how external tool and server capabilities are exposed, configured, and constrained inside DeepSeek TUI workflows.",
        "summary_zh": "MCP 文档说明了外部工具和服务器能力，如何在 DeepSeek TUI 工作流里被暴露、配置和约束。",
        "when_en": "Read this when plain model chat is not enough and you need connected tools, structured capabilities, or a clearer mental model for extension boundaries.",
        "when_zh": "当单纯模型对话已经不够，你需要接入工具、结构化能力或更清楚的扩展边界时，就该先看 MCP 文档。",
        "questions_en": [
            "What role does MCP play compared with built-in tools or simple provider settings?",
            "How should you think about trust, permissions, and failure handling when external capabilities are attached?",
            "Which docs should you read next to move from concept to a working MCP setup?",
        ],
        "questions_zh": [
            "相比内建工具或简单的提供方设置，MCP 在这里承担什么角色？",
            "当外部能力接进来后，信任、权限和失败处理该怎么理解？",
            "从概念走到可运行的 MCP 配置，下一步应该接哪些文档？",
        ],
        "focus_en": [
            "Connection model, server definitions, and where MCP belongs in the config surface.",
            "Permission boundaries and operator expectations once tools can act beyond plain text completion.",
            "The difference between adding capability and keeping the workflow understandable and safe.",
            "How MCP concepts connect back to tool surface, runtime, and troubleshooting pages.",
        ],
        "focus_zh": [
            "连接模型、服务定义，以及 MCP 在配置面的真实位置。",
            "当工具能力超出纯文本补全后，权限边界和操作者预期应该如何设定。",
            "“扩能力”和“保持流程可理解、可控”之间的平衡。",
            "MCP 概念如何回连到工具边界、运行时和排错页面。",
        ],
        "pitfalls_en": [
            "Treating MCP as just another config flag instead of a capability boundary.",
            "Adding servers without documenting trust and failure expectations.",
            "Skipping the runtime and troubleshooting implications of new tool access.",
        ],
        "pitfalls_zh": [
            "把 MCP 当成普通配置项，而不是能力边界。",
            "加了服务器却不说明信任模型和失败预期。",
            "只看接入，不看运行时和排错影响。",
        ],
        "related": ["docs", "mcp", "config"],
    },
    "memory": {
        "upstream": "MEMORY.md",
        "category": "usage",
        "summary_en": "Memory docs explain how session continuity, saved context, and longer-running workflows should behave instead of relying on ad hoc repetition.",
        "summary_zh": "记忆文档解释的是会话连续性、已保存上下文和长流程任务应该怎样运作，而不是靠临时重复输入撑起来。",
        "when_en": "Read this when you want DeepSeek TUI to feel consistent across sessions, or when you need to understand what should be remembered, ignored, or reset.",
        "when_zh": "当你希望 DeepSeek TUI 跨会话保持一致，或者你需要搞清楚什么该记住、什么该忽略、什么该重置时，这页最有用。",
        "questions_en": [
            "What kinds of state are worth preserving across sessions and which should stay ephemeral?",
            "How does memory affect trust, review, and reproducibility?",
            "Where do memory expectations connect back to prompts, modes, and config?",
        ],
        "questions_zh": [
            "哪些状态值得跨会话保留，哪些更应该保持临时性？",
            "记忆能力会怎样影响信任、审查和可复现性？",
            "记忆相关预期又会怎样回连到提示词、模式和配置？",
        ],
        "focus_en": [
            "The boundary between useful continuity and stale or misleading context carryover.",
            "How memory should support operator efficiency without hiding state from review.",
            "Reset, override, and audit expectations for longer-lived sessions.",
            "Where memory docs complement config docs rather than replacing them.",
        ],
        "focus_zh": [
            "有用连续性和陈旧误导性上下文延续之间的边界。",
            "记忆如何提升操作者效率，但又不把状态隐藏到无法审查。",
            "更长会话里，重置、覆盖和审计应该如何设计。",
            "记忆文档和配置文档的边界在哪里，它们不是互相替代。",
        ],
        "pitfalls_en": [
            "Assuming memory means the system should remember everything forever.",
            "Ignoring auditability when context persists across sessions.",
            "Confusing config persistence with conversational memory.",
        ],
        "pitfalls_zh": [
            "把记忆理解成“所有内容都应该永久保留”。",
            "忽视跨会话上下文持续存在时的可审计性。",
            "把配置持久化和会话记忆混为一谈。",
        ],
        "related": ["docs", "config", "modes"],
    },
    "modes": {
        "upstream": "MODES.md",
        "category": "usage",
        "summary_en": "Modes docs explain the different interaction styles available in DeepSeek TUI and why mode choice changes prompt flow, tool usage, and review patterns.",
        "summary_zh": "模式文档解释的是 DeepSeek TUI 里不同的交互风格，以及为什么模式选择会改变提示词流、工具使用和审查方式。",
        "when_en": "Read this when the app is installed and connected but you still do not know which workflow style should drive your day-to-day use.",
        "when_zh": "当程序已经装好、也能连通，但你仍然不确定日常该用哪种工作流风格时，模式文档最该先看。",
        "questions_en": [
            "What practical differences separate one mode from another in live work?",
            "How do modes change tool behavior, review expectations, and decision speed?",
            "Which mode should you start with if you are optimizing for safety, speed, or autonomy?",
        ],
        "questions_zh": [
            "在真实工作里，不同模式之间最实际的差异是什么？",
            "模式会怎样改变工具行为、审查预期和决策速度？",
            "如果你优先考虑安全、速度或自主性，应该从哪种模式开始？",
        ],
        "focus_en": [
            "The decision criteria for choosing a mode rather than memorizing labels only.",
            "Where mode behavior intersects with prompts, keybindings, and tool permissions.",
            "What should remain stable across modes and what is intentionally different.",
            "How to change modes without losing a predictable workflow.",
        ],
        "focus_zh": [
            "选择模式的判断标准，而不是只记标签名称。",
            "模式行为和提示词、快捷键、工具权限之间的交叉点。",
            "哪些体验应该跨模式保持稳定，哪些差异是刻意设计的。",
            "怎样切换模式而不丢掉可预测的工作流。",
        ],
        "pitfalls_en": [
            "Treating mode names as self-explanatory without checking workflow trade-offs.",
            "Changing modes while keeping the same review expectations.",
            "Choosing the fastest-looking mode before you understand its control surface.",
        ],
        "pitfalls_zh": [
            "只看模式名字，不核对背后的工作流取舍。",
            "切了模式，却仍然沿用原来的审查预期。",
            "在没理解控制面的前提下，先选看起来最快的模式。",
        ],
        "related": ["docs", "modes", "guides"],
    },
    "operations-runbook": {
        "upstream": "OPERATIONS_RUNBOOK.md",
        "category": "ops",
        "summary_en": "Operations runbook docs describe repeatable operational checks, failure handling, and expected operator responses for day-two maintenance.",
        "summary_zh": "运维手册描述的是可重复的运行检查、故障处理和日常维护中操作者应该做出的响应。",
        "when_en": "Read this when the question is not feature usage but how to operate, recover, inspect, and stabilize the system under real maintenance pressure.",
        "when_zh": "当问题已经不是功能怎么用，而是系统在真实维护压力下该怎样操作、恢复、检查和稳定时，就该先看运维手册。",
        "questions_en": [
            "Which checks should happen before, during, and after operational changes?",
            "How should operators respond when normal workflows become unstable or partially degraded?",
            "Which other docs define the configuration, runtime, or release assumptions behind the runbook?",
        ],
        "questions_zh": [
            "在运行变更前、中、后，分别应该做哪些检查？",
            "当正常工作流开始不稳定或部分退化时，操作者该怎么响应？",
            "运维手册背后的配置、运行时和发布假设，分别由哪些文档定义？",
        ],
        "focus_en": [
            "Checklists, observability touchpoints, and rollback thinking instead of only happy-path flows.",
            "Operational boundaries between routine validation and deeper incident response.",
            "How to keep runbooks short enough to act on while still capturing the real decision points.",
            "Places where runbooks should stay synchronized with release and configuration docs.",
        ],
        "focus_zh": [
            "清单、观测点和回滚思路，而不是只写 happy path。",
            "日常验证和更深层故障响应之间的边界。",
            "怎样让 runbook 足够短、能执行，同时保留真正的决策点。",
            "哪些地方必须和发布文档、配置文档保持同步。",
        ],
        "pitfalls_en": [
            "Writing runbooks as background essays instead of actionable procedures.",
            "Keeping rollback vague while making forward steps very specific.",
            "Letting runbooks drift away from real release and config practice.",
        ],
        "pitfalls_zh": [
            "把 runbook 写成背景说明，而不是可执行步骤。",
            "前进步骤写得很细，回滚却写得很含糊。",
            "让 runbook 与真实发布和配置实践逐渐脱节。",
        ],
        "related": ["docs", "troubleshooting", "config"],
    },
    "release-runbook": {
        "upstream": "RELEASE_RUNBOOK.md",
        "category": "ops",
        "summary_en": "Release runbook docs explain how changes move from implementation to shippable output with checks, sequencing, and rollback awareness.",
        "summary_zh": "发布手册解释的是变更如何从实现走到可交付版本，包括检查、顺序控制和回滚意识。",
        "when_en": "Read this when you need to understand shipping discipline, not just feature behavior—especially if you own versioning, packaging, or release communication.",
        "when_zh": "当你要理解的是发布纪律，而不是单纯功能行为时，这页更关键，尤其适合负责版本、打包或发布沟通的人。",
        "questions_en": [
            "What has to be true before a release is considered ready?",
            "Which checks are release-critical and which are merely useful context?",
            "How should release docs stay aligned with install docs, changelog expectations, and operational follow-up?",
        ],
        "questions_zh": [
            "一个版本要被视为可发布，前提到底有哪些？",
            "哪些检查是发布关键项，哪些只是有帮助的背景信息？",
            "发布文档怎样和安装文档、变更日志预期以及发布后跟进保持一致？",
        ],
        "focus_en": [
            "Release gates, sequencing, and evidence of readiness instead of vague confidence language.",
            "The transition from local success to distributable artifact and public update path.",
            "Rollback and post-release verification as first-class parts of the flow.",
            "Where release docs rely on architecture, config, and install assumptions.",
        ],
        "focus_zh": [
            "发布门槛、步骤顺序和就绪证据，而不是模糊的“感觉可以发了”。",
            "从本地成功过渡到可分发制品和公开更新路径。",
            "把回滚和发布后验证当作流程中的一等公民。",
            "发布文档依赖哪些架构、配置和安装前提。",
        ],
        "pitfalls_en": [
            "Treating release as packaging only, with no operator validation path.",
            "Skipping rollback documentation because the release seems small.",
            "Letting release notes and install expectations drift apart.",
        ],
        "pitfalls_zh": [
            "把发布只当成打包，不给操作者留验证路径。",
            "觉得版本小就省略回滚说明。",
            "让发布说明和安装预期逐渐脱节。",
        ],
        "related": ["docs", "install", "troubleshooting"],
    },
    "runtime-api": {
        "upstream": "RUNTIME_API.md",
        "category": "usage",
        "summary_en": "Runtime API docs explain how deeper programmatic control or integration hooks fit around the normal interactive CLI flow.",
        "summary_zh": "运行时 API 文档解释的是更深层的程序化控制或集成钩子，如何围绕普通交互式 CLI 流程工作。",
        "when_en": "Read this when you are moving from direct terminal usage into automation, embedding, or integration-aware workflows.",
        "when_zh": "当你开始从直接终端使用，转向自动化、嵌入式使用或集成式工作流时，这页就该优先看。",
        "questions_en": [
            "What can be controlled programmatically that is not obvious from the terminal UI alone?",
            "Where does the runtime API sit relative to config, prompts, tools, and modes?",
            "How should integration behavior be validated so it matches the interactive experience closely enough?",
        ],
        "questions_zh": [
            "有哪些能力可以通过程序控制，而单看终端 UI 并不明显？",
            "运行时 API 相比配置、提示词、工具和模式，处在什么位置？",
            "怎样验证集成行为，才能让它和交互式体验足够一致？",
        ],
        "focus_en": [
            "Lifecycle boundaries between setup, live runtime state, and external callers.",
            "What the runtime API should expose versus what should remain internal implementation detail.",
            "Integration expectations around errors, retries, and tool invocation side effects.",
            "How runtime API docs should connect back to tool surface and modes docs.",
        ],
        "focus_zh": [
            "初始化、运行时状态和外部调用者之间的生命周期边界。",
            "哪些东西应该暴露给运行时 API，哪些仍应保留为内部实现细节。",
            "错误、重试和工具调用副作用方面的集成预期。",
            "运行时 API 文档如何和工具边界、模式文档互相回连。",
        ],
        "pitfalls_en": [
            "Assuming interactive UI behavior automatically translates into API guarantees.",
            "Skipping error-model reading and focusing only on the success path.",
            "Embedding runtime control without checking tool or permission implications.",
        ],
        "pitfalls_zh": [
            "以为交互 UI 的行为自然就等于 API 保证。",
            "只看成功路径，不看错误模型。",
            "做运行时集成时忽略工具权限和副作用。",
        ],
        "related": ["docs", "config", "guides"],
    },
    "subagents": {
        "upstream": "SUBAGENTS.md",
        "category": "usage",
        "summary_en": "Subagents docs explain how work can be delegated, partitioned, and recomposed when one agent loop is no longer enough.",
        "summary_zh": "子代理文档解释的是，当单一代理循环不够时，工作如何被拆分、委派并重新合并。",
        "when_en": "Read this when tasks become parallel, multi-step, or too context-heavy for a single uninterrupted interaction loop.",
        "when_zh": "当任务开始变成并行、多步骤，或者上下文重到单一交互循环撑不住时，就该看子代理文档。",
        "questions_en": [
            "What kinds of work should be delegated to subagents and what should stay local?",
            "How do you preserve ownership, context, and integration quality across multiple agent threads?",
            "Which failure modes appear once work is split into parallel or semi-independent branches?",
        ],
        "questions_zh": [
            "哪些工作适合交给子代理，哪些更应该留在主流程里？",
            "当任务分到多个代理线程后，怎样保住所有权、上下文和集成质量？",
            "工作一旦拆成并行或半独立分支，会出现哪些新的失败模式？",
        ],
        "focus_en": [
            "Delegation criteria, write ownership, and synchronization boundaries.",
            "How subagents affect latency, coordination overhead, and review requirements.",
            "When a multi-agent pattern clarifies work and when it only hides confusion.",
            "How subagent docs connect back to modes, tool surface, and coordinator prompt material.",
        ],
        "focus_zh": [
            "委派标准、写入所有权和同步边界。",
            "子代理如何影响延迟、协调成本和审查要求。",
            "什么时候多代理能让工作更清晰，什么时候只是把混乱藏起来。",
            "子代理文档怎样回连到模式、工具边界和协调器提示词。",
        ],
        "pitfalls_en": [
            "Delegating work that is actually on the critical path right now.",
            "Splitting tasks without a clear ownership boundary.",
            "Assuming more agents automatically means better throughput.",
        ],
        "pitfalls_zh": [
            "把当前关键路径上的事情直接委派出去。",
            "拆任务时不先定义清楚所有权边界。",
            "以为代理越多，吞吐就一定越高。",
        ],
        "related": ["docs", "modes", "guides"],
    },
    "tool-surface": {
        "upstream": "TOOL_SURFACE.md",
        "category": "usage",
        "summary_en": "Tool surface docs define what DeepSeek TUI can act on, what requires approval, and what should remain outside the agent boundary.",
        "summary_zh": "工具边界文档定义的是 DeepSeek TUI 能对什么动手、什么需要审批，以及哪些事情本来就应该留在代理边界之外。",
        "when_en": "Read this when you need to understand practical action limits, approval rules, or why one workflow can execute changes while another only explains them.",
        "when_zh": "当你需要理解实际行动边界、审批规则，或者为什么某条工作流能执行变更而另一条只能解释时，这页最关键。",
        "questions_en": [
            "Which tools are exposed and what kinds of actions do they enable?",
            "Where are the safety boundaries between read, write, network, and escalated actions?",
            "How should users choose between tool power and review control?",
        ],
        "questions_zh": [
            "哪些工具被暴露出来，它们分别能启用什么动作？",
            "读、写、联网和提权动作之间的安全边界在哪里？",
            "用户应该怎样在工具能力和审查控制之间取舍？",
        ],
        "focus_en": [
            "Capability boundaries instead of only tool names.",
            "Approval flow, sandbox expectations, and what still needs human confirmation.",
            "How tool surface assumptions influence modes, subagents, and runbook design.",
            "The difference between available capability and recommended workflow.",
        ],
        "focus_zh": [
            "关注能力边界，而不只是工具名称。",
            "审批流程、沙箱预期，以及哪些动作仍然需要人工确认。",
            "工具边界假设如何影响模式、子代理和 runbook 设计。",
            "“工具可用”与“工作流推荐”之间的差异。",
        ],
        "pitfalls_en": [
            "Reading the tool list without understanding the approval model.",
            "Confusing availability with permission to use in every context.",
            "Skipping the workflow implications of a stronger tool surface.",
        ],
        "pitfalls_zh": [
            "只看工具列表，不理解审批模型。",
            "把“可用”误解成“任何场景都默认允许”。",
            "忽略工具能力增强后对工作流本身的影响。",
        ],
        "related": ["docs", "guides", "modes"],
    },
    "v0-7-5-implementation-plan": {
        "upstream": "V0_7_5_IMPLEMENTATION_PLAN.md",
        "category": "history",
        "summary_en": "The v0.7.5 implementation plan records how a specific feature set was intended to be delivered, which is useful for historical design context and roadmap archaeology.",
        "summary_zh": "v0.7.5 实现计划记录的是某一批功能原本计划如何落地，因此更适合用来理解历史设计语境和路线图演化。",
        "when_en": "Read this when you want to understand why the project looks the way it does now, or which earlier assumptions shaped later architecture and workflow choices.",
        "when_zh": "当你想理解项目为什么长成今天这样，或者早期哪些假设塑造了后来的架构和工作流选择时，这页会更有用。",
        "questions_en": [
            "What did the project intend to build at that moment and what actually shipped later?",
            "Which ideas from the plan still explain current structure or naming?",
            "How should historical planning docs inform present decisions without dominating them?",
        ],
        "questions_zh": [
            "那个时间点项目原本想做什么，后来实际交付了什么？",
            "计划里的哪些想法今天仍然解释得通当前结构或命名？",
            "历史规划文档该如何影响今天的判断，而不是反过来绑住当前决策？",
        ],
        "focus_en": [
            "Intent, scope, and sequencing rather than treating the plan as final truth.",
            "What assumptions still survived into current architecture or modes.",
            "The gap between planned milestones and live behavior.",
            "How to cross-check historical plans against release and operations docs.",
        ],
        "focus_zh": [
            "先看意图、范围和顺序，而不是把计划当成最终事实。",
            "哪些假设后来真的延续到了现在的架构或模式里。",
            "计划里写的里程碑和当前真实行为之间的差距。",
            "怎样把历史计划和发布、运维文档互相对照。",
        ],
        "pitfalls_en": [
            "Reading historical plans as if they are still the current roadmap.",
            "Ignoring what later runbooks and releases reveal about actual outcomes.",
            "Using old plan terminology without checking if the product moved on.",
        ],
        "pitfalls_zh": [
            "把历史计划当成今天仍然有效的路线图。",
            "不看后续 runbook 和发布记录，就直接假设结果和计划一致。",
            "直接沿用旧计划术语，而不核对产品是否早已变化。",
        ],
        "related": ["docs", "guides", "troubleshooting"],
    },
    "capacity-controller": {
        "upstream": "capacity_controller.md",
        "category": "architecture",
        "summary_en": "Capacity controller docs explain how advanced orchestration keeps workload, delegation, or concurrency from outgrowing the operator’s control surface.",
        "summary_zh": "容量控制器文档解释的是高级编排如何防止工作量、委派或并发超出操作者的控制面。",
        "when_en": "Read this when you need to reason about throttling, backpressure, or why orchestration logic does not simply fan out work without limits.",
        "when_zh": "当你需要理解限流、背压，或者为什么编排逻辑不会无限扩散任务时，这页就很关键。",
        "questions_en": [
            "What problem does capacity control solve inside a multi-step agent workflow?",
            "How does it relate to coordination, subagents, and runtime decision quality?",
            "What should operators expect when capacity rules constrain throughput or delegation?",
        ],
        "questions_zh": [
            "在多步骤代理工作流里，容量控制到底解决什么问题？",
            "它和协调、子代理、运行时决策质量之间有什么关系？",
            "当容量规则开始限制吞吐或委派时，操作者应该预期看到什么？",
        ],
        "focus_en": [
            "Protection of review quality, not only raw throughput control.",
            "How capacity interacts with delegation and coordination prompts.",
            "When a limit is a safety feature versus when it becomes a usability issue.",
            "Which adjacent docs define the runtime and orchestration assumptions behind it.",
        ],
        "focus_zh": [
            "它保护的是审查质量，而不只是限制吞吐。",
            "容量控制如何和委派逻辑、协调提示词联动。",
            "什么时候限制是安全特性，什么时候反而成了可用性问题。",
            "哪些相邻文档定义了它背后的运行时和编排假设。",
        ],
        "pitfalls_en": [
            "Treating capacity as only a performance knob.",
            "Ignoring the operator-review reason behind throughput limits.",
            "Changing coordination behavior without checking capacity assumptions.",
        ],
        "pitfalls_zh": [
            "把容量控制只当成性能旋钮。",
            "忽略吞吐限制背后的操作者审查原因。",
            "改协调逻辑时不核对容量控制假设。",
        ],
        "related": ["docs", "modes", "mcp"],
    },
    "v0-8-8-coordinator-prompt": {
        "upstream": "v0.8.8-coordinator-prompt.md",
        "category": "architecture",
        "summary_en": "The v0.8.8 coordinator prompt doc explains how orchestration behavior was shaped at a specific version and why the coordinator’s instructions matter to agent outcomes.",
        "summary_zh": "v0.8.8 协调器提示词文档说明了某个版本里编排行为是怎样被塑造的，以及协调器指令为什么会直接影响代理结果。",
        "when_en": "Read this when you are debugging orchestration quality, delegation behavior, or the difference between tool capability and prompt-governed behavior.",
        "when_zh": "当你在排查编排质量、委派行为，或者想区分“工具能力”和“提示词治理行为”时，这页很值得看。",
        "questions_en": [
            "What did the coordinator prompt instruct the system to prioritize at that version?",
            "How does coordinator behavior shape delegation, sequencing, and review quality?",
            "Which later docs should you check to see whether these prompt assumptions are still current?",
        ],
        "questions_zh": [
            "在那个版本里，协调器提示词要求系统优先考虑什么？",
            "协调器行为怎样影响委派、顺序控制和审查质量？",
            "如果要判断这些提示词假设今天是否还有效，接下来该看哪些文档？",
        ],
        "focus_en": [
            "Prompt-governed behavior rather than raw capability lists.",
            "Where coordination policy lives relative to modes, subagents, and capacity control.",
            "Version-specific assumptions that should not be generalized blindly.",
            "The link between coordinator prompt changes and user-visible workflow differences.",
        ],
        "focus_zh": [
            "关注的是提示词治理行为，而不是原始能力列表。",
            "协调策略相对模式、子代理和容量控制所处的位置。",
            "哪些版本特定假设不能盲目泛化。",
            "协调器提示词变化如何传导成用户可见的工作流差异。",
        ],
        "pitfalls_en": [
            "Confusing prompt policy with hard runtime guarantees.",
            "Applying version-specific coordinator assumptions to every later release.",
            "Changing orchestration without checking adjacent mode or subagent docs.",
        ],
        "pitfalls_zh": [
            "把提示词策略误认为硬性的运行时保证。",
            "把版本特定的协调器假设套用到所有后续版本。",
            "修改编排逻辑时不去核对模式或子代理文档。",
        ],
        "related": ["docs", "modes", "mcp"],
    },
}

RELATED_LINKS = {
    "docs": {
        "en": ("Docs hub", "/docs/index.html"),
        "zh": ("文档总页", "/zh/docs/index.html"),
    },
    "guides": {
        "en": ("Guides hub", "/guides/index.html"),
        "zh": ("指南总页", "/zh/guides/index.html"),
    },
    "troubleshooting": {
        "en": ("Troubleshooting hub", "/troubleshooting/index.html"),
        "zh": ("排错总页", "/zh/troubleshooting/index.html"),
    },
    "install": {
        "en": ("Install hub", "/install/index.html"),
        "zh": ("安装总页", "/zh/install/index.html"),
    },
    "config": {
        "en": ("Config hub", "/config/index.html"),
        "zh": ("配置总页", "/zh/config/index.html"),
    },
    "modes": {
        "en": ("Modes hub", "/modes/index.html"),
        "zh": ("模式总页", "/zh/modes/index.html"),
    },
    "mcp": {
        "en": ("MCP hub", "/mcp/index.html"),
        "zh": ("MCP 总页", "/zh/mcp/index.html"),
    },
    "comparisons": {
        "en": ("Comparisons hub", "/comparisons/index.html"),
        "zh": ("对比总页", "/zh/comparisons/index.html"),
    },
}

CATEGORY_READ_ORDER = {
    "setup": {
        "en": [
            ("Confirm the environment first", "Verify the platform, shell, package route, and credentials assumptions before you edit deeper settings."),
            ("Map the doc to your exact path", "Separate official install or config steps from provider-specific and environment-specific overrides."),
            ("Validate with live checks", "Finish by testing the real binary, active config, and first successful request path."),
        ],
        "zh": [
            ("先确认环境前提", "先核对平台、shell、安装路线和凭据假设，再去改更深层设置。"),
            ("把文档对应到你的具体路径", "把官方安装或配置步骤，和提供方、环境特定的覆盖逻辑分开看。"),
            ("最后做真实验证", "收尾时一定验证当前二进制、激活配置和第一次成功请求路径。"),
        ],
    },
    "usage": {
        "en": [
            ("Anchor the workflow question", "Decide whether your blocker is navigation, modes, memory, tools, or operator review speed."),
            ("Read the behavior, not only the labels", "Focus on how the feature changes day-to-day flow instead of memorizing names alone."),
            ("Return to the right hub next", "After the upstream topic is clear, jump back into guides, modes, or config to keep the workflow coherent."),
        ],
        "zh": [
            ("先锁定工作流问题", "先判断你当前的卡点更偏导航、模式、记忆、工具还是审查效率。"),
            ("看行为，不只看标签", "重点理解这个主题如何改变日常流程，而不是只记名称。"),
            ("再回到正确 hub", "上游主题看清后，再回到 guides、modes 或 config，把整条工作流串起来。"),
        ],
    },
    "architecture": {
        "en": [
            ("Identify the boundary", "Start by locating which subsystem or policy this doc is actually describing."),
            ("Connect it to runtime behavior", "Ask how the documented structure shows up in live orchestration, prompts, tools, or panes."),
            ("Cross-check adjacent policies", "Finish by reading the linked modes, MCP, or config pages so the architecture context stays grounded."),
        ],
        "zh": [
            ("先找到边界", "先定位这份文档描述的到底是哪一个子系统或策略边界。"),
            ("把它接回运行时行为", "继续问：这套结构在真实编排、提示词、工具或面板里怎么体现。"),
            ("再核对相邻策略", "最后补看 modes、MCP 或 config，避免架构理解悬空。"),
        ],
    },
    "ops": {
        "en": [
            ("Start from the operator trigger", "Frame the runbook around the change, failure, or release event that brings you here."),
            ("Look for checks and reversibility", "Highlight the points where validation, rollback, and evidence matter most."),
            ("Tie the procedure back to live state", "Make sure the documented steps still match current install, config, and runtime behavior."),
        ],
        "zh": [
            ("先从操作者触发点出发", "围绕把你带到这页的变更、故障或发布事件来理解 runbook。"),
            ("重点看检查和可逆性", "标出最需要验证、回滚和留证据的地方。"),
            ("再接回当前实际状态", "确保文档步骤仍然和现在的安装、配置、运行时行为一致。"),
        ],
    },
    "history": {
        "en": [
            ("Lock the version context", "Read the document as a snapshot of a moment, not as a timeless truth."),
            ("Separate lasting ideas from old assumptions", "Keep the concepts that still explain current structure, and discard what only fit the historical moment."),
            ("Compare against current docs", "Use live architecture, runbook, and feature docs to decide what still matters today."),
        ],
        "zh": [
            ("先锁定版本语境", "把这份文档当成某个时点的快照，而不是永远成立的真理。"),
            ("把长期有效的想法和旧假设分开", "保留今天仍能解释结构的部分，丢掉只适用于历史时点的内容。"),
            ("再对照当前文档", "拿现在的架构、runbook 和功能文档来判断它今天还值不值得信。"),
        ],
    },
}


def replace_once(text: str, pattern: str, repl: str) -> str:
    return re.sub(pattern, repl, text, count=1, flags=re.S)


def render_list(items: list[str]) -> str:
    return "".join(f"<li>{html.escape(item)}</li>" for item in items)


def render_cards(cards: list[tuple[str, str]]) -> str:
    return "".join(
        f'<article class="content-card"><span class="tag">Step {index}</span><h3>{html.escape(title)}</h3><p>{html.escape(body)}</p></article>'
        for index, (title, body) in enumerate(cards, start=1)
    )


def render_cards_zh(cards: list[tuple[str, str]]) -> str:
    return "".join(
        f'<article class="content-card"><span class="tag">步骤 {index}</span><h3>{html.escape(title)}</h3><p>{html.escape(body)}</p></article>'
        for index, (title, body) in enumerate(cards, start=1)
    )


def render_links(link_keys: list[str], zh: bool) -> str:
    lang_key = "zh" if zh else "en"
    return "".join(
        f'<a href="{RELATED_LINKS[key][lang_key][1]}">{html.escape(RELATED_LINKS[key][lang_key][0])}</a>'
        for key in link_keys
    )


def build_title_desc(slug: str, zh: bool) -> tuple[str, str]:
    label = DOC_LABELS_ZH[slug] if zh else DOC_LABELS_EN[slug]
    if zh:
        title = f"DeepSeek TUI {label}指南"
        desc = f"查看 {label} 的覆盖范围、阅读顺序、重点检查项、常见误区，以及下一步该接哪条 DeepSeek TUI 页面。"
    else:
        title = f"DeepSeek TUI {label} Guide"
        desc = f"See what {label.lower()} cover, when to read them, what to verify, common mistakes, and which DeepSeek TUI pages to open next."
    return title, desc


def build_main(slug: str, zh: bool) -> str:
    topic = TOPIC_DATA[slug]
    label = DOC_LABELS_ZH[slug] if zh else DOC_LABELS_EN[slug]
    title, _ = build_title_desc(slug, zh)
    cards = CATEGORY_READ_ORDER[topic["category"]]["zh" if zh else "en"]
    cards_html = render_cards_zh(cards) if zh else render_cards(cards)
    links_html = render_links(topic["related"], zh)
    detail_pack = CATEGORY_DETAILS[topic["category"]]["zh" if zh else "en"]
    concrete_cards = "".join(
        f'<article class="content-card"><h3>{"具体点" if zh else "Specific detail"} {index}</h3><p>{html.escape(item)}</p></article>'
        for index, item in enumerate(detail_pack["concrete"], start=1)
    )
    workflow_list = render_list(detail_pack["workflow"])
    mirror_head = "为什么这批页面之前看起来不像原文镜像" if zh else "Why these pages did not look like raw doc mirrors before"
    mirror_text = (
        "这批 docs 详情页最初是按“阅读路线图”来做的：先告诉用户这份文档为什么值得看、该先看哪部分、看完回站内哪条分支继续走。所以它们一开始更像导读页，而不是完整镜像页。现在这层已经在补强，会逐步往“直接在站内读具体内容”的方向收。"
        if zh else
        "These docs detail pages were originally built as reading maps first: they explained why a repo doc mattered, which parts deserved attention first, and which branch of the site should take over next. That made them navigable, but also lighter than a true doc mirror. This layer is now being strengthened so the pages carry more concrete document content directly on-site."
    )
    if zh:
        questions = render_list(topic["questions_zh"])
        focus = render_list(topic["focus_zh"])
        pitfalls = render_list(topic["pitfalls_zh"])
        return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">文档详情</span><h1>{html.escape(title)}</h1><p>{html.escape(topic["summary_zh"])}</p><div class="hero-points"><span>上游源文件：{html.escape(topic["upstream"])}</span><span>适合按主题阅读</span><span>可回连到站内 hub</span></div></div><aside class="answer-card"><span class="panel-kicker">最快用法</span><h2>先把这页当成 {html.escape(label)} 的阅读路线图，而不是仓库文档清单。</h2><p>{html.escape(topic["when_zh"])}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>这份文档真正覆盖什么</h2><p>{html.escape(topic["summary_zh"])}</p><h2>这页能直接回答的问题</h2><ul>{questions}</ul><h2>读上游文档时最该盯住的部分</h2><ul>{focus}</ul><h2>最常见的误区</h2><ul>{pitfalls}</ul></article><aside class="panel-card"><span class="panel-kicker">阅读顺序</span><div class="link-stack">{links_html}</div></aside></div></section><section class="section section-alt"><div class="container"><div class="section-head"><h2>这份上游文档里应该真正拿到的具体内容</h2><p>{html.escape(mirror_text)}</p></div><div class="card-grid card-grid-2">{concrete_cards}</div></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>把文档转成你自己工作流时该保留什么</h2><ul>{workflow_list}</ul><h2>{mirror_head}</h2><p>{html.escape(mirror_text)}</p></article><aside class="panel-card"><span class="panel-kicker">上游阅读提示</span><div class="link-stack">{links_html}</div></aside></div></section><section class="section section-alt"><div class="container"><div class="section-head"><h2>推荐阅读顺序</h2><p>先按问题类型读，再决定要不要切回安装、配置、模式、MCP 或排错分支。</p></div><div class="card-grid card-grid-3">{cards_html}</div></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>这页在站内结构里的位置</h2><p>这批 docs 详情页的作用，不是简单复述上游 Markdown，而是帮你更快判断：这份文档为什么值得看、先看哪几段、看完之后要回站内哪条主线继续走。对于 DeepSeek TUI 这种同时覆盖安装、配置、模式、工具和运维的项目，这种按问题分流的正文结构，会比“仓库原样镜像”更容易用。</p><h2>什么时候应该离开这页</h2><p>如果你已经明确自己接下来要改配置、切模式、接 MCP、排查问题，或者进入更具体的使用指南，就不要停留在 docs 详情页本身。它最有价值的时候，是帮你建立主题边界和阅读顺序，而不是替代所有后续操作页。</p></article><aside class="panel-card"><span class="panel-kicker">下一步</span><div class="link-stack">{links_html}</div></aside></div></section></main>"""
    questions = render_list(topic["questions_en"])
    focus = render_list(topic["focus_en"])
    pitfalls = render_list(topic["pitfalls_en"])
    return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">Docs Detail</span><h1>{html.escape(title)}</h1><p>{html.escape(topic["summary_en"])}</p><div class="hero-points"><span>Upstream source: {html.escape(topic["upstream"])}</span><span>Best read by intent</span><span>Routes back into site hubs</span></div></div><aside class="answer-card"><span class="panel-kicker">Best Use</span><h2>Treat this page as the reading map for {html.escape(label)}, not as a raw repo mirror.</h2><p>{html.escape(topic["when_en"])}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>What this document actually covers</h2><p>{html.escape(topic["summary_en"])}</p><h2>Questions this page should answer fast</h2><ul>{questions}</ul><h2>What to focus on inside the upstream doc</h2><ul>{focus}</ul><h2>Common mistakes</h2><ul>{pitfalls}</ul></article><aside class="panel-card"><span class="panel-kicker">Read next</span><div class="link-stack">{links_html}</div></aside></div></section><section class="section section-alt"><div class="container"><div class="section-head"><h2>Concrete details you should actually pull out of the upstream doc</h2><p>{html.escape(mirror_text)}</p></div><div class="card-grid card-grid-2">{concrete_cards}</div></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>What to carry from the doc into your own workflow</h2><ul>{workflow_list}</ul><h2>{mirror_head}</h2><p>{html.escape(mirror_text)}</p></article><aside class="panel-card"><span class="panel-kicker">Upstream reading tips</span><div class="link-stack">{links_html}</div></aside></div></section><section class="section section-alt"><div class="container"><div class="section-head"><h2>Recommended reading order</h2><p>Read by problem type first, then branch back into install, config, modes, MCP, or troubleshooting only when the next step is clear.</p></div><div class="card-grid card-grid-3">{cards_html}</div></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>Where this page sits in the site</h2><p>These docs detail pages are not just repo mirrors. Their job is to tell you why a topic matters, which parts deserve attention first, and which branch of the site should take over once the document boundary is clear. For a project that spans install, configuration, modes, tools, and operator workflows, that route-first structure is more useful than a flat Markdown mirror.</p><h2>When to leave this page</h2><p>Once you know whether the next action belongs in install, config, modes, MCP, troubleshooting, or hands-on guides, move there quickly. The detail page is most useful when it gives you a sharper reading order and a better mental boundary for the topic, not when it tries to absorb every downstream action page.</p></article><aside class="panel-card"><span class="panel-kicker">Next pages</span><div class="link-stack">{links_html}</div></aside></div></section></main>"""


def process(path: Path) -> None:
    rel = path.relative_to(ROOT)
    zh = rel.parts[0] == "zh"
    parts = rel.parts[1:] if zh else rel.parts
    if len(parts) != 3 or parts[0] != "docs" or parts[2] != "index.html" or parts[1] == "index":
        return
    slug = parts[1]
    if slug not in TOPIC_DATA:
        return
    text = path.read_text(encoding="utf-8")
    title, desc = build_title_desc(slug, zh)
    text = replace_once(text, r"<title>.*?</title>", f"<title>{html.escape(title)}</title>")
    text = replace_once(text, r'<meta name="description" content=".*?">', f'<meta name="description" content="{html.escape(desc)}">')
    text = replace_once(text, r'<meta property="og:title" content=".*?">', f'<meta property="og:title" content="{html.escape(title)}">')
    text = replace_once(text, r'<meta property="og:description" content=".*?">', f'<meta property="og:description" content="{html.escape(desc)}">')
    text = replace_once(text, r'<meta name="twitter:title" content=".*?">', f'<meta name="twitter:title" content="{html.escape(title)}">')
    text = replace_once(text, r'<meta name="twitter:description" content=".*?">', f'<meta name="twitter:description" content="{html.escape(desc)}">')
    text = replace_once(text, r'"headline": ".*?"', f'"headline": "{html.escape(title)}"')
    text = replace_once(text, r'"name": ".*?"', f'"name": "{html.escape(title)}"')
    text = replace_once(text, r'"description": ".*?"', f'"description": "{html.escape(desc)}"')
    text = replace_once(text, r"<main>.*?</main>", build_main(slug, zh))
    path.write_text(text, encoding="utf-8")


def main() -> None:
    for path in ROOT.rglob("index.html"):
        process(path)


if __name__ == "__main__":
    main()
