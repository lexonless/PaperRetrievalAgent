# Paper Search Debug Trace

**Query:** Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

Return 5-10 relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining whether the paper is a direct match or a closely related paper, and why

Then summarize:
- major method categories
- recent trends
- open challenges

Rank the most directly relevant papers first, but do not over-filter papers merely because they use multi-stage pipelines or different wording for the same task.
**Generated At:** 2026-03-24T22:03:44
**Stop Reason:** Text 'TERMINATE' mentioned

## Run Summary

- Stop reason: `Text 'TERMINATE' mentioned`
- Total messages: `14`
- Planner JSON messages: `2`
- Retrieval JSON messages: `2`
- Review decisions seen: `2`
- Tool activity events: `4`

## Planner Outputs

### Planner Output 2

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research (2022-2026) on methods for reconstructing or generating B-rep (CAD boundary representation) models directly from point cloud data, to understand the state of the art, major approaches, trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "B-rep reconstruction from point clouds",
    "point cloud to CAD",
    "boundary representation generation",
    "geometric deep learning for CAD reconstruction",
    "reverse engineering from scans"
  ],
  "exclude_areas": [
    "mesh reconstruction only",
    "surface reconstruction without B-rep",
    "pure segmentation/classification",
    "point cloud registration only",
    "B-rep from images only"
  ],
  "fallback_queries": [
    "point cloud to CAD reconstruction",
    "B-rep reconstruction deep learning",
    "reverse engineering point cloud CAD"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2022",
      "reason": "Direct search for the core task in the start year of the range."
    },
    {
      "query": "deep learning B-rep generation from point clouds",
      "reason": "Captures recent data-driven and learning-based approaches."
    },
    {
      "query": "CAD boundary representation reconstruction from scanned point cloud",
      "reason": "Broader phrasing to catch reverse engineering and scanning literature."
    }
  ],
  "assumptions": [
    "The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.",
    "Papers on 'CAD reconstruction from point clouds' inherently target B-rep outputs.",
    "Multi-stage pipelines (e.g., point cloud -> primitive fitting -> B-rep) are relevant.",
    "The user wants a mix of direct matches and substantial contributions to sub-problems like primitive detection or segmentation that feed into B-rep creation."
  ],
  "success_criteria": [
    "Retrieve at least 5-10 papers from 2022-2026 that are directly about or substantially contribute to B-rep reconstruction from point clouds.",
    "Identify clear method categories (e.g., learning-based primitive fitting, optimization-based, hybrid).",
    "Capture recent trends such as the use of transformers or diffusion models.",
    "Highlight open challenges like handling complex topology or noisy data."
  ]
}
```

### Planner Output 8

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research (2022-2026) on methods for reconstructing or generating B-rep (CAD boundary representation) models directly from point cloud data, to understand the state of the art, major approaches, trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "B-rep reconstruction from point clouds",
    "point cloud to CAD",
    "boundary representation generation",
    "geometric deep learning for CAD reconstruction",
    "reverse engineering from scans"
  ],
  "exclude_areas": [
    "mesh reconstruction only",
    "surface reconstruction without B-rep",
    "pure segmentation/classification",
    "point cloud registration only",
    "B-rep from images only"
  ],
  "fallback_queries": [
    "reverse engineering point cloud CAD",
    "point cloud to parametric CAD",
    "B-rep from scan deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Direct core query, now without year suffix to capture all relevant papers in the range."
    },
    {
      "query": "reverse engineering CAD from point cloud deep learning",
      "reason": "Targets the reverse engineering aspect with a learning focus, likely to yield core methods."
    },
    {
      "query": "parametric CAD model reconstruction from 3D scan",
      "reason": "Broader phrasing to capture papers that might use 'parametric CAD' or '3D scan' synonymously."
    }
  ],
  "assumptions": [
    "The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.",
    "Papers on 'CAD reconstruction from point clouds' inherently target B-rep outputs.",
    "Multi-stage pipelines (e.g., point cloud -> primitive fitting -> B-rep) are relevant.",
    "The user wants a mix of direct matches and substantial contributions to sub-problems like primitive detection or segmentation that feed into B-rep creation.",
    "Based on the Reviewer's feedback, we need to verify core method fit by ensuring abstracts explicitly mention point cloud input and B-rep/CAD model output."
  ],
  "success_criteria": [
    "Retrieve at least 5-10 papers from 2022-2026 that are directly about or substantially contribute to B-rep reconstruction from point clouds, with clear evidence from abstracts.",
    "Identify clear method categories (e.g., learning-based primitive fitting, optimization-based, hybrid).",
    "Capture recent trends such as the use of transformers or diffusion models.",
    "Highlight open challenges like handling complex topology or noisy data.",
    "Ensure relevance notes are specific and based on concrete evidence, not generic matches."
  ]
}
```

## Retrieval Outputs

### Retrieval Output 6

- Summary: 10 papers from 3 sources, supported_evidence=10, in_range=10

```json
{
  "sources_used": [
    "Crossref",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "point cloud to B-rep reconstruction 2022",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "deep learning B-rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD boundary representation reconstruction from scanned point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-05-04T09:42:03Z",
      "url": "http://arxiv.org/abs/2505.02043v3",
      "doi": "",
      "authors": [
        "Xinzhu Ma",
        "Cheng Wang",
        "Chen Tang",
        "Bin Wang",
        "Shixiang Tang",
        "Yuan Meng",
        "Yunhong Wang",
        "Di Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
      ]
    },
    {
      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-02-27T16:53:16Z",
      "url": "http://arxiv.org/abs/2402.17678v1",
      "doi": "",
      "authors": [
        "Mohammad Sadil Khan",
        "Elona Dupont",
        "Sk Aziz Ali",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    },
    {
      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-12-18T16:55:42Z",
      "url": "http://arxiv.org/abs/2412.14042v2",
      "doi": "",
      "authors": [
        "Danila Rukhovich",
        "Elona Dupont",
        "Dimitrios Mallis",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-12-28",
      "url": "https://doi.org/10.1093/jcde/qwae005",
      "doi": "10.1093/jcde/qwae005",
      "authors": [
        "Shuming Zhang",
        "Zhidong Guan",
        "Hao Jiang",
        "Ning Tao",
        "Xiaodong Wang",
        "Pingan Tan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'deep learning brep generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-05-29T05:30:33Z",
      "url": "http://arxiv.org/abs/2205.14573v1",
      "doi": "",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction 2022'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-10-04T08:00:05Z",
      "url": "http://arxiv.org/abs/2310.02638v1",
      "doi": "",
      "authors": [
        "Zhihao Zong",
        "Fazhi He",
        "Rubin Fan",
        "Yuxin Liu"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-12-07T08:23:44Z",
      "url": "http://arxiv.org/abs/2312.04962v1",
      "doi": "",
      "authors": [
        "Yujia Liu",
        "Anton Obukhov",
        "Jan Dirk Wegner",
        "Konrad Schindler"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"
      ]
    },
    {
      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-06-15T16:27:01Z",
      "url": "http://arxiv.org/abs/2206.07636v2",
      "doi": "",
      "authors": [
        "Chiara Romanengo",
        "Andrea Raffo",
        "Silvia Biasotti",
        "Bianca Falcidieno",
        "Vlassis Fotis",
        "Ioannis Romanelis",
        "Eleftheria Psatha",
        "Konstantinos Moustakas"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction 2022'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-11-07T18:31:08Z",
      "url": "http://arxiv.org/abs/2411.04954v3",
      "doi": "",
      "authors": [
        "Jingwei Xu",
        "Chenyu Wang",
        "Zibo Zhao",
        "Wen Liu",
        "Yi Ma",
        "Shenghua Gao"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    },
    {
      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",
      "source": "Crossref / Remote Sensing",
      "year": 2023,
      "date": "2023-7-17",
      "url": "https://doi.org/10.3390/rs15143578",
      "doi": "10.3390/rs15143578",
      "authors": [
        "Galadrielle Humblot-Renaux",
        "Simon Buus Jensen",
        "Andreas Møgelmose"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "reverse engineering point cloud CAD"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2022",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2022",
      "deep learning B-rep generation from point clouds",
      "CAD boundary representation reconstruction from scanned point cloud"
    ],
    "fallback_used": false
  }
}
```

### Retrieval Output 12

- Summary: 12 papers from 3 sources, supported_evidence=12, in_range=12

```json
{
  "sources_used": [
    "Crossref",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "reverse engineering CAD from point cloud deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "parametric CAD model reconstruction from 3D scan",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-12-18T16:55:42Z",
      "url": "http://arxiv.org/abs/2412.14042v2",
      "doi": "",
      "authors": [
        "Danila Rukhovich",
        "Elona Dupont",
        "Dimitrios Mallis",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-05-29",
      "url": "http://arxiv.org/abs/2205.14573",
      "doi": "10.48550/arxiv.2205.14573",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-05-29T05:30:33Z",
      "url": "http://arxiv.org/abs/2205.14573v1",
      "doi": "",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-12-28",
      "url": "https://doi.org/10.1093/jcde/qwae005",
      "doi": "10.1093/jcde/qwae005",
      "authors": [
        "Shuming Zhang",
        "Zhidong Guan",
        "Hao Jiang",
        "Ning Tao",
        "Xiaodong Wang",
        "Pingan Tan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-07-26",
      "url": "https://doi.org/10.1145/3730842",
      "doi": "10.1145/3730842",
      "authors": [
        "Yilin Liu",
        "Duoteng Xu",
        "Xingyao Yu",
        "Xiang Xu",
        "Daniel Cohen‐Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ]
    },
    {
      "title": "ComplexGen",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-07-01",
      "url": "https://doi.org/10.1145/3528223.3530078",
      "doi": "10.1145/3528223.3530078",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ]
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref | OpenAlex",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "yihang fu",
        "jing li",
        "Falai Chen",
        "Yihang Fu",
        "Jing Li",
        "FaLai Chen"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
    {
      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-10-27T15:33:51Z",
      "url": "http://arxiv.org/abs/2510.23429v1",
      "doi": "",
      "authors": [
        "Ahmet Serdar Karadeniz",
        "Dimitrios Mallis",
        "Danila Rukhovich",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'parametric cad model reconstruction from 3d scan'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"
      ]
    },
    {
      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-07-19",
      "url": "https://doi.org/10.1145/3658155",
      "doi": "10.1145/3658155",
      "authors": [
        "Yilin Liu",
        "Jiale Chen",
        "Shanshan Pan",
        "Daniel Cohen‐Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-11-07T18:31:08Z",
      "url": "http://arxiv.org/abs/2411.04954v3",
      "doi": "",
      "authors": [
        "Jingwei Xu",
        "Chenyu Wang",
        "Zibo Zhao",
        "Wen Liu",
        "Yi Ma",
        "Shenghua Gao"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    },
    {
      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-09-03",
      "url": "https://doi.org/10.3233/ica-240744",
      "doi": "10.3233/ica-240744",
      "authors": [
        "Rubin Fan",
        "Fazhi He",
        "Yuxin Liu",
        "Yupeng Song",
        "Linkun Fan",
        "Xiaohu Yan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ]
    },
    {
      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-24",
      "url": "https://doi.org/10.1016/j.autcon.2022.104440",
      "doi": "10.1016/j.autcon.2022.104440",
      "authors": [
        "Shanaka Kristombu Baduge",
        "Sadeep Thilakarathna",
        "Jude Shalitha Perera",
        "Mehrdad Arashpour",
        "P. Sharafi",
        "Bertrand Teodosio",
        "Ankit Shringi",
        "Priyan Mendis"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 14 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "reverse engineering point cloud CAD",
      "point cloud to parametric CAD",
      "B-rep from scan deep learning"
    ],
    "effective_query": "reverse engineering CAD from point cloud deep learning",
    "used_override_query": true,
    "executed_queries": [
      "reverse engineering CAD from point cloud deep learning",
      "point cloud to B-rep reconstruction",
      "parametric CAD model reconstruction from 3D scan"
    ],
    "fallback_used": false
  }
}
```

## Review Decisions

### Review 7

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval captured a promising set of recent papers (2022-2025) on the target topic, with good source coverage and metadata. However, the evidence for core-method fit is insufficient. The relevance notes are generic, and the evidence snippets are too brief to confidently determine if each paper is a direct match for B-rep reconstruction from point clouds, as opposed to related tasks like CAD generation from other inputs or point cloud segmentation. The hard requirement for core-method fit is not met because we cannot verify that at least 3 papers are core candidates based on the provided evidence.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 2,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "At least 3 distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, the relevance cannot be confidently assessed. The relevance notes are generic ('Abstract or excerpt matched retrieval query terms...'), and the evidence snippets are too short to confirm clear alignment with the user's topic of B-rep reconstruction from point clouds. For example, 'CAD-MLLM' appears to be about multimodal CAD generation, not specifically from point clouds. 'From CAD Models to Soft Point Cloud Labels' is about annotation for segmentation, not reconstruction. Without clearer evidence, we cannot confirm at least 2-3 are clearly aligned."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the explicit time constraint. The set appears focused on CAD/B-rep and point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be verified. The evidence snippets and relevance notes are insufficient to determine if at least 3 papers are plausibly core candidates for B-rep reconstruction from point clouds. Papers like 'SHREC 2022' are about primitive fitting benchmarks, not necessarily B-rep reconstruction. 'CAD-MLLM' is about multimodal generation. 'From CAD Models to Soft Point Cloud Labels' is about annotation. We need clearer evidence from abstracts or content to confirm their role as core methods for the user's task."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range. No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major evidence hole or over-reliance on one weak source is apparent. The set covers various approaches (primitive prediction, sequence generation, chain complexes)."
    }
  },
  "key_risks": [
    "Relevance of several papers is ambiguous based on current evidence snippets.",
    "Potential inclusion of papers that are adjacent (e.g., benchmark, annotation, multimodal generation) rather than core reconstruction methods.",
    "Evidence snippets are truncated and do not clearly state the input (point cloud) and output (B-rep) for all candidates."
  ],
  "next_actions": [
    "For each candidate paper, especially those with ambiguous titles (e.g., 'CAD-MLLM', 'SHREC 2022', 'From CAD Models to Soft Point Cloud Labels'), retrieve and present a more complete abstract or introductory paragraph that explicitly mentions the input (point cloud) and output (B-rep/CAD model).",
    "Re-rank the papers based on the strengthened evidence, placing direct matches (point cloud -> B-rep) first and clearly labeling closely related contributions.",
    "If the evidence reveals some papers are not directly relevant, consider executing a fallback query (e.g., 'reverse engineering point cloud CAD') to find additional core candidates to ensure at least 5 strong papers remain."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has improved, with several papers appearing highly relevant (e.g., CAD-Recode, ComplexGen, Point2Brep, MiCADangelo). However, the evidence snippets remain truncated and the relevance notes are still generic, making it difficult to confidently verify core-method fit. Furthermore, the set contains duplicates (ComplexGen appears three times) and includes papers that are clearly off-topic (e.g., a review on AI in construction, a dataset paper). The hard requirements for candidate depth (non-duplicate count) and core-method fit are not met due to insufficient evidence and contamination by irrelevant entries.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "At least 3 distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After accounting for duplicates (ComplexGen appears 3 times), the number of unique candidate papers is less than 5. The list also includes clearly irrelevant papers (e.g., the construction review), further reducing the count of valid candidates."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be confidently assessed. While some titles look promising, the evidence snippets are too brief and the relevance notes are generic. Papers like 'Artificial intelligence and smart vision for building and construction 4.0' are clearly not about B-rep reconstruction from point clouds. 'A parametric and feature-based CAD dataset' is about a dataset, not reconstruction. Without clearer evidence, we cannot confirm at least 2-3 are clearly aligned."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the time constraint. The queries executed are aligned with the topic."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be verified. The evidence snippets are truncated and do not explicitly confirm point cloud input and B-rep output for most papers. The presence of duplicates and off-topic papers further obscures the count of core candidates. We need clear abstracts to confirm papers like 'Point2Brep', 'MiCADangelo', 'Split-and-Fit', and 'HoLa' are indeed about reconstruction from point clouds."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major evidence hole, but the set is cluttered with duplicates and irrelevant papers."
    }
  },
  "key_risks": [
    "High duplication rate (ComplexGen appears 3 times) inflates the candidate count.",
    "Inclusion of clearly irrelevant papers (construction review, dataset paper) reduces signal-to-noise.",
    "Evidence snippets are still truncated, preventing verification of core method fit.",
    "Relevance notes remain generic and unhelpful."
  ],
  "next_actions": [
    "Deduplicate the list rigorously by DOI, URL, and normalized title. Remove all duplicate entries of 'ComplexGen' and any other duplicates.",
    "Filter out clearly irrelevant papers based on title and snippet inspection (e.g., 'Artificial intelligence and smart vision for building and construction 4.0', 'A parametric and feature-based CAD dataset').",
    "For the remaining unique and potentially relevant papers (e.g., CAD-Recode, ComplexGen, Point2Brep, MiCADangelo, Split-and-Fit, HoLa, Brep2Seq), retrieve and present the full abstract or a substantial paragraph that explicitly states the input (point cloud/3D scan) and output (B-rep/CAD model).",
    "If after deduplication and filtering the number of unique, relevant candidates falls below 5, execute a targeted fallback query (e.g., 'point cloud to parametric CAD reconstruction 2024') to find additional core papers."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_JVQ4HxRKldZuRzRPSwNXmo5B', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2022",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "deep learning B-rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD boundary representation reconstruction from scanned point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'deep learning brep generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction 2022\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-07T08:23:44Z",\n      "url": "http://arxiv.org/abs/2312.04962v1",\n      "doi": "",\n      "authors": [\n        "Yujia Liu",\n        "Anton Obukhov",\n        "Jan Dirk Wegner",\n        "Konrad Schindler"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"\n      ]\n    },\n    {\n      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-06-15T16:27:01Z",\n      "url": "http://arxiv.org/abs/2206.07636v2",\n      "doi": "",\n      "authors": [\n        "Chiara Romanengo",\n        "Andrea Raffo",\n        "Silvia Biasotti",\n        "Bianca Falcidieno",\n        "Vlassis Fotis",\n        "Ioannis Romanelis",\n        "Eleftheria Psatha",\n        "Konstantinos Moustakas"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction 2022\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "reverse engineering point cloud CAD"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2022",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2022",\n      "deep learning B-rep generation from point clouds",\n      "CAD boundary representation reconstruction from scanned point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_JVQ4HxRKldZuRzRPSwNXmo5B' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_s1S4GXRnU7kynMsDs6fOecie', arguments='{"top_k": 12, "max_results_per_source": 25, "query": "reverse engineering CAD from point cloud deep learning"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "reverse engineering CAD from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "parametric CAD model reconstruction from 3D scan",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-10-27T15:33:51Z",\n      "url": "http://arxiv.org/abs/2510.23429v1",\n      "doi": "",\n      "authors": [\n        "Ahmet Serdar Karadeniz",\n        "Dimitrios Mallis",\n        "Danila Rukhovich",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'parametric cad model reconstruction from 3d scan\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ]\n    },\n    {\n      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-24",\n      "url": "https://doi.org/10.1016/j.autcon.2022.104440",\n      "doi": "10.1016/j.autcon.2022.104440",\n      "authors": [\n        "Shanaka Kristombu Baduge",\n        "Sadeep Thilakarathna",\n        "Jude Shalitha Perera",\n        "Mehrdad Arashpour",\n        "P. Sharafi",\n        "Bertrand Teodosio",\n        "Ankit Shringi",\n        "Priyan Mendis"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 14 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "reverse engineering point cloud CAD",\n      "point cloud to parametric CAD",\n      "B-rep from scan deep learning"\n    ],\n    "effective_query": "reverse engineering CAD from point cloud deep learning",\n    "used_override_query": true,\n    "executed_queries": [\n      "reverse engineering CAD from point cloud deep learning",\n      "point cloud to B-rep reconstruction",\n      "parametric CAD model reconstruction from 3D scan"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_s1S4GXRnU7kynMsDs6fOecie' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search research from the last 5 years on reconstructing B-rep models from point clouds.

```text
Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

Return 5-10 relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining whether the paper is a direct match or a closely related paper, and why

Then summarize:
- major method categories
- recent trends
- open challenges

Rank the most directly relevant papers first, but do not over-filter papers merely because they use multi-stage pipelines or different wording for the same task.

[Runtime Search Context]
Today's date for this run is 2026-03-24.
- Resolve "last 5 years" as the inclusive year window 2022-2026.
- Treat that resolved year window as authoritative unless a later agent explicitly labels a broader range as an extra.
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3, years=2022-2026

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research (2022-2026) on methods for reconstructing or generating B-rep (CAD boundary representation) models directly from point cloud data, to understand the state of the art, major approaches, trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep reconstruction from point clouds", "point cloud to CAD", "boundary representation generation", "geometric deep learning for CAD reconstruction", "reverse engineering from scans"],
  "exclude_areas": ["mesh reconstruction only", "surface reconstruction without B-rep", "pure segmentation/classification", "point cloud registration only", "B-rep from images only"],
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep reconstruction deep learning", "reverse engineering point cloud CAD"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2022",
      "reason": "Direct search for the core task in the start year of the range."
    },
    {
      "query": "deep learning B-rep generation from point clouds",
      "reason": "Captures recent data-driven and learning-based approaches."
    },
    {
      "query": "CAD boundary representation reconstruction from scanned point cloud",
      "reason": "Broader phrasing to catch reverse engineering and scanning literature."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.", "Papers on 'CAD reconstruction from point clouds' inherently target B-rep outputs.", "Multi-stage pipelines (e.g., point cloud -> primitive fitting -> B-rep) are relevant.", "The user wants a mix of direct matches and substantial contributions to sub-problems like primitive detection or segmentation that feed into B-rep creation."],
  "success_criteria": ["Retrieve at least 5-10 papers from 2022-2026 that are directly about or substantially contribute to B-rep reconstruction from point clouds.", "Identify clear method categories (e.g., learning-based primitive fitting, optimization-based, hybrid).", "Capture recent trends such as the use of transformers or diffusion models.", "Highlight open challenges like handling complex topology or noisy data."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find relevant papers on B-rep reconstruction from point clouds from 2022-2026.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_JVQ4HxRKldZuRzRPSwNXmo5B', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2022",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "deep learning B-rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD boundary representation reconstruction from scanned point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'deep learning brep generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction 2022\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-07T08:23:44Z",\n      "url": "http://arxiv.org/abs/2312.04962v1",\n      "doi": "",\n      "authors": [\n        "Yujia Liu",\n        "Anton Obukhov",\n        "Jan Dirk Wegner",\n        "Konrad Schindler"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"\n      ]\n    },\n    {\n      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-06-15T16:27:01Z",\n      "url": "http://arxiv.org/abs/2206.07636v2",\n      "doi": "",\n      "authors": [\n        "Chiara Romanengo",\n        "Andrea Raffo",\n        "Silvia Biasotti",\n        "Bianca Falcidieno",\n        "Vlassis Fotis",\n        "Ioannis Romanelis",\n        "Eleftheria Psatha",\n        "Konstantinos Moustakas"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction 2022\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'cad brep reconstruction from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "reverse engineering point cloud CAD"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2022",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2022",\n      "deep learning B-rep generation from point clouds",\n      "CAD boundary representation reconstruction from scanned point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_JVQ4HxRKldZuRzRPSwNXmo5B' is_error=False
```

### Message 6

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Structured retrieval output: papers=10, sources=3, supported_evidence=10, in_range=10

```text
{
  "sources_used": [
    "Crossref",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "point cloud to B-rep reconstruction 2022",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "deep learning B-rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD boundary representation reconstruction from scanned point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-05-04T09:42:03Z",
      "url": "http://arxiv.org/abs/2505.02043v3",
      "doi": "",
      "authors": [
        "Xinzhu Ma",
        "Cheng Wang",
        "Chen Tang",
        "Bin Wang",
        "Shixiang Tang",
        "Yuan Meng",
        "Yunhong Wang",
        "Di Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
      ]
    },
    {
      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-02-27T16:53:16Z",
      "url": "http://arxiv.org/abs/2402.17678v1",
      "doi": "",
      "authors": [
        "Mohammad Sadil Khan",
        "Elona Dupont",
        "Sk Aziz Ali",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    },
    {
      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-12-18T16:55:42Z",
      "url": "http://arxiv.org/abs/2412.14042v2",
      "doi": "",
      "authors": [
        "Danila Rukhovich",
        "Elona Dupont",
        "Dimitrios Mallis",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-12-28",
      "url": "https://doi.org/10.1093/jcde/qwae005",
      "doi": "10.1093/jcde/qwae005",
      "authors": [
        "Shuming Zhang",
        "Zhidong Guan",
        "Hao Jiang",
        "Ning Tao",
        "Xiaodong Wang",
        "Pingan Tan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'deep learning brep generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-05-29T05:30:33Z",
      "url": "http://arxiv.org/abs/2205.14573v1",
      "doi": "",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction 2022'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-10-04T08:00:05Z",
      "url": "http://arxiv.org/abs/2310.02638v1",
      "doi": "",
      "authors": [
        "Zhihao Zong",
        "Fazhi He",
        "Rubin Fan",
        "Yuxin Liu"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-12-07T08:23:44Z",
      "url": "http://arxiv.org/abs/2312.04962v1",
      "doi": "",
      "authors": [
        "Yujia Liu",
        "Anton Obukhov",
        "Jan Dirk Wegner",
        "Konrad Schindler"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"
      ]
    },
    {
      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-06-15T16:27:01Z",
      "url": "http://arxiv.org/abs/2206.07636v2",
      "doi": "",
      "authors": [
        "Chiara Romanengo",
        "Andrea Raffo",
        "Silvia Biasotti",
        "Bianca Falcidieno",
        "Vlassis Fotis",
        "Ioannis Romanelis",
        "Eleftheria Psatha",
        "Konstantinos Moustakas"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction 2022'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-11-07T18:31:08Z",
      "url": "http://arxiv.org/abs/2411.04954v3",
      "doi": "",
      "authors": [
        "Jingwei Xu",
        "Chenyu Wang",
        "Zibo Zhao",
        "Wen Liu",
        "Yi Ma",
        "Shenghua Gao"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    },
    {
      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",
      "source": "Crossref / Remote Sensing",
      "year": 2023,
      "date": "2023-7-17",
      "url": "https://doi.org/10.3390/rs15143578",
      "doi": "10.3390/rs15143578",
      "authors": [
        "Galadrielle Humblot-Renaux",
        "Simon Buus Jensen",
        "Andreas Møgelmose"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'cad brep reconstruction from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "reverse engineering point cloud CAD"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2022",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2022",
      "deep learning B-rep generation from point clouds",
      "CAD boundary representation reconstruction from scanned point cloud"
    ],
    "fallback_used": false
  }
}
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=8

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval captured a promising set of recent papers (2022-2025) on the target topic, with good source coverage and metadata. However, the evidence for core-method fit is insufficient. The relevance notes are generic, and the evidence snippets are too brief to confidently determine if each paper is a direct match for B-rep reconstruction from point clouds, as opposed to related tasks like CAD generation from other inputs or point cloud segmentation. The hard requirement for core-method fit is not met because we cannot verify that at least 3 papers are core candidates based on the provided evidence.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 2,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "At least 3 distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, the relevance cannot be confidently assessed. The relevance notes are generic ('Abstract or excerpt matched retrieval query terms...'), and the evidence snippets are too short to confirm clear alignment with the user's topic of B-rep reconstruction from point clouds. For example, 'CAD-MLLM' appears to be about multimodal CAD generation, not specifically from point clouds. 'From CAD Models to Soft Point Cloud Labels' is about annotation for segmentation, not reconstruction. Without clearer evidence, we cannot confirm at least 2-3 are clearly aligned."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the explicit time constraint. The set appears focused on CAD/B-rep and point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be verified. The evidence snippets and relevance notes are insufficient to determine if at least 3 papers are plausibly core candidates for B-rep reconstruction from point clouds. Papers like 'SHREC 2022' are about primitive fitting benchmarks, not necessarily B-rep reconstruction. 'CAD-MLLM' is about multimodal generation. 'From CAD Models to Soft Point Cloud Labels' is about annotation. We need clearer evidence from abstracts or content to confirm their role as core methods for the user's task."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range. No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major evidence hole or over-reliance on one weak source is apparent. The set covers various approaches (primitive prediction, sequence generation, chain complexes)."
    }
  },
  "key_risks": [
    "Relevance of several papers is ambiguous based on current evidence snippets.",
    "Potential inclusion of papers that are adjacent (e.g., benchmark, annotation, multimodal generation) rather than core reconstruction methods.",
    "Evidence snippets are truncated and do not clearly state the input (point cloud) and output (B-rep) for all candidates."
  ],
  "next_actions": [
    "For each candidate paper, especially those with ambiguous titles (e.g., 'CAD-MLLM', 'SHREC 2022', 'From CAD Models to Soft Point Cloud Labels'), retrieve and present a more complete abstract or introductory paragraph that explicitly mentions the input (point cloud) and output (B-rep/CAD model).",
    "Re-rank the papers based on the strengthened evidence, placing direct matches (point cloud -> B-rep) first and clearly labeling closely related contributions.",
    "If the evidence reveals some papers are not directly relevant, consider executing a fallback query (e.g., 'reverse engineering point cloud CAD') to find additional core candidates to ensure at least 5 strong papers remain."
  ]
}
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3, years=2022-2026

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research (2022-2026) on methods for reconstructing or generating B-rep (CAD boundary representation) models directly from point cloud data, to understand the state of the art, major approaches, trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep reconstruction from point clouds", "point cloud to CAD", "boundary representation generation", "geometric deep learning for CAD reconstruction", "reverse engineering from scans"],
  "exclude_areas": ["mesh reconstruction only", "surface reconstruction without B-rep", "pure segmentation/classification", "point cloud registration only", "B-rep from images only"],
  "fallback_queries": ["reverse engineering point cloud CAD", "point cloud to parametric CAD", "B-rep from scan deep learning"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Direct core query, now without year suffix to capture all relevant papers in the range."
    },
    {
      "query": "reverse engineering CAD from point cloud deep learning",
      "reason": "Targets the reverse engineering aspect with a learning focus, likely to yield core methods."
    },
    {
      "query": "parametric CAD model reconstruction from 3D scan",
      "reason": "Broader phrasing to capture papers that might use 'parametric CAD' or '3D scan' synonymously."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.", "Papers on 'CAD reconstruction from point clouds' inherently target B-rep outputs.", "Multi-stage pipelines (e.g., point cloud -> primitive fitting -> B-rep) are relevant.", "The user wants a mix of direct matches and substantial contributions to sub-problems like primitive detection or segmentation that feed into B-rep creation.", "Based on the Reviewer's feedback, we need to verify core method fit by ensuring abstracts explicitly mention point cloud input and B-rep/CAD model output."],
  "success_criteria": ["Retrieve at least 5-10 papers from 2022-2026 that are directly about or substantially contribute to B-rep reconstruction from point clouds, with clear evidence from abstracts.", "Identify clear method categories (e.g., learning-based primitive fitting, optimization-based, hybrid).", "Capture recent trends such as the use of transformers or diffusion models.", "Highlight open challenges like handling complex topology or noisy data.", "Ensure relevance notes are specific and based on concrete evidence, not generic matches."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the revised search plan with a focus on verifying core method fit through more detailed evidence examination.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_s1S4GXRnU7kynMsDs6fOecie', arguments='{"top_k": 12, "max_results_per_source": 25, "query": "reverse engineering CAD from point cloud deep learning"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "reverse engineering CAD from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "parametric CAD model reconstruction from 3D scan",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-10-27T15:33:51Z",\n      "url": "http://arxiv.org/abs/2510.23429v1",\n      "doi": "",\n      "authors": [\n        "Ahmet Serdar Karadeniz",\n        "Dimitrios Mallis",\n        "Danila Rukhovich",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'parametric cad model reconstruction from 3d scan\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ]\n    },\n    {\n      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-24",\n      "url": "https://doi.org/10.1016/j.autcon.2022.104440",\n      "doi": "10.1016/j.autcon.2022.104440",\n      "authors": [\n        "Shanaka Kristombu Baduge",\n        "Sadeep Thilakarathna",\n        "Jude Shalitha Perera",\n        "Mehrdad Arashpour",\n        "P. Sharafi",\n        "Bertrand Teodosio",\n        "Ankit Shringi",\n        "Priyan Mendis"\n      ],\n      "relevance_note": "Abstract or excerpt matched retrieval query terms around \'reverse engineering cad from pointcloud deep learning\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 14 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "reverse engineering point cloud CAD",\n      "point cloud to parametric CAD",\n      "B-rep from scan deep learning"\n    ],\n    "effective_query": "reverse engineering CAD from point cloud deep learning",\n    "used_override_query": true,\n    "executed_queries": [\n      "reverse engineering CAD from point cloud deep learning",\n      "point cloud to B-rep reconstruction",\n      "parametric CAD model reconstruction from 3D scan"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_s1S4GXRnU7kynMsDs6fOecie' is_error=False
```

### Message 12

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Structured retrieval output: papers=12, sources=3, supported_evidence=12, in_range=12

```text
{
  "sources_used": [
    "Crossref",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "reverse engineering CAD from point cloud deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "parametric CAD model reconstruction from 3D scan",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-12-18T16:55:42Z",
      "url": "http://arxiv.org/abs/2412.14042v2",
      "doi": "",
      "authors": [
        "Danila Rukhovich",
        "Elona Dupont",
        "Dimitrios Mallis",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-05-29",
      "url": "http://arxiv.org/abs/2205.14573",
      "doi": "10.48550/arxiv.2205.14573",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-05-29T05:30:33Z",
      "url": "http://arxiv.org/abs/2205.14573v1",
      "doi": "",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    },
    {
      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-12-28",
      "url": "https://doi.org/10.1093/jcde/qwae005",
      "doi": "10.1093/jcde/qwae005",
      "authors": [
        "Shuming Zhang",
        "Zhidong Guan",
        "Hao Jiang",
        "Ning Tao",
        "Xiaodong Wang",
        "Pingan Tan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-07-26",
      "url": "https://doi.org/10.1145/3730842",
      "doi": "10.1145/3730842",
      "authors": [
        "Yilin Liu",
        "Duoteng Xu",
        "Xingyao Yu",
        "Xiang Xu",
        "Daniel Cohen‐Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ]
    },
    {
      "title": "ComplexGen",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-07-01",
      "url": "https://doi.org/10.1145/3528223.3530078",
      "doi": "10.1145/3528223.3530078",
      "authors": [
        "Haoxiang Guo",
        "Shilin Liu",
        "Hao Pan",
        "Yang Liu",
        "Xin Tong",
        "Baining Guo"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ]
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref | OpenAlex",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "yihang fu",
        "jing li",
        "Falai Chen",
        "Yihang Fu",
        "Jing Li",
        "FaLai Chen"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
    {
      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-10-27T15:33:51Z",
      "url": "http://arxiv.org/abs/2510.23429v1",
      "doi": "",
      "authors": [
        "Ahmet Serdar Karadeniz",
        "Dimitrios Mallis",
        "Danila Rukhovich",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'parametric cad model reconstruction from 3d scan'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"
      ]
    },
    {
      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-07-19",
      "url": "https://doi.org/10.1145/3658155",
      "doi": "10.1145/3658155",
      "authors": [
        "Yilin Liu",
        "Jiale Chen",
        "Shanshan Pan",
        "Daniel Cohen‐Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-11-07T18:31:08Z",
      "url": "http://arxiv.org/abs/2411.04954v3",
      "doi": "",
      "authors": [
        "Jingwei Xu",
        "Chenyu Wang",
        "Zibo Zhao",
        "Wen Liu",
        "Yi Ma",
        "Shenghua Gao"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    },
    {
      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-09-03",
      "url": "https://doi.org/10.3233/ica-240744",
      "doi": "10.3233/ica-240744",
      "authors": [
        "Rubin Fan",
        "Fazhi He",
        "Yuxin Liu",
        "Yupeng Song",
        "Linkun Fan",
        "Xiaohu Yan"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ]
    },
    {
      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-24",
      "url": "https://doi.org/10.1016/j.autcon.2022.104440",
      "doi": "10.1016/j.autcon.2022.104440",
      "authors": [
        "Shanaka Kristombu Baduge",
        "Sadeep Thilakarathna",
        "Jude Shalitha Perera",
        "Mehrdad Arashpour",
        "P. Sharafi",
        "Bertrand Teodosio",
        "Ankit Shringi",
        "Priyan Mendis"
      ],
      "relevance_note": "Abstract or excerpt matched retrieval query terms around 'reverse engineering cad from pointcloud deep learning'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 14 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "reverse engineering point cloud CAD",
      "point cloud to parametric CAD",
      "B-rep from scan deep learning"
    ],
    "effective_query": "reverse engineering CAD from point cloud deep learning",
    "used_override_query": true,
    "executed_queries": [
      "reverse engineering CAD from point cloud deep learning",
      "point cloud to B-rep reconstruction",
      "parametric CAD model reconstruction from 3D scan"
    ],
    "fallback_used": false
  }
}
```

### Message 13

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=7

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has improved, with several papers appearing highly relevant (e.g., CAD-Recode, ComplexGen, Point2Brep, MiCADangelo). However, the evidence snippets remain truncated and the relevance notes are still generic, making it difficult to confidently verify core-method fit. Furthermore, the set contains duplicates (ComplexGen appears three times) and includes papers that are clearly off-topic (e.g., a review on AI in construction, a dataset paper). The hard requirements for candidate depth (non-duplicate count) and core-method fit are not met due to insufficient evidence and contamination by irrelevant entries.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "At least 3 distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After accounting for duplicates (ComplexGen appears 3 times), the number of unique candidate papers is less than 5. The list also includes clearly irrelevant papers (e.g., the construction review), further reducing the count of valid candidates."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be confidently assessed. While some titles look promising, the evidence snippets are too brief and the relevance notes are generic. Papers like 'Artificial intelligence and smart vision for building and construction 4.0' are clearly not about B-rep reconstruction from point clouds. 'A parametric and feature-based CAD dataset' is about a dataset, not reconstruction. Without clearer evidence, we cannot confirm at least 2-3 are clearly aligned."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the time constraint. The queries executed are aligned with the topic."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be verified. The evidence snippets are truncated and do not explicitly confirm point cloud input and B-rep output for most papers. The presence of duplicates and off-topic papers further obscures the count of core candidates. We need clear abstracts to confirm papers like 'Point2Brep', 'MiCADangelo', 'Split-and-Fit', and 'HoLa' are indeed about reconstruction from point clouds."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major evidence hole, but the set is cluttered with duplicates and irrelevant papers."
    }
  },
  "key_risks": [
    "High duplication rate (ComplexGen appears 3 times) inflates the candidate count.",
    "Inclusion of clearly irrelevant papers (construction review, dataset paper) reduces signal-to-noise.",
    "Evidence snippets are still truncated, preventing verification of core method fit.",
    "Relevance notes remain generic and unhelpful."
  ],
  "next_actions": [
    "Deduplicate the list rigorously by DOI, URL, and normalized title. Remove all duplicate entries of 'ComplexGen' and any other duplicates.",
    "Filter out clearly irrelevant papers based on title and snippet inspection (e.g., 'Artificial intelligence and smart vision for building and construction 4.0', 'A parametric and feature-based CAD dataset').",
    "For the remaining unique and potentially relevant papers (e.g., CAD-Recode, ComplexGen, Point2Brep, MiCADangelo, Split-and-Fit, HoLa, Brep2Seq), retrieve and present the full abstract or a substantial paragraph that explicitly states the input (point cloud/3D scan) and output (B-rep/CAD model).",
    "If after deduplication and filtering the number of unique, relevant candidates falls below 5, execute a targeted fallback query (e.g., 'point cloud to parametric CAD reconstruction 2024') to find additional core papers."
  ]
}
```

### Message 14

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal is to identify recent research (2022–2026) on methods that reconstruct or generate Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on the core task of point-cloud-to-B-rep reconstruction, including closely related works that make substantial contributions to this problem (e.g., primitive detection, parametric CAD sequence recovery). Papers that only address mesh reconstruction, pure segmentation, or use other primary inputs (e.g., images) are excluded.

## Search Strategy
The search was conducted in two phases using sources including arXiv, Crossref, and OpenAlex.
1.  **Initial Queries:** Targeted direct phrases like "point cloud to B-rep reconstruction" and "deep learning B-rep generation from point clouds."
2.  **Refined Queries:** Based on reviewer feedback, queries were adjusted to emphasize "reverse engineering CAD from point cloud" and "parametric CAD model reconstruction from 3D scan" to better capture core methods.
The process aimed to verify that each paper's abstract explicitly mentions point cloud input and B-rep/CAD model output.

## Candidate Papers
*The search did not clear the quality bar.* The review process identified unresolved issues: evidence snippets remained too brief to confirm core method fit for several papers, and the final list contained duplicates and entries that were not directly relevant to the specified task. Therefore, a definitive set of recommended papers cannot be provided.

### Verified Candidates
No papers reached a `verified` status. The following papers had `partial` verification, meaning their abstracts suggest relevance but full confirmation is lacking:
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds (2024)** – Abstract indicates reconstruction of CAD operation sequences from point clouds.
*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)** – Abstract frames CAD model reconstruction in B-Rep as detection of geometric primitives.
*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title and snippet directly describe B-rep reconstruction from point clouds.

### Unverified Leads
The following papers have titles that appear strong for the topic but lack sufficient evidence in the retrieved snippets to confirm they are core methods for point-cloud-to-B-rep reconstruction. They are suggested as leads for follow-up investigation, not as recommendations.
1.  **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans (2025)** – Title mentions reconstruction from 3D scans.
2.  **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning (2024)** – Title suggests a method for acquiring B-Reps.
3.  **HoLa: B-Rep Generation using a Holistic Latent Representation (2025)** – Title focuses on B-Rep generation.

## Notes and Gaps
*   **Evidence Insufficiency:** The primary gap was the inability to retrieve and present complete abstracts or introductory paragraphs for candidate papers, which is necessary to confirm the core task alignment (point cloud input, B-rep output).
*   **Result Contamination:** The final retrieval set contained duplicate entries (e.g., multiple instances of "ComplexGen") and papers clearly outside the scope (e.g., a broad review on AI in construction, a dataset paper).
*   **Methodological Clarity:** Without full paper details, it is impossible to reliably categorize major methods, identify recent trends, or list open challenges.

## Recommended Next Steps
1.  **Manual Abstract Retrieval:** For the leads listed above, directly access the provided URLs (e.g., arXiv links) to read the abstracts and confirm relevance.
2.  **Targeted Database Search:** Use academic databases (e.g., ACM Digital Library, IEEE Xplore) with precise queries like `"B-rep" AND "point cloud" AND reconstruction` and filter by publication date (2022-2026).
3.  **Citation Tracking:** Identify seminal papers in the area (e.g., "ComplexGen") and use citation tracking tools to find more recent works that build upon them.
4.  **Venue Focus:** Prioritize searching in relevant conference proceedings (e.g., SIGGRAPH, CVPR, CAD) and journals (e.g., Computer-Aided Design, IEEE Transactions on Visualization and Computer Graphics).

TERMINATE
```
