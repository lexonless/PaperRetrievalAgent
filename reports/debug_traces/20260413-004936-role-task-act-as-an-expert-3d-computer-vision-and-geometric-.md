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
**Generated At:** 2026-04-13T00:49:36
**Stop Reason:** Text 'TERMINATE' mentioned

## Run Summary

- Stop reason: `Text 'TERMINATE' mentioned`
- Total messages: `20`
- Planner JSON messages: `3`
- Retrieval JSON messages: `3`
- Review decisions seen: `3`
- Tool activity events: `6`

## Planner Outputs

### Planner Output 2

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction",
    "deep learning boundary representation generation",
    "point cloud to CAD boundary representation"
  ],
  "queries": [
    {
      "query": "neural direct B-Rep generation from point clouds",
      "reason": "Targets the core task of generating boundary representation data structures directly from unstructured 3D data using neural methods."
    },
    {
      "query": "end-to-end learning of B-Rep topology and geometry",
      "reason": "Focuses on modern architectures that learn to output the complete topological graph and geometric surfaces without intermediate operation sequences."
    },
    {
      "query": "latent diffusion models for B-Rep shape generation",
      "reason": "Captures recent advanced generative approaches (post-2022) that might be applied to structured CAD outputs like B-Reps."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic."
  ],
  "success_criteria": [
    "Retrieve 8-10 papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps."
  ]
}
```

### Planner Output 8

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps",
    "neural implicit surface reconstruction (unless it explicitly outputs a B-Rep)"
  ],
  "fallback_queries": [
    "B-Rep reconstruction from 3D scan deep learning",
    "boundary representation generation neural network",
    "CAD B-Rep learning from point cloud"
  ],
  "queries": [
    {
      "query": "point cloud to boundary representation reconstruction neural network",
      "reason": "Directly targets the core task of converting unstructured 3D data into a structured B-Rep using neural methods, addressing the primary input requirement."
    },
    {
      "query": "B-Rep generation diffusion model transformer",
      "reason": "Captures recent advanced generative architectures (post-2022) that are state-of-the-art for structured output generation, as seen in initial results."
    },
    {
      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",
      "reason": "Focuses on high-impact conference venues to improve source diversity and find published papers beyond preprint repositories."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic.",
    "We must diversify sources beyond arXiv and Crossref/OpenAlex overlaps to include Semantic Scholar, DBLP, or direct publisher indexes to meet source coverage requirements."
  ],
  "success_criteria": [
    "Retrieve 8-10 distinct papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history or implicit surface.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps.",
    "Improve source diversity by using at least 3 distinct scholarly sources (e.g., Semantic Scholar, DBLP, publisher sites) in addition to initial sources."
  ]
}
```

### Planner Output 14

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations",
    "point cloud to B-Rep reconstruction"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps",
    "neural implicit surface reconstruction (unless it explicitly outputs a B-Rep)"
  ],
  "fallback_queries": [
    "3D scan to boundary representation deep learning",
    "neural network B-Rep reconstruction from point cloud",
    "CAD model reconstruction from point cloud B-Rep"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2023",
      "reason": "Directly targets the core reconstruction task from point clouds with a recent year filter to capture state-of-the-art methods within the range."
    },
    {
      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",
      "reason": "Focuses on high-impact conference venues (CVPR) to improve source diversity and find published papers on reconstruction, not just generation."
    },
    {
      "query": "neural B-Rep generation from point cloud diffusion",
      "reason": "Captures hybrid approaches that might generate B-Reps conditionally from point clouds using modern architectures like diffusion models."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic.",
    "We must diversify sources beyond arXiv and OpenAlex overlaps to include Semantic Scholar, DBLP, or direct publisher indexes to meet source coverage requirements.",
    "The primary input focus is point clouds or 3D scans; we will prioritize papers that explicitly mention these inputs in abstracts or titles."
  ],
  "success_criteria": [
    "Retrieve 8-10 distinct papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history or implicit surface.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps.",
    "Improve source diversity by using at least 3 distinct scholarly sources (e.g., Semantic Scholar, DBLP, publisher sites) in addition to initial sources.",
    "Balance the set to include both reconstruction-from-point-clouds and generative models, with emphasis on reconstruction."
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
      "query": "neural direct B-Rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "end-to-end learning of B-Rep topology and geometry",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "latent diffusion models for B-Rep shape generation",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
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
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-07-27",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. ≈50%."
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
      "title": "Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6301470",
      "doi": "10.2139/ssrn.6301470",
      "authors": [
        "Fulin Tang",
        "An Liu",
        "Rudong Xue",
        "Bingxi Liu",
        "ZeJin Gao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents an unsupervised method for directly learning neural implicit functions from 3D point clouds, aiming to tackle the core challenge of lacking ground-truth implicit values for supervisory training. Current approaches typically rely on global geometric constraints to learn implicit functions; however, this strategy often causes the optimization process to fall into local minima, resulting in over-smoothing artifacts, loss of fine geometric details, and blurring of sharp features.Although hand-crafted filters can be applied to point clouds to capture high-frequency details—thereby mitigating over-smoothing of geometric structures and avoiding the generation of coarse surfaces—their performance is highly dependent on manual parameter tuning, which severely restricts their generalization ability across diverse 3D shapes.To address these limitations, we propose a dynamic graph filter that integrates the adaptability of graph neural networks with the geometric characteristics of hand-crafted bilateral filters, enabling the learning of high-quality neural implicit functions from 3D point clouds. Our approach dynamically evolves graph features during the training process, automatically capturing high-frequency geometric details without the need for manual parameter adjustment.Ultimately, high-quality surface reconstruction can be achieved from the learned neural implicit function, even in the complete absence of ground-truth supervision. Experimental results on multiple datasets demonstrate that our proposed method effectively preserves complex geometric details and sharp features, achieving superior surface reconstruction quality compared to state-of-the-art approaches.</jats:p>"
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
      "neural network B-Rep reconstruction",
      "deep learning boundary representation generation",
      "point cloud to CAD boundary representation"
    ],
    "effective_query": "neural direct B-Rep generation from point clouds",
    "used_override_query": true,
    "executed_queries": [
      "neural direct B-Rep generation from point clouds",
      "end-to-end learning of B-Rep topology and geometry",
      "latent diffusion models for B-Rep shape generation"
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
      "query": "point cloud to boundary representation reconstruction neural network",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep generation diffusion model transformer",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",
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
      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-06-10",
      "url": "https://doi.org/10.1109/cvpr52734.2025.01997",
      "doi": "10.1109/cvpr52734.2025.01997",
      "authors": [
        "Jing Li",
        "Yangyang Fu",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
      ]
    },
    {
      "title": "HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-04-03T08:06:51Z",
      "url": "http://arxiv.org/abs/2604.02847v1",
      "doi": "",
      "authors": [
        "Shurui Liu",
        "Weide Chen",
        "Ancong Wu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the standard 3D modeling format in CAD systems, encoding both geometric primitives and topological connectivity. Despite its prevalence, deep generative modeling of valid B-rep structures remains challenging due to the intricate interplay between discrete topology and continuous geometry. In this paper, we propose HiDiGen, a hierarchical generation framework that decouples geometry modeling into two stages, each guided by explicitly modeled topological constraints. Specifically, our approach first establishes face-edge incidence relations to define a coherent topological scaffold, upon which face proxies and initial edge curves are generated. Subsequently, multiple Transformer-based diffusion modules are employed to refine the geometry by generating precise face surfaces and vertex positions, with edge-vertex adjacencies dynamically established and enforced to preserve structural consistency. This progressive geometry hierarchy enables the generation of more novel and diverse shapes, while two-stage topological modeling ensures high validity. Experimental results show that HiDiGen achieves strong performance, generating novel, diverse, and topologically sound CAD models."
      ]
    },
    {
      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-01-23T14:15:02Z",
      "url": "http://arxiv.org/abs/2601.16771v2",
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 2 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "B-Rep reconstruction from 3D scan deep learning",
      "boundary representation generation neural network",
      "CAD B-Rep learning from point cloud"
    ],
    "effective_query": "point cloud to boundary representation reconstruction neural network",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to boundary representation reconstruction neural network",
      "B-Rep generation diffusion model transformer",
      "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH"
    ],
    "fallback_used": false
  }
}
```

### Retrieval Output 18

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
      "query": "point cloud to B-Rep reconstruction neural network 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "neural B-Rep generation from point cloud diffusion",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p id=\"p1\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."
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
      "title": "DPR-GAN: Dual-Stream Progressive Refinement for Adversarial 3D Point Cloud Generation",
      "source": "Crossref / Neural Processing Letters",
      "year": 2024,
      "date": "2024-2-24",
      "url": "https://doi.org/10.1007/s11063-024-11454-x",
      "doi": "10.1007/s11063-024-11454-x",
      "authors": [
        "Xiangyang Wang",
        "Jiale Chen",
        "Rui Wang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title><jats:p>Point cloud generation aims to transfer a latent code to realistic 3D shapes through generative models. However, most of progressive generative methods ignore the spatial relationship among different stages and suffer from the loss of contextual information. To address this issue, we propose dual-stream progressive refinement adversarial network (DPR-GAN), which utilizes a dual-stream structure to establish the relationship between two adjacent stages. Such a mechanism can learn the spatial context and preserve more spatial details of point clouds at different stages. In addition, DPR-GAN adopts 3D gridding transformation to guide the shape deformation. In this way, 3D gridding transformation can learn a reasonable correspondence between the local regions of 3D shapes and latent codes. Benefiting from the uniformity and adaptability of the 3D grids, our proposed DPR-GAN can improve the quality and consistency of generated point clouds. We conduct comprehensive experiments to demonstrate that the proposed DPR-GAN is capable of generating pluralistic point clouds, as compared with state-of-the-art generation methods in terms of both visual and quantitative evaluations.</jats:p>"
      ]
    },
    {
      "title": "GRASP-Net: Geometric Residual Analysis and Synthesis for Point Cloud Compression",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-09-09T17:09:02Z",
      "url": "http://arxiv.org/abs/2209.04401v1",
      "doi": "",
      "authors": [
        "Jiahao Pang",
        "Muhammad Asad Lodhi",
        "Dong Tian"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Point cloud compression (PCC) is a key enabler for various 3-D applications, owing to the universality of the point cloud format. Ideally, 3D point clouds endeavor to depict object/scene surfaces that are continuous. Practically, as a set of discrete samples, point clouds are locally disconnected and sparsely distributed. This sparse nature is hindering the discovery of local correlation among points for compression. Motivated by an analysis with fractal dimension, we propose a heterogeneous approach with deep learning for lossy point cloud geometry compression. On top of a base layer compressing a coarse representation of the input, an enhancement layer is designed to cope with the challenging geometric residual/details. Specifically, a point-based network is applied to convert the erratic local details to latent features residing on the coarse point cloud. Then a sparse convolutional neural network operating on the coarse point cloud is launched. It utilizes the continuity/smoothness of the coarse geometry to compress the latent features as an enhancement bit-stream that greatly benefits the reconstruction quality. When this bit-stream is unavailable, e.g., due to packet loss, we support a skip mode with the same architecture which generates geometric details from the coarse point cloud directly. Experimentation on both dense and sparse point clouds demonstrate the state-of-the-art compression performance achieved by our proposal. Our code is available at https://github.com/InterDigitalInc/GRASP-Net."
      ]
    },
    {
      "title": "3D Point Cloud Compression with Recurrent Neural Network and Image Compression Methods",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-02-18T19:08:19Z",
      "url": "http://arxiv.org/abs/2402.11680v1",
      "doi": "",
      "authors": [
        "Till Beemelmanns",
        "Yuchen Tao",
        "Bastian Lampe",
        "Lennart Reiher",
        "Raphael van Kempen",
        "Timo Woopen",
        "Lutz Eckstein"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Storing and transmitting LiDAR point cloud data is essential for many AV applications, such as training data collection, remote control, cloud services or SLAM. However, due to the sparsity and unordered structure of the data, it is difficult to compress point cloud data to a low volume. Transforming the raw point cloud data into a dense 2D matrix structure is a promising way for applying compression algorithms. We propose a new lossless and calibrated 3D-to-2D transformation which allows compression algorithms to efficiently exploit spatial correlations within the 2D representation. To compress the structured representation, we use common image compression methods and also a self-supervised deep compression approach using a recurrent neural network. We also rearrange the LiDAR's intensity measurements to a dense 2D representation and propose a new metric to evaluate the compression performance of the intensity. Compared to approaches that are based on generic octree point cloud compression or based on raw point cloud data compression, our approach achieves the best quantitative and visual performance. Source code and dataset are available at https://github.com/ika-rwth-aachen/Point-Cloud-Compression."
      ]
    },
    {
      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-06-23T02:21:48Z",
      "url": "http://arxiv.org/abs/2406.15982v1",
      "doi": "",
      "authors": [
        "Yangdi Lu",
        "Wenbo He"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and safety; smart operation, building management and health monitoring; and durability, life cycle analysis, and circular economy. This paper presents a unique perspective on applications of AI/DL/ML in these domains for the complete building lifecycle, from conceptual stage, design stage, construction stage, operational and maintenance stage until the end of life. Furthermore, data collection strategies using smart vision and sensors, data cleaning methods (post-processing), data storage for developing these models are discussed, and the challenges in model development and strategies to overcome these challenges are elaborated. Future trends in these domains and possible research avenues are also presented."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "3D scan to boundary representation deep learning",
      "neural network B-Rep reconstruction from point cloud",
      "CAD model reconstruction from point cloud B-Rep"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2023",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2023",
      "B-Rep reconstruction from 3D scan deep learning CVPR",
      "neural B-Rep generation from point cloud diffusion"
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
  "review_summary": "The retrieval captured several highly relevant papers (Point2Brep, BrepGen, ComplexGen, HoLa, AutoBrep, BrepGPT) that directly output B-Reps from point clouds or via generative models, satisfying the core topic and exclusions. However, the set fails the hard requirement for source coverage (only 2 distinct sources used: Crossref, OpenAlex, arXiv; but arXiv is a preprint repository, not a distinct scholarly source like a publisher or index). Additionally, the evidence snippets are strong but the candidate depth is borderline (5 unique in-range papers after merging duplicates, but one is a duplicate entry and another is about neural implicit functions, which is not direct B-Rep generation). The time range is respected, and metadata is mostly complete. A revise is needed to broaden source coverage and ensure a robust set of 8-10 distinct, in-range core papers.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct scholarly sources were effectively used (Crossref, OpenAlex). arXiv is a preprint repository, not a distinct publisher/index. The user did not explicitly restrict the search space, so at least 2 distinct sources are required. This set relies heavily on arXiv and Crossref/OpenAlex overlaps."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, there are 7 unique papers. However, 'Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering' is about surface reconstruction via implicit functions, not direct B-Rep generation (output is not a B-Rep data structure). Removing that leaves 6. Among these, 'HoLa' appears twice from different sources but is the same paper. Thus, only 5 distinct in-range candidate papers remain that are potentially core to the topic, which is below the minimum of 5 non-duplicate candidates required for a robust set aiming for 8-10."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 3 (Point2Brep, BrepGen, ComplexGen) are clearly aligned with the user's topic of direct B-Rep generation from point clouds or generative modeling, not just keyword overlap."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set reflects the user's constraints: papers are from 2021-2026, focus on direct B-Rep output, use neural architectures, and avoid CAD operation sequences, CSG, and program synthesis."
    },
    "core_method_fit": {
      "passed": true,
      "reason": "At least 3 papers (Point2Brep, BrepGen, ComplexGen) are plausible core candidates for direct B-Rep generation from point clouds or generative modeling, based on title and abstract evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious missing core subtopic or major evidence hole is apparent from the current set, though the limited number of distinct papers suggests the coverage may be incomplete."
    }
  },
  "key_risks": [
    "Source diversity is insufficient; over-reliance on arXiv and Crossref/OpenAlex may miss venue-published papers from SIGGRAPH, CVPR, etc.",
    "Candidate depth is borderline; the set includes only ~5 distinct core papers, short of the target 8-10.",
    "One paper (Unsupervised Learning of Neural Implicit Functions...) is likely irrelevant as it outputs implicit surfaces, not B-Reps."
  ],
  "next_actions": [
    "Execute a new search using additional distinct sources (e.g., Semantic Scholar, DBLP, or direct conference proceedings) to improve source coverage.",
    "Refine queries to explicitly target point-cloud-to-B-Rep reconstruction, e.g., 'point cloud to boundary representation reconstruction neural network' or 'B-Rep reconstruction from 3D scan deep learning'.",
    "Filter out papers that are not directly about B-Rep generation (e.g., neural implicit surface reconstruction) and ensure each candidate outputs a B-Rep data structure as per the user's strict inclusion criteria."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has improved, capturing a strong set of highly relevant papers on direct B-Rep generation using modern neural architectures (diffusion, autoregressive, graph-based). The papers are within the 2021-2026 range and strictly avoid excluded categories. However, the hard requirement for source coverage is still not met: only 2 distinct scholarly sources were effectively used (arXiv and OpenAlex; Crossref appears in the list but not as a distinct source for unique papers). The user did not restrict the search space, so at least 2 distinct sources are required. Additionally, while candidate depth is better (8 unique papers after merging duplicates), the evidence snippets are strong but the set is heavily skewed towards generative models (BrepGen, DTGBrepGen, AutoBrep, HiDiGen, BrepARG, GraphBrep) with only one clear reconstruction-from-point-clouds paper (ComplexGen). The user's primary focus is on reconstruction from point clouds, so this imbalance is a gap. A revise is needed to diversify sources and ensure more papers on point-cloud-to-B-Rep reconstruction are included.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct scholarly sources were effectively used: arXiv (preprint repository) and OpenAlex (index). Crossref appears in the sources_used list but no unique papers are attributed solely to Crossref; all papers are from arXiv or OpenAlex. The user did not explicitly restrict the search space, so at least 2 distinct sources are required. This set still relies heavily on arXiv and OpenAlex overlaps."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, there are 8 unique candidate papers (BrepGen, DTGBrepGen, AutoBrep, ComplexGen, HiDiGen, BrepARG, GraphBrep, and one duplicate merged). This meets the minimum of 5 non-duplicate candidates."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 3 (BrepGen, ComplexGen, DTGBrepGen) are clearly aligned with the user's topic of direct B-Rep generation, using neural architectures and outputting B-Rep data structures."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set reflects the user's constraints: papers are from 2021-2026, focus on direct B-Rep output, use neural architectures, and avoid CAD operation sequences, CSG, and program synthesis. However, the primary input focus (point clouds) is underrepresented."
    },
    "core_method_fit": {
      "passed": true,
      "reason": "At least 3 papers (BrepGen, ComplexGen, DTGBrepGen) are plausible core candidates for direct B-Rep generation, based on title and abstract evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: reconstruction from point clouds. The user's primary focus is 'B-Rep reconstruction and generation from point clouds', but the set is heavily skewed towards unconditional generative models (BrepGen, DTGBrepGen, AutoBrep, HiDiGen, BrepARG, GraphBrep) with only one clear reconstruction-from-point-clouds paper (ComplexGen). This imbalance is a significant gap."
    }
  },
  "key_risks": [
    "Source diversity is insufficient; over-reliance on arXiv and OpenAlex may miss venue-published papers from other indexes.",
    "The set is imbalanced: heavily focused on generative models (diffusion/autoregressive) with limited representation of reconstruction from point clouds, which is the user's primary input requirement.",
    "Some papers may not explicitly handle point cloud input; evidence snippets do not always specify input modality."
  ],
  "next_actions": [
    "Execute a new search using additional distinct sources (e.g., Semantic Scholar, DBLP, or direct conference proceedings like CVPR, SIGGRAPH) to improve source coverage.",
    "Refine queries to explicitly target point-cloud-to-B-Rep reconstruction, e.g., 'point cloud to B-Rep reconstruction neural network 2023' or '3D scan to boundary representation deep learning'.",
    "Prioritize papers that explicitly mention point clouds or 3D scans as input in their abstracts to ensure alignment with the user's primary focus."
  ]
}
```

### Review 19

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has severely regressed. While source coverage now includes Crossref, OpenAlex, and arXiv (3 distinct sources), the relevance of the papers is extremely poor. Only 2 papers (BrepGen and ComplexGen) are directly about B-Rep generation/reconstruction; the remaining 8 are about point cloud completion, compression, single-image 3D reconstruction, or general surveys, which do not output B-Rep data structures and violate the user's strict exclusion criteria. The candidate depth is insufficient for core B-Rep papers, and the set fails the relevance and core-method-fit hard requirements. A revise is urgently needed to refocus on the core topic and exclude irrelevant papers.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "3 distinct sources were used: Crossref, OpenAlex, and arXiv. This meets the requirement of at least 2 distinct sources."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, there are 10 candidate papers, but only 2 (BrepGen, ComplexGen) are about direct B-Rep generation/reconstruction. The others are irrelevant (point cloud completion, compression, etc.). Thus, the number of non-duplicate candidates relevant to the topic is below the minimum of 5."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 2 are clearly aligned with the user's topic of direct B-Rep generation from point clouds. The majority are about point cloud completion, compression, or general AI surveys, which do not output B-Rep data structures."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "The retrieved set does not reflect the user's constraints: most papers do not output B-Rep data structures, and many are about point cloud compression, completion, or single-image reconstruction, which are outside the scope."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers (BrepGen, ComplexGen) are plausible core candidates for direct B-Rep generation. The rest are not about B-Rep output."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: the set is dominated by irrelevant papers, leaving a huge gap in relevant B-Rep reconstruction/generation papers."
    }
  },
  "key_risks": [
    "Extreme irrelevance: most papers are about point cloud completion, compression, or general AI surveys, not B-Rep generation/reconstruction.",
    "The set includes only 2 core B-Rep papers, far short of the target 8-10.",
    "The retrieval appears to have been misled by broad queries that captured point cloud methods unrelated to B-Rep."
  ],
  "next_actions": [
    "Execute a new search with strict keyword filtering to exclude irrelevant topics. Use queries like: '\"B-Rep\" reconstruction point cloud neural' or '\"boundary representation\" generation from point cloud deep learning'.",
    "Explicitly exclude papers with keywords like 'compression', 'completion', 'survey', 'LiDAR', 'NeRF', 'image-based' unless they also mention B-Rep output.",
    "Prioritize papers from known relevant venues (SIGGRAPH, CVPR, NeurIPS) that have previously published B-Rep work, and verify each candidate's output is a B-Rep data structure via abstract evidence."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_4IWkq9xNE2lVHMlXkz1C4cl3', arguments='{"query": "neural direct B-Rep generation from point clouds", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural direct B-Rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end learning of B-Rep topology and geometry",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "latent diffusion models for B-Rep shape generation",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-27",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. ≈50%."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6301470",\n      "doi": "10.2139/ssrn.6301470",\n      "authors": [\n        "Fulin Tang",\n        "An Liu",\n        "Rudong Xue",\n        "Bingxi Liu",\n        "ZeJin Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents an unsupervised method for directly learning neural implicit functions from 3D point clouds, aiming to tackle the core challenge of lacking ground-truth implicit values for supervisory training. Current approaches typically rely on global geometric constraints to learn implicit functions; however, this strategy often causes the optimization process to fall into local minima, resulting in over-smoothing artifacts, loss of fine geometric details, and blurring of sharp features.Although hand-crafted filters can be applied to point clouds to capture high-frequency details—thereby mitigating over-smoothing of geometric structures and avoiding the generation of coarse surfaces—their performance is highly dependent on manual parameter tuning, which severely restricts their generalization ability across diverse 3D shapes.To address these limitations, we propose a dynamic graph filter that integrates the adaptability of graph neural networks with the geometric characteristics of hand-crafted bilateral filters, enabling the learning of high-quality neural implicit functions from 3D point clouds. Our approach dynamically evolves graph features during the training process, automatically capturing high-frequency geometric details without the need for manual parameter adjustment.Ultimately, high-quality surface reconstruction can be achieved from the learned neural implicit function, even in the complete absence of ground-truth supervision. Experimental results on multiple datasets demonstrate that our proposed method effectively preserves complex geometric details and sharp features, achieving superior surface reconstruction quality compared to state-of-the-art approaches.</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction",\n      "deep learning boundary representation generation",\n      "point cloud to CAD boundary representation"\n    ],\n    "effective_query": "neural direct B-Rep generation from point clouds",\n    "used_override_query": true,\n    "executed_queries": [\n      "neural direct B-Rep generation from point clouds",\n      "end-to-end learning of B-Rep topology and geometry",\n      "latent diffusion models for B-Rep shape generation"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_4IWkq9xNE2lVHMlXkz1C4cl3' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_vrVuUkcvZS2s94FpDgROFWfx', arguments='{"query": "point cloud to boundary representation reconstruction neural network", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to boundary representation reconstruction neural network",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep generation diffusion model transformer",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-06-10",\n      "url": "https://doi.org/10.1109/cvpr52734.2025.01997",\n      "doi": "10.1109/cvpr52734.2025.01997",\n      "authors": [\n        "Jing Li",\n        "Yangyang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-04-03T08:06:51Z",\n      "url": "http://arxiv.org/abs/2604.02847v1",\n      "doi": "",\n      "authors": [\n        "Shurui Liu",\n        "Weide Chen",\n        "Ancong Wu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the standard 3D modeling format in CAD systems, encoding both geometric primitives and topological connectivity. Despite its prevalence, deep generative modeling of valid B-rep structures remains challenging due to the intricate interplay between discrete topology and continuous geometry. In this paper, we propose HiDiGen, a hierarchical generation framework that decouples geometry modeling into two stages, each guided by explicitly modeled topological constraints. Specifically, our approach first establishes face-edge incidence relations to define a coherent topological scaffold, upon which face proxies and initial edge curves are generated. Subsequently, multiple Transformer-based diffusion modules are employed to refine the geometry by generating precise face surfaces and vertex positions, with edge-vertex adjacencies dynamically established and enforced to preserve structural consistency. This progressive geometry hierarchy enables the generation of more novel and diverse shapes, while two-stage topological modeling ensures high validity. Experimental results show that HiDiGen achieves strong performance, generating novel, diverse, and topologically sound CAD models."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v2",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 2 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "B-Rep reconstruction from 3D scan deep learning",\n      "boundary representation generation neural network",\n      "CAD B-Rep learning from point cloud"\n    ],\n    "effective_query": "point cloud to boundary representation reconstruction neural network",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to boundary representation reconstruction neural network",\n      "B-Rep generation diffusion model transformer",\n      "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_vrVuUkcvZS2s94FpDgROFWfx' is_error=False
```

### Tool Event 16

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_12iSyGDviNi9ulgVOtWPVxXk', arguments='{"query": "point cloud to B-Rep reconstruction neural network 2023", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 17

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "neural B-Rep generation from point cloud diffusion",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "DPR-GAN: Dual-Stream Progressive Refinement for Adversarial 3D Point Cloud Generation",\n      "source": "Crossref / Neural Processing Letters",\n      "year": 2024,\n      "date": "2024-2-24",\n      "url": "https://doi.org/10.1007/s11063-024-11454-x",\n      "doi": "10.1007/s11063-024-11454-x",\n      "authors": [\n        "Xiangyang Wang",\n        "Jiale Chen",\n        "Rui Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title><jats:p>Point cloud generation aims to transfer a latent code to realistic 3D shapes through generative models. However, most of progressive generative methods ignore the spatial relationship among different stages and suffer from the loss of contextual information. To address this issue, we propose dual-stream progressive refinement adversarial network (DPR-GAN), which utilizes a dual-stream structure to establish the relationship between two adjacent stages. Such a mechanism can learn the spatial context and preserve more spatial details of point clouds at different stages. In addition, DPR-GAN adopts 3D gridding transformation to guide the shape deformation. In this way, 3D gridding transformation can learn a reasonable correspondence between the local regions of 3D shapes and latent codes. Benefiting from the uniformity and adaptability of the 3D grids, our proposed DPR-GAN can improve the quality and consistency of generated point clouds. We conduct comprehensive experiments to demonstrate that the proposed DPR-GAN is capable of generating pluralistic point clouds, as compared with state-of-the-art generation methods in terms of both visual and quantitative evaluations.</jats:p>"\n      ]\n    },\n    {\n      "title": "GRASP-Net: Geometric Residual Analysis and Synthesis for Point Cloud Compression",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-09-09T17:09:02Z",\n      "url": "http://arxiv.org/abs/2209.04401v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Pang",\n        "Muhammad Asad Lodhi",\n        "Dong Tian"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Point cloud compression (PCC) is a key enabler for various 3-D applications, owing to the universality of the point cloud format. Ideally, 3D point clouds endeavor to depict object/scene surfaces that are continuous. Practically, as a set of discrete samples, point clouds are locally disconnected and sparsely distributed. This sparse nature is hindering the discovery of local correlation among points for compression. Motivated by an analysis with fractal dimension, we propose a heterogeneous approach with deep learning for lossy point cloud geometry compression. On top of a base layer compressing a coarse representation of the input, an enhancement layer is designed to cope with the challenging geometric residual/details. Specifically, a point-based network is applied to convert the erratic local details to latent features residing on the coarse point cloud. Then a sparse convolutional neural network operating on the coarse point cloud is launched. It utilizes the continuity/smoothness of the coarse geometry to compress the latent features as an enhancement bit-stream that greatly benefits the reconstruction quality. When this bit-stream is unavailable, e.g., due to packet loss, we support a skip mode with the same architecture which generates geometric details from the coarse point cloud directly. Experimentation on both dense and sparse point clouds demonstrate the state-of-the-art compression performance achieved by our proposal. Our code is available at https://github.com/InterDigitalInc/GRASP-Net."\n      ]\n    },\n    {\n      "title": "3D Point Cloud Compression with Recurrent Neural Network and Image Compression Methods",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-18T19:08:19Z",\n      "url": "http://arxiv.org/abs/2402.11680v1",\n      "doi": "",\n      "authors": [\n        "Till Beemelmanns",\n        "Yuchen Tao",\n        "Bastian Lampe",\n        "Lennart Reiher",\n        "Raphael van Kempen",\n        "Timo Woopen",\n        "Lutz Eckstein"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Storing and transmitting LiDAR point cloud data is essential for many AV applications, such as training data collection, remote control, cloud services or SLAM. However, due to the sparsity and unordered structure of the data, it is difficult to compress point cloud data to a low volume. Transforming the raw point cloud data into a dense 2D matrix structure is a promising way for applying compression algorithms. We propose a new lossless and calibrated 3D-to-2D transformation which allows compression algorithms to efficiently exploit spatial correlations within the 2D representation. To compress the structured representation, we use common image compression methods and also a self-supervised deep compression approach using a recurrent neural network. We also rearrange the LiDAR\'s intensity measurements to a dense 2D representation and propose a new metric to evaluate the compression performance of the intensity. Compared to approaches that are based on generic octree point cloud compression or based on raw point cloud data compression, our approach achieves the best quantitative and visual performance. Source code and dataset are available at https://github.com/ika-rwth-aachen/Point-Cloud-Compression."\n      ]\n    },\n    {\n      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-06-23T02:21:48Z",\n      "url": "http://arxiv.org/abs/2406.15982v1",\n      "doi": "",\n      "authors": [\n        "Yangdi Lu",\n        "Wenbo He"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."\n      ]\n    },\n    {\n      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-24",\n      "url": "https://doi.org/10.1016/j.autcon.2022.104440",\n      "doi": "10.1016/j.autcon.2022.104440",\n      "authors": [\n        "Shanaka Kristombu Baduge",\n        "Sadeep Thilakarathna",\n        "Jude Shalitha Perera",\n        "Mehrdad Arashpour",\n        "P. Sharafi",\n        "Bertrand Teodosio",\n        "Ankit Shringi",\n        "Priyan Mendis"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and safety; smart operation, building management and health monitoring; and durability, life cycle analysis, and circular economy. This paper presents a unique perspective on applications of AI/DL/ML in these domains for the complete building lifecycle, from conceptual stage, design stage, construction stage, operational and maintenance stage until the end of life. Furthermore, data collection strategies using smart vision and sensors, data cleaning methods (post-processing), data storage for developing these models are discussed, and the challenges in model development and strategies to overcome these challenges are elaborated. Future trends in these domains and possible research avenues are also presented."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "3D scan to boundary representation deep learning",\n      "neural network B-Rep reconstruction from point cloud",\n      "CAD model reconstruction from point cloud B-Rep"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2023",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2023",\n      "B-Rep reconstruction from 3D scan deep learning CVPR",\n      "neural B-Rep generation from point cloud diffusion"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_12iSyGDviNi9ulgVOtWPVxXk' is_error=False
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
Today's date for this run is 2026-04-13.
- The query contains a vague recency hint. PlannerAgent must resolve it into an explicit year range against today's date and all later agents must preserve that range.
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction",
    "deep learning boundary representation generation",
    "point cloud to CAD boundary representation"
  ],
  "queries": [
    {
      "query": "neural direct B-Rep generation from point clouds",
      "reason": "Targets the core task of generating boundary representation data structures directly from unstructured 3D data using neural methods."
    },
    {
      "query": "end-to-end learning of B-Rep topology and geometry",
      "reason": "Focuses on modern architectures that learn to output the complete topological graph and geometric surfaces without intermediate operation sequences."
    },
    {
      "query": "latent diffusion models for B-Rep shape generation",
      "reason": "Captures recent advanced generative approaches (post-2022) that might be applied to structured CAD outputs like B-Reps."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic."
  ],
  "success_criteria": [
    "Retrieve 8-10 papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps."
  ]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find papers on 3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks. Let me start with the primary query.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_4IWkq9xNE2lVHMlXkz1C4cl3', arguments='{"query": "neural direct B-Rep generation from point clouds", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "neural direct B-Rep generation from point clouds",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end learning of B-Rep topology and geometry",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "latent diffusion models for B-Rep shape generation",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6172545",\n      "doi": "10.2139/ssrn.6172545",\n      "authors": [\n        "yihang fu",\n        "jing li",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>"\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-07-27",\n      "url": "https://doi.org/10.1145/3730842",\n      "doi": "10.1145/3730842",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen‐Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. ≈50%."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6301470",\n      "doi": "10.2139/ssrn.6301470",\n      "authors": [\n        "Fulin Tang",\n        "An Liu",\n        "Rudong Xue",\n        "Bingxi Liu",\n        "ZeJin Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents an unsupervised method for directly learning neural implicit functions from 3D point clouds, aiming to tackle the core challenge of lacking ground-truth implicit values for supervisory training. Current approaches typically rely on global geometric constraints to learn implicit functions; however, this strategy often causes the optimization process to fall into local minima, resulting in over-smoothing artifacts, loss of fine geometric details, and blurring of sharp features.Although hand-crafted filters can be applied to point clouds to capture high-frequency details—thereby mitigating over-smoothing of geometric structures and avoiding the generation of coarse surfaces—their performance is highly dependent on manual parameter tuning, which severely restricts their generalization ability across diverse 3D shapes.To address these limitations, we propose a dynamic graph filter that integrates the adaptability of graph neural networks with the geometric characteristics of hand-crafted bilateral filters, enabling the learning of high-quality neural implicit functions from 3D point clouds. Our approach dynamically evolves graph features during the training process, automatically capturing high-frequency geometric details without the need for manual parameter adjustment.Ultimately, high-quality surface reconstruction can be achieved from the learned neural implicit function, even in the complete absence of ground-truth supervision. Experimental results on multiple datasets demonstrate that our proposed method effectively preserves complex geometric details and sharp features, achieving superior surface reconstruction quality compared to state-of-the-art approaches.</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 10 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction",\n      "deep learning boundary representation generation",\n      "point cloud to CAD boundary representation"\n    ],\n    "effective_query": "neural direct B-Rep generation from point clouds",\n    "used_override_query": true,\n    "executed_queries": [\n      "neural direct B-Rep generation from point clouds",\n      "end-to-end learning of B-Rep topology and geometry",\n      "latent diffusion models for B-Rep shape generation"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_4IWkq9xNE2lVHMlXkz1C4cl3' is_error=False
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
      "query": "neural direct B-Rep generation from point clouds",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "end-to-end learning of B-Rep topology and geometry",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "latent diffusion models for B-Rep shape generation",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
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
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-07-27",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of boundary representations (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a holistic latent (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. ≈50%."
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
      "title": "Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6301470",
      "doi": "10.2139/ssrn.6301470",
      "authors": [
        "Fulin Tang",
        "An Liu",
        "Rudong Xue",
        "Bingxi Liu",
        "ZeJin Gao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents an unsupervised method for directly learning neural implicit functions from 3D point clouds, aiming to tackle the core challenge of lacking ground-truth implicit values for supervisory training. Current approaches typically rely on global geometric constraints to learn implicit functions; however, this strategy often causes the optimization process to fall into local minima, resulting in over-smoothing artifacts, loss of fine geometric details, and blurring of sharp features.Although hand-crafted filters can be applied to point clouds to capture high-frequency details—thereby mitigating over-smoothing of geometric structures and avoiding the generation of coarse surfaces—their performance is highly dependent on manual parameter tuning, which severely restricts their generalization ability across diverse 3D shapes.To address these limitations, we propose a dynamic graph filter that integrates the adaptability of graph neural networks with the geometric characteristics of hand-crafted bilateral filters, enabling the learning of high-quality neural implicit functions from 3D point clouds. Our approach dynamically evolves graph features during the training process, automatically capturing high-frequency geometric details without the need for manual parameter adjustment.Ultimately, high-quality surface reconstruction can be achieved from the learned neural implicit function, even in the complete absence of ground-truth supervision. Experimental results on multiple datasets demonstrate that our proposed method effectively preserves complex geometric details and sharp features, achieving superior surface reconstruction quality compared to state-of-the-art approaches.</jats:p>"
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
      "neural network B-Rep reconstruction",
      "deep learning boundary representation generation",
      "point cloud to CAD boundary representation"
    ],
    "effective_query": "neural direct B-Rep generation from point clouds",
    "used_override_query": true,
    "executed_queries": [
      "neural direct B-Rep generation from point clouds",
      "end-to-end learning of B-Rep topology and geometry",
      "latent diffusion models for B-Rep shape generation"
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
  "review_summary": "The retrieval captured several highly relevant papers (Point2Brep, BrepGen, ComplexGen, HoLa, AutoBrep, BrepGPT) that directly output B-Reps from point clouds or via generative models, satisfying the core topic and exclusions. However, the set fails the hard requirement for source coverage (only 2 distinct sources used: Crossref, OpenAlex, arXiv; but arXiv is a preprint repository, not a distinct scholarly source like a publisher or index). Additionally, the evidence snippets are strong but the candidate depth is borderline (5 unique in-range papers after merging duplicates, but one is a duplicate entry and another is about neural implicit functions, which is not direct B-Rep generation). The time range is respected, and metadata is mostly complete. A revise is needed to broaden source coverage and ensure a robust set of 8-10 distinct, in-range core papers.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct scholarly sources were effectively used (Crossref, OpenAlex). arXiv is a preprint repository, not a distinct publisher/index. The user did not explicitly restrict the search space, so at least 2 distinct sources are required. This set relies heavily on arXiv and Crossref/OpenAlex overlaps."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, there are 7 unique papers. However, 'Unsupervised Learning of Neural Implicit Functions from Point Clouds via Graph Filtering' is about surface reconstruction via implicit functions, not direct B-Rep generation (output is not a B-Rep data structure). Removing that leaves 6. Among these, 'HoLa' appears twice from different sources but is the same paper. Thus, only 5 distinct in-range candidate papers remain that are potentially core to the topic, which is below the minimum of 5 non-duplicate candidates required for a robust set aiming for 8-10."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 3 (Point2Brep, BrepGen, ComplexGen) are clearly aligned with the user's topic of direct B-Rep generation from point clouds or generative modeling, not just keyword overlap."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set reflects the user's constraints: papers are from 2021-2026, focus on direct B-Rep output, use neural architectures, and avoid CAD operation sequences, CSG, and program synthesis."
    },
    "core_method_fit": {
      "passed": true,
      "reason": "At least 3 papers (Point2Brep, BrepGen, ComplexGen) are plausible core candidates for direct B-Rep generation from point clouds or generative modeling, based on title and abstract evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": true,
      "reason": "No obvious missing core subtopic or major evidence hole is apparent from the current set, though the limited number of distinct papers suggests the coverage may be incomplete."
    }
  },
  "key_risks": [
    "Source diversity is insufficient; over-reliance on arXiv and Crossref/OpenAlex may miss venue-published papers from SIGGRAPH, CVPR, etc.",
    "Candidate depth is borderline; the set includes only ~5 distinct core papers, short of the target 8-10.",
    "One paper (Unsupervised Learning of Neural Implicit Functions...) is likely irrelevant as it outputs implicit surfaces, not B-Reps."
  ],
  "next_actions": [
    "Execute a new search using additional distinct sources (e.g., Semantic Scholar, DBLP, or direct conference proceedings) to improve source coverage.",
    "Refine queries to explicitly target point-cloud-to-B-Rep reconstruction, e.g., 'point cloud to boundary representation reconstruction neural network' or 'B-Rep reconstruction from 3D scan deep learning'.",
    "Filter out papers that are not directly about B-Rep generation (e.g., neural implicit surface reconstruction) and ensure each candidate outputs a B-Rep data structure as per the user's strict inclusion criteria."
  ]
}
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps",
    "neural implicit surface reconstruction (unless it explicitly outputs a B-Rep)"
  ],
  "fallback_queries": [
    "B-Rep reconstruction from 3D scan deep learning",
    "boundary representation generation neural network",
    "CAD B-Rep learning from point cloud"
  ],
  "queries": [
    {
      "query": "point cloud to boundary representation reconstruction neural network",
      "reason": "Directly targets the core task of converting unstructured 3D data into a structured B-Rep using neural methods, addressing the primary input requirement."
    },
    {
      "query": "B-Rep generation diffusion model transformer",
      "reason": "Captures recent advanced generative architectures (post-2022) that are state-of-the-art for structured output generation, as seen in initial results."
    },
    {
      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",
      "reason": "Focuses on high-impact conference venues to improve source diversity and find published papers beyond preprint repositories."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic.",
    "We must diversify sources beyond arXiv and Crossref/OpenAlex overlaps to include Semantic Scholar, DBLP, or direct publisher indexes to meet source coverage requirements."
  ],
  "success_criteria": [
    "Retrieve 8-10 distinct papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history or implicit surface.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps.",
    "Improve source diversity by using at least 3 distinct scholarly sources (e.g., Semantic Scholar, DBLP, publisher sites) in addition to initial sources."
  ]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a revised search with improved queries to find more papers and diversify the sources. Let me start with the first refined query.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_vrVuUkcvZS2s94FpDgROFWfx', arguments='{"query": "point cloud to boundary representation reconstruction neural network", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to boundary representation reconstruction neural network",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep generation diffusion model transformer",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-07-19",\n      "url": "https://doi.org/10.1145/3658129",\n      "doi": "10.1145/3658129",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen , a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-06-10",\n      "url": "https://doi.org/10.1109/cvpr52734.2025.01997",\n      "doi": "10.1109/cvpr52734.2025.01997",\n      "authors": [\n        "Jing Li",\n        "Yangyang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-05-29",\n      "url": "http://arxiv.org/abs/2205.14573",\n      "doi": "10.48550/arxiv.2205.14573",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-04-03T08:06:51Z",\n      "url": "http://arxiv.org/abs/2604.02847v1",\n      "doi": "",\n      "authors": [\n        "Shurui Liu",\n        "Weide Chen",\n        "Ancong Wu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the standard 3D modeling format in CAD systems, encoding both geometric primitives and topological connectivity. Despite its prevalence, deep generative modeling of valid B-rep structures remains challenging due to the intricate interplay between discrete topology and continuous geometry. In this paper, we propose HiDiGen, a hierarchical generation framework that decouples geometry modeling into two stages, each guided by explicitly modeled topological constraints. Specifically, our approach first establishes face-edge incidence relations to define a coherent topological scaffold, upon which face proxies and initial edge curves are generated. Subsequently, multiple Transformer-based diffusion modules are employed to refine the geometry by generating precise face surfaces and vertex positions, with edge-vertex adjacencies dynamically established and enforced to preserve structural consistency. This progressive geometry hierarchy enables the generation of more novel and diverse shapes, while two-stage topological modeling ensures high validity. Experimental results show that HiDiGen achieves strong performance, generating novel, diverse, and topologically sound CAD models."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v2",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-01-28",\n      "url": "http://arxiv.org/abs/2401.15563",\n      "doi": "10.48550/arxiv.2401.15563",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 2 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "B-Rep reconstruction from 3D scan deep learning",\n      "boundary representation generation neural network",\n      "CAD B-Rep learning from point cloud"\n    ],\n    "effective_query": "point cloud to boundary representation reconstruction neural network",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to boundary representation reconstruction neural network",\n      "B-Rep generation diffusion model transformer",\n      "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_vrVuUkcvZS2s94FpDgROFWfx' is_error=False
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
      "query": "point cloud to boundary representation reconstruction neural network",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep generation diffusion model transformer",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH",
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
      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-06-10",
      "url": "https://doi.org/10.1109/cvpr52734.2025.01997",
      "doi": "10.1109/cvpr52734.2025.01997",
      "authors": [
        "Jing Li",
        "Yangyang Fu",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
      ]
    },
    {
      "title": "HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-04-03T08:06:51Z",
      "url": "http://arxiv.org/abs/2604.02847v1",
      "doi": "",
      "authors": [
        "Shurui Liu",
        "Weide Chen",
        "Ancong Wu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Boundary representation (B-rep) is the standard 3D modeling format in CAD systems, encoding both geometric primitives and topological connectivity. Despite its prevalence, deep generative modeling of valid B-rep structures remains challenging due to the intricate interplay between discrete topology and continuous geometry. In this paper, we propose HiDiGen, a hierarchical generation framework that decouples geometry modeling into two stages, each guided by explicitly modeled topological constraints. Specifically, our approach first establishes face-edge incidence relations to define a coherent topological scaffold, upon which face proxies and initial edge curves are generated. Subsequently, multiple Transformer-based diffusion modules are employed to refine the geometry by generating precise face surfaces and vertex positions, with edge-vertex adjacencies dynamically established and enforced to preserve structural consistency. This progressive geometry hierarchy enables the generation of more novel and diverse shapes, while two-stage topological modeling ensures high validity. Experimental results show that HiDiGen achieves strong performance, generating novel, diverse, and topologically sound CAD models."
      ]
    },
    {
      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-01-23T14:15:02Z",
      "url": "http://arxiv.org/abs/2601.16771v2",
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 2 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "B-Rep reconstruction from 3D scan deep learning",
      "boundary representation generation neural network",
      "CAD B-Rep learning from point cloud"
    ],
    "effective_query": "point cloud to boundary representation reconstruction neural network",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to boundary representation reconstruction neural network",
      "B-Rep generation diffusion model transformer",
      "end-to-end B-Rep learning from point clouds CVPR SIGGRAPH"
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
  "review_summary": "The retrieval has improved, capturing a strong set of highly relevant papers on direct B-Rep generation using modern neural architectures (diffusion, autoregressive, graph-based). The papers are within the 2021-2026 range and strictly avoid excluded categories. However, the hard requirement for source coverage is still not met: only 2 distinct scholarly sources were effectively used (arXiv and OpenAlex; Crossref appears in the list but not as a distinct source for unique papers). The user did not restrict the search space, so at least 2 distinct sources are required. Additionally, while candidate depth is better (8 unique papers after merging duplicates), the evidence snippets are strong but the set is heavily skewed towards generative models (BrepGen, DTGBrepGen, AutoBrep, HiDiGen, BrepARG, GraphBrep) with only one clear reconstruction-from-point-clouds paper (ComplexGen). The user's primary focus is on reconstruction from point clouds, so this imbalance is a gap. A revise is needed to diversify sources and ensure more papers on point-cloud-to-B-Rep reconstruction are included.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 2,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": false,
      "reason": "Only 2 distinct scholarly sources were effectively used: arXiv (preprint repository) and OpenAlex (index). Crossref appears in the sources_used list but no unique papers are attributed solely to Crossref; all papers are from arXiv or OpenAlex. The user did not explicitly restrict the search space, so at least 2 distinct sources are required. This set still relies heavily on arXiv and OpenAlex overlaps."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "After deduplication, there are 8 unique candidate papers (BrepGen, DTGBrepGen, AutoBrep, ComplexGen, HiDiGen, BrepARG, GraphBrep, and one duplicate merged). This meets the minimum of 5 non-duplicate candidates."
    },
    "relevance": {
      "passed": true,
      "reason": "Among the top candidates, at least 3 (BrepGen, ComplexGen, DTGBrepGen) are clearly aligned with the user's topic of direct B-Rep generation, using neural architectures and outputting B-Rep data structures."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": true,
      "reason": "The retrieved set reflects the user's constraints: papers are from 2021-2026, focus on direct B-Rep output, use neural architectures, and avoid CAD operation sequences, CSG, and program synthesis. However, the primary input focus (point clouds) is underrepresented."
    },
    "core_method_fit": {
      "passed": true,
      "reason": "At least 3 papers (BrepGen, ComplexGen, DTGBrepGen) are plausible core candidates for direct B-Rep generation, based on title and abstract evidence."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: reconstruction from point clouds. The user's primary focus is 'B-Rep reconstruction and generation from point clouds', but the set is heavily skewed towards unconditional generative models (BrepGen, DTGBrepGen, AutoBrep, HiDiGen, BrepARG, GraphBrep) with only one clear reconstruction-from-point-clouds paper (ComplexGen). This imbalance is a significant gap."
    }
  },
  "key_risks": [
    "Source diversity is insufficient; over-reliance on arXiv and OpenAlex may miss venue-published papers from other indexes.",
    "The set is imbalanced: heavily focused on generative models (diffusion/autoregressive) with limited representation of reconstruction from point clouds, which is the user's primary input requirement.",
    "Some papers may not explicitly handle point cloud input; evidence snippets do not always specify input modality."
  ],
  "next_actions": [
    "Execute a new search using additional distinct sources (e.g., Semantic Scholar, DBLP, or direct conference proceedings like CVPR, SIGGRAPH) to improve source coverage.",
    "Refine queries to explicitly target point-cloud-to-B-Rep reconstruction, e.g., 'point cloud to B-Rep reconstruction neural network 2023' or '3D scan to boundary representation deep learning'.",
    "Prioritize papers that explicitly mention point clouds or 3D scans as input in their abstracts to ensure alignment with the user's primary focus."
  ]
}
```

### Message 14

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art research papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-04-13",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for 3D shape generation",
    "geometric deep learning for boundary representations",
    "point cloud to B-Rep reconstruction"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "procedural modeling steps",
    "neural implicit surface reconstruction (unless it explicitly outputs a B-Rep)"
  ],
  "fallback_queries": [
    "3D scan to boundary representation deep learning",
    "neural network B-Rep reconstruction from point cloud",
    "CAD model reconstruction from point cloud B-Rep"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2023",
      "reason": "Directly targets the core reconstruction task from point clouds with a recent year filter to capture state-of-the-art methods within the range."
    },
    {
      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",
      "reason": "Focuses on high-impact conference venues (CVPR) to improve source diversity and find published papers on reconstruction, not just generation."
    },
    {
      "query": "neural B-Rep generation from point cloud diffusion",
      "reason": "Captures hybrid approaches that might generate B-Reps conditionally from point clouds using modern architectures like diffusion models."
    }
  ],
  "assumptions": [
    "The user's explicit year range (2021-2026) is authoritative; we will not broaden it.",
    "The term 'frontier research' implies a preference for very recent papers (2024-2026) within the range.",
    "Multimodal or sketch/image input papers will only be considered if they represent a major, cited breakthrough in direct B-Rep generation, as per the user's instruction.",
    "Conferences like CVPR, SIGGRAPH, NeurIPS, ICCV, ECCV, and ICLR are the primary venues for this topic.",
    "We must diversify sources beyond arXiv and OpenAlex overlaps to include Semantic Scholar, DBLP, or direct publisher indexes to meet source coverage requirements.",
    "The primary input focus is point clouds or 3D scans; we will prioritize papers that explicitly mention these inputs in abstracts or titles."
  ],
  "success_criteria": [
    "Retrieve 8-10 distinct papers that strictly meet the inclusion/exclusion criteria.",
    "All papers must output the final B-Rep data structure, not a construction history or implicit surface.",
    "Primary input for most papers should be point clouds or 3D scans.",
    "Papers should demonstrate a novel neural architecture or representation for B-Reps.",
    "Improve source diversity by using at least 3 distinct scholarly sources (e.g., Semantic Scholar, DBLP, publisher sites) in addition to initial sources.",
    "Balance the set to include both reconstruction-from-point-clouds and generative models, with emphasis on reconstruction."
  ]
}
```

### Message 15

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a final search focusing on point cloud to B-Rep reconstruction to address the gaps and improve source diversity.
```

### Message 16

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_12iSyGDviNi9ulgVOtWPVxXk', arguments='{"query": "point cloud to B-Rep reconstruction neural network 2023", "top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 17

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "neural B-Rep generation from point cloud diffusion",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-05-29T05:30:33Z",\n      "url": "http://arxiv.org/abs/2205.14573v1",\n      "doi": "",\n      "authors": [\n        "Haoxiang Guo",\n        "Shilin Liu",\n        "Hao Pan",\n        "Yang Liu",\n        "Xin Tong",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."\n      ]\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "DPR-GAN: Dual-Stream Progressive Refinement for Adversarial 3D Point Cloud Generation",\n      "source": "Crossref / Neural Processing Letters",\n      "year": 2024,\n      "date": "2024-2-24",\n      "url": "https://doi.org/10.1007/s11063-024-11454-x",\n      "doi": "10.1007/s11063-024-11454-x",\n      "authors": [\n        "Xiangyang Wang",\n        "Jiale Chen",\n        "Rui Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title><jats:p>Point cloud generation aims to transfer a latent code to realistic 3D shapes through generative models. However, most of progressive generative methods ignore the spatial relationship among different stages and suffer from the loss of contextual information. To address this issue, we propose dual-stream progressive refinement adversarial network (DPR-GAN), which utilizes a dual-stream structure to establish the relationship between two adjacent stages. Such a mechanism can learn the spatial context and preserve more spatial details of point clouds at different stages. In addition, DPR-GAN adopts 3D gridding transformation to guide the shape deformation. In this way, 3D gridding transformation can learn a reasonable correspondence between the local regions of 3D shapes and latent codes. Benefiting from the uniformity and adaptability of the 3D grids, our proposed DPR-GAN can improve the quality and consistency of generated point clouds. We conduct comprehensive experiments to demonstrate that the proposed DPR-GAN is capable of generating pluralistic point clouds, as compared with state-of-the-art generation methods in terms of both visual and quantitative evaluations.</jats:p>"\n      ]\n    },\n    {\n      "title": "GRASP-Net: Geometric Residual Analysis and Synthesis for Point Cloud Compression",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-09-09T17:09:02Z",\n      "url": "http://arxiv.org/abs/2209.04401v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Pang",\n        "Muhammad Asad Lodhi",\n        "Dong Tian"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Point cloud compression (PCC) is a key enabler for various 3-D applications, owing to the universality of the point cloud format. Ideally, 3D point clouds endeavor to depict object/scene surfaces that are continuous. Practically, as a set of discrete samples, point clouds are locally disconnected and sparsely distributed. This sparse nature is hindering the discovery of local correlation among points for compression. Motivated by an analysis with fractal dimension, we propose a heterogeneous approach with deep learning for lossy point cloud geometry compression. On top of a base layer compressing a coarse representation of the input, an enhancement layer is designed to cope with the challenging geometric residual/details. Specifically, a point-based network is applied to convert the erratic local details to latent features residing on the coarse point cloud. Then a sparse convolutional neural network operating on the coarse point cloud is launched. It utilizes the continuity/smoothness of the coarse geometry to compress the latent features as an enhancement bit-stream that greatly benefits the reconstruction quality. When this bit-stream is unavailable, e.g., due to packet loss, we support a skip mode with the same architecture which generates geometric details from the coarse point cloud directly. Experimentation on both dense and sparse point clouds demonstrate the state-of-the-art compression performance achieved by our proposal. Our code is available at https://github.com/InterDigitalInc/GRASP-Net."\n      ]\n    },\n    {\n      "title": "3D Point Cloud Compression with Recurrent Neural Network and Image Compression Methods",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-02-18T19:08:19Z",\n      "url": "http://arxiv.org/abs/2402.11680v1",\n      "doi": "",\n      "authors": [\n        "Till Beemelmanns",\n        "Yuchen Tao",\n        "Bastian Lampe",\n        "Lennart Reiher",\n        "Raphael van Kempen",\n        "Timo Woopen",\n        "Lutz Eckstein"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Storing and transmitting LiDAR point cloud data is essential for many AV applications, such as training data collection, remote control, cloud services or SLAM. However, due to the sparsity and unordered structure of the data, it is difficult to compress point cloud data to a low volume. Transforming the raw point cloud data into a dense 2D matrix structure is a promising way for applying compression algorithms. We propose a new lossless and calibrated 3D-to-2D transformation which allows compression algorithms to efficiently exploit spatial correlations within the 2D representation. To compress the structured representation, we use common image compression methods and also a self-supervised deep compression approach using a recurrent neural network. We also rearrange the LiDAR\'s intensity measurements to a dense 2D representation and propose a new metric to evaluate the compression performance of the intensity. Compared to approaches that are based on generic octree point cloud compression or based on raw point cloud data compression, our approach achieves the best quantitative and visual performance. Source code and dataset are available at https://github.com/ika-rwth-aachen/Point-Cloud-Compression."\n      ]\n    },\n    {\n      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-06-23T02:21:48Z",\n      "url": "http://arxiv.org/abs/2406.15982v1",\n      "doi": "",\n      "authors": [\n        "Yangdi Lu",\n        "Wenbo He"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."\n      ]\n    },\n    {\n      "title": "Artificial intelligence and smart vision for building and construction 4.0: Machine and deep learning methods and applications",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-24",\n      "url": "https://doi.org/10.1016/j.autcon.2022.104440",\n      "doi": "10.1016/j.autcon.2022.104440",\n      "authors": [\n        "Shanaka Kristombu Baduge",\n        "Sadeep Thilakarathna",\n        "Jude Shalitha Perera",\n        "Mehrdad Arashpour",\n        "P. Sharafi",\n        "Bertrand Teodosio",\n        "Ankit Shringi",\n        "Priyan Mendis"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and safety; smart operation, building management and health monitoring; and durability, life cycle analysis, and circular economy. This paper presents a unique perspective on applications of AI/DL/ML in these domains for the complete building lifecycle, from conceptual stage, design stage, construction stage, operational and maintenance stage until the end of life. Furthermore, data collection strategies using smart vision and sensors, data cleaning methods (post-processing), data storage for developing these models are discussed, and the challenges in model development and strategies to overcome these challenges are elaborated. Future trends in these domains and possible research avenues are also presented."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "3D scan to boundary representation deep learning",\n      "neural network B-Rep reconstruction from point cloud",\n      "CAD model reconstruction from point cloud B-Rep"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2023",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2023",\n      "B-Rep reconstruction from 3D scan deep learning CVPR",\n      "neural B-Rep generation from point cloud diffusion"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_12iSyGDviNi9ulgVOtWPVxXk' is_error=False
```

### Message 18

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
      "query": "point cloud to B-Rep reconstruction neural network 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from 3D scan deep learning CVPR",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "neural B-Rep generation from point cloud diffusion",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results."
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p id=\"p1\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."
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
      "title": "DPR-GAN: Dual-Stream Progressive Refinement for Adversarial 3D Point Cloud Generation",
      "source": "Crossref / Neural Processing Letters",
      "year": 2024,
      "date": "2024-2-24",
      "url": "https://doi.org/10.1007/s11063-024-11454-x",
      "doi": "10.1007/s11063-024-11454-x",
      "authors": [
        "Xiangyang Wang",
        "Jiale Chen",
        "Rui Wang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title><jats:p>Point cloud generation aims to transfer a latent code to realistic 3D shapes through generative models. However, most of progressive generative methods ignore the spatial relationship among different stages and suffer from the loss of contextual information. To address this issue, we propose dual-stream progressive refinement adversarial network (DPR-GAN), which utilizes a dual-stream structure to establish the relationship between two adjacent stages. Such a mechanism can learn the spatial context and preserve more spatial details of point clouds at different stages. In addition, DPR-GAN adopts 3D gridding transformation to guide the shape deformation. In this way, 3D gridding transformation can learn a reasonable correspondence between the local regions of 3D shapes and latent codes. Benefiting from the uniformity and adaptability of the 3D grids, our proposed DPR-GAN can improve the quality and consistency of generated point clouds. We conduct comprehensive experiments to demonstrate that the proposed DPR-GAN is capable of generating pluralistic point clouds, as compared with state-of-the-art generation methods in terms of both visual and quantitative evaluations.</jats:p>"
      ]
    },
    {
      "title": "GRASP-Net: Geometric Residual Analysis and Synthesis for Point Cloud Compression",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-09-09T17:09:02Z",
      "url": "http://arxiv.org/abs/2209.04401v1",
      "doi": "",
      "authors": [
        "Jiahao Pang",
        "Muhammad Asad Lodhi",
        "Dong Tian"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Point cloud compression (PCC) is a key enabler for various 3-D applications, owing to the universality of the point cloud format. Ideally, 3D point clouds endeavor to depict object/scene surfaces that are continuous. Practically, as a set of discrete samples, point clouds are locally disconnected and sparsely distributed. This sparse nature is hindering the discovery of local correlation among points for compression. Motivated by an analysis with fractal dimension, we propose a heterogeneous approach with deep learning for lossy point cloud geometry compression. On top of a base layer compressing a coarse representation of the input, an enhancement layer is designed to cope with the challenging geometric residual/details. Specifically, a point-based network is applied to convert the erratic local details to latent features residing on the coarse point cloud. Then a sparse convolutional neural network operating on the coarse point cloud is launched. It utilizes the continuity/smoothness of the coarse geometry to compress the latent features as an enhancement bit-stream that greatly benefits the reconstruction quality. When this bit-stream is unavailable, e.g., due to packet loss, we support a skip mode with the same architecture which generates geometric details from the coarse point cloud directly. Experimentation on both dense and sparse point clouds demonstrate the state-of-the-art compression performance achieved by our proposal. Our code is available at https://github.com/InterDigitalInc/GRASP-Net."
      ]
    },
    {
      "title": "3D Point Cloud Compression with Recurrent Neural Network and Image Compression Methods",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-02-18T19:08:19Z",
      "url": "http://arxiv.org/abs/2402.11680v1",
      "doi": "",
      "authors": [
        "Till Beemelmanns",
        "Yuchen Tao",
        "Bastian Lampe",
        "Lennart Reiher",
        "Raphael van Kempen",
        "Timo Woopen",
        "Lutz Eckstein"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Storing and transmitting LiDAR point cloud data is essential for many AV applications, such as training data collection, remote control, cloud services or SLAM. However, due to the sparsity and unordered structure of the data, it is difficult to compress point cloud data to a low volume. Transforming the raw point cloud data into a dense 2D matrix structure is a promising way for applying compression algorithms. We propose a new lossless and calibrated 3D-to-2D transformation which allows compression algorithms to efficiently exploit spatial correlations within the 2D representation. To compress the structured representation, we use common image compression methods and also a self-supervised deep compression approach using a recurrent neural network. We also rearrange the LiDAR's intensity measurements to a dense 2D representation and propose a new metric to evaluate the compression performance of the intensity. Compared to approaches that are based on generic octree point cloud compression or based on raw point cloud data compression, our approach achieves the best quantitative and visual performance. Source code and dataset are available at https://github.com/ika-rwth-aachen/Point-Cloud-Compression."
      ]
    },
    {
      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-06-23T02:21:48Z",
      "url": "http://arxiv.org/abs/2406.15982v1",
      "doi": "",
      "authors": [
        "Yangdi Lu",
        "Wenbo He"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This article presents a state-of-the-art review of the applications of Artificial Intelligence (AI), Machine Learning (ML), and Deep Learning (DL) in building and construction industry 4.0 in the facets of architectural design and visualization; material design and optimization; structural design and analysis; offsite manufacturing and automation; construction management, progress monitoring, and safety; smart operation, building management and health monitoring; and durability, life cycle analysis, and circular economy. This paper presents a unique perspective on applications of AI/DL/ML in these domains for the complete building lifecycle, from conceptual stage, design stage, construction stage, operational and maintenance stage until the end of life. Furthermore, data collection strategies using smart vision and sensors, data cleaning methods (post-processing), data storage for developing these models are discussed, and the challenges in model development and strategies to overcome these challenges are elaborated. Future trends in these domains and possible research avenues are also presented."
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 21 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "3D scan to boundary representation deep learning",
      "neural network B-Rep reconstruction from point cloud",
      "CAD model reconstruction from point cloud B-Rep"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2023",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2023",
      "B-Rep reconstruction from 3D scan deep learning CVPR",
      "neural B-Rep generation from point cloud diffusion"
    ],
    "fallback_used": false
  }
}
```

### Message 19

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=7

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval has severely regressed. While source coverage now includes Crossref, OpenAlex, and arXiv (3 distinct sources), the relevance of the papers is extremely poor. Only 2 papers (BrepGen and ComplexGen) are directly about B-Rep generation/reconstruction; the remaining 8 are about point cloud completion, compression, single-image 3D reconstruction, or general surveys, which do not output B-Rep data structures and violate the user's strict exclusion criteria. The candidate depth is insufficient for core B-Rep papers, and the set fails the relevance and core-method-fit hard requirements. A revise is urgently needed to refocus on the core topic and exclude irrelevant papers.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 2
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "3 distinct sources were used: Crossref, OpenAlex, and arXiv. This meets the requirement of at least 2 distinct sources."
    },
    "candidate_depth": {
      "passed": false,
      "reason": "After deduplication, there are 10 candidate papers, but only 2 (BrepGen, ComplexGen) are about direct B-Rep generation/reconstruction. The others are irrelevant (point cloud completion, compression, etc.). Thus, the number of non-duplicate candidates relevant to the topic is below the minimum of 5."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 2 are clearly aligned with the user's topic of direct B-Rep generation from point clouds. The majority are about point cloud completion, compression, or general AI surveys, which do not output B-Rep data structures."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL when available. Authors are also provided."
    },
    "query_fit": {
      "passed": false,
      "reason": "The retrieved set does not reflect the user's constraints: most papers do not output B-Rep data structures, and many are about point cloud compression, completion, or single-image reconstruction, which are outside the scope."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Only 2 papers (BrepGen, ComplexGen) are plausible core candidates for direct B-Rep generation. The rest are not about B-Rep output."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range. No out-of-range papers dominate the set."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: the set is dominated by irrelevant papers, leaving a huge gap in relevant B-Rep reconstruction/generation papers."
    }
  },
  "key_risks": [
    "Extreme irrelevance: most papers are about point cloud completion, compression, or general AI surveys, not B-Rep generation/reconstruction.",
    "The set includes only 2 core B-Rep papers, far short of the target 8-10.",
    "The retrieval appears to have been misled by broad queries that captured point cloud methods unrelated to B-Rep."
  ],
  "next_actions": [
    "Execute a new search with strict keyword filtering to exclude irrelevant topics. Use queries like: '\"B-Rep\" reconstruction point cloud neural' or '\"boundary representation\" generation from point cloud deep learning'.",
    "Explicitly exclude papers with keywords like 'compression', 'completion', 'survey', 'LiDAR', 'NeRF', 'image-based' unless they also mention B-Rep output.",
    "Prioritize papers from known relevant venues (SIGGRAPH, CVPR, NeurIPS) that have previously published B-Rep work, and verify each candidate's output is a B-Rep data structure via abstract evidence."
  ]
}
```

### Message 20

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: {

```text
{
  "report_title": "Paper Search Report",
  "report_type": "failure",
  "query_understanding": "The user requested 8-10 state-of-the-art research papers (2021-2026) focused on 3D Boundary Representation (B-Rep) reconstruction and generation. The core requirement is that the model's primary output must be the B-Rep data structure itself (faces, edges, vertices, topology), generated directly from unstructured point clouds or 3D scans using modern neural architectures. The search must strictly exclude methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "search_strategy": ["Initial queries targeted neural direct B-Rep generation and end-to-end learning of B-Rep topology.", "Subsequent revisions aimed to improve source diversity and focus on point-cloud-to-B-Rep reconstruction.", "Final queries attempted to balance generative models with reconstruction papers, but the retrieval was misled by broad point cloud topics."],
  "candidate_section_intro": "The search did not clear the quality bar. After three review cycles, the team could not assemble a robust set of 8-10 distinct, credible papers that strictly meet the user's inclusion and exclusion criteria. The latest retrieval, while having adequate source coverage, was dominated by papers irrelevant to direct B-Rep generation (e.g., point cloud compression, completion, general surveys). Only a handful of verified candidates were identified.",
  "candidate_papers": [],
  "verified_candidates": [
    {
      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",
      "year": 2024,
      "source": "arXiv / OpenAlex",
      "link": "http://arxiv.org/abs/2401.15563v3",
      "summary": "A diffusion-based generative model that directly outputs a B-Rep CAD model using a hierarchical tree-structured latent representation. It employs Transformer-based diffusion to denoise node features and recovers topology by merging duplicated nodes, enabling the generation of shapes with free-form surfaces.",
      "why_included": "Directly outputs a B-Rep data structure using a modern neural architecture (diffusion model). It is a core, highly cited paper in neural B-Rep generation, strictly avoiding operation sequences."
    },
    {
      "title": "ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation",
      "year": 2022,
      "source": "arXiv / OpenAlex",
      "link": "http://arxiv.org/abs/2205.14573v1",
      "summary": "Reconstructs CAD models in B-Rep by detecting geometric primitives (vertices, edges, surfaces) and their correspondences, modeled as a chain complex. It uses a sparse CNN encoder for point cloud processing and a transformer decoder, followed by global optimization to recover a valid B-Rep.",
      "why_included": "Directly reconstructs B-Rep models from point clouds using a neural framework, outputting the topological and geometric structure without a construction history."
    }
  ],
  "unverified_leads": [
    {
      "title": "Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds",
      "year": 2026,
      "source": "Crossref",
      "link": "https://doi.org/10.2139/ssrn.6172545",
      "summary": "A framework that reconstructs complete and topologically consistent B-rep models from noisy point clouds by integrating learning-based surface patch segmentation with geometric reasoning to recover edges and vertices.",
      "why_included": "Title and abstract strongly suggest direct B-Rep reconstruction from point clouds, aligning perfectly with the primary input requirement. However, full verification of its neural architecture and exclusion of operation sequences is needed."
    },
    {
      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",
      "year": 2025,
      "source": "arXiv",
      "link": "http://arxiv.org/abs/2504.14257v3",
      "summary": "Introduces a holistic latent space that unifies B-Rep geometry and topology, learning to derive curve geometries from surface pairs via a neural intersection network, enabling diffusion-based generation from various inputs.",
      "why_included": "Proposes a novel neural representation for B-Reps and a diffusion-based generator, indicating direct B-Rep output. Its input includes point clouds, but full verification against exclusion criteria is pending."
    },
    {
      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",
      "year": 2025,
      "source": "arXiv",
      "link": "http://arxiv.org/abs/2512.03018v1",
      "summary": "An autoregressive Transformer model that tokenizes B-Rep geometry and topology into a unified sequence, generating watertight B-Reps via next-token prediction.",
      "why_included": "Represents a state-of-the-art neural approach for direct B-Rep generation. The abstract confirms output is a B-Rep, but its primary input modality requires verification to ensure alignment with point cloud focus."
    }
  ],
  "notes_and_gaps": ["The search consistently struggled to find a sufficient volume of papers specifically on point-cloud-to-B-Rep reconstruction. The field appears niche, with many neural CAD papers focusing on operation sequences or CSG, which were excluded.", "Recent trends are strongly towards generative models (diffusion, autoregressive) for B-Rep synthesis, but these often use category labels or latent codes as input, not strictly point clouds.", "Source diversity was achieved in the final attempt, but at the cost of relevance, indicating a trade-off between broad sourcing and precise topic filtering.", "The exclusion of 'neural implicit surface reconstruction' papers was necessary but may have removed some relevant work that bridges to B-Rep output."],
  "recommended_next_steps": ["Conduct a targeted search using precise Boolean queries in academic databases (e.g., \"B-Rep\" AND \"point cloud\" AND (reconstruction OR generation) NOT \"CSG\" NOT \"operation sequence\").", "Manually examine proceedings of key venues (SIGGRAPH, CVPR, NeurIPS) from 2021-2026 for sessions on 3D reconstruction and CAD learning.", "Verify the unverified leads by reading their full texts to confirm they output B-Rep data structures and use point clouds as a primary input.", "Consider expanding the input scope slightly to include multimodal inputs if the method represents a major breakthrough in direct B-Rep generation, as per the user's original allowance."],
  "termination": "TERMINATE"
}
```
