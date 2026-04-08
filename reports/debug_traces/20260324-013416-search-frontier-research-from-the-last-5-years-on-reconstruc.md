# Paper Search Debug Trace

**Query:** Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus only on papers where the main task is to take point clouds as input and directly reconstruct B-rep outputs as the final representation.

Prioritize methods that explicitly address the full reconstruction pipeline.

Exclude papers whose main contribution is only a subproblem, intermediate representation, auxiliary module, downstream application, or alternative task rather than end-to-end point-cloud-to-B-rep reconstruction.

A paper should not be treated as a core candidate unless reconstructing B-rep from point clouds is the primary task and final output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it is truly an end-to-end point-cloud-to-B-rep reconstruction method

Then summarize:
- major method categories
- recent trends
- open challenges

Be strict: prefer fewer but truly on-task papers over loosely related reconstruction, CAD, or geometric modeling papers.
**Generated At:** 2026-03-24T01:34:16
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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations, excluding works focused only on subproblems or intermediate representations.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "direct B-rep output from point clouds",
    "full reconstruction pipeline",
    "end-to-end learning or optimization methods",
    "boundary representation reconstruction"
  ],
  "exclude_areas": [
    "subproblem-only papers (e.g., segmentation, fitting)",
    "intermediate representations (e.g., mesh, voxel, implicit surface) as final output",
    "downstream applications (e.g., editing, simulation)",
    "alternative tasks (e.g., point cloud to CAD sequence, to CSG)"
  ],
  "query_variants": [
    "point cloud to B-rep reconstruction",
    "point cloud to boundary representation reconstruction",
    "learning B-rep from point clouds",
    "end-to-end B-rep reconstruction from point clouds",
    "direct CAD B-rep reconstruction from 3D points"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Directly captures the core task of converting point clouds to boundary representations.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ]
    },
    {
      "query": "end-to-end B-rep reconstruction from point clouds",
      "reason": "Emphasizes the full pipeline requirement, filtering methods that stop at intermediate representations.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ]
    },
    {
      "query": "learning B-rep from point clouds",
      "reason": "Targets data-driven or learning-based approaches that directly output B-rep, a likely frontier area.",
      "sources": [
        "arXiv",
        "OpenAlex"
      ]
    }
  ],
  "assumptions": [
    "The field is nascent; the number of truly end-to-end point-cloud-to-B-rep papers may be limited within 2022-2026.",
    "Some relevant works may use 'CAD reconstruction' or 'parametric CAD' synonymously with B-rep; queries aim to capture these.",
    "If few papers meet the strict criteria, the retrieval should prioritize those that do, even if the total is below 5."
  ],
  "success_criteria": [
    "Retrieved papers have point clouds as primary input and B-rep as final, explicit output.",
    "Each paper's core contribution is the reconstruction pipeline itself, not a component.",
    "Results enable categorization of methods, trends, and challenges in this specific frontier."
  ]
}
```

### Planner Output 8

- Topic: `End-to-end B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "End-to-end B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) where the primary, explicit task is a complete pipeline from raw point cloud input to boundary representation (B-rep) output, excluding works focused on subproblems, intermediate representations, or alternative tasks.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "direct B-rep output from point clouds",
    "full end-to-end reconstruction pipeline",
    "learning-based B-rep reconstruction",
    "parametric CAD model recovery from scans"
  ],
  "exclude_areas": [
    "SLAM and point cloud registration",
    "B-rep segmentation or feature recognition",
    "reconstruction to mesh/voxel/implicit surface",
    "single-image to 3D shape",
    "robotics or control applications",
    "point cloud generation or completion"
  ],
  "query_variants": [
    "\"B-rep\" reconstruction point cloud",
    "point cloud to CAD B-rep",
    "learning boundary representation from point cloud",
    "end-to-end parametric CAD from point cloud",
    "direct B-rep reconstruction from 3D scan"
  ],
  "queries": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "reason": "Uses the specific term 'B-rep' to filter out generic reconstruction papers and targets the core representation.",
      "sources": [
        "Crossref",
        "OpenAlex"
      ]
    },
    {
      "query": "point cloud to CAD B-rep",
      "reason": "Combines the input (point cloud), target domain (CAD), and output representation (B-rep) for precision.",
      "sources": [
        "Crossref",
        "OpenAlex",
        "arXiv"
      ]
    },
    {
      "query": "learning boundary representation from point cloud",
      "reason": "Targets data-driven, learning-based approaches which are likely frontier methods for this task.",
      "sources": [
        "arXiv",
        "OpenAlex"
      ]
    }
  ],
  "assumptions": [
    "The field is specialized; the total number of papers meeting strict criteria may be small (potentially <5).",
    "Relevant papers are likely published at computer vision (CVPR, ICCV, ECCV), graphics (SIGGRAPH, SIGGRAPH Asia), and CAD (CAD, JCISE) venues.",
    "If evidence confirms a paper's primary task is point-cloud-to-B-rep, it should be included even if the title/abstract uses 'CAD model' or 'parametric CAD' synonymously."
  ],
  "success_criteria": [
    "Retrieved papers explicitly state point cloud as input and B-rep (or boundary representation) as the final output.",
    "The paper's core contribution is the reconstruction pipeline itself, not a component like segmentation or fitting.",
    "At least 3-5 distinct, verified core candidates are identified to enable analysis of categories, trends, and challenges."
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
      "query": "end-to-end B-rep reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning B-rep from point clouds",
      "sources": [
        "arXiv",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": "doi:10 2139 ssrn 6172545"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": "doi:10 1093 jcde qwae005"
    },
    {
      "title": "Eigen-Factors a Bilevel Optimization for Back-end Plane SLAM of 3D Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-7-9",
      "url": "https://doi.org/10.21203/rs.3.rs-4601229/v1",
      "doi": "10.21203/rs.3.rs-4601229/v1",
      "authors": [
        "Gonzalo Ferrer",
        "Dmitrii Iarosh",
        "Anastasiia Kornilova"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p>Modern depth sensors can generate a huge number of 3D points in few seconds to be later processed by Localization and Mapping algorithms.Ideally, these algorithms should handle efficiently large sizes of Point Clouds (PC) under the assumption that using more points implies more information available.The Eigen Factors (EF) is a new algorithm that solves PC SLAM by using p"
      ],
      "duplicate_group": ""
    },
    {
      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-11-03",
      "url": "https://doi.org/10.1093/jcde/qwad106",
      "doi": "10.1093/jcde/qwad106",
      "authors": [
        "Jinwon Lee",
        "Changmo Yeo",
        "Sang-Uk Cheon",
        "Jun Hwan Park",
        "Duhwan Mun"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in dec"
      ],
      "duplicate_group": ""
    },
    {
      "title": "End-to-End Reinforcement Learning for Torque Based Variable Height Hopping",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-07-31T13:51:29Z",
      "url": "http://arxiv.org/abs/2307.16676v2",
      "doi": "",
      "authors": [
        "Raghav Soni",
        "Daniel Harnack",
        "Hannah Isermann",
        "Sotaro Fushimi",
        "Shivesh Kumar",
        "Frank Kirchner"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Legged locomotion is arguably the most suited and versatile mode to deal with natural or unstructured terrains. Intensive research into dynamic walking and running controllers has recently yielded great advances, both in the optimal control and reinforcement learning (RL) literature. Hopping is a challenging dynamic task involving a flight phase and has the potential to increase the traversability"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "3D Object Reconstruction From 2D Point Clouds Using Multi-stage Edge Detector",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-6-17",
      "url": "https://doi.org/10.32920/26052358.v1",
      "doi": "10.32920/26052358.v1",
      "authors": [
        "Oleg Prykladovskyi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt;The research, as described in this paper, is focused on finding a low-cost alternative to modern 3D reconstruction technologies used to recreate objects from orthogonal images. The main objective of the research is to create a 3D shape of an object, applying various software filters (C++ software environment) on six principal views of the object (bottom, top, front, back, left, an"
      ],
      "duplicate_group": ""
    },
    {
      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-02-21T13:37:07Z",
      "url": "http://arxiv.org/abs/2302.10668v2",
      "doi": "",
      "authors": [
        "Luke Melas-Kyriazi",
        "Christian Rupprecht",
        "Andrea Vedaldi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3"
      ],
      "duplicate_group": ""
    },
    {
      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",
      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",
      "year": 2023,
      "date": "2023-8",
      "url": "https://doi.org/10.24963/ijcai.2023/134",
      "doi": "10.24963/ijcai.2023/134",
      "authors": [
        "Quan Liu",
        "Yunsong Zhou",
        "Hongzi Zhu",
        "Shan Chang",
        "Minyi Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 18 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "point cloud to boundary representation reconstruction",
      "learning B-rep from point clouds",
      "end-to-end B-rep reconstruction from point clouds",
      "direct CAD B-rep reconstruction from 3D points"
    ],
    "planned_queries": [
      "point cloud to B-rep reconstruction",
      "end-to-end B-rep reconstruction from point clouds",
      "learning B-rep from point clouds"
    ],
    "fallback_topic": "B-rep reconstruction from point clouds",
    "executed_queries": [
      "point cloud to B-rep reconstruction",
      "end-to-end B-rep reconstruction from point clouds",
      "learning B-rep from point clouds"
    ]
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
      "query": "\"B-rep\" reconstruction point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to CAD B-rep",
      "sources": [
        "Crossref",
        "OpenAlex",
        "arXiv"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning boundary representation from point cloud",
      "sources": [
        "arXiv",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "FuS-GCN: Efficient B-rep based graph convolutional networks for 3D-CAD model classification and retrieval",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-04-01",
      "url": "https://doi.org/10.1016/j.aei.2023.102008",
      "doi": "10.1016/j.aei.2023.102008",
      "authors": [
        "Junhao Hou",
        "Chenqi Luo",
        "Feiwei Qin",
        "Yanli Shao",
        "Xiaxuan Chen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Performing 3-dimensional computer-aided design (3D-CAD) model classification , retrieval, and reuse is of vital importance in industrial manufacturing, as it considerably shortens the engineering development cycle and reduces development costs. Although existing 3D model classification and retrieval methods achieve satisfactory performance when operating on meshes or point clouds, they cannot be a"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": "doi:10 2139 ssrn 6172545"
    },
    {
      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-02-24",
      "url": "http://arxiv.org/abs/2602.21105",
      "doi": "",
      "authors": [
        "Jiaxing Yu",
        "Dongyang Ren",
        "Hangyu Xu",
        "Zhouyuxiao Yang",
        "Yuanqi Li",
        "Jie Guo",
        "Zhengkang Zhou",
        "Yanwen Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"
      ],
      "duplicate_group": ""
    },
    {
      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-02-24",
      "url": "https://doi.org/10.48550/arxiv.2602.21105",
      "doi": "10.48550/arxiv.2602.21105",
      "authors": [
        "Jiaxing Yu",
        "Dongyang Ren",
        "Hangyu Xu",
        "Zhouyuxiao Yang",
        "Yuanqi Li",
        "Jie Guo",
        "Zhengkang Zhou",
        "Yanwen Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-12T11:54:29Z",
      "url": "http://arxiv.org/abs/2603.11831v1",
      "doi": "",
      "authors": [
        "Jiahao Li",
        "Qingwang Zhang",
        "Qiuyu Chen",
        "Guozhan Qiu",
        "Yunzhong Lou",
        "Xiangdong Zhou"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) requir"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ],
      "duplicate_group": "doi:10 3233 ica 240744"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": "doi:10 1145 3528223 3530078"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ],
      "duplicate_group": "doi:10 48550 arxiv 2205 14573"
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 39 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "\"B-rep\" reconstruction point cloud",
    "effective_query": "\"B-rep\" reconstruction point cloud",
    "used_override_query": true,
    "query_variants": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud",
      "end-to-end parametric CAD from point cloud",
      "direct B-rep reconstruction from 3D scan"
    ],
    "planned_queries": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud"
    ],
    "fallback_topic": "End-to-end B-rep reconstruction from point clouds",
    "executed_queries": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud"
    ]
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
  "review_summary": "The retrieval output fails multiple hard requirements. While three distinct sources were used, the candidate set is dominated by papers that are not core to the user's strict end-to-end point-cloud-to-B-rep reconstruction task. Only one paper (P2CADNet) appears to be a plausible core candidate, and its evidence is only partial. Several retrieved papers are clearly off-topic (e.g., SLAM, robotics, point cloud registration). The relevance, core-method fit, and query fit requirements are not met. The evidence quality is weak, with most papers having only abstract snippets that do not confirm the required input/output pipeline.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 1,
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
      "reason": "After deduplication, 10 candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 candidates, only 1 (P2CADNet) appears strongly aligned. Others are either off-topic (e.g., Eigen-Factors (SLAM), End-to-End Reinforcement Learning for Hopping) or their relevance is not substantiated by the provided evidence snippets."
    },
    "metadata": {
      "passed": true,
      "reason": "Each candidate has title, source, year/date, and URL. Author lists are present but sometimes duplicated (e.g., Point2Brep)."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (end-to-end pipeline, point cloud input, B-rep output, exclude subproblems) are not reflected in the majority of the retrieved set. Many papers are about SLAM, point cloud registration, feature segmentation, or single-image 3D reconstruction to point clouds, not B-rep reconstruction from point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only one paper (P2CADNet) is flagged as a core candidate and has partial evidence. Its abstract suggests an end-to-end network for featured CAD model from point cloud, which is promising. However, at least 3 core candidates are required. Other papers like Point2Brep and ComplexGen have titles suggesting relevance, but their evidence snippets are incomplete and do not confirm the point-cloud-to-B-rep pipeline; they are marked as non-core by the retrieval layer. BRepGAT is about segmentation of existing B-rep models, not reconstruction from point clouds."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: the retrieval failed to find several known recent works on learning-based B-rep reconstruction from point clouds (e.g., from CVPR, SIGGRAPH, CAD conferences). The set is over-reliant on broad keyword matching, resulting in many irrelevant papers."
    }
  },
  "key_risks": ["The field is nascent, but the current retrieval is too noisy and includes many false positives.", "Evidence snippets are too short to verify the core task for borderline papers (e.g., Point2Brep, ComplexGen).", "If the writer uses this set as-is, the report will be misleading and include irrelevant work."],
  "next_actions": ["Refine search queries to be more precise and include venue filters. Use queries like: '\"B-rep\" reconstruction point cloud' 'point cloud to CAD B-rep' 'learning boundary representation from point cloud' 'CVPR point cloud B-rep reconstruction'.", "Prioritize sources like ACM Digital Library, IEEE Xplore, and specific conference proceedings (e.g., SIGGRAPH, CVPR, CAD) where such frontier work is likely published.", "For each candidate, retrieve and inspect the full abstract or introduction to definitively confirm the input (point cloud) and output (B-rep) and that it is the paper's primary task. Exclude papers where B-rep is an intermediate representation or the input is not a raw point cloud.", "If the number of true core papers is below 5, acknowledge this as a finding and focus the report on the identified few, explicitly stating the strict criteria limited the set."]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows improved focus on B-rep and CAD, but critical hard requirements remain unmet. The relevance and core-method fit are insufficient because the evidence snippets do not confirm that point clouds are the primary input for most papers. Several papers are about datasets, classification, generation from images, or annotation pipelines, not end-to-end point-cloud-to-B-rep reconstruction. Only Point2Brep and ComplexGen appear promising, but their evidence is partial and does not explicitly state point cloud as the sole input. The candidate set lacks depth of verified, on-topic papers.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 candidate papers remain (though some are duplicates of the same work, e.g., ComplexGen appears twice)."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 candidates, only Point2Brep and ComplexGen appear relevant based on titles and snippets. FuS-GCN is about classification/retrieval of existing B-rep models, not reconstruction from point clouds. BrepGaussian uses multi-view images as input, not point clouds. The LLM-driven paper is about generation, not reconstruction from point clouds."
    },
    "metadata": {
      "passed": true,
      "reason": "Each candidate has title, source, year/date, and URL. Author lists are present."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraint of 'point clouds as input' is not satisfied for many papers. BrepGaussian uses multi-view images. FuS-GCN uses existing B-rep models. The dataset paper and annotation pipeline paper are not about reconstruction pipelines. The LLM-driven paper is about generation, not reconstruction from sensor data."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers (Point2Brep, ComplexGen) are plausible core candidates based on titles and snippets, but their evidence is partial and does not explicitly confirm point cloud as the input. At least 3 verified core candidates are required. Other papers are clearly not core (dataset, classification, image-based, annotation)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence hole: the retrieval did not verify the input modality for each candidate. The set is missing known works like 'P2CADNet' (from the previous retrieval) which explicitly mentions point cloud input. The search appears to have over-prioritized the term 'B-rep' without ensuring 'point cloud' is in the evidence."
    }
  },
  "key_risks": ["The evidence snippets are too vague to confirm the input/output pipeline. Without full abstract inspection, we cannot be sure which papers truly meet the strict criteria.", "The retrieval may have excluded relevant papers that use 'parametric CAD' instead of 'B-rep' in the title/abstract.", "If the writer proceeds, they might incorrectly include dataset or image-based papers as core reconstruction methods."],
  "next_actions": ["For each candidate marked as core_candidate=true, retrieve the full abstract (or at least a longer snippet) to explicitly check for phrases like 'from point cloud', 'point cloud as input', 'scan data', '3D points'. Exclude papers where input is images, meshes, voxels, or existing CAD models.", "Re-include 'P2CADNet' from the previous retrieval if its abstract confirms point cloud input and B-rep output.", "Execute a new query that explicitly combines both terms: '\"point cloud\" \"B-rep\" reconstruction' and '\"point cloud\" \"boundary representation\" reconstruction'.", "Search in specific venues known for CAD reconstruction: ACM Transactions on Graphics (TOG), Computer-Aided Design, IEEE CVPR/ICCV/ECCV proceedings, using their digital libraries if accessible.", "If after verification the number of true core papers is still below 3, acknowledge this as a finding and prepare to report on the limited set, explicitly stating the strict criteria resulted in a small frontier."]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_y0Jl6yr7dqtGGOXgpJx5kUZ9', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end B-rep reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning B-rep from point clouds",\n      "sources": [\n        "arXiv",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": "doi:10 2139 ssrn 6172545"\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "Eigen-Factors a Bilevel Optimization for Back-end Plane SLAM of 3D Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-7-9",\n      "url": "https://doi.org/10.21203/rs.3.rs-4601229/v1",\n      "doi": "10.21203/rs.3.rs-4601229/v1",\n      "authors": [\n        "Gonzalo Ferrer",\n        "Dmitrii Iarosh",\n        "Anastasiia Kornilova"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p>Modern depth sensors can generate a huge number of 3D points in few seconds to be later processed by Localization and Mapping algorithms.Ideally, these algorithms should handle efficiently large sizes of Point Clouds (PC) under the assumption that using more points implies more information available.The Eigen Factors (EF) is a new algorithm that solves PC SLAM by using p"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-11-03",\n      "url": "https://doi.org/10.1093/jcde/qwad106",\n      "doi": "10.1093/jcde/qwad106",\n      "authors": [\n        "Jinwon Lee",\n        "Changmo Yeo",\n        "Sang-Uk Cheon",\n        "Jun Hwan Park",\n        "Duhwan Mun"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in dec"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "End-to-End Reinforcement Learning for Torque Based Variable Height Hopping",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-07-31T13:51:29Z",\n      "url": "http://arxiv.org/abs/2307.16676v2",\n      "doi": "",\n      "authors": [\n        "Raghav Soni",\n        "Daniel Harnack",\n        "Hannah Isermann",\n        "Sotaro Fushimi",\n        "Shivesh Kumar",\n        "Frank Kirchner"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Legged locomotion is arguably the most suited and versatile mode to deal with natural or unstructured terrains. Intensive research into dynamic walking and running controllers has recently yielded great advances, both in the optimal control and reinforcement learning (RL) literature. Hopping is a challenging dynamic task involving a flight phase and has the potential to increase the traversability"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "3D Object Reconstruction From 2D Point Clouds Using Multi-stage Edge Detector",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-6-17",\n      "url": "https://doi.org/10.32920/26052358.v1",\n      "doi": "10.32920/26052358.v1",\n      "authors": [\n        "Oleg Prykladovskyi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt;The research, as described in this paper, is focused on finding a low-cost alternative to modern 3D reconstruction technologies used to recreate objects from orthogonal images. The main objective of the research is to create a 3D shape of an object, applying various software filters (C++ software environment) on six principal views of the object (bottom, top, front, back, left, an"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",\n      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n      "year": 2023,\n      "date": "2023-8",\n      "url": "https://doi.org/10.24963/ijcai.2023/134",\n      "doi": "10.24963/ijcai.2023/134",\n      "authors": [\n        "Quan Liu",\n        "Yunsong Zhou",\n        "Hongzi Zhu",\n        "Shan Chang",\n        "Minyi Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 18 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "point cloud to boundary representation reconstruction",\n      "learning B-rep from point clouds",\n      "end-to-end B-rep reconstruction from point clouds",\n      "direct CAD B-rep reconstruction from 3D points"\n    ],\n    "planned_queries": [\n      "point cloud to B-rep reconstruction",\n      "end-to-end B-rep reconstruction from point clouds",\n      "learning B-rep from point clouds"\n    ],\n    "fallback_topic": "B-rep reconstruction from point clouds",\n    "executed_queries": [\n      "point cloud to B-rep reconstruction",\n      "end-to-end B-rep reconstruction from point clouds",\n      "learning B-rep from point clouds"\n    ]\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_y0Jl6yr7dqtGGOXgpJx5kUZ9' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_RsdIMaXUbOoypgln1elaoH5X', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "\\"B-rep\\" reconstruction point cloud"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"B-rep\\" reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to CAD B-rep",\n      "sources": [\n        "Crossref",\n        "OpenAlex",\n        "arXiv"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning boundary representation from point cloud",\n      "sources": [\n        "arXiv",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "FuS-GCN: Efficient B-rep based graph convolutional networks for 3D-CAD model classification and retrieval",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-04-01",\n      "url": "https://doi.org/10.1016/j.aei.2023.102008",\n      "doi": "10.1016/j.aei.2023.102008",\n      "authors": [\n        "Junhao Hou",\n        "Chenqi Luo",\n        "Feiwei Qin",\n        "Yanli Shao",\n        "Xiaxuan Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Performing 3-dimensional computer-aided design (3D-CAD) model classification , retrieval, and reuse is of vital importance in industrial manufacturing, as it considerably shortens the engineering development cycle and reduces development costs. Although existing 3D model classification and retrieval methods achieve satisfactory performance when operating on meshes or point clouds, they cannot be a"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": "doi:10 2139 ssrn 6172545"\n    },\n    {\n      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-02-24",\n      "url": "http://arxiv.org/abs/2602.21105",\n      "doi": "",\n      "authors": [\n        "Jiaxing Yu",\n        "Dongyang Ren",\n        "Hangyu Xu",\n        "Zhouyuxiao Yang",\n        "Yuanqi Li",\n        "Jie Guo",\n        "Zhengkang Zhou",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-02-24",\n      "url": "https://doi.org/10.48550/arxiv.2602.21105",\n      "doi": "10.48550/arxiv.2602.21105",\n      "authors": [\n        "Jiaxing Yu",\n        "Dongyang Ren",\n        "Hangyu Xu",\n        "Zhouyuxiao Yang",\n        "Yuanqi Li",\n        "Jie Guo",\n        "Zhengkang Zhou",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-12T11:54:29Z",\n      "url": "http://arxiv.org/abs/2603.11831v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Qingwang Zhang",\n        "Qiuyu Chen",\n        "Guozhan Qiu",\n        "Yunzhong Lou",\n        "Xiangdong Zhou"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) requir"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": "doi:10 3233 ica 240744"\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": "doi:10 1145 3528223 3530078"\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": "doi:10 48550 arxiv 2205 14573"\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 39 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "\\"B-rep\\" reconstruction point cloud",\n    "effective_query": "\\"B-rep\\" reconstruction point cloud",\n    "used_override_query": true,\n    "query_variants": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud",\n      "end-to-end parametric CAD from point cloud",\n      "direct B-rep reconstruction from 3D scan"\n    ],\n    "planned_queries": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud"\n    ],\n    "fallback_topic": "End-to-end B-rep reconstruction from point clouds",\n    "executed_queries": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud"\n    ]\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_RsdIMaXUbOoypgln1elaoH5X' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

```text
Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus only on papers where the main task is to take point clouds as input and directly reconstruct B-rep outputs as the final representation.

Prioritize methods that explicitly address the full reconstruction pipeline.

Exclude papers whose main contribution is only a subproblem, intermediate representation, auxiliary module, downstream application, or alternative task rather than end-to-end point-cloud-to-B-rep reconstruction.

A paper should not be treated as a core candidate unless reconstructing B-rep from point clouds is the primary task and final output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it is truly an end-to-end point-cloud-to-B-rep reconstruction method

Then summarize:
- major method categories
- recent trends
- open challenges

Be strict: prefer fewer but truly on-task papers over loosely related reconstruction, CAD, or geometric modeling papers.

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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations, excluding works focused only on subproblems or intermediate representations.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["direct B-rep output from point clouds", "full reconstruction pipeline", "end-to-end learning or optimization methods", "boundary representation reconstruction"],
  "exclude_areas": ["subproblem-only papers (e.g., segmentation, fitting)", "intermediate representations (e.g., mesh, voxel, implicit surface) as final output", "downstream applications (e.g., editing, simulation)", "alternative tasks (e.g., point cloud to CAD sequence, to CSG)"],
  "query_variants": ["point cloud to B-rep reconstruction", "point cloud to boundary representation reconstruction", "learning B-rep from point clouds", "end-to-end B-rep reconstruction from point clouds", "direct CAD B-rep reconstruction from 3D points"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction",
      "reason": "Directly captures the core task of converting point clouds to boundary representations.",
      "sources": ["arXiv", "Crossref", "OpenAlex"]
    },
    {
      "query": "end-to-end B-rep reconstruction from point clouds",
      "reason": "Emphasizes the full pipeline requirement, filtering methods that stop at intermediate representations.",
      "sources": ["arXiv", "Crossref", "OpenAlex"]
    },
    {
      "query": "learning B-rep from point clouds",
      "reason": "Targets data-driven or learning-based approaches that directly output B-rep, a likely frontier area.",
      "sources": ["arXiv", "OpenAlex"]
    }
  ],
  "assumptions": ["The field is nascent; the number of truly end-to-end point-cloud-to-B-rep papers may be limited within 2022-2026.", "Some relevant works may use 'CAD reconstruction' or 'parametric CAD' synonymously with B-rep; queries aim to capture these.", "If few papers meet the strict criteria, the retrieval should prioritize those that do, even if the total is below 5."],
  "success_criteria": ["Retrieved papers have point clouds as primary input and B-rep as final, explicit output.", "Each paper's core contribution is the reconstruction pipeline itself, not a component.", "Results enable categorization of methods, trends, and challenges in this specific frontier."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find papers on B-rep reconstruction from point clouds within the 2022-2026 timeframe. Let me start with the primary retrieval.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_y0Jl6yr7dqtGGOXgpJx5kUZ9', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end B-rep reconstruction from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning B-rep from point clouds",\n      "sources": [\n        "arXiv",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": "doi:10 2139 ssrn 6172545"\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "Eigen-Factors a Bilevel Optimization for Back-end Plane SLAM of 3D Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-7-9",\n      "url": "https://doi.org/10.21203/rs.3.rs-4601229/v1",\n      "doi": "10.21203/rs.3.rs-4601229/v1",\n      "authors": [\n        "Gonzalo Ferrer",\n        "Dmitrii Iarosh",\n        "Anastasiia Kornilova"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p>Modern depth sensors can generate a huge number of 3D points in few seconds to be later processed by Localization and Mapping algorithms.Ideally, these algorithms should handle efficiently large sizes of Point Clouds (PC) under the assumption that using more points implies more information available.The Eigen Factors (EF) is a new algorithm that solves PC SLAM by using p"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-11-03",\n      "url": "https://doi.org/10.1093/jcde/qwad106",\n      "doi": "10.1093/jcde/qwad106",\n      "authors": [\n        "Jinwon Lee",\n        "Changmo Yeo",\n        "Sang-Uk Cheon",\n        "Jun Hwan Park",\n        "Duhwan Mun"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in dec"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "End-to-End Reinforcement Learning for Torque Based Variable Height Hopping",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-07-31T13:51:29Z",\n      "url": "http://arxiv.org/abs/2307.16676v2",\n      "doi": "",\n      "authors": [\n        "Raghav Soni",\n        "Daniel Harnack",\n        "Hannah Isermann",\n        "Sotaro Fushimi",\n        "Shivesh Kumar",\n        "Frank Kirchner"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Legged locomotion is arguably the most suited and versatile mode to deal with natural or unstructured terrains. Intensive research into dynamic walking and running controllers has recently yielded great advances, both in the optimal control and reinforcement learning (RL) literature. Hopping is a challenging dynamic task involving a flight phase and has the potential to increase the traversability"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "3D Object Reconstruction From 2D Point Clouds Using Multi-stage Edge Detector",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-6-17",\n      "url": "https://doi.org/10.32920/26052358.v1",\n      "doi": "10.32920/26052358.v1",\n      "authors": [\n        "Oleg Prykladovskyi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'end to end brep reconstruction from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt;The research, as described in this paper, is focused on finding a low-cost alternative to modern 3D reconstruction technologies used to recreate objects from orthogonal images. The main objective of the research is to create a 3D shape of an object, applying various software filters (C++ software environment) on six principal views of the object (bottom, top, front, back, left, an"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",\n      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n      "year": 2023,\n      "date": "2023-8",\n      "url": "https://doi.org/10.24963/ijcai.2023/134",\n      "doi": "10.24963/ijcai.2023/134",\n      "authors": [\n        "Quan Liu",\n        "Yunsong Zhou",\n        "Hongzi Zhu",\n        "Shan Chang",\n        "Minyi Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 18 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "point cloud to boundary representation reconstruction",\n      "learning B-rep from point clouds",\n      "end-to-end B-rep reconstruction from point clouds",\n      "direct CAD B-rep reconstruction from 3D points"\n    ],\n    "planned_queries": [\n      "point cloud to B-rep reconstruction",\n      "end-to-end B-rep reconstruction from point clouds",\n      "learning B-rep from point clouds"\n    ],\n    "fallback_topic": "B-rep reconstruction from point clouds",\n    "executed_queries": [\n      "point cloud to B-rep reconstruction",\n      "end-to-end B-rep reconstruction from point clouds",\n      "learning B-rep from point clouds"\n    ]\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_y0Jl6yr7dqtGGOXgpJx5kUZ9' is_error=False
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
      "query": "end-to-end B-rep reconstruction from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning B-rep from point clouds",
      "sources": [
        "arXiv",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "Crossref / Crossref | OpenAlex | Crossref / Crossref",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": "doi:10 2139 ssrn 6172545"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": "doi:10 1093 jcde qwae005"
    },
    {
      "title": "Eigen-Factors a Bilevel Optimization for Back-end Plane SLAM of 3D Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-7-9",
      "url": "https://doi.org/10.21203/rs.3.rs-4601229/v1",
      "doi": "10.21203/rs.3.rs-4601229/v1",
      "authors": [
        "Gonzalo Ferrer",
        "Dmitrii Iarosh",
        "Anastasiia Kornilova"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p>Modern depth sensors can generate a huge number of 3D points in few seconds to be later processed by Localization and Mapping algorithms.Ideally, these algorithms should handle efficiently large sizes of Point Clouds (PC) under the assumption that using more points implies more information available.The Eigen Factors (EF) is a new algorithm that solves PC SLAM by using p"
      ],
      "duplicate_group": ""
    },
    {
      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-11-03",
      "url": "https://doi.org/10.1093/jcde/qwad106",
      "doi": "10.1093/jcde/qwad106",
      "authors": [
        "Jinwon Lee",
        "Changmo Yeo",
        "Sang-Uk Cheon",
        "Jun Hwan Park",
        "Duhwan Mun"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in dec"
      ],
      "duplicate_group": ""
    },
    {
      "title": "End-to-End Reinforcement Learning for Torque Based Variable Height Hopping",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-07-31T13:51:29Z",
      "url": "http://arxiv.org/abs/2307.16676v2",
      "doi": "",
      "authors": [
        "Raghav Soni",
        "Daniel Harnack",
        "Hannah Isermann",
        "Sotaro Fushimi",
        "Shivesh Kumar",
        "Frank Kirchner"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Legged locomotion is arguably the most suited and versatile mode to deal with natural or unstructured terrains. Intensive research into dynamic walking and running controllers has recently yielded great advances, both in the optimal control and reinforcement learning (RL) literature. Hopping is a challenging dynamic task involving a flight phase and has the potential to increase the traversability"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "3D Object Reconstruction From 2D Point Clouds Using Multi-stage Edge Detector",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-6-17",
      "url": "https://doi.org/10.32920/26052358.v1",
      "doi": "10.32920/26052358.v1",
      "authors": [
        "Oleg Prykladovskyi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'end to end brep reconstruction from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt;The research, as described in this paper, is focused on finding a low-cost alternative to modern 3D reconstruction technologies used to recreate objects from orthogonal images. The main objective of the research is to create a 3D shape of an object, applying various software filters (C++ software environment) on six principal views of the object (bottom, top, front, back, left, an"
      ],
      "duplicate_group": ""
    },
    {
      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-02-21T13:37:07Z",
      "url": "http://arxiv.org/abs/2302.10668v2",
      "doi": "",
      "authors": [
        "Luke Melas-Kyriazi",
        "Christian Rupprecht",
        "Andrea Vedaldi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3"
      ],
      "duplicate_group": ""
    },
    {
      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",
      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",
      "year": 2023,
      "date": "2023-8",
      "url": "https://doi.org/10.24963/ijcai.2023/134",
      "doi": "10.24963/ijcai.2023/134",
      "authors": [
        "Quan Liu",
        "Yunsong Zhou",
        "Hongzi Zhu",
        "Shan Chang",
        "Minyi Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 18 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "point cloud to boundary representation reconstruction",
      "learning B-rep from point clouds",
      "end-to-end B-rep reconstruction from point clouds",
      "direct CAD B-rep reconstruction from 3D points"
    ],
    "planned_queries": [
      "point cloud to B-rep reconstruction",
      "end-to-end B-rep reconstruction from point clouds",
      "learning B-rep from point clouds"
    ],
    "fallback_topic": "B-rep reconstruction from point clouds",
    "executed_queries": [
      "point cloud to B-rep reconstruction",
      "end-to-end B-rep reconstruction from point clouds",
      "learning B-rep from point clouds"
    ]
  }
}
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=4

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output fails multiple hard requirements. While three distinct sources were used, the candidate set is dominated by papers that are not core to the user's strict end-to-end point-cloud-to-B-rep reconstruction task. Only one paper (P2CADNet) appears to be a plausible core candidate, and its evidence is only partial. Several retrieved papers are clearly off-topic (e.g., SLAM, robotics, point cloud registration). The relevance, core-method fit, and query fit requirements are not met. The evidence quality is weak, with most papers having only abstract snippets that do not confirm the required input/output pipeline.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 1,
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
      "reason": "After deduplication, 10 candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 candidates, only 1 (P2CADNet) appears strongly aligned. Others are either off-topic (e.g., Eigen-Factors (SLAM), End-to-End Reinforcement Learning for Hopping) or their relevance is not substantiated by the provided evidence snippets."
    },
    "metadata": {
      "passed": true,
      "reason": "Each candidate has title, source, year/date, and URL. Author lists are present but sometimes duplicated (e.g., Point2Brep)."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraints (end-to-end pipeline, point cloud input, B-rep output, exclude subproblems) are not reflected in the majority of the retrieved set. Many papers are about SLAM, point cloud registration, feature segmentation, or single-image 3D reconstruction to point clouds, not B-rep reconstruction from point clouds."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only one paper (P2CADNet) is flagged as a core candidate and has partial evidence. Its abstract suggests an end-to-end network for featured CAD model from point cloud, which is promising. However, at least 3 core candidates are required. Other papers like Point2Brep and ComplexGen have titles suggesting relevance, but their evidence snippets are incomplete and do not confirm the point-cloud-to-B-rep pipeline; they are marked as non-core by the retrieval layer. BRepGAT is about segmentation of existing B-rep models, not reconstruction from point clouds."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: the retrieval failed to find several known recent works on learning-based B-rep reconstruction from point clouds (e.g., from CVPR, SIGGRAPH, CAD conferences). The set is over-reliant on broad keyword matching, resulting in many irrelevant papers."
    }
  },
  "key_risks": ["The field is nascent, but the current retrieval is too noisy and includes many false positives.", "Evidence snippets are too short to verify the core task for borderline papers (e.g., Point2Brep, ComplexGen).", "If the writer uses this set as-is, the report will be misleading and include irrelevant work."],
  "next_actions": ["Refine search queries to be more precise and include venue filters. Use queries like: '\"B-rep\" reconstruction point cloud' 'point cloud to CAD B-rep' 'learning boundary representation from point cloud' 'CVPR point cloud B-rep reconstruction'.", "Prioritize sources like ACM Digital Library, IEEE Xplore, and specific conference proceedings (e.g., SIGGRAPH, CVPR, CAD) where such frontier work is likely published.", "For each candidate, retrieve and inspect the full abstract or introduction to definitively confirm the input (point cloud) and output (B-rep) and that it is the paper's primary task. Exclude papers where B-rep is an intermediate representation or the input is not a raw point cloud.", "If the number of true core papers is below 5, acknowledge this as a finding and focus the report on the identified few, explicitly stating the strict criteria limited the set."]
}
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=End-to-end B-rep reconstruction from point clouds, queries=3, years=2022-2026

```text
{
  "topic": "End-to-end B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) where the primary, explicit task is a complete pipeline from raw point cloud input to boundary representation (B-rep) output, excluding works focused on subproblems, intermediate representations, or alternative tasks.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["direct B-rep output from point clouds", "full end-to-end reconstruction pipeline", "learning-based B-rep reconstruction", "parametric CAD model recovery from scans"],
  "exclude_areas": ["SLAM and point cloud registration", "B-rep segmentation or feature recognition", "reconstruction to mesh/voxel/implicit surface", "single-image to 3D shape", "robotics or control applications", "point cloud generation or completion"],
  "query_variants": ["\"B-rep\" reconstruction point cloud", "point cloud to CAD B-rep", "learning boundary representation from point cloud", "end-to-end parametric CAD from point cloud", "direct B-rep reconstruction from 3D scan"],
  "queries": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "reason": "Uses the specific term 'B-rep' to filter out generic reconstruction papers and targets the core representation.",
      "sources": ["Crossref", "OpenAlex"]
    },
    {
      "query": "point cloud to CAD B-rep",
      "reason": "Combines the input (point cloud), target domain (CAD), and output representation (B-rep) for precision.",
      "sources": ["Crossref", "OpenAlex", "arXiv"]
    },
    {
      "query": "learning boundary representation from point cloud",
      "reason": "Targets data-driven, learning-based approaches which are likely frontier methods for this task.",
      "sources": ["arXiv", "OpenAlex"]
    }
  ],
  "assumptions": ["The field is specialized; the total number of papers meeting strict criteria may be small (potentially <5).", "Relevant papers are likely published at computer vision (CVPR, ICCV, ECCV), graphics (SIGGRAPH, SIGGRAPH Asia), and CAD (CAD, JCISE) venues.", "If evidence confirms a paper's primary task is point-cloud-to-B-rep, it should be included even if the title/abstract uses 'CAD model' or 'parametric CAD' synonymously."],
  "success_criteria": ["Retrieved papers explicitly state point cloud as input and B-rep (or boundary representation) as the final output.", "The paper's core contribution is the reconstruction pipeline itself, not a component like segmentation or fitting.", "At least 3-5 distinct, verified core candidates are identified to enable analysis of categories, trends, and challenges."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a revised search with more precise queries to find papers that truly match the strict criteria of end-to-end point-cloud-to-B-rep reconstruction.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_RsdIMaXUbOoypgln1elaoH5X', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "\\"B-rep\\" reconstruction point cloud"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"B-rep\\" reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to CAD B-rep",\n      "sources": [\n        "Crossref",\n        "OpenAlex",\n        "arXiv"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning boundary representation from point cloud",\n      "sources": [\n        "arXiv",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "FuS-GCN: Efficient B-rep based graph convolutional networks for 3D-CAD model classification and retrieval",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-04-01",\n      "url": "https://doi.org/10.1016/j.aei.2023.102008",\n      "doi": "10.1016/j.aei.2023.102008",\n      "authors": [\n        "Junhao Hou",\n        "Chenqi Luo",\n        "Feiwei Qin",\n        "Yanli Shao",\n        "Xiaxuan Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Performing 3-dimensional computer-aided design (3D-CAD) model classification , retrieval, and reuse is of vital importance in industrial manufacturing, as it considerably shortens the engineering development cycle and reduces development costs. Although existing 3D model classification and retrieval methods achieve satisfactory performance when operating on meshes or point clouds, they cannot be a"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref | OpenAlex",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen",\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": "doi:10 2139 ssrn 6172545"\n    },\n    {\n      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-02-24",\n      "url": "http://arxiv.org/abs/2602.21105",\n      "doi": "",\n      "authors": [\n        "Jiaxing Yu",\n        "Dongyang Ren",\n        "Hangyu Xu",\n        "Zhouyuxiao Yang",\n        "Yuanqi Li",\n        "Jie Guo",\n        "Zhengkang Zhou",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-02-24",\n      "url": "https://doi.org/10.48550/arxiv.2602.21105",\n      "doi": "10.48550/arxiv.2602.21105",\n      "authors": [\n        "Jiaxing Yu",\n        "Dongyang Ren",\n        "Hangyu Xu",\n        "Zhouyuxiao Yang",\n        "Yuanqi Li",\n        "Jie Guo",\n        "Zhengkang Zhou",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-12T11:54:29Z",\n      "url": "http://arxiv.org/abs/2603.11831v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Qingwang Zhang",\n        "Qiuyu Chen",\n        "Guozhan Qiu",\n        "Yunzhong Lou",\n        "Xiangdong Zhou"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) requir"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan",\n        "Xiaohu Yan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": "doi:10 3233 ica 240744"\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to cad brep\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": "doi:10 1145 3528223 3530078"\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction pointcloud\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": "doi:10 48550 arxiv 2205 14573"\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 39 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "\\"B-rep\\" reconstruction point cloud",\n    "effective_query": "\\"B-rep\\" reconstruction point cloud",\n    "used_override_query": true,\n    "query_variants": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud",\n      "end-to-end parametric CAD from point cloud",\n      "direct B-rep reconstruction from 3D scan"\n    ],\n    "planned_queries": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud"\n    ],\n    "fallback_topic": "End-to-end B-rep reconstruction from point clouds",\n    "executed_queries": [\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD B-rep",\n      "learning boundary representation from point cloud"\n    ]\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_RsdIMaXUbOoypgln1elaoH5X' is_error=False
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
      "query": "\"B-rep\" reconstruction point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to CAD B-rep",
      "sources": [
        "Crossref",
        "OpenAlex",
        "arXiv"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning boundary representation from point cloud",
      "sources": [
        "arXiv",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    }
  ],
  "papers": [
    {
      "title": "FuS-GCN: Efficient B-rep based graph convolutional networks for 3D-CAD model classification and retrieval",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-04-01",
      "url": "https://doi.org/10.1016/j.aei.2023.102008",
      "doi": "10.1016/j.aei.2023.102008",
      "authors": [
        "Junhao Hou",
        "Chenqi Luo",
        "Feiwei Qin",
        "Yanli Shao",
        "Xiaxuan Chen"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Performing 3-dimensional computer-aided design (3D-CAD) model classification , retrieval, and reuse is of vital importance in industrial manufacturing, as it considerably shortens the engineering development cycle and reduces development costs. Although existing 3D model classification and retrieval methods achieve satisfactory performance when operating on meshes or point clouds, they cannot be a"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
      ],
      "duplicate_group": "doi:10 2139 ssrn 6172545"
    },
    {
      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-02-24",
      "url": "http://arxiv.org/abs/2602.21105",
      "doi": "",
      "authors": [
        "Jiaxing Yu",
        "Dongyang Ren",
        "Hangyu Xu",
        "Zhouyuxiao Yang",
        "Yuanqi Li",
        "Jie Guo",
        "Zhengkang Zhou",
        "Yanwen Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"
      ],
      "duplicate_group": ""
    },
    {
      "title": "BrepGaussian: CAD reconstruction from Multi-View Images with Gaussian Splatting",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-02-24",
      "url": "https://doi.org/10.48550/arxiv.2602.21105",
      "doi": "10.48550/arxiv.2602.21105",
      "authors": [
        "Jiaxing Yu",
        "Dongyang Ren",
        "Hangyu Xu",
        "Zhouyuxiao Yang",
        "Yuanqi Li",
        "Jie Guo",
        "Zhengkang Zhou",
        "Yanwen Guo"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-rep) models a 3D solid as its explicit boundaries: trimmed corners, edges, and faces. Recovering B-rep representation from unstructured data is a challenging and valuable task of computer vision and graphics. Recent advances in deep learning have greatly improved the recovery of 3D shape geometry, but still depend on dense and clean point clouds and struggle to gener"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-12T11:54:29Z",
      "url": "http://arxiv.org/abs/2603.11831v1",
      "doi": "",
      "authors": [
        "Jiahao Li",
        "Qingwang Zhang",
        "Qiuyu Chen",
        "Guozhan Qiu",
        "Yunzhong Lou",
        "Xiangdong Zhou"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) requir"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"
      ],
      "duplicate_group": "doi:10 3233 ica 240744"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to cad brep'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": "doi:10 1145 3528223 3530078"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction pointcloud'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"
      ],
      "duplicate_group": "doi:10 48550 arxiv 2205 14573"
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 39 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "\"B-rep\" reconstruction point cloud",
    "effective_query": "\"B-rep\" reconstruction point cloud",
    "used_override_query": true,
    "query_variants": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud",
      "end-to-end parametric CAD from point cloud",
      "direct B-rep reconstruction from 3D scan"
    ],
    "planned_queries": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud"
    ],
    "fallback_topic": "End-to-end B-rep reconstruction from point clouds",
    "executed_queries": [
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD B-rep",
      "learning boundary representation from point cloud"
    ]
  }
}
```

### Message 13

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=5

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows improved focus on B-rep and CAD, but critical hard requirements remain unmet. The relevance and core-method fit are insufficient because the evidence snippets do not confirm that point clouds are the primary input for most papers. Several papers are about datasets, classification, generation from images, or annotation pipelines, not end-to-end point-cloud-to-B-rep reconstruction. Only Point2Brep and ComplexGen appear promising, but their evidence is partial and does not explicitly state point cloud as the sole input. The candidate set lacks depth of verified, on-topic papers.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, 10 candidate papers remain (though some are duplicates of the same work, e.g., ComplexGen appears twice)."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 candidates, only Point2Brep and ComplexGen appear relevant based on titles and snippets. FuS-GCN is about classification/retrieval of existing B-rep models, not reconstruction from point clouds. BrepGaussian uses multi-view images as input, not point clouds. The LLM-driven paper is about generation, not reconstruction from point clouds."
    },
    "metadata": {
      "passed": true,
      "reason": "Each candidate has title, source, year/date, and URL. Author lists are present."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user's explicit constraint of 'point clouds as input' is not satisfied for many papers. BrepGaussian uses multi-view images. FuS-GCN uses existing B-rep models. The dataset paper and annotation pipeline paper are not about reconstruction pipelines. The LLM-driven paper is about generation, not reconstruction from sensor data."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers (Point2Brep, ComplexGen) are plausible core candidates based on titles and snippets, but their evidence is partial and does not explicitly confirm point cloud as the input. At least 3 verified core candidates are required. Other papers are clearly not core (dataset, classification, image-based, annotation)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2022-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence hole: the retrieval did not verify the input modality for each candidate. The set is missing known works like 'P2CADNet' (from the previous retrieval) which explicitly mentions point cloud input. The search appears to have over-prioritized the term 'B-rep' without ensuring 'point cloud' is in the evidence."
    }
  },
  "key_risks": ["The evidence snippets are too vague to confirm the input/output pipeline. Without full abstract inspection, we cannot be sure which papers truly meet the strict criteria.", "The retrieval may have excluded relevant papers that use 'parametric CAD' instead of 'B-rep' in the title/abstract.", "If the writer proceeds, they might incorrectly include dataset or image-based papers as core reconstruction methods."],
  "next_actions": ["For each candidate marked as core_candidate=true, retrieve the full abstract (or at least a longer snippet) to explicitly check for phrases like 'from point cloud', 'point cloud as input', 'scan data', '3D points'. Exclude papers where input is images, meshes, voxels, or existing CAD models.", "Re-include 'P2CADNet' from the previous retrieval if its abstract confirms point cloud input and B-rep output.", "Execute a new query that explicitly combines both terms: '\"point cloud\" \"B-rep\" reconstruction' and '\"point cloud\" \"boundary representation\" reconstruction'.", "Search in specific venues known for CAD reconstruction: ACM Transactions on Graphics (TOG), Computer-Aided Design, IEEE CVPR/ICCV/ECCV proceedings, using their digital libraries if accessible.", "If after verification the number of true core papers is still below 3, acknowledge this as a finding and prepare to report on the limited set, explicitly stating the strict criteria resulted in a small frontier."]
}
```

### Message 14

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal is to identify frontier research (2022–2026) where the **primary task** is an end-to-end pipeline that takes **point clouds as input** and directly outputs **B-rep (boundary representation)** as the final representation. The search strictly excludes works focused on subproblems (e.g., segmentation, fitting), intermediate representations (e.g., mesh, voxel), downstream applications, or alternative tasks (e.g., generation from images, classification of existing B-reps).

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv using refined queries targeting the intersection of "point cloud," "B-rep," and "reconstruction." Initial broad queries yielded many off-topic results (e.g., SLAM, robotics, point cloud registration). Subsequent queries were narrowed to phrases like `"B-rep" reconstruction point cloud` and `point cloud to CAD B-rep`. Despite these efforts, the retrieval process did not yield a sufficient number of papers that could be verified as meeting all strict criteria, particularly the confirmation of point cloud as the primary input.

## Candidate Papers
The search did not clear the quality bar. After two retrieval and review cycles, an insufficient number of papers were verified to satisfy the strict end-to-end, point-cloud-to-B-rep requirement. Below is a split of the findings.

### Verified Candidates
*No papers were fully verified.* The evidence snippets available were partial and did not explicitly confirm the required input/output pipeline for any candidate.

### Unverified Leads
The following papers have titles suggesting relevance but lack verified evidence confirming point cloud as the primary input and B-rep as the direct, final output. They are presented as potential leads for follow-up investigation, not as recommendations.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title strongly suggests relevance. The abstract snippet mentions "reconstructing accurate boundary representations (B-reps) from unstructured point clouds," but the full context and methodology are unverified.
*   **ComplexGen / ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)** – Presents a method for B-rep reconstruction. The abstract discusses reconstructing CAD models in B-rep, but the specified input ("original shapes, including point clouds...") is broad, and it is unclear if point clouds are the primary focus.
*   **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds (2023)** – From the first retrieval round. The title explicitly mentions point clouds. The abstract suggests an end-to-end network for featured CAD models, making it a promising lead, but full verification is needed.

## Notes and Gaps
*   **Nascent Field:** The strict criteria define a highly specialized research niche. The low yield suggests that truly end-to-end point-cloud-to-B-rep reconstruction is a frontier area with limited published work.
*   **Evidence Gap:** The primary gap was the inability to verify the core input/output pipeline from available abstract snippets. Many papers use "B-rep" or "CAD" but do not specify point clouds as the input in the retrieved evidence.
*   **Off-Topic Retrievals:** Searches frequently returned papers on related but excluded topics, such as B-rep segmentation (BRepGAT), image-to-CAD (BrepGaussian), dataset creation, and annotation pipelines.
*   **Venue Focus:** A targeted search within specific computer vision (CVPR, ICCV), graphics (SIGGRAPH), and CAD journal/conference proceedings may be necessary to find relevant work.

## Recommended Next Steps
1.  **Manual Verification:** For the leads above (Point2Brep, ComplexGen, P2CADNet), manually inspect the full paper to definitively confirm if point cloud is the primary input and B-rep is the final output.
2.  **Venue-Specific Search:** Conduct a focused search within the proceedings of key venues (ACM TOG, Computer-Aided Design, CVPR, ICCV) using advanced search tools.
3.  **Broaden Terminology:** Consider searching for synonyms like "parametric CAD reconstruction from scan" or "boundary representation recovery from 3D points," while manually filtering for the required pipeline.
4.  **Adjust Scope:** If the strict criteria prove too limiting, consider defining a broader scope that includes hybrid methods or pipelines where B-rep is a key, explicit output stage from point cloud data.

TERMINATE
```
