// Publication metadata, contribution notes, official links, figures and demo previews.
// Only explicitly confirmed contribution roles are displayed.
export const ME = "J. Li";

export const publications = [
  {
    "id": "li2026ctvam",
    "title": "CT-VAM: A Cerebello-Thalamic-Inspired Vision-Action Model for Efficient Visuomotor Control",
    "authors": [
      "J. Li",
      "Y. Guo",
      "J. Guo",
      "Q. Liu",
      "J. Qin"
    ],
    "venue": "arXiv preprint",
    "venueShort": "arXiv",
    "year": 2026,
    "links": {
      "arxiv": "https://arxiv.org/abs/2606.09572",
      "video": "https://www.bilibili.com/video/BV1qkEr68E4M/"
    },
    "bibtex": {
      "type": "article",
      "journal": "arXiv preprint arXiv:2606.09572"
    },
    "contribution": "co-first",
    "media": {
      "gif": "./assets/media/ct-vam.gif",
      "poster": "./assets/media/ct-vam.jpg",
      "width": 384,
      "height": 216,
      "alt": {
        "en": "CT-VAM robot manipulation demonstration",
        "zh": "CT-VAM 机器人操作演示"
      },
      "webp": "./assets/media/ct-vam.webp"
    },
    "figure": {
      "src": "./assets/media/figures/ct-vam-overview.webp",
      "thumbnail": "./assets/media/figures/ct-vam-overview-thumb.webp",
      "width": 1382,
      "height": 435,
      "label": {
        "en": "Model overview",
        "zh": "模型概览"
      },
      "alt": {
        "en": "CT-VAM model overview from Figure 1, including architecture and deployment; the dashed high-level module is future work.",
        "zh": "论文图 1：CT-VAM 模型结构与部署概览；虚线高层决策模块属于未来工作。"
      }
    }
  },
  {
    "id": "li2026gpbound",
    "title": "Toward Reliable Probabilistic Robustness: A Nonconservative Uncertainty Bound for Gaussian Processes With Applications to Constrained Motion Control",
    "authors": [
      "J. Li",
      "Q. Liu",
      "Q. Ma",
      "M. Li",
      "J. Qin"
    ],
    "venue": "IEEE Transactions on Control Systems Technology",
    "venueShort": "TCST",
    "year": 2026,
    "links": {
      "publisher": "https://ieeexplore.ieee.org/document/11409465",
      "video": "https://www.bilibili.com/video/BV1TF4m1A7eC/"
    },
    "bibtex": {
      "type": "article",
      "journal": "IEEE Transactions on Control Systems Technology",
      "doi": "10.1109/TCST.2026.3663686",
      "volume": "34",
      "number": "3",
      "pages": "1367--1380"
    },
    "media": {
      "gif": "./assets/media/gp-bound.gif",
      "poster": "./assets/media/gp-bound.jpg",
      "width": 560,
      "height": 350,
      "alt": {
        "en": "Balloon manipulation (top) and writing (bottom), comparing the initial constraint and NCUB",
        "zh": "气球按压（上）与弹性表面书写（下），左列为初始约束，右列为 NCUB"
      },
      "webp": "./assets/media/gp-bound.webp"
    }
  },
  {
    "id": "guo2026dgacmp",
    "title": "DG-ACMP: Deformation-Guided Motion Planning with Acceptable Contacts for Manipulators in Cluttered Environments",
    "authors": [
      "Y. Guo",
      "J. Li",
      "Q. Liu",
      "W. Fu",
      "J. Qin",
      "Y. Kang"
    ],
    "venue": "IEEE Robotics and Automation Letters",
    "venueShort": "RA-L",
    "year": 2026,
    "links": {
      "publisher": "https://ieeexplore.ieee.org/document/11479852",
      "video": "https://www.bilibili.com/video/BV1YP9TBGEzr/"
    },
    "bibtex": {
      "type": "article",
      "journal": "IEEE Robotics and Automation Letters",
      "doi": "10.1109/LRA.2026.3683317",
      "volume": "11",
      "number": "6",
      "pages": "7046--7053"
    },
    "media": {
      "gif": "./assets/media/dg-acmp.gif",
      "poster": "./assets/media/dg-acmp.jpg",
      "width": 384,
      "height": 324,
      "alt": {
        "en": "DG-ACMP contact-aware robot motion planning demonstration",
        "zh": "DG-ACMP 允许接触的机器人运动规划演示"
      },
      "webp": "./assets/media/dg-acmp.webp"
    }
  },
  {
    "id": "jiang2026stgp",
    "title": "Enhancing Mapping Consistency for Motion Consistency: Spatio-Temporal Gaussian Process Maps for Autonomous Navigation in Dynamic Environments",
    "authors": [
      "Z. Jiang",
      "J. Li",
      "Q. Liu",
      "J. Qin"
    ],
    "venue": "IEEE Robotics and Automation Letters",
    "venueShort": "RA-L",
    "year": 2026,
    "links": {
      "publisher": "https://ieeexplore.ieee.org/document/11614467",
      "video": "https://www.bilibili.com/video/BV1WxN36XEQB/"
    },
    "bibtex": {
      "type": "article",
      "journal": "IEEE Robotics and Automation Letters",
      "doi": "10.1109/LRA.2026.3715028",
      "volume": "11",
      "number": "9",
      "pages": "10664--10671"
    },
    "contribution": "co-first",
    "media": {
      "gif": "./assets/media/stgp.gif",
      "poster": "./assets/media/stgp.jpg",
      "width": 320,
      "height": 216,
      "alt": {
        "en": "Navigation with spatio-temporal Gaussian-process maps",
        "zh": "基于时空高斯过程地图的自主导航演示"
      },
      "webp": "./assets/media/stgp.webp"
    },
    "figure": {
      "src": "./assets/media/figures/stgp-consistency.webp",
      "thumbnail": "./assets/media/figures/stgp-consistency-thumb.webp",
      "width": 648,
      "height": 273,
      "label": {
        "en": "Map–motion consistency",
        "zh": "地图与运动一致性"
      },
      "alt": {
        "en": "Figure 1: inconsistent distance-field mapping on the left and the proposed consistent map with a smoother trajectory on the right.",
        "zh": "论文图 1：左侧为不一致的距离场地图，右侧为本文一致地图及更平滑的轨迹。"
      }
    },
    "figureFirst": true
  },
  {
    "id": "ma2026dtcbf",
    "title": "Enhanced Safe Control for Arbitrary Relative Degree: A Generalized Discrete-Time CBF Approach",
    "authors": [
      "Q. Ma",
      "J. Li",
      "Q. Liu",
      "J. Qin",
      "J. Sun"
    ],
    "venue": "Automatica, vol. 189, 113026",
    "venueShort": "Automatica",
    "year": 2026,
    "links": {
      "publisher": "https://www.sciencedirect.com/science/article/pii/S0005109826002104"
    },
    "bibtex": {
      "type": "article",
      "journal": "Automatica",
      "volume": "189",
      "pages": "113026",
      "doi": "10.1016/j.automatica.2026.113026"
    },
    "contribution": "corresponding",
    "figure": {
      "src": "./assets/media/figures/gd-cbf-trajectories.webp",
      "thumbnail": "./assets/media/figures/gd-cbf-trajectories-thumb.webp",
      "width": 872,
      "height": 485,
      "label": {
        "en": "Attitude trajectories",
        "zh": "姿态轨迹对比"
      },
      "alt": {
        "en": "Figure 5: quadrotor body z-axis trajectories under GD-CBF on the left and HO-CBF on the right.",
        "zh": "论文图 5：GD-CBF（左）与 HO-CBF（右）控制下的四旋翼机体 z 轴轨迹。"
      }
    }
  },
  {
    "id": "li2024humanswarm",
    "title": "Game-Based Approximate Optimal Motion Planning for Safe Human-Swarm Interaction",
    "authors": [
      "M. Li",
      "J. Qin",
      "J. Li",
      "Q. Liu",
      "Y. Shi",
      "Y. Kang"
    ],
    "venue": "IEEE Transactions on Cybernetics, 54(10): 5649–5660",
    "venueShort": "T-CYB",
    "year": 2024,
    "links": {
      "publisher": "https://ieeexplore.ieee.org/document/10378739"
    },
    "bibtex": {
      "type": "article",
      "journal": "IEEE Transactions on Cybernetics",
      "volume": "54",
      "number": "10",
      "pages": "5649--5660",
      "doi": "10.1109/TCYB.2023.3340659"
    },
    "figure": {
      "src": "./assets/media/figures/human-swarm-scene.webp",
      "thumbnail": "./assets/media/figures/human-swarm-scene-thumb.webp",
      "width": 869,
      "height": 505,
      "label": {
        "en": "Human–swarm interaction",
        "zh": "人机群协作场景"
      },
      "alt": {
        "en": "Figure 1: composite illustration of a human-guided quadrotor swarm, with a person as an obstacle and a potential collision along the commanded trajectory.",
        "zh": "论文图 1：人引导四旋翼集群的复合场景示意，标出作为障碍物的行人及指令轨迹上可能的碰撞。"
      }
    }
  },
  {
    "id": "li2023uscbf",
    "title": "Robust Safe Learning and Control in an Unknown Environment: An Uncertainty-Separated Control Barrier Function Approach",
    "authors": [
      "J. Li",
      "Q. Liu",
      "W. Jin",
      "J. Qin",
      "S. Hirche"
    ],
    "venue": "IEEE Robotics and Automation Letters, 8(10): 6539–6546",
    "venueShort": "RA-L",
    "year": 2023,
    "links": {
      "publisher": "https://ieeexplore.ieee.org/document/10232876",
      "video": "https://www.bilibili.com/video/BV1aj42197G2/"
    },
    "bibtex": {
      "type": "article",
      "journal": "IEEE Robotics and Automation Letters",
      "volume": "8",
      "number": "10",
      "pages": "6539--6546",
      "doi": "10.1109/LRA.2023.3309130"
    },
    "contribution": "co-first",
    "media": {
      "gif": "./assets/media/us-cbf.gif",
      "poster": "./assets/media/us-cbf.jpg",
      "width": 384,
      "height": 335,
      "alt": {
        "en": "Safe navigation using uncertainty-separated control barrier functions",
        "zh": "基于不确定性分离控制障碍函数的安全导航演示"
      },
      "webp": "./assets/media/us-cbf.webp"
    }
  }
];
