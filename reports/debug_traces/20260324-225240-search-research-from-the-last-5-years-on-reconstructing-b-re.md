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
**Generated At:** 2026-03-24T22:52:40
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
  "user_intent": "Find recent research (2022-2026) on methods for generating, reconstructing, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data, with a focus on core contributions and trends.",
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
    "CAD model generation from point clouds",
    "boundary representation recovery",
    "point cloud to CAD",
    "geometric deep learning for B-rep"
  ],
  "exclude_areas": [
    "point cloud to mesh only",
    "point cloud registration without reconstruction",
    "pure mesh-to-B-rep conversion",
    "unrelated CAD applications"
  ],
  "fallback_queries": [
    "point cloud to CAD reconstruction",
    "B-rep reconstruction deep learning",
    "CAD from scan data"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Directly targets the core task of converting point clouds to boundary representations."
    },
    {
      "query": "CAD model generation from point clouds",
      "reason": "Captures papers that may use 'CAD model' or 'CAD generation' terminology for B-rep output."
    },
    {
      "query": "deep learning B-rep reconstruction point cloud",
      "reason": "Focuses on recent learning-based methods, which are likely dominant in the specified time range."
    }
  ],
  "assumptions": [
    "The term 'B-rep' is used interchangeably with 'CAD boundary representation' in relevant literature.",
    "Papers may present multi-stage pipelines (e.g., point cloud → primitive fitting → B-rep) which are still relevant.",
    "The field may include both traditional geometric and data-driven approaches."
  ],
  "success_criteria": [
    "Retrieve papers where point cloud is a primary input and B-rep/CAD model is a target output.",
    "Identify major methodological categories (e.g., primitive fitting, neural synthesis, hybrid).",
    "Capture recent trends and open challenges as requested for the summary."
  ]
}
```

### Planner Output 8

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research (2022-2026) on methods for generating, reconstructing, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data, with a focus on core contributions and trends.",
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
    "CAD model generation from point clouds",
    "boundary representation recovery",
    "point cloud to CAD",
    "geometric deep learning for B-rep",
    "parametric CAD reverse engineering from scans"
  ],
  "exclude_areas": [
    "point cloud to mesh only",
    "point cloud registration without reconstruction",
    "pure mesh-to-B-rep conversion",
    "unrelated CAD applications",
    "multimodal generation not focused on point clouds"
  ],
  "fallback_queries": [
    "point cloud to CAD reconstruction",
    "B-rep reconstruction deep learning",
    "CAD from scan data"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "reason": "Direct query with explicit years to prioritize recent core papers and retrieve full abstracts for verification."
    },
    {
      "query": "parametric CAD reconstruction from point cloud",
      "reason": "Captures papers focusing on editable, feature-based CAD models, a key aspect of B-rep output."
    },
    {
      "query": "reverse engineering CAD from point cloud scan",
      "reason": "Targets the applied reverse-engineering literature, which often deals with B-rep reconstruction from scanned data."
    }
  ],
  "assumptions": [
    "The term 'B-rep' is used interchangeably with 'CAD boundary representation' in relevant literature.",
    "Papers may present multi-stage pipelines (e.g., point cloud → primitive fitting → B-rep) which are still relevant.",
    "The field may include both traditional geometric and data-driven approaches.",
    "We will prioritize retrieving full abstracts to confirm relevance and core contribution."
  ],
  "success_criteria": [
    "Retrieve papers where point cloud is a primary input and B-rep/CAD model is a target output, confirmed by abstract.",
    "Identify major methodological categories (e.g., primitive fitting, neural synthesis, hybrid).",
    "Capture recent trends and open challenges as requested for the summary.",
    "Ensure a final list of 5-10 unique, relevant papers with complete metadata."
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
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "deep learning B-rep reconstruction point cloud",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",
      "source": "Crossref / Journal of Electronic Research and Application",
      "year": 2025,
      "date": "2025-12-16",
      "url": "https://doi.org/10.26689/jera.v9i6.13185",
      "doi": "10.26689/jera.v9i6.13185",
      "authors": [
        "Yangzhi Zhang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "CAD from scan data"
    ],
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-rep reconstruction",
      "CAD model generation from point clouds",
      "deep learning B-rep reconstruction point cloud"
    ],
    "fallback_used": false
  }
}
```

### Retrieval Output 12

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
      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "parametric CAD reconstruction from point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "reverse engineering CAD from point cloud scan",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "yihang fu",
        "jing li",
        "Falai Chen"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction 2022 2023 2024 2025 2026'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
    {
      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",
      "source": "Crossref / Journal of Electronic Research and Application",
      "year": 2025,
      "date": "2025-12-16",
      "url": "https://doi.org/10.26689/jera.v9i6.13185",
      "doi": "10.26689/jera.v9i6.13185",
      "authors": [
        "Yangzhi Zhang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
      ]
    },
    {
      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-07-17T16:24:36Z",
      "url": "http://arxiv.org/abs/2407.12702v2",
      "doi": "",
      "authors": [
        "Elona Dupont",
        "Kseniya Cherenkova",
        "Dimitrios Mallis",
        "Gleb Gusev",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'reverse engineering cad from pointcloud scan'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    },
    {
      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-10-04",
      "url": "http://arxiv.org/abs/2310.02638",
      "doi": "10.48550/arxiv.2310.02638",
      "authors": [
        "Zhihao Zong",
        "Fazhi He",
        "Rubin Fan",
        "Yuxin Liu"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-11-17",
      "url": "https://doi.org/10.1016/j.engappai.2025.113107",
      "doi": "10.1016/j.engappai.2025.113107",
      "authors": [
        "Jiaxing Lu",
        "Yixuan Wang",
        "Yangyong Wu",
        "Heran Li",
        "Yan Shi",
        "Fangwei Ning"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering of industrial parts from three-dimensional (3D) point clouds is vital for modern computer-aided design (CAD) workflows in manufacturing and design. However, the unordered nature of point clouds and its substantial modality gap from sequential, parameterized CAD modeling make accurate and editable reconstruction particularly challenging. Existing methods often struggle to addres"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-07-19",
      "url": "https://doi.org/10.1145/3588432.3591522",
      "doi": "10.1145/3588432.3591522",
      "authors": [
        "Yuanqi Li",
        "Shun Liu",
        "Xinran Yang",
        "Jianwei Guo",
        "Jie Guo",
        "Yanwen Guo"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction 2022 2023 2024 2025 2026'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 34 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "CAD from scan data"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "parametric CAD reconstruction from point cloud",
      "reverse engineering CAD from point cloud scan"
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
  "review_summary": "The retrieval captured several promising papers within the 2022-2026 range, but the evidence is insufficient to confidently satisfy the hard requirements. The relevance of many papers is unclear from the provided snippets, and the core-method fit cannot be verified. The set includes duplicates (e.g., ComplexGen appears multiple times) and lacks clear evidence that at least 3 papers are direct matches for point-cloud-to-B-rep reconstruction. The metadata is incomplete for some entries, and the relevance notes are generic, failing to explain the specific contribution to the user's topic.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, at least 5 distinct candidate papers remain (e.g., Point2Brep, Point2Primitive, Brep2Seq, ComplexGen, P2CADNet, CAD-Recode, CAD-MLLM, Research on Reverse Modeling)."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, it is unclear if 2-3 are clearly aligned with the user's topic. The evidence snippets are vague and the relevance notes are generic ('matched retrieval query terms'). For example, 'CAD-MLLM' appears to be a multimodal generation system, not specifically focused on point clouds as the primary input for B-rep reconstruction. The direct match status cannot be determined from the provided evidence."
    },
    "metadata": {
      "passed": false,
      "reason": "Not all retained candidates have complete metadata. For instance, several arXiv entries lack DOIs, and the 'Research on Reverse Modeling' paper has a single author list which may be incomplete. More critically, the evidence snippets are truncated and do not provide full abstracts or clear confirmation of the paper's focus."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set respects the 2022-2026 time range and appears to focus on CAD/B-rep reconstruction from point clouds, based on the titles and partial snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot verify that at least 3 papers are core candidates for point-cloud-to-B-rep reconstruction. The evidence snippets are insufficient to judge the core contribution and methodology. Papers like 'CAD-MLLM' and 'Brep2Seq' may be related but not directly focused on point cloud as the primary input. The verification_status is 'partial' for all, but the evidence_level 'abstract' snippets are too brief."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are within the 2022-2026 range, and no out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious evidence hole: the retrieved abstracts/snippets are truncated and do not clearly confirm the papers' relevance to the specific task. Additionally, there is potential over-reliance on arXiv as a source for several entries, and the set includes duplicates (ComplexGen appears multiple times from different sources)."
    }
  },
  "key_risks": [
    "Relevance is uncertain; several papers may be about CAD generation from other inputs (e.g., text, images) rather than primarily from point clouds.",
    "Evidence snippets are incomplete, making it impossible to verify the core contribution and methodology alignment.",
    "Duplicate entries (ComplexGen) suggest the deduplication was not fully effective in the presented list."
  ],
  "next_actions": [
    "Retrieve full abstracts or more complete evidence snippets for the top candidate papers (e.g., Point2Brep, Point2Primitive, ComplexGen, P2CADNet, CAD-Recode) to confirm their focus on point-cloud-to-B-rep reconstruction.",
    "Explicitly filter out papers that are not primarily focused on point cloud as input (e.g., CAD-MLLM which conditions on multiple modalities) unless they have a substantial contribution to the point-cloud-specific problem.",
    "Perform a final deduplication pass to ensure the list contains unique papers, merging entries for the same work from different sources."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has improved focus on parametric CAD reconstruction from point clouds, but critical hard requirements remain unmet. The evidence snippets are still truncated and do not provide full abstracts, making it impossible to verify core-method fit and relevance. Several papers appear highly relevant (e.g., Point2Brep, CAD-Recode, TransCAD), but the evidence is insufficient to confirm they are direct matches for B-rep reconstruction from point clouds. The set includes duplicates (P2CADNet appears twice) and papers that may be about primitive fitting benchmarks (SHREC 2022) rather than B-rep reconstruction. Metadata completeness is still an issue for arXiv entries lacking DOIs.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, at least 5 distinct candidate papers remain (e.g., CAD-Recode, Point2Brep, TransCAD, CAD-SIGNet, P2CADNet, autoregressive framework, Surface and Edge Detection, SHREC 2022)."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot confirm that at least 2-3 top candidates are clearly aligned with the user's topic. The evidence snippets are truncated and the relevance notes are generic. For example, 'Surface and Edge Detection for Primitive Fitting of Point Clouds' may be a segmentation method, not necessarily producing a B-rep. 'SHREC 2022' is a benchmark track, not a reconstruction method. The direct match status is unclear."
    },
    "metadata": {
      "passed": false,
      "reason": "Metadata is incomplete for several entries. Multiple arXiv papers lack DOIs (e.g., CAD-Recode, TransCAD, CAD-SIGNet). The evidence snippets are still partial abstracts, not full abstracts, which limits verification."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set respects the 2022-2026 time range and the queries are aligned with the user's focus on parametric CAD and reverse engineering from point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot verify that at least 3 papers are core candidates for point-cloud-to-B-rep reconstruction. The evidence snippets are too brief to assess the core contribution and methodology. Papers like 'Surface and Edge Detection' and 'SHREC 2022' are likely about primitive fitting evaluation, not B-rep reconstruction. The verification_status is 'partial' but evidence_level 'abstract' snippets are incomplete."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence gap: the abstracts are truncated, preventing confirmation of relevance and core contribution. The set includes potential false positives (benchmark, primitive fitting) and duplicates (P2CADNet). The diversity of methods is unclear."
    }
  },
  "key_risks": [
    "Truncated evidence snippets make it impossible to judge the relevance and core contribution of papers, leading to potential inclusion of off-topic works.",
    "Duplicates (P2CADNet) and potential false positives (SHREC 2022 benchmark) could mislead the final report.",
    "Lack of full abstracts may hide that some papers are not primarily about B-rep reconstruction from point clouds."
  ],
  "next_actions": [
    "Retrieve FULL abstracts (not truncated snippets) for the top 8 candidate papers to confirm their focus on point-cloud-to-B-rep/parametric CAD reconstruction. Use direct API calls or source links to obtain complete text.",
    "Explicitly filter out papers that are benchmarks (e.g., SHREC 2022) or focus solely on primitive fitting without B-rep output, unless they are directly relevant to the reconstruction pipeline.",
    "Perform a final deduplication pass to ensure each paper appears only once in the final list, merging entries from different sources."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_TK99kgTxWN5IvByUIjl8q03M', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "deep learning B-rep reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "CAD from scan data"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction",\n      "CAD model generation from point clouds",\n      "deep learning B-rep reconstruction point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_TK99kgTxWN5IvByUIjl8q03M' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_zIYgyvYuG0EVKAxtCP9URWBy', arguments='{"top_k": 10, "max_results_per_source": 25, "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "parametric CAD reconstruction from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "reverse engineering CAD from point cloud scan",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction 2022 2023 2024 2025 2026\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ]\n    },\n    {\n      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-17T16:24:36Z",\n      "url": "http://arxiv.org/abs/2407.12702v2",\n      "doi": "",\n      "authors": [\n        "Elona Dupont",\n        "Kseniya Cherenkova",\n        "Dimitrios Mallis",\n        "Gleb Gusev",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'reverse engineering cad from pointcloud scan\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-10-04",\n      "url": "http://arxiv.org/abs/2310.02638",\n      "doi": "10.48550/arxiv.2310.02638",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-11-17",\n      "url": "https://doi.org/10.1016/j.engappai.2025.113107",\n      "doi": "10.1016/j.engappai.2025.113107",\n      "authors": [\n        "Jiaxing Lu",\n        "Yixuan Wang",\n        "Yangyong Wu",\n        "Heran Li",\n        "Yan Shi",\n        "Fangwei Ning"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering of industrial parts from three-dimensional (3D) point clouds is vital for modern computer-aided design (CAD) workflows in manufacturing and design. However, the unordered nature of point clouds and its substantial modality gap from sequential, parameterized CAD modeling make accurate and editable reconstruction particularly challenging. Existing methods often struggle to addres"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ]\n    },\n    {\n      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-06-15T16:27:01Z",\n      "url": "http://arxiv.org/abs/2206.07636v2",\n      "doi": "",\n      "authors": [\n        "Chiara Romanengo",\n        "Andrea Raffo",\n        "Silvia Biasotti",\n        "Bianca Falcidieno",\n        "Vlassis Fotis",\n        "Ioannis Romanelis",\n        "Eleftheria Psatha",\n        "Konstantinos Moustakas"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction 2022 2023 2024 2025 2026\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 34 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "CAD from scan data"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n      "parametric CAD reconstruction from point cloud",\n      "reverse engineering CAD from point cloud scan"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_zIYgyvYuG0EVKAxtCP9URWBy' is_error=False
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
  "user_intent": "Find recent research (2022-2026) on methods for generating, reconstructing, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data, with a focus on core contributions and trends.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep reconstruction from point clouds", "CAD model generation from point clouds", "boundary representation recovery", "point cloud to CAD", "geometric deep learning for B-rep"],
  "exclude_areas": ["point cloud to mesh only", "point cloud registration without reconstruction", "pure mesh-to-B-rep conversion", "unrelated CAD applications"],
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep reconstruction deep learning", "CAD from scan data"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Directly targets the core task of converting point clouds to boundary representations."
    },
    {
      "query": "CAD model generation from point clouds",
      "reason": "Captures papers that may use 'CAD model' or 'CAD generation' terminology for B-rep output."
    },
    {
      "query": "deep learning B-rep reconstruction point cloud",
      "reason": "Focuses on recent learning-based methods, which are likely dominant in the specified time range."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'CAD boundary representation' in relevant literature.", "Papers may present multi-stage pipelines (e.g., point cloud → primitive fitting → B-rep) which are still relevant.", "The field may include both traditional geometric and data-driven approaches."],
  "success_criteria": ["Retrieve papers where point cloud is a primary input and B-rep/CAD model is a target output.", "Identify major methodological categories (e.g., primitive fitting, neural synthesis, hybrid).", "Capture recent trends and open challenges as requested for the summary."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan using the provided queries and parameters.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_TK99kgTxWN5IvByUIjl8q03M', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "deep learning B-rep reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad model generation from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "CAD from scan data"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction",\n      "CAD model generation from point clouds",\n      "deep learning B-rep reconstruction point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_TK99kgTxWN5IvByUIjl8q03M' is_error=False
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
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "deep learning B-rep reconstruction point cloud",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",
      "source": "Crossref / Journal of Electronic Research and Application",
      "year": 2025,
      "date": "2025-12-16",
      "url": "https://doi.org/10.26689/jera.v9i6.13185",
      "doi": "10.26689/jera.v9i6.13185",
      "authors": [
        "Yangzhi Zhang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad model generation from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "CAD from scan data"
    ],
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-rep reconstruction",
      "CAD model generation from point clouds",
      "deep learning B-rep reconstruction point cloud"
    ],
    "fallback_used": false
  }
}
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=6

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval captured several promising papers within the 2022-2026 range, but the evidence is insufficient to confidently satisfy the hard requirements. The relevance of many papers is unclear from the provided snippets, and the core-method fit cannot be verified. The set includes duplicates (e.g., ComplexGen appears multiple times) and lacks clear evidence that at least 3 papers are direct matches for point-cloud-to-B-rep reconstruction. The metadata is incomplete for some entries, and the relevance notes are generic, failing to explain the specific contribution to the user's topic.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, at least 5 distinct candidate papers remain (e.g., Point2Brep, Point2Primitive, Brep2Seq, ComplexGen, P2CADNet, CAD-Recode, CAD-MLLM, Research on Reverse Modeling)."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, it is unclear if 2-3 are clearly aligned with the user's topic. The evidence snippets are vague and the relevance notes are generic ('matched retrieval query terms'). For example, 'CAD-MLLM' appears to be a multimodal generation system, not specifically focused on point clouds as the primary input for B-rep reconstruction. The direct match status cannot be determined from the provided evidence."
    },
    "metadata": {
      "passed": false,
      "reason": "Not all retained candidates have complete metadata. For instance, several arXiv entries lack DOIs, and the 'Research on Reverse Modeling' paper has a single author list which may be incomplete. More critically, the evidence snippets are truncated and do not provide full abstracts or clear confirmation of the paper's focus."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set respects the 2022-2026 time range and appears to focus on CAD/B-rep reconstruction from point clouds, based on the titles and partial snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot verify that at least 3 papers are core candidates for point-cloud-to-B-rep reconstruction. The evidence snippets are insufficient to judge the core contribution and methodology. Papers like 'CAD-MLLM' and 'Brep2Seq' may be related but not directly focused on point cloud as the primary input. The verification_status is 'partial' for all, but the evidence_level 'abstract' snippets are too brief."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are within the 2022-2026 range, and no out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious evidence hole: the retrieved abstracts/snippets are truncated and do not clearly confirm the papers' relevance to the specific task. Additionally, there is potential over-reliance on arXiv as a source for several entries, and the set includes duplicates (ComplexGen appears multiple times from different sources)."
    }
  },
  "key_risks": [
    "Relevance is uncertain; several papers may be about CAD generation from other inputs (e.g., text, images) rather than primarily from point clouds.",
    "Evidence snippets are incomplete, making it impossible to verify the core contribution and methodology alignment.",
    "Duplicate entries (ComplexGen) suggest the deduplication was not fully effective in the presented list."
  ],
  "next_actions": [
    "Retrieve full abstracts or more complete evidence snippets for the top candidate papers (e.g., Point2Brep, Point2Primitive, ComplexGen, P2CADNet, CAD-Recode) to confirm their focus on point-cloud-to-B-rep reconstruction.",
    "Explicitly filter out papers that are not primarily focused on point cloud as input (e.g., CAD-MLLM which conditions on multiple modalities) unless they have a substantial contribution to the point-cloud-specific problem.",
    "Perform a final deduplication pass to ensure the list contains unique papers, merging entries for the same work from different sources."
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
  "user_intent": "Find recent research (2022-2026) on methods for generating, reconstructing, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data, with a focus on core contributions and trends.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep reconstruction from point clouds", "CAD model generation from point clouds", "boundary representation recovery", "point cloud to CAD", "geometric deep learning for B-rep", "parametric CAD reverse engineering from scans"],
  "exclude_areas": ["point cloud to mesh only", "point cloud registration without reconstruction", "pure mesh-to-B-rep conversion", "unrelated CAD applications", "multimodal generation not focused on point clouds"],
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep reconstruction deep learning", "CAD from scan data"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "reason": "Direct query with explicit years to prioritize recent core papers and retrieve full abstracts for verification."
    },
    {
      "query": "parametric CAD reconstruction from point cloud",
      "reason": "Captures papers focusing on editable, feature-based CAD models, a key aspect of B-rep output."
    },
    {
      "query": "reverse engineering CAD from point cloud scan",
      "reason": "Targets the applied reverse-engineering literature, which often deals with B-rep reconstruction from scanned data."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'CAD boundary representation' in relevant literature.", "Papers may present multi-stage pipelines (e.g., point cloud → primitive fitting → B-rep) which are still relevant.", "The field may include both traditional geometric and data-driven approaches.", "We will prioritize retrieving full abstracts to confirm relevance and core contribution."],
  "success_criteria": ["Retrieve papers where point cloud is a primary input and B-rep/CAD model is a target output, confirmed by abstract.", "Identify major methodological categories (e.g., primitive fitting, neural synthesis, hybrid).", "Capture recent trends and open challenges as requested for the summary.", "Ensure a final list of 5-10 unique, relevant papers with complete metadata."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the revised search plan with more specific queries to get better evidence for verification.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_zIYgyvYuG0EVKAxtCP9URWBy', arguments='{"top_k": 10, "max_results_per_source": 25, "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "parametric CAD reconstruction from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "reverse engineering CAD from point cloud scan",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction 2022 2023 2024 2025 2026\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ]\n    },\n    {\n      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-17T16:24:36Z",\n      "url": "http://arxiv.org/abs/2407.12702v2",\n      "doi": "",\n      "authors": [\n        "Elona Dupont",\n        "Kseniya Cherenkova",\n        "Dimitrios Mallis",\n        "Gleb Gusev",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'reverse engineering cad from pointcloud scan\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-10-04",\n      "url": "http://arxiv.org/abs/2310.02638",\n      "doi": "10.48550/arxiv.2310.02638",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-11-17",\n      "url": "https://doi.org/10.1016/j.engappai.2025.113107",\n      "doi": "10.1016/j.engappai.2025.113107",\n      "authors": [\n        "Jiaxing Lu",\n        "Yixuan Wang",\n        "Yangyong Wu",\n        "Heran Li",\n        "Yan Shi",\n        "Fangwei Ning"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering of industrial parts from three-dimensional (3D) point clouds is vital for modern computer-aided design (CAD) workflows in manufacturing and design. However, the unordered nature of point clouds and its substantial modality gap from sequential, parameterized CAD modeling make accurate and editable reconstruction particularly challenging. Existing methods often struggle to addres"\n      ]\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ]\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'parametric cad reconstruction from pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ]\n    },\n    {\n      "title": "SHREC 2022: Fitting and recognition of simple geometric primitives on point clouds",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-06-15T16:27:01Z",\n      "url": "http://arxiv.org/abs/2206.07636v2",\n      "doi": "",\n      "authors": [\n        "Chiara Romanengo",\n        "Andrea Raffo",\n        "Silvia Biasotti",\n        "Bianca Falcidieno",\n        "Vlassis Fotis",\n        "Ioannis Romanelis",\n        "Eleftheria Psatha",\n        "Konstantinos Moustakas"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud to brep reconstruction 2022 2023 2024 2025 2026\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 34 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep reconstruction deep learning",\n      "CAD from scan data"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",\n      "parametric CAD reconstruction from point cloud",\n      "reverse engineering CAD from point cloud scan"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_zIYgyvYuG0EVKAxtCP9URWBy' is_error=False
```

### Message 12

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
      "query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "parametric CAD reconstruction from point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "reverse engineering CAD from point cloud scan",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ]
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "yihang fu",
        "jing li",
        "Falai Chen"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction 2022 2023 2024 2025 2026'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ]
    },
    {
      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",
      "source": "Crossref / Journal of Electronic Research and Application",
      "year": 2025,
      "date": "2025-12-16",
      "url": "https://doi.org/10.26689/jera.v9i6.13185",
      "doi": "10.26689/jera.v9i6.13185",
      "authors": [
        "Yangzhi Zhang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
      ]
    },
    {
      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-07-17T16:24:36Z",
      "url": "http://arxiv.org/abs/2407.12702v2",
      "doi": "",
      "authors": [
        "Elona Dupont",
        "Kseniya Cherenkova",
        "Dimitrios Mallis",
        "Gleb Gusev",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'reverse engineering cad from pointcloud scan'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    },
    {
      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-10-04",
      "url": "http://arxiv.org/abs/2310.02638",
      "doi": "10.48550/arxiv.2310.02638",
      "authors": [
        "Zhihao Zong",
        "Fazhi He",
        "Rubin Fan",
        "Yuxin Liu"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-11-17",
      "url": "https://doi.org/10.1016/j.engappai.2025.113107",
      "doi": "10.1016/j.engappai.2025.113107",
      "authors": [
        "Jiaxing Lu",
        "Yixuan Wang",
        "Yangyong Wu",
        "Heran Li",
        "Yan Shi",
        "Fangwei Ning"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering of industrial parts from three-dimensional (3D) point clouds is vital for modern computer-aided design (CAD) workflows in manufacturing and design. However, the unordered nature of point clouds and its substantial modality gap from sequential, parameterized CAD modeling make accurate and editable reconstruction particularly challenging. Existing methods often struggle to addres"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ]
    },
    {
      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-07-19",
      "url": "https://doi.org/10.1145/3588432.3591522",
      "doi": "10.1145/3588432.3591522",
      "authors": [
        "Yuanqi Li",
        "Shun Liu",
        "Xinran Yang",
        "Jianwei Guo",
        "Jie Guo",
        "Yanwen Guo"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'parametric cad reconstruction from pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud to brep reconstruction 2022 2023 2024 2025 2026'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents the methods that have participated in the SHREC 2022 track on the fitting and recognition of simple geometric primitives on point clouds. As simple primitives we mean the classical surface primitives derived from constructive solid geometry, i.e., planes, spheres, cylinders, cones and tori. The aim of the track is to evaluate the quality of automatic algorithms for fitting and "
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 34 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep reconstruction deep learning",
      "CAD from scan data"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2022 2023 2024 2025 2026",
      "parametric CAD reconstruction from point cloud",
      "reverse engineering CAD from point cloud scan"
    ],
    "fallback_used": false
  }
}
```

### Message 13

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=6

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has improved focus on parametric CAD reconstruction from point clouds, but critical hard requirements remain unmet. The evidence snippets are still truncated and do not provide full abstracts, making it impossible to verify core-method fit and relevance. Several papers appear highly relevant (e.g., Point2Brep, CAD-Recode, TransCAD), but the evidence is insufficient to confirm they are direct matches for B-rep reconstruction from point clouds. The set includes duplicates (P2CADNet appears twice) and papers that may be about primitive fitting benchmarks (SHREC 2022) rather than B-rep reconstruction. Metadata completeness is still an issue for arXiv entries lacking DOIs.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, at least 5 distinct candidate papers remain (e.g., CAD-Recode, Point2Brep, TransCAD, CAD-SIGNet, P2CADNet, autoregressive framework, Surface and Edge Detection, SHREC 2022)."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot confirm that at least 2-3 top candidates are clearly aligned with the user's topic. The evidence snippets are truncated and the relevance notes are generic. For example, 'Surface and Edge Detection for Primitive Fitting of Point Clouds' may be a segmentation method, not necessarily producing a B-rep. 'SHREC 2022' is a benchmark track, not a reconstruction method. The direct match status is unclear."
    },
    "metadata": {
      "passed": false,
      "reason": "Metadata is incomplete for several entries. Multiple arXiv papers lack DOIs (e.g., CAD-Recode, TransCAD, CAD-SIGNet). The evidence snippets are still partial abstracts, not full abstracts, which limits verification."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set respects the 2022-2026 time range and the queries are aligned with the user's focus on parametric CAD and reverse engineering from point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot verify that at least 3 papers are core candidates for point-cloud-to-B-rep reconstruction. The evidence snippets are too brief to assess the core contribution and methodology. Papers like 'Surface and Edge Detection' and 'SHREC 2022' are likely about primitive fitting evaluation, not B-rep reconstruction. The verification_status is 'partial' but evidence_level 'abstract' snippets are incomplete."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence gap: the abstracts are truncated, preventing confirmation of relevance and core contribution. The set includes potential false positives (benchmark, primitive fitting) and duplicates (P2CADNet). The diversity of methods is unclear."
    }
  },
  "key_risks": [
    "Truncated evidence snippets make it impossible to judge the relevance and core contribution of papers, leading to potential inclusion of off-topic works.",
    "Duplicates (P2CADNet) and potential false positives (SHREC 2022 benchmark) could mislead the final report.",
    "Lack of full abstracts may hide that some papers are not primarily about B-rep reconstruction from point clouds."
  ],
  "next_actions": [
    "Retrieve FULL abstracts (not truncated snippets) for the top 8 candidate papers to confirm their focus on point-cloud-to-B-rep/parametric CAD reconstruction. Use direct API calls or source links to obtain complete text.",
    "Explicitly filter out papers that are benchmarks (e.g., SHREC 2022) or focus solely on primitive fitting without B-rep output, unless they are directly relevant to the reconstruction pipeline.",
    "Perform a final deduplication pass to ensure each paper appears only once in the final list, merging entries from different sources."
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
The goal is to identify recent research (2022–2026) on methods that reconstruct Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on core techniques for generating, recovering, or reconstructing editable, parametric CAD models from scanned point clouds, excluding work that outputs only meshes or deals with unrelated CAD applications.

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv using queries targeting:
*   Direct point-cloud-to-B-rep reconstruction.
*   Parametric CAD model generation from point clouds.
*   Reverse engineering of CAD from scanned point cloud data.
The search was refined over two cycles to improve relevance and evidence quality, focusing on retrieving full abstracts to verify the core method and fit.

## Candidate Papers
The search did not clear the quality bar. The evidence gathered from retrieved abstracts is insufficient to confidently verify that a sufficient number of papers are direct matches for the specific task of B-rep reconstruction from point clouds. The final list is split into verified candidates and unverified leads.

### Verified Candidates
Based on the available evidence, no papers could be fully verified as direct matches. The `verification_status` for all retrieved papers remained "partial," with truncated abstract snippets that prevent definitive confirmation of the core method's alignment with the user's request.

### Unverified Leads
The following papers appear title-strong and are within the correct timeframe, but their relevance could not be verified due to incomplete evidence. They are presented as potential leads for follow-up investigation, not as recommendations.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title directly mentions B-rep reconstruction from point clouds; abstract snippet indicates a learning-based framework.
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds (2024)** – Title suggests reverse engineering of CAD operations from point clouds; abstract snippet mentions reconstructing sketch and operation sequences.
*   **TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds (2024)** – Title indicates an end-to-end method for predicting CAD sequences from point clouds.

## Notes and Gaps
*   **Evidence Gap:** The primary failure reason is insufficient evidence. Retrieved abstract snippets were consistently truncated, making it impossible to verify the core contribution, methodology, and whether point clouds are the primary input for B-rep output.
*   **Relevance Uncertainty:** Several papers in the retrieved set (e.g., "SHREC 2022: Fitting and recognition of simple geometric primitives") appear to be benchmark or primitive-fitting studies, not direct B-rep reconstruction methods. Without full abstracts, these could not be confidently filtered out.
*   **Metadata Incompleteness:** Several arXiv entries lacked DOIs, and some author lists appeared incomplete or duplicated.

## Recommended Next Steps
1.  **Manual Abstract Retrieval:** Directly visit the source links (e.g., arXiv, DOI links) for the top candidate papers to read full abstracts and confirm relevance.
2.  **Citation Chaining:** Use the most promising leads (e.g., "Point2Brep," "CAD-Recode") as seed papers to search for citing and related work in Google Scholar or Semantic Scholar.
3.  **Focused Database Search:** Conduct a targeted search in engineering and computer graphics databases (e.g., ACM Digital Library, IEEE Xplore) using combined keywords like `("B-rep" OR "boundary representation") AND ("point cloud" AND reconstruction)`.
4.  **Conference Focus:** Prioritize searching proceedings from top-tier conferences in computer graphics (SIGGRAPH, SIGGRAPH Asia) and CAD (CAD/Graphics, SPM) from the 2022-2026 period.

TERMINATE
```
