import { ME, publications } from "./publications.js";

const LINK_LABELS = {
  project: ["Project page", "项目主页"],
  arxiv: ["arXiv", "arXiv"],
  pdf: ["PDF", "PDF"],
  code: ["Code", "代码"],
  video: ["Video", "视频"],
  doi: ["DOI", "DOI"],
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

function renderPub(pub) {
  const isFirst = pub.authors[0] === ME;
  const primary = pub.links.project || pub.links.arxiv || pub.links.pdf || pub.links.doi;
  const scholarSearch = `https://scholar.google.com/scholar?q=${encodeURIComponent(`"${pub.title}"`)}`;

  const titleHtml = primary
    ? `<a href="${escapeHtml(primary)}" target="_blank" rel="noopener">${escapeHtml(pub.title)}</a>`
    : escapeHtml(pub.title);

  const links = Object.entries(LINK_LABELS)
    .filter(([key]) => pub.links[key])
    .map(([key, [en, zh]]) => `<a href="${escapeHtml(pub.links[key])}" target="_blank" rel="noopener"><span data-l="en">${en}</span><span data-l="zh">${zh}</span></a>`);
  links.push(`<a href="${scholarSearch}" target="_blank" rel="noopener"><span data-l="en">Scholar</span><span data-l="zh">学术搜索</span></a>`);
  links.push(
    `<button type="button" data-bib="${pub.id}" aria-expanded="false" aria-controls="bib-${pub.id}">BibTeX</button>`,
  );

  return `
    <article class="pub${pub.featured ? " is-featured" : ""}" data-first="${isFirst}">
      <h3 class="pub-title">${titleHtml}</h3>
      <p class="pub-authors">${renderAuthors(pub.authors)}</p>
      <p class="pub-venue">
        <span class="badge">${escapeHtml(pub.venueShort)} ${pub.year}</span>
        ${isFirst ? '<span class="badge badge-muted"><span data-l="en">First author</span><span data-l="zh">第一作者</span></span>' : ""}
        <em>${escapeHtml(pub.venue)}</em>
      </p>
      <div class="pub-links">${links.join("")}</div>
      <pre class="bibtex" id="bib-${pub.id}" hidden>${escapeHtml(toBibtex(pub))}</pre>
    </article>`;
}

function renderPublications(filter) {
  const list = document.getElementById("pub-list");
  const items = publications
    .filter((p) => filter !== "first" || p.authors[0] === ME)
    .sort((a, b) => b.year - a.year);

  if (!items.length) {
    list.innerHTML =
      '<p class="pub-empty"><span data-l="en">No publications match this filter yet.</span><span data-l="zh">暂无符合条件的论文。</span></p>';
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

function initFilter() {
  const buttons = document.querySelectorAll(".filter button");
  buttons.forEach((btn) =>
    btn.addEventListener("click", () => {
      buttons.forEach((b) => {
        const active = b === btn;
        b.classList.toggle("is-active", active);
        b.setAttribute("aria-selected", String(active));
      });
      renderPublications(btn.dataset.filter);
    }),
  );
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

function initThemeToggle() {
  const root = document.documentElement;
  const prefersDark = window.matchMedia("(prefers-color-scheme: dark)");
  document.querySelector(".theme-toggle").addEventListener("click", () => {
    const current = root.dataset.theme || (prefersDark.matches ? "dark" : "light");
    const next = current === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    localStorage.setItem("theme", next);
  });
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
}

function initLangSwitch() {
  setLang(document.documentElement.dataset.lang === "zh" ? "zh" : "en");
  document.querySelectorAll("[data-set-lang]").forEach((btn) =>
    btn.addEventListener("click", () => {
      setLang(btn.dataset.setLang);
      localStorage.setItem("lang", btn.dataset.setLang);
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

renderPublications("all");
initFilter();
initBibtexToggles();
initThemeToggle();
initLangSwitch();
initScrollSpy();
