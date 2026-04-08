# Paper Search Debug Trace

**Query:** Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus on papers where the primary task is to take point clouds as input and reconstruct B-rep as the final output representation.

Prioritize papers whose main contribution is the full B-rep reconstruction problem itself, rather than only a subproblem, intermediate representation, auxiliary module, downstream application, or a different reconstruction/CAD task.

A paper should be treated as a core candidate only if reconstructing B-rep from point clouds is the paper's primary task and B-rep is the final target output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it truly fits the point-cloud-to-B-rep reconstruction task

Then summarize:
- major method categories
- recent trends
- open challenges

Be selective, but avoid over-filtering papers merely because the method is multi-stage or uses intermediate steps within the reconstruction pipeline.
**Generated At:** 2026-03-24T12:56:45
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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is reconstructing B-rep representations directly from point clouds as the final output, focusing on core methods for the full problem rather than subproblems or auxiliary modules.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "point cloud to B-rep reconstruction",
    "boundary representation reconstruction",
    "CAD from 3D scans",
    "geometric deep learning for B-rep generation",
    "structured CAD model recovery"
  ],
  "exclude_areas": [
    "mesh reconstruction only",
    "surface fitting without topological structure",
    "intermediate representation learning (e.g., CSG, SDF) not outputting B-rep",
    "downstream applications like segmentation or classification",
    "B-rep reconstruction from other inputs (e.g., images, sketches)"
  ],
  "fallback_queries": [
    "CAD reconstruction from point clouds",
    "B-rep generation 3D scanning",
    "reverse engineering point cloud to CAD"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction deep learning",
      "reason": "Targets modern learning-based methods that directly output B-rep structures from point cloud input."
    },
    {
      "query": "B-rep reconstruction from 3D scans recent",
      "reason": "Captures reverse engineering and scanning-focused literature that may not explicitly use 'point cloud' in the title."
    },
    {
      "query": "CAD model recovery from point clouds 2024",
      "reason": "Focuses on the CAD reconstruction task, which often implies B-rep as the target representation in recent research."
    }
  ],
  "assumptions": [
    "The term 'B-rep' in recent literature may be interchanged with 'CAD model', 'boundary representation', or 'structured CAD'.",
    "Some papers may present multi-stage pipelines where B-rep is the final output; these are included if the primary task is full reconstruction.",
    "Conference venues likely include SIGGRAPH, CVPR, ICCV, CAD, and SPM."
  ],
  "success_criteria": [
    "Retrieve 5-10 papers where the abstract or contribution explicitly states B-rep reconstruction from point clouds as the primary goal.",
    "Papers should present a complete method or framework yielding a B-rep model.",
    "Exclude papers where B-rep is only an intermediate step or not the final output."
  ]
}
```

### Planner Output 8

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) where the primary task is reconstructing B-rep representations directly from point clouds as the final output, focusing on core methods for the full problem rather than subproblems or auxiliary modules.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "point cloud to B-rep reconstruction",
    "boundary representation reconstruction",
    "CAD from 3D scans",
    "geometric deep learning for B-rep generation",
    "structured CAD model recovery",
    "reverse engineering CAD from point clouds"
  ],
  "exclude_areas": [
    "mesh reconstruction only",
    "surface fitting without topological structure",
    "intermediate representation learning (e.g., CSG, SDF) not outputting B-rep",
    "downstream applications like segmentation or classification",
    "B-rep reconstruction from other inputs (e.g., images, sketches)",
    "medical imaging reconstruction",
    "point cloud denoising or upsampling",
    "general multi-view 3D reconstruction"
  ],
  "fallback_queries": [
    "CAD reconstruction from 3D point clouds",
    "reverse engineering B-rep from scans",
    "structured CAD model generation point cloud"
  ],
  "queries": [
    {
      "query": "boundary representation reconstruction from point clouds",
      "reason": "Directly targets the core task using precise terminology to filter out irrelevant works on meshes or other representations."
    },
    {
      "query": "B-rep CAD model generation from 3D point cloud",
      "reason": "Focuses on the generative aspect and CAD context, likely to capture recent learning-based methods in top venues."
    },
    {
      "query": "reverse engineering parametric CAD from point cloud deep learning",
      "reason": "Emphasizes the reverse engineering pipeline and parametric CAD, which inherently involves B-rep output."
    }
  ],
  "assumptions": [
    "Key venues include SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, ECCV, CAD, and SPM.",
    "A paper's primary contribution is considered 'core' if the abstract explicitly states reconstruction of a B-rep or editable CAD model from a point cloud.",
    "Multi-stage pipelines are included if B-rep is the final, explicit output."
  ],
  "success_criteria": [
    "Retrieve 5-10 papers where the abstract confirms point cloud input and B-rep/CAD model output as the main goal.",
    "Exclude papers focused solely on segmentation, feature detection, or intermediate representations without final B-rep reconstruction.",
    "Ensure evidence snippets explicitly mention 'B-rep', 'boundary representation', 'editable CAD model', or 'parametric CAD' from point clouds."
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
      "query": "point cloud to B-rep reconstruction deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-rep reconstruction from 3D scans recent",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model recovery from point clouds 2024",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models",
      "source": "Crossref / Electronics",
      "year": 2025,
      "date": "2025-1-20",
      "url": "https://doi.org/10.3390/electronics14020399",
      "doi": "10.3390/electronics14020399",
      "authors": [
        "Seyyedbehrad Emadi",
        "Marco Limongiello"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ],
      "duplicate_group": ""
    },
    {
      "title": "AI-Powered 3D Reconstruction from 2D Scans",
      "source": "Crossref / International Journal of Humanities and Information Technology",
      "year": 2024,
      "date": "2024-6-28",
      "url": "https://doi.org/10.21590/ijhit.06.02.4",
      "doi": "10.21590/ijhit.06.02.4",
      "authors": [
        "Arjun Deshraje Urs"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Artificial intelligence (AI) is reshaping how medical images are interpreted and used in practice. Traditionally, clinicians rely on 2D radiological slices such as CT and MRI to infer 3D anatomical structures, a process that is mentally demanding and often variable between observers. With AI, these 2D slices can now be transformed into detailed, interactive 3D models in real time. Such mod"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Puzzles: Unbounded Video-Depth Augmentation for Scalable End-to-End 3D Reconstruction",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-06-30T13:57:24Z",
      "url": "http://arxiv.org/abs/2506.23863v1",
      "doi": "",
      "authors": [
        "Jiahao Ma",
        "Lei Wang",
        "Miaomiao liu",
        "David Ahmedt-Aristizabal",
        "Chuong Nguyen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Multi-view 3D reconstruction remains a core challenge in computer vision. Recent methods, such as DUST3R and its successors, directly regress pointmaps from image pairs without relying on known scene geometry or camera parameters. However, the performance of these models is constrained by the diversity and scale of available training data. In this work, we introduce Puzzles, a data augmentation st"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Self-Supervised Kidney Tumor Segmentation Using Random Block Reconstruction on 3D CT Scans",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026-2-11",
      "url": "https://doi.org/10.21203/rs.3.rs-8138834/v1",
      "doi": "10.21203/rs.3.rs-8138834/v1",
      "authors": [
        "Adrian Krenzer",
        "Patrick Straßer",
        "Tobias Friedetzki",
        "Frank Puppe"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p> <bold>Background</bold> : Self-supervised learning (SSL) has shown strong potential to improve medical image segmentation by leveraging unlabeled data for representation learning. However, most existing SSL methods are designed for 2D natural images and rely heavily on semantic transformations that do not generalize well to volumetric medical imaging. To address this li"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 5 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "point cloud to B-rep reconstruction deep learning",
    "used_override_query": false,
    "fallback_queries": [
      "CAD reconstruction from point clouds",
      "B-rep generation 3D scanning",
      "reverse engineering point cloud to CAD"
    ],
    "executed_queries": [
      "point cloud to B-rep reconstruction deep learning",
      "B-rep reconstruction from 3D scans recent",
      "CAD model recovery from point clouds 2024"
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
      "query": "boundary representation reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-rep CAD model generation from 3D point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "reverse engineering parametric CAD from point cloud deep learning",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'reverse engineering parametric cad from pointcloud deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": "doi:10 1093 jcde qwae005"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ],
      "duplicate_group": "url:http arxiv org abs 2412 14042"
    },
    {
      "title": "NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-12-17",
      "url": "https://doi.org/10.32388/q45a8j",
      "doi": "10.32388/q45a8j",
      "authors": [
        "Ruikai Cui",
        "Shi Qiu",
        "Jiawei Liu",
        "Saeed Anwar",
        "Nick Barnes"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this pa"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Railway reconstruction from 3D point cloud using Deep Learning and Parametric Modeling",
      "source": "Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences",
      "year": 2024,
      "date": "2024-12-14",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",
      "doi": "10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",
      "authors": [
        "Anass Yarroudh",
        "Abderrazzaq Kharroubi",
        "Imane Jeddoub",
        "Zouhair Ballouch",
        "Roland Billen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'reverse engineering parametric cad from pointcloud deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Abstract. Railway infrastructure is crucial for transporting goods and passengers, making its maintenance and reconstruction vital for safety and reliability. Traditional methods reliant on manual surveys are time-consuming and prone to inaccuracies. Although 3D point cloud data provides detailed representations of railway environments, its unstructured nature complicates processing and mo"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"
      ],
      "duplicate_group": ""
    },
    {
      "title": "TreeON: Reconstructing 3D Tree Point Clouds from Orthophotos and Heightmaps",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-11T17:21:12Z",
      "url": "http://arxiv.org/abs/2603.10996v1",
      "doi": "",
      "authors": [
        "Angeliki Grammatikaki",
        "Johannes Eschner",
        "Pedro Hermosilla",
        "Oscar Argudo",
        "Manuela Waldner"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We present TreeON, a novel neural-based framework for reconstructing detailed 3D tree point clouds from sparse top-down geodata, using only a single orthophoto and its corresponding Digital Surface Model (DSM). Our method introduces a new training supervision strategy that combines both geometric supervision and differentiable shadow and silhouette losses to learn point cloud representations of tr"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 13 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "boundary representation reconstruction from point clouds",
    "used_override_query": true,
    "fallback_queries": [
      "CAD reconstruction from 3D point clouds",
      "reverse engineering B-rep from scans",
      "structured CAD model generation point cloud"
    ],
    "executed_queries": [
      "boundary representation reconstruction from point clouds",
      "B-rep CAD model generation from 3D point cloud",
      "reverse engineering parametric CAD from point cloud deep learning"
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
  "review_summary": "The retrieval output contains several promising papers, but fails to meet multiple hard requirements. The relevance of many candidates is questionable based on the provided evidence snippets, which do not clearly confirm the papers address B-rep reconstruction from point clouds as the primary task. The set includes off-topic papers (e.g., medical imaging, general 3D reconstruction), and the evidence quality is insufficient to verify core fit. Source coverage is adequate, but the candidate depth is borderline and the core-method-fit requirement is not satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only a few (e.g., 'Point2CAD', 'CAD-Recode', 'ComplexGen') appear aligned based on titles. However, the evidence snippets for many papers are too vague or clearly off-topic (e.g., 'AI-Powered 3D Reconstruction from 2D Scans' is about medical imaging, 'Optimizing 3D Point Cloud Reconstruction...' is about denoising, 'Puzzles' is about multi-view reconstruction, 'Self-Supervised Kidney Tumor Segmentation' is medical segmentation). The relevance_note is generic and does not confirm the papers fit the specific point-cloud-to-B-rep task."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (last 5 years, primary task is B-rep reconstruction from point clouds) are not reliably reflected. Several papers are out of scope (medical, general point cloud processing, multi-view reconstruction without B-rep output). The time range is respected, but the topical fit is poor."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 papers must be core candidates with non-weak evidence. Only papers like 'Point2CAD', 'CAD-Recode', 'ComplexGen', and 'P2CADNet' have titles suggesting core fit, but their evidence snippets are partial and do not explicitly confirm B-rep as the final output from point clouds. The verification_status is 'partial' and evidence_level is 'abstract', but the snippets are truncated and lack conclusive statements. Papers marked as core_candidate=true (e.g., 'Optimizing 3D Point Cloud Reconstruction...', 'Puzzles') appear to be incorrectly labeled based on their evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious over-reliance on arXiv and a lack of papers from key conferences (e.g., SIGGRAPH, CVPR, ICCV, CAD). The retrieval seems to have captured many papers with only tangential keyword overlap, missing a focused set on the core problem. The evidence snippets are insufficient to assess the true contribution of each paper."
    }
  },
  "key_risks": ["High risk of including irrelevant papers due to vague evidence snippets.", "Potential missing of seminal works from top-tier vision/graphics conferences.", "Retrieval may have been overly broad, capturing papers about general CAD generation or point cloud processing rather than the specific B-rep reconstruction task."],
  "next_actions": ["Execute a revised, more precise search query focusing on 'boundary representation reconstruction from point clouds' and filter for conferences like SIGGRAPH, CVPR, ICCV, SPM, and CAD.", "For each candidate paper, retrieve full abstracts or key sentences to verify that the primary task is indeed B-rep reconstruction from point clouds, not a subproblem or different representation.", "Explicitly exclude papers where the input is not a point cloud (e.g., images, 2D sketches) or the output is not a B-rep (e.g., mesh, SDF, CSG)."]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows improved focus but still contains several papers that are not core to the specific point-cloud-to-B-rep reconstruction task. While some candidates like 'Point2Brep' and 'CAD-Recode' appear highly relevant, others are about surface reconstruction ('NumGrad-Pull'), domain-specific applications ('Railway reconstruction'), or are datasets/annotation pipelines ('A parametric and feature-based CAD dataset', 'From CAD Models to Soft Point Cloud Labels'). The evidence snippets remain partial and do not conclusively verify that B-rep is the final output for all core candidates. The set lacks sufficient depth of verified, in-scope papers from top-tier conferences.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only a subset ('Point2Brep', 'CAD-Recode', 'Brep2Seq', 'Research on Reverse Modeling...') appear aligned. Others are clearly off-topic: 'NumGrad-Pull' is about surface reconstruction (likely mesh/SDF), 'Railway reconstruction' is a domain-specific application without confirmed B-rep output, 'TreeON' reconstructs tree point clouds, 'Surface and Edge Detection' is a subproblem (primitive fitting), and 'From CAD Models to Soft Point Cloud Labels' is about annotation for segmentation. The relevance_note is still generic and does not filter out these mismatches."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (B-rep as final output from point clouds) are not fully met. Several papers do not have evidence confirming B-rep output; some are about intermediate steps ('Surface and Edge Detection'), specific applications, or different reconstruction targets (point clouds, surfaces). The exclusion areas (mesh reconstruction, intermediate representations) are violated by some candidates."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 papers must be core candidates with non-weak evidence. While 'Point2Brep', 'CAD-Recode', and 'Brep2Seq' have promising titles and snippets, the evidence snippets are truncated and do not explicitly state that B-rep is the final output from point clouds. For example, 'Brep2Seq' snippet mentions recovering editable CAD models from various inputs including point clouds, but does not confirm the primary task is reconstruction from point clouds. 'Research on Reverse Modeling...' mentions parametric CAD from point clouds, which is closer. Other papers marked as core_candidate=true (e.g., 'NumGrad-Pull', 'Railway reconstruction', 'TreeON') are not core to the B-rep reconstruction problem. The verification_status is 'partial' but the evidence is insufficient to confirm core fit."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is still a significant gap in papers from premier computer vision/graphics conferences (SIGGRAPH, CVPR, ICCV, etc.). The set is mixed with lower-tier or application-specific venues. The evidence snippets are too brief to assess the methodological contribution and final output representation. An over-reliance on arXiv and Crossref preprints persists."
    }
  },
  "key_risks": ["Inclusion of papers that address surface or mesh reconstruction rather than B-rep.", "Risk of missing seminal works due to venue bias.", "Evidence snippets are not conclusive, leading to potential misclassification of core papers."],
  "next_actions": ["For each promising candidate (e.g., 'Point2Brep', 'CAD-Recode', 'Brep2Seq', 'Research on Reverse Modeling...'), retrieve the full abstract or introduction to explicitly verify that the input is a point cloud and the output is a B-rep/editable CAD model.", "Execute a targeted search on top-tier conference venues using queries like '\"B-rep\" \"point cloud\" reconstruction SIGGRAPH' or '\"boundary representation\" \"point cloud\" CAD CVPR' to capture high-impact papers.", "Explicitly filter out papers where the title or abstract mentions 'surface reconstruction', 'mesh', 'SDF', 'neural rendering', or domain-specific applications (e.g., railways, trees) unless they explicitly state B-rep output."]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_wNxygtBTLAcQZdtkG6eBcLuL', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-rep reconstruction from 3D scans recent",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model recovery from point clouds 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models",\n      "source": "Crossref / Electronics",\n      "year": 2025,\n      "date": "2025-1-20",\n      "url": "https://doi.org/10.3390/electronics14020399",\n      "doi": "10.3390/electronics14020399",\n      "authors": [\n        "Seyyedbehrad Emadi",\n        "Marco Limongiello"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "AI-Powered 3D Reconstruction from 2D Scans",\n      "source": "Crossref / International Journal of Humanities and Information Technology",\n      "year": 2024,\n      "date": "2024-6-28",\n      "url": "https://doi.org/10.21590/ijhit.06.02.4",\n      "doi": "10.21590/ijhit.06.02.4",\n      "authors": [\n        "Arjun Deshraje Urs"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Artificial intelligence (AI) is reshaping how medical images are interpreted and used in practice. Traditionally, clinicians rely on 2D radiological slices such as CT and MRI to infer 3D anatomical structures, a process that is mentally demanding and often variable between observers. With AI, these 2D slices can now be transformed into detailed, interactive 3D models in real time. Such mod"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Puzzles: Unbounded Video-Depth Augmentation for Scalable End-to-End 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-06-30T13:57:24Z",\n      "url": "http://arxiv.org/abs/2506.23863v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Ma",\n        "Lei Wang",\n        "Miaomiao liu",\n        "David Ahmedt-Aristizabal",\n        "Chuong Nguyen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Multi-view 3D reconstruction remains a core challenge in computer vision. Recent methods, such as DUST3R and its successors, directly regress pointmaps from image pairs without relying on known scene geometry or camera parameters. However, the performance of these models is constrained by the diversity and scale of available training data. In this work, we introduce Puzzles, a data augmentation st"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-07T08:23:44Z",\n      "url": "http://arxiv.org/abs/2312.04962v1",\n      "doi": "",\n      "authors": [\n        "Yujia Liu",\n        "Anton Obukhov",\n        "Jan Dirk Wegner",\n        "Konrad Schindler"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Self-Supervised Kidney Tumor Segmentation Using Random Block Reconstruction on 3D CT Scans",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026-2-11",\n      "url": "https://doi.org/10.21203/rs.3.rs-8138834/v1",\n      "doi": "10.21203/rs.3.rs-8138834/v1",\n      "authors": [\n        "Adrian Krenzer",\n        "Patrick Straßer",\n        "Tobias Friedetzki",\n        "Frank Puppe"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p> <bold>Background</bold> : Self-supervised learning (SSL) has shown strong potential to improve medical image segmentation by leveraging unlabeled data for representation learning. However, most existing SSL methods are designed for 2D natural images and rely heavily on semantic transformations that do not generalize well to volumetric medical imaging. To address this li"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 5 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "point cloud to B-rep reconstruction deep learning",\n    "used_override_query": false,\n    "fallback_queries": [\n      "CAD reconstruction from point clouds",\n      "B-rep generation 3D scanning",\n      "reverse engineering point cloud to CAD"\n    ],\n    "executed_queries": [\n      "point cloud to B-rep reconstruction deep learning",\n      "B-rep reconstruction from 3D scans recent",\n      "CAD model recovery from point clouds 2024"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_wNxygtBTLAcQZdtkG6eBcLuL' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_HSiPIu3VNdXKfVFiY5V3udt5', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "boundary representation reconstruction from point clouds"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "boundary representation reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-rep CAD model generation from 3D point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "reverse engineering parametric CAD from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'reverse engineering parametric cad from pointcloud deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ],\n      "duplicate_group": "url:http arxiv org abs 2412 14042"\n    },\n    {\n      "title": "NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-12-17",\n      "url": "https://doi.org/10.32388/q45a8j",\n      "doi": "10.32388/q45a8j",\n      "authors": [\n        "Ruikai Cui",\n        "Shi Qiu",\n        "Jiawei Liu",\n        "Saeed Anwar",\n        "Nick Barnes"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this pa"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Railway reconstruction from 3D point cloud using Deep Learning and Parametric Modeling",\n      "source": "Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences",\n      "year": 2024,\n      "date": "2024-12-14",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",\n      "doi": "10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",\n      "authors": [\n        "Anass Yarroudh",\n        "Abderrazzaq Kharroubi",\n        "Imane Jeddoub",\n        "Zouhair Ballouch",\n        "Roland Billen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'reverse engineering parametric cad from pointcloud deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Abstract. Railway infrastructure is crucial for transporting goods and passengers, making its maintenance and reconstruction vital for safety and reliability. Traditional methods reliant on manual surveys are time-consuming and prone to inaccuracies. Although 3D point cloud data provides detailed representations of railway environments, its unstructured nature complicates processing and mo"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "TreeON: Reconstructing 3D Tree Point Clouds from Orthophotos and Heightmaps",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-11T17:21:12Z",\n      "url": "http://arxiv.org/abs/2603.10996v1",\n      "doi": "",\n      "authors": [\n        "Angeliki Grammatikaki",\n        "Johannes Eschner",\n        "Pedro Hermosilla",\n        "Oscar Argudo",\n        "Manuela Waldner"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We present TreeON, a novel neural-based framework for reconstructing detailed 3D tree point clouds from sparse top-down geodata, using only a single orthophoto and its corresponding Digital Surface Model (DSM). Our method introduces a new training supervision strategy that combines both geometric supervision and differentiable shadow and silhouette losses to learn point cloud representations of tr"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 13 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "boundary representation reconstruction from point clouds",\n    "used_override_query": true,\n    "fallback_queries": [\n      "CAD reconstruction from 3D point clouds",\n      "reverse engineering B-rep from scans",\n      "structured CAD model generation point cloud"\n    ],\n    "executed_queries": [\n      "boundary representation reconstruction from point clouds",\n      "B-rep CAD model generation from 3D point cloud",\n      "reverse engineering parametric CAD from point cloud deep learning"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_HSiPIu3VNdXKfVFiY5V3udt5' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

```text
Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus on papers where the primary task is to take point clouds as input and reconstruct B-rep as the final output representation.

Prioritize papers whose main contribution is the full B-rep reconstruction problem itself, rather than only a subproblem, intermediate representation, auxiliary module, downstream application, or a different reconstruction/CAD task.

A paper should be treated as a core candidate only if reconstructing B-rep from point clouds is the paper's primary task and B-rep is the final target output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it truly fits the point-cloud-to-B-rep reconstruction task

Then summarize:
- major method categories
- recent trends
- open challenges

Be selective, but avoid over-filtering papers merely because the method is multi-stage or uses intermediate steps within the reconstruction pipeline.

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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is reconstructing B-rep representations directly from point clouds as the final output, focusing on core methods for the full problem rather than subproblems or auxiliary modules.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["point cloud to B-rep reconstruction", "boundary representation reconstruction", "CAD from 3D scans", "geometric deep learning for B-rep generation", "structured CAD model recovery"],
  "exclude_areas": ["mesh reconstruction only", "surface fitting without topological structure", "intermediate representation learning (e.g., CSG, SDF) not outputting B-rep", "downstream applications like segmentation or classification", "B-rep reconstruction from other inputs (e.g., images, sketches)"],
  "fallback_queries": ["CAD reconstruction from point clouds", "B-rep generation 3D scanning", "reverse engineering point cloud to CAD"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction deep learning",
      "reason": "Targets modern learning-based methods that directly output B-rep structures from point cloud input."
    },
    {
      "query": "B-rep reconstruction from 3D scans recent",
      "reason": "Captures reverse engineering and scanning-focused literature that may not explicitly use 'point cloud' in the title."
    },
    {
      "query": "CAD model recovery from point clouds 2024",
      "reason": "Focuses on the CAD reconstruction task, which often implies B-rep as the target representation in recent research."
    }
  ],
  "assumptions": ["The term 'B-rep' in recent literature may be interchanged with 'CAD model', 'boundary representation', or 'structured CAD'.", "Some papers may present multi-stage pipelines where B-rep is the final output; these are included if the primary task is full reconstruction.", "Conference venues likely include SIGGRAPH, CVPR, ICCV, CAD, and SPM."],
  "success_criteria": ["Retrieve 5-10 papers where the abstract or contribution explicitly states B-rep reconstruction from point clouds as the primary goal.", "Papers should present a complete method or framework yielding a B-rep model.", "Exclude papers where B-rep is only an intermediate step or not the final output."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find relevant papers on B-rep reconstruction from point clouds within the 2022-2026 timeframe.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_wNxygtBTLAcQZdtkG6eBcLuL', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-rep reconstruction from 3D scans recent",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model recovery from point clouds 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models",\n      "source": "Crossref / Electronics",\n      "year": 2025,\n      "date": "2025-1-20",\n      "url": "https://doi.org/10.3390/electronics14020399",\n      "doi": "10.3390/electronics14020399",\n      "authors": [\n        "Seyyedbehrad Emadi",\n        "Marco Limongiello"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "AI-Powered 3D Reconstruction from 2D Scans",\n      "source": "Crossref / International Journal of Humanities and Information Technology",\n      "year": 2024,\n      "date": "2024-6-28",\n      "url": "https://doi.org/10.21590/ijhit.06.02.4",\n      "doi": "10.21590/ijhit.06.02.4",\n      "authors": [\n        "Arjun Deshraje Urs"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Artificial intelligence (AI) is reshaping how medical images are interpreted and used in practice. Traditionally, clinicians rely on 2D radiological slices such as CT and MRI to infer 3D anatomical structures, a process that is mentally demanding and often variable between observers. With AI, these 2D slices can now be transformed into detailed, interactive 3D models in real time. Such mod"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Puzzles: Unbounded Video-Depth Augmentation for Scalable End-to-End 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-06-30T13:57:24Z",\n      "url": "http://arxiv.org/abs/2506.23863v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Ma",\n        "Lei Wang",\n        "Miaomiao liu",\n        "David Ahmedt-Aristizabal",\n        "Chuong Nguyen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Multi-view 3D reconstruction remains a core challenge in computer vision. Recent methods, such as DUST3R and its successors, directly regress pointmaps from image pairs without relying on known scene geometry or camera parameters. However, the performance of these models is constrained by the diversity and scale of available training data. In this work, we introduce Puzzles, a data augmentation st"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-07T08:23:44Z",\n      "url": "http://arxiv.org/abs/2312.04962v1",\n      "doi": "",\n      "authors": [\n        "Yujia Liu",\n        "Anton Obukhov",\n        "Jan Dirk Wegner",\n        "Konrad Schindler"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'cad model recovery from pointclouds 2024\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Self-Supervised Kidney Tumor Segmentation Using Random Block Reconstruction on 3D CT Scans",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026-2-11",\n      "url": "https://doi.org/10.21203/rs.3.rs-8138834/v1",\n      "doi": "10.21203/rs.3.rs-8138834/v1",\n      "authors": [\n        "Adrian Krenzer",\n        "Patrick Straßer",\n        "Tobias Friedetzki",\n        "Frank Puppe"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from 3d scans recent\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p> <bold>Background</bold> : Self-supervised learning (SSL) has shown strong potential to improve medical image segmentation by leveraging unlabeled data for representation learning. However, most existing SSL methods are designed for 2D natural images and rely heavily on semantic transformations that do not generalize well to volumetric medical imaging. To address this li"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 5 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "point cloud to B-rep reconstruction deep learning",\n    "used_override_query": false,\n    "fallback_queries": [\n      "CAD reconstruction from point clouds",\n      "B-rep generation 3D scanning",\n      "reverse engineering point cloud to CAD"\n    ],\n    "executed_queries": [\n      "point cloud to B-rep reconstruction deep learning",\n      "B-rep reconstruction from 3D scans recent",\n      "CAD model recovery from point clouds 2024"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_wNxygtBTLAcQZdtkG6eBcLuL' is_error=False
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
      "query": "point cloud to B-rep reconstruction deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-rep reconstruction from 3D scans recent",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model recovery from point clouds 2024",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models",
      "source": "Crossref / Electronics",
      "year": 2025,
      "date": "2025-1-20",
      "url": "https://doi.org/10.3390/electronics14020399",
      "doi": "10.3390/electronics14020399",
      "authors": [
        "Seyyedbehrad Emadi",
        "Marco Limongiello"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ],
      "duplicate_group": ""
    },
    {
      "title": "AI-Powered 3D Reconstruction from 2D Scans",
      "source": "Crossref / International Journal of Humanities and Information Technology",
      "year": 2024,
      "date": "2024-6-28",
      "url": "https://doi.org/10.21590/ijhit.06.02.4",
      "doi": "10.21590/ijhit.06.02.4",
      "authors": [
        "Arjun Deshraje Urs"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Artificial intelligence (AI) is reshaping how medical images are interpreted and used in practice. Traditionally, clinicians rely on 2D radiological slices such as CT and MRI to infer 3D anatomical structures, a process that is mentally demanding and often variable between observers. With AI, these 2D slices can now be transformed into detailed, interactive 3D models in real time. Such mod"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within t"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Puzzles: Unbounded Video-Depth Augmentation for Scalable End-to-End 3D Reconstruction",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-06-30T13:57:24Z",
      "url": "http://arxiv.org/abs/2506.23863v1",
      "doi": "",
      "authors": [
        "Jiahao Ma",
        "Lei Wang",
        "Miaomiao liu",
        "David Ahmedt-Aristizabal",
        "Chuong Nguyen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Multi-view 3D reconstruction remains a core challenge in computer vision. Recent methods, such as DUST3R and its successors, directly regress pointmaps from image pairs without relying on known scene geometry or camera parameters. However, the performance of these models is constrained by the diversity and scale of available training data. In this work, we introduce Puzzles, a data augmentation st"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'cad model recovery from pointclouds 2024'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) model reconstruction from point clouds is an important problem at the intersection of computer vision, graphics, and machine learning; it saves the designer significant time when iterating on in-the-wild objects. Recent advancements in this direction achieve relatively reliable semantic segmentation but still struggle to produce an adequate topology of the CAD model. In"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Self-Supervised Kidney Tumor Segmentation Using Random Block Reconstruction on 3D CT Scans",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026-2-11",
      "url": "https://doi.org/10.21203/rs.3.rs-8138834/v1",
      "doi": "10.21203/rs.3.rs-8138834/v1",
      "authors": [
        "Adrian Krenzer",
        "Patrick Straßer",
        "Tobias Friedetzki",
        "Frank Puppe"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from 3d scans recent'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p> <bold>Background</bold> : Self-supervised learning (SSL) has shown strong potential to improve medical image segmentation by leveraging unlabeled data for representation learning. However, most existing SSL methods are designed for 2D natural images and rely heavily on semantic transformations that do not generalize well to volumetric medical imaging. To address this li"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 5 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "point cloud to B-rep reconstruction deep learning",
    "used_override_query": false,
    "fallback_queries": [
      "CAD reconstruction from point clouds",
      "B-rep generation 3D scanning",
      "reverse engineering point cloud to CAD"
    ],
    "executed_queries": [
      "point cloud to B-rep reconstruction deep learning",
      "B-rep reconstruction from 3D scans recent",
      "CAD model recovery from point clouds 2024"
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
  "review_summary": "The retrieval output contains several promising papers, but fails to meet multiple hard requirements. The relevance of many candidates is questionable based on the provided evidence snippets, which do not clearly confirm the papers address B-rep reconstruction from point clouds as the primary task. The set includes off-topic papers (e.g., medical imaging, general 3D reconstruction), and the evidence quality is insufficient to verify core fit. Source coverage is adequate, but the candidate depth is borderline and the core-method-fit requirement is not satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only a few (e.g., 'Point2CAD', 'CAD-Recode', 'ComplexGen') appear aligned based on titles. However, the evidence snippets for many papers are too vague or clearly off-topic (e.g., 'AI-Powered 3D Reconstruction from 2D Scans' is about medical imaging, 'Optimizing 3D Point Cloud Reconstruction...' is about denoising, 'Puzzles' is about multi-view reconstruction, 'Self-Supervised Kidney Tumor Segmentation' is medical segmentation). The relevance_note is generic and does not confirm the papers fit the specific point-cloud-to-B-rep task."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (last 5 years, primary task is B-rep reconstruction from point clouds) are not reliably reflected. Several papers are out of scope (medical, general point cloud processing, multi-view reconstruction without B-rep output). The time range is respected, but the topical fit is poor."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 papers must be core candidates with non-weak evidence. Only papers like 'Point2CAD', 'CAD-Recode', 'ComplexGen', and 'P2CADNet' have titles suggesting core fit, but their evidence snippets are partial and do not explicitly confirm B-rep as the final output from point clouds. The verification_status is 'partial' and evidence_level is 'abstract', but the snippets are truncated and lack conclusive statements. Papers marked as core_candidate=true (e.g., 'Optimizing 3D Point Cloud Reconstruction...', 'Puzzles') appear to be incorrectly labeled based on their evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious over-reliance on arXiv and a lack of papers from key conferences (e.g., SIGGRAPH, CVPR, ICCV, CAD). The retrieval seems to have captured many papers with only tangential keyword overlap, missing a focused set on the core problem. The evidence snippets are insufficient to assess the true contribution of each paper."
    }
  },
  "key_risks": ["High risk of including irrelevant papers due to vague evidence snippets.", "Potential missing of seminal works from top-tier vision/graphics conferences.", "Retrieval may have been overly broad, capturing papers about general CAD generation or point cloud processing rather than the specific B-rep reconstruction task."],
  "next_actions": ["Execute a revised, more precise search query focusing on 'boundary representation reconstruction from point clouds' and filter for conferences like SIGGRAPH, CVPR, ICCV, SPM, and CAD.", "For each candidate paper, retrieve full abstracts or key sentences to verify that the primary task is indeed B-rep reconstruction from point clouds, not a subproblem or different representation.", "Explicitly exclude papers where the input is not a point cloud (e.g., images, 2D sketches) or the output is not a B-rep (e.g., mesh, SDF, CSG)."]
}
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3, years=2022-2026

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) where the primary task is reconstructing B-rep representations directly from point clouds as the final output, focusing on core methods for the full problem rather than subproblems or auxiliary modules.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["point cloud to B-rep reconstruction", "boundary representation reconstruction", "CAD from 3D scans", "geometric deep learning for B-rep generation", "structured CAD model recovery", "reverse engineering CAD from point clouds"],
  "exclude_areas": ["mesh reconstruction only", "surface fitting without topological structure", "intermediate representation learning (e.g., CSG, SDF) not outputting B-rep", "downstream applications like segmentation or classification", "B-rep reconstruction from other inputs (e.g., images, sketches)", "medical imaging reconstruction", "point cloud denoising or upsampling", "general multi-view 3D reconstruction"],
  "fallback_queries": ["CAD reconstruction from 3D point clouds", "reverse engineering B-rep from scans", "structured CAD model generation point cloud"],
  "queries": [
    {
      "query": "boundary representation reconstruction from point clouds",
      "reason": "Directly targets the core task using precise terminology to filter out irrelevant works on meshes or other representations."
    },
    {
      "query": "B-rep CAD model generation from 3D point cloud",
      "reason": "Focuses on the generative aspect and CAD context, likely to capture recent learning-based methods in top venues."
    },
    {
      "query": "reverse engineering parametric CAD from point cloud deep learning",
      "reason": "Emphasizes the reverse engineering pipeline and parametric CAD, which inherently involves B-rep output."
    }
  ],
  "assumptions": ["Key venues include SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, ECCV, CAD, and SPM.", "A paper's primary contribution is considered 'core' if the abstract explicitly states reconstruction of a B-rep or editable CAD model from a point cloud.", "Multi-stage pipelines are included if B-rep is the final, explicit output."],
  "success_criteria": ["Retrieve 5-10 papers where the abstract confirms point cloud input and B-rep/CAD model output as the main goal.", "Exclude papers focused solely on segmentation, feature detection, or intermediate representations without final B-rep reconstruction.", "Ensure evidence snippets explicitly mention 'B-rep', 'boundary representation', 'editable CAD model', or 'parametric CAD' from point clouds."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the revised search plan with more precise queries to find papers that truly focus on B-rep reconstruction from point clouds.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_HSiPIu3VNdXKfVFiY5V3udt5', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "boundary representation reconstruction from point clouds"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "boundary representation reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-rep CAD model generation from 3D point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "reverse engineering parametric CAD from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds",\n      "source": "Crossref / Journal of Electronic Research and Application",\n      "year": 2025,\n      "date": "2025-12-16",\n      "url": "https://doi.org/10.26689/jera.v9i6.13185",\n      "doi": "10.26689/jera.v9i6.13185",\n      "authors": [\n        "Yangzhi Zhang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'reverse engineering parametric cad from pointcloud deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-Recode: Reverse Engineering CAD Code from Point Clouds",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-12-18T16:55:42Z",\n      "url": "http://arxiv.org/abs/2412.14042v2",\n      "doi": "",\n      "authors": [\n        "Danila Rukhovich",\n        "Elona Dupont",\n        "Dimitrios Mallis",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"\n      ],\n      "duplicate_group": "url:http arxiv org abs 2412 14042"\n    },\n    {\n      "title": "NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-12-17",\n      "url": "https://doi.org/10.32388/q45a8j",\n      "doi": "10.32388/q45a8j",\n      "authors": [\n        "Ruikai Cui",\n        "Shi Qiu",\n        "Jiawei Liu",\n        "Saeed Anwar",\n        "Nick Barnes"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this pa"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Railway reconstruction from 3D point cloud using Deep Learning and Parametric Modeling",\n      "source": "Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences",\n      "year": 2024,\n      "date": "2024-12-14",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",\n      "doi": "10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",\n      "authors": [\n        "Anass Yarroudh",\n        "Abderrazzaq Kharroubi",\n        "Imane Jeddoub",\n        "Zouhair Ballouch",\n        "Roland Billen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'reverse engineering parametric cad from pointcloud deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Abstract. Railway infrastructure is crucial for transporting goods and passengers, making its maintenance and reconstruction vital for safety and reliability. Traditional methods reliant on manual surveys are time-consuming and prone to inaccuracies. Although 3D point cloud data provides detailed representations of railway environments, its unstructured nature complicates processing and mo"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "TreeON: Reconstructing 3D Tree Point Clouds from Orthophotos and Heightmaps",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-11T17:21:12Z",\n      "url": "http://arxiv.org/abs/2603.10996v1",\n      "doi": "",\n      "authors": [\n        "Angeliki Grammatikaki",\n        "Johannes Eschner",\n        "Pedro Hermosilla",\n        "Oscar Argudo",\n        "Manuela Waldner"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We present TreeON, a novel neural-based framework for reconstructing detailed 3D tree point clouds from sparse top-down geodata, using only a single orthophoto and its corresponding Digital Surface Model (DSM). Our method introduces a new training supervision strategy that combines both geometric supervision and differentiable shadow and silhouette losses to learn point cloud representations of tr"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep cad model generation from 3d pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 13 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "boundary representation reconstruction from point clouds",\n    "used_override_query": true,\n    "fallback_queries": [\n      "CAD reconstruction from 3D point clouds",\n      "reverse engineering B-rep from scans",\n      "structured CAD model generation point cloud"\n    ],\n    "executed_queries": [\n      "boundary representation reconstruction from point clouds",\n      "B-rep CAD model generation from 3D point cloud",\n      "reverse engineering parametric CAD from point cloud deep learning"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_HSiPIu3VNdXKfVFiY5V3udt5' is_error=False
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
      "query": "boundary representation reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-rep CAD model generation from 3D point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "reverse engineering parametric CAD from point cloud deep learning",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'reverse engineering parametric cad from pointcloud deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Existing reverse-engineering methods struggle to directly generate editable, parametric CAD models from scanned data. To address this limitation, this paper proposes a reverse-modeling approach that reconstructs parametric CAD models from multi-view RGB-D point clouds. Multi-frame point-cloud registration and fusion are first employed to obtain a complete 3-D point cloud of the target obje"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": "doi:10 1093 jcde qwae005"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) models are typically constructed by sequentially drawing parametric sketches and applying CAD operations to obtain a 3D model. The problem of 3D CAD reverse engineering consists of reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds. In this paper, we address this challenge through novel contributions across three levels: C"
      ],
      "duplicate_group": "url:http arxiv org abs 2412 14042"
    },
    {
      "title": "NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-12-17",
      "url": "https://doi.org/10.32388/q45a8j",
      "doi": "10.32388/q45a8j",
      "authors": [
        "Ruikai Cui",
        "Shi Qiu",
        "Jiawei Liu",
        "Saeed Anwar",
        "Nick Barnes"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this pa"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Railway reconstruction from 3D point cloud using Deep Learning and Parametric Modeling",
      "source": "Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences",
      "year": 2024,
      "date": "2024-12-14",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",
      "doi": "10.5194/isprs-archives-xlviii-2-w8-2024-477-2024",
      "authors": [
        "Anass Yarroudh",
        "Abderrazzaq Kharroubi",
        "Imane Jeddoub",
        "Zouhair Ballouch",
        "Roland Billen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'reverse engineering parametric cad from pointcloud deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Abstract. Railway infrastructure is crucial for transporting goods and passengers, making its maintenance and reconstruction vital for safety and reliability. Traditional methods reliant on manual surveys are time-consuming and prone to inaccuracies. Although 3D point cloud data provides detailed representations of railway environments, its unstructured nature complicates processing and mo"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"
      ],
      "duplicate_group": ""
    },
    {
      "title": "TreeON: Reconstructing 3D Tree Point Clouds from Orthophotos and Heightmaps",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-11T17:21:12Z",
      "url": "http://arxiv.org/abs/2603.10996v1",
      "doi": "",
      "authors": [
        "Angeliki Grammatikaki",
        "Johannes Eschner",
        "Pedro Hermosilla",
        "Oscar Argudo",
        "Manuela Waldner"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We present TreeON, a novel neural-based framework for reconstructing detailed 3D tree point clouds from sparse top-down geodata, using only a single orthophoto and its corresponding Digital Surface Model (DSM). Our method introduces a new training supervision strategy that combines both geometric supervision and differentiable shadow and silhouette losses to learn point cloud representations of tr"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep cad model generation from 3d pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 13 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "boundary representation reconstruction from point clouds",
    "used_override_query": true,
    "fallback_queries": [
      "CAD reconstruction from 3D point clouds",
      "reverse engineering B-rep from scans",
      "structured CAD model generation point cloud"
    ],
    "executed_queries": [
      "boundary representation reconstruction from point clouds",
      "B-rep CAD model generation from 3D point cloud",
      "reverse engineering parametric CAD from point cloud deep learning"
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
  "review_summary": "The retrieval output shows improved focus but still contains several papers that are not core to the specific point-cloud-to-B-rep reconstruction task. While some candidates like 'Point2Brep' and 'CAD-Recode' appear highly relevant, others are about surface reconstruction ('NumGrad-Pull'), domain-specific applications ('Railway reconstruction'), or are datasets/annotation pipelines ('A parametric and feature-based CAD dataset', 'From CAD Models to Soft Point Cloud Labels'). The evidence snippets remain partial and do not conclusively verify that B-rep is the final output for all core candidates. The set lacks sufficient depth of verified, in-scope papers from top-tier conferences.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, and arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers are listed."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only a subset ('Point2Brep', 'CAD-Recode', 'Brep2Seq', 'Research on Reverse Modeling...') appear aligned. Others are clearly off-topic: 'NumGrad-Pull' is about surface reconstruction (likely mesh/SDF), 'Railway reconstruction' is a domain-specific application without confirmed B-rep output, 'TreeON' reconstructs tree point clouds, 'Surface and Edge Detection' is a subproblem (primitive fitting), and 'From CAD Models to Soft Point Cloud Labels' is about annotation for segmentation. The relevance_note is still generic and does not filter out these mismatches."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (B-rep as final output from point clouds) are not fully met. Several papers do not have evidence confirming B-rep output; some are about intermediate steps ('Surface and Edge Detection'), specific applications, or different reconstruction targets (point clouds, surfaces). The exclusion areas (mesh reconstruction, intermediate representations) are violated by some candidates."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 papers must be core candidates with non-weak evidence. While 'Point2Brep', 'CAD-Recode', and 'Brep2Seq' have promising titles and snippets, the evidence snippets are truncated and do not explicitly state that B-rep is the final output from point clouds. For example, 'Brep2Seq' snippet mentions recovering editable CAD models from various inputs including point clouds, but does not confirm the primary task is reconstruction from point clouds. 'Research on Reverse Modeling...' mentions parametric CAD from point clouds, which is closer. Other papers marked as core_candidate=true (e.g., 'NumGrad-Pull', 'Railway reconstruction', 'TreeON') are not core to the B-rep reconstruction problem. The verification_status is 'partial' but the evidence is insufficient to confirm core fit."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is still a significant gap in papers from premier computer vision/graphics conferences (SIGGRAPH, CVPR, ICCV, etc.). The set is mixed with lower-tier or application-specific venues. The evidence snippets are too brief to assess the methodological contribution and final output representation. An over-reliance on arXiv and Crossref preprints persists."
    }
  },
  "key_risks": ["Inclusion of papers that address surface or mesh reconstruction rather than B-rep.", "Risk of missing seminal works due to venue bias.", "Evidence snippets are not conclusive, leading to potential misclassification of core papers."],
  "next_actions": ["For each promising candidate (e.g., 'Point2Brep', 'CAD-Recode', 'Brep2Seq', 'Research on Reverse Modeling...'), retrieve the full abstract or introduction to explicitly verify that the input is a point cloud and the output is a B-rep/editable CAD model.", "Execute a targeted search on top-tier conference venues using queries like '\"B-rep\" \"point cloud\" reconstruction SIGGRAPH' or '\"boundary representation\" \"point cloud\" CAD CVPR' to capture high-impact papers.", "Explicitly filter out papers where the title or abstract mentions 'surface reconstruction', 'mesh', 'SDF', 'neural rendering', or domain-specific applications (e.g., railways, trees) unless they explicitly state B-rep output."]
}
```

### Message 14

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal is to identify frontier research (2022–2026) where the **primary task** is reconstructing Boundary Representation (B-rep) models directly from point clouds as the final output. The focus is on core methods for the full reconstruction problem, not subproblems (e.g., segmentation, primitive fitting) or auxiliary modules. Outputs like meshes, SDFs, or CSG without a final B-rep are excluded.

## Search Strategy
The search was conducted in two phases:
1.  **Initial broad search** using queries like "point cloud to B-rep reconstruction deep learning" and "CAD model recovery from point clouds". This returned many tangential results (e.g., medical imaging, point cloud denoising).
2.  **Refined, precise search** using targeted queries like "boundary representation reconstruction from point clouds" and "reverse engineering parametric CAD from point cloud". This improved focus but still captured papers on surface reconstruction, domain-specific applications, and datasets that do not meet the core criteria.

Searches were performed across Crossref, OpenAlex, and arXiv. A key gap was the lack of papers from premier computer vision/graphics conferences (e.g., SIGGRAPH, CVPR), indicating the niche nature of the problem or a potential retrieval bias.

## Candidate Papers
The search did not clear the quality bar. No papers were fully verified to meet all hard requirements (point cloud input, B-rep output as primary task, within top-tier venues). The results are split into partially verified candidates and unverified leads.

### Verified Candidates
*Papers with evidence suggesting relevance, but verification is incomplete.*

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Evidence:** Abstract snippet states it "reconstructs complete and topologically consistent B-rep models" and is a "geometry-aware framework." Strong title match.
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2412.14042v2
    *   **Evidence:** Abstract explicitly frames the problem as "reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds," which implies a parametric CAD/B-rep output.
*   **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** OpenAlex / Journal of Computational Design and Engineering
    *   **Link:** https://doi.org/10.1093/jcde/qwae005
    *   **Evidence:** Abstract mentions recovering "editable CAD models" from inputs including "point clouds" and "boundary representations (B-rep)." The role of point clouds as input versus other representations is unclear from the snippet.
*   **Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds** (2025)
    *   **Source:** Journal of Electronic Research and Application
    *   **Link:** https://doi.org/10.26689/jera.v9i6.13185
    *   **Evidence:** Abstract states the goal is to "reconstructs parametric CAD models from multi-view RGB-D point clouds." Directly addresses the target task.

### Unverified Leads
*Title-strong papers that require follow-up verification but are not recommendations.*

1.  **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022, arXiv): Title suggests B-rep reconstruction, but the abstract snippet does not confirm point cloud as the primary input.
2.  **Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds** (2023, arXiv): Title is a direct match, but the abstract snippet discusses topology challenges without explicitly confirming B-rep as the final output format.
3.  **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023, arXiv): Title indicates a parametric CAD output from point clouds, aligning with the goal.

## Notes and Gaps
*   **Evidence Quality:** Most retrieved papers have only partial abstract snippets, making it impossible to conclusively verify that B-rep reconstruction from point clouds is the *primary* task and final output.
*   **Venue Gap:** The search did not surface papers from top-tier computer vision/graphics conferences (e.g., SIGGRAPH, CVPR, ICCV), which are likely venues for frontier research on this topic.
*   **Scope Creep:** Many retrieved papers were off-topic, focusing on:
    *   General surface or mesh reconstruction (e.g., NumGrad-Pull).
    *   Domain-specific applications without confirmed B-rep output (e.g., Railway reconstruction, TreeON).
    *   Subproblems like primitive fitting or edge detection (e.g., Surface and Edge Detection for Primitive Fitting).
    *   Dataset creation or annotation pipelines.

## Recommended Next Steps
1.  **Manual Verification:** For the strongest leads (e.g., Point2Brep, CAD-Recode, Point2CAD), retrieve and read the full paper to confirm the input (point cloud) and output (B-rep/editable CAD model).
2.  **Targeted Venue Search:** Conduct a manual or advanced search within the proceedings of key conferences (SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, SPM) using terms like `"B-rep"`, `"boundary representation"`, `"CAD reconstruction"`, and `"point cloud"`.
3.  **Citation Tracking:** Use the verified papers (if any) as seeds for backward and forward citation analysis to find related core research.
4.  **Broaden Terminology:** Consider that some relevant work may be framed as "reverse engineering of CAD models" or "structured CAD generation" without explicitly using "B-rep" in the title or abstract.

TERMINATE
```
