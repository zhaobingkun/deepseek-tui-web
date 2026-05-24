# 文档更新流程

这份站的更新，不要靠记忆做。按下面顺序走。

## 1. 先判断这次改的是哪一类内容

- 如果上游仓库 `docs/*.md` 变了：
  - 运行 `scripts/sync_upstream_docs_fulltext.py`
- 如果你改的是非 `docs` 分支的详情页正文：
  - 运行 `scripts/fill_core_detail_pages.py`
  - 再运行 `scripts/fill_remaining_detail_pages.py`
- 如果你改的是导航、样式或栏目结构：
  - 直接改对应 HTML / CSS / JS

## 2. 上游 docs 同步顺序

在项目根目录运行：

```bash
cd /Users/zhaobingkun/dev/DeepSeek-TUI
python3 scripts/sync_upstream_docs_fulltext.py
```

这一步会做：

- 从 GitHub 上游抓取 `docs/*.md`
- 如果当前没网，会回退到本地缓存 `upstream-docs/`
- 重建：
  - `docs/*`
  - `zh/docs/*`
- 自动生成：
  - 正文 HTML
  - 页内标题锚点
  - 右侧目录
  - 页尾 `Back to top / 回到顶部`

## 3. 非 docs 详情页补正文顺序

如果你改的是这些分支：

- `install/*`
- `config/*`
- `mcp/*`
- `modes/*`
- `guides/*`
- `skills/*`
- `comparisons/*`
- `troubleshooting/*`
- `news/*`

运行：

```bash
cd /Users/zhaobingkun/dev/DeepSeek-TUI
python3 scripts/fill_core_detail_pages.py
python3 scripts/fill_remaining_detail_pages.py
```

其中：

- `fill_core_detail_pages.py`
  - 负责核心详情页
- `fill_remaining_detail_pages.py`
  - 负责剩余那批详情页
  - 也包含 `news/what-is-deepseek-tui`

## 4. 每次更新后都要检查什么

至少检查这几类页面：

### docs 正文页

- `docs/install/index.html`
- `docs/configuration/index.html`
- `docs/mcp/index.html`
- `zh/docs/install/index.html`
- `zh/docs/configuration/index.html`
- `zh/docs/mcp/index.html`

看点：

- 正文有没有完整出来
- 右侧目录能不能看见
- 标题锚点是否正常
- 页尾有没有 `Back to top / 回到顶部`

### 非 docs 详情页

- `install/npm/index.html`
- `config/provider-setup/index.html`
- `modes/plan-mode/index.html`
- `troubleshooting/command-not-found/index.html`
- 对应 `zh/*`

看点：

- 不是提要页
- 第一屏就能回答问题
- 页面里有正文结构，不只是“下一步看什么”

## 5. 建议的本地校验命令

```bash
cd /Users/zhaobingkun/dev/DeepSeek-TUI
python3 -m py_compile scripts/sync_upstream_docs_fulltext.py
python3 -m py_compile scripts/fill_core_detail_pages.py
python3 -m py_compile scripts/fill_remaining_detail_pages.py
node --check assets/js/site.js
python3 -m http.server 4173
```

然后浏览器打开：

- `http://127.0.0.1:4173/docs/install/`
- `http://127.0.0.1:4173/docs/mcp/`
- `http://127.0.0.1:4173/zh/docs/install/`
- `http://127.0.0.1:4173/install/npm/`

## 6. 发布前最后确认

- `docs/*` 和 `zh/docs/*` 不是提要壳
- `news/*` 详情页不是提要壳
- hub 页仍然保持“列表 / 分流”角色
- detail 页保持“正文 / 解决问题”角色

## 7. 这套站现在的原则

- hub 页可以是目录页
- detail 页必须是正文页
- 以后不要再做“只有提要、没有实内容”的详情页
