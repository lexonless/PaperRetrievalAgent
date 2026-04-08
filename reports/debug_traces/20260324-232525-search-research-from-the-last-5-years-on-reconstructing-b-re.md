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
**Generated At:** 2026-03-24T23:25:25
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
    "B-rep generation from 3D scans",
    "deep learning for CAD reconstruction"
  ],
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds",
      "reason": "Directly targets the core task described by the user."
    },
    {
      "query": "point cloud to boundary representation deep learning",
      "reason": "Captures modern data-driven methods that are likely prominent in recent literature."
    },
    {
      "query": "CAD reverse engineering from scanned point cloud",
      "reason": "Broadens to the applied reverse-engineering context, which often involves B-rep output."
    }
  ],
  "assumptions": [
    "The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.",
    "Recent high-impact papers may use 'CAD reconstruction' or 'structured CAD generation' with point clouds as input.",
    "Multi-stage pipelines that ultimately produce a B-rep are considered relevant."
  ],
  "success_criteria": [
    "Retrieve papers where point cloud is a primary input and B-rep/CAD model is an explicit output.",
    "Identify key methodological categories (e.g., optimization-based, learning-based, hybrid).",
    "Cover significant advances from 2022-2026 to enable trend analysis."
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
    "point cloud to CAD reconstruction",
    "B-rep generation from 3D scans",
    "deep learning for CAD reconstruction"
  ],
  "queries": [
    {
      "query": "Point2Brep point cloud reconstruction",
      "reason": "Targets a specific, highly relevant 2026 paper identified in the initial retrieval to verify its input modality and contribution."
    },
    {
      "query": "CAD reverse engineering point cloud scan B-rep",
      "reason": "Broad query to capture papers that explicitly mention point cloud/scan as input for CAD/B-rep reverse engineering, addressing the evidence gap."
    },
    {
      "query": "\"point cloud\" \"B-rep\" reconstruction",
      "reason": "A more precise query to force the co-occurrence of the key terms 'point cloud' and 'B-rep' in the retrieved evidence."
    }
  ],
  "assumptions": [
    "The initial retrieval captured relevant papers, but their abstracts need verification for point cloud input and B-rep output.",
    "Papers like 'CAD-Recode' and 'TransCAD' are likely relevant as they mention '3D scan' and 'point cloud' in snippets, but this must be confirmed.",
    "If primary queries fail, the fallback queries will be used to ensure coverage."
  ],
  "success_criteria": [
    "Retrieve full abstracts or introductory text for candidate papers to explicitly confirm point cloud input and B-rep/CAD output.",
    "Replace generic relevance notes with evidence-based statements for each retained paper.",
    "Filter out papers not meeting the core input/output requirement.",
    "Provide a verified set of at least 5-7 papers for the final report."
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
      "query": "B-rep reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to boundary representation deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD reverse engineering from scanned point cloud",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ]
    },
    {
      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-11-27T07:16:53Z",
      "url": "http://arxiv.org/abs/2511.22171v1",
      "doi": "",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Weize Quan",
        "Biao Zhang",
        "Peter Wonka",
        "Dong-Ming Yan"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive fram"
      ]
    },
    {
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-04-19T10:34:24Z",
      "url": "http://arxiv.org/abs/2504.14257v3",
      "doi": "",
      "authors": [
        "Yilin Liu",
        "Duoteng Xu",
        "Xingyao Yu",
        "Xiang Xu",
        "Daniel Cohen-Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\textit{holistic latent}$ (HoLa) space. This is based on the s"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ]
    },
    {
      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds Using Layer-Wise Sketch Instance Guided Attention",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-06-16",
      "url": "https://doi.org/10.1109/cvpr52733.2024.00451",
      "doi": "10.1109/cvpr52733.2024.00451",
      "authors": [
        "Mohammad Sadil Khan",
        "Elona Dupont",
        "Sk Aziz Ali",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and aetoregressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion fr"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep generation from 3D scans",
      "deep learning for CAD reconstruction"
    ],
    "effective_query": "B-rep reconstruction from point clouds",
    "used_override_query": false,
    "executed_queries": [
      "B-rep reconstruction from point clouds",
      "point cloud to boundary representation deep learning",
      "CAD reverse engineering from scanned point cloud"
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
      "query": "\"point cloud\" \"B-rep\" reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "Point2Brep point cloud reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD reverse engineering point cloud scan B-rep",
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
      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref | OpenAlex",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-07-07T08:43:46Z",
      "url": "http://arxiv.org/abs/2507.04765v1",
      "doi": "",
      "authors": [
        "Weilin Lai",
        "Tie Xu",
        "Hu Wang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometr"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "excerpt",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve",
        "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation HAOXIANG GUO, Tsinghua University, and Microsoft Research Asia, China SHILIN LIU, University of Science and Technology of China, and Microsoft Research Asia, China HAO PAN, YANG LIU, XIN TONG, and BAINING GUO,Microsoft Research Asia, China (a) (b) (c) (d) Fig. 1. ComplexGen for CAD reconstruction from point clouds. Given an input poi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 41 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep generation from 3D scans",
      "deep learning for CAD reconstruction"
    ],
    "effective_query": "\"point cloud\" \"B-rep\" reconstruction",
    "used_override_query": true,
    "executed_queries": [
      "\"point cloud\" \"B-rep\" reconstruction",
      "Point2Brep point cloud reconstruction",
      "CAD reverse engineering point cloud scan B-rep"
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
  "review_summary": "The retrieval captured a promising set of recent papers (2022-2026) on B-rep and CAD reconstruction from point clouds, with good source coverage and metadata. However, the evidence for core relevance is insufficient. The 'relevance_note' for every paper is a generic placeholder stating 'Final task fit should be determined by reranking and reviewer inspection,' and the evidence snippets are truncated abstracts that do not explicitly confirm the papers take point clouds as input. This prevents a reliable assessment of whether the hard requirements for relevance, core-method fit, and query fit are met. A revision is needed to verify the input modality and core contribution of each candidate.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 2,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 distinct candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be determined. The evidence snippets and relevance notes do not explicitly confirm that these papers use point clouds as the primary input for B-rep reconstruction. The notes are generic placeholders."
    },
    "metadata": {
      "passed": true,
      "reason": "All retained candidates have title, source, year/date, and URL. Author lists are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "Cannot be verified. The user's explicit constraint is 'point clouds are the main input.' The current evidence does not confirm this for any paper. The time range (2022-2026) is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be assessed. To count as a core candidate, a paper must be clearly aligned with the topic. The current evidence is insufficient to judge this for any paper, as the snippets do not establish the input modality or specific B-rep reconstruction contribution."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are from 2024-2026, within the resolved range (2022-2026). No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major gaps are apparent from the titles and years. The set appears to cover learning-based and structured generation methods."
    }
  },
  "key_risks": [
    "The evidence does not confirm point cloud input. Several papers (e.g., 'CAD-Recode', 'TransCAD', 'CAD-SIGNet') mention '3D scan' or 'point cloud' in the snippet, but the connection is not explicit enough to satisfy the hard requirement without verification.",
    "The 'relevance_note' field is not populated with actual reasoning, making automated assessment impossible.",
    "Potential over-reliance on arXiv preprints; however, conference versions are also indicated for some."
  ],
  "next_actions": [
    "For each candidate paper, especially the top 5-7, retrieve a fuller abstract or introductory text to explicitly verify: 1) that point cloud/3D scan is a primary input, and 2) that the output is a B-rep or CAD model (not just a mesh).",
    "Replace the generic 'relevance_note' placeholder with a concise, evidence-based statement for each paper, explaining its direct or close relation to the user's topic.",
    "Filter out any papers where the primary input is clearly not a point cloud (e.g., images, text-only) or where the output is not a B-rep/CAD model.",
    "Ensure the final retained set has at least 3 papers with strong, verified evidence of being core to point-cloud-to-B-rep reconstruction."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The revision improved evidence for some papers (e.g., ComplexGen now has a snippet explicitly mentioning 'input point clouds'), and the set includes strong candidates like Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet. However, the 'relevance_note' field remains a generic placeholder ('Final task fit should be determined by reranking and reviewer inspection') for every paper, preventing automated verification of relevance and core-method fit. Furthermore, evidence for papers like Split-and-Fit, GraphBrep, and Brep2Seq does not explicitly confirm point cloud input. The hard requirements for relevance and core-method fit cannot be passed without explicit, evidence-based relevance notes. A final verification step is needed to populate these notes and filter any non-conforming papers.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 distinct candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be definitively assessed. While snippets for Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet strongly suggest point cloud input and B-rep/CAD output, the relevance notes are generic placeholders and do not provide the required explanation. Papers like Split-and-Fit and GraphBrep lack explicit point cloud evidence in their snippets."
    },
    "metadata": {
      "passed": true,
      "reason": "All retained candidates have title, source, year/date, and URL. Author lists are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "Partially satisfied for some papers, but not verified across the set. The user's constraint 'point clouds are the main input' is explicitly mentioned in evidence for Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet. However, other papers (e.g., Split-and-Fit, GraphBrep, Brep2Seq) lack this confirmation in the provided snippets. The time range is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be reliably assessed. At least 4 papers (Point2Brep, ComplexGen, CAD-Recode, CAD-SIGNet) appear to be core candidates based on evidence snippets, but the generic relevance notes prevent a formal pass. The reviewer cannot confirm the 'core contribution' or alignment without evidence-based notes."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are from 2022-2026, within the resolved range. No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "The set appears to cover a range of methods (learning-based, sequence prediction, geometric partitioning). No obvious major subtopic is missing given the evidence."
    }
  },
  "key_risks": [
    "The 'relevance_note' field is still populated with a boilerplate placeholder, not actual reasoning. This is a critical failure for the review gate.",
    "Evidence for some papers (Split-and-Fit, GraphBrep, Brep2Seq) does not explicitly mention point cloud input, leaving their relevance ambiguous.",
    "Potential duplication: 'ComplexGen' appears three times (OpenAlex, arXiv, and another OpenAlex entry) with different source strings; they are likely the same paper but are listed as separate entries."
  ],
  "next_actions": [
    "For each retained paper, replace the generic 'relevance_note' with a concise, evidence-based statement. Example: 'Direct match: proposes a learning-based framework to reconstruct B-rep models from unstructured point clouds, as stated in the abstract.'",
    "Explicitly verify the input modality for papers with ambiguous evidence (Split-and-Fit, GraphBrep, Brep2Seq, CAD-MLLM). If point cloud is not a primary input, filter them out.",
    "Merge duplicate entries for 'ComplexGen' into a single record with combined source information.",
    "Ensure the final list contains at least 5 papers with verified point cloud input and B-rep/CAD output, and that each has a proper relevance note."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_kXqqsKj5vo5KUexYL2RnxboZ', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to boundary representation deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD reverse engineering from scanned point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-17T16:24:36Z",\n      "url": "http://arxiv.org/abs/2407.12702v2",\n      "doi": "",\n      "authors": [\n        "Elona Dupont",\n        "Kseniya Cherenkova",\n        "Dimitrios Mallis",\n        "Gleb Gusev",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive fram"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the s"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds Using Layer-Wise Sketch Instance Guided Attention",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-06-16",\n      "url": "https://doi.org/10.1109/cvpr52733.2024.00451",\n      "doi": "10.1109/cvpr52733.2024.00451",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and aetoregressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion fr"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep generation from 3D scans",\n      "deep learning for CAD reconstruction"\n    ],\n    "effective_query": "B-rep reconstruction from point clouds",\n    "used_override_query": false,\n    "executed_queries": [\n      "B-rep reconstruction from point clouds",\n      "point cloud to boundary representation deep learning",\n      "CAD reverse engineering from scanned point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_kXqqsKj5vo5KUexYL2RnxboZ' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_PQ6vtHHLKnlCv8R5Fn6N65RN', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "\\"point cloud\\" \\"B-rep\\" reconstruction"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"point cloud\\" \\"B-rep\\" reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "Point2Brep point cloud reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD reverse engineering point cloud scan B-rep",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometr"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "excerpt",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve",\n        "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation HAOXIANG GUO, Tsinghua University, and Microsoft Research Asia, China SHILIN LIU, University of Science and Technology of China, and Microsoft Research Asia, China HAO PAN, YANG LIU, XIN TONG, and BAINING GUO,Microsoft Research Asia, China (a) (b) (c) (d) Fig. 1. ComplexGen for CAD reconstruction from point clouds. Given an input poi"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 41 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep generation from 3D scans",\n      "deep learning for CAD reconstruction"\n    ],\n    "effective_query": "\\"point cloud\\" \\"B-rep\\" reconstruction",\n    "used_override_query": true,\n    "executed_queries": [\n      "\\"point cloud\\" \\"B-rep\\" reconstruction",\n      "Point2Brep point cloud reconstruction",\n      "CAD reverse engineering point cloud scan B-rep"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_PQ6vtHHLKnlCv8R5Fn6N65RN' is_error=False
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
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep generation from 3D scans", "deep learning for CAD reconstruction"],
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds",
      "reason": "Directly targets the core task described by the user."
    },
    {
      "query": "point cloud to boundary representation deep learning",
      "reason": "Captures modern data-driven methods that are likely prominent in recent literature."
    },
    {
      "query": "CAD reverse engineering from scanned point cloud",
      "reason": "Broadens to the applied reverse-engineering context, which often involves B-rep output."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.", "Recent high-impact papers may use 'CAD reconstruction' or 'structured CAD generation' with point clouds as input.", "Multi-stage pipelines that ultimately produce a B-rep are considered relevant."],
  "success_criteria": ["Retrieve papers where point cloud is a primary input and B-rep/CAD model is an explicit output.", "Identify key methodological categories (e.g., optimization-based, learning-based, hybrid).", "Cover significant advances from 2022-2026 to enable trend analysis."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan using the provided queries to find relevant papers from 2022-2026 on B-rep reconstruction from point clouds.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_kXqqsKj5vo5KUexYL2RnxboZ', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to boundary representation deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD reverse engineering from scanned point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-17T16:24:36Z",\n      "url": "http://arxiv.org/abs/2407.12702v2",\n      "doi": "",\n      "authors": [\n        "Elona Dupont",\n        "Kseniya Cherenkova",\n        "Dimitrios Mallis",\n        "Gleb Gusev",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive fram"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the s"\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds Using Layer-Wise Sketch Instance Guided Attention",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-06-16",\n      "url": "https://doi.org/10.1109/cvpr52733.2024.00451",\n      "doi": "10.1109/cvpr52733.2024.00451",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and aetoregressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion fr"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering from scanned pointcloud\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep generation from 3D scans",\n      "deep learning for CAD reconstruction"\n    ],\n    "effective_query": "B-rep reconstruction from point clouds",\n    "used_override_query": false,\n    "executed_queries": [\n      "B-rep reconstruction from point clouds",\n      "point cloud to boundary representation deep learning",\n      "CAD reverse engineering from scanned point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_kXqqsKj5vo5KUexYL2RnxboZ' is_error=False
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
      "query": "B-rep reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to boundary representation deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD reverse engineering from scanned point cloud",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D reverse engineering, in which a CAD model is inferred given a 3D scan of a physical object, is a research direction that offers many promising practical applications. This paper proposes TransCAD, an end-to-end transformer-based architecture that predicts the CAD sequence from a point cloud. TransCAD leverages the structure of CAD sequences by using a hierarchical learning strategy. A loop refi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ]
    },
    {
      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-11-27T07:16:53Z",
      "url": "http://arxiv.org/abs/2511.22171v1",
      "doi": "",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Weize Quan",
        "Biao Zhang",
        "Peter Wonka",
        "Dong-Ming Yan"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive fram"
      ]
    },
    {
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-04-19T10:34:24Z",
      "url": "http://arxiv.org/abs/2504.14257v3",
      "doi": "",
      "authors": [
        "Yilin Liu",
        "Duoteng Xu",
        "Xingyao Yu",
        "Xiang Xu",
        "Daniel Cohen-Or",
        "Hao Zhang",
        "Hui Huang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\textit{holistic latent}$ (HoLa) space. This is based on the s"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'brep reconstruction from pointclouds'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ]
    },
    {
      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds Using Layer-Wise Sketch Instance Guided Attention",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-06-16",
      "url": "https://doi.org/10.1109/cvpr52733.2024.00451",
      "doi": "10.1109/cvpr52733.2024.00451",
      "authors": [
        "Mohammad Sadil Khan",
        "Elona Dupont",
        "Sk Aziz Ali",
        "Kseniya Cherenkova",
        "Anis Kacem",
        "Djamila Aouada"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and aetoregressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion fr"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering from scanned pointcloud'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep generation from 3D scans",
      "deep learning for CAD reconstruction"
    ],
    "effective_query": "B-rep reconstruction from point clouds",
    "used_override_query": false,
    "executed_queries": [
      "B-rep reconstruction from point clouds",
      "point cloud to boundary representation deep learning",
      "CAD reverse engineering from scanned point cloud"
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
  "review_summary": "The retrieval captured a promising set of recent papers (2022-2026) on B-rep and CAD reconstruction from point clouds, with good source coverage and metadata. However, the evidence for core relevance is insufficient. The 'relevance_note' for every paper is a generic placeholder stating 'Final task fit should be determined by reranking and reviewer inspection,' and the evidence snippets are truncated abstracts that do not explicitly confirm the papers take point clouds as input. This prevents a reliable assessment of whether the hard requirements for relevance, core-method fit, and query fit are met. A revision is needed to verify the input modality and core contribution of each candidate.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 2,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 distinct candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be determined. The evidence snippets and relevance notes do not explicitly confirm that these papers use point clouds as the primary input for B-rep reconstruction. The notes are generic placeholders."
    },
    "metadata": {
      "passed": true,
      "reason": "All retained candidates have title, source, year/date, and URL. Author lists are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "Cannot be verified. The user's explicit constraint is 'point clouds are the main input.' The current evidence does not confirm this for any paper. The time range (2022-2026) is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be assessed. To count as a core candidate, a paper must be clearly aligned with the topic. The current evidence is insufficient to judge this for any paper, as the snippets do not establish the input modality or specific B-rep reconstruction contribution."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are from 2024-2026, within the resolved range (2022-2026). No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious major gaps are apparent from the titles and years. The set appears to cover learning-based and structured generation methods."
    }
  },
  "key_risks": [
    "The evidence does not confirm point cloud input. Several papers (e.g., 'CAD-Recode', 'TransCAD', 'CAD-SIGNet') mention '3D scan' or 'point cloud' in the snippet, but the connection is not explicit enough to satisfy the hard requirement without verification.",
    "The 'relevance_note' field is not populated with actual reasoning, making automated assessment impossible.",
    "Potential over-reliance on arXiv preprints; however, conference versions are also indicated for some."
  ],
  "next_actions": [
    "For each candidate paper, especially the top 5-7, retrieve a fuller abstract or introductory text to explicitly verify: 1) that point cloud/3D scan is a primary input, and 2) that the output is a B-rep or CAD model (not just a mesh).",
    "Replace the generic 'relevance_note' placeholder with a concise, evidence-based statement for each paper, explaining its direct or close relation to the user's topic.",
    "Filter out any papers where the primary input is clearly not a point cloud (e.g., images, text-only) or where the output is not a B-rep/CAD model.",
    "Ensure the final retained set has at least 3 papers with strong, verified evidence of being core to point-cloud-to-B-rep reconstruction."
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
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep generation from 3D scans", "deep learning for CAD reconstruction"],
  "queries": [
    {
      "query": "Point2Brep point cloud reconstruction",
      "reason": "Targets a specific, highly relevant 2026 paper identified in the initial retrieval to verify its input modality and contribution."
    },
    {
      "query": "CAD reverse engineering point cloud scan B-rep",
      "reason": "Broad query to capture papers that explicitly mention point cloud/scan as input for CAD/B-rep reverse engineering, addressing the evidence gap."
    },
    {
      "query": "\"point cloud\" \"B-rep\" reconstruction",
      "reason": "A more precise query to force the co-occurrence of the key terms 'point cloud' and 'B-rep' in the retrieved evidence."
    }
  ],
  "assumptions": ["The initial retrieval captured relevant papers, but their abstracts need verification for point cloud input and B-rep output.", "Papers like 'CAD-Recode' and 'TransCAD' are likely relevant as they mention '3D scan' and 'point cloud' in snippets, but this must be confirmed.", "If primary queries fail, the fallback queries will be used to ensure coverage."],
  "success_criteria": ["Retrieve full abstracts or introductory text for candidate papers to explicitly confirm point cloud input and B-rep/CAD output.", "Replace generic relevance notes with evidence-based statements for each retained paper.", "Filter out papers not meeting the core input/output requirement.", "Provide a verified set of at least 5-7 papers for the final report."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the revised search plan with more targeted queries to verify the input modality and contributions of the papers.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_PQ6vtHHLKnlCv8R5Fn6N65RN', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "\\"point cloud\\" \\"B-rep\\" reconstruction"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"point cloud\\" \\"B-rep\\" reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "Point2Brep point cloud reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD reverse engineering point cloud scan B-rep",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometr"\n      ]\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ]\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ]\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "excerpt",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve",\n        "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation HAOXIANG GUO, Tsinghua University, and Microsoft Research Asia, China SHILIN LIU, University of Science and Technology of China, and Microsoft Research Asia, China HAO PAN, YANG LIU, XIN TONG, and BAINING GUO,Microsoft Research Asia, China (a) (b) (c) (d) Fig. 1. ComplexGen for CAD reconstruction from point clouds. Given an input poi"\n      ]\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'pointcloud brep reconstruction\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around \'cad reverse engineering pointcloud scan brep\'. Final task fit should be determined by reranking and reviewer inspection.",\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 41 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "point cloud to CAD reconstruction",\n      "B-rep generation from 3D scans",\n      "deep learning for CAD reconstruction"\n    ],\n    "effective_query": "\\"point cloud\\" \\"B-rep\\" reconstruction",\n    "used_override_query": true,\n    "executed_queries": [\n      "\\"point cloud\\" \\"B-rep\\" reconstruction",\n      "Point2Brep point cloud reconstruction",\n      "CAD reverse engineering point cloud scan B-rep"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_PQ6vtHHLKnlCv8R5Fn6N65RN' is_error=False
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
      "query": "\"point cloud\" \"B-rep\" reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "Point2Brep point cloud reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD reverse engineering point cloud scan B-rep",
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
      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref | OpenAlex",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ]
    },
    {
      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-07-07T08:43:46Z",
      "url": "http://arxiv.org/abs/2507.04765v1",
      "doi": "",
      "authors": [
        "Weilin Lai",
        "Tie Xu",
        "Hu Wang"
      ],
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometr"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "excerpt",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve",
        "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation HAOXIANG GUO, Tsinghua University, and Microsoft Research Asia, China SHILIN LIU, University of Science and Technology of China, and Microsoft Research Asia, China HAO PAN, YANG LIU, XIN TONG, and BAINING GUO,Microsoft Research Asia, China (a) (b) (c) (d) Fig. 1. ComplexGen for CAD reconstruction from point clouds. Given an input poi"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'pointcloud brep reconstruction'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
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
      "relevance_note": "Abstract or excerpt evidence matched retrieval query terms around 'cad reverse engineering pointcloud scan brep'. Final task fit should be determined by reranking and reviewer inspection.",
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 41 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "point cloud to CAD reconstruction",
      "B-rep generation from 3D scans",
      "deep learning for CAD reconstruction"
    ],
    "effective_query": "\"point cloud\" \"B-rep\" reconstruction",
    "used_override_query": true,
    "executed_queries": [
      "\"point cloud\" \"B-rep\" reconstruction",
      "Point2Brep point cloud reconstruction",
      "CAD reverse engineering point cloud scan B-rep"
    ],
    "fallback_used": false
  }
}
```

### Message 13

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=8

```text
{
  "decision": "REVISE",
  "review_summary": "The revision improved evidence for some papers (e.g., ComplexGen now has a snippet explicitly mentioning 'input point clouds'), and the set includes strong candidates like Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet. However, the 'relevance_note' field remains a generic placeholder ('Final task fit should be determined by reranking and reviewer inspection') for every paper, preventing automated verification of relevance and core-method fit. Furthermore, evidence for papers like Split-and-Fit, GraphBrep, and Brep2Seq does not explicitly confirm point cloud input. The hard requirements for relevance and core-method fit cannot be passed without explicit, evidence-based relevance notes. A final verification step is needed to populate these notes and filter any non-conforming papers.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 distinct candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Cannot be definitively assessed. While snippets for Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet strongly suggest point cloud input and B-rep/CAD output, the relevance notes are generic placeholders and do not provide the required explanation. Papers like Split-and-Fit and GraphBrep lack explicit point cloud evidence in their snippets."
    },
    "metadata": {
      "passed": true,
      "reason": "All retained candidates have title, source, year/date, and URL. Author lists are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "Partially satisfied for some papers, but not verified across the set. The user's constraint 'point clouds are the main input' is explicitly mentioned in evidence for Point2Brep, ComplexGen, CAD-Recode, and CAD-SIGNet. However, other papers (e.g., Split-and-Fit, GraphBrep, Brep2Seq) lack this confirmation in the provided snippets. The time range is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Cannot be reliably assessed. At least 4 papers (Point2Brep, ComplexGen, CAD-Recode, CAD-SIGNet) appear to be core candidates based on evidence snippets, but the generic relevance notes prevent a formal pass. The reviewer cannot confirm the 'core contribution' or alignment without evidence-based notes."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All listed papers are from 2022-2026, within the resolved range. No out-of-range papers are present."
    },
    "gaps": {
      "passed": true,
      "reason": "The set appears to cover a range of methods (learning-based, sequence prediction, geometric partitioning). No obvious major subtopic is missing given the evidence."
    }
  },
  "key_risks": [
    "The 'relevance_note' field is still populated with a boilerplate placeholder, not actual reasoning. This is a critical failure for the review gate.",
    "Evidence for some papers (Split-and-Fit, GraphBrep, Brep2Seq) does not explicitly mention point cloud input, leaving their relevance ambiguous.",
    "Potential duplication: 'ComplexGen' appears three times (OpenAlex, arXiv, and another OpenAlex entry) with different source strings; they are likely the same paper but are listed as separate entries."
  ],
  "next_actions": [
    "For each retained paper, replace the generic 'relevance_note' with a concise, evidence-based statement. Example: 'Direct match: proposes a learning-based framework to reconstruct B-rep models from unstructured point clouds, as stated in the abstract.'",
    "Explicitly verify the input modality for papers with ambiguous evidence (Split-and-Fit, GraphBrep, Brep2Seq, CAD-MLLM). If point cloud is not a primary input, filter them out.",
    "Merge duplicate entries for 'ComplexGen' into a single record with combined source information.",
    "Ensure the final list contains at least 5 papers with verified point cloud input and B-rep/CAD output, and that each has a proper relevance note."
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
The goal is to identify recent research (2022–2026) on methods that reconstruct or generate Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on works where point clouds are the primary input and a structured B-rep is the explicit output, encompassing reverse engineering and geometric deep learning approaches.

## Search Strategy
The search was conducted in three phases:
1.  **Initial Broad Search:** Queries like "B-rep reconstruction from point clouds" and "CAD reverse engineering from scanned point cloud" were used to capture a wide candidate set from Crossref, OpenAlex, and arXiv.
2.  **Targeted Verification:** A second round used precise queries (e.g., `"point cloud" "B-rep" reconstruction`) to force co-occurrence of key terms and verify the input modality of promising candidates.
3.  **Review & Filtering:** Papers were assessed against hard requirements: publication within 2022-2026, point cloud as a main input, and B-rep/CAD model as the target output. Ambiguous candidates were filtered out.

## Candidate Papers
The following papers represent the strongest, verified candidates for point-cloud-to-B-rep reconstruction from the last five years.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref / SSRN
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Core Contribution:** Proposes a geometry-aware framework that integrates learning-based inference with explicit parametric fitting to reconstruct complete, topologically consistent B-rep models from unstructured point clouds.
    *   **Relevance Note:** **Direct match.** The abstract explicitly states the method reconstructs B-reps "from unstructured point clouds."

*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   **Source:** ACM TOG / arXiv
    *   **Link:** https://doi.org/10.1145/3528223.3530078
    *   **Core Contribution:** Frames B-rep reconstruction as the detection of vertices, edges, and surfaces, holistically modeled as a chain complex. Presents an end-to-end network that directly predicts the structured B-rep from an input point cloud.
    *   **Relevance Note:** **Direct match.** The paper's introduction and figures explicitly demonstrate reconstruction "from point clouds."

*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2412.14042v2
    *   **Core Contribution:** Addresses CAD reverse engineering by reconstructing parametric sketch and operation sequences from 3D representations, explicitly including point clouds.
    *   **Relevance Note:** **Direct match.** The abstract defines the problem as reconstructing CAD sequences "from 3D representations such as point clouds."

*   **CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention** (2024)
    *   **Source:** CVPR / arXiv
    *   **Link:** https://arxiv.org/abs/2402.17678v1
    *   **Core Contribution:** An end-to-end, autoregressive architecture designed to recover a CAD model's design history (sketch-and-extrusion sequence) from a 3D scan/point cloud.
    *   **Relevance Note:** **Direct match.** The abstract states the aim is to uncover the CAD process "given its 3D scan."

*   **TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2407.12702v2
    *   **Core Contribution:** An end-to-end transformer-based architecture that predicts a CAD construction sequence directly from an input point cloud, using a hierarchical refinement strategy.
    *   **Relevance Note:** **Direct match.** The paper's core task is predicting "the CAD sequence from a point cloud" for 3D reverse engineering.

## Notes and Gaps
*   **Methodological Focus:** The state-of-the-art is dominated by deep learning approaches, particularly transformer-based and graph-based networks that predict structured outputs (sequences, graphs, or complex hierarchies).
*   **Trend:** A clear shift from classic geometric fitting to data-driven, holistic reconstruction that jointly reasons about geometry and topology.
*   **Evidence Gaps:** Several initially retrieved papers (e.g., Split-and-Fit, GraphBrep, Brep2Seq) were excluded from the final list because their provided abstracts did not explicitly confirm point cloud as the primary input, highlighting a gap in easily verifiable metadata for this niche.
*   **Scope:** The search focused on academic literature. Patents or industry-specific techniques may not be covered.

## Recommended Next Steps
1.  **Explore Hybrid Methods:** Investigate recent works that combine the robustness of classical geometric processing with the high-level reasoning of learning-based models.
2.  **Benchmark Datasets:** Examine the datasets used by these papers (e.g., ABC dataset, Fusion 360 Gallery) to understand the scope and limitations of current evaluation.
3.  **Downstream Applications:** Look for research applying these reconstruction methods to specific domains like digital twins, legacy part redesign, or additive manufacturing preparation.
4.  **Follow-up on Leads:** Papers like **HoLa: B-Rep Generation using a Holistic Latent Representation** (2025) and **BrepGPT** (2025) appeared relevant by title but lacked explicit point-cloud input confirmation in snippets; they represent strong leads for manual follow-up.

TERMINATE
```
