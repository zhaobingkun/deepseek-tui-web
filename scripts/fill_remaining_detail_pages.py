from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path("/Users/zhaobingkun/dev/DeepSeek-TUI")


PAGES = {
    ("guides", "pricing-and-cost"): {
        "en": {
            "eyebrow": "Pricing Guide",
            "h1": "DeepSeek TUI pricing only makes sense once you split terminal access from provider billing",
            "intro": "Most people who search for DeepSeek TUI pricing are not really asking about a subscription page. They are trying to understand where the money goes in practice: whether the terminal client itself is paid, whether the provider behind it charges per request, and how model choice changes ongoing cost.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Treat DeepSeek TUI cost as a stack: local client, provider account, model usage, and your own workflow habits.",
            "answer_p": "If you mix those layers together, you will misread nearly every pricing discussion. The terminal app may be easy to install, but your real bill often comes from the provider and from how aggressively you use higher-cost models.",
            "questions": [
                "Is the thing you are paying for the terminal tool, the model provider, or both?",
                "How does the cost change when you switch provider or model tier?",
                "What workflow choices quietly make the bill larger even if pricing tables look stable?",
            ],
            "coverage": "This page should help a reader separate tool access from model spend, identify the provider path currently active in their setup, and estimate which habits actually move the cost needle.",
            "diagnosis": [
                ("Tool access question", "Ask whether you are paying for the DeepSeek TUI wrapper itself or just using it as a local client over a billed provider connection."),
                ("Provider billing question", "Check whether your active provider bills by token, model family, request class, or team plan instead of assuming every backend behaves like the same SaaS product."),
                ("Usage pattern question", "Look at how often you use long contexts, heavy reasoning modes, or repeated retries, because those are often bigger cost drivers than the interface choice."),
            ],
            "workflow": [
                ("Identify the active provider first", "Open your config and confirm which backend is actually live. Pricing research is meaningless if you are comparing the wrong provider."),
                ("Map the provider to the model you really use", "A cheap provider route can still become expensive if your default model is the heavier tier and you leave long-running sessions open."),
                ("Check whether your workflow multiplies spend", "Repeated re-runs, overlong contexts, and unbounded experimentation with higher-cost models can matter more than the base price table."),
                ("Only then compare alternatives", "After you know your current provider-model-workflow combination, compare it against another provider or another model family."),
            ],
            "mistakes": [
                "Treating the terminal app and the model bill as if they were one product with one price.",
                "Comparing providers without first confirming which model ID is actually active in your config.",
                "Ignoring workflow habits like repeated retries and oversized contexts when estimating practical cost.",
            ],
            "leave": "Leave this page once you know which provider and model combination you are using now, what part of the stack creates the real bill, and which config page you need next to change that path safely.",
            "links": [
                ("Provider setup", "/config/provider-setup/index.html"),
                ("API key setup", "/config/api-key/index.html"),
                ("Environment variables", "/config/environment-variables/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "价格指南",
            "h1": "只有把终端客户端和 provider 计费拆开看，DeepSeek TUI 的“价格”问题才会讲清楚",
            "intro": "大多数搜索 DeepSeek TUI 价格的人，并不是在找一个简单的订阅页。他们真正想知道的是：到底是终端工具本身收费，还是背后的 provider 收费，以及模型选择会怎样影响长期使用成本。",
            "answer_kicker": "直接答案",
            "answer_h2": "看 DeepSeek TUI 成本时，要把它拆成几层：本地客户端、provider 账号、模型使用量，以及你自己的使用习惯。",
            "answer_p": "如果把这些层混在一起看，几乎所有价格讨论都会被你误读。终端工具本身可能很容易安装，但真正产生费用的，往往是 provider 和你对高成本模型的使用方式。",
            "questions": [
                "你付的钱到底是终端工具本身，还是后面的模型 provider，还是两者都有？",
                "切换 provider 或模型档位后，费用会怎么变？",
                "哪些使用习惯会在价格表看起来差不多时，把实际账单悄悄拉高？",
            ],
            "coverage": "这页要帮用户把工具访问成本和模型调用成本分开，看清当前启用的是哪条 provider 路线，并判断真正影响花费的环节在哪里。",
            "diagnosis": [
                ("工具访问层", "先判断你付费的是不是 DeepSeek TUI 这个终端壳，还是它只是一个连接到付费 provider 的本地客户端。"),
                ("Provider 计费层", "确认当前 provider 是按 token、按模型等级、按请求类型，还是按团队计划收费，不要默认所有后端都一样。"),
                ("使用模式层", "检查自己是否常开长上下文、重度 reasoning 模式、或频繁重试，因为这些习惯往往比页面上的基础价格更影响实际支出。"),
            ],
            "workflow": [
                ("先确认当前实际 provider", "打开配置文件，确认当前真正生效的是哪一个 backend。provider 看错了，后面所有价格比较都没有意义。"),
                ("再确认当前真正用的模型", "看清楚默认模型到底是哪一档。provider 看起来便宜，不代表你当前模型路线也便宜。"),
                ("检查自己的使用习惯", "长上下文、频繁重跑、重度模型试验，往往比基础定价更容易推高实际账单。"),
                ("最后才做横向比较", "先弄清自己当前这一套 provider + model + workflow 的成本，再去和其他路线对比。"),
            ],
            "mistakes": [
                "把终端工具和模型计费当成一个产品、一个价格去理解。",
                "还没确认当前生效模型，就开始比较 provider 价格。",
                "忽略长上下文、反复重试等实际习惯，只盯着价格表看。",
            ],
            "leave": "当你已经知道当前用的是哪条 provider 路线、真正产生费用的是哪一层，以及下一步该去哪个配置页改 provider 或模型时，就可以离开这页了。",
            "links": [
                ("Provider 设置", "/zh/config/provider-setup/index.html"),
                ("API Key 设置", "/zh/config/api-key/index.html"),
                ("环境变量", "/zh/config/environment-variables/index.html"),
            ],
        },
    },
    ("skills", "examples"): {
        "en": {
            "eyebrow": "Skills Examples",
            "h1": "DeepSeek TUI skills examples should show repeatable workflow design, not just clever prompt text",
            "intro": "A useful skills example is not a decorative snippet. It should show what kind of repeated task deserves its own structure, what the skill boundary is, and what problem gets easier after the skill exists.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "A strong skills example turns a repeated workflow into a reusable operating pattern.",
            "answer_p": "If the example only looks like a nice paragraph of instruction text, it is probably still just a prompt. A skill becomes valuable when it preserves scope, ordering, defaults, and decision boundaries across sessions.",
            "questions": [
                "What makes an example feel like a real skill rather than a fancy prompt?",
                "Which repeated workflows deserve a dedicated skill first?",
                "How do examples help you decide what to extract and what to leave as normal chat context?",
            ],
            "coverage": "This page should help the reader spot reusable patterns, understand the anatomy of a good skills example, and decide when to keep a workflow as normal prompting instead.",
            "diagnosis": [
                ("Repeated task", "A good example starts from work that returns often enough to justify structure."),
                ("Stable boundary", "The workflow should have a clear scope: what the skill does, what it does not do, and what inputs it expects."),
                ("Reusable defaults", "The example should save time by encoding common assumptions, next steps, or checks that would otherwise be rewritten each time."),
            ],
            "workflow": [
                ("Start from repetition, not from elegance", "Do not create a skill because the wording sounds impressive. Create it because the same workflow keeps returning."),
                ("Define the boundary clearly", "A skill example becomes useful when a future session can tell where the skill starts, where it stops, and what remains human judgment."),
                ("Show what becomes easier", "The best examples make one thing obviously cheaper: setup time, consistency, error checking, or context reuse."),
                ("Keep the example close to real work", "Examples should look like something you would actually call from a terminal coding workflow, not like generic AI inspiration text."),
            ],
            "mistakes": [
                "Calling any long prompt a skill even when it has no stable workflow boundary.",
                "Writing examples that sound polished but do not save repeated work.",
                "Forgetting to show why the example matters in a real terminal agent session.",
            ],
            "leave": "Leave this page once you can look at a repeated task and decide whether it deserves a reusable skill or should remain a one-off prompt.",
            "links": [
                ("Skills vs prompts", "/skills/vs-prompts/index.html"),
                ("Skills hub", "/skills/index.html"),
                ("MCP setup", "/mcp/setup/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "技能示例",
            "h1": "DeepSeek TUI 的技能示例，应该展示可复用的工作流设计，而不只是写得漂亮的提示词",
            "intro": "一个有价值的技能示例，不应该只是一个好看的文本片段。它应该说明：什么样的重复任务值得抽成技能、技能边界在哪里、抽出来以后到底哪一步变轻松了。",
            "answer_kicker": "直接答案",
            "answer_h2": "好的技能示例，本质上是在把重复工作流变成可反复调用的操作模式。",
            "answer_p": "如果一个示例看起来只像一段写得不错的提示词，它大概率还只是 prompt。技能真正有价值的地方，在于它能跨会话保留范围、顺序、默认假设和决策边界。",
            "questions": [
                "什么样的示例才像真正的 skill，而不是花哨 prompt？",
                "哪些重复工作最值得先抽成 skill？",
                "示例应该怎样帮助你判断：什么该抽出来，什么还该留在普通对话里？",
            ],
            "coverage": "这页要帮助用户识别可复用模式，理解一个好 skill 示例的构成，并判断什么时候应该继续用普通 prompting。",
            "diagnosis": [
                ("任务是否重复", "好的示例一定来自足够常见、值得结构化的重复任务。"),
                ("边界是否稳定", "工作流要有清楚的范围：做什么、不做什么、需要什么输入。"),
                ("默认值是否可复用", "示例应该替你保存那些每次都要重新写的假设、检查项和下一步。"),
            ],
            "workflow": [
                ("从重复出发，不要从文案出发", "不要因为一句话写得好看就做成 skill，要因为工作真的反复出现才做。"),
                ("先把边界定清楚", "未来的会话必须一眼看出 skill 的起点、终点，以及哪些判断仍然需要人来做。"),
                ("明确它到底省了什么", "最好的示例一定能明显减少某个成本：准备时间、一致性问题、检查遗漏，或者上下文重复。"),
                ("让示例贴近真实终端工作", "技能示例应该像你真的会在终端代理里调用的东西，而不是泛泛的 AI 灵感模板。"),
            ],
            "mistakes": [
                "把任何长 prompt 都叫成 skill，但其实并没有稳定工作流边界。",
                "示例写得很完整，却没有真正减少重复劳动。",
                "没有说明这个示例在真实终端会话里到底为什么有用。",
            ],
            "leave": "当你已经能判断一个重复任务该不该抽成技能，以及 skill 和普通 prompt 的边界时，就可以离开这页了。",
            "links": [
                ("Skills vs Prompts", "/zh/skills/vs-prompts/index.html"),
                ("技能总页", "/zh/skills/index.html"),
                ("MCP 设置", "/zh/mcp/setup/index.html"),
            ],
        },
    },
    ("skills", "vs-prompts"): {
        "en": {
            "eyebrow": "Skills vs Prompts",
            "h1": "Skills vs prompts becomes clear once you compare reusable workflow boundaries against one-off instruction text",
            "intro": "People often compare skills and prompts as if they were just two writing styles. That misses the important distinction. A prompt is usually optimized for one request. A skill is optimized for a pattern that keeps returning.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Use prompts for isolated requests and skills for repeatable workflows with stable boundaries.",
            "answer_p": "The difference is not about which one sounds smarter. It is about whether you need reuse, consistency, and a maintained operating shape across many future sessions.",
            "questions": [
                "When does a prompt stay the right tool?",
                "When has a repeated prompt already become a skill in disguise?",
                "What do you gain when you move a workflow from prompting into a skill?",
            ],
            "coverage": "This page should help the reader compare one-off prompting against reusable workflow packaging, and understand when repetition, boundary control, and consistency start to matter more than prose quality.",
            "diagnosis": [
                ("One-off request", "If the task is isolated and unlikely to return in the same form, a prompt is usually enough."),
                ("Repeated workflow", "If the same workflow keeps coming back, you are already paying the cost of not having a skill."),
                ("Need for guardrails", "If the work benefits from stable scope, ordering, file boundaries, or verification steps, a skill becomes more attractive."),
            ],
            "workflow": [
                ("Look for repetition first", "Do not ask whether the text is complex enough. Ask whether the workflow itself returns often enough."),
                ("Check whether consistency matters", "If future sessions need the same order, same limits, or same checks, prompts become harder to maintain than a skill."),
                ("Decide what should stay flexible", "A skill should hold the stable part of the process. The rest can remain normal prompting."),
                ("Upgrade only when the structure pays for itself", "The move from prompt to skill should reduce friction, not create ceremony for a workflow that barely repeats."),
            ],
            "mistakes": [
                "Treating a prompt and a skill as interchangeable because both contain instructions.",
                "Converting too early, before a workflow has actually repeated enough to justify maintenance.",
                "Making a skill so broad that it loses the stable boundary that made it useful.",
            ],
            "leave": "Leave this page once you can judge whether your current problem is a one-off instruction problem or a reusable workflow problem.",
            "links": [
                ("Skills examples", "/skills/examples/index.html"),
                ("Skills hub", "/skills/index.html"),
                ("Guides hub", "/guides/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "Skills vs Prompts",
            "h1": "只有把“可复用工作流边界”和“一次性指令文本”拆开看，skills 和 prompts 的区别才会清楚",
            "intro": "很多人把 skills 和 prompts 当成两种写法来比较，这样会错过真正重要的区别。prompt 通常是为一次请求优化的；skill 是为会反复出现的工作流模式优化的。",
            "answer_kicker": "直接答案",
            "answer_h2": "一次性问题用 prompt，反复出现且边界稳定的工作流用 skill。",
            "answer_p": "重点不在于谁写得更“聪明”，而在于你是否需要跨很多次会话复用同一套流程、约束和检查项。",
            "questions": [
                "什么时候 prompt 依然是最合适的工具？",
                "什么时候一个反复使用的 prompt，其实已经是伪装成 prompt 的 skill？",
                "把工作流从 prompt 提升到 skill 以后，到底能获得什么？",
            ],
            "coverage": "这页要帮助用户比较一次性 prompting 和可复用 workflow packaging，理解什么时候“重复、边界控制、一致性”会比文案本身更重要。",
            "diagnosis": [
                ("一次性请求", "如果任务只会出现一次，或者以后很少以同样形式回来，prompt 往往就够了。"),
                ("重复工作流", "如果同一套流程反复出现，你其实已经在持续支付“没有 skill”的成本。"),
                ("是否需要护栏", "当工作真的依赖稳定范围、固定顺序、文件边界或检查步骤时，skill 会更有价值。"),
            ],
            "workflow": [
                ("先看重复性", "不要先问文本是不是够复杂，要先问这个流程本身是不是会反复出现。"),
                ("再看一致性需求", "如果未来每次都需要同样顺序、同样限制、同样核对项，prompt 会比 skill 更难维护。"),
                ("保留该灵活的部分", "skill 只应该固定住稳定部分，剩下的判断仍然可以交给普通对话。"),
                ("只有在结构真正回本时才升级", "从 prompt 升级成 skill 的前提，是它真的减少摩擦，而不是为了形式感增加负担。"),
            ],
            "mistakes": [
                "因为两者都包含指令文本，就把 prompt 和 skill 当成同一件事。",
                "工作流还没真正重复起来，就过早抽成 skill。",
                "把 skill 做得太宽，最后失去原本最有价值的稳定边界。",
            ],
            "leave": "当你已经能判断自己面对的是一次性指令问题，还是一个值得沉淀成 skill 的重复工作流时，就可以离开这页了。",
            "links": [
                ("技能示例", "/zh/skills/examples/index.html"),
                ("技能总页", "/zh/skills/index.html"),
                ("Guides 总页", "/zh/guides/index.html"),
            ],
        },
    },
    ("comparisons", "vs-claude-code"): {
        "en": {
            "eyebrow": "Comparison",
            "h1": "DeepSeek TUI vs Claude Code is mainly a workflow and ecosystem comparison, not just a feature checklist",
            "intro": "People search this comparison because both tools live near the same terminal-agent category, but they do not feel identical in setup assumptions, model alignment, and how they structure day-to-day work. A useful comparison should help the reader understand fit, not just count features.",
            "answer_kicker": "Short Version",
            "answer_h2": "Choose based on workflow posture: model ecosystem, guardrails, session style, and the kind of terminal agent experience you actually want.",
            "answer_p": "A better comparison starts with how you work, not with who has the longest feature list. If the tool's assumptions match your environment, setup and daily use usually feel easier even before you compare every command.",
            "questions": [
                "Which tool feels closer to your normal coding-agent workflow?",
                "How much do ecosystem alignment and model preference matter in daily use?",
                "Where do guardrails, planning style, and execution philosophy start to matter more than install friction?",
            ],
            "coverage": "This page should help the reader compare setup posture, execution style, and everyday fit rather than stop at superficial similarity between two terminal coding tools.",
            "diagnosis": [
                ("Ecosystem fit", "Decide whether you are optimizing around a DeepSeek-centered workflow, a Claude-centered workflow, or a broader multi-tool environment."),
                ("Execution posture", "Compare how much direct execution freedom you want versus how much structured guidance you expect around planning and approval."),
                ("Daily session feel", "Look at which workflow feels more natural for repeated terminal use, not just for the first five minutes after install."),
            ],
            "workflow": [
                ("Start from your real environment", "Ask which model ecosystem and shell workflow you already trust. That often decides more than the marketing comparison."),
                ("Compare planning and action balance", "Some users care more about explicit planning steps, while others optimize for faster direct execution with fewer pauses."),
                ("Check setup and maintenance path", "A tool can look powerful on paper but still be a poor fit if its account, provider, or terminal assumptions fight your setup."),
                ("Choose based on repeated use", "The best comparison result is the one that still feels right after many sessions, not just after one successful install."),
            ],
            "mistakes": [
                "Comparing terminal agents only through feature bullets and ignoring workflow philosophy.",
                "Judging fit after one launch instead of after repeated coding sessions.",
                "Assuming the better-known comparison target is automatically the better long-term fit.",
            ],
            "leave": "Leave this page once you know which workflow posture matches your real terminal habits and which branch to read next for setup, modes, or guardrails.",
            "links": [
                ("Modes hub", "/modes/index.html"),
                ("Install hub", "/install/index.html"),
                ("Docs hub", "/docs/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "对比",
            "h1": "DeepSeek TUI vs Claude Code，本质上更像工作流和生态位的比较，而不是纯功能表对比",
            "intro": "用户会搜这组对比，是因为两者都属于终端代理这一类工具，但它们在安装假设、模型生态、以及日常工作组织方式上并不完全一样。真正有用的比较，应该帮助用户判断适配度，而不是只数功能点。",
            "answer_kicker": "短答案",
            "answer_h2": "按工作流姿态来选：模型生态、护栏强度、会话风格，以及你真正想要的终端代理体验。",
            "answer_p": "更好的比较方式不是先看谁功能多，而是先看你的工作方式和环境更贴近哪一边。如果工具的默认假设本来就更接近你的环境，后面的安装和日常使用通常都会更顺。",
            "questions": [
                "哪个工具更接近你平时真实的 coding-agent 工作流？",
                "模型生态偏好和 provider 对日常使用到底影响有多大？",
                "什么时候 guardrails、计划风格和执行哲学，会比安装摩擦更重要？",
            ],
            "coverage": "这页应该帮助用户比较 setup 姿态、执行风格和长期日常适配度，而不是停留在两个终端编码工具表面上都能做什么。",
            "diagnosis": [
                ("生态位匹配", "先判断你是更想围绕 DeepSeek 工作流、Claude 工作流，还是更广义的多工具环境来优化。"),
                ("执行姿态", "比较你更想要多少直接执行自由度，以及是否更依赖明确的计划和审批护栏。"),
                ("长期会话体验", "看哪一边更适合重复使用，而不是只看首次启动是不是成功。"),
            ],
            "workflow": [
                ("先从自己的真实环境出发", "先问自己已经信任的是哪一套模型生态和 shell 工作流，这往往比营销对比更重要。"),
                ("比较计划与执行的平衡", "有的人更依赖显式 planning，有的人更偏向少停顿、快执行。"),
                ("检查 setup 和维护路径", "纸面上很强的工具，如果账号、provider 或终端假设和你当前环境打架，也不会是好选择。"),
                ("按长期使用来判断", "真正好的比较结果，是你在连续很多次会话后仍然觉得自然，而不是第一次安装成功就结束。"),
            ],
            "mistakes": [
                "只看功能条目，不看工作流哲学。",
                "只开一次就下结论，没有看长期会话体验。",
                "因为 Claude Code 更有名，就默认它更适合自己。",
            ],
            "leave": "当你已经知道哪种工作流姿态更接近自己的终端习惯，以及下一步该去看 setup、modes 还是 docs 时，就可以离开这页了。",
            "links": [
                ("Modes 总页", "/zh/modes/index.html"),
                ("安装总页", "/zh/install/index.html"),
                ("Docs 总页", "/zh/docs/index.html"),
            ],
        },
    },
    ("comparisons", "vs-codex-cli"): {
        "en": {
            "eyebrow": "Comparison",
            "h1": "DeepSeek TUI vs Codex CLI should be judged by workflow fit, guardrails, and terminal operating style",
            "intro": "This comparison matters because both tools can live in a serious terminal workflow, but they do not guide planning, execution, and model alignment in exactly the same way. A useful page here should help the reader compare operating posture, not just command inventory.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Pick the tool whose session model, guardrails, and ecosystem assumptions better match the way you already work.",
            "answer_p": "If you ignore those workflow differences, the comparison becomes shallow very quickly. The better fit often shows up in repeated terminal use long before it shows up in a spreadsheet of features.",
            "questions": [
                "Which tool's workflow feels closer to how you already plan and execute terminal work?",
                "How much do approval models and guardrails influence your choice?",
                "Where do ecosystem assumptions matter more than surface-level feature overlap?",
            ],
            "coverage": "This page should help the reader compare daily terminal-agent fit, planning posture, guardrail expectations, and maintenance assumptions between the two tools.",
            "diagnosis": [
                ("Session model", "Compare how each tool expects you to move through planning, execution, and tool use during a normal session."),
                ("Guardrail preference", "Some users want strong approval boundaries and explicit workflow segmentation; others optimize for less friction and faster iteration."),
                ("Environment fit", "Ask which model and config ecosystem feels more natural on your machine and in your current team habits."),
            ],
            "workflow": [
                ("Compare daily usage, not only installation", "The install route matters, but the more important question is how the tool behaves once it becomes part of daily coding work."),
                ("Check the planning-execution handoff", "A tool may look similar on paper while still feeling very different in how it moves from intent to action."),
                ("Look at approval and safety posture", "If your workflow depends on clear guardrails, compare that directly rather than assuming all terminal agents behave the same."),
                ("Prefer the better long-session fit", "The right answer is the tool that continues to feel natural across many sessions and many projects."),
            ],
            "mistakes": [
                "Reducing the comparison to install commands and headline features.",
                "Ignoring how planning mode, approval flow, or tool boundaries affect real work.",
                "Assuming a broad feature overlap means the day-to-day experience is interchangeable.",
            ],
            "leave": "Leave this page once you know which tool's workflow posture fits your terminal habits and which deeper branch you need next.",
            "links": [
                ("Modes hub", "/modes/index.html"),
                ("Config hub", "/config/index.html"),
                ("Comparisons hub", "/comparisons/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "对比",
            "h1": "DeepSeek TUI vs Codex CLI，更该按工作流适配度、护栏和终端操作风格来判断",
            "intro": "这组对比有价值，是因为两者都能进入严肃的终端工作流，但它们在 planning、execution 和 model alignment 上并不完全一样。真正有用的页面，应该帮助用户比较操作姿态，而不是只列命令数量。",
            "answer_kicker": "直接答案",
            "answer_h2": "选那个会话模型、护栏强度和生态假设更贴近你现有工作方式的工具。",
            "answer_p": "如果忽略这些工作流差异，这组对比很快就会变得很浅。真正的适配度，往往在很多次终端会话里比在功能表里更早暴露出来。",
            "questions": [
                "哪个工具的工作流更接近你现在的计划与执行方式？",
                "审批模型和护栏强度对你的选择影响有多大？",
                "什么时候生态假设会比表面功能重叠更重要？",
            ],
            "coverage": "这页要帮助用户比较日常终端代理适配度、planning 姿态、guardrail 预期，以及两者在维护层面的差异。",
            "diagnosis": [
                ("会话模型", "比较它们在正常会话里，是如何组织 planning、execution 和 tool use 的。"),
                ("护栏偏好", "有些用户更需要明确审批边界，有些用户更追求少摩擦、快迭代。"),
                ("环境匹配", "看哪一边的模型生态、配置方式和团队习惯更贴近你当前机器和工作流。"),
            ],
            "workflow": [
                ("先比较日常使用，不只比较安装", "安装路径重要，但更重要的是它进入你的日常编码工作以后到底顺不顺。"),
                ("看 planning 到 execution 的过渡", "纸面上看着相似的工具，在从意图走到动作的过程中，实际感受可能完全不同。"),
                ("直接比较 approval 和 safety 姿态", "如果你的流程依赖清楚的护栏，就要把这点单独拿出来比较。"),
                ("优先选长期会话更顺的一边", "真正正确的答案，是在很多项目、很多次会话里依然自然的那一边。"),
            ],
            "mistakes": [
                "把比较缩减成安装命令和表层功能。",
                "忽略 planning mode、approval flow 和 tool boundary 对真实工作的影响。",
                "因为功能有重叠，就以为日常体验也能互换。",
            ],
            "leave": "当你已经知道哪一边的工作流姿态更贴近自己的终端习惯，以及下一步该进哪个更深的栏目时，就可以离开这页了。",
            "links": [
                ("Modes 总页", "/zh/modes/index.html"),
                ("配置总页", "/zh/config/index.html"),
                ("对比总页", "/zh/comparisons/index.html"),
            ],
        },
    },
    ("troubleshooting", "command-not-found"): {
        "en": {
            "eyebrow": "Path Troubleshooting",
            "h1": "A DeepSeek TUI command not found error usually means install ownership and shell path do not agree yet",
            "intro": "The generic command-not-found failure almost never means the app logic is broken. It usually means the install completed in one ecosystem, while your current shell still resolves commands through another path or an older terminal profile.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Do not reinstall first. Confirm which package path owns the binary and whether your active shell actually exports that location.",
            "answer_p": "Reinstalling can sometimes hide the problem for one session, but it rarely fixes the underlying path mismatch. The important question is where the binary landed and what your shell sees first.",
            "questions": [
                "Which installer actually owns the current binary?",
                "Does the shell you are testing in read the right PATH entries?",
                "Are you debugging a missing binary or only a missing shell exposure problem?",
            ],
            "coverage": "This page should help the reader distinguish between package-manager ownership, shell path visibility, and stale terminal-session state.",
            "diagnosis": [
                ("Install owner", "Work out whether npm, cargo, Homebrew, or a release binary is supposed to own the command."),
                ("Shell visibility", "Check whether the directory that should contain `deepseek` is actually exported in the shell profile you are using now."),
                ("Session freshness", "Some path fixes only appear after a new shell or a full terminal restart, so confirm whether you are testing in a stale session."),
            ],
            "workflow": [
                ("Identify the install route first", "Do not start from random fixes. Start from the package path that should own the binary."),
                ("Check the active shell path", "Inspect the current shell and verify whether that binary directory is present and ordered correctly."),
                ("Retest in a fresh shell", "If you only tested in the installation shell, you may be reading a temporary environment that vanishes later."),
                ("Escalate to route-specific troubleshooting", "If the generic path checks fail, move into the npm, cargo, Homebrew, or release-binary variant that matches your install route."),
            ],
            "mistakes": [
                "Reinstalling before you know which package path is supposed to own the command.",
                "Testing in one shell and assuming every terminal profile now sees the same PATH.",
                "Debugging provider auth before the command itself resolves cleanly.",
            ],
            "leave": "Leave this page once you know which install route owns the binary and whether the shell path mismatch is generic or route-specific.",
            "links": [
                ("npm install", "/install/npm/index.html"),
                ("Homebrew command not found", "/troubleshooting/homebrew-command-not-found/index.html"),
                ("Release binaries", "/troubleshooting/release-binaries/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "路径排错",
            "h1": "DeepSeek TUI 的 command not found，通常不是工具坏了，而是安装归属和 shell 路径还没对齐",
            "intro": "通用的 command-not-found 错误，几乎不意味着应用逻辑本身坏掉。更常见的情况是：安装发生在一个包管理生态里，但你当前 shell 解析命令时走的还是另一条路径，或者还是旧终端配置。",
            "answer_kicker": "直接答案",
            "answer_h2": "先别重装，先确认到底是谁安装了这个二进制，以及当前 shell 是否真的导出了那条路径。",
            "answer_p": "重装有时会暂时掩盖问题，但很少真正解决底层路径不匹配。关键在于：二进制落在了哪里，以及 shell 先看到了哪条路径。",
            "questions": [
                "当前二进制到底应该归哪个安装路线负责？",
                "你现在测试的 shell，真的读到了正确的 PATH 吗？",
                "你现在遇到的是“二进制不存在”，还是“shell 没看到”这个问题？",
            ],
            "coverage": "这页要帮助用户区分：包管理器归属、shell 路径可见性，以及旧会话缓存三类问题。",
            "diagnosis": [
                ("安装归属", "先弄清是 npm、cargo、Homebrew 还是 release binary 理应拥有这个命令。"),
                ("Shell 可见性", "确认当前 shell 配置里，包含 `deepseek` 的目录是否真的被导出，而且顺序正确。"),
                ("会话是否新鲜", "有些路径修复只有在新 shell 或完全重开终端后才会生效，所以要确认你不是在旧会话里误测。"),
            ],
            "workflow": [
                ("先识别安装路线", "不要先试一堆随机修复，先从理论上应该拥有二进制的那条安装路线开始查。"),
                ("再查当前 shell 路径", "确认当前 shell 里包含二进制目录，而且路径顺序没有被别的安装方式挡住。"),
                ("用新 shell 重测", "如果你只在安装窗口里测过一次，那可能只是临时环境，不能代表长期状态。"),
                ("必要时进入路线专属排错", "如果通用路径检查不够，就进入 npm、cargo、Homebrew 或 release binary 对应的排错页。"),
            ],
            "mistakes": [
                "还没搞清安装归属，就先重装。",
                "只在一个 shell 里测试，就默认所有终端配置都已经同步。",
                "命令还没解析成功，就先去排 provider 认证问题。",
            ],
            "leave": "当你已经知道是谁安装了二进制，以及当前 shell 的问题是通用 PATH 问题还是路线专属问题时，就可以离开这页了。",
            "links": [
                ("npm 安装", "/zh/install/npm/index.html"),
                ("Homebrew command not found", "/zh/troubleshooting/homebrew-command-not-found/index.html"),
                ("Release binaries", "/zh/troubleshooting/release-binaries/index.html"),
            ],
        },
    },
    ("troubleshooting", "homebrew-command-not-found"): {
        "en": {
            "eyebrow": "Homebrew Path Fix",
            "h1": "Homebrew command not found usually means brew installed the package but your shell still does not expose the brew-owned binary",
            "intro": "This variant deserves its own page because Homebrew users often trust the package install step but forget that terminal sessions still need the correct Homebrew path exported and prioritized.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "If brew says install succeeded, focus on shell exposure and binary ownership before you try another install command.",
            "answer_p": "The Homebrew case is less about whether the package exists and more about whether the active shell sees the expected brew location ahead of everything else.",
            "questions": [
                "Did brew install into a directory your shell exports?",
                "Is another package path shadowing the brew binary?",
                "Did you verify the command in a truly fresh terminal session?",
            ],
            "coverage": "This page should help the reader isolate brew-path exposure, shell profile ordering, and binary shadowing by other package routes.",
            "diagnosis": [
                ("Brew location", "Check whether the package lives under the Homebrew prefix your machine actually uses."),
                ("Shell export", "Make sure your shell profile exports that Homebrew bin location for the terminal you really use."),
                ("Shadowing", "Look for an older npm, cargo, or manual binary that still resolves earlier than the brew path."),
            ],
            "workflow": [
                ("Confirm the brew install really exists", "Verify the package is present before assuming the install itself failed."),
                ("Inspect the active shell path", "Check whether the Homebrew bin path is exported and whether it appears early enough to win resolution."),
                ("Retest after a new terminal session", "A path fix that only exists in one shell window is not a real fix yet."),
                ("Remove or deprioritize competing routes", "If another package path resolves first, the brew install may be correct but effectively invisible."),
            ],
            "mistakes": [
                "Re-running `brew install` when the real issue is shell path export.",
                "Assuming every terminal profile on macOS reads the same startup files.",
                "Leaving another package manager's binary earlier in PATH and blaming Homebrew.",
            ],
            "leave": "Leave this page once the brew-owned binary resolves first in the shell you actually use every day.",
            "links": [
                ("Homebrew install", "/install/homebrew/index.html"),
                ("Generic command not found", "/troubleshooting/command-not-found/index.html"),
                ("Release binaries", "/troubleshooting/release-binaries/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "Homebrew 路径修复",
            "h1": "Homebrew 的 command not found，通常不是没装上，而是 shell 还没把 brew 二进制正确暴露出来",
            "intro": "这个变体值得单独做一页，因为 Homebrew 用户往往相信安装步骤本身没问题，却忘了终端会话还需要正确导出并优先使用 Homebrew 路径。",
            "answer_kicker": "直接答案",
            "answer_h2": "如果 brew 已经提示安装成功，就优先检查 shell 暴露和二进制归属，不要先换别的安装命令。",
            "answer_p": "Homebrew 这一类问题，重点不在包有没有安装，而在当前 shell 是否真的先看到了 brew 对应的目录。",
            "questions": [
                "brew 安装位置是不是当前 shell 真正导出的目录？",
                "有没有别的包管理路径把 brew 二进制挡住？",
                "你是不是只在旧终端窗口里测过，没有用全新会话验证？",
            ],
            "coverage": "这页要帮助用户定位 brew 路径暴露、shell 启动文件顺序，以及其他安装路线造成的二进制遮挡问题。",
            "diagnosis": [
                ("Brew 目录位置", "先确认包是不是装在机器当前真正使用的 Homebrew 前缀下面。"),
                ("Shell 导出", "确认当前 shell 启动文件里确实导出了对应 Homebrew bin 目录，而且用于你真正工作的那个终端。"),
                ("二进制遮挡", "检查是不是旧的 npm、cargo 或手动二进制先被解析到了。"),
            ],
            "workflow": [
                ("先确认 brew 安装确实存在", "不要一开始就假设安装失败，先确认包已经在 brew 体系里。"),
                ("检查当前 shell 路径顺序", "确认 Homebrew bin 目录已导出，而且位置足够靠前。"),
                ("用全新终端重测", "只在当前窗口里生效的修复，不算真正稳定。"),
                ("处理竞争路径", "如果别的安装路线先被命中，brew 安装虽然存在，但等于不可见。"),
            ],
            "mistakes": [
                "路径问题还没查，就一直重复 `brew install`。",
                "以为 macOS 上所有终端都读同一套启动文件。",
                "PATH 里还有别的包管理器二进制更靠前，却把锅甩给 Homebrew。",
            ],
            "leave": "当 brew 对应的二进制已经在你日常使用的 shell 里优先解析出来时，就可以离开这页了。",
            "links": [
                ("Homebrew 安装", "/zh/install/homebrew/index.html"),
                ("通用 command not found", "/zh/troubleshooting/command-not-found/index.html"),
                ("Release binaries", "/zh/troubleshooting/release-binaries/index.html"),
            ],
        },
    },
    ("troubleshooting", "mcp-troubleshooting"): {
        "en": {
            "eyebrow": "MCP Troubleshooting",
            "h1": "MCP troubleshooting becomes manageable once you separate base-tool health from server-layer problems",
            "intro": "MCP failures are easy to overdiagnose because they appear at an advanced layer of the stack. In practice, many so-called MCP issues are still install, config, provider, or shell problems that only become visible once you add servers on top.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Prove the base DeepSeek TUI path is stable before blaming the MCP layer.",
            "answer_p": "If install, config, provider auth, or shell behavior is still unstable, MCP debugging will waste time because the server layer is not the real root cause yet.",
            "questions": [
                "Does the base tool behave correctly without MCP at all?",
                "Is the server reachable and declared the way the config expects?",
                "Are you debugging an MCP server issue or a lower-layer failure wearing an MCP label?",
            ],
            "coverage": "This page should help the reader diagnose MCP in layers: base install, config, server declaration, server reachability, and expected tool surface.",
            "diagnosis": [
                ("Base tool layer", "Confirm the app works normally without involving MCP so you know the foundation is sound."),
                ("Declaration layer", "Check whether the server definition, path, and startup command match what your config actually expects."),
                ("Reachability layer", "Verify the server can start and remain reachable long enough for the tool surface to appear."),
                ("Expectation layer", "Make sure you are not expecting tools or behaviors the current server never promised to expose."),
            ],
            "workflow": [
                ("Start with the non-MCP baseline", "If the tool is already unstable before MCP enters the picture, fix that first."),
                ("Review the server declaration", "Inspect the config path, command, and environment needed to launch the MCP server correctly."),
                ("Test server availability", "Check whether the server can start cleanly and remain available rather than dying immediately after launch."),
                ("Compare expected vs actual tool surface", "A missing capability may be a server limitation, not a launch failure."),
            ],
            "mistakes": [
                "Treating any advanced failure as an MCP-specific bug before checking the base install.",
                "Assuming the server exposes tools or schemas it never claimed to provide.",
                "Skipping server-start visibility and debugging only from the client side.",
            ],
            "leave": "Leave this page once you know whether the failure belongs to the base stack, the MCP declaration, the server runtime, or your expectation of the tool surface.",
            "links": [
                ("MCP setup", "/mcp/setup/index.html"),
                ("MCP server examples", "/mcp/server-examples/index.html"),
                ("Provider troubleshooting", "/troubleshooting/provider-troubleshooting/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "MCP 排错",
            "h1": "只要把基础工具层和 server 层分开看，MCP 排错就会清楚很多",
            "intro": "MCP 问题很容易被过度诊断，因为它出现在栈的更高层。现实里，很多所谓 MCP 故障，其实还是安装、配置、provider 或 shell 层的问题，只是加了 server 以后才暴露出来。",
            "answer_kicker": "直接答案",
            "answer_h2": "先证明基础 DeepSeek TUI 路线稳定，再去怪 MCP 层。",
            "answer_p": "如果安装、配置、provider 认证或 shell 行为本身都还不稳定，直接排 MCP 只会浪费时间，因为根因并不在 server 层。",
            "questions": [
                "不启用 MCP 时，基础工具本身是否工作正常？",
                "server 是否以配置预期的方式被声明和启动？",
                "你现在排的是 MCP server 问题，还是一个披着 MCP 外衣的更底层问题？",
            ],
            "coverage": "这页要帮助用户按层排 MCP：基础安装、配置、server 声明、server 可达性，以及预期工具面。",
            "diagnosis": [
                ("基础工具层", "先确认不带 MCP 时应用也能正常工作，保证基础层是稳的。"),
                ("声明层", "检查 server 的配置路径、启动命令和环境变量是否真的和当前配置一致。"),
                ("可达层", "确认 server 能启动且持续存活，而不是刚起就挂。"),
                ("预期层", "别把没有暴露的能力误当成启动失败，要确认 server 原本承诺的 tool surface 是什么。"),
            ],
            "workflow": [
                ("先跑非 MCP 基线", "如果不带 MCP 时工具已经不稳定，先修基础层。"),
                ("再看 server 声明", "核对配置文件里的 server 定义、命令和环境。"),
                ("验证 server 可用性", "确认 server 能正确启动并持续可用，而不是瞬间退出。"),
                ("比较预期与实际 tool surface", "缺少某个能力，不一定是故障，也可能只是 server 本来就没有提供。"),
            ],
            "mistakes": [
                "基础安装都没稳，就先把所有高级问题归咎于 MCP。",
                "默认 server 会提供它从未承诺的工具或 schema。",
                "只从客户端侧看问题，没有确认 server 启动层是否正常。",
            ],
            "leave": "当你已经知道问题属于基础栈、MCP 声明、server 运行时，还是自己对 tool surface 的预期错误时，就可以离开这页了。",
            "links": [
                ("MCP 设置", "/zh/mcp/setup/index.html"),
                ("MCP server 示例", "/zh/mcp/server-examples/index.html"),
                ("Provider 排错", "/zh/troubleshooting/provider-troubleshooting/index.html"),
            ],
        },
    },
    ("troubleshooting", "provider-troubleshooting"): {
        "en": {
            "eyebrow": "Provider Troubleshooting",
            "h1": "Provider troubleshooting gets faster when you separate credentials, endpoints, and backend assumptions",
            "intro": "Provider errors look deceptively similar. A key can be valid while the endpoint is wrong. The endpoint can be correct while the provider selection is wrong. Or the whole stack can be fine while your mental model still assumes a different backend path is active.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Do not collapse every provider failure into an API-key problem.",
            "answer_p": "A useful provider workflow isolates credentials, provider selection, and endpoint behavior one layer at a time instead of changing everything at once.",
            "questions": [
                "Is the key wrong, the provider wrong, or the endpoint wrong?",
                "Which backend path is actually active in the current config?",
                "Are you debugging auth, routing, or expectation mismatch?",
            ],
            "coverage": "This page should help the reader isolate provider issues into credential, provider-selection, endpoint, and runtime-expectation buckets.",
            "diagnosis": [
                ("Credential bucket", "Check whether the key belongs to the backend you think you are using right now."),
                ("Provider bucket", "Confirm that the selected provider in config matches the credentials and model path you intend to use."),
                ("Endpoint bucket", "Verify the base URL and backend routing assumptions before assuming the auth secret itself is invalid."),
                ("Expectation bucket", "Make sure the current runtime is not still inheriting an older environment variable or shell profile."),
            ],
            "workflow": [
                ("Read the current config first", "Look at the active provider, model, and endpoint rather than trusting memory."),
                ("Test credentials in the right context", "A valid key for one backend does not prove anything about another backend path."),
                ("Compare config with environment overrides", "Environment variables can silently override the file-based provider route."),
                ("Retest only after narrowing the bucket", "Change one layer at a time so you know whether the problem was auth, routing, or environment inheritance."),
            ],
            "mistakes": [
                "Rotating keys before confirming the provider and endpoint are even the expected ones.",
                "Assuming the config file wins when environment variables are still active.",
                "Changing credentials, provider, and URL all at once and losing the real signal.",
            ],
            "leave": "Leave this page once you know whether the failure lives in credentials, provider selection, endpoint routing, or environment inheritance.",
            "links": [
                ("Provider setup", "/config/provider-setup/index.html"),
                ("API key setup", "/config/api-key/index.html"),
                ("Environment variables", "/config/environment-variables/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "Provider 排错",
            "h1": "把凭证、endpoint 和 backend 假设拆开看以后，provider 排错会快很多",
            "intro": "provider 报错看起来很像，但根因经常完全不同。key 可能是对的，只是 endpoint 错了；endpoint 可能是对的，但 provider 选错了；也可能整套配置没问题，只是你还以为当前走的是另一条 backend 路线。",
            "answer_kicker": "直接答案",
            "answer_h2": "不要把所有 provider 错误都压缩成 API key 问题。",
            "answer_p": "真正有效的 provider 排错，要把凭证、provider 选择和 endpoint 行为一层层拆开，而不是一次改一堆设置。",
            "questions": [
                "到底是 key 错了、provider 错了，还是 endpoint 错了？",
                "当前配置里真正生效的是哪条 backend 路线？",
                "你现在排的是认证、路由，还是预期不一致问题？",
            ],
            "coverage": "这页要帮助用户把 provider 问题拆成凭证、provider 选择、endpoint 路由和运行时继承四类。",
            "diagnosis": [
                ("凭证层", "先确认当前 key 是否真的属于你以为正在使用的 backend。"),
                ("Provider 选择层", "确认配置中的 provider 是否和你的 key、模型路线一致。"),
                ("Endpoint 层", "在怀疑密钥前，先确认 base URL 和后端路由假设是否正确。"),
                ("继承层", "确认当前运行时没有被旧环境变量或旧 shell 配置悄悄覆盖。"),
            ],
            "workflow": [
                ("先读当前配置", "先看当前 provider、model 和 endpoint，而不是靠记忆判断。"),
                ("在正确上下文里验证凭证", "一个 backend 的有效 key，并不能证明另一条 backend 路线也没问题。"),
                ("比较配置文件和环境变量", "环境变量可能在你没注意时覆盖文件里的 provider 路线。"),
                ("缩小范围后再重测", "每次只改一层，才能看清到底是认证、路由，还是继承问题。"),
            ],
            "mistakes": [
                "provider 和 endpoint 还没确认，就先疯狂换 key。",
                "以为配置文件一定生效，但其实环境变量还在覆盖。",
                "一次把凭证、provider 和 URL 全改掉，最后反而丢失信号。",
            ],
            "leave": "当你已经知道问题属于凭证、provider 选择、endpoint 路由，还是环境变量继承时，就可以离开这页了。",
            "links": [
                ("Provider 设置", "/zh/config/provider-setup/index.html"),
                ("API Key 设置", "/zh/config/api-key/index.html"),
                ("环境变量", "/zh/config/environment-variables/index.html"),
            ],
        },
    },
    ("troubleshooting", "release-binaries"): {
        "en": {
            "eyebrow": "Release Binaries",
            "h1": "Release binaries make sense when you want direct ownership of the executable and do not want a package manager to mediate every step",
            "intro": "Binary downloads are often the cleanest route on locked-down machines or on setups where npm, cargo, or Homebrew add more confusion than help. But the tradeoff is that you become more responsible for path placement, update discipline, and version awareness.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "Use release binaries when you want explicit executable ownership and you are willing to manage placement and updates yourself.",
            "answer_p": "The route is simple only if you are comfortable deciding where the binary lives, how the shell finds it, and how you will replace it later.",
            "questions": [
                "When is a direct binary better than a package-manager install?",
                "What do you need to verify after placing the executable manually?",
                "Which maintenance costs grow when you stop using a package manager?",
            ],
            "coverage": "This page should help the reader decide when binary downloads are appropriate, how to place them safely, and what to verify after manual installation.",
            "diagnosis": [
                ("Fit question", "Choose this route when package managers are blocked, undesirable, or harder to reason about than one explicit executable."),
                ("Placement question", "Know where the binary should live so your real shell can resolve it predictably."),
                ("Maintenance question", "Accept that updates and version replacement are now your job instead of the package manager's."),
            ],
            "workflow": [
                ("Decide why you are avoiding package managers", "If the reason is not clear, you may just be moving complexity around."),
                ("Place the binary in a shell-visible directory", "The install only counts once the executable lives in a location your daily shell actually reads."),
                ("Verify in a new session", "Manual path placement should still survive a fresh terminal, not only the shell where you tested it."),
                ("Plan the next upgrade path", "Know how you will replace the binary later so the route stays maintainable."),
            ],
            "mistakes": [
                "Choosing manual binaries to avoid one problem but creating a larger path-management problem.",
                "Dropping the executable somewhere convenient without confirming shell visibility.",
                "Forgetting that updates are now manual and letting versions drift silently.",
            ],
            "leave": "Leave this page once you know whether manual binaries are the right fit and where the executable should live for your shell.",
            "links": [
                ("Install hub", "/install/index.html"),
                ("Command not found", "/troubleshooting/command-not-found/index.html"),
                ("Update or upgrade", "/install/update-or-upgrade/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "Release Binaries",
            "h1": "如果你想直接拥有可执行文件，而不想让包管理器介入每一步，release binaries 会更合适",
            "intro": "在受限机器上，或者 npm、cargo、Homebrew 只会让环境更乱时，直接下载二进制往往是最干净的路线。但代价也很明确：路径放置、更新节奏和版本管理都要你自己负责。",
            "answer_kicker": "直接答案",
            "answer_h2": "只有在你愿意自己管理可执行文件位置和后续更新时，release binaries 才是真正简单的路线。",
            "answer_p": "这条路只有在你能清楚决定：二进制放哪里、shell 怎么找到它、以后怎么替换它时，才算真的简单。",
            "questions": [
                "什么时候直接下载二进制比包管理器更好？",
                "手动放置可执行文件后，最先该验证什么？",
                "一旦不再依赖包管理器，后续维护成本会增加在哪些地方？",
            ],
            "coverage": "这页要帮助用户判断什么时候适合用二进制下载、应该怎样放置，以及手动安装后该如何验证和维护。",
            "diagnosis": [
                ("适配性问题", "当包管理器受限、不受欢迎，或比一个明确二进制更难解释时，这条路才有意义。"),
                ("放置问题", "要知道二进制应该放到哪里，才能让你真正工作的 shell 稳定找到它。"),
                ("维护问题", "接受升级和替换现在都归你自己管，而不是交给包管理器。"),
            ],
            "workflow": [
                ("先想清楚为什么不用包管理器", "如果理由不明确，你可能只是把复杂度从一个地方挪到另一个地方。"),
                ("把二进制放到 shell 可见目录", "只有当它落在你日常 shell 会读取的目录里，安装才算真的完成。"),
                ("在新会话中验证", "手动路径修复必须在新终端里也稳定生效。"),
                ("提前想好升级路线", "现在就明确以后如何替换二进制，避免后面维护失控。"),
            ],
            "mistakes": [
                "为了躲开一个问题选手动二进制，结果引入更大的路径管理问题。",
                "只是把文件放到一个顺手位置，却没确认 shell 真能看到。",
                "忘记更新要手动处理，结果版本长期漂移。",
            ],
            "leave": "当你已经知道手动二进制是不是适合自己，以及它该放在哪里才能被 shell 稳定识别时，就可以离开这页了。",
            "links": [
                ("安装总页", "/zh/install/index.html"),
                ("command not found", "/zh/troubleshooting/command-not-found/index.html"),
                ("更新与升级", "/zh/install/update-or-upgrade/index.html"),
            ],
        },
    },
    ("news", "what-is-deepseek-tui"): {
        "en": {
            "eyebrow": "Product Context",
            "h1": "What DeepSeek TUI is becomes much clearer once you treat it as a terminal coding-agent workflow instead of a simple chat wrapper",
            "intro": "People who search for this phrase usually are not looking for a marketing slogan. They are trying to understand what category the tool belongs to, what it can actually do in a terminal session, and which pages matter next if they want to install or evaluate it seriously.",
            "answer_kicker": "Direct Answer",
            "answer_h2": "DeepSeek TUI is best understood as a terminal coding-agent product with files, shell, config, modes, and extension workflows around it.",
            "answer_p": "If you frame it only as terminal chat, the rest of the site feels fragmented. Once you frame it as a coding-agent workflow, the install, config, docs, MCP, and mode branches all make sense as parts of one operating shape.",
            "questions": [
                "What kind of product category does DeepSeek TUI really belong to?",
                "Why do users keep searching for install, config, modes, and comparisons right after they discover the name?",
                "Which branch should a new reader open first after understanding the product at a high level?",
            ],
            "coverage": "This page should help the reader classify DeepSeek TUI correctly, understand why the surrounding site is split into setup, docs, modes, and troubleshooting branches, and choose the right next branch without guessing.",
            "diagnosis": [
                ("Category confusion", "If someone still thinks the product is only a terminal chat shell, they will miss why files, shell actions, approval flows, and config pages matter so much."),
                ("Workflow confusion", "If the user understands it as a coding-agent workflow, the surrounding branches become easier to navigate because each branch answers a different operational question."),
                ("Next-step confusion", "A new reader usually does not need every branch at once. They need the one that matches their current question: install, config, docs, modes, or comparison."),
            ],
            "workflow": [
                ("Start from the operating shape", "Explain the tool as a terminal agent that works across prompts, files, shell commands, config, and structured workflows rather than as a thin chat layer."),
                ("Map the core branches to real questions", "Install answers how to get started, Config answers how to connect and tune it, Docs answer what the upstream project formally says, and Modes answer how the work style changes."),
                ("Choose the next page by actual need", "A new user who cannot run the binary should go to Install. A user who installed it but cannot connect should go to Config. A user comparing tools should go to Comparisons."),
                ("Leave once the category is clear", "This page should narrow the product definition and send the reader into the correct operational branch, not keep them at the overview layer forever."),
            ],
            "mistakes": [
                "Treating DeepSeek TUI as just another terminal chatbot and missing the coding-agent workflow around it.",
                "Opening docs, modes, or MCP pages before basic install and config questions are settled.",
                "Reading this page as if it should replace the deeper branches instead of choosing the right one.",
            ],
            "leave": "Leave this page once you can explain what DeepSeek TUI is in one sentence and know whether your next stop should be install, config, docs, modes, or comparisons.",
            "links": [
                ("Install DeepSeek TUI", "/install/index.html"),
                ("Configure DeepSeek TUI", "/config/index.html"),
                ("Docs hub", "/docs/index.html"),
            ],
        },
        "zh": {
            "eyebrow": "产品背景",
            "h1": "只有把 DeepSeek TUI 当成终端编码代理工作流来看，它到底是什么这件事才会真正讲清楚",
            "intro": "搜索这个词的人，通常不是在找一句营销口号，而是在试图判断：它到底属于什么产品类别、在终端里究竟能做什么，以及如果要认真安装或评估，下一步最该看哪一组页面。",
            "answer_kicker": "直接答案",
            "answer_h2": "DeepSeek TUI 更适合被理解成一个终端里的编码代理产品，而不是普通聊天壳。",
            "answer_p": "如果只把它理解成终端聊天，你会觉得站里的 install、config、docs、modes、MCP 都像散页。只有把它看成一条编码代理工作流，这些分支才会连成一套完整结构。",
            "questions": [
                "DeepSeek TUI 到底属于什么产品类别？",
                "为什么用户认识这个名字以后，很快就会继续搜索安装、配置、模式和对比？",
                "当你先知道它是什么之后，下一页应该优先开哪一条分支？",
            ],
            "coverage": "这页应该帮助用户正确给 DeepSeek TUI 分类，理解为什么整站会拆成 setup、docs、modes、troubleshooting 等分支，并且不用靠猜就能判断下一步该去哪一页。",
            "diagnosis": [
                ("类别误解", "如果还把它当成普通终端聊天壳，就会很难理解为什么文件、shell、审批、配置和模式页面都这么重要。"),
                ("工作流误解", "一旦把它理解成终端编码代理工作流，周围这些栏目就会变得好懂，因为每条分支都在回答不同的操作问题。"),
                ("下一步误解", "第一次来的读者并不需要同时打开所有栏目，而是应该先按自己当前的问题，去 install、config、docs、modes 或 comparisons。"),
            ],
            "workflow": [
                ("先从操作形态解释它", "把它解释成能跨提示词、文件、shell 命令、配置和结构化工作流工作的终端代理，而不是单薄的聊天界面。"),
                ("把主要分支映射到真实问题", "Install 负责解决怎么开始，Config 负责解决怎么连通和调优，Docs 负责解释上游正式文档，Modes 负责解释工作方式怎么切换。"),
                ("按当前问题选下一页", "如果用户连二进制都还没跑起来，就先去 Install；如果已经装好但连不上 provider，就去 Config；如果是在比较工具，就去 Comparisons。"),
                ("一旦类别清楚就离开这页", "这页的作用是把产品定义压清楚，再把用户送进正确分支，而不是把人长期留在概览层。"),
            ],
            "mistakes": [
                "把 DeepSeek TUI 当成普通终端聊天工具，忽略了它周围整套编码代理工作流。",
                "安装和配置都还没解决，就过早去读 modes、MCP 或更深的 docs 页面。",
                "把这页当成替代所有后续分支的总说明，而不是分流入口。",
            ],
            "leave": "当你已经能用一句话解释 DeepSeek TUI 是什么，并且知道下一步该去 install、config、docs、modes 还是 comparisons 时，就可以离开这页了。",
            "links": [
                ("安装总页", "/zh/install/index.html"),
                ("配置总页", "/zh/config/index.html"),
                ("Docs 总页", "/zh/docs/index.html"),
            ],
        },
    },
}


def render_links(links: list[tuple[str, str]]) -> str:
    return "".join(f'<a href="{html.escape(href, quote=True)}">{html.escape(label)}</a>' for label, href in links)


def render_list(items: list[str]) -> str:
    return "".join(f"<li>{html.escape(item)}</li>" for item in items)


def render_diagnosis(rows: list[tuple[str, str]]) -> str:
    parts = []
    for title, body in rows:
        parts.append(f"<h3>{html.escape(title)}</h3><p>{html.escape(body)}</p>")
    return "".join(parts)


def render_workflow(rows: list[tuple[str, str]]) -> str:
    items = []
    for title, body in rows:
        items.append(f"<li><strong>{html.escape(title)}</strong><br>{html.escape(body)}</li>")
    return "".join(items)


def build_main(copy: dict[str, object], zh: bool) -> str:
    questions = render_list(copy["questions"])  # type: ignore[index]
    mistakes = render_list(copy["mistakes"])  # type: ignore[index]
    diagnosis = render_diagnosis(copy["diagnosis"])  # type: ignore[index]
    workflow = render_workflow(copy["workflow"])  # type: ignore[index]
    links = render_links(copy["links"])  # type: ignore[index]
    labels = {
        "questions": "这页应该先回答的问题" if zh else "Questions this page should answer fast",
        "coverage": "这页应该帮你判断什么" if zh else "What this page should help you decide",
        "diagnosis": "快速定位" if zh else "Fast diagnosis",
        "next": "下一步最该去的页面" if zh else "Best next pages",
        "workflow": "逐步处理流程" if zh else "Step-by-step workflow",
        "mistakes": "常见误区" if zh else "Common mistakes",
        "leave": "什么时候可以离开这页" if zh else "When to leave this page",
        "detail_kicker": "把这页当作正文页来用" if zh else "Use this as a detail page",
        "detail_body": (
            "这页的目标是直接回答当前这个具体问题，而不是只把你推回栏目页。适合已经明确分支、现在需要更清楚处理路径的时候打开。"
            if zh
            else "This page is meant to answer the concrete question directly, not just point back to a hub. Use it when you already know the branch and need a clearer working path."
        ),
    }
    return f"""<main><section class="page-hero"><div class="container two-col"><div><span class="eyebrow">{html.escape(copy['eyebrow'])}</span><h1>{html.escape(copy['h1'])}</h1><p>{html.escape(copy['intro'])}</p></div><aside class="answer-card"><span class="panel-kicker">{html.escape(copy['answer_kicker'])}</span><h2>{html.escape(copy['answer_h2'])}</h2><p>{html.escape(copy['answer_p'])}</p></aside></div></section><section class="section"><div class="container two-col"><article class="prose"><h2>{labels['questions']}</h2><ul>{questions}</ul><h2>{labels['coverage']}</h2><p>{html.escape(copy['coverage'])}</p><h2>{labels['diagnosis']}</h2>{diagnosis}</article><aside class="panel-card"><span class="panel-kicker">{labels['next']}</span><div class="link-stack">{links}</div></aside></div></section><section class="section section-alt"><div class="container two-col"><article class="prose"><h2>{labels['workflow']}</h2><ol>{workflow}</ol><h2>{labels['mistakes']}</h2><ul>{mistakes}</ul><h2>{labels['leave']}</h2><p>{html.escape(copy['leave'])}</p></article><aside class="panel-card"><span class="panel-kicker">{labels['detail_kicker']}</span><p>{html.escape(labels['detail_body'])}</p></aside></div></section></main>"""


def process_page(path: Path, copy: dict[str, object], zh: bool) -> None:
    text = path.read_text(encoding="utf-8")
    if not re.search(r"<main>.*?</main>", text, flags=re.S):
        raise RuntimeError(f"Failed to replace <main> block in {path}")
    updated = re.sub(r"<main>.*?</main>", build_main(copy, zh), text, flags=re.S, count=1)
    path.write_text(updated, encoding="utf-8")


def main() -> None:
    for (section, slug), payload in PAGES.items():
        process_page(ROOT / section / slug / "index.html", payload["en"], False)
        process_page(ROOT / "zh" / section / slug / "index.html", payload["zh"], True)
        print(f"Updated {section}/{slug}")


if __name__ == "__main__":
    main()
