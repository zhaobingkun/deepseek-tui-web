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
      home: "/zh/index.html",
      switchLabel: "English",
      sidebarKicker: "副菜单",
      sidebarIntro: "先打开栏目列表，再进入你真正需要的那篇文章。",
      switchHref:
        window.location.pathname === "/zh/" || window.location.pathname === "/zh/index.html"
          ? "/index.html"
          : window.location.pathname.replace(/^\/zh/, "") || "/index.html",
      items: [
        { label: "首页", href: "/zh/index.html", match: "/zh/" },
        { label: "指南", href: "/zh/guides/index.html", match: "/zh/guides/" },
        { label: "文档", href: "/zh/docs/index.html", match: "/zh/docs/" },
        { label: "安装", href: "/zh/install/index.html", match: "/zh/install/" },
        { label: "配置", href: "/zh/config/index.html", match: "/zh/config/" },
        { label: "MCP", href: "/zh/mcp/index.html", match: "/zh/mcp/" },
        { label: "模式", href: "/zh/modes/index.html", match: "/zh/modes/" },
        { label: "技能", href: "/zh/skills/index.html", match: "/zh/skills/" },
        { label: "对比", href: "/zh/comparisons/index.html", match: "/zh/comparisons/" },
        { label: "排错", href: "/zh/troubleshooting/index.html", match: "/zh/troubleshooting/" },
        { label: "资讯", href: "/zh/news/index.html", match: "/zh/news/" },
      ],
      sections: {
        guides: {
          label: "指南菜单",
          match: "/zh/guides/",
          items: [
            { label: "指南总页", href: "/zh/guides/index.html" },
            { label: "价格与成本", href: "/zh/guides/pricing-and-cost/index.html" },
          ],
        },
        docs: {
          label: "文档菜单",
          match: "/zh/docs/",
          items: [
            { label: "文档总页", href: "/zh/docs/index.html" },
            { label: "安装文档", href: "/zh/docs/install/index.html" },
            { label: "配置文档", href: "/zh/docs/configuration/index.html" },
            { label: "MCP 文档", href: "/zh/docs/mcp/index.html" },
            { label: "模式文档", href: "/zh/docs/modes/index.html" },
            { label: "快捷键", href: "/zh/docs/keybindings/index.html" },
            { label: "运行时 API", href: "/zh/docs/runtime-api/index.html" },
            { label: "子代理", href: "/zh/docs/subagents/index.html" },
            { label: "工具边界", href: "/zh/docs/tool-surface/index.html" },
            { label: "Docker", href: "/zh/docs/docker/index.html" },
            { label: "记忆", href: "/zh/docs/memory/index.html" },
            { label: "运维手册", href: "/zh/docs/operations-runbook/index.html" },
            { label: "发布手册", href: "/zh/docs/release-runbook/index.html" },
            { label: "容量控制器", href: "/zh/docs/capacity-controller/index.html" },
            { label: "协调器提示词", href: "/zh/docs/v0-8-8-coordinator-prompt/index.html" },
            { label: "架构", href: "/zh/docs/architecture/index.html" },
            { label: "本地化", href: "/zh/docs/localization/index.html" },
            { label: "旧版 Rust 审计", href: "/zh/docs/legacy-rust-audit-0-7-6/index.html" },
            { label: "v0.7.5 实现计划", href: "/zh/docs/v0-7-5-implementation-plan/index.html" },
            { label: "竞争分析", href: "/zh/docs/competitive-analysis/index.html" },
            { label: "可访问性", href: "/zh/docs/accessibility/index.html" },
          ],
        },
        install: {
          label: "安装菜单",
          match: "/zh/install/",
          items: [
            { label: "安装总页", href: "/zh/install/index.html" },
            { label: "Homebrew", href: "/zh/install/homebrew/index.html" },
            { label: "npm", href: "/zh/install/npm/index.html" },
            { label: "Cargo", href: "/zh/install/cargo/index.html" },
            { label: "Windows", href: "/zh/install/windows/index.html" },
            { label: "更新与升级", href: "/zh/install/update-or-upgrade/index.html" },
          ],
        },
        config: {
          label: "配置菜单",
          match: "/zh/config/",
          items: [
            { label: "配置总页", href: "/zh/config/index.html" },
            { label: "API Key", href: "/zh/config/api-key/index.html" },
            { label: "Provider 设置", href: "/zh/config/provider-setup/index.html" },
            { label: "Provider 成本", href: "/zh/config/provider-cost/index.html" },
            { label: "环境变量", href: "/zh/config/environment-variables/index.html" },
            { label: "文件位置", href: "/zh/config/file-location/index.html" },
            { label: "重置配置", href: "/zh/config/reset/index.html" },
          ],
        },
        mcp: {
          label: "MCP 菜单",
          match: "/zh/mcp/",
          items: [
            { label: "MCP 总页", href: "/zh/mcp/index.html" },
            { label: "MCP 安装设置", href: "/zh/mcp/setup/index.html" },
            { label: "Server 示例", href: "/zh/mcp/server-examples/index.html" },
            { label: "Server 列表", href: "/zh/mcp/servers/index.html" },
          ],
        },
        modes: {
          label: "模式菜单",
          match: "/zh/modes/",
          items: [
            { label: "模式总页", href: "/zh/modes/index.html" },
            { label: "Plan Mode", href: "/zh/modes/plan-mode/index.html" },
            { label: "Yolo Mode", href: "/zh/modes/yolo-mode/index.html" },
            { label: "Plan vs Yolo", href: "/zh/modes/plan-vs-yolo/index.html" },
          ],
        },
        skills: {
          label: "技能菜单",
          match: "/zh/skills/",
          items: [
            { label: "技能总页", href: "/zh/skills/index.html" },
            { label: "示例", href: "/zh/skills/examples/index.html" },
            { label: "技能 vs 提示词", href: "/zh/skills/vs-prompts/index.html" },
          ],
        },
        comparisons: {
          label: "对比菜单",
          match: "/zh/comparisons/",
          items: [
            { label: "对比总页", href: "/zh/comparisons/index.html" },
            { label: "vs Claude Code", href: "/zh/comparisons/vs-claude-code/index.html" },
            { label: "vs Codex CLI", href: "/zh/comparisons/vs-codex-cli/index.html" },
          ],
        },
        troubleshooting: {
          label: "排错菜单",
          match: "/zh/troubleshooting/",
          items: [
            { label: "排错总页", href: "/zh/troubleshooting/index.html" },
            { label: "Command Not Found", href: "/zh/troubleshooting/command-not-found/index.html" },
            { label: "Homebrew Command Not Found", href: "/zh/troubleshooting/homebrew-command-not-found/index.html" },
            { label: "Provider 排错", href: "/zh/troubleshooting/provider-troubleshooting/index.html" },
            { label: "MCP 排错", href: "/zh/troubleshooting/mcp-troubleshooting/index.html" },
            { label: "Release Binaries", href: "/zh/troubleshooting/release-binaries/index.html" },
          ],
        },
        news: {
          label: "资讯菜单",
          match: "/zh/news/",
          items: [
            { label: "资讯总页", href: "/zh/news/index.html" },
            { label: "什么是 DeepSeek TUI", href: "/zh/news/what-is-deepseek-tui/index.html" },
          ],
        },
      },
    }
  : {
      home: "/index.html",
      switchLabel: "中文",
      sidebarKicker: "Section Menu",
      sidebarIntro: "Open the section list first, then move into the exact article you need.",
      switchHref:
        window.location.pathname === "/" || window.location.pathname === "/index.html"
          ? "/zh/index.html"
          : `/zh${window.location.pathname}`,
      items: [
        { label: "Home", href: "/index.html", match: "/" },
        { label: "Guides", href: "/guides/index.html", match: "/guides/" },
        { label: "Docs", href: "/docs/index.html", match: "/docs/" },
        { label: "Install", href: "/install/index.html", match: "/install/" },
        { label: "Config", href: "/config/index.html", match: "/config/" },
        { label: "MCP", href: "/mcp/index.html", match: "/mcp/" },
        { label: "Modes", href: "/modes/index.html", match: "/modes/" },
        { label: "Skills", href: "/skills/index.html", match: "/skills/" },
        { label: "Comparisons", href: "/comparisons/index.html", match: "/comparisons/" },
        { label: "Troubleshooting", href: "/troubleshooting/index.html", match: "/troubleshooting/" },
        { label: "News", href: "/news/index.html", match: "/news/" },
      ],
      sections: {
        guides: {
          label: "Guide Menu",
          match: "/guides/",
          items: [
            { label: "Guides Hub", href: "/guides/index.html" },
            { label: "Pricing and Cost", href: "/guides/pricing-and-cost/index.html" },
          ],
        },
        docs: {
          label: "Docs Menu",
          match: "/docs/",
          items: [
            { label: "Docs Hub", href: "/docs/index.html" },
            { label: "Install Docs", href: "/docs/install/index.html" },
            { label: "Configuration", href: "/docs/configuration/index.html" },
            { label: "MCP Docs", href: "/docs/mcp/index.html" },
            { label: "Modes Docs", href: "/docs/modes/index.html" },
            { label: "Keybindings", href: "/docs/keybindings/index.html" },
            { label: "Runtime API", href: "/docs/runtime-api/index.html" },
            { label: "Subagents", href: "/docs/subagents/index.html" },
            { label: "Tool Surface", href: "/docs/tool-surface/index.html" },
            { label: "Docker", href: "/docs/docker/index.html" },
            { label: "Memory", href: "/docs/memory/index.html" },
            { label: "Operations Runbook", href: "/docs/operations-runbook/index.html" },
            { label: "Release Runbook", href: "/docs/release-runbook/index.html" },
            { label: "Capacity Controller", href: "/docs/capacity-controller/index.html" },
            { label: "Coordinator Prompt", href: "/docs/v0-8-8-coordinator-prompt/index.html" },
            { label: "Architecture", href: "/docs/architecture/index.html" },
            { label: "Localization", href: "/docs/localization/index.html" },
            { label: "Legacy Rust Audit", href: "/docs/legacy-rust-audit-0-7-6/index.html" },
            { label: "v0.7.5 Plan", href: "/docs/v0-7-5-implementation-plan/index.html" },
            { label: "Competitive Analysis", href: "/docs/competitive-analysis/index.html" },
            { label: "Accessibility", href: "/docs/accessibility/index.html" },
          ],
        },
        install: {
          label: "Install Menu",
          match: "/install/",
          items: [
            { label: "Install Hub", href: "/install/index.html" },
            { label: "Homebrew", href: "/install/homebrew/index.html" },
            { label: "npm", href: "/install/npm/index.html" },
            { label: "Cargo", href: "/install/cargo/index.html" },
            { label: "Windows", href: "/install/windows/index.html" },
            { label: "Update or Upgrade", href: "/install/update-or-upgrade/index.html" },
          ],
        },
        config: {
          label: "Config Menu",
          match: "/config/",
          items: [
            { label: "Config Hub", href: "/config/index.html" },
            { label: "API Key", href: "/config/api-key/index.html" },
            { label: "Provider Setup", href: "/config/provider-setup/index.html" },
            { label: "Provider Cost", href: "/config/provider-cost/index.html" },
            { label: "Environment Variables", href: "/config/environment-variables/index.html" },
            { label: "File Location", href: "/config/file-location/index.html" },
            { label: "Reset Config", href: "/config/reset/index.html" },
          ],
        },
        mcp: {
          label: "MCP Menu",
          match: "/mcp/",
          items: [
            { label: "MCP Hub", href: "/mcp/index.html" },
            { label: "MCP Setup", href: "/mcp/setup/index.html" },
            { label: "Server Examples", href: "/mcp/server-examples/index.html" },
            { label: "Server List", href: "/mcp/servers/index.html" },
          ],
        },
        modes: {
          label: "Modes Menu",
          match: "/modes/",
          items: [
            { label: "Modes Hub", href: "/modes/index.html" },
            { label: "Plan Mode", href: "/modes/plan-mode/index.html" },
            { label: "Yolo Mode", href: "/modes/yolo-mode/index.html" },
            { label: "Plan vs Yolo", href: "/modes/plan-vs-yolo/index.html" },
          ],
        },
        skills: {
          label: "Skills Menu",
          match: "/skills/",
          items: [
            { label: "Skills Hub", href: "/skills/index.html" },
            { label: "Examples", href: "/skills/examples/index.html" },
            { label: "Skills vs Prompts", href: "/skills/vs-prompts/index.html" },
          ],
        },
        comparisons: {
          label: "Comparisons Menu",
          match: "/comparisons/",
          items: [
            { label: "Comparisons Hub", href: "/comparisons/index.html" },
            { label: "vs Claude Code", href: "/comparisons/vs-claude-code/index.html" },
            { label: "vs Codex CLI", href: "/comparisons/vs-codex-cli/index.html" },
          ],
        },
        troubleshooting: {
          label: "Troubleshooting Menu",
          match: "/troubleshooting/",
          items: [
            { label: "Troubleshooting Hub", href: "/troubleshooting/index.html" },
            { label: "Command Not Found", href: "/troubleshooting/command-not-found/index.html" },
            { label: "Homebrew Command Not Found", href: "/troubleshooting/homebrew-command-not-found/index.html" },
            { label: "Provider Troubleshooting", href: "/troubleshooting/provider-troubleshooting/index.html" },
            { label: "MCP Troubleshooting", href: "/troubleshooting/mcp-troubleshooting/index.html" },
            { label: "Release Binaries", href: "/troubleshooting/release-binaries/index.html" },
          ],
        },
        news: {
          label: "News Menu",
          match: "/news/",
          items: [
            { label: "News Hub", href: "/news/index.html" },
            { label: "What Is DeepSeek TUI?", href: "/news/what-is-deepseek-tui/index.html" },
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
