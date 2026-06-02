# deepseek-tui.app 性能优化计划

更新时间：2026-06-02

基于 PageSpeed Insights 报告：

- 桌面 Performance：63
- 移动 Performance：40
- Accessibility：100
- Best Practices：96
- SEO：100

目标：尽量接近 Lighthouse 100 分。真正冲 100 分需要控制第三方脚本，尤其是 AdSense 和 Google Analytics。

## 结论

当前最大瓶颈不是站内 HTML/CSS/JS 体积，而是第三方脚本。

报告里的主要问题：

- 桌面 Total Blocking Time：1430 ms
- 桌面 JavaScript 执行用时：2.1 s
- 桌面主线程工作：3.8 s
- 移动 FCP：4.6 s
- 移动 LCP：6.3 s
- 移动 CLS：0.869
- 未使用 JS：约 224-225 KiB

主要来源：

- Google AdSense：未使用 JS 约 160 KiB，执行时间约 1.2 s+
- Google Analytics / gtag：未使用 JS 约 65 KiB，执行时间约 645 ms
- Cloudflare Insights：缓存生命周期提示，体积小但不可控
- 本地 `site.js`：体积小，主要负责年份、导航、侧栏，不是主瓶颈

## P0：必须先做

### 1. 延迟或移除 AdSense

优先级：P0  
状态：已执行延迟加载  
预计收益：最高  
影响：可能影响广告展示速度和广告收入统计

当前所有页面在 `<head>` 里直接加载：

```html
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6428701926694635" crossorigin="anonymous"></script>
```

建议方案：

1. 如果目标是 Lighthouse 100：测试环境和关键页面先禁用 AdSense。
2. 如果要保留广告：把 AdSense 延迟到首屏稳定后加载，例如 `requestIdleCallback`、首次滚动、首次点击、或 2500-4000 ms 后加载。
3. 如果使用 Auto Ads：移动端 CLS 风险较高，应考虑关闭自动插入位置，改成固定广告位并预留高度。

建议决策：

- 若短期目标是性能分：先延迟 AdSense。
- 若短期目标是广告收入：保留 AdSense，但接受 Lighthouse 很难 100。

当前执行方式：通过 `assets/js/third-party-loader.js` 在 window `load` 后 3000 ms 加载；如果用户先滚动、点击、触摸或按键，则提前加载。

### 2. 延迟 Google Analytics

优先级：P0  
状态：已执行延迟加载  
预计收益：高  
影响：可能少记极短停留用户和首屏前退出用户

当前所有页面在底部直接加载：

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CLJNJ2GEVB"></script>
```

建议方案：

1. 用轻量本地队列先接收 pageview。
2. 在 `requestIdleCallback` 或 2500 ms 后再加载 gtag。
3. 或只在真实用户交互后加载。

当前执行方式：通过 `assets/js/third-party-loader.js` 延迟初始化 `gtag`，并在加载第三方脚本前先建立本地 `dataLayer` 队列。

### 3. 控制 Auto Ads 导致的移动 CLS

优先级：P0  
预计收益：高，特别是移动端 CLS  
影响：可能减少自动广告位置

移动端 CLS 为 0.869，站内布局本身没有图片首屏，也没有明显大资源插入。最可疑来源是 AdSense Auto Ads 或第三方脚本在移动端插入内容。

建议方案：

1. 关闭 Auto Ads 的页面内自动插入。
2. 使用固定广告容器。
3. 每个广告容器设置 `min-height`，例如 250px 或 280px。
4. 不在首屏 hero 上方或中间插入广告。

需要确认：是否允许调整广告策略。

## P1：已开始执行的安全优化

### 4. 本地脚本改为 defer

优先级：P1  
状态：已执行

所有页面：

```html
<script src="/assets/js/site.js" defer></script>
```

目的：

- 避免本地 JS 参与阻塞解析。
- 保留导航、年份、侧栏功能。
- 该改动不影响广告和统计策略。

### 5. 增加移动布局稳定 CSS

优先级：P1  
状态：已执行

已为首屏终端卡片增加稳定高度，并为后续 section/footer 加入 `content-visibility` 和 `contain-intrinsic-size`。

目的：

- 降低后续区块渲染成本。
- 给首屏右侧终端卡片更稳定的空间。
- 减少移动端 style/layout 工作。

## P2：建议继续做

### 6. 把第三方脚本集中到一个本地 loader

优先级：P2  
状态：已执行  
预计收益：中高  
影响：需要统一改所有 HTML

已新增：

```text
assets/js/third-party-loader.js
```

职责：

- 延迟加载 AdSense。
- 延迟加载 GA。
- 保证只加载一次。
- 支持以后通过一个开关控制广告/统计。

好处：

- 不需要在 100 多个 HTML 页面里重复维护第三方脚本。
- 后续切换策略更简单。

### 7. 页面头部只保留必要资源

优先级：P2  
状态：已执行第三方脚本移出 head  
预计收益：中  

当前 head 里 AdSense 对首屏没有必要。建议 head 只保留：

- title
- meta description
- canonical
- robots
- hreflang
- favicon
- CSS
- JSON-LD

广告和统计全部交给底部 defer loader。

### 8. 验证 Cloudflare Web Analytics / Insights 是否必须

优先级：P2  
预计收益：低到中  

报告里出现：

```text
https://static.cloudflareinsights.com/beacon.min.js
```

如果来自 Cloudflare Web Analytics，可在 Cloudflare 后台关闭或保留。体积不大，但对 Lighthouse 100 有影响。

需要确认：是否需要保留 Cloudflare Web Analytics。

## P3：锦上添花

### 9. CSS 拆分或内联 critical CSS

优先级：P3  
预计收益：低到中

当前 CSS 只有约 4 KB，收益不如处理第三方脚本。若后续仍卡在渲染阻塞，可考虑：

- 首页内联 critical CSS。
- 非首屏 CSS 延迟加载。
- 但维护成本会增加。

### 10. 进一步减少 JS DOM 重写

优先级：P3  
预计收益：低

`site.js` 会重写导航和生成侧栏。它不是主要瓶颈，但如果以后继续追求极限分数，可以：

- 把导航和侧栏在构建时写入 HTML。
- 减少运行时 DOM 操作。

## 推荐执行顺序

1. 已完成：本地 `site.js` 加 `defer`。
2. 已完成：CSS 增加内容可见性和布局稳定规则。
3. 已完成：AdSense 延迟加载。
4. 已完成：GA 延迟加载。
5. 待确认：是否关闭 Cloudflare Web Analytics / Insights。
6. 已完成：新增 `third-party-loader.js`，批量替换所有页面第三方脚本。
7. 部署后重新跑 PSI，重点看移动端 CLS、FCP、LCP。

## 预期结果

如果只做 P1：

- 桌面分数可能小幅提升。
- 移动端可能改善有限。
- 第三方 JS 仍会压制分数。

如果做 P0 + P1：

- 桌面 Performance 有机会接近 95-100。
- 移动 Performance 有机会大幅提升。
- CLS 有机会从 0.869 降到接近 0。

如果保留 AdSense 和 GA 立即加载：

- 100 分目标基本不现实。
- 尤其移动端很难稳定过 90。

## 需要你确认的决策

为了继续冲 100 分，需要确认：

1. 如果移动端 CLS 仍高，是否允许关闭 Auto Ads 或改成固定广告位？
2. 是否需要保留 Cloudflare Web Analytics / Insights？
