// Edit this list to update the Publications section.
// `authors`: write "J. Li" exactly to have your name highlighted.
// `featured`: true gives the entry a soft highlight.
// `links`: any of { arxiv, pdf, project, code, doi, video } — omitted keys are hidden.

export const ME = "J. Li";

export const publications = [
  {
    id: "li2026ctvam",
    title: "CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control",
    authors: ["J. Li", "Y. Guo", "J. Guo", "Q. Liu", "J. Qin"],
    venue: "arXiv preprint",
    venueShort: "arXiv",
    year: 2026,
    featured: true,
    links: { arxiv: "https://arxiv.org/abs/2606.09572" },
    bibtex: {
      type: "article",
      journal: "arXiv preprint arXiv:2606.09572",
    },
  },
  {
    id: "li2026gpbound",
    title:
      "Toward Reliable Probabilistic Robustness: A Nonconservative Uncertainty Bound for Gaussian Processes With Applications to Constrained Motion Control",
    authors: ["J. Li", "Q. Liu", "Q. Ma", "M. Li", "J. Qin"],
    venue: "IEEE Transactions on Control Systems Technology",
    venueShort: "TCST",
    year: 2026,
    featured: true,
    links: {},
    bibtex: { type: "article", journal: "IEEE Transactions on Control Systems Technology" },
  },
  {
    id: "guo2026dgacmp",
    title:
      "DG-ACMP: Deformation-Guided Motion Planning with Acceptable Contacts for Manipulators in Cluttered Environments",
    authors: ["Y. Guo", "J. Li", "Q. Liu", "W. Fu", "J. Qin", "Y. Kang"],
    venue: "IEEE Robotics and Automation Letters",
    venueShort: "RA-L",
    year: 2026,
    links: {},
    bibtex: { type: "article", journal: "IEEE Robotics and Automation Letters" },
  },
  {
    id: "jiang2026stgp",
    title:
      "Enhancing Mapping Consistency for Motion Consistency: Spatio-Temporal Gaussian Process Maps for Autonomous Navigation in Dynamic Environments",
    authors: ["Z. Jiang", "J. Li", "Q. Liu", "J. Qin"],
    venue: "IEEE Robotics and Automation Letters",
    venueShort: "RA-L",
    year: 2026,
    links: {},
    bibtex: { type: "article", journal: "IEEE Robotics and Automation Letters" },
  },
  {
    id: "ma2026dtcbf",
    title: "Enhanced Safe Control for Arbitrary Relative Degree: A Generalized Discrete-Time CBF Approach",
    authors: ["Q. Ma", "J. Li", "Q. Liu", "J. Qin", "J. Sun"],
    venue: "Automatica, vol. 189, 113026",
    venueShort: "Automatica",
    year: 2026,
    links: {},
    bibtex: { type: "article", journal: "Automatica", volume: "189", pages: "113026" },
  },
  {
    id: "li2024humanswarm",
    title: "Game-Based Approximate Optimal Motion Planning for Safe Human-Swarm Interaction",
    authors: ["M. Li", "J. Qin", "J. Li", "Q. Liu", "Y. Shi", "Y. Kang"],
    venue: "IEEE Transactions on Cybernetics, 54(10): 5649–5660",
    venueShort: "T-CYB",
    year: 2024,
    links: {},
    bibtex: {
      type: "article",
      journal: "IEEE Transactions on Cybernetics",
      volume: "54",
      number: "10",
      pages: "5649--5660",
    },
  },
  {
    id: "li2023uscbf",
    title:
      "Robust Safe Learning and Control in an Unknown Environment: An Uncertainty-Separated Control Barrier Function Approach",
    authors: ["J. Li", "Q. Liu", "W. Jin", "J. Qin", "S. Hirche"],
    venue: "IEEE Robotics and Automation Letters, 8(10): 6539–6546",
    venueShort: "RA-L",
    year: 2023,
    featured: true,
    links: {},
    bibtex: {
      type: "article",
      journal: "IEEE Robotics and Automation Letters",
      volume: "8",
      number: "10",
      pages: "6539--6546",
    },
  },
];
