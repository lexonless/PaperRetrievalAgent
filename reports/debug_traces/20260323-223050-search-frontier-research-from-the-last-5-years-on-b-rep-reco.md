# Paper Search Debug Trace

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T22:30:50
**Stop Reason:** Text 'TERMINATE' mentioned

## Run Summary

- Stop reason: `Text 'TERMINATE' mentioned`
- Total messages: `12`
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
  "user_intent": "Identify frontier research (2022-2026) on converting point clouds to CAD/B-rep models, focusing on parametric surface reconstruction, topology recovery, and geometry-constrained modeling, to survey method categories, recent trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-23",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "point-cloud-to-CAD/B-rep methods",
    "parametric surface reconstruction",
    "topology recovery",
    "geometry-constrained modeling"
  ],
  "exclude_areas": [
    "mesh-only reconstruction without B-rep/CAD output",
    "pure mesh generation",
    "non-parametric surface reconstruction"
  ],
  "core_concepts": [
    "B-rep reconstruction from point clouds",
    "point cloud to CAD",
    "parametric surface reconstruction"
  ],
  "related_terms": [
    "CAD from scans",
    "reverse engineering",
    "geometric modeling",
    "solid reconstruction",
    "feature recovery"
  ],
  "core_signals": [
    "B-rep",
    "boundary representation",
    "CAD model",
    "parametric surfaces",
    "topology recovery",
    "feature extraction",
    "reverse engineering"
  ],
  "supporting_signals": [
    "point cloud",
    "scan-to-CAD",
    "geometry constraints",
    "primitive fitting",
    "surface fitting",
    "CSG",
    "feature recognition",
    "modeling from point clouds"
  ],
  "negative_signals": [
    "mesh reconstruction",
    "mesh generation",
    "surface mesh",
    "triangulation",
    "non-parametric",
    "implicit surface",
    "NeRF",
    "3D deep learning without CAD output"
  ],
  "query_variants": [
    "point cloud to B-rep reconstruction",
    "CAD reconstruction from point clouds",
    "parametric surface fitting point cloud",
    "topology recovery point cloud CAD"
  ],
  "source_specific_queries": {
    "DBLP": [
      "point cloud B-rep reconstruction",
      "CAD from point clouds",
      "parametric surface reconstruction point cloud"
    ]
  },
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds",
      "reason": "Directly targets the core concept of boundary representation reconstruction.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    },
    {
      "query": "point cloud to CAD parametric surface reconstruction",
      "reason": "Emphasizes the CAD output and parametric surface methods, aligning with focus areas.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    },
    {
      "query": "topology recovery point cloud reverse engineering",
      "reason": "Captures the topology recovery and reverse engineering aspects critical for B-rep/CAD models.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    }
  ],
  "assumptions": [
    "The user seeks a survey of recent advanced methods, not a comprehensive historical review. Papers from 2022-2026 are prioritized. 'Frontier research' implies state-of-the-art or novel approaches published in top venues (e.g., SIGGRAPH, CAD, CVPR, ICCV, journals like CAD, CAGD, IEEE TVCG)."
  ],
  "success_criteria": [
    "Retrieve 5-10 highly relevant papers from 2022-2026 that explicitly address B-rep/CAD reconstruction from point clouds. Papers should cover at least one focus area (parametric surfaces, topology recovery, geometry-constrained modeling). Exclude mesh-only methods. Results should enable a summary of method categories, trends, and open challenges."
  ]
}
```

### Planner Output 7

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) on converting point clouds to CAD/B-rep models, focusing on parametric surface reconstruction, topology recovery, and geometry-constrained modeling, to survey method categories, recent trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-23",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "point-cloud-to-CAD/B-rep methods",
    "parametric surface reconstruction",
    "topology recovery",
    "geometry-constrained modeling"
  ],
  "exclude_areas": [
    "mesh-only reconstruction without B-rep/CAD output",
    "pure mesh generation",
    "non-parametric surface reconstruction",
    "point cloud registration without CAD output",
    "CAD datasets without reconstruction methods"
  ],
  "core_concepts": [
    "B-rep reconstruction from point clouds",
    "point cloud to CAD",
    "parametric surface reconstruction"
  ],
  "related_terms": [
    "CAD from scans",
    "reverse engineering",
    "geometric modeling",
    "solid reconstruction",
    "feature recovery",
    "scan-to-CAD"
  ],
  "core_signals": [
    "B-rep",
    "boundary representation",
    "CAD model",
    "parametric surfaces",
    "topology recovery",
    "feature extraction",
    "reverse engineering",
    "primitive fitting"
  ],
  "supporting_signals": [
    "point cloud",
    "scan-to-CAD",
    "geometry constraints",
    "surface fitting",
    "CSG",
    "feature recognition",
    "modeling from point clouds",
    "Voronoi",
    "chain complex"
  ],
  "negative_signals": [
    "mesh reconstruction",
    "mesh generation",
    "surface mesh",
    "triangulation",
    "non-parametric",
    "implicit surface",
    "NeRF",
    "3D deep learning without CAD output",
    "point cloud registration",
    "dataset",
    "voxel"
  ],
  "query_variants": [
    "point cloud to B-rep reconstruction",
    "CAD reconstruction from point clouds",
    "parametric surface fitting point cloud",
    "topology recovery point cloud CAD",
    "B-rep reconstruction point cloud 2024",
    "scan to CAD reverse engineering"
  ],
  "source_specific_queries": {
    "DBLP": [
      "point cloud B-rep reconstruction",
      "CAD from point clouds reconstruction",
      "parametric surface reconstruction point cloud",
      "topology recovery B-rep"
    ]
  },
  "queries": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "reason": "Targets the specific boundary representation output from point clouds, using quotes to reduce noise.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    },
    {
      "query": "point cloud to CAD parametric surface fitting",
      "reason": "Focuses on parametric surface methods for CAD model generation, a key user focus area.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    },
    {
      "query": "topology recovery B-rep point cloud",
      "reason": "Directly addresses the topology recovery subtopic for B-rep models from point clouds.",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ]
    }
  ],
  "assumptions": [
    "The user seeks a survey of recent advanced methods from top venues (e.g., SIGGRAPH, CVPR, ICCV, CAD journals). Papers from 2022-2026 are prioritized. 'Frontier research' implies state-of-the-art or novel approaches. We will explicitly filter out papers that are solely about point cloud registration, datasets, or mesh reconstruction without B-rep output."
  ],
  "success_criteria": [
    "Retrieve 5-10 highly relevant, distinct papers from 2022-2026 that explicitly address B-rep/CAD reconstruction from point clouds, with clear evidence from abstracts. Papers should cover at least one focus area (parametric surfaces, topology recovery, geometry-constrained modeling). Exclude mesh-only, registration-only, and dataset-only papers. Results should enable a summary of method categories, trends, and open challenges."
  ]
}
```

## Retrieval Outputs

### Retrieval Output 5

- Summary: 10 papers from 4 sources, supported_core=9, in_range=10

```json
{
  "sources_used": [
    "Crossref / Crossref",
    "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ],
      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."
    }
  ],
  "papers": [
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
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
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
        "Xiaodong Wang"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-01-01",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "Yihang Fu",
        "Jing Li",
        "FaLai Chen"
      ],
      "relevance_note": "title core concept: B-rep reconstruction from point clouds; title core signal: B-rep; title supporting signal: point cloud; penalty: title-only metadata",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": false,
      "verification_status": "weak",
      "evidence_level": "title_only",
      "time_range_status": "in_range",
      "evidence_snippets": [],
      "duplicate_group": ""
    },
    {
      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-06-26",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "authors": [
        "O. V. Roman",
        "M. Avena",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Antonia Teresa Spano"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"
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
        "Linkun Fan"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: CAD model; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "parametric surface reconstruction",
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
      "relevance_note": "summary core signal: feature extraction; title supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "
      ],
      "duplicate_group": ""
    },
    {
      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",
      "source": "Crossref / Crossref",
      "year": 2025,
      "date": "2025-3-3",
      "url": "https://doi.org/10.20944/preprints202502.2231.v1",
      "doi": "10.20944/preprints202502.2231.v1",
      "authors": [
        "Wen Xie"
      ],
      "relevance_note": "title supporting signal: point cloud; quality boost: abstract available; penalty: no planner core signal matched",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstr"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt verification is added."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "CAD reconstruction from point clouds",
      "parametric surface fitting point cloud",
      "topology recovery point cloud CAD",
      "B-rep reconstruction from point clouds",
      "point cloud to CAD parametric surface reconstruction",
      "topology recovery point cloud reverse engineering"
    ],
    "source_query_overrides": {
      "DBLP": "point cloud B-rep reconstruction"
    }
  }
}
```

### Retrieval Output 10

- Summary: 10 papers from 2 sources, supported_core=10, in_range=10

```json
{
  "sources_used": [
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ],
      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."
    }
  ],
  "papers": [
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
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-06-07",
      "url": "http://arxiv.org/abs/2406.05261",
      "doi": "10.48550/arxiv.2406.05261",
      "authors": [
        "Yilin Liu",
        "Jiale Chen",
        "Shanshan Pan",
        "Daniel Cohen‐Or",
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning, referred to as the ``split``, followed by a ``fit`` operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep pr"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Integrating Reverse Engineering for Digital Model Reconstruction and Remanufacturing of Mechanical Components: A Systematic Review",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-11-05",
      "url": "https://doi.org/10.3390/metrology5040066",
      "doi": "10.3390/metrology5040066",
      "authors": [
        "Binoy Debnath",
        "Zahra Pourfarash",
        "Bhairavsingh Ghorpade",
        "Shivakumar Raman"
      ],
      "relevance_note": "title related term: reverse engineering; summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering (RE) is increasingly recognized as a vital methodology for reconstructing mechanical components, particularly in high-value sectors such as aerospace, transportation, and energy, where technical documentation is often missing or outdated. This study presents a systematic review that investigates the application, challenges, and future directions of RE in mechanical component re"
      ],
      "duplicate_group": ""
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
        "Daniel Cohen‐Or"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "topology-aware reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ],
      "duplicate_group": ""
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-06-26",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "authors": [
        "O. V. Roman",
        "M. Avena",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Antonia Teresa Spano"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"
      ],
      "duplicate_group": ""
    },
    {
      "title": "A robust workflow for b-rep generation from image masks",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-07-01",
      "url": "http://dx.doi.org/10.1016/j.gmod.2023.101174",
      "doi": "10.1016/j.gmod.2023.101174",
      "authors": [
        "Omar Hafez",
        "Mark M. Rashid"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; summary supporting signal: Voronoi",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "A novel approach to generating watertight, manifold boundary representations from noisy binary image masks of MRI or CT scans is presented. The method samples an input segmented image and locally approximates the material boundary. Geometric error metrics between the voxelated boundary and an approximating template surface are minimized, and boundary point/normals are correspondingly generated. Vo"
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
        "Xiaodong Wang"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt verification is added."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "\"B-rep\" reconstruction point cloud",
    "used_override_query": true,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "CAD reconstruction from point clouds",
      "parametric surface fitting point cloud",
      "topology recovery point cloud CAD",
      "B-rep reconstruction point cloud 2024",
      "scan to CAD reverse engineering",
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD parametric surface fitting",
      "topology recovery B-rep point cloud",
      "B-rep reconstruction from point clouds"
    ],
    "source_query_overrides": {
      "DBLP": "point cloud B-rep reconstruction"
    }
  }
}
```

## Review Decisions

### Review 6

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval contains several relevant papers from 2022-2026, but fails multiple hard requirements. The core-method-fit requirement is not met, as only 2 papers are verified core candidates for B-rep reconstruction from point clouds. The relevance of the top candidates is mixed, with some papers focusing on datasets, registration, or generic point cloud reconstruction rather than the specific B-rep/CAD output. Source coverage is weak, with most results from OpenAlex and a single Crossref source, lacking diversity. The evidence quality is insufficient, with many relevance notes based on keyword matching rather than substantive explanation of the method's contribution to the requested topic.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct sources (OpenAlex, Crossref) were effectively used. The planner specified multiple sources (arXiv, Crossref, OpenAlex, DBLP), but the retrieval shows limited source diversity, with most papers from OpenAlex."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After merging duplicates (e.g., ComplexGen appears 3 times), there are at least 7 distinct candidate papers."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 distinct candidates, only 2-3 are strongly aligned with B-rep reconstruction from point clouds. Papers like 'APR: Online Distant Point Cloud Registration' and 'Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm' are about point cloud registration/reconstruction but lack explicit B-rep/CAD output focus. 'A parametric and feature-based CAD dataset' is a dataset paper, not a reconstruction method."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL/DOI where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. The exclusion of 'mesh-only reconstruction' is not clearly enforced (some papers may be ambiguous). The focus on 'parametric surface reconstruction' and 'topology recovery' is not strongly evidenced in the retrieved papers' relevance notes. The time range (2022-2026) is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers are clear core candidates with verification_status 'partial' and explicit focus on B-rep reconstruction from point clouds: 'Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning' and 'ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation'. Others are either weak (title-only), about datasets, or not directly about B-rep reconstruction from point clouds. Need at least 3."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All retained papers are within 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing subtopics: no papers explicitly addressing 'geometry-constrained modeling' or robust 'topology recovery' from point clouds. Over-reliance on OpenAlex as a source. The set lacks papers from core venues like SIGGRAPH, CAD, CVPR, etc., suggesting a potential coverage gap for frontier research."
    }
  },
  "key_risks": ["Weak evidence quality: relevance notes are largely keyword matches, not substantive explanations of method contributions.", "Potential inclusion of non-core papers (point cloud registration, dataset papers) could mislead the survey.", "Lack of diversity in sources and venues may miss key state-of-the-art methods."],
  "next_actions": ["Execute targeted queries on DBLP and arXiv using specific phrases like 'point cloud to B-rep reconstruction 2024', 'parametric surface fitting point cloud CAD', 'topology recovery B-rep point cloud' to find core methods from top conferences (SIGGRAPH, CVPR, ICCV, CAD).", "Explicitly filter out papers that are solely about point cloud registration, datasets, or mesh reconstruction without B-rep output. Verify abstracts for explicit mention of B-rep/CAD model generation from point clouds.", "Prioritize retrieving papers with strong evidence (full abstracts) that clearly address at least one focus area: parametric surface reconstruction, topology recovery, or geometry-constrained modeling for B-rep output."]
}
```

### Review 11

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval shows improvement with several core B-rep reconstruction papers, but still fails key hard requirements. The core-method-fit requirement is not satisfied because many 'core candidates' are not verified as methods for B-rep reconstruction *from point clouds* specifically. The relevance requirement fails because among the top distinct papers, only 2-3 directly address the user's topic of point-cloud-to-CAD/B-rep. Source coverage remains weak with only 2 sources used. Evidence quality is poor, with relevance notes relying on keyword matching rather than substantive explanation of how each paper contributes to the requested focus areas.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct sources (OpenAlex, arXiv) were effectively used. The planner specified multiple sources including Crossref and DBLP, but they are not represented in the results. This limits diversity and may miss key papers from top venues."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After merging duplicates (e.g., Split-and-Fit appears twice, ComplexGen appears three times), there are at least 7 distinct candidate papers."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 distinct candidates, only 'Split-and-Fit', 'ComplexGen', and possibly 'HoLa' are strongly aligned with B-rep reconstruction from point clouds. 'Integrating Reverse Engineering...' is a systematic review, not a reconstruction method. 'A SEMI-AUTOMATED APPROACH...' is BIM-focused and may not emphasize parametric surface reconstruction. 'A robust workflow for b-rep generation from image masks' uses image masks, not point clouds. Need at least 3 strongly aligned papers."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL/DOI where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. The exclusion of 'mesh-only reconstruction' is addressed, but papers like 'Brep2Seq' focus on dataset and generation from multiple inputs, not specifically point cloud to B-rep. The focus on 'parametric surface reconstruction' and 'topology recovery' is not clearly evidenced in the relevance notes for most papers."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers are clear core candidates for B-rep reconstruction from point clouds with verification_status 'partial' and explicit evidence: 'Split-and-Fit' and 'ComplexGen'. 'HoLa' is about B-rep generation but evidence snippets do not mention point cloud input. 'Integrating Reverse Engineering...' is a review. 'A SEMI-AUTOMATED APPROACH...' is BIM/scan-to-BIM, not necessarily parametric CAD. Need at least 3 verified core candidates."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All retained papers are within 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing subtopics: no papers explicitly addressing 'geometry-constrained modeling' from point clouds. Limited coverage of 'topology recovery' specific methods. Over-reliance on OpenAlex; missing papers from core computer vision/graphics conferences (CVPR, ICCV, SIGGRAPH) that likely publish frontier research on this topic."
    }
  },
  "key_risks": ["Poor evidence quality: relevance notes are generic keyword matches, not explaining how each paper's method addresses parametric surfaces, topology recovery, or geometry constraints.", "Inclusion of review papers and dataset papers may dilute the focus on reconstruction methods.", "Lack of source diversity may mean missing key state-of-the-art works from specialized venues."],
  "next_actions": ["Execute queries on DBLP and Crossref specifically targeting top conference venues: use queries like 'point cloud to B-rep site:siggraph.org', 'CAD reconstruction from point clouds CVPR', 'parametric surface fitting point cloud CAD journal'.", "Manually verify abstracts of candidate papers to ensure they explicitly mention point cloud input and B-rep/CAD output. Filter out papers that are reviews, datasets, or use other input modalities (e.g., images, voxels) unless they also handle point clouds.", "Expand search to include specific method names from known literature (e.g., 'Point2CAD', 'Scan2CAD', 'BRepNet') and related terms like 'primitive fitting point cloud', 'CSG reconstruction from points' to capture geometry-constrained modeling approaches."]
}
```

## Tool Activity

### Tool Event 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_nbTq379E2lUmbNNxblbGBwko', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref / Crossref",\n    "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex",\n        "DBLP"\n      ],\n      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-01-01",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "title core concept: B-rep reconstruction from point clouds; title core signal: B-rep; title supporting signal: point cloud; penalty: title-only metadata",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": false,\n      "verification_status": "weak",\n      "evidence_level": "title_only",\n      "time_range_status": "in_range",\n      "evidence_snippets": [],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-06-26",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "authors": [\n        "O. V. Roman",\n        "M. Avena",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Antonia Teresa Spano"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: CAD model; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",\n      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n      "year": 2023,\n      "date": "2023-8",\n      "url": "https://doi.org/10.24963/ijcai.2023/134",\n      "doi": "10.24963/ijcai.2023/134",\n      "authors": [\n        "Quan Liu",\n        "Yunsong Zhou",\n        "Hongzi Zhu",\n        "Shan Chang",\n        "Minyi Guo"\n      ],\n      "relevance_note": "summary core signal: feature extraction; title supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2025,\n      "date": "2025-3-3",\n      "url": "https://doi.org/10.20944/preprints202502.2231.v1",\n      "doi": "10.20944/preprints202502.2231.v1",\n      "authors": [\n        "Wen Xie"\n      ],\n      "relevance_note": "title supporting signal: point cloud; quality boost: abstract available; penalty: no planner core signal matched",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstr"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt verification is added."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "CAD reconstruction from point clouds",\n      "parametric surface fitting point cloud",\n      "topology recovery point cloud CAD",\n      "B-rep reconstruction from point clouds",\n      "point cloud to CAD parametric surface reconstruction",\n      "topology recovery point cloud reverse engineering"\n    ],\n    "source_query_overrides": {\n      "DBLP": "point cloud B-rep reconstruction"\n    }\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_nbTq379E2lUmbNNxblbGBwko' is_error=False
```

### Tool Event 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_d59m3dke0H0aJ1sHiMfhAxJ3', arguments='{"top_k": 10, "max_results_per_source": 25, "query": "\\"B-rep\\" reconstruction point cloud"}', name='retrieve_candidates_from_plan')
```

### Tool Event 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"B-rep\\" reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex",\n        "DBLP"\n      ],\n      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-06-07",\n      "url": "http://arxiv.org/abs/2406.05261",\n      "doi": "10.48550/arxiv.2406.05261",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning, referred to as the ``split``, followed by a ``fit`` operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep pr"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Integrating Reverse Engineering for Digital Model Reconstruction and Remanufacturing of Mechanical Components: A Systematic Review",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-11-05",\n      "url": "https://doi.org/10.3390/metrology5040066",\n      "doi": "10.3390/metrology5040066",\n      "authors": [\n        "Binoy Debnath",\n        "Zahra Pourfarash",\n        "Bhairavsingh Ghorpade",\n        "Shivakumar Raman"\n      ],\n      "relevance_note": "title related term: reverse engineering; summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering (RE) is increasingly recognized as a vital methodology for reconstructing mechanical components, particularly in high-value sectors such as aerospace, transportation, and energy, where technical documentation is often missing or outdated. This study presents a systematic review that investigates the application, challenges, and future directions of RE in mechanical component re"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "topology-aware reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-06-26",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "authors": [\n        "O. V. Roman",\n        "M. Avena",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Antonia Teresa Spano"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A robust workflow for b-rep generation from image masks",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-01",\n      "url": "http://dx.doi.org/10.1016/j.gmod.2023.101174",\n      "doi": "10.1016/j.gmod.2023.101174",\n      "authors": [\n        "Omar Hafez",\n        "Mark M. Rashid"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; summary supporting signal: Voronoi",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "A novel approach to generating watertight, manifold boundary representations from noisy binary image masks of MRI or CT scans is presented. The method samples an input segmented image and locally approximates the material boundary. Geometric error metrics between the voxelated boundary and an approximating template surface are minimized, and boundary point/normals are correspondingly generated. Vo"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt verification is added."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "\\"B-rep\\" reconstruction point cloud",\n    "used_override_query": true,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "CAD reconstruction from point clouds",\n      "parametric surface fitting point cloud",\n      "topology recovery point cloud CAD",\n      "B-rep reconstruction point cloud 2024",\n      "scan to CAD reverse engineering",\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD parametric surface fitting",\n      "topology recovery B-rep point cloud",\n      "B-rep reconstruction from point clouds"\n    ],\n    "source_query_overrides": {\n      "DBLP": "point cloud B-rep reconstruction"\n    }\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_d59m3dke0H0aJ1sHiMfhAxJ3' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search frontier research from the last 5 years on B-rep reconstruction from point clouds.

```text
Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.

[Runtime Search Context]
Today's date for this run is 2026-03-23.
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
  "user_intent": "Identify frontier research (2022-2026) on converting point clouds to CAD/B-rep models, focusing on parametric surface reconstruction, topology recovery, and geometry-constrained modeling, to survey method categories, recent trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-23",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["point-cloud-to-CAD/B-rep methods", "parametric surface reconstruction", "topology recovery", "geometry-constrained modeling"],
  "exclude_areas": ["mesh-only reconstruction without B-rep/CAD output", "pure mesh generation", "non-parametric surface reconstruction"],
  "core_concepts": ["B-rep reconstruction from point clouds", "point cloud to CAD", "parametric surface reconstruction"],
  "related_terms": ["CAD from scans", "reverse engineering", "geometric modeling", "solid reconstruction", "feature recovery"],
  "core_signals": ["B-rep", "boundary representation", "CAD model", "parametric surfaces", "topology recovery", "feature extraction", "reverse engineering"],
  "supporting_signals": ["point cloud", "scan-to-CAD", "geometry constraints", "primitive fitting", "surface fitting", "CSG", "feature recognition", "modeling from point clouds"],
  "negative_signals": ["mesh reconstruction", "mesh generation", "surface mesh", "triangulation", "non-parametric", "implicit surface", "NeRF", "3D deep learning without CAD output"],
  "query_variants": ["point cloud to B-rep reconstruction", "CAD reconstruction from point clouds", "parametric surface fitting point cloud", "topology recovery point cloud CAD"],
  "source_specific_queries": {
    "DBLP": ["point cloud B-rep reconstruction", "CAD from point clouds", "parametric surface reconstruction point cloud"]
  },
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds",
      "reason": "Directly targets the core concept of boundary representation reconstruction.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    },
    {
      "query": "point cloud to CAD parametric surface reconstruction",
      "reason": "Emphasizes the CAD output and parametric surface methods, aligning with focus areas.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    },
    {
      "query": "topology recovery point cloud reverse engineering",
      "reason": "Captures the topology recovery and reverse engineering aspects critical for B-rep/CAD models.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    }
  ],
  "assumptions": ["The user seeks a survey of recent advanced methods, not a comprehensive historical review. Papers from 2022-2026 are prioritized. 'Frontier research' implies state-of-the-art or novel approaches published in top venues (e.g., SIGGRAPH, CAD, CVPR, ICCV, journals like CAD, CAGD, IEEE TVCG)."],
  "success_criteria": ["Retrieve 5-10 highly relevant papers from 2022-2026 that explicitly address B-rep/CAD reconstruction from point clouds. Papers should cover at least one focus area (parametric surfaces, topology recovery, geometry-constrained modeling). Exclude mesh-only methods. Results should enable a summary of method categories, trends, and open challenges."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_nbTq379E2lUmbNNxblbGBwko', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref / Crossref",\n    "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex",\n        "DBLP"\n      ],\n      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "OpenAlex",\n      "year": 2026,\n      "date": "2026-01-01",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "Yihang Fu",\n        "Jing Li",\n        "FaLai Chen"\n      ],\n      "relevance_note": "title core concept: B-rep reconstruction from point clouds; title core signal: B-rep; title supporting signal: point cloud; penalty: title-only metadata",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": false,\n      "verification_status": "weak",\n      "evidence_level": "title_only",\n      "time_range_status": "in_range",\n      "evidence_snippets": [],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-06-26",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "authors": [\n        "O. V. Roman",\n        "M. Avena",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Antonia Teresa Spano"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A parametric and feature-based CAD dataset to support human-computer interaction for advanced 3D shape learning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-09-03",\n      "url": "https://doi.org/10.3233/ica-240744",\n      "doi": "10.3233/ica-240744",\n      "authors": [\n        "Rubin Fan",\n        "Fazhi He",\n        "Yuxin Liu",\n        "Yupeng Song",\n        "Linkun Fan"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: CAD model; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "3D shape learning is an important research topic in computer vision, in which the datasets play a critical role. However, most of the existing 3D datasets use voxels, point clouds, mesh, and B-rep, which are not parametric and feature-based. Thus they can not support the generation of real-world engineering computer-aided design (CAD) models with complicated shape features. Furthermore, they are b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "APR: Online Distant Point Cloud Registration through Aggregated Point Cloud Reconstruction",\n      "source": "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",\n      "year": 2023,\n      "date": "2023-8",\n      "url": "https://doi.org/10.24963/ijcai.2023/134",\n      "doi": "10.24963/ijcai.2023/134",\n      "authors": [\n        "Quan Liu",\n        "Yunsong Zhou",\n        "Hongzi Zhu",\n        "Shan Chang",\n        "Minyi Guo"\n      ],\n      "relevance_note": "summary core signal: feature extraction; title supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2025,\n      "date": "2025-3-3",\n      "url": "https://doi.org/10.20944/preprints202502.2231.v1",\n      "doi": "10.20944/preprints202502.2231.v1",\n      "authors": [\n        "Wen Xie"\n      ],\n      "relevance_note": "title supporting signal: point cloud; quality boost: abstract available; penalty: no planner core signal matched",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstr"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt verification is added."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "point cloud to B-rep reconstruction",\n    "used_override_query": false,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "CAD reconstruction from point clouds",\n      "parametric surface fitting point cloud",\n      "topology recovery point cloud CAD",\n      "B-rep reconstruction from point clouds",\n      "point cloud to CAD parametric surface reconstruction",\n      "topology recovery point cloud reverse engineering"\n    ],\n    "source_query_overrides": {\n      "DBLP": "point cloud B-rep reconstruction"\n    }\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_nbTq379E2lUmbNNxblbGBwko' is_error=False
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Structured retrieval output: papers=10, sources=4, supported_core=9, in_range=10

```text
{
  "sources_used": [
    "Crossref / Crossref",
    "Crossref / Proceedings of the Thirty-Second International Joint Conference on Artificial Intelligence",
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "point cloud to B-rep reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ],
      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."
    }
  ],
  "papers": [
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
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
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
        "Xiaodong Wang"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "source": "OpenAlex",
      "year": 2026,
      "date": "2026-01-01",
      "url": "https://doi.org/10.2139/ssrn.6172545",
      "doi": "10.2139/ssrn.6172545",
      "authors": [
        "Yihang Fu",
        "Jing Li",
        "FaLai Chen"
      ],
      "relevance_note": "title core concept: B-rep reconstruction from point clouds; title core signal: B-rep; title supporting signal: point cloud; penalty: title-only metadata",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": false,
      "verification_status": "weak",
      "evidence_level": "title_only",
      "time_range_status": "in_range",
      "evidence_snippets": [],
      "duplicate_group": ""
    },
    {
      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-06-26",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "authors": [
        "O. V. Roman",
        "M. Avena",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Antonia Teresa Spano"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"
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
        "Linkun Fan"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: CAD model; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "parametric surface reconstruction",
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
      "relevance_note": "summary core signal: feature extraction; title supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>For many driving safety applications, it is of great importance to accurately register LiDAR point clouds generated on distant moving vehicles. However, such point clouds have extremely different point density and sensor perspective on the same object, making registration on such point clouds very hard. In this paper, we propose a novel feature extraction framework, called APR, for online "
      ],
      "duplicate_group": ""
    },
    {
      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",
      "source": "Crossref / Crossref",
      "year": 2025,
      "date": "2025-3-3",
      "url": "https://doi.org/10.20944/preprints202502.2231.v1",
      "doi": "10.20944/preprints202502.2231.v1",
      "authors": [
        "Wen Xie"
      ],
      "relevance_note": "title supporting signal: point cloud; quality boost: abstract available; penalty: no planner core signal matched",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstr"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt verification is added."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "point cloud to B-rep reconstruction",
    "used_override_query": false,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "CAD reconstruction from point clouds",
      "parametric surface fitting point cloud",
      "topology recovery point cloud CAD",
      "B-rep reconstruction from point clouds",
      "point cloud to CAD parametric surface reconstruction",
      "topology recovery point cloud reverse engineering"
    ],
    "source_query_overrides": {
      "DBLP": "point cloud B-rep reconstruction"
    }
  }
}
```

### Message 6

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=5

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval contains several relevant papers from 2022-2026, but fails multiple hard requirements. The core-method-fit requirement is not met, as only 2 papers are verified core candidates for B-rep reconstruction from point clouds. The relevance of the top candidates is mixed, with some papers focusing on datasets, registration, or generic point cloud reconstruction rather than the specific B-rep/CAD output. Source coverage is weak, with most results from OpenAlex and a single Crossref source, lacking diversity. The evidence quality is insufficient, with many relevance notes based on keyword matching rather than substantive explanation of the method's contribution to the requested topic.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct sources (OpenAlex, Crossref) were effectively used. The planner specified multiple sources (arXiv, Crossref, OpenAlex, DBLP), but the retrieval shows limited source diversity, with most papers from OpenAlex."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After merging duplicates (e.g., ComplexGen appears 3 times), there are at least 7 distinct candidate papers."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 distinct candidates, only 2-3 are strongly aligned with B-rep reconstruction from point clouds. Papers like 'APR: Online Distant Point Cloud Registration' and 'Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm' are about point cloud registration/reconstruction but lack explicit B-rep/CAD output focus. 'A parametric and feature-based CAD dataset' is a dataset paper, not a reconstruction method."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL/DOI where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. The exclusion of 'mesh-only reconstruction' is not clearly enforced (some papers may be ambiguous). The focus on 'parametric surface reconstruction' and 'topology recovery' is not strongly evidenced in the retrieved papers' relevance notes. The time range (2022-2026) is respected."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers are clear core candidates with verification_status 'partial' and explicit focus on B-rep reconstruction from point clouds: 'Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning' and 'ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation'. Others are either weak (title-only), about datasets, or not directly about B-rep reconstruction from point clouds. Need at least 3."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All retained papers are within 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing subtopics: no papers explicitly addressing 'geometry-constrained modeling' or robust 'topology recovery' from point clouds. Over-reliance on OpenAlex as a source. The set lacks papers from core venues like SIGGRAPH, CAD, CVPR, etc., suggesting a potential coverage gap for frontier research."
    }
  },
  "key_risks": ["Weak evidence quality: relevance notes are largely keyword matches, not substantive explanations of method contributions.", "Potential inclusion of non-core papers (point cloud registration, dataset papers) could mislead the survey.", "Lack of diversity in sources and venues may miss key state-of-the-art methods."],
  "next_actions": ["Execute targeted queries on DBLP and arXiv using specific phrases like 'point cloud to B-rep reconstruction 2024', 'parametric surface fitting point cloud CAD', 'topology recovery B-rep point cloud' to find core methods from top conferences (SIGGRAPH, CVPR, ICCV, CAD).", "Explicitly filter out papers that are solely about point cloud registration, datasets, or mesh reconstruction without B-rep output. Verify abstracts for explicit mention of B-rep/CAD model generation from point clouds.", "Prioritize retrieving papers with strong evidence (full abstracts) that clearly address at least one focus area: parametric surface reconstruction, topology recovery, or geometry-constrained modeling for B-rep output."]
}
```

### Message 7

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3, years=2022-2026

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) on converting point clouds to CAD/B-rep models, focusing on parametric surface reconstruction, topology recovery, and geometry-constrained modeling, to survey method categories, recent trends, and open challenges.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-23",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["point-cloud-to-CAD/B-rep methods", "parametric surface reconstruction", "topology recovery", "geometry-constrained modeling"],
  "exclude_areas": ["mesh-only reconstruction without B-rep/CAD output", "pure mesh generation", "non-parametric surface reconstruction", "point cloud registration without CAD output", "CAD datasets without reconstruction methods"],
  "core_concepts": ["B-rep reconstruction from point clouds", "point cloud to CAD", "parametric surface reconstruction"],
  "related_terms": ["CAD from scans", "reverse engineering", "geometric modeling", "solid reconstruction", "feature recovery", "scan-to-CAD"],
  "core_signals": ["B-rep", "boundary representation", "CAD model", "parametric surfaces", "topology recovery", "feature extraction", "reverse engineering", "primitive fitting"],
  "supporting_signals": ["point cloud", "scan-to-CAD", "geometry constraints", "surface fitting", "CSG", "feature recognition", "modeling from point clouds", "Voronoi", "chain complex"],
  "negative_signals": ["mesh reconstruction", "mesh generation", "surface mesh", "triangulation", "non-parametric", "implicit surface", "NeRF", "3D deep learning without CAD output", "point cloud registration", "dataset", "voxel"],
  "query_variants": ["point cloud to B-rep reconstruction", "CAD reconstruction from point clouds", "parametric surface fitting point cloud", "topology recovery point cloud CAD", "B-rep reconstruction point cloud 2024", "scan to CAD reverse engineering"],
  "source_specific_queries": {
    "DBLP": ["point cloud B-rep reconstruction", "CAD from point clouds reconstruction", "parametric surface reconstruction point cloud", "topology recovery B-rep"]
  },
  "queries": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "reason": "Targets the specific boundary representation output from point clouds, using quotes to reduce noise.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    },
    {
      "query": "point cloud to CAD parametric surface fitting",
      "reason": "Focuses on parametric surface methods for CAD model generation, a key user focus area.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    },
    {
      "query": "topology recovery B-rep point cloud",
      "reason": "Directly addresses the topology recovery subtopic for B-rep models from point clouds.",
      "sources": ["arXiv", "Crossref", "OpenAlex", "DBLP"]
    }
  ],
  "assumptions": ["The user seeks a survey of recent advanced methods from top venues (e.g., SIGGRAPH, CVPR, ICCV, CAD journals). Papers from 2022-2026 are prioritized. 'Frontier research' implies state-of-the-art or novel approaches. We will explicitly filter out papers that are solely about point cloud registration, datasets, or mesh reconstruction without B-rep output."],
  "success_criteria": ["Retrieve 5-10 highly relevant, distinct papers from 2022-2026 that explicitly address B-rep/CAD reconstruction from point clouds, with clear evidence from abstracts. Papers should cover at least one focus area (parametric surfaces, topology recovery, geometry-constrained modeling). Exclude mesh-only, registration-only, and dataset-only papers. Results should enable a summary of method categories, trends, and open challenges."]
}
```

### Message 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_d59m3dke0H0aJ1sHiMfhAxJ3', arguments='{"top_k": 10, "max_results_per_source": 25, "query": "\\"B-rep\\" reconstruction point cloud"}', name='retrieve_candidates_from_plan')
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "\\"B-rep\\" reconstruction point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex",\n        "DBLP"\n      ],\n      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658155",\n      "doi": "10.1145/3658155",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \\"split\\", followed by a \\"fit\\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-06-07",\n      "url": "http://arxiv.org/abs/2406.05261",\n      "doi": "10.48550/arxiv.2406.05261",\n      "authors": [\n        "Yilin Liu",\n        "Jiale Chen",\n        "Shanshan Pan",\n        "Daniel Cohen‐Or",\n        "Hao Zhang"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",\n      "method_category": "parametric surface reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning, referred to as the ``split``, followed by a ``fit`` operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep pr"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Integrating Reverse Engineering for Digital Model Reconstruction and Remanufacturing of Mechanical Components: A Systematic Review",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-11-05",\n      "url": "https://doi.org/10.3390/metrology5040066",\n      "doi": "10.3390/metrology5040066",\n      "authors": [\n        "Binoy Debnath",\n        "Zahra Pourfarash",\n        "Bhairavsingh Ghorpade",\n        "Shivakumar Raman"\n      ],\n      "relevance_note": "title related term: reverse engineering; summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering (RE) is increasingly recognized as a vital methodology for reconstructing mechanical components, particularly in high-value sectors such as aerospace, transportation, and energy, where technical documentation is often missing or outdated. This study presents a systematic review that investigates the application, challenges, and future directions of RE in mechanical component re"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-26",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "topology-aware reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "ComplexGen",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-07-01",\n      "url": "https://doi.org/10.1145/3528223.3530078",\n      "doi": "10.1145/3528223.3530078",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-06-26",\n      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",\n      "authors": [\n        "O. V. Roman",\n        "M. Avena",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Antonia Teresa Spano"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "A robust workflow for b-rep generation from image masks",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-01",\n      "url": "http://dx.doi.org/10.1016/j.gmod.2023.101174",\n      "doi": "10.1016/j.gmod.2023.101174",\n      "authors": [\n        "Omar Hafez",\n        "Mark M. Rashid"\n      ],\n      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; summary supporting signal: Voronoi",\n      "method_category": "point-cloud reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "A novel approach to generating watertight, manifold boundary representations from noisy binary image masks of MRI or CT scans is presented. The method samples an input segmented image and locally approximates the material boundary. Geometric error metrics between the voxelated boundary and an approximating template surface are minimized, and boundary point/normals are correspondingly generated. Vo"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang"\n      ],\n      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",\n      "method_category": "cad/b-rep reconstruction",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt verification is added."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "planner_primary_query": "point cloud to B-rep reconstruction",\n    "effective_query": "\\"B-rep\\" reconstruction point cloud",\n    "used_override_query": true,\n    "query_variants": [\n      "point cloud to B-rep reconstruction",\n      "CAD reconstruction from point clouds",\n      "parametric surface fitting point cloud",\n      "topology recovery point cloud CAD",\n      "B-rep reconstruction point cloud 2024",\n      "scan to CAD reverse engineering",\n      "\\"B-rep\\" reconstruction point cloud",\n      "point cloud to CAD parametric surface fitting",\n      "topology recovery B-rep point cloud",\n      "B-rep reconstruction from point clouds"\n    ],\n    "source_query_overrides": {\n      "DBLP": "point cloud B-rep reconstruction"\n    }\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_d59m3dke0H0aJ1sHiMfhAxJ3' is_error=False
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Structured retrieval output: papers=10, sources=2, supported_core=10, in_range=10

```text
{
  "sources_used": [
    "OpenAlex",
    "arXiv"
  ],
  "queries_executed": [
    {
      "query": "\"B-rep\" reconstruction point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex",
        "DBLP"
      ],
      "notes": "Derived from the latest planner payload and converted from ranked retrieval candidates."
    }
  ],
  "papers": [
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
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning , referred to as the \"split\", followed by a \"fit\" operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep primi"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-06-07",
      "url": "http://arxiv.org/abs/2406.05261",
      "doi": "10.48550/arxiv.2406.05261",
      "authors": [
        "Yilin Liu",
        "Jiale Chen",
        "Shanshan Pan",
        "Daniel Cohen‐Or",
        "Hao Zhang"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary core signal: parametric surfaces",
      "method_category": "parametric surface reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel method for acquiring boundary representations (B-Reps) of 3D CAD models which involves a two-step process: it first applies a spatial partitioning, referred to as the ``split``, followed by a ``fit`` operation to derive a single primitive within each partition. Specifically, our partitioning aims to produce the classical Voronoi diagram of the set of ground-truth (GT) B-Rep pr"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Integrating Reverse Engineering for Digital Model Reconstruction and Remanufacturing of Mechanical Components: A Systematic Review",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-11-05",
      "url": "https://doi.org/10.3390/metrology5040066",
      "doi": "10.3390/metrology5040066",
      "authors": [
        "Binoy Debnath",
        "Zahra Pourfarash",
        "Bhairavsingh Ghorpade",
        "Shivakumar Raman"
      ],
      "relevance_note": "title related term: reverse engineering; summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering (RE) is increasingly recognized as a vital methodology for reconstructing mechanical components, particularly in high-value sectors such as aerospace, transportation, and energy, where technical documentation is often missing or outdated. This study presents a systematic review that investigates the application, challenges, and future directions of RE in mechanical component re"
      ],
      "duplicate_group": ""
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
        "Daniel Cohen‐Or"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "topology-aware reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that"
      ],
      "duplicate_group": ""
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
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
        "Xin Tong"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. , vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We sol"
      ],
      "duplicate_group": ""
    },
    {
      "title": "A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-06-26",
      "url": "https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "doi": "10.5194/isprs-archives-xlviii-m-2-2023-1345-2023",
      "authors": [
        "O. V. Roman",
        "M. Avena",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Antonia Teresa Spano"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; quality boost: abstract available",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In the last years, the AEC (Architecture, Engineering and Construction) domain has exponentially increased the use of BIM and HBIM models for several applications, such as planning renovation and restoration, building maintenance, cost managing, or structural/energetic retrofit design. However, obtaining detailed as-built BIM models is a demanding and time-consuming process. Especially i"
      ],
      "duplicate_group": ""
    },
    {
      "title": "A robust workflow for b-rep generation from image masks",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-07-01",
      "url": "http://dx.doi.org/10.1016/j.gmod.2023.101174",
      "doi": "10.1016/j.gmod.2023.101174",
      "authors": [
        "Omar Hafez",
        "Mark M. Rashid"
      ],
      "relevance_note": "title core signal: B-rep; summary core signal: boundary representation; summary supporting signal: point cloud; summary supporting signal: Voronoi",
      "method_category": "point-cloud reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "A novel approach to generating watertight, manifold boundary representations from noisy binary image masks of MRI or CT scans is presented. The method samples an input segmented image and locally approximates the material boundary. Geometric error metrics between the voxelated boundary and an approximating template surface are minimized, and boundary point/normals are correspondingly generated. Vo"
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
        "Xiaodong Wang"
      ],
      "relevance_note": "summary core signal: B-rep; summary core signal: boundary representation; summary core signal: CAD model; summary supporting signal: point cloud",
      "method_category": "cad/b-rep reconstruction",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Candidates were deduplicated by DOI, URL, or normalized title before retrieval JSON conversion."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt verification is added."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "planner_primary_query": "point cloud to B-rep reconstruction",
    "effective_query": "\"B-rep\" reconstruction point cloud",
    "used_override_query": true,
    "query_variants": [
      "point cloud to B-rep reconstruction",
      "CAD reconstruction from point clouds",
      "parametric surface fitting point cloud",
      "topology recovery point cloud CAD",
      "B-rep reconstruction point cloud 2024",
      "scan to CAD reverse engineering",
      "\"B-rep\" reconstruction point cloud",
      "point cloud to CAD parametric surface fitting",
      "topology recovery B-rep point cloud",
      "B-rep reconstruction from point clouds"
    ],
    "source_query_overrides": {
      "DBLP": "point cloud B-rep reconstruction"
    }
  }
}
```

### Message 11

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=5

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval shows improvement with several core B-rep reconstruction papers, but still fails key hard requirements. The core-method-fit requirement is not satisfied because many 'core candidates' are not verified as methods for B-rep reconstruction *from point clouds* specifically. The relevance requirement fails because among the top distinct papers, only 2-3 directly address the user's topic of point-cloud-to-CAD/B-rep. Source coverage remains weak with only 2 sources used. Evidence quality is poor, with relevance notes relying on keyword matching rather than substantive explanation of how each paper contributes to the requested focus areas.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 1,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 0
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct sources (OpenAlex, arXiv) were effectively used. The planner specified multiple sources including Crossref and DBLP, but they are not represented in the results. This limits diversity and may miss key papers from top venues."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After merging duplicates (e.g., Split-and-Fit appears twice, ComplexGen appears three times), there are at least 7 distinct candidate papers."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top 5 distinct candidates, only 'Split-and-Fit', 'ComplexGen', and possibly 'HoLa' are strongly aligned with B-rep reconstruction from point clouds. 'Integrating Reverse Engineering...' is a systematic review, not a reconstruction method. 'A SEMI-AUTOMATED APPROACH...' is BIM-focused and may not emphasize parametric surface reconstruction. 'A robust workflow for b-rep generation from image masks' uses image masks, not point clouds. Need at least 3 strongly aligned papers."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL/DOI where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. The exclusion of 'mesh-only reconstruction' is addressed, but papers like 'Brep2Seq' focus on dataset and generation from multiple inputs, not specifically point cloud to B-rep. The focus on 'parametric surface reconstruction' and 'topology recovery' is not clearly evidenced in the relevance notes for most papers."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers are clear core candidates for B-rep reconstruction from point clouds with verification_status 'partial' and explicit evidence: 'Split-and-Fit' and 'ComplexGen'. 'HoLa' is about B-rep generation but evidence snippets do not mention point cloud input. 'Integrating Reverse Engineering...' is a review. 'A SEMI-AUTOMATED APPROACH...' is BIM/scan-to-BIM, not necessarily parametric CAD. Need at least 3 verified core candidates."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All retained papers are within 2022-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing subtopics: no papers explicitly addressing 'geometry-constrained modeling' from point clouds. Limited coverage of 'topology recovery' specific methods. Over-reliance on OpenAlex; missing papers from core computer vision/graphics conferences (CVPR, ICCV, SIGGRAPH) that likely publish frontier research on this topic."
    }
  },
  "key_risks": ["Poor evidence quality: relevance notes are generic keyword matches, not explaining how each paper's method addresses parametric surfaces, topology recovery, or geometry constraints.", "Inclusion of review papers and dataset papers may dilute the focus on reconstruction methods.", "Lack of source diversity may mean missing key state-of-the-art works from specialized venues."],
  "next_actions": ["Execute queries on DBLP and Crossref specifically targeting top conference venues: use queries like 'point cloud to B-rep site:siggraph.org', 'CAD reconstruction from point clouds CVPR', 'parametric surface fitting point cloud CAD journal'.", "Manually verify abstracts of candidate papers to ensure they explicitly mention point cloud input and B-rep/CAD output. Filter out papers that are reviews, datasets, or use other input modalities (e.g., images, voxels) unless they also handle point clouds.", "Expand search to include specific method names from known literature (e.g., 'Point2CAD', 'Scan2CAD', 'BRepNet') and related terms like 'primitive fitting point cloud', 'CSG reconstruction from points' to capture geometry-constrained modeling approaches."]
}
```

### Message 12

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal was to survey frontier research (2022–2026) on converting point clouds to CAD/B-rep models. The focus areas were:
*   **Point-cloud-to-CAD/B-rep methods**: Direct conversion to editable, parametric CAD models.
*   **Parametric surface reconstruction**: Fitting analytic surfaces (planes, cylinders, etc.) to point data.
*   **Topology recovery**: Inferring the connectivity between surfaces, edges, and vertices in a B-rep.
*   **Geometry-constrained modeling**: Applying geometric regularity constraints during reconstruction.

The search explicitly excluded mesh-only reconstruction, point cloud registration, dataset papers, and methods not producing a B-rep or CAD output.

## Search Strategy
The search was conducted in two phases:
1.  **Initial Broad Search**: Used queries like "point cloud to B-rep reconstruction" across arXiv, Crossref, and OpenAlex. This retrieved several relevant papers but also included off-topic results (e.g., registration, datasets).
2.  **Targeted Refinement**: A revised search used more specific queries like `"B-rep" reconstruction point cloud` to filter noise. However, the search remained limited primarily to OpenAlex and arXiv, missing broader coverage from specialized databases like DBLP and core conference proceedings (e.g., SIGGRAPH, CVPR, CAD). This limitation impacted the final set's diversity and relevance to "frontier research."

## Candidate Papers
The final retrieval contains **7 distinct papers** after merging duplicates. The following 5 are the strongest candidates that align with the query's focus on B-rep reconstruction from point clouds. Two papers were omitted: "Integrating Reverse Engineering for Digital Model Reconstruction..." (a review paper) and "A robust workflow for b-rep generation from image masks" (uses image input, not point clouds).

| Title | Year | Source | Link | Core Contribution | Relevance Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning** | 2024 | ACM TOG (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3658155) | Introduces a two-step method: a neural network learns to partition point clouds into Voronoi cells, each fitted with a single geometric primitive (plane, cylinder, etc.) to form a B-rep. | Directly addresses **parametric surface reconstruction** from point clouds. The "split-and-fit" paradigm is a clear example of a geometry-constrained, learning-based approach to B-rep generation. |
| **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** | 2022 | SIGGRAPH (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3528223.3530078) | Frames B-rep reconstruction as the joint detection of geometric primitives (surfaces, curves) and their topological relations, modeled holistically as a chain complex. | A foundational deep learning method for **topology-aware B-rep reconstruction**. It explicitly reasons about the connectivity between fitted primitives. |
| **HoLa: B-Rep Generation using a Holistic Latent Representation** | 2025 | ACM TOG (via OpenAlex) | [DOI](https://doi.org/10.1145/3730842) | Proposes a unified latent representation that jointly encodes the continuous geometry and discrete topology of B-rep primitives for generative modeling. | While the abstract does not explicitly mention point cloud input, the method is a state-of-the-art approach for **structured B-rep generation** and is highly relevant for topology recovery research. |
| **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** | 2023 | Journal of Computational Design and Engineering | [DOI](https://doi.org/10.1093/jcde/qwae005) | Presents a large-scale B-rep dataset and a sequence-based deep learning model for CAD reconstruction from various inputs, including point clouds. | Provides a **dataset and method** for learning-based CAD reconstruction. While not exclusively for point clouds, it is a relevant resource for data-driven B-rep research. |
| **A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES** | 2023 | ISPRS Archives | [DOI](https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023) | Describes a workflow for creating BIM models (which often use B-rep) from point cloud scans, focusing on architectural elements. | An applied example of **scan-to-B-rep (BIM)** in AEC. It highlights the practical challenges of reverse engineering from real-world scans. |

## Notes and Gaps
*   **Limited Scope & Source Diversity**: The search did not effectively cover core computer vision/graphics venues (CVPR, ICCV, ECCV, CAD conferences) via databases like DBLP. Consequently, several known frontier methods from 2022-2026 may be missing.
*   **Partial Focus Area Coverage**:
    *   **Parametric Surface Reconstruction**: Partially covered by "Split-and-Fit".
    *   **Topology Recovery**: Addressed by "ComplexGen" and "HoLa".
    *   **Geometry-Constrained Modeling**: Not explicitly covered by any retrieved paper. Methods that enforce geometric constraints (e.g., parallelism, orthogonality) during point cloud fitting are absent.
*   **Evidence Quality**: Relevance assessments were based on keyword matching in abstracts rather than a deep analysis of methodological contributions to the specified focus areas.
*   **Result Set**: The final set is small (5 core papers) and includes one applied BIM paper, indicating a gap in pure CAD geometry research from point clouds.

## Recommended Next Steps
1.  **Venue-Specific Search**: Conduct targeted searches on DBLP and conference websites using queries like:
    *   `"B-rep" point cloud site:cvpr.cc`
    *   `"CAD reconstruction" point cloud venue:"SIGGRAPH"`
    *   `"primitive fitting" point cloud "B-rep"`.
2.  **Expand Methodological Keywords**: Include terms like "geometric constraint solving," "regularization," "CSG reconstruction," and "feature recognition" to capture **geometry-constrained modeling** approaches.
3.  **Snowballing**: Use the citation lists of the core papers found ("Split-and-Fit," "ComplexGen") to identify related recent work.
4.  **Verify and Deepen**: For candidate papers, move beyond abstract keyword matching to review introductions and methodologies, ensuring they specifically address point cloud input and B-rep output.

TERMINATE
```
