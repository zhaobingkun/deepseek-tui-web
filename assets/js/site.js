document.querySelectorAll("[data-year]").forEach((node) => {
  node.textContent = new Date().getFullYear();
});

const normalizePath = (value) => {
  if (!value) return "/";
  let next = value.replace(/index\.html$/, "");
  if (!next.endsWith("/")) next += "/";
  next = next.replace(/\/+/g, "/");
  if (next === "//") next = "/";
  return next;
};

const pathStartsWith = (path, prefix) => path === prefix || path.startsWith(prefix);

const currentPath = normalizePath(window.location.pathname);
const isZh = currentPath.startsWith("/zh/");

const navConfig = isZh
  ? {
      home: "/zh/",
      switchLabel: "English",
      sidebarKicker: "副菜单",
      sidebarIntro: "先打开栏目列表，再进入你真正需要的那篇文章。",
      switchHref: currentPath === "/zh/" ? "/" : currentPath.replace(/^\/zh/, "") || "/",
      items: [
        { label: "首页", href: "/zh/", match: "/zh/" },
        { label: "指南", href: "/zh/guides/", match: "/zh/guides/" },
        { label: "文档", href: "/zh/docs/", match: "/zh/docs/" },
        { label: "安装", href: "/zh/install/", match: "/zh/install/" },
        { label: "配置", href: "/zh/config/", match: "/zh/config/" },
        { label: "MCP", href: "/zh/mcp/", match: "/zh/mcp/" },
        { label: "模式", href: "/zh/modes/", match: "/zh/modes/" },
        { label: "技能", href: "/zh/skills/", match: "/zh/skills/" },
        { label: "对比", href: "/zh/comparisons/", match: "/zh/comparisons/" },
        { label: "排错", href: "/zh/troubleshooting/", match: "/zh/troubleshooting/" },
        { label: "资讯", href: "/zh/news/", match: "/zh/news/" },
      ],
      sections: {
        guides: {
          label: "指南菜单",
          match: "/zh/guides/",
          items: [
            { label: "指南总页", href: "/zh/guides/" },
            { label: "价格与成本", href: "/zh/guides/pricing-and-cost/" },
          ],
        },
        docs: {
          label: "文档菜单",
          match: "/zh/docs/",
          items: [
            { label: "文档总页", href: "/zh/docs/" },
            { label: "安装文档", href: "/zh/docs/install/" },
            { label: "配置文档", href: "/zh/docs/configuration/" },
            { label: "MCP 文档", href: "/zh/docs/mcp/" },
            { label: "模式文档", href: "/zh/docs/modes/" },
            { label: "快捷键", href: "/zh/docs/keybindings/" },
            { label: "运行时 API", href: "/zh/docs/runtime-api/" },
            { label: "子代理", href: "/zh/docs/subagents/" },
            { label: "工具边界", href: "/zh/docs/tool-surface/" },
            { label: "Docker", href: "/zh/docs/docker/" },
            { label: "记忆", href: "/zh/docs/memory/" },
            { label: "运维手册", href: "/zh/docs/operations-runbook/" },
            { label: "发布手册", href: "/zh/docs/release-runbook/" },
            { label: "容量控制器", href: "/zh/docs/capacity-controller/" },
            { label: "协调器提示词", href: "/zh/docs/v0-8-8-coordinator-prompt/" },
            { label: "架构", href: "/zh/docs/architecture/" },
            { label: "本地化", href: "/zh/docs/localization/" },
            { label: "旧版 Rust 审计", href: "/zh/docs/legacy-rust-audit-0-7-6/" },
            { label: "v0.7.5 实现计划", href: "/zh/docs/v0-7-5-implementation-plan/" },
            { label: "竞争分析", href: "/zh/docs/competitive-analysis/" },
            { label: "可访问性", href: "/zh/docs/accessibility/" },
          ],
        },
        install: {
          label: "安装菜单",
          match: "/zh/install/",
          items: [
            { label: "安装总页", href: "/zh/install/" },
            { label: "Homebrew", href: "/zh/install/homebrew/" },
            { label: "npm", href: "/zh/install/npm/" },
            { label: "Cargo", href: "/zh/install/cargo/" },
            { label: "Windows", href: "/zh/install/windows/" },
            { label: "更新与升级", href: "/zh/install/update-or-upgrade/" },
          ],
        },
        config: {
          label: "配置菜单",
          match: "/zh/config/",
          items: [
            { label: "配置总页", href: "/zh/config/" },
            { label: "API Key", href: "/zh/config/api-key/" },
            { label: "Provider 设置", href: "/zh/config/provider-setup/" },
            { label: "Provider 成本", href: "/zh/config/provider-cost/" },
            { label: "环境变量", href: "/zh/config/environment-variables/" },
            { label: "文件位置", href: "/zh/config/file-location/" },
            { label: "重置配置", href: "/zh/config/reset/" },
          ],
        },
        mcp: {
          label: "MCP 菜单",
          match: "/zh/mcp/",
          items: [
            { label: "MCP 总页", href: "/zh/mcp/" },
            { label: "MCP 安装设置", href: "/zh/mcp/setup/" },
            { label: "Server 示例", href: "/zh/mcp/server-examples/" },
            { label: "Server 列表", href: "/zh/mcp/servers/" },
          ],
        },
        modes: {
          label: "模式菜单",
          match: "/zh/modes/",
          items: [
            { label: "模式总页", href: "/zh/modes/" },
            { label: "Plan Mode", href: "/zh/modes/plan-mode/" },
            { label: "Yolo Mode", href: "/zh/modes/yolo-mode/" },
            { label: "Plan vs Yolo", href: "/zh/modes/plan-vs-yolo/" },
          ],
        },
        skills: {
          label: "技能菜单",
          match: "/zh/skills/",
          items: [
            { label: "技能总页", href: "/zh/skills/" },
            { label: "示例", href: "/zh/skills/examples/" },
            { label: "技能 vs 提示词", href: "/zh/skills/vs-prompts/" },
          ],
        },
        comparisons: {
          label: "对比菜单",
          match: "/zh/comparisons/",
          items: [
            { label: "对比总页", href: "/zh/comparisons/" },
            { label: "vs Claude Code", href: "/zh/comparisons/vs-claude-code/" },
            { label: "vs Codex CLI", href: "/zh/comparisons/vs-codex-cli/" },
          ],
        },
        troubleshooting: {
          label: "排错菜单",
          match: "/zh/troubleshooting/",
          items: [
            { label: "排错总页", href: "/zh/troubleshooting/" },
            { label: "Command Not Found", href: "/zh/troubleshooting/command-not-found/" },
            { label: "Homebrew Command Not Found", href: "/zh/troubleshooting/homebrew-command-not-found/" },
            { label: "Provider 排错", href: "/zh/troubleshooting/provider-troubleshooting/" },
            { label: "MCP 排错", href: "/zh/troubleshooting/mcp-troubleshooting/" },
            { label: "Release Binaries", href: "/zh/troubleshooting/release-binaries/" },
          ],
        },
        news: {
          label: "资讯菜单",
          match: "/zh/news/",
          items: [
            { label: "资讯总页", href: "/zh/news/" },
            { label: "什么是 DeepSeek TUI", href: "/zh/news/what-is-deepseek-tui/" },
          ],
        },
      },
    }
  : {
      home: "/",
      switchLabel: "中文",
      sidebarKicker: "Section Menu",
      sidebarIntro: "Open the section list first, then move into the exact article you need.",
      switchHref: currentPath === "/" ? "/zh/" : `/zh${currentPath.replace(/\/$/, "")}/`,
      items: [
        { label: "Home", href: "/", match: "/" },
        { label: "Guides", href: "/guides/", match: "/guides/" },
        { label: "Docs", href: "/docs/", match: "/docs/" },
        { label: "Install", href: "/install/", match: "/install/" },
        { label: "Config", href: "/config/", match: "/config/" },
        { label: "MCP", href: "/mcp/", match: "/mcp/" },
        { label: "Modes", href: "/modes/", match: "/modes/" },
        { label: "Skills", href: "/skills/", match: "/skills/" },
        { label: "Comparisons", href: "/comparisons/", match: "/comparisons/" },
        { label: "Troubleshooting", href: "/troubleshooting/", match: "/troubleshooting/" },
        { label: "News", href: "/news/", match: "/news/" },
      ],
      sections: {
        guides: {
          label: "Guide Menu",
          match: "/guides/",
          items: [
            { label: "Guides Hub", href: "/guides/" },
            { label: "Pricing and Cost", href: "/guides/pricing-and-cost/" },
          ],
        },
        docs: {
          label: "Docs Menu",
          match: "/docs/",
          items: [
            { label: "Docs Hub", href: "/docs/" },
            { label: "Install Docs", href: "/docs/install/" },
            { label: "Configuration", href: "/docs/configuration/" },
            { label: "MCP Docs", href: "/docs/mcp/" },
            { label: "Modes Docs", href: "/docs/modes/" },
            { label: "Keybindings", href: "/docs/keybindings/" },
            { label: "Runtime API", href: "/docs/runtime-api/" },
            { label: "Subagents", href: "/docs/subagents/" },
            { label: "Tool Surface", href: "/docs/tool-surface/" },
            { label: "Docker", href: "/docs/docker/" },
            { label: "Memory", href: "/docs/memory/" },
            { label: "Operations Runbook", href: "/docs/operations-runbook/" },
            { label: "Release Runbook", href: "/docs/release-runbook/" },
            { label: "Capacity Controller", href: "/docs/capacity-controller/" },
            { label: "Coordinator Prompt", href: "/docs/v0-8-8-coordinator-prompt/" },
            { label: "Architecture", href: "/docs/architecture/" },
            { label: "Localization", href: "/docs/localization/" },
            { label: "Legacy Rust Audit", href: "/docs/legacy-rust-audit-0-7-6/" },
            { label: "v0.7.5 Plan", href: "/docs/v0-7-5-implementation-plan/" },
            { label: "Competitive Analysis", href: "/docs/competitive-analysis/" },
            { label: "Accessibility", href: "/docs/accessibility/" },
          ],
        },
        install: {
          label: "Install Menu",
          match: "/install/",
          items: [
            { label: "Install Hub", href: "/install/" },
            { label: "Homebrew", href: "/install/homebrew/" },
            { label: "npm", href: "/install/npm/" },
            { label: "Cargo", href: "/install/cargo/" },
            { label: "Windows", href: "/install/windows/" },
            { label: "Update or Upgrade", href: "/install/update-or-upgrade/" },
          ],
        },
        config: {
          label: "Config Menu",
          match: "/config/",
          items: [
            { label: "Config Hub", href: "/config/" },
            { label: "API Key", href: "/config/api-key/" },
            { label: "Provider Setup", href: "/config/provider-setup/" },
            { label: "Provider Cost", href: "/config/provider-cost/" },
            { label: "Environment Variables", href: "/config/environment-variables/" },
            { label: "File Location", href: "/config/file-location/" },
            { label: "Reset Config", href: "/config/reset/" },
          ],
        },
        mcp: {
          label: "MCP Menu",
          match: "/mcp/",
          items: [
            { label: "MCP Hub", href: "/mcp/" },
            { label: "MCP Setup", href: "/mcp/setup/" },
            { label: "Server Examples", href: "/mcp/server-examples/" },
            { label: "Server List", href: "/mcp/servers/" },
          ],
        },
        modes: {
          label: "Modes Menu",
          match: "/modes/",
          items: [
            { label: "Modes Hub", href: "/modes/" },
            { label: "Plan Mode", href: "/modes/plan-mode/" },
            { label: "Yolo Mode", href: "/modes/yolo-mode/" },
            { label: "Plan vs Yolo", href: "/modes/plan-vs-yolo/" },
          ],
        },
        skills: {
          label: "Skills Menu",
          match: "/skills/",
          items: [
            { label: "Skills Hub", href: "/skills/" },
            { label: "Examples", href: "/skills/examples/" },
            { label: "Skills vs Prompts", href: "/skills/vs-prompts/" },
          ],
        },
        comparisons: {
          label: "Comparisons Menu",
          match: "/comparisons/",
          items: [
            { label: "Comparisons Hub", href: "/comparisons/" },
            { label: "vs Claude Code", href: "/comparisons/vs-claude-code/" },
            { label: "vs Codex CLI", href: "/comparisons/vs-codex-cli/" },
          ],
        },
        troubleshooting: {
          label: "Troubleshooting Menu",
          match: "/troubleshooting/",
          items: [
            { label: "Troubleshooting Hub", href: "/troubleshooting/" },
            { label: "Command Not Found", href: "/troubleshooting/command-not-found/" },
            { label: "Homebrew Command Not Found", href: "/troubleshooting/homebrew-command-not-found/" },
            { label: "Provider Troubleshooting", href: "/troubleshooting/provider-troubleshooting/" },
            { label: "MCP Troubleshooting", href: "/troubleshooting/mcp-troubleshooting/" },
            { label: "Release Binaries", href: "/troubleshooting/release-binaries/" },
          ],
        },
        news: {
          label: "News Menu",
          match: "/news/",
          items: [
            { label: "News Hub", href: "/news/" },
            { label: "What Is DeepSeek TUI?", href: "/news/what-is-deepseek-tui/" },
          ],
        },
      },
    };

const currentSection = Object.values(navConfig.sections).find((section) =>
  pathStartsWith(currentPath, normalizePath(section.match))
);

const navLinks = document.querySelector("[data-nav-links]");
if (navLinks) {
  const navItems = [
    ...navConfig.items.map((item) => {
      const isActive =
        item.match === "/"
          ? currentPath === "/"
          : pathStartsWith(currentPath, normalizePath(item.match));
      return `<a href="${item.href}" class="${isActive ? "is-active" : ""}">${item.label}</a>`;
    }),
    `<a href="${navConfig.switchHref}">${navConfig.switchLabel}</a>`,
  ];
  navLinks.innerHTML = navItems.join("");
}

const toggle = document.querySelector("[data-nav-toggle]");
const links = document.querySelector("[data-nav-links]");

if (toggle && links) {
  toggle.addEventListener("click", () => {
    links.classList.toggle("is-open");
  });
}

const shouldBuildSidebar =
  currentSection &&
  currentPath !== "/" &&
  currentPath !== "/zh/" &&
  document.querySelector(".page-path") &&
  document.querySelector("main");

if (shouldBuildSidebar) {
  const main = document.querySelector("main");
  if (main && !main.dataset.sidebarReady) {
    const layout = document.createElement("div");
    layout.className = "doc-layout";

    const sidebar = document.createElement("aside");
    sidebar.className = "section-sidebar";
    const sidebarItems = currentSection.items
      .map((item) => {
        const active = normalizePath(item.href) === currentPath;
        return `<a href="${item.href}" class="sidebar-link${active ? " is-current" : ""}">${item.label}</a>`;
      })
      .join("");

    sidebar.innerHTML = `
      <div class="section-sidebar-card">
        <span class="panel-kicker">${navConfig.sidebarKicker}</span>
        <h2>${currentSection.label}</h2>
        <p>${navConfig.sidebarIntro}</p>
        <nav class="sidebar-links" aria-label="${currentSection.label}">
          ${sidebarItems}
        </nav>
      </div>
    `;

    const content = document.createElement("div");
    content.className = "doc-content";
    while (main.firstChild) {
      content.appendChild(main.firstChild);
    }

    layout.append(sidebar, content);
    main.appendChild(layout);
    main.dataset.sidebarReady = "true";
    main.classList.add("main-with-sidebar");
  }
}
