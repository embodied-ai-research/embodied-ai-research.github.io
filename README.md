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
| 基础样式 | `assets/style.css` |
| Apple 风格、颜色、字体、响应式布局 | `assets/apple.css`（顶部 `:root` 变量） |
| 论文配图及来源记录 | `assets/media/figures/` |

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
- `teaser.en` / `teaser.zh` 保存各论文的静态框架图与替代文字；页面随语言切换，点击可查看完整 SVG。
- `scripts/build_teasers.py` 生成 1440 × 960 的中英双语图，统一颜色、字号、图标和连线；内容按每篇论文的真实结构组织。
- `assets/media/teasers/sources.json` 记录论文与图示依据。图中的曲线、地图与场景是方法示意，不是实验结果。
- `assets/media/robots/` 保存具有透明背景的机器人模型渲染、来源和许可证。用 `scripts/render_robot_models.py MODEL_ROOT` 可重新渲染；需要 MuJoCo 3.2.7、NumPy、Pillow 和源模型目录（见 `SOURCES.md`，包含 `franka_hand/hand.xml` 及其 `assets/`）。可用 `--only fr3` 仅渲染带夹爪的 Franka。
- 论文不再显示动图，视频仍通过 Video / 视频链接访问。旧视频和论文截取素材保留在 `assets/media/`，便于追溯。
- 站点使用系统字体，支持浅色/深色模式、减少动态效果、减少透明度和高对比度偏好；手机端将完整框架图放在文章文字上方。
