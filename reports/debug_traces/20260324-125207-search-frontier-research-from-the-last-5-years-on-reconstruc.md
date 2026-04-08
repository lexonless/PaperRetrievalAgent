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
**Generated At:** 2026-03-24T12:52:07
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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations as the final result, excluding work focused only on subproblems or intermediate representations.",
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
    "end-to-end methods",
    "boundary representation reconstruction"
  ],
  "exclude_areas": [
    "subproblem-only papers (e.g., segmentation, fitting)",
    "intermediate representations (e.g., mesh, CSG, implicit)",
    "auxiliary modules",
    "downstream applications",
    "alternative tasks (e.g., point cloud to mesh)"
  ],
  "fallback_queries": [
    "point cloud to boundary representation reconstruction",
    "learning-based B-rep reconstruction from scans",
    "automatic CAD model generation from point clouds"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction end-to-end",
      "reason": "Directly targets the full pipeline with B-rep as final output."
    },
    {
      "query": "learning to reconstruct boundary representation from point clouds",
      "reason": "Captures data-driven methods that output B-rep primitives and topology."
    },
    {
      "query": "direct B-rep generation from 3D point cloud data",
      "reason": "Focuses on methods where B-rep is the primary reconstructed format."
    }
  ],
  "assumptions": [
    "The field is nascent; there may be few purely end-to-end papers. Some relevant work may combine learned segmentation with geometric fitting to produce B-rep.",
    "If primary queries return sparse results, fallback queries will broaden slightly while still emphasizing B-rep reconstruction."
  ],
  "success_criteria": [
    "Retrieved papers have point cloud as input and B-rep as the explicit final output.",
    "The core contribution is the reconstruction pipeline, not a component.",
    "At least 5 highly relevant papers are identified within 2022-2026."
  ]
}
```

### Planner Output 8

- Topic: `B-rep reconstruction from point clouds (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations as the final result, excluding work focused only on subproblems or intermediate representations.",
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
    "end-to-end methods",
    "boundary representation reconstruction",
    "CAD reconstruction from scans"
  ],
  "exclude_areas": [
    "subproblem-only papers (e.g., segmentation, fitting)",
    "intermediate representations (e.g., mesh, CSG, implicit)",
    "auxiliary modules",
    "downstream applications",
    "alternative tasks (e.g., point cloud to mesh, point cloud generation, detection)"
  ],
  "fallback_queries": [
    "point cloud to CAD model reconstruction",
    "learning-based B-rep reconstruction from 3D scans",
    "automatic boundary representation generation from point clouds"
  ],
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds deep learning",
      "reason": "Directly targets learning-based methods that output boundary representations, focusing on the core task."
    },
    {
      "query": "point cloud to boundary representation CAD reconstruction",
      "reason": "Emphasizes CAD and B-rep output, likely used in geometry processing and CAD conferences."
    },
    {
      "query": "automatic CAD model reconstruction from 3D point cloud scans",
      "reason": "Broadens to CAD reconstruction while maintaining the requirement for final CAD/B-rep output."
    }
  ],
  "assumptions": [
    "The field is specialized; relevant papers may appear in venues like ACM TOG, CAD, CVPR, ICCV, SIGGRAPH. Queries must explicitly include 'B-rep' or 'boundary representation' to filter out mesh/CSG methods.",
    "If primary queries are too sparse, fallback queries will relax 'B-rep' to 'CAD model' but still require reconstruction from point clouds as the main task."
  ],
  "success_criteria": [
    "Retrieved papers explicitly mention B-rep/boundary representation as the output format.",
    "The core contribution is the reconstruction pipeline from point cloud to B-rep, not a component.",
    "At least 5 highly relevant, on-task papers are identified within 2022-2026."
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
      "query": "point cloud to B-rep reconstruction end-to-end",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning to reconstruct boundary representation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-rep generation from 3D point cloud data",
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
      "title": "Automated Generation of Geometric FE Models for Timber Structures Using 3D Point Cloud Data",
      "source": "Crossref / Buildings",
      "year": 2025,
      "date": "2025-6-24",
      "url": "https://doi.org/10.3390/buildings15132213",
      "doi": "10.3390/buildings15132213",
      "authors": [
        "Lin Chen",
        "Liufang Jiang",
        "Haibei Xiong"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Manual geometric modeling of timber structures is time-intensive and error-prone, impeding efficient structural analysis. To overcome this limitation, this study develops an automated framework for the rapid generation of 3D geometric finite element (FE) models directly from LiDAR point clouds. The methodology first employs a region-growing algorithm for component segmentation. This is fol"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction end to end'; the current evidence suggests topical relevance.",
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
      "title": "SARL: Structure-Aware Representation Learning for 3D Human Pose Estimation from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6168355",
      "doi": "10.2139/ssrn.6168355",
      "authors": [
        "Kefan Chen",
        "Yong Wang",
        "Xin Du",
        "Mengyuan Liu"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning to reconstruct brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Current research on point cloud-based 3D human pose estimation faces notable challenges in effectively modeling intrinsic point correlations and fine-grained local geometric structures. In global coordinate systems, subtle joint movements are often suppressed, especially under noise interference, which hinders accurate feature extraction. To address these limitations, we propose Structure-"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-8-25",
      "url": "https://doi.org/10.36227/techrxiv.20514681.v1",
      "doi": "10.36227/techrxiv.20514681.v1",
      "authors": [
        "Tsukasa Mizutani",
        "Takahiro Yamaguchi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Comparative Assessment of Neural Radiance Fields and 3D Gaussian Splatting for Point Cloud Generation from UAV Imagery",
      "source": "Crossref / Sensors",
      "year": 2025,
      "date": "2025-5-9",
      "url": "https://doi.org/10.3390/s25102995",
      "doi": "10.3390/s25102995",
      "authors": [
        "Muhammed Enes Atik"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Point clouds continue to be the main data source in 3D modeling studies with unmanned aerial vehicle (UAV) images. Structure-from-Motion (SfM) and MultiView Stereo (MVS) have high time costs for point cloud generation, especially in large data sets. For this reason, state-of-the-art methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have emerged as powerful alte"
      ],
      "duplicate_group": ""
    },
    {
      "title": "TLSynth: A Novel Blender Add-on for Real-Time Point Cloud Generation from 3D Models",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-12-6",
      "url": "https://doi.org/10.20944/preprints202412.0539.v1",
      "doi": "10.20944/preprints202412.0539.v1",
      "authors": [
        "Emiliano Pérez",
        "Adolfo Sánchez-Hermosell",
        "Pilar Merchán"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Point clouds are a crucial element in the process of scanning and reconstructing 3D environments, such as buildings or heritage sites. They allow for the creation of 3D models that can be used in a wide range of applications. In some cases, however, only the 3D model of an environment is available, and it is necessary to obtain point clouds with the same characteristics as those captured b"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-8-25",
      "url": "https://doi.org/10.36227/techrxiv.20514681",
      "doi": "10.36227/techrxiv.20514681",
      "authors": [
        "Tsukasa Mizutani",
        "Takahiro Yamaguchi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"
      ],
      "duplicate_group": ""
    },
    {
      "title": "DeepCurrents: Learning Implicit Representations of Shapes with Boundaries",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-01",
      "url": "https://doi.org/10.1109/cvpr52688.2022.01811",
      "doi": "10.1109/cvpr52688.2022.01811",
      "authors": [
        "D. R. Palmer",
        "Dmitriy Smirnov",
        "Stephanie Wang",
        "Albert Chern",
        "Justin Solomon"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning to reconstruct brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent techniques have been successful in reconstructing surfaces as level sets of learned functions (such as signed distance fields) parameterized by deep neural networks. Many of these methods, however, learn only closed surfaces and are unable to reconstruct shapes with boundary curves. We propose a hybrid shape representation that combines explicit boundary curves with implicit learned interio"
      ],
      "duplicate_group": ""
    },
    {
      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",
      "source": "Crossref / SAE Technical Paper Series",
      "year": 2022,
      "date": "2022-3-29",
      "url": "https://doi.org/10.4271/2022-01-0164",
      "doi": "10.4271/2022-01-0164",
      "authors": [
        "Karthik Karur",
        "Georgios Pappas",
        "Joshua Siegel",
        "Mi Zhang"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction end to end'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;div class=\"section abstract\"&gt;&lt;div class=\"htmlview paragraph\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are"
      ],
      "duplicate_group": ""
    },
    {
      "title": "AI-driven point cloud framework for predicting solder joint reliability using 3D FEA data",
      "source": "Crossref / Scientific Reports",
      "year": 2025,
      "date": "2025-7-8",
      "url": "https://doi.org/10.1038/s41598-025-06902-0",
      "doi": "10.1038/s41598-025-06902-0",
      "authors": [
        "Mohd Zubair Akhtar",
        "Maximilian Schmid",
        "Gordon Elger"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title> <jats:p> Crack propagation in solder joints remains a major challenge impacting the thermo-mechanical reliability of electronic devices, underscoring the importance of optimizing package and solder pad designs. Traditional Finite Element Analysis (FEA) techniques for predicting solder joint lifespan often rely on manual post-processing to identify high-risk region"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "point cloud to B-rep reconstruction end-to-end",
    "used_override_query": false,
    "fallback_queries": [
      "point cloud to boundary representation reconstruction",
      "learning-based B-rep reconstruction from scans",
      "automatic CAD model generation from point clouds"
    ],
    "executed_queries": [
      "point cloud to B-rep reconstruction end-to-end",
      "learning to reconstruct boundary representation from point clouds",
      "direct B-rep generation from 3D point cloud data"
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
      "query": "B-rep reconstruction from point clouds deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to boundary representation CAD reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "automatic CAD model reconstruction from 3D point cloud scans",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds deep learning'; the current evidence suggests topical relevance.",
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
      "title": "From CAD models to soft point cloud labels: An automatic annotation pipeline for cheaply supervised 3D semantic segmentation",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-02-06T20:33:16Z",
      "url": "http://arxiv.org/abs/2302.03114v3",
      "doi": "",
      "authors": [
        "Galadrielle Humblot-Renaux",
        "Simon Buus Jensen",
        "Andreas Møgelmose"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual inter"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ],
      "duplicate_group": "url:http arxiv org abs 2310 02638"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-5-2",
      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",
      "doi": "10.22541/au.171462597.77668952/v1",
      "authors": [
        "jian wang",
        "Zhenglin LI",
        "Zhijie FANG",
        "Yuan MA",
        "Binjie SHI",
        "Qingqing FAN",
        "Zhiwen WANG"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p id=\"p1\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, th"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 30 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "B-rep reconstruction from point clouds deep learning",
    "used_override_query": true,
    "fallback_queries": [
      "point cloud to CAD model reconstruction",
      "learning-based B-rep reconstruction from 3D scans",
      "automatic boundary representation generation from point clouds"
    ],
    "executed_queries": [
      "B-rep reconstruction from point clouds deep learning",
      "point cloud to boundary representation CAD reconstruction",
      "automatic CAD model reconstruction from 3D point cloud scans"
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
  "review_summary": "The retrieval output fails to meet the user's strict requirement for end-to-end point-cloud-to-B-rep reconstruction papers. Most retrieved papers are off-topic, focusing on point cloud generation, detection, human pose estimation, or FE modeling, not B-rep reconstruction. The only potential candidate (P2CADNet) lacks sufficient evidence to confirm it outputs B-rep. Hard requirements for relevance, core-method fit, and query fit are not satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
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
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, almost none are clearly aligned with the user's topic of reconstructing B-rep from point clouds. Papers are about FE model generation, human pose estimation, delamination detection, point cloud generation, and synthetic data validation. The relevance notes are generic and do not demonstrate B-rep output."
    },
    "metadata": {
      "passed": false,
      "reason": "Metadata is incomplete for core verification. Titles, years, and URLs are present, but the 'core contribution' and detailed 'relevance note' fields requested by the user are missing from the output structure. The provided 'relevance_note' is a retrieval tag, not a substantive explanation."
    },
    "query_fit": {
      "passed": false,
      "reason": "The retrieved set does not reflect the user's explicit constraints. The user demanded papers where the main task is point-cloud-to-B-rep reconstruction, excluding subproblems and intermediate representations. The current set is dominated by papers on unrelated tasks."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "After inspection, no paper has been verified as a core candidate for end-to-end B-rep reconstruction from point clouds. 'P2CADNet' mentions 'featured CAD model' but evidence does not confirm B-rep output. Other papers marked as core candidates (e.g., on FE models, point cloud generation) are not on the core task."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the resolved time range (2022-2026)."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a massive, obvious gap: the retrieval missed the core topic entirely. The field of learning-based B-rep reconstruction from point clouds (e.g., works from CVPR, SIGGRAPH, CAD conferences) is not represented. The queries may have been too narrow or misinterpreted."
    }
  },
  "key_risks": [
    "The retrieval appears to have matched keywords like 'point cloud' and 'generation' but ignored the specific 'B-rep' constraint, returning a noisy set.",
    "Without a relevant core set, any subsequent report would be misleading or empty on the requested frontier research."
  ],
  "next_actions": [
    "Revise search strategy to explicitly target the CAD/geometry processing community. Use queries like: 'B-rep reconstruction from point clouds learning', 'point cloud to boundary representation CAD', 'automatic CAD reconstruction from scans 2023', 'BREP reconstruction point cloud deep learning'.",
    "Prioritize searching in relevant venues: ACM Transactions on Graphics, Computer-Aided Design, CVPR, ICCV, SIGGRAPH, SIGGRAPH Asia.",
    "For each candidate, manually verify the abstract or introduction to confirm that the input is a point cloud and the final output is a B-rep model, not a mesh, CSG, or implicit surface.",
    "Explicitly filter out papers where 'B-rep' is not mentioned or where the output is an intermediate representation (e.g., segmentation maps, primitive fits without topology)."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has significantly improved, identifying several highly relevant papers on point-cloud-to-CAD/B-rep reconstruction (e.g., Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet). However, the output structure is missing the required 'core contribution' and detailed 'relevance note' fields specified by the user. Furthermore, the evidence for some key papers is still at the abstract level, and one paper ('From CAD Models to Soft Point Cloud Labels') is off-topic (annotation pipeline, not reconstruction). Hard requirements for metadata completeness and core-method fit are not fully satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 1,
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
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 6-7 are clearly aligned with the user's topic of reconstructing CAD/B-rep models from point clouds (e.g., Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet, Brep2Seq). The off-topic paper on annotation is an outlier."
    },
    "metadata": {
      "passed": false,
      "reason": "The user requested specific fields: 'core contribution' and 'relevance note explaining why it is truly an end-to-end point-cloud-to-B-rep reconstruction method'. The current output provides only a generic 'relevance_note' (a retrieval tag) and lacks the 'core contribution' field entirely. This is a structural failure to meet the user's explicit output format."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set largely reflects the user's constraints: papers focus on CAD/B-rep reconstruction from point clouds, with many explicitly mentioning 'end-to-end' or 'reconstruction'. The queries were well-targeted to the CAD/geometry community."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "While several papers appear to be core candidates (Point2Brep, P2CADNet, etc.), the verification status is 'partial' with evidence_level 'abstract'. The user's instruction requires the reviewer to determine core fit from metadata and evidence. The abstracts strongly suggest these are on-task, but the evidence snippets are truncated and do not conclusively prove the output is a final B-rep (vs. an intermediate representation). More complete evidence is needed for a confident 'core' designation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the resolved time range (2022-2026)."
    },
    "gaps": {
      "passed": true,
      "reason": "The retrieval now covers the core topic well, with papers representing different approaches (direct primitive prediction, sequence-based, geometry-aware). No obvious major subtopic is missing given the nascent state of the field."
    }
  },
  "key_risks": [
    "The evidence for most papers is limited to partial abstracts; full-text verification is needed to confirm the output is indeed a B-rep and not a CSG tree or other intermediate representation.",
    "The output format does not match the user's requested structure, which will hinder the subsequent report-writing step."
  ],
  "next_actions": [
    "For the top 5-7 candidate papers (especially Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet), retrieve full abstracts or introductory sections to confirm: 1) input is a point cloud, 2) final output is a B-rep or parametric CAD model, 3) the paper's primary contribution is the end-to-end reconstruction pipeline.",
    "Reformat the output to include the user-requested fields: 'core contribution' (a concise summary of the method's novelty) and a detailed 'relevance note' explicitly justifying why the paper qualifies as an end-to-end point-cloud-to-B-rep reconstruction method.",
    "Filter out the clearly off-topic paper 'From CAD Models to Soft Point Cloud Labels' (it is about annotation, not reconstruction).",
    "Ensure the final list contains 5-10 papers, prioritizing those with the strongest evidence of being on-task."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_cFVbkYZhFTZEr5qAhp6ZRI8p', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction end-to-end",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning to reconstruct boundary representation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-rep generation from 3D point cloud data",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Automated Generation of Geometric FE Models for Timber Structures Using 3D Point Cloud Data",\n      "source": "Crossref / Buildings",\n      "year": 2025,\n      "date": "2025-6-24",\n      "url": "https://doi.org/10.3390/buildings15132213",\n      "doi": "10.3390/buildings15132213",\n      "authors": [\n        "Lin Chen",\n        "Liufang Jiang",\n        "Haibei Xiong"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Manual geometric modeling of timber structures is time-intensive and error-prone, impeding efficient structural analysis. To overcome this limitation, this study develops an automated framework for the rapid generation of 3D geometric finite element (FE) models directly from LiDAR point clouds. The methodology first employs a region-growing algorithm for component segmentation. This is fol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction end to end\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "SARL: Structure-Aware Representation Learning for 3D Human Pose Estimation from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6168355",\n      "doi": "10.2139/ssrn.6168355",\n      "authors": [\n        "Kefan Chen",\n        "Yong Wang",\n        "Xin Du",\n        "Mengyuan Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning to reconstruct brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Current research on point cloud-based 3D human pose estimation faces notable challenges in effectively modeling intrinsic point correlations and fine-grained local geometric structures. In global coordinate systems, subtle joint movements are often suppressed, especially under noise interference, which hinders accurate feature extraction. To address these limitations, we propose Structure-"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-8-25",\n      "url": "https://doi.org/10.36227/techrxiv.20514681.v1",\n      "doi": "10.36227/techrxiv.20514681.v1",\n      "authors": [\n        "Tsukasa Mizutani",\n        "Takahiro Yamaguchi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Comparative Assessment of Neural Radiance Fields and 3D Gaussian Splatting for Point Cloud Generation from UAV Imagery",\n      "source": "Crossref / Sensors",\n      "year": 2025,\n      "date": "2025-5-9",\n      "url": "https://doi.org/10.3390/s25102995",\n      "doi": "10.3390/s25102995",\n      "authors": [\n        "Muhammed Enes Atik"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Point clouds continue to be the main data source in 3D modeling studies with unmanned aerial vehicle (UAV) images. Structure-from-Motion (SfM) and MultiView Stereo (MVS) have high time costs for point cloud generation, especially in large data sets. For this reason, state-of-the-art methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have emerged as powerful alte"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "TLSynth: A Novel Blender Add-on for Real-Time Point Cloud Generation from 3D Models",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-12-6",\n      "url": "https://doi.org/10.20944/preprints202412.0539.v1",\n      "doi": "10.20944/preprints202412.0539.v1",\n      "authors": [\n        "Emiliano Pérez",\n        "Adolfo Sánchez-Hermosell",\n        "Pilar Merchán"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Point clouds are a crucial element in the process of scanning and reconstructing 3D environments, such as buildings or heritage sites. They allow for the creation of 3D models that can be used in a wide range of applications. In some cases, however, only the 3D model of an environment is available, and it is necessary to obtain point clouds with the same characteristics as those captured b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-8-25",\n      "url": "https://doi.org/10.36227/techrxiv.20514681",\n      "doi": "10.36227/techrxiv.20514681",\n      "authors": [\n        "Tsukasa Mizutani",\n        "Takahiro Yamaguchi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "DeepCurrents: Learning Implicit Representations of Shapes with Boundaries",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-01",\n      "url": "https://doi.org/10.1109/cvpr52688.2022.01811",\n      "doi": "10.1109/cvpr52688.2022.01811",\n      "authors": [\n        "D. R. Palmer",\n        "Dmitriy Smirnov",\n        "Stephanie Wang",\n        "Albert Chern",\n        "Justin Solomon"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning to reconstruct brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent techniques have been successful in reconstructing surfaces as level sets of learned functions (such as signed distance fields) parameterized by deep neural networks. Many of these methods, however, learn only closed surfaces and are unable to reconstruct shapes with boundary curves. We propose a hybrid shape representation that combines explicit boundary curves with implicit learned interio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",\n      "source": "Crossref / SAE Technical Paper Series",\n      "year": 2022,\n      "date": "2022-3-29",\n      "url": "https://doi.org/10.4271/2022-01-0164",\n      "doi": "10.4271/2022-01-0164",\n      "authors": [\n        "Karthik Karur",\n        "Georgios Pappas",\n        "Joshua Siegel",\n        "Mi Zhang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction end to end\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;div class=\\"section abstract\\"&gt;&lt;div class=\\"htmlview paragraph\\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "AI-driven point cloud framework for predicting solder joint reliability using 3D FEA data",\n      "source": "Crossref / Scientific Reports",\n      "year": 2025,\n      "date": "2025-7-8",\n      "url": "https://doi.org/10.1038/s41598-025-06902-0",\n      "doi": "10.1038/s41598-025-06902-0",\n      "authors": [\n        "Mohd Zubair Akhtar",\n        "Maximilian Schmid",\n        "Gordon Elger"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title> <jats:p> Crack propagation in solder joints remains a major challenge impacting the thermo-mechanical reliability of electronic devices, underscoring the importance of optimizing package and solder pad designs. Traditional Finite Element Analysis (FEA) techniques for predicting solder joint lifespan often rely on manual post-processing to identify high-risk region"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "point cloud to B-rep reconstruction end-to-end",\n    "used_override_query": false,\n    "fallback_queries": [\n      "point cloud to boundary representation reconstruction",\n      "learning-based B-rep reconstruction from scans",\n      "automatic CAD model generation from point clouds"\n    ],\n    "executed_queries": [\n      "point cloud to B-rep reconstruction end-to-end",\n      "learning to reconstruct boundary representation from point clouds",\n      "direct B-rep generation from 3D point cloud data"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_cFVbkYZhFTZEr5qAhp6ZRI8p' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_XH9G8YAgRZIZaY4BPtzizo1e', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "B-rep reconstruction from point clouds deep learning"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep reconstruction from point clouds deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to boundary representation CAD reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "automatic CAD model reconstruction from 3D point cloud scans",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "From CAD models to soft point cloud labels: An automatic annotation pipeline for cheaply supervised 3D semantic segmentation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-06T20:33:16Z",\n      "url": "http://arxiv.org/abs/2302.03114v3",\n      "doi": "",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual inter"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": "url:http arxiv org abs 2310 02638"\n    },\n    {\n      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-10-27T15:33:51Z",\n      "url": "http://arxiv.org/abs/2510.23429v1",\n      "doi": "",\n      "authors": [\n        "Ahmet Serdar Karadeniz",\n        "Dimitrios Mallis",\n        "Danila Rukhovich",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, th"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 30 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "B-rep reconstruction from point clouds deep learning",\n    "used_override_query": true,\n    "fallback_queries": [\n      "point cloud to CAD model reconstruction",\n      "learning-based B-rep reconstruction from 3D scans",\n      "automatic boundary representation generation from point clouds"\n    ],\n    "executed_queries": [\n      "B-rep reconstruction from point clouds deep learning",\n      "point cloud to boundary representation CAD reconstruction",\n      "automatic CAD model reconstruction from 3D point cloud scans"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_XH9G8YAgRZIZaY4BPtzizo1e' is_error=False
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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations as the final result, excluding work focused only on subproblems or intermediate representations.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["direct B-rep output from point clouds", "full reconstruction pipeline", "end-to-end methods", "boundary representation reconstruction"],
  "exclude_areas": ["subproblem-only papers (e.g., segmentation, fitting)", "intermediate representations (e.g., mesh, CSG, implicit)", "auxiliary modules", "downstream applications", "alternative tasks (e.g., point cloud to mesh)"],
  "fallback_queries": ["point cloud to boundary representation reconstruction", "learning-based B-rep reconstruction from scans", "automatic CAD model generation from point clouds"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction end-to-end",
      "reason": "Directly targets the full pipeline with B-rep as final output."
    },
    {
      "query": "learning to reconstruct boundary representation from point clouds",
      "reason": "Captures data-driven methods that output B-rep primitives and topology."
    },
    {
      "query": "direct B-rep generation from 3D point cloud data",
      "reason": "Focuses on methods where B-rep is the primary reconstructed format."
    }
  ],
  "assumptions": ["The field is nascent; there may be few purely end-to-end papers. Some relevant work may combine learned segmentation with geometric fitting to produce B-rep.", "If primary queries return sparse results, fallback queries will broaden slightly while still emphasizing B-rep reconstruction."],
  "success_criteria": ["Retrieved papers have point cloud as input and B-rep as the explicit final output.", "The core contribution is the reconstruction pipeline, not a component.", "At least 5 highly relevant papers are identified within 2022-2026."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find papers on B-rep reconstruction from point clouds within the 2022-2026 timeframe.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_cFVbkYZhFTZEr5qAhp6ZRI8p', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction end-to-end",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "learning to reconstruct boundary representation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-rep generation from 3D point cloud data",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Automated Generation of Geometric FE Models for Timber Structures Using 3D Point Cloud Data",\n      "source": "Crossref / Buildings",\n      "year": 2025,\n      "date": "2025-6-24",\n      "url": "https://doi.org/10.3390/buildings15132213",\n      "doi": "10.3390/buildings15132213",\n      "authors": [\n        "Lin Chen",\n        "Liufang Jiang",\n        "Haibei Xiong"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Manual geometric modeling of timber structures is time-intensive and error-prone, impeding efficient structural analysis. To overcome this limitation, this study develops an automated framework for the rapid generation of 3D geometric finite element (FE) models directly from LiDAR point clouds. The methodology first employs a region-growing algorithm for component segmentation. This is fol"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction end to end\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "SARL: Structure-Aware Representation Learning for 3D Human Pose Estimation from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6168355",\n      "doi": "10.2139/ssrn.6168355",\n      "authors": [\n        "Kefan Chen",\n        "Yong Wang",\n        "Xin Du",\n        "Mengyuan Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning to reconstruct brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Current research on point cloud-based 3D human pose estimation faces notable challenges in effectively modeling intrinsic point correlations and fine-grained local geometric structures. In global coordinate systems, subtle joint movements are often suppressed, especially under noise interference, which hinders accurate feature extraction. To address these limitations, we propose Structure-"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-8-25",\n      "url": "https://doi.org/10.36227/techrxiv.20514681.v1",\n      "doi": "10.36227/techrxiv.20514681.v1",\n      "authors": [\n        "Tsukasa Mizutani",\n        "Takahiro Yamaguchi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Comparative Assessment of Neural Radiance Fields and 3D Gaussian Splatting for Point Cloud Generation from UAV Imagery",\n      "source": "Crossref / Sensors",\n      "year": 2025,\n      "date": "2025-5-9",\n      "url": "https://doi.org/10.3390/s25102995",\n      "doi": "10.3390/s25102995",\n      "authors": [\n        "Muhammed Enes Atik"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Point clouds continue to be the main data source in 3D modeling studies with unmanned aerial vehicle (UAV) images. Structure-from-Motion (SfM) and MultiView Stereo (MVS) have high time costs for point cloud generation, especially in large data sets. For this reason, state-of-the-art methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have emerged as powerful alte"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "TLSynth: A Novel Blender Add-on for Real-Time Point Cloud Generation from 3D Models",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-12-6",\n      "url": "https://doi.org/10.20944/preprints202412.0539.v1",\n      "doi": "10.20944/preprints202412.0539.v1",\n      "authors": [\n        "Emiliano Pérez",\n        "Adolfo Sánchez-Hermosell",\n        "Pilar Merchán"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Point clouds are a crucial element in the process of scanning and reconstructing 3D environments, such as buildings or heritage sites. They allow for the creation of 3D models that can be used in a wide range of applications. In some cases, however, only the 3D model of an environment is available, and it is necessary to obtain point clouds with the same characteristics as those captured b"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-8-25",\n      "url": "https://doi.org/10.36227/techrxiv.20514681",\n      "doi": "10.36227/techrxiv.20514681",\n      "authors": [\n        "Tsukasa Mizutani",\n        "Takahiro Yamaguchi"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "DeepCurrents: Learning Implicit Representations of Shapes with Boundaries",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-01",\n      "url": "https://doi.org/10.1109/cvpr52688.2022.01811",\n      "doi": "10.1109/cvpr52688.2022.01811",\n      "authors": [\n        "D. R. Palmer",\n        "Dmitriy Smirnov",\n        "Stephanie Wang",\n        "Albert Chern",\n        "Justin Solomon"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'learning to reconstruct brep from pointclouds\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent techniques have been successful in reconstructing surfaces as level sets of learned functions (such as signed distance fields) parameterized by deep neural networks. Many of these methods, however, learn only closed surfaces and are unable to reconstruct shapes with boundary curves. We propose a hybrid shape representation that combines explicit boundary curves with implicit learned interio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",\n      "source": "Crossref / SAE Technical Paper Series",\n      "year": 2022,\n      "date": "2022-3-29",\n      "url": "https://doi.org/10.4271/2022-01-0164",\n      "doi": "10.4271/2022-01-0164",\n      "authors": [\n        "Karthik Karur",\n        "Georgios Pappas",\n        "Joshua Siegel",\n        "Mi Zhang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep reconstruction end to end\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;div class=\\"section abstract\\"&gt;&lt;div class=\\"htmlview paragraph\\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "AI-driven point cloud framework for predicting solder joint reliability using 3D FEA data",\n      "source": "Crossref / Scientific Reports",\n      "year": 2025,\n      "date": "2025-7-8",\n      "url": "https://doi.org/10.1038/s41598-025-06902-0",\n      "doi": "10.1038/s41598-025-06902-0",\n      "authors": [\n        "Mohd Zubair Akhtar",\n        "Maximilian Schmid",\n        "Gordon Elger"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'direct brep generation from 3d pointcloud data\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title> <jats:p> Crack propagation in solder joints remains a major challenge impacting the thermo-mechanical reliability of electronic devices, underscoring the importance of optimizing package and solder pad designs. Traditional Finite Element Analysis (FEA) techniques for predicting solder joint lifespan often rely on manual post-processing to identify high-risk region"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "point cloud to B-rep reconstruction end-to-end",\n    "used_override_query": false,\n    "fallback_queries": [\n      "point cloud to boundary representation reconstruction",\n      "learning-based B-rep reconstruction from scans",\n      "automatic CAD model generation from point clouds"\n    ],\n    "executed_queries": [\n      "point cloud to B-rep reconstruction end-to-end",\n      "learning to reconstruct boundary representation from point clouds",\n      "direct B-rep generation from 3D point cloud data"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_cFVbkYZhFTZEr5qAhp6ZRI8p' is_error=False
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
      "query": "point cloud to B-rep reconstruction end-to-end",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "learning to reconstruct boundary representation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-rep generation from 3D point cloud data",
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
      "title": "Automated Generation of Geometric FE Models for Timber Structures Using 3D Point Cloud Data",
      "source": "Crossref / Buildings",
      "year": 2025,
      "date": "2025-6-24",
      "url": "https://doi.org/10.3390/buildings15132213",
      "doi": "10.3390/buildings15132213",
      "authors": [
        "Lin Chen",
        "Liufang Jiang",
        "Haibei Xiong"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Manual geometric modeling of timber structures is time-intensive and error-prone, impeding efficient structural analysis. To overcome this limitation, this study develops an automated framework for the rapid generation of 3D geometric finite element (FE) models directly from LiDAR point clouds. The methodology first employs a region-growing algorithm for component segmentation. This is fol"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction end to end'; the current evidence suggests topical relevance.",
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
      "title": "SARL: Structure-Aware Representation Learning for 3D Human Pose Estimation from Point Clouds",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6168355",
      "doi": "10.2139/ssrn.6168355",
      "authors": [
        "Kefan Chen",
        "Yong Wang",
        "Xin Du",
        "Mengyuan Liu"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning to reconstruct brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Current research on point cloud-based 3D human pose estimation faces notable challenges in effectively modeling intrinsic point correlations and fine-grained local geometric structures. In global coordinate systems, subtle joint movements are often suppressed, especially under noise interference, which hinders accurate feature extraction. To address these limitations, we propose Structure-"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-8-25",
      "url": "https://doi.org/10.36227/techrxiv.20514681.v1",
      "doi": "10.36227/techrxiv.20514681.v1",
      "authors": [
        "Tsukasa Mizutani",
        "Takahiro Yamaguchi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Comparative Assessment of Neural Radiance Fields and 3D Gaussian Splatting for Point Cloud Generation from UAV Imagery",
      "source": "Crossref / Sensors",
      "year": 2025,
      "date": "2025-5-9",
      "url": "https://doi.org/10.3390/s25102995",
      "doi": "10.3390/s25102995",
      "authors": [
        "Muhammed Enes Atik"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Point clouds continue to be the main data source in 3D modeling studies with unmanned aerial vehicle (UAV) images. Structure-from-Motion (SfM) and MultiView Stereo (MVS) have high time costs for point cloud generation, especially in large data sets. For this reason, state-of-the-art methods such as Neural Radiance Fields (NeRF) and 3D Gaussian Splatting (3DGS) have emerged as powerful alte"
      ],
      "duplicate_group": ""
    },
    {
      "title": "TLSynth: A Novel Blender Add-on for Real-Time Point Cloud Generation from 3D Models",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-12-6",
      "url": "https://doi.org/10.20944/preprints202412.0539.v1",
      "doi": "10.20944/preprints202412.0539.v1",
      "authors": [
        "Emiliano Pérez",
        "Adolfo Sánchez-Hermosell",
        "Pilar Merchán"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Point clouds are a crucial element in the process of scanning and reconstructing 3D environments, such as buildings or heritage sites. They allow for the creation of 3D models that can be used in a wide range of applications. In some cases, however, only the 3D model of an environment is available, and it is necessary to obtain point clouds with the same characteristics as those captured b"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Automatic Detection of Delamination on Tunnel Lining Surfaces from Laser 3D Point Cloud Data by 3D Features and Support Vector Machine",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-8-25",
      "url": "https://doi.org/10.36227/techrxiv.20514681",
      "doi": "10.36227/techrxiv.20514681",
      "authors": [
        "Tsukasa Mizutani",
        "Takahiro Yamaguchi"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;p&gt; A completely automatic and accurate detection algorithm for the delamination on tunnel concrete lining surfaces from laser 3D point cloud data is proposed. A Mobile Mapping System (MMS), which mounts laser sensors and a positioning system, is utilized to measure the geometry of tunnel lining surfaces highspeed. The proposed algorithm consists of 4 steps: removal of tunnel profile"
      ],
      "duplicate_group": ""
    },
    {
      "title": "DeepCurrents: Learning Implicit Representations of Shapes with Boundaries",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-01",
      "url": "https://doi.org/10.1109/cvpr52688.2022.01811",
      "doi": "10.1109/cvpr52688.2022.01811",
      "authors": [
        "D. R. Palmer",
        "Dmitriy Smirnov",
        "Stephanie Wang",
        "Albert Chern",
        "Justin Solomon"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'learning to reconstruct brep from pointclouds'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent techniques have been successful in reconstructing surfaces as level sets of learned functions (such as signed distance fields) parameterized by deep neural networks. Many of these methods, however, learn only closed surfaces and are unable to reconstruct shapes with boundary curves. We propose a hybrid shape representation that combines explicit boundary curves with implicit learned interio"
      ],
      "duplicate_group": ""
    },
    {
      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",
      "source": "Crossref / SAE Technical Paper Series",
      "year": 2022,
      "date": "2022-3-29",
      "url": "https://doi.org/10.4271/2022-01-0164",
      "doi": "10.4271/2022-01-0164",
      "authors": [
        "Karthik Karur",
        "Georgios Pappas",
        "Joshua Siegel",
        "Mi Zhang"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep reconstruction end to end'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;div class=\"section abstract\"&gt;&lt;div class=\"htmlview paragraph\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are"
      ],
      "duplicate_group": ""
    },
    {
      "title": "AI-driven point cloud framework for predicting solder joint reliability using 3D FEA data",
      "source": "Crossref / Scientific Reports",
      "year": 2025,
      "date": "2025-7-8",
      "url": "https://doi.org/10.1038/s41598-025-06902-0",
      "doi": "10.1038/s41598-025-06902-0",
      "authors": [
        "Mohd Zubair Akhtar",
        "Maximilian Schmid",
        "Gordon Elger"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'direct brep generation from 3d pointcloud data'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title> <jats:p> Crack propagation in solder joints remains a major challenge impacting the thermo-mechanical reliability of electronic devices, underscoring the importance of optimizing package and solder pad designs. Traditional Finite Element Analysis (FEA) techniques for predicting solder joint lifespan often rely on manual post-processing to identify high-risk region"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 19 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "point cloud to B-rep reconstruction end-to-end",
    "used_override_query": false,
    "fallback_queries": [
      "point cloud to boundary representation reconstruction",
      "learning-based B-rep reconstruction from scans",
      "automatic CAD model generation from point clouds"
    ],
    "executed_queries": [
      "point cloud to B-rep reconstruction end-to-end",
      "learning to reconstruct boundary representation from point clouds",
      "direct B-rep generation from 3D point cloud data"
    ],
    "fallback_used": false
  }
}
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=5

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output fails to meet the user's strict requirement for end-to-end point-cloud-to-B-rep reconstruction papers. Most retrieved papers are off-topic, focusing on point cloud generation, detection, human pose estimation, or FE modeling, not B-rep reconstruction. The only potential candidate (P2CADNet) lacks sufficient evidence to confirm it outputs B-rep. Hard requirements for relevance, core-method fit, and query fit are not satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
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
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, almost none are clearly aligned with the user's topic of reconstructing B-rep from point clouds. Papers are about FE model generation, human pose estimation, delamination detection, point cloud generation, and synthetic data validation. The relevance notes are generic and do not demonstrate B-rep output."
    },
    "metadata": {
      "passed": false,
      "reason": "Metadata is incomplete for core verification. Titles, years, and URLs are present, but the 'core contribution' and detailed 'relevance note' fields requested by the user are missing from the output structure. The provided 'relevance_note' is a retrieval tag, not a substantive explanation."
    },
    "query_fit": {
      "passed": false,
      "reason": "The retrieved set does not reflect the user's explicit constraints. The user demanded papers where the main task is point-cloud-to-B-rep reconstruction, excluding subproblems and intermediate representations. The current set is dominated by papers on unrelated tasks."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "After inspection, no paper has been verified as a core candidate for end-to-end B-rep reconstruction from point clouds. 'P2CADNet' mentions 'featured CAD model' but evidence does not confirm B-rep output. Other papers marked as core candidates (e.g., on FE models, point cloud generation) are not on the core task."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the resolved time range (2022-2026)."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a massive, obvious gap: the retrieval missed the core topic entirely. The field of learning-based B-rep reconstruction from point clouds (e.g., works from CVPR, SIGGRAPH, CAD conferences) is not represented. The queries may have been too narrow or misinterpreted."
    }
  },
  "key_risks": [
    "The retrieval appears to have matched keywords like 'point cloud' and 'generation' but ignored the specific 'B-rep' constraint, returning a noisy set.",
    "Without a relevant core set, any subsequent report would be misleading or empty on the requested frontier research."
  ],
  "next_actions": [
    "Revise search strategy to explicitly target the CAD/geometry processing community. Use queries like: 'B-rep reconstruction from point clouds learning', 'point cloud to boundary representation CAD', 'automatic CAD reconstruction from scans 2023', 'BREP reconstruction point cloud deep learning'.",
    "Prioritize searching in relevant venues: ACM Transactions on Graphics, Computer-Aided Design, CVPR, ICCV, SIGGRAPH, SIGGRAPH Asia.",
    "For each candidate, manually verify the abstract or introduction to confirm that the input is a point cloud and the final output is a B-rep model, not a mesh, CSG, or implicit surface.",
    "Explicitly filter out papers where 'B-rep' is not mentioned or where the output is an intermediate representation (e.g., segmentation maps, primitive fits without topology)."
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
  "user_intent": "Identify frontier research (2022-2026) where the primary task is an end-to-end pipeline taking point clouds as input and directly outputting B-rep representations as the final result, excluding work focused only on subproblems or intermediate representations.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["direct B-rep output from point clouds", "full reconstruction pipeline", "end-to-end methods", "boundary representation reconstruction", "CAD reconstruction from scans"],
  "exclude_areas": ["subproblem-only papers (e.g., segmentation, fitting)", "intermediate representations (e.g., mesh, CSG, implicit)", "auxiliary modules", "downstream applications", "alternative tasks (e.g., point cloud to mesh, point cloud generation, detection)"],
  "fallback_queries": ["point cloud to CAD model reconstruction", "learning-based B-rep reconstruction from 3D scans", "automatic boundary representation generation from point clouds"],
  "queries": [
    {
      "query": "B-rep reconstruction from point clouds deep learning",
      "reason": "Directly targets learning-based methods that output boundary representations, focusing on the core task."
    },
    {
      "query": "point cloud to boundary representation CAD reconstruction",
      "reason": "Emphasizes CAD and B-rep output, likely used in geometry processing and CAD conferences."
    },
    {
      "query": "automatic CAD model reconstruction from 3D point cloud scans",
      "reason": "Broadens to CAD reconstruction while maintaining the requirement for final CAD/B-rep output."
    }
  ],
  "assumptions": ["The field is specialized; relevant papers may appear in venues like ACM TOG, CAD, CVPR, ICCV, SIGGRAPH. Queries must explicitly include 'B-rep' or 'boundary representation' to filter out mesh/CSG methods.", "If primary queries are too sparse, fallback queries will relax 'B-rep' to 'CAD model' but still require reconstruction from point clouds as the main task."],
  "success_criteria": ["Retrieved papers explicitly mention B-rep/boundary representation as the output format.", "The core contribution is the reconstruction pipeline from point cloud to B-rep, not a component.", "At least 5 highly relevant, on-task papers are identified within 2022-2026."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the revised search plan with more targeted queries for B-rep reconstruction from point clouds.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_XH9G8YAgRZIZaY4BPtzizo1e', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "B-rep reconstruction from point clouds deep learning"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep reconstruction from point clouds deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "point cloud to boundary representation CAD reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "automatic CAD model reconstruction from 3D point cloud scans",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manu"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning m"\n      ],\n      "duplicate_group": "doi:10 1093 jcde qwae005"\n    },\n    {\n      "title": "From CAD models to soft point cloud labels: An automatic annotation pipeline for cheaply supervised 3D semantic segmentation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-06T20:33:16Z",\n      "url": "http://arxiv.org/abs/2302.03114v3",\n      "doi": "",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual inter"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-10-04T08:00:05Z",\n      "url": "http://arxiv.org/abs/2310.02638v1",\n      "doi": "",\n      "authors": [\n        "Zhihao Zong",\n        "Fazhi He",\n        "Rubin Fan",\n        "Yuxin Liu"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"\n      ],\n      "duplicate_group": "url:http arxiv org abs 2310 02638"\n    },\n    {\n      "title": "MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-10-27T15:33:51Z",\n      "url": "http://arxiv.org/abs/2510.23429v1",\n      "doi": "",\n      "authors": [\n        "Ahmet Serdar Karadeniz",\n        "Dimitrios Mallis",\n        "Danila Rukhovich",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-04T09:42:03Z",\n      "url": "http://arxiv.org/abs/2505.02043v3",\n      "doi": "",\n      "authors": [\n        "Xinzhu Ma",\n        "Cheng Wang",\n        "Chen Tang",\n        "Bin Wang",\n        "Shixiang Tang",\n        "Yuan Meng",\n        "Yunhong Wang",\n        "Di Huang"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'brep reconstruction from pointclouds deep learning\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": false,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Surface and Edge Detection for Primitive Fitting of Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-07-19",\n      "url": "https://doi.org/10.1145/3588432.3591522",\n      "doi": "10.1145/3588432.3591522",\n      "authors": [\n        "Yuanqi Li",\n        "Shun Liu",\n        "Xinran Yang",\n        "Jianwei Guo",\n        "Jie Guo",\n        "Yanwen Guo"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Fitting primitives for point cloud data to obtain a structural representation has been widely adopted for reverse engineering and other graphics applications. Existing segmentation-based approaches only segment primitive patches but ignore edges that indicate boundaries of primitives, leading to inaccurate and incomplete reconstruction. To fill the gap, we present a novel surface and edge detectio"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-27T16:53:16Z",\n      "url": "http://arxiv.org/abs/2402.17678v1",\n      "doi": "",\n      "authors": [\n        "Mohammad Sadil Khan",\n        "Elona Dupont",\n        "Sk Aziz Ali",\n        "Kseniya Cherenkova",\n        "Anis Kacem",\n        "Djamila Aouada"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'pointcloud to brep cad reconstruction\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"\n      ],\n      "duplicate_group": ""\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "relevance_note": "Title/evidence matched retrieval query terms around \'automatic cad model reconstruction from 3d pointcloud scans\'; the current evidence suggests topical relevance.",\n      "method_category": "unspecified",\n      "is_core_candidate": true,\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, th"\n      ],\n      "duplicate_group": ""\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 30 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or webpage evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "effective_query": "B-rep reconstruction from point clouds deep learning",\n    "used_override_query": true,\n    "fallback_queries": [\n      "point cloud to CAD model reconstruction",\n      "learning-based B-rep reconstruction from 3D scans",\n      "automatic boundary representation generation from point clouds"\n    ],\n    "executed_queries": [\n      "B-rep reconstruction from point clouds deep learning",\n      "point cloud to boundary representation CAD reconstruction",\n      "automatic CAD model reconstruction from 3D point cloud scans"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_XH9G8YAgRZIZaY4BPtzizo1e' is_error=False
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
      "query": "B-rep reconstruction from point clouds deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "point cloud to boundary representation CAD reconstruction",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "automatic CAD model reconstruction from 3D point cloud scans",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds deep learning'; the current evidence suggests topical relevance.",
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
      "title": "From CAD models to soft point cloud labels: An automatic annotation pipeline for cheaply supervised 3D semantic segmentation",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-02-06T20:33:16Z",
      "url": "http://arxiv.org/abs/2302.03114v3",
      "doi": "",
      "authors": [
        "Galadrielle Humblot-Renaux",
        "Simon Buus Jensen",
        "Andreas Møgelmose"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual inter"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet arch"
      ],
      "duplicate_group": "url:http arxiv org abs 2310 02638"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Computer-Aided Design (CAD) plays a foundational role in modern manufacturing and product development, often requiring designers to modify or build upon existing models. Converting 3D scans into parametric CAD representations--a process known as CAD reverse engineering--remains a significant challenge due to the high precision and structural complexity of CAD models. Existing deep learning-based a"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recovering CAD models from point clouds requires reconstructing their topology and sketch-based extrusion primitives. A dominant paradigm for representing sketches involves implicit neural representations such as Signed Distance Fields (SDFs). However, this indirect approach inherently struggles with precision, leading to unintended curved edges and models that are difficult to edit. In this paper"
      ],
      "duplicate_group": ""
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'brep reconstruction from pointclouds deep learning'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": false,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit param"
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
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
      "relevance_note": "Title/evidence matched retrieval query terms around 'pointcloud to brep cad reconstruction'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reverse engineering in the realm of Computer-Aided Design (CAD) has been a longstanding aspiration, though not yet entirely realized. Its primary aim is to uncover the CAD process behind a physical object given its 3D scan. We propose CAD-SIGNet, an end-to-end trainable and auto-regressive architecture to recover the design history of a CAD model represented as a sequence of sketch-and-extrusion f"
      ],
      "duplicate_group": ""
    },
    {
      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-5-2",
      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",
      "doi": "10.22541/au.171462597.77668952/v1",
      "authors": [
        "jian wang",
        "Zhenglin LI",
        "Zhijie FANG",
        "Yuan MA",
        "Binjie SHI",
        "Qingqing FAN",
        "Zhiwen WANG"
      ],
      "relevance_note": "Title/evidence matched retrieval query terms around 'automatic cad model reconstruction from 3d pointcloud scans'; the current evidence suggests topical relevance.",
      "method_category": "unspecified",
      "is_core_candidate": true,
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p id=\"p1\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, th"
      ],
      "duplicate_group": ""
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 30 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or webpage evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "effective_query": "B-rep reconstruction from point clouds deep learning",
    "used_override_query": true,
    "fallback_queries": [
      "point cloud to CAD model reconstruction",
      "learning-based B-rep reconstruction from 3D scans",
      "automatic boundary representation generation from point clouds"
    ],
    "executed_queries": [
      "B-rep reconstruction from point clouds deep learning",
      "point cloud to boundary representation CAD reconstruction",
      "automatic CAD model reconstruction from 3D point cloud scans"
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
  "review_summary": "The retrieval has significantly improved, identifying several highly relevant papers on point-cloud-to-CAD/B-rep reconstruction (e.g., Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet). However, the output structure is missing the required 'core contribution' and detailed 'relevance note' fields specified by the user. Furthermore, the evidence for some key papers is still at the abstract level, and one paper ('From CAD Models to Soft Point Cloud Labels') is off-topic (annotation pipeline, not reconstruction). Hard requirements for metadata completeness and core-method fit are not fully satisfied.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 1,
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
      "reason": "10 non-duplicate candidate papers remain after merging."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 6-7 are clearly aligned with the user's topic of reconstructing CAD/B-rep models from point clouds (e.g., Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet, Brep2Seq). The off-topic paper on annotation is an outlier."
    },
    "metadata": {
      "passed": false,
      "reason": "The user requested specific fields: 'core contribution' and 'relevance note explaining why it is truly an end-to-end point-cloud-to-B-rep reconstruction method'. The current output provides only a generic 'relevance_note' (a retrieval tag) and lacks the 'core contribution' field entirely. This is a structural failure to meet the user's explicit output format."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set largely reflects the user's constraints: papers focus on CAD/B-rep reconstruction from point clouds, with many explicitly mentioning 'end-to-end' or 'reconstruction'. The queries were well-targeted to the CAD/geometry community."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "While several papers appear to be core candidates (Point2Brep, P2CADNet, etc.), the verification status is 'partial' with evidence_level 'abstract'. The user's instruction requires the reviewer to determine core fit from metadata and evidence. The abstracts strongly suggest these are on-task, but the evidence snippets are truncated and do not conclusively prove the output is a final B-rep (vs. an intermediate representation). More complete evidence is needed for a confident 'core' designation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the resolved time range (2022-2026)."
    },
    "gaps": {
      "passed": true,
      "reason": "The retrieval now covers the core topic well, with papers representing different approaches (direct primitive prediction, sequence-based, geometry-aware). No obvious major subtopic is missing given the nascent state of the field."
    }
  },
  "key_risks": [
    "The evidence for most papers is limited to partial abstracts; full-text verification is needed to confirm the output is indeed a B-rep and not a CSG tree or other intermediate representation.",
    "The output format does not match the user's requested structure, which will hinder the subsequent report-writing step."
  ],
  "next_actions": [
    "For the top 5-7 candidate papers (especially Point2Brep, P2CADNet, MiCADangelo, Point2Primitive, CAD-SIGNet), retrieve full abstracts or introductory sections to confirm: 1) input is a point cloud, 2) final output is a B-rep or parametric CAD model, 3) the paper's primary contribution is the end-to-end reconstruction pipeline.",
    "Reformat the output to include the user-requested fields: 'core contribution' (a concise summary of the method's novelty) and a detailed 'relevance note' explicitly justifying why the paper qualifies as an end-to-end point-cloud-to-B-rep reconstruction method.",
    "Filter out the clearly off-topic paper 'From CAD Models to Soft Point Cloud Labels' (it is about annotation, not reconstruction).",
    "Ensure the final list contains 5-10 papers, prioritizing those with the strongest evidence of being on-task."
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
The goal is to identify frontier research (2022–2026) where the **primary task** is an **end-to-end pipeline** that takes **point clouds as input** and directly outputs **B-rep (Boundary Representation) models** as the final result. The search strictly excludes work focused only on subproblems (e.g., segmentation, fitting), intermediate representations (e.g., mesh, CSG), auxiliary modules, or alternative tasks.

## Search Strategy
The search was conducted in two phases:
1.  **Initial Phase:** Queries focused on general "point cloud to B-rep" terms, which returned many off-topic results (e.g., point cloud generation, detection, FE modeling).
2.  **Revised Phase:** Queries were refined to target the CAD and geometry processing community explicitly, using terms like "B-rep reconstruction from point clouds deep learning" and "point cloud to boundary representation CAD reconstruction." Sources included Crossref, OpenAlex, and arXiv.

## Candidate Papers
**The search did not clear the quality bar.** The retrieval process identified several promising leads, but the reviewer determined that the evidence was insufficient to verify that these papers meet the strict, end-to-end B-rep reconstruction criteria. The team hit the review budget without achieving a passing verification status.

### Verified Candidates
*No papers were verified as core candidates meeting all user criteria.*

### Unverified Leads
The following papers appear highly relevant based on titles and partial abstracts but require full-text verification to confirm they are strictly end-to-end point-cloud-to-B-rep reconstruction methods. They are presented as follow-up leads, not recommendations.

1.  **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref / SSRN
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Note:** Title and abstract snippet explicitly mention reconstructing "complete and topologically consistent B-rep models" from point clouds, making it a very strong candidate for verification.

2.  **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2310.02638v1
    *   **Note:** Described as an "end-to-end network to reconstruct featured CAD model from point cloud." Requires verification that the output is a B-rep and not another CAD representation.

3.  **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans** (2025)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2510.23429v1
    *   **Note:** Focuses on "converting 3D scans into parametric CAD representations," a core task in CAD reverse engineering. Needs confirmation of B-rep output.

## Notes and Gaps
*   **Evidence Gap:** The primary gap is a lack of conclusive, full-text evidence for the most promising papers. Verification was limited to partial abstracts, which often do not explicitly confirm the output format as a B-rep versus other CAD representations (e.g., a construction sequence, CSG tree).
*   **Field Nascent:** The strict definition of "end-to-end point-cloud-to-B-rep" appears to be a very specialized and emerging niche. Many related works reconstruct parametric CAD models or primitives, but the final representation may not always be a strict B-rep.
*   **Off-Topic Retrieval:** Initial searches were noisy, retrieving papers on point cloud generation, annotation, and detection, highlighting the need for precise terminology.

## Recommended Next Steps
1.  **Manual Verification:** For the leads above (especially Point2Brep and P2CADNet), obtain and review the full text to confirm:
    *   Input is explicitly a raw point cloud.
    *   Final output is explicitly a B-rep model.
    *   The paper's primary contribution is the reconstruction pipeline itself.
2.  **Venue-Specific Search:** Conduct targeted searches in key conferences and journals such as ACM Transactions on Graphics, Computer-Aided Design, SIGGRAPH, and CVPR using advanced search filters.
3.  **Citation Tracking:** Use the identified leads as seed papers for backward and forward citation analysis to find related work.
4.  **Broaden Definition (If Allowed):** If the strict B-rep requirement can be relaxed to "editable parametric CAD model," the pool of relevant, verified literature would likely be larger.

TERMINATE
```
