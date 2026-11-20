import { ME, publications } from "./publications.js?v=20261120-manipscope";

const LINK_LABELS = {
  arxiv: ["arXiv", "arXiv"],
  publisher: ["Paper", "论文官网"],
  project: ["Project page", "项目主页"],
  pdf: ["PDF", "PDF"],
  code: ["Code", "代码"],
  evaluate: ["Evaluate", "评测入口"],
  leaderboard: ["Leaderboard", "排行榜"],
  video: ["Video", "视频"],
  doi: ["DOI", "DOI"],
};

const CONTRIBUTION_LABELS = {
  "co-first": ["Co-first author", "共同第一作者"],
  corresponding: ["Corresponding author", "通讯作者"],
};

const escapeHtml = (s) =>
  String(s).replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c]);

function toBibtex(pub) {
  const { type = "article", ...fields } = pub.bibtex || {};
  const entries = {
    title: `{${pub.title}}`,
    author: pub.authors.join(" and "),
    ...fields,
    year: String(pub.year),
  };
  const body = Object.entries(entries)
    .map(([k, v]) => `  ${k.padEnd(7)} = {${v}}`)
    .join(",\n");
  return `@${type}{${pub.id},\n${body}\n}`;
}

function renderAuthors(authors) {
  return authors
    .map((a) => (a === ME ? `<span class="me">${escapeHtml(a)}</span>` : escapeHtml(a)))
    .join(", ");
}

function renderVisuals(pub) {
  if (!pub.teaser) return "";
  return ["en", "zh"].map(lang => {
    const { src, alt } = pub.teaser[lang];
    return `<a data-l="${lang}" class="paper-teaser" href="${escapeHtml(src)}" target="_blank" rel="noopener">
      <img src="${escapeHtml(src)}" alt="${escapeHtml(alt)}" width="1440" height="960" loading="lazy" decoding="async">
    </a>`;
  }).join("");
}

function renderPub(pub) {
  const contribution = CONTRIBUTION_LABELS[pub.contribution];
  const primary = pub.links.arxiv || pub.links.publisher || pub.links.project || pub.links.pdf || pub.links.doi;

  const titleHtml = primary
    ? `<a href="${escapeHtml(primary)}" target="_blank" rel="noopener">${escapeHtml(pub.title)}</a>`
    : escapeHtml(pub.title);

  const links = Object.entries(LINK_LABELS)
    .filter(([key]) => pub.links[key] || pub.pendingLinks?.includes(key))
    .map(([key, [en, zh]]) => pub.links[key]
      ? `<a href="${escapeHtml(pub.links[key])}" target="_blank" rel="noopener"><span data-l="en">${en}</span><span data-l="zh">${zh}</span></a>`
      : `<button type="button" class="link-pending" disabled><span data-l="en">${en} · coming soon</span><span data-l="zh">${zh} · 待发布</span></button>`);
  links.push(
    `<button type="button" data-bib="${pub.id}" aria-expanded="false" aria-controls="bib-${pub.id}">BibTeX</button>`,
  );

  return `
    <article class="pub${pub.teaser ? " has-media" : ""}" id="${pub.id}">
      ${renderVisuals(pub)}
      <div class="pub-content">
      <h3 class="pub-title">${titleHtml}</h3>
      <p class="pub-authors">${renderAuthors(pub.authors)}</p>
      <p class="pub-venue">
        <span class="badge">${escapeHtml(pub.venueShort)} ${pub.year}</span>
        ${contribution ? `<span class="badge badge-muted"><span data-l="en">${contribution[0]}</span><span data-l="zh">${contribution[1]}</span></span>` : ""}
        <em>${escapeHtml(pub.venue)}</em>
      </p>
      <div class="pub-links">${links.join("")}</div>
      <pre class="bibtex" id="bib-${pub.id}" hidden>${escapeHtml(toBibtex(pub))}</pre>
      </div>
    </article>`;
}

function renderPublications() {
  const list = document.getElementById("pub-list");
  const items = [...publications].sort((a, b) => b.year - a.year);

  if (!items.length) {
    list.innerHTML =
      '<p class="pub-empty"><span data-l="en">Publications will be added here.</span><span data-l="zh">论文将在此处更新。</span></p>';
    return;
  }

  let html = "";
  let currentYear = null;
  for (const pub of items) {
    if (pub.year !== currentYear) {
      currentYear = pub.year;
      html += `<h3 class="pub-year">${currentYear}</h3>`;
    }
    html += renderPub(pub);
  }
  list.innerHTML = html;
}

function initBibtexToggles() {
  document.getElementById("pub-list").addEventListener("click", (e) => {
    const btn = e.target.closest("button[data-bib]");
    if (!btn) return;
    const block = document.getElementById(`bib-${btn.dataset.bib}`);
    const open = block.hidden;
    block.hidden = !open;
    btn.setAttribute("aria-expanded", String(open));
  });
}

function updateThemeControl() {
  const root = document.documentElement;
  const dark = (root.dataset.theme || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light")) === "dark";
  const zh = root.dataset.lang === "zh";
  const label = zh ? (dark ? "切换至浅色模式" : "切换至深色模式") : (dark ? "Switch to light mode" : "Switch to dark mode");
  const button = document.querySelector(".theme-toggle");
  button.setAttribute("aria-label", label);
  button.setAttribute("aria-pressed", String(dark));
  button.title = label;
}

function initThemeToggle() {
  const root = document.documentElement;
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
  document.querySelector(".theme-toggle").addEventListener("click", () => {
    const current = root.dataset.theme || (prefersDark.matches ? "dark" : "light");
    const next = current === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("theme", next);
    updateThemeControl();
  });
  prefersDark.addEventListener("change", updateThemeControl);
  updateThemeControl();
}

function setLang(lang) {
  const root = document.documentElement;
  root.dataset.lang = lang;
  root.lang = lang === "zh" ? "zh-CN" : "en";
  document.title =
    lang === "zh" ? "李嘉诚 · 具身智能与机器人操作" : "Jiacheng Li · Embodied AI & Robot Manipulation";
  document.querySelectorAll("[data-set-lang]").forEach((b) =>
    b.setAttribute("aria-pressed", String(b.dataset.setLang === lang)),
  );
  document.querySelectorAll("[data-alt-en]").forEach((image) => {
    image.alt = lang === "zh" ? image.dataset.altZh : image.dataset.altEn;
  });
  updateThemeControl();
}

function initLangSwitch() {
  setLang(document.documentElement.dataset.lang === "zh" ? "zh" : "en");
  document.querySelectorAll("[data-set-lang]").forEach((btn) =>
    btn.addEventListener("click", () => {
      setLang(btn.dataset.setLang);
    }),
  );
}

function initScrollSpy() {
  const links = [...document.querySelectorAll(".nav a")];
  const sections = links.map((a) => document.querySelector(a.getAttribute("href")));
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        links.forEach((a) => a.classList.toggle("is-current", a.getAttribute("href") === `#${entry.target.id}`));
      });
    },
    { rootMargin: "-40% 0px -55% 0px" },
  );
  sections.forEach((s) => s && observer.observe(s));
}

document.querySelector("[data-year]").textContent = new Date().getFullYear();

renderPublications();
initBibtexToggles();
initThemeToggle();
initLangSwitch();
initScrollSpy();
