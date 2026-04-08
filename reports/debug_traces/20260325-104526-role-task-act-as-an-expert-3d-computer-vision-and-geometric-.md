# Paper Search Debug Trace

**Query:** **Role & Task:**
Act as an expert 3D computer vision and geometric deep learning researcher. Your task is to search for and analyze 8-10 state-of-the-art frontier research papers (published between 2021-2026) focused explicitly on 3D Boundary Representation (B-Rep) reconstruction and generation. 

**Primary Focus (What to INCLUDE):**
* **Target Output:** The primary output of the model MUST be the B-Rep data structure itself (faces, edges, vertices, and their topological relationships).
* **Target Input:** Unstructured Point Clouds or 3D scans are the highest priority. Multimodal or sketch/image inputs are acceptable only if the method is a major breakthrough in B-Rep generation.
* **Methodology:** Highly prioritize modern neural architectures, including latent space representations, variational approaches, or end-to-end direct neural generation of continuous B-Rep geometry and topology.

**CRITICAL EXCLUSIONS (What to strictly AVOID):**
You MUST STRICTLY EXCLUDE any paper that falls into these categories:
1.  **NO CAD Operation Sequences:** Do not include papers where the goal is to reconstruct CAD construction trees, sketch-and-extrude histories, or sequential modeling steps (e.g., DeepCAD, Sketex).
2.  **NO CSG Trees:** Exclude papers focusing on Constructive Solid Geometry (CSG) primitive combinations.
3.  **NO Program Synthesis:** Exclude papers that generate CAD programs or macros.
*If the model outputs a step-by-step modeling history rather than directly outputting the final B-Rep topological/geometric data structure, it is a hard fail. Discard it.*

**Output Format:**
For each of the 8-10 selected papers, provide:
* **Title & Year:**
* **Source/Venue:** (e.g., CVPR, SIGGRAPH, NeurIPS)
* **Link:**
* **Core Contribution:** (1-2 sentences on their specific technical breakthrough)
* **Relevance Note:** (Explain exactly how it tackles direct B-Rep generation from point clouds, and confirm it does not rely on step-by-step operation sequences).

**Synthesis Report:**
After listing the papers, provide a concise summary covering:
1.  **Major Method Categories:** (How are current models representing B-Rep natively for neural networks?)
2.  **Recent Trends:** (e.g., shifts in handling topology vs. geometry)
3.  **Open Challenges:** (Specific bottlenecks in point-cloud-to-B-Rep tasks)
**Generated At:** 2026-03-25T10:45:26
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

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods based on CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct B-Rep output from neural networks",
    "point cloud to B-Rep reconstruction",
    "geometric deep learning for B-Rep",
    "topology-aware 3D generation",
    "latent representations for B-Rep"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "CSG tree generation",
    "CAD program synthesis",
    "procedural modeling steps"
  ],
  "fallback_queries": [
    "neural B-Rep generation",
    "3D shape reconstruction to boundary representation",
    "point cloud to CAD model deep learning"
  ],
  "queries": [
    {
      "query": "neural network direct B-Rep generation from point clouds",
      "reason": "Targets the core requirement of end-to-end B-Rep output from unstructured 3D data."
    },
    {
      "query": "boundary representation reconstruction deep learning 2023",
      "reason": "Focuses on B-Rep reconstruction with a recency filter aligned to the time range."
    },
    {
      "query": "topology aware 3D point cloud to CAD faces and edges",
      "reason": "Emphasizes the topological relationship learning critical for B-Rep, distinct from sequential modeling."
    }
  ],
  "assumptions": [
    "The user's 'between 2021-2026' is inclusive of both years.",
    "The primary input is unstructured point clouds; multimodal inputs are secondary unless they represent a major B-Rep breakthrough.",
    "Methods outputting a final B-Rep mesh/data structure directly are acceptable, even if they use intermediate representations.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, and ECCV are likely venues."
  ],
  "success_criteria": [
    "Retrieve papers where the model's primary output is a B-Rep structure.",
    "Exclude any paper reconstructing a step-by-step CAD modeling history.",
    "Identify 8-10 papers from the specified time window that are directly relevant.",
    "Cover recent advances in neural architectures for B-Rep geometry and topology."
  ]
}
```

### Planner Output 8

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods based on CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct B-Rep output from neural networks",
    "point cloud to B-Rep reconstruction",
    "geometric deep learning for B-Rep",
    "topology-aware 3D generation",
    "latent representations for B-Rep",
    "diffusion models for B-Rep",
    "autoregressive B-Rep generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "CSG tree generation",
    "CAD program synthesis",
    "procedural modeling steps",
    "command sequences",
    "construction history"
  ],
  "fallback_queries": [
    "neural B-Rep generation from point cloud",
    "B-Rep reconstruction deep learning",
    "point cloud to boundary representation neural network"
  ],
  "queries": [
    {
      "query": "direct B-Rep generation neural network point cloud",
      "reason": "Targets the core requirement of end-to-end B-Rep output from unstructured 3D data, using more precise terminology."
    },
    {
      "query": "B-Rep reconstruction from point cloud CVPR",
      "reason": "Focuses search on a key high-impact venue likely to publish state-of-the-art work in the specified time range."
    },
    {
      "query": "diffusion model B-Rep generation",
      "reason": "Captures a recent trend in generative models for structured outputs, as indicated by relevant papers like BrepGPT and HoLa."
    }
  ],
  "assumptions": [
    "The user's 'between 2021-2026' is inclusive of both years.",
    "The primary input is unstructured point clouds; multimodal inputs are secondary unless they represent a major B-Rep breakthrough.",
    "Methods outputting a final B-Rep mesh/data structure directly are acceptable, even if they use intermediate representations.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, and ECCV are likely venues.",
    "We must verify each candidate's method section or abstract to ensure it does not rely on CAD operation sequences, CSG, or program synthesis."
  ],
  "success_criteria": [
    "Retrieve papers where the model's primary output is a B-Rep structure and the method is described as direct generation/reconstruction.",
    "Exclude any paper reconstructing a step-by-step CAD modeling history, command sequence, or CSG tree.",
    "Identify 8-10 papers from the specified time window that are directly relevant, building on the 3 core candidates found.",
    "Cover recent advances in neural architectures (diffusion, autoregressive, latent space) for B-Rep geometry and topology."
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
      "query": "neural network direct B-Rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation reconstruction deep learning 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "topology aware 3D point cloud to CAD faces and edges",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\approx$50%."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"
      ]
    },
    {
      "title": "Automatic generation of structural geometric digital twins from point clouds",
      "source": "Crossref / Scientific Reports",
      "year": 2022,
      "date": "2022-12-24",
      "url": "https://doi.org/10.1038/s41598-022-26307-7",
      "doi": "10.1038/s41598-022-26307-7",
      "authors": [
        "Kaveh Mirzaei",
        "Mehrdad Arashpour",
        "Ehsan Asadi",
        "Hossein Masoumi",
        "Heng Li"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title><jats:p>A geometric digital twin (gDT) model capable of leveraging acquired 3D geometric data plays a vital role in digitizing the process of structural health monitoring. This study presents a framework for generating and updating digital twins of existing buildings by inferring semantic information from as-is point clouds (gDT’s data) acquired regularly from laser scanners (gDT’s connection). The information is stored in updatable Building Information Models (BIMs) as gDT’s virtual model, and dimensional outputs are extracted for structural health monitoring (gDT’s service) of different structural members and shapes (gDT’s physical part). First, geometric information, including position and section shape, is obtained from the acquired point cloud using domain-specific contextual knowledge and supervised classification. Then, structural members’ function and section family type is inferred from geometric information. Finally, a BIM is automatically generated or updated as the virtual model of an existing facility and incorporated within the gDT for structural health monitoring. Experiments on real-world construction data are performed to illustrate the efficiency and precision of the proposed model for creating as-is gDT of building structural members.</jats:p>"
      ]
    },
    {
      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-12-21T18:46:27Z",
      "url": "http://arxiv.org/abs/2312.14124v2",
      "doi": "",
      "authors": [
        "Philipp Schröppel",
        "Christopher Wewer",
        "Jan Eric Lenssen",
        "Eddy Ilg",
        "Thomas Brox"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."
      ]
    },
    {
      "title": "Edge Aware Learning for 3D Point Cloud",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-09-23T20:12:32Z",
      "url": "http://arxiv.org/abs/2309.13472v2",
      "doi": "",
      "authors": [
        "Lei Li"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper proposes an innovative approach to Hierarchical Edge Aware 3D Point Cloud Learning (HEA-Net) that seeks to address the challenges of noise in point cloud data, and improve object recognition and segmentation by focusing on edge features. In this study, we present an innovative edge-aware learning methodology, specifically designed to enhance point cloud classification and segmentation. Drawing inspiration from the human visual system, the concept of edge-awareness has been incorporated into this methodology, contributing to improved object recognition while simultaneously reducing computational time. Our research has led to the development of an advanced 3D point cloud learning framework that effectively manages object classification and segmentation tasks. A unique fusion of local and global network learning paradigms has been employed, enriched by edge-focused local and global embeddings, thereby significantly augmenting the model's interpretative prowess. Further, we have applied a hierarchical transformer architecture to boost point cloud processing efficiency, thus providing nuanced insights into structural understanding. Our approach demonstrates significant promise in managing noisy point cloud data and highlights the potential of edge-aware strategies in 3D point cloud learning. The proposed approach is shown to outperform existing techniques in object classification and segmentation tasks, as demonstrated by experiments on ModelNet40 and ShapeNet datasets."
      ]
    },
    {
      "title": "MDGroup: Multi-Grained Dual-Aware Grouping for 3D Point Cloud Instance Segmentation",
      "source": "Crossref / Electronics",
      "year": 2026,
      "date": "2026-2-24",
      "url": "https://doi.org/10.3390/electronics15050915",
      "doi": "10.3390/electronics15050915",
      "authors": [
        "Wenyun Sun",
        "Ruifeng Han"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Instance segmentation of 3D point clouds is a fundamental task for scene understanding in applications such as autonomous driving, robotics, and augmented reality. The inherent irregularity and sparsity of point clouds, compounded by scale variations and instance adhesion, pose significant challenges to accurate segmentation. Existing grouping-based methods are often limited by the loss of geometric details in single-path backbones and by error propagation near complex boundaries. To address these issues, a Multi-grained Dual-aware Grouping algorithm (MDGroup) is proposed, which explicitly integrates multi-grained feature representation with dual awareness of class and boundary. The algorithm features a Dual-Resolution 3D U-Net (DRNet) that preserves local geometric details while aggregating global semantics through adaptive alignment. A four-branch prediction scheme enhances semantic and offset estimation with boundary and directional cues, enabling fine-grained boundary modeling. Furthermore, a Hierarchical Adaptive Multi-grained Feature fusion framework (HAMF) achieves efficient cross-scale alignment by combining Class-Aware Dynamic Voxelization and Class-Aware Pyramid Scaling. Finally, a Boundary-Aware Weighted Aggregation mechanism (BAWA) refines instance grouping by dynamically weighting semantic confidence, geometric distance, boundary probability, and directional consistency. To extend the model to dynamic scenes, a Temporal Adaptive Gating (TAG) module is introduced to leverage historical frame correlations. Extensive experiments on the ScanNet v2, S3DIS, STPLS3D, SemanticKITTI, LiDAR-Net, and OCID benchmarks demonstrate that MDGroup achieves state-of-the-art performance among grouping-based methods, particularly on small objects, complex boundaries, and dynamic environments.</jats:p>"
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual intervention or dataset-specific parameters. Our labeling pipeline outputs semantic classes and soft point-wise object scores, which can either be binarized into standard one-hot-encoded labels, thresholded into weak labels with ambiguous points left unlabeled, or used directly as soft labels during training. We evaluate the label quality and segmentation performance of PointNet++ on a dataset of real industrial point clouds and Scan2CAD, a public dataset of indoor scenes. Our results indicate that reducing supervision in areas that are more difficult to label automatically is beneficial compared with the conventional approach of naively assigning a hard “best guess” label to every point.</jats:p>"
      ]
    },
    {
      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-08-12T12:58:44Z",
      "url": "http://arxiv.org/abs/2508.08910v1",
      "doi": "",
      "authors": [
        "Bin Ren",
        "Xiaoshui Huang",
        "Mengyuan Liu",
        "Hong Liu",
        "Fabio Poiesi",
        "Nicu Sebe",
        "Guofeng Mei"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural B-Rep generation",
      "3D shape reconstruction to boundary representation",
      "point cloud to CAD model deep learning"
    ],
    "effective_query": "neural network direct B-Rep generation from point clouds",
    "used_override_query": false,
    "executed_queries": [
      "neural network direct B-Rep generation from point clouds",
      "boundary representation reconstruction deep learning 2023",
      "topology aware 3D point cloud to CAD faces and edges"
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
      "query": "neural B-Rep generation from point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-Rep generation neural network point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from point cloud CVPR",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "diffusion model B-Rep generation",
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
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-01-28T04:07:59Z",
      "url": "http://arxiv.org/abs/2401.15563v3",
      "doi": "",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
      ]
    },
    {
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-07-19",
      "url": "https://doi.org/10.1145/3658129",
      "doi": "10.1145/3658129",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"
      ]
    },
    {
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-01-28",
      "url": "http://arxiv.org/abs/2401.15563",
      "doi": "10.48550/arxiv.2401.15563",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
      ]
    },
    {
      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-01-23T14:15:02Z",
      "url": "http://arxiv.org/abs/2601.16771v1",
      "doi": "",
      "authors": [
        "Jiahao Li",
        "Yunpeng Bai",
        "Yongkang Dai",
        "Hao Guo",
        "Hongping Gan",
        "Yilei Shi"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep's geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."
      ]
    },
    {
      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-12-02T18:46:25Z",
      "url": "http://arxiv.org/abs/2512.03018v1",
      "doi": "",
      "authors": [
        "Xiang Xu",
        "Pradeep Kumar Jayaraman",
        "Joseph G. Lambourne",
        "Yilin Liu",
        "Durvesh Malpure",
        "Pete Meltzer"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."
      ]
    },
    {
      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-03-17T12:34:14Z",
      "url": "http://arxiv.org/abs/2503.13110v1",
      "doi": "",
      "authors": [
        "Jing Li",
        "Yihang Fu",
        "Falai Chen"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."
      ]
    },
    {
      "title": "CADDreamer: CAD Object Generation from Single-view Images",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-06-10",
      "url": "https://doi.org/10.1109/cvpr52734.2025.01998",
      "doi": "10.1109/cvpr52734.2025.01998",
      "authors": [
        "Yuan Li",
        "Cheng Lin",
        "Yuan Liu",
        "Xiaoxiao Long",
        "Chenxu Zhang",
        "Ningna Wang",
        "Xin Li",
        "Wenping Wang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Diffusion-based 3D generation has made remarkable progress in recent years. However, existing 3D generative models often produce overly dense and unstructured meshes, which stand in stark contrast to the compact, structured, and sharply-edged Computer-Aided Design (CAD) models crafted by human designers. To address this gap, we introduce CADDreamer, a novel approach for generating boundary representations (B-rep) of CAD objects from a single image. CADDreamer employs a primitive-aware multi-view diffusion model that captures both local geometric details and high-level structural semantics during the generation process. By encoding primitive semantics into the color domain, the method leverages the strong priors of pre-trained diffusion models to align with well-defined primitives. This enables the inference of multi-view normal maps and semantic maps from a single image, facilitating the reconstruction of a mesh with primitive labels. Furthermore, we introduce geometric optimization techniques and topology-preserving extraction methods to mitigate noise and distortion in the generated primitives. These enhancements result in a complete and seamless B-rep of the CAD model. Experimental results demonstrate that our method effectively recovers high-quality CAD objects from single-view images. Compared to existing 3D generation techniques, the B-rep models produced by CADDreamer are compact in representation, clear in structure, sharp in edges, and watertight in topology."
      ]
    },
    {
      "title": "B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions?",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-11-18T19:40:34Z",
      "url": "http://arxiv.org/abs/2511.14870v1",
      "doi": "",
      "authors": [
        "Fuyang Zhang",
        "Pradeep Kumar Jayaraman",
        "Xiang Xu",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents a novel geometric representation for CAD Boundary Representation (B-Rep) based on volumetric distance functions, dubbed B-Rep Distance Functions (BR-DF). BR-DF encodes the surface mesh geometry of a CAD model as signed distance function (SDF). B-Rep vertices, edges, faces and their topology information are encoded as per-face unsigned distance functions (UDFs). An extension of the Marching Cubes algorithm converts BR-DF directly into watertight CAD B-Rep model (strictly speaking a faceted B-Rep model). A surprising characteristic of BR-DF is that this conversion process never fails. Leveraging the volumetric nature of BR-DF, we propose a multi-branch latent diffusion with 3D U-Net backbone for jointly generating the SDF and per-face UDFs of a BR-DF model. Our approach achieves comparable CAD generation performance against SOTA methods while reaching the unprecedented 100% success rate in producing (faceted) B-Rep models."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 58 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural B-Rep generation from point cloud",
      "B-Rep reconstruction deep learning",
      "point cloud to boundary representation neural network"
    ],
    "effective_query": "neural B-Rep generation from point cloud",
    "used_override_query": true,
    "executed_queries": [
      "neural B-Rep generation from point cloud",
      "direct B-Rep generation neural network point cloud",
      "B-Rep reconstruction from point cloud CVPR",
      "diffusion model B-Rep generation"
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
  "review_summary": "The retrieval output contains several relevant papers, but fails to meet multiple hard requirements. The candidate depth is insufficient, with only 3 papers clearly aligned with the core topic of direct B-Rep generation from point clouds. Several papers are about general point cloud processing, segmentation, or digital twins, not B-Rep reconstruction. The query fit is poor as the set does not reflect the user's strict exclusion of CAD operation sequences, and the evidence snippets are insufficient to verify compliance with these exclusions. The core-method fit is weak, with only Point2Brep, BrepGPT, and HoLa appearing as plausible core candidates.",
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
      "reason": "3 distinct sources used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, HoLa) are clearly aligned with the core topic of direct B-Rep generation from point clouds. Others are about point cloud segmentation, digital twins, or general point cloud learning, not B-Rep reconstruction/generation."
    },
    "relevance": {
      "passed": false,
      "reason": "Among top candidates, only 2-3 are clearly aligned. Papers like 'Automatic generation of structural geometric digital twins...', 'Neural Point Cloud Diffusion...', 'Edge Aware Learning...', 'MDGroup...', 'From CAD Models to Soft Point Cloud Labels...', and 'Masked Clustering Prediction...' are not about B-Rep reconstruction/generation; they are about point cloud segmentation, digital twins, or general representation learning."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not reflect the user's strict exclusion criteria. For example, 'CAD-MLLM' mentions 'command sequences of CAD models', which strongly suggests it involves CAD operation sequences, which the user explicitly excluded. Evidence snippets are insufficient to verify that other papers avoid CAD operation sequences, CSG trees, or program synthesis."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, HoLa) plausibly look like core candidates for direct B-Rep generation from point clouds. Others are not core to the topic."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing core subtopic: there is a lack of papers specifically on neural direct B-Rep generation from point clouds published in key venues (CVPR, SIGGRAPH, etc.) between 2021-2024. The set over-relies on arXiv and includes many off-topic papers, indicating a major evidence hole."
    }
  },
  "key_risks": ["High risk of including papers that violate exclusion criteria (e.g., CAD-MLLM likely uses command sequences).", "Insufficient core papers to meet the user's request for 8-10 state-of-the-art frontier papers.", "Evidence snippets are abstract-only and do not provide enough detail to confirm the method outputs B-Rep directly without operation sequences."],
  "next_actions": ["Execute fallback queries: 'neural B-Rep generation', '3D shape reconstruction to boundary representation', 'point cloud to CAD model deep learning'.", "Focus search on specific venues: CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, ACM Transactions on Graphics.", "For each candidate, retrieve full abstract or method section to verify it outputs B-Rep directly and does not use CAD operation sequences, CSG, or program synthesis.", "Explicitly filter out papers mentioning 'command sequence', 'construction history', 'CSG', 'program synthesis', 'sketch-and-extrude' in the evidence."]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows significant improvement in topic alignment, with many papers explicitly about B-Rep generation. However, critical hard requirements are still not met. The candidate depth is insufficient due to extensive duplication (58 duplicates merged), leaving only 9 distinct papers, some of which violate exclusion criteria (e.g., Brep2Seq outputs 'parametrized feature-based modeling operations', which likely involves CAD operation sequences). The evidence snippets are insufficient to verify that all papers avoid CAD operation sequences, CSG, or program synthesis. The core-method fit is weak because several papers are generative only, not reconstruction from point clouds as the user prioritized. The set lacks sufficient papers focused on point cloud to B-Rep reconstruction.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "3 distinct sources used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, only 9 distinct candidate papers remain (Point2Brep, BrepGPT, BrepGen, AutoRegressive Generation with B-rep Holistic Token Sequence Representation, AutoBrep, DTGBrepGen, GraphBrep, CADDreamer, B-Rep Distance Functions, Brep2Seq). This is below the required 10, and some are not valid (Brep2Seq likely violates exclusions)."
    },
    "relevance": {
      "passed": true,
      "reason": "Among top candidates, at least 2-3 are clearly aligned with direct B-Rep generation (e.g., Point2Brep, BrepGPT, BrepGen)."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. Brep2Seq explicitly mentions 'parametrized feature-based modeling operations', which strongly suggests CAD operation sequences, a hard exclusion. CADDreamer generates from single-view images, not point clouds, which is secondary unless a major breakthrough; evidence does not establish it as such. Many papers are unconditional generative models, not reconstruction from point clouds as the user prioritized."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, BrepGen) plausibly look like core candidates for direct B-Rep generation from point clouds. Others are either generative only (not reconstruction), or input is images (CADDreamer), or may involve operation sequences (Brep2Seq)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing core subtopic: insufficient papers on point cloud to B-Rep reconstruction. The set is skewed towards unconditional generative models and image-conditioned generation. Major evidence hole: lack of verification that papers avoid CAD operation sequences; evidence snippets are abstract-only and insufficient."
    }
  },
  "key_risks": ["High risk of including papers that violate exclusion criteria (e.g., Brep2Seq).", "Insufficient papers focused on point cloud to B-Rep reconstruction, which is the user's highest priority.", "Evidence snippets are abstract-only and do not provide enough detail to confirm the method outputs B-Rep directly without operation sequences or CSG.", "Candidate depth is borderline even after deduplication, and some candidates are off-topic."],
  "next_actions": ["Execute targeted query: 'point cloud to B-Rep reconstruction neural network 2023 2024 2025' to prioritize reconstruction over unconditional generation.", "For each candidate, retrieve full method section or explicit statements to verify it does not use CAD operation sequences, CSG, or program synthesis.", "Explicitly filter out papers mentioning 'feature-based modeling operations', 'command sequence', 'construction history', 'CSG', 'program synthesis'.", "Search for papers in CVPR, SIGGRAPH, ICCV, ECCV, NeurIPS from 2021-2024 that specifically address B-Rep reconstruction from point clouds."]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_95OeClEmWdNWygMEGO7wbaXR', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural network direct B-Rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation reconstruction deep learning 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "topology aware 3D point cloud to CAD faces and edges",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "Automatic generation of structural geometric digital twins from point clouds",\n      "source": "Crossref / Scientific Reports",\n      "year": 2022,\n      "date": "2022-12-24",\n      "url": "https://doi.org/10.1038/s41598-022-26307-7",\n      "doi": "10.1038/s41598-022-26307-7",\n      "authors": [\n        "Kaveh Mirzaei",\n        "Mehrdad Arashpour",\n        "Ehsan Asadi",\n        "Hossein Masoumi",\n        "Heng Li"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title><jats:p>A geometric digital twin (gDT) model capable of leveraging acquired 3D geometric data plays a vital role in digitizing the process of structural health monitoring. This study presents a framework for generating and updating digital twins of existing buildings by inferring semantic information from as-is point clouds (gDT’s data) acquired regularly from laser scanners (gDT’s connection). The information is stored in updatable Building Information Models (BIMs) as gDT’s virtual model, and dimensional outputs are extracted for structural health monitoring (gDT’s service) of different structural members and shapes (gDT’s physical part). First, geometric information, including position and section shape, is obtained from the acquired point cloud using domain-specific contextual knowledge and supervised classification. Then, structural members’ function and section family type is inferred from geometric information. Finally, a BIM is automatically generated or updated as the virtual model of an existing facility and incorporated within the gDT for structural health monitoring. Experiments on real-world construction data are performed to illustrate the efficiency and precision of the proposed model for creating as-is gDT of building structural members.</jats:p>"\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "Edge Aware Learning for 3D Point Cloud",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-09-23T20:12:32Z",\n      "url": "http://arxiv.org/abs/2309.13472v2",\n      "doi": "",\n      "authors": [\n        "Lei Li"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper proposes an innovative approach to Hierarchical Edge Aware 3D Point Cloud Learning (HEA-Net) that seeks to address the challenges of noise in point cloud data, and improve object recognition and segmentation by focusing on edge features. In this study, we present an innovative edge-aware learning methodology, specifically designed to enhance point cloud classification and segmentation. Drawing inspiration from the human visual system, the concept of edge-awareness has been incorporated into this methodology, contributing to improved object recognition while simultaneously reducing computational time. Our research has led to the development of an advanced 3D point cloud learning framework that effectively manages object classification and segmentation tasks. A unique fusion of local and global network learning paradigms has been employed, enriched by edge-focused local and global embeddings, thereby significantly augmenting the model\'s interpretative prowess. Further, we have applied a hierarchical transformer architecture to boost point cloud processing efficiency, thus providing nuanced insights into structural understanding. Our approach demonstrates significant promise in managing noisy point cloud data and highlights the potential of edge-aware strategies in 3D point cloud learning. The proposed approach is shown to outperform existing techniques in object classification and segmentation tasks, as demonstrated by experiments on ModelNet40 and ShapeNet datasets."\n      ]\n    },\n    {\n      "title": "MDGroup: Multi-Grained Dual-Aware Grouping for 3D Point Cloud Instance Segmentation",\n      "source": "Crossref / Electronics",\n      "year": 2026,\n      "date": "2026-2-24",\n      "url": "https://doi.org/10.3390/electronics15050915",\n      "doi": "10.3390/electronics15050915",\n      "authors": [\n        "Wenyun Sun",\n        "Ruifeng Han"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Instance segmentation of 3D point clouds is a fundamental task for scene understanding in applications such as autonomous driving, robotics, and augmented reality. The inherent irregularity and sparsity of point clouds, compounded by scale variations and instance adhesion, pose significant challenges to accurate segmentation. Existing grouping-based methods are often limited by the loss of geometric details in single-path backbones and by error propagation near complex boundaries. To address these issues, a Multi-grained Dual-aware Grouping algorithm (MDGroup) is proposed, which explicitly integrates multi-grained feature representation with dual awareness of class and boundary. The algorithm features a Dual-Resolution 3D U-Net (DRNet) that preserves local geometric details while aggregating global semantics through adaptive alignment. A four-branch prediction scheme enhances semantic and offset estimation with boundary and directional cues, enabling fine-grained boundary modeling. Furthermore, a Hierarchical Adaptive Multi-grained Feature fusion framework (HAMF) achieves efficient cross-scale alignment by combining Class-Aware Dynamic Voxelization and Class-Aware Pyramid Scaling. Finally, a Boundary-Aware Weighted Aggregation mechanism (BAWA) refines instance grouping by dynamically weighting semantic confidence, geometric distance, boundary probability, and directional consistency. To extend the model to dynamic scenes, a Temporal Adaptive Gating (TAG) module is introduced to leverage historical frame correlations. Extensive experiments on the ScanNet v2, S3DIS, STPLS3D, SemanticKITTI, LiDAR-Net, and OCID benchmarks demonstrate that MDGroup achieves state-of-the-art performance among grouping-based methods, particularly on small objects, complex boundaries, and dynamic environments.</jats:p>"\n      ]\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual intervention or dataset-specific parameters. Our labeling pipeline outputs semantic classes and soft point-wise object scores, which can either be binarized into standard one-hot-encoded labels, thresholded into weak labels with ambiguous points left unlabeled, or used directly as soft labels during training. We evaluate the label quality and segmentation performance of PointNet++ on a dataset of real industrial point clouds and Scan2CAD, a public dataset of indoor scenes. Our results indicate that reducing supervision in areas that are more difficult to label automatically is beneficial compared with the conventional approach of naively assigning a hard “best guess” label to every point.</jats:p>"\n      ]\n    },\n    {\n      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-08-12T12:58:44Z",\n      "url": "http://arxiv.org/abs/2508.08910v1",\n      "doi": "",\n      "authors": [\n        "Bin Ren",\n        "Xiaoshui Huang",\n        "Mengyuan Liu",\n        "Hong Liu",\n        "Fabio Poiesi",\n        "Nicu Sebe",\n        "Guofeng Mei"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural B-Rep generation",\n      "3D shape reconstruction to boundary representation",\n      "point cloud to CAD model deep learning"\n    ],\n    "effective_query": "neural network direct B-Rep generation from point clouds",\n    "used_override_query": false,\n    "executed_queries": [\n      "neural network direct B-Rep generation from point clouds",\n      "boundary representation reconstruction deep learning 2023",\n      "topology aware 3D point cloud to CAD faces and edges"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_95OeClEmWdNWygMEGO7wbaXR' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_83tzkAOChzDSIUKuil34BINJ', arguments='{"top_k": 12, "max_results_per_source": 25, "query": "neural B-Rep generation from point cloud"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural B-Rep generation from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-Rep generation neural network point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from point cloud CVPR",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "diffusion model B-Rep generation",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    },\n    {\n      "title": "CADDreamer: CAD Object Generation from Single-view Images",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-06-10",\n      "url": "https://doi.org/10.1109/cvpr52734.2025.01998",\n      "doi": "10.1109/cvpr52734.2025.01998",\n      "authors": [\n        "Yuan Li",\n        "Cheng Lin",\n        "Yuan Liu",\n        "Xiaoxiao Long",\n        "Chenxu Zhang",\n        "Ningna Wang",\n        "Xin Li",\n        "Wenping Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Diffusion-based 3D generation has made remarkable progress in recent years. However, existing 3D generative models often produce overly dense and unstructured meshes, which stand in stark contrast to the compact, structured, and sharply-edged Computer-Aided Design (CAD) models crafted by human designers. To address this gap, we introduce CADDreamer, a novel approach for generating boundary representations (B-rep) of CAD objects from a single image. CADDreamer employs a primitive-aware multi-view diffusion model that captures both local geometric details and high-level structural semantics during the generation process. By encoding primitive semantics into the color domain, the method leverages the strong priors of pre-trained diffusion models to align with well-defined primitives. This enables the inference of multi-view normal maps and semantic maps from a single image, facilitating the reconstruction of a mesh with primitive labels. Furthermore, we introduce geometric optimization techniques and topology-preserving extraction methods to mitigate noise and distortion in the generated primitives. These enhancements result in a complete and seamless B-rep of the CAD model. Experimental results demonstrate that our method effectively recovers high-quality CAD objects from single-view images. Compared to existing 3D generation techniques, the B-rep models produced by CADDreamer are compact in representation, clear in structure, sharp in edges, and watertight in topology."\n      ]\n    },\n    {\n      "title": "B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions?",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-18T19:40:34Z",\n      "url": "http://arxiv.org/abs/2511.14870v1",\n      "doi": "",\n      "authors": [\n        "Fuyang Zhang",\n        "Pradeep Kumar Jayaraman",\n        "Xiang Xu",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents a novel geometric representation for CAD Boundary Representation (B-Rep) based on volumetric distance functions, dubbed B-Rep Distance Functions (BR-DF). BR-DF encodes the surface mesh geometry of a CAD model as signed distance function (SDF). B-Rep vertices, edges, faces and their topology information are encoded as per-face unsigned distance functions (UDFs). An extension of the Marching Cubes algorithm converts BR-DF directly into watertight CAD B-Rep model (strictly speaking a faceted B-Rep model). A surprising characteristic of BR-DF is that this conversion process never fails. Leveraging the volumetric nature of BR-DF, we propose a multi-branch latent diffusion with 3D U-Net backbone for jointly generating the SDF and per-face UDFs of a BR-DF model. Our approach achieves comparable CAD generation performance against SOTA methods while reaching the unprecedented 100% success rate in producing (faceted) B-Rep models."\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 58 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural B-Rep generation from point cloud",\n      "B-Rep reconstruction deep learning",\n      "point cloud to boundary representation neural network"\n    ],\n    "effective_query": "neural B-Rep generation from point cloud",\n    "used_override_query": true,\n    "executed_queries": [\n      "neural B-Rep generation from point cloud",\n      "direct B-Rep generation neural network point cloud",\n      "B-Rep reconstruction from point cloud CVPR",\n      "diffusion model B-Rep generation"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_83tzkAOChzDSIUKuil34BINJ' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: **Role & Task:**

```text
**Role & Task:**
Act as an expert 3D computer vision and geometric deep learning researcher. Your task is to search for and analyze 8-10 state-of-the-art frontier research papers (published between 2021-2026) focused explicitly on 3D Boundary Representation (B-Rep) reconstruction and generation. 

**Primary Focus (What to INCLUDE):**
* **Target Output:** The primary output of the model MUST be the B-Rep data structure itself (faces, edges, vertices, and their topological relationships).
* **Target Input:** Unstructured Point Clouds or 3D scans are the highest priority. Multimodal or sketch/image inputs are acceptable only if the method is a major breakthrough in B-Rep generation.
* **Methodology:** Highly prioritize modern neural architectures, including latent space representations, variational approaches, or end-to-end direct neural generation of continuous B-Rep geometry and topology.

**CRITICAL EXCLUSIONS (What to strictly AVOID):**
You MUST STRICTLY EXCLUDE any paper that falls into these categories:
1.  **NO CAD Operation Sequences:** Do not include papers where the goal is to reconstruct CAD construction trees, sketch-and-extrude histories, or sequential modeling steps (e.g., DeepCAD, Sketex).
2.  **NO CSG Trees:** Exclude papers focusing on Constructive Solid Geometry (CSG) primitive combinations.
3.  **NO Program Synthesis:** Exclude papers that generate CAD programs or macros.
*If the model outputs a step-by-step modeling history rather than directly outputting the final B-Rep topological/geometric data structure, it is a hard fail. Discard it.*

**Output Format:**
For each of the 8-10 selected papers, provide:
* **Title & Year:**
* **Source/Venue:** (e.g., CVPR, SIGGRAPH, NeurIPS)
* **Link:**
* **Core Contribution:** (1-2 sentences on their specific technical breakthrough)
* **Relevance Note:** (Explain exactly how it tackles direct B-Rep generation from point clouds, and confirm it does not rely on step-by-step operation sequences).

**Synthesis Report:**
After listing the papers, provide a concise summary covering:
1.  **Major Method Categories:** (How are current models representing B-Rep natively for neural networks?)
2.  **Recent Trends:** (e.g., shifts in handling topology vs. geometry)
3.  **Open Challenges:** (Specific bottlenecks in point-cloud-to-B-Rep tasks)

[Runtime Search Context]
Today's date for this run is 2026-03-25.
- The query contains a vague recency hint. PlannerAgent must resolve it into an explicit year range against today's date and all later agents must preserve that range.
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods based on CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": ["direct B-Rep output from neural networks", "point cloud to B-Rep reconstruction", "geometric deep learning for B-Rep", "topology-aware 3D generation", "latent representations for B-Rep"],
  "exclude_areas": ["CAD operation sequence reconstruction", "sketch-and-extrude history modeling", "CSG tree generation", "CAD program synthesis", "procedural modeling steps"],
  "fallback_queries": ["neural B-Rep generation", "3D shape reconstruction to boundary representation", "point cloud to CAD model deep learning"],
  "queries": [
    {
      "query": "neural network direct B-Rep generation from point clouds",
      "reason": "Targets the core requirement of end-to-end B-Rep output from unstructured 3D data."
    },
    {
      "query": "boundary representation reconstruction deep learning 2023",
      "reason": "Focuses on B-Rep reconstruction with a recency filter aligned to the time range."
    },
    {
      "query": "topology aware 3D point cloud to CAD faces and edges",
      "reason": "Emphasizes the topological relationship learning critical for B-Rep, distinct from sequential modeling."
    }
  ],
  "assumptions": ["The user's 'between 2021-2026' is inclusive of both years.", "The primary input is unstructured point clouds; multimodal inputs are secondary unless they represent a major B-Rep breakthrough.", "Methods outputting a final B-Rep mesh/data structure directly are acceptable, even if they use intermediate representations.", "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, and ECCV are likely venues."],
  "success_criteria": ["Retrieve papers where the model's primary output is a B-Rep structure.", "Exclude any paper reconstructing a step-by-step CAD modeling history.", "Identify 8-10 papers from the specified time window that are directly relevant.", "Cover recent advances in neural architectures for B-Rep geometry and topology."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find relevant papers on 3D B-Rep reconstruction and generation from point clouds using neural networks.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_95OeClEmWdNWygMEGO7wbaXR', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural network direct B-Rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation reconstruction deep learning 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "topology aware 3D point cloud to CAD faces and edges",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "Automatic generation of structural geometric digital twins from point clouds",\n      "source": "Crossref / Scientific Reports",\n      "year": 2022,\n      "date": "2022-12-24",\n      "url": "https://doi.org/10.1038/s41598-022-26307-7",\n      "doi": "10.1038/s41598-022-26307-7",\n      "authors": [\n        "Kaveh Mirzaei",\n        "Mehrdad Arashpour",\n        "Ehsan Asadi",\n        "Hossein Masoumi",\n        "Heng Li"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title><jats:p>A geometric digital twin (gDT) model capable of leveraging acquired 3D geometric data plays a vital role in digitizing the process of structural health monitoring. This study presents a framework for generating and updating digital twins of existing buildings by inferring semantic information from as-is point clouds (gDT’s data) acquired regularly from laser scanners (gDT’s connection). The information is stored in updatable Building Information Models (BIMs) as gDT’s virtual model, and dimensional outputs are extracted for structural health monitoring (gDT’s service) of different structural members and shapes (gDT’s physical part). First, geometric information, including position and section shape, is obtained from the acquired point cloud using domain-specific contextual knowledge and supervised classification. Then, structural members’ function and section family type is inferred from geometric information. Finally, a BIM is automatically generated or updated as the virtual model of an existing facility and incorporated within the gDT for structural health monitoring. Experiments on real-world construction data are performed to illustrate the efficiency and precision of the proposed model for creating as-is gDT of building structural members.</jats:p>"\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "Edge Aware Learning for 3D Point Cloud",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-09-23T20:12:32Z",\n      "url": "http://arxiv.org/abs/2309.13472v2",\n      "doi": "",\n      "authors": [\n        "Lei Li"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper proposes an innovative approach to Hierarchical Edge Aware 3D Point Cloud Learning (HEA-Net) that seeks to address the challenges of noise in point cloud data, and improve object recognition and segmentation by focusing on edge features. In this study, we present an innovative edge-aware learning methodology, specifically designed to enhance point cloud classification and segmentation. Drawing inspiration from the human visual system, the concept of edge-awareness has been incorporated into this methodology, contributing to improved object recognition while simultaneously reducing computational time. Our research has led to the development of an advanced 3D point cloud learning framework that effectively manages object classification and segmentation tasks. A unique fusion of local and global network learning paradigms has been employed, enriched by edge-focused local and global embeddings, thereby significantly augmenting the model\'s interpretative prowess. Further, we have applied a hierarchical transformer architecture to boost point cloud processing efficiency, thus providing nuanced insights into structural understanding. Our approach demonstrates significant promise in managing noisy point cloud data and highlights the potential of edge-aware strategies in 3D point cloud learning. The proposed approach is shown to outperform existing techniques in object classification and segmentation tasks, as demonstrated by experiments on ModelNet40 and ShapeNet datasets."\n      ]\n    },\n    {\n      "title": "MDGroup: Multi-Grained Dual-Aware Grouping for 3D Point Cloud Instance Segmentation",\n      "source": "Crossref / Electronics",\n      "year": 2026,\n      "date": "2026-2-24",\n      "url": "https://doi.org/10.3390/electronics15050915",\n      "doi": "10.3390/electronics15050915",\n      "authors": [\n        "Wenyun Sun",\n        "Ruifeng Han"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Instance segmentation of 3D point clouds is a fundamental task for scene understanding in applications such as autonomous driving, robotics, and augmented reality. The inherent irregularity and sparsity of point clouds, compounded by scale variations and instance adhesion, pose significant challenges to accurate segmentation. Existing grouping-based methods are often limited by the loss of geometric details in single-path backbones and by error propagation near complex boundaries. To address these issues, a Multi-grained Dual-aware Grouping algorithm (MDGroup) is proposed, which explicitly integrates multi-grained feature representation with dual awareness of class and boundary. The algorithm features a Dual-Resolution 3D U-Net (DRNet) that preserves local geometric details while aggregating global semantics through adaptive alignment. A four-branch prediction scheme enhances semantic and offset estimation with boundary and directional cues, enabling fine-grained boundary modeling. Furthermore, a Hierarchical Adaptive Multi-grained Feature fusion framework (HAMF) achieves efficient cross-scale alignment by combining Class-Aware Dynamic Voxelization and Class-Aware Pyramid Scaling. Finally, a Boundary-Aware Weighted Aggregation mechanism (BAWA) refines instance grouping by dynamically weighting semantic confidence, geometric distance, boundary probability, and directional consistency. To extend the model to dynamic scenes, a Temporal Adaptive Gating (TAG) module is introduced to leverage historical frame correlations. Extensive experiments on the ScanNet v2, S3DIS, STPLS3D, SemanticKITTI, LiDAR-Net, and OCID benchmarks demonstrate that MDGroup achieves state-of-the-art performance among grouping-based methods, particularly on small objects, complex boundaries, and dynamic environments.</jats:p>"\n      ]\n    },\n    {\n      "title": "From CAD Models to Soft Point Cloud Labels: An Automatic Annotation Pipeline for Cheaply Supervised 3D Semantic Segmentation",\n      "source": "Crossref / Remote Sensing",\n      "year": 2023,\n      "date": "2023-7-17",\n      "url": "https://doi.org/10.3390/rs15143578",\n      "doi": "10.3390/rs15143578",\n      "authors": [\n        "Galadrielle Humblot-Renaux",\n        "Simon Buus Jensen",\n        "Andreas Møgelmose"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual intervention or dataset-specific parameters. Our labeling pipeline outputs semantic classes and soft point-wise object scores, which can either be binarized into standard one-hot-encoded labels, thresholded into weak labels with ambiguous points left unlabeled, or used directly as soft labels during training. We evaluate the label quality and segmentation performance of PointNet++ on a dataset of real industrial point clouds and Scan2CAD, a public dataset of indoor scenes. Our results indicate that reducing supervision in areas that are more difficult to label automatically is beneficial compared with the conventional approach of naively assigning a hard “best guess” label to every point.</jats:p>"\n      ]\n    },\n    {\n      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-08-12T12:58:44Z",\n      "url": "http://arxiv.org/abs/2508.08910v1",\n      "doi": "",\n      "authors": [\n        "Bin Ren",\n        "Xiaoshui Huang",\n        "Mengyuan Liu",\n        "Hong Liu",\n        "Fabio Poiesi",\n        "Nicu Sebe",\n        "Guofeng Mei"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural B-Rep generation",\n      "3D shape reconstruction to boundary representation",\n      "point cloud to CAD model deep learning"\n    ],\n    "effective_query": "neural network direct B-Rep generation from point clouds",\n    "used_override_query": false,\n    "executed_queries": [\n      "neural network direct B-Rep generation from point clouds",\n      "boundary representation reconstruction deep learning 2023",\n      "topology aware 3D point cloud to CAD faces and edges"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_95OeClEmWdNWygMEGO7wbaXR' is_error=False
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
      "query": "neural network direct B-Rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation reconstruction deep learning 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "topology aware 3D point cloud to CAD faces and edges",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\approx$50%."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"
      ]
    },
    {
      "title": "Automatic generation of structural geometric digital twins from point clouds",
      "source": "Crossref / Scientific Reports",
      "year": 2022,
      "date": "2022-12-24",
      "url": "https://doi.org/10.1038/s41598-022-26307-7",
      "doi": "10.1038/s41598-022-26307-7",
      "authors": [
        "Kaveh Mirzaei",
        "Mehrdad Arashpour",
        "Ehsan Asadi",
        "Hossein Masoumi",
        "Heng Li"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title><jats:p>A geometric digital twin (gDT) model capable of leveraging acquired 3D geometric data plays a vital role in digitizing the process of structural health monitoring. This study presents a framework for generating and updating digital twins of existing buildings by inferring semantic information from as-is point clouds (gDT’s data) acquired regularly from laser scanners (gDT’s connection). The information is stored in updatable Building Information Models (BIMs) as gDT’s virtual model, and dimensional outputs are extracted for structural health monitoring (gDT’s service) of different structural members and shapes (gDT’s physical part). First, geometric information, including position and section shape, is obtained from the acquired point cloud using domain-specific contextual knowledge and supervised classification. Then, structural members’ function and section family type is inferred from geometric information. Finally, a BIM is automatically generated or updated as the virtual model of an existing facility and incorporated within the gDT for structural health monitoring. Experiments on real-world construction data are performed to illustrate the efficiency and precision of the proposed model for creating as-is gDT of building structural members.</jats:p>"
      ]
    },
    {
      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-12-21T18:46:27Z",
      "url": "http://arxiv.org/abs/2312.14124v2",
      "doi": "",
      "authors": [
        "Philipp Schröppel",
        "Christopher Wewer",
        "Jan Eric Lenssen",
        "Eddy Ilg",
        "Thomas Brox"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."
      ]
    },
    {
      "title": "Edge Aware Learning for 3D Point Cloud",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-09-23T20:12:32Z",
      "url": "http://arxiv.org/abs/2309.13472v2",
      "doi": "",
      "authors": [
        "Lei Li"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper proposes an innovative approach to Hierarchical Edge Aware 3D Point Cloud Learning (HEA-Net) that seeks to address the challenges of noise in point cloud data, and improve object recognition and segmentation by focusing on edge features. In this study, we present an innovative edge-aware learning methodology, specifically designed to enhance point cloud classification and segmentation. Drawing inspiration from the human visual system, the concept of edge-awareness has been incorporated into this methodology, contributing to improved object recognition while simultaneously reducing computational time. Our research has led to the development of an advanced 3D point cloud learning framework that effectively manages object classification and segmentation tasks. A unique fusion of local and global network learning paradigms has been employed, enriched by edge-focused local and global embeddings, thereby significantly augmenting the model's interpretative prowess. Further, we have applied a hierarchical transformer architecture to boost point cloud processing efficiency, thus providing nuanced insights into structural understanding. Our approach demonstrates significant promise in managing noisy point cloud data and highlights the potential of edge-aware strategies in 3D point cloud learning. The proposed approach is shown to outperform existing techniques in object classification and segmentation tasks, as demonstrated by experiments on ModelNet40 and ShapeNet datasets."
      ]
    },
    {
      "title": "MDGroup: Multi-Grained Dual-Aware Grouping for 3D Point Cloud Instance Segmentation",
      "source": "Crossref / Electronics",
      "year": 2026,
      "date": "2026-2-24",
      "url": "https://doi.org/10.3390/electronics15050915",
      "doi": "10.3390/electronics15050915",
      "authors": [
        "Wenyun Sun",
        "Ruifeng Han"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Instance segmentation of 3D point clouds is a fundamental task for scene understanding in applications such as autonomous driving, robotics, and augmented reality. The inherent irregularity and sparsity of point clouds, compounded by scale variations and instance adhesion, pose significant challenges to accurate segmentation. Existing grouping-based methods are often limited by the loss of geometric details in single-path backbones and by error propagation near complex boundaries. To address these issues, a Multi-grained Dual-aware Grouping algorithm (MDGroup) is proposed, which explicitly integrates multi-grained feature representation with dual awareness of class and boundary. The algorithm features a Dual-Resolution 3D U-Net (DRNet) that preserves local geometric details while aggregating global semantics through adaptive alignment. A four-branch prediction scheme enhances semantic and offset estimation with boundary and directional cues, enabling fine-grained boundary modeling. Furthermore, a Hierarchical Adaptive Multi-grained Feature fusion framework (HAMF) achieves efficient cross-scale alignment by combining Class-Aware Dynamic Voxelization and Class-Aware Pyramid Scaling. Finally, a Boundary-Aware Weighted Aggregation mechanism (BAWA) refines instance grouping by dynamically weighting semantic confidence, geometric distance, boundary probability, and directional consistency. To extend the model to dynamic scenes, a Temporal Adaptive Gating (TAG) module is introduced to leverage historical frame correlations. Extensive experiments on the ScanNet v2, S3DIS, STPLS3D, SemanticKITTI, LiDAR-Net, and OCID benchmarks demonstrate that MDGroup achieves state-of-the-art performance among grouping-based methods, particularly on small objects, complex boundaries, and dynamic environments.</jats:p>"
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>We propose a fully automatic annotation scheme that takes a raw 3D point cloud with a set of fitted CAD models as input and outputs convincing point-wise labels that can be used as cheap training data for point cloud segmentation. Compared with manual annotations, we show that our automatic labels are accurate while drastically reducing the annotation time and eliminating the need for manual intervention or dataset-specific parameters. Our labeling pipeline outputs semantic classes and soft point-wise object scores, which can either be binarized into standard one-hot-encoded labels, thresholded into weak labels with ambiguous points left unlabeled, or used directly as soft labels during training. We evaluate the label quality and segmentation performance of PointNet++ on a dataset of real industrial point clouds and Scan2CAD, a public dataset of indoor scenes. Our results indicate that reducing supervision in areas that are more difficult to label automatically is beneficial compared with the conventional approach of naively assigning a hard “best guess” label to every point.</jats:p>"
      ]
    },
    {
      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-08-12T12:58:44Z",
      "url": "http://arxiv.org/abs/2508.08910v1",
      "doi": "",
      "authors": [
        "Bin Ren",
        "Xiaoshui Huang",
        "Mengyuan Liu",
        "Hong Liu",
        "Fabio Poiesi",
        "Nicu Sebe",
        "Guofeng Mei"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural B-Rep generation",
      "3D shape reconstruction to boundary representation",
      "point cloud to CAD model deep learning"
    ],
    "effective_query": "neural network direct B-Rep generation from point clouds",
    "used_override_query": false,
    "executed_queries": [
      "neural network direct B-Rep generation from point clouds",
      "boundary representation reconstruction deep learning 2023",
      "topology aware 3D point cloud to CAD faces and edges"
    ],
    "fallback_used": false
  }
}
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=7

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output contains several relevant papers, but fails to meet multiple hard requirements. The candidate depth is insufficient, with only 3 papers clearly aligned with the core topic of direct B-Rep generation from point clouds. Several papers are about general point cloud processing, segmentation, or digital twins, not B-Rep reconstruction. The query fit is poor as the set does not reflect the user's strict exclusion of CAD operation sequences, and the evidence snippets are insufficient to verify compliance with these exclusions. The core-method fit is weak, with only Point2Brep, BrepGPT, and HoLa appearing as plausible core candidates.",
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
      "reason": "3 distinct sources used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, HoLa) are clearly aligned with the core topic of direct B-Rep generation from point clouds. Others are about point cloud segmentation, digital twins, or general point cloud learning, not B-Rep reconstruction/generation."
    },
    "relevance": {
      "passed": false,
      "reason": "Among top candidates, only 2-3 are clearly aligned. Papers like 'Automatic generation of structural geometric digital twins...', 'Neural Point Cloud Diffusion...', 'Edge Aware Learning...', 'MDGroup...', 'From CAD Models to Soft Point Cloud Labels...', and 'Masked Clustering Prediction...' are not about B-Rep reconstruction/generation; they are about point cloud segmentation, digital twins, or general representation learning."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not reflect the user's strict exclusion criteria. For example, 'CAD-MLLM' mentions 'command sequences of CAD models', which strongly suggests it involves CAD operation sequences, which the user explicitly excluded. Evidence snippets are insufficient to verify that other papers avoid CAD operation sequences, CSG trees, or program synthesis."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, HoLa) plausibly look like core candidates for direct B-Rep generation from point clouds. Others are not core to the topic."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing core subtopic: there is a lack of papers specifically on neural direct B-Rep generation from point clouds published in key venues (CVPR, SIGGRAPH, etc.) between 2021-2024. The set over-relies on arXiv and includes many off-topic papers, indicating a major evidence hole."
    }
  },
  "key_risks": ["High risk of including papers that violate exclusion criteria (e.g., CAD-MLLM likely uses command sequences).", "Insufficient core papers to meet the user's request for 8-10 state-of-the-art frontier papers.", "Evidence snippets are abstract-only and do not provide enough detail to confirm the method outputs B-Rep directly without operation sequences."],
  "next_actions": ["Execute fallback queries: 'neural B-Rep generation', '3D shape reconstruction to boundary representation', 'point cloud to CAD model deep learning'.", "Focus search on specific venues: CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, ACM Transactions on Graphics.", "For each candidate, retrieve full abstract or method section to verify it outputs B-Rep directly and does not use CAD operation sequences, CSG, or program synthesis.", "Explicitly filter out papers mentioning 'command sequence', 'construction history', 'CSG', 'program synthesis', 'sketch-and-extrude' in the evidence."]
}
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods based on CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": ["direct B-Rep output from neural networks", "point cloud to B-Rep reconstruction", "geometric deep learning for B-Rep", "topology-aware 3D generation", "latent representations for B-Rep", "diffusion models for B-Rep", "autoregressive B-Rep generation"],
  "exclude_areas": ["CAD operation sequence reconstruction", "sketch-and-extrude history modeling", "CSG tree generation", "CAD program synthesis", "procedural modeling steps", "command sequences", "construction history"],
  "fallback_queries": ["neural B-Rep generation from point cloud", "B-Rep reconstruction deep learning", "point cloud to boundary representation neural network"],
  "queries": [
    {
      "query": "direct B-Rep generation neural network point cloud",
      "reason": "Targets the core requirement of end-to-end B-Rep output from unstructured 3D data, using more precise terminology."
    },
    {
      "query": "B-Rep reconstruction from point cloud CVPR",
      "reason": "Focuses search on a key high-impact venue likely to publish state-of-the-art work in the specified time range."
    },
    {
      "query": "diffusion model B-Rep generation",
      "reason": "Captures a recent trend in generative models for structured outputs, as indicated by relevant papers like BrepGPT and HoLa."
    }
  ],
  "assumptions": ["The user's 'between 2021-2026' is inclusive of both years.", "The primary input is unstructured point clouds; multimodal inputs are secondary unless they represent a major B-Rep breakthrough.", "Methods outputting a final B-Rep mesh/data structure directly are acceptable, even if they use intermediate representations.", "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, and ECCV are likely venues.", "We must verify each candidate's method section or abstract to ensure it does not rely on CAD operation sequences, CSG, or program synthesis."],
  "success_criteria": ["Retrieve papers where the model's primary output is a B-Rep structure and the method is described as direct generation/reconstruction.", "Exclude any paper reconstructing a step-by-step CAD modeling history, command sequence, or CSG tree.", "Identify 8-10 papers from the specified time window that are directly relevant, building on the 3 core candidates found.", "Cover recent advances in neural architectures (diffusion, autoregressive, latent space) for B-Rep geometry and topology."]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a revised search using the fallback queries and more targeted search terms to find relevant B-Rep generation papers while excluding CAD operation sequences.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_83tzkAOChzDSIUKuil34BINJ', arguments='{"top_k": 12, "max_results_per_source": 25, "query": "neural B-Rep generation from point cloud"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural B-Rep generation from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-Rep generation neural network point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from point cloud CVPR",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "diffusion model B-Rep generation",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    },\n    {\n      "title": "CADDreamer: CAD Object Generation from Single-view Images",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-06-10",\n      "url": "https://doi.org/10.1109/cvpr52734.2025.01998",\n      "doi": "10.1109/cvpr52734.2025.01998",\n      "authors": [\n        "Yuan Li",\n        "Cheng Lin",\n        "Yuan Liu",\n        "Xiaoxiao Long",\n        "Chenxu Zhang",\n        "Ningna Wang",\n        "Xin Li",\n        "Wenping Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Diffusion-based 3D generation has made remarkable progress in recent years. However, existing 3D generative models often produce overly dense and unstructured meshes, which stand in stark contrast to the compact, structured, and sharply-edged Computer-Aided Design (CAD) models crafted by human designers. To address this gap, we introduce CADDreamer, a novel approach for generating boundary representations (B-rep) of CAD objects from a single image. CADDreamer employs a primitive-aware multi-view diffusion model that captures both local geometric details and high-level structural semantics during the generation process. By encoding primitive semantics into the color domain, the method leverages the strong priors of pre-trained diffusion models to align with well-defined primitives. This enables the inference of multi-view normal maps and semantic maps from a single image, facilitating the reconstruction of a mesh with primitive labels. Furthermore, we introduce geometric optimization techniques and topology-preserving extraction methods to mitigate noise and distortion in the generated primitives. These enhancements result in a complete and seamless B-rep of the CAD model. Experimental results demonstrate that our method effectively recovers high-quality CAD objects from single-view images. Compared to existing 3D generation techniques, the B-rep models produced by CADDreamer are compact in representation, clear in structure, sharp in edges, and watertight in topology."\n      ]\n    },\n    {\n      "title": "B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions?",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-18T19:40:34Z",\n      "url": "http://arxiv.org/abs/2511.14870v1",\n      "doi": "",\n      "authors": [\n        "Fuyang Zhang",\n        "Pradeep Kumar Jayaraman",\n        "Xiang Xu",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents a novel geometric representation for CAD Boundary Representation (B-Rep) based on volumetric distance functions, dubbed B-Rep Distance Functions (BR-DF). BR-DF encodes the surface mesh geometry of a CAD model as signed distance function (SDF). B-Rep vertices, edges, faces and their topology information are encoded as per-face unsigned distance functions (UDFs). An extension of the Marching Cubes algorithm converts BR-DF directly into watertight CAD B-Rep model (strictly speaking a faceted B-Rep model). A surprising characteristic of BR-DF is that this conversion process never fails. Leveraging the volumetric nature of BR-DF, we propose a multi-branch latent diffusion with 3D U-Net backbone for jointly generating the SDF and per-face UDFs of a BR-DF model. Our approach achieves comparable CAD generation performance against SOTA methods while reaching the unprecedented 100% success rate in producing (faceted) B-Rep models."\n      ]\n    },\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 58 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural B-Rep generation from point cloud",\n      "B-Rep reconstruction deep learning",\n      "point cloud to boundary representation neural network"\n    ],\n    "effective_query": "neural B-Rep generation from point cloud",\n    "used_override_query": true,\n    "executed_queries": [\n      "neural B-Rep generation from point cloud",\n      "direct B-Rep generation neural network point cloud",\n      "B-Rep reconstruction from point cloud CVPR",\n      "diffusion model B-Rep generation"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_83tzkAOChzDSIUKuil34BINJ' is_error=False
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
      "query": "neural B-Rep generation from point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-Rep generation neural network point cloud",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from point cloud CVPR",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "diffusion model B-Rep generation",
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
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-01-28T04:07:59Z",
      "url": "http://arxiv.org/abs/2401.15563v3",
      "doi": "",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
      ]
    },
    {
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-07-19",
      "url": "https://doi.org/10.1145/3658129",
      "doi": "10.1145/3658129",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"
      ]
    },
    {
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-01-28",
      "url": "http://arxiv.org/abs/2401.15563",
      "doi": "10.48550/arxiv.2401.15563",
      "authors": [
        "Xiang Xu",
        "Joseph G. Lambourne",
        "Pradeep Kumar Jayaraman",
        "Zhengqing Wang",
        "Karl D. D. Willis",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."
      ]
    },
    {
      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-01-23T14:15:02Z",
      "url": "http://arxiv.org/abs/2601.16771v1",
      "doi": "",
      "authors": [
        "Jiahao Li",
        "Yunpeng Bai",
        "Yongkang Dai",
        "Hao Guo",
        "Hongping Gan",
        "Yilei Shi"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep's geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."
      ]
    },
    {
      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-12-02T18:46:25Z",
      "url": "http://arxiv.org/abs/2512.03018v1",
      "doi": "",
      "authors": [
        "Xiang Xu",
        "Pradeep Kumar Jayaraman",
        "Joseph G. Lambourne",
        "Yilin Liu",
        "Durvesh Malpure",
        "Pete Meltzer"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."
      ]
    },
    {
      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-03-17T12:34:14Z",
      "url": "http://arxiv.org/abs/2503.13110v1",
      "doi": "",
      "authors": [
        "Jing Li",
        "Yihang Fu",
        "Falai Chen"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."
      ]
    },
    {
      "title": "CADDreamer: CAD Object Generation from Single-view Images",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-06-10",
      "url": "https://doi.org/10.1109/cvpr52734.2025.01998",
      "doi": "10.1109/cvpr52734.2025.01998",
      "authors": [
        "Yuan Li",
        "Cheng Lin",
        "Yuan Liu",
        "Xiaoxiao Long",
        "Chenxu Zhang",
        "Ningna Wang",
        "Xin Li",
        "Wenping Wang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Diffusion-based 3D generation has made remarkable progress in recent years. However, existing 3D generative models often produce overly dense and unstructured meshes, which stand in stark contrast to the compact, structured, and sharply-edged Computer-Aided Design (CAD) models crafted by human designers. To address this gap, we introduce CADDreamer, a novel approach for generating boundary representations (B-rep) of CAD objects from a single image. CADDreamer employs a primitive-aware multi-view diffusion model that captures both local geometric details and high-level structural semantics during the generation process. By encoding primitive semantics into the color domain, the method leverages the strong priors of pre-trained diffusion models to align with well-defined primitives. This enables the inference of multi-view normal maps and semantic maps from a single image, facilitating the reconstruction of a mesh with primitive labels. Furthermore, we introduce geometric optimization techniques and topology-preserving extraction methods to mitigate noise and distortion in the generated primitives. These enhancements result in a complete and seamless B-rep of the CAD model. Experimental results demonstrate that our method effectively recovers high-quality CAD objects from single-view images. Compared to existing 3D generation techniques, the B-rep models produced by CADDreamer are compact in representation, clear in structure, sharp in edges, and watertight in topology."
      ]
    },
    {
      "title": "B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions?",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-11-18T19:40:34Z",
      "url": "http://arxiv.org/abs/2511.14870v1",
      "doi": "",
      "authors": [
        "Fuyang Zhang",
        "Pradeep Kumar Jayaraman",
        "Xiang Xu",
        "Yasutaka Furukawa"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper presents a novel geometric representation for CAD Boundary Representation (B-Rep) based on volumetric distance functions, dubbed B-Rep Distance Functions (BR-DF). BR-DF encodes the surface mesh geometry of a CAD model as signed distance function (SDF). B-Rep vertices, edges, faces and their topology information are encoded as per-face unsigned distance functions (UDFs). An extension of the Marching Cubes algorithm converts BR-DF directly into watertight CAD B-Rep model (strictly speaking a faceted B-Rep model). A surprising characteristic of BR-DF is that this conversion process never fails. Leveraging the volumetric nature of BR-DF, we propose a multi-branch latent diffusion with 3D U-Net backbone for jointly generating the SDF and per-face UDFs of a BR-DF model. Our approach achieves comparable CAD generation performance against SOTA methods while reaching the unprecedented 100% success rate in producing (faceted) B-Rep models."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 58 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural B-Rep generation from point cloud",
      "B-Rep reconstruction deep learning",
      "point cloud to boundary representation neural network"
    ],
    "effective_query": "neural B-Rep generation from point cloud",
    "used_override_query": true,
    "executed_queries": [
      "neural B-Rep generation from point cloud",
      "direct B-Rep generation neural network point cloud",
      "B-Rep reconstruction from point cloud CVPR",
      "diffusion model B-Rep generation"
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
  "review_summary": "The retrieval output shows significant improvement in topic alignment, with many papers explicitly about B-Rep generation. However, critical hard requirements are still not met. The candidate depth is insufficient due to extensive duplication (58 duplicates merged), leaving only 9 distinct papers, some of which violate exclusion criteria (e.g., Brep2Seq outputs 'parametrized feature-based modeling operations', which likely involves CAD operation sequences). The evidence snippets are insufficient to verify that all papers avoid CAD operation sequences, CSG, or program synthesis. The core-method fit is weak because several papers are generative only, not reconstruction from point clouds as the user prioritized. The set lacks sufficient papers focused on point cloud to B-Rep reconstruction.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "3 distinct sources used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, only 9 distinct candidate papers remain (Point2Brep, BrepGPT, BrepGen, AutoRegressive Generation with B-rep Holistic Token Sequence Representation, AutoBrep, DTGBrepGen, GraphBrep, CADDreamer, B-Rep Distance Functions, Brep2Seq). This is below the required 10, and some are not valid (Brep2Seq likely violates exclusions)."
    },
    "relevance": {
      "passed": true,
      "reason": "Among top candidates, at least 2-3 are clearly aligned with direct B-Rep generation (e.g., Point2Brep, BrepGPT, BrepGen)."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The set does not fully reflect user constraints. Brep2Seq explicitly mentions 'parametrized feature-based modeling operations', which strongly suggests CAD operation sequences, a hard exclusion. CADDreamer generates from single-view images, not point clouds, which is secondary unless a major breakthrough; evidence does not establish it as such. Many papers are unconditional generative models, not reconstruction from point clouds as the user prioritized."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 3 papers (Point2Brep, BrepGPT, BrepGen) plausibly look like core candidates for direct B-Rep generation from point clouds. Others are either generative only (not reconstruction), or input is images (CADDreamer), or may involve operation sequences (Brep2Seq)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "Obvious missing core subtopic: insufficient papers on point cloud to B-Rep reconstruction. The set is skewed towards unconditional generative models and image-conditioned generation. Major evidence hole: lack of verification that papers avoid CAD operation sequences; evidence snippets are abstract-only and insufficient."
    }
  },
  "key_risks": ["High risk of including papers that violate exclusion criteria (e.g., Brep2Seq).", "Insufficient papers focused on point cloud to B-Rep reconstruction, which is the user's highest priority.", "Evidence snippets are abstract-only and do not provide enough detail to confirm the method outputs B-Rep directly without operation sequences or CSG.", "Candidate depth is borderline even after deduplication, and some candidates are off-topic."],
  "next_actions": ["Execute targeted query: 'point cloud to B-Rep reconstruction neural network 2023 2024 2025' to prioritize reconstruction over unconditional generation.", "For each candidate, retrieve full method section or explicit statements to verify it does not use CAD operation sequences, CSG, or program synthesis.", "Explicitly filter out papers mentioning 'feature-based modeling operations', 'command sequence', 'construction history', 'CSG', 'program synthesis'.", "Search for papers in CVPR, SIGGRAPH, ICCV, ECCV, NeurIPS from 2021-2024 that specifically address B-Rep reconstruction from point clouds."]
}
```

### Message 14

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal was to find 8-10 state-of-the-art research papers (2021-2026) focused on the direct neural generation or reconstruction of 3D Boundary Representation (B-Rep) data structures. The core requirement is that the model's primary output is the B-Rep itself (faces, edges, vertices, and topology), not a sequence of modeling operations. The highest-priority input is unstructured point clouds or 3D scans. The search strictly excluded methods based on CAD operation sequences, CSG trees, or program synthesis.

## Search Strategy
The search was conducted in multiple phases using sources including Crossref, OpenAlex, and arXiv. Initial queries targeted "neural network direct B-Rep generation from point clouds." A subsequent revision, prompted by reviewer feedback, employed more precise queries like "direct B-Rep generation neural network point cloud" and "diffusion model B-Rep generation" to better capture recent generative architectures. The strategy prioritized high-impact venues (CVPR, SIGGRAPH) and aimed to verify that each candidate's method avoided the excluded categories. Despite these efforts, the final retrieval did not yield a sufficient number of verified, on-topic papers that met all hard constraints.

## Candidate Papers
**The search did not clear the quality bar.** The reviewer's final decision was REVISE, indicating the retrieved set did not meet critical requirements: insufficient candidate depth, high risk of including papers that violate exclusion criteria (e.g., generating CAD operation sequences), and a lack of focus on the prioritized task of point-cloud-to-B-Rep reconstruction. Below is a breakdown of the findings.

### Verified Candidates
Based on the evidence snippets, no papers achieved a `verified` status. The following papers have `partial` verification and are the strongest leads that appear to align with the core topic, though their compliance with all exclusion criteria could not be fully confirmed.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)**
    *   **Source:** Crossref
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Core Contribution:** A two-stage framework that segments point clouds into surface patches and then predicts geometric distance fields to recover B-Rep edges, vertices, and connectivity, integrating learning with explicit geometric reasoning.
    *   **Relevance Note:** Directly targets B-Rep reconstruction from unstructured point clouds. The abstract describes outputting "complete and topologically consistent B-rep models," with no mention of operation sequences.

*   **BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch (2025)**
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2511.22171v1
    *   **Core Contribution:** Proposes a single-stage autoregressive framework using a novel Voronoi Half-Patch representation and a decoder-only Transformer to generate B-Rep tokens, which are decoded into complete models.
    *   **Relevance Note:** Describes direct B-Rep generation. The framework supports conditional generation from point clouds, among other inputs. The method appears to output the B-Rep structure directly.

*   **HoLa: B-Rep Generation using a Holistic Latent Representation (2025)**
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2504.14257v3
    *   **Core Contribution:** Introduces a holistic latent space that unifies B-Rep geometry and topology, enabling a diffusion-based generator to produce B-Reps from various inputs, including point clouds.
    *   **Relevance Note:** Focuses on generating the full B-Rep data structure. The method learns to derive curve geometry from surface pairs, implicitly encoding topology without reconstructing a modeling history.

### Unverified Leads
The following papers have titles strongly related to B-Rep generation but lack sufficient evidence in the provided snippets to confirm they avoid CAD operation sequences or prioritize point cloud input. They are presented as potential leads for follow-up investigation, not as verified recommendations.

1.  **BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024)** - A diffusion model that directly outputs a B-Rep using a hierarchical tree representation. (Needs verification that it does not use CSG or operation sequences).
2.  **AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025)** - A Transformer model that tokenizes B-Rep geometry and topology for autoregressive generation. (Input modality and exclusion compliance need verification).
3.  **B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions? (2025)** - Proposes a volumetric distance function representation for B-Reps and a diffusion model for generation. (Application to point cloud input is unclear).

## Notes and Gaps
*   **Evidence Gap:** The search relied primarily on paper abstracts. This level of evidence is insufficient to conclusively verify that a method does **not** rely on CAD operation sequences, CSG, or program synthesis, which was a critical user requirement.
*   **Topic Skew:** The retrieved set is skewed towards **unconditional B-Rep generation** or **image-conditioned generation**. There is a notable shortage of papers specifically addressing **reconstruction from point clouds**, which was the user's highest priority.
*   **Exclusion Risks:** Several promising papers (e.g., `Brep2Seq`) were identified but their abstracts contained terms like "parametrized feature-based modeling operations," which strongly suggest a violation of the exclusion criteria. These were therefore not included as verified candidates.
*   **Venue Coverage:** The search successfully identified relevant pre-prints (arXiv) but found fewer papers from major computer vision/geometry conferences (CVPR, SIGGRAPH, etc.) within the 2021-2024 period that strictly met all criteria.

## Recommended Next Steps
1.  **Manual Verification:** The most critical step is to manually review the full text of the "Verified Candidates" (`Point2Brep`, `BrepGPT`, `HoLa`) to definitively confirm they output B-Reps directly and do not use any prohibited methodologies.
2.  **Targeted Search:** Conduct a new, highly targeted search using queries that combine reconstruction and exclusion terms, such as:
    *   `"B-rep reconstruction" point cloud -"operation sequence" -CSG -"program synthesis"`
    *   `"boundary representation" "point cloud" neural network -sketch -extrude`
3.  **Citation Tracking:** Use the "Verified Candidates" as seeds for backward and forward citation analysis to discover related work that may have been missed.
4.  **Venue-Specific Search:** Manually browse the proceedings of key conferences (SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, ECCV) from 2022-2025 for sessions related to 3D reconstruction, geometric deep learning, and CAD.

TERMINATE
```
