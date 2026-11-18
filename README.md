# Jiacheng Li — Personal Homepage

个人学术主页（Embodied AI / Manipulation Learning / Visuomotor Skills）。
纯静态站点（HTML + CSS + 原生 JS），无需构建，可直接部署到 GitHub Pages。

## 本地预览

```bash
npm install
npm run dev        # http://localhost:4627 ，保存文件后浏览器自动刷新
```

## 修改内容

页面中英双语：每段文字都有一对 `data-l="en"` / `data-l="zh"` 元素，修改时两边一起改。
顶部按钮切换语言并记住选择；链接加 `?lang=zh` 可直接打开中文版。

| 想改的内容 | 文件 |
| --- | --- |
| 个人简介、侧边栏链接 | `index.html` |
| 论文列表（作者里写 `"J. Li"` 会自动加粗） | `assets/publications.js` |
| 颜色、字体、布局 | `assets/style.css`（顶部 `:root` 变量） |

## 部署到 GitHub Pages

1. 在 GitHub 上新建仓库 `embodied-ai-research.github.io`（公开）。
2. 推送本仓库：

   ```bash
   git remote add github https://github.com/embodied-ai-research/embodied-ai-research.github.io.git
   git push github main
   ```

3. 仓库 Settings → Pages → Source 选择 `Deploy from a branch`，分支 `main`，目录 `/ (root)`。

直接发布根目录的 `index.html`、`assets/` 和 `.nojekyll`，不运行 `vite build`。

几分钟后访问 <https://embodied-ai-research.github.io>。
