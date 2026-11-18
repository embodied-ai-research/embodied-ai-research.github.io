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
| 个人简介、开源项目介绍、侧边栏链接 | `index.html` |
| 论文列表、共同一作/通讯作者标注、官网和视频链接 | `assets/publications.js` |
| 论文动图、静态预览和片段来源记录 | `assets/media/` |
| 开源项目演示素材和来源记录 | `assets/projects/` |
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

## 论文与演示素材

- 所有论文统一展示，不按第一作者筛选，也不设置普通第一作者徽标。
- `contribution` 仅使用经本人确认的 `co-first`（共同第一作者）或 `corresponding`（通讯作者）。
- 有 arXiv 的论文保留 arXiv 链接，其余标题链接到出版社的正式文章页面。
- `media` 保存动图的 `webp` / `gif`、静态 `poster`、尺寸和中英文 `alt`；优先加载动画 WebP，GIF 用于兼容回退。系统开启减少动态效果时显示静态预览。
- `assets/media/sources.json` 记录每段演示的原视频、起始秒数、时长和裁切区域；保持原视频播放速度。原始完整视频不放入站点仓库。
