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
**Generated At:** 2026-03-25T10:58:05
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
  "user_intent": "Find 8-10 state-of-the-art papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for B-Rep generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "step-by-step modeling history output"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction",
    "deep learning boundary representation generation",
    "point cloud to B-Rep deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2021",
      "reason": "Targets the core task with a focus on neural methods and anchors the start of the time range."
    },
    {
      "query": "direct B-Rep generation from 3D scans deep learning",
      "reason": "Emphasizes direct output of the B-Rep structure, excluding intermediate representations like sequences."
    },
    {
      "query": "neural implicit representation for B-Rep faces and edges",
      "reason": "Focuses on modern architectural approaches for representing continuous B-Rep geometry and topology."
    }
  ],
  "assumptions": [
    "The user wants frontier research, so the search should prioritize top-tier venues (CVPR, SIGGRAPH, NeurIPS, etc.).",
    "The phrase 'between 2021-2026' is interpreted as inclusive of both years.",
    "Methods that output a B-Rep mesh (with topological adjacency) qualify, even if they use intermediate neural fields, as long as the final output is the B-Rep data structure.",
    "If fewer than 8-10 papers perfectly match the strict criteria within the time range, the retrieval should include the most relevant ones, and the report will note the scarcity."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must use point clouds or 3D scans as a primary or acceptable input.",
    "Papers must employ modern neural architectures (e.g., transformers, graph networks, implicit functions).",
    "No included paper should focus on reconstructing CAD modeling sequences or CSG trees."
  ]
}
```

### Planner Output 8

- Topic: `3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction and generation from point clouds using neural networks",
  "user_intent": "Find 8-10 state-of-the-art papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry from point clouds",
    "latent space representations for B-Reps",
    "end-to-end learning from unstructured 3D scans to B-Reps",
    "variational and autoregressive models for B-Rep generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "step-by-step modeling history output",
    "implicit neural representations for non-B-Rep tasks"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction from scans",
    "deep learning boundary representation generation point cloud",
    "3D scan to CAD B-Rep deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep neural network 2023",
      "reason": "Directly targets the core input modality (point cloud) and the output (B-Rep) within a recent year to capture state-of-the-art."
    },
    {
      "query": "B-Rep generation from 3D scans transformer",
      "reason": "Focuses on modern neural architectures (transformer) for the specific task, emphasizing scan input."
    },
    {
      "query": "SolidGen HoLa AutoBrep point cloud input",
      "reason": "Targets known promising papers from the previous retrieval to verify their input modality and ensure they meet the strict criteria."
    }
  ],
  "assumptions": [
    "The user's highest priority is point cloud or 3D scan input. Papers using only images, text, or latent codes as input are secondary and should only be included if they represent a major breakthrough in B-Rep generation.",
    "The previous retrieval captured relevant B-Rep generation papers, but their abstracts did not explicitly confirm point cloud input. This revised plan seeks to verify that or find alternatives.",
    "If fewer than 8-10 papers perfectly match the strict criteria, the final report will note the scarcity and focus on the most relevant ones.",
    "The time range remains inclusive of 2021-2026."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must explicitly mention point clouds or 3D scans as a primary or supported input modality.",
    "Papers must employ modern neural architectures (e.g., transformers, graph networks, diffusion models).",
    "No included paper should focus on reconstructing CAD modeling sequences, CSG trees, or program synthesis."
  ]
}
```

### Planner Output 14

- Topic: `3D Boundary Representation (B-Rep) reconstruction from point clouds using neural networks (3 queries, 2021-2026)`

```json
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction from point clouds using neural networks",
  "user_intent": "Find state-of-the-art papers (2021-2026) that directly reconstruct B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans using modern neural architectures, excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "neural reconstruction of B-Rep topology and geometry from point clouds",
    "direct mapping from 3D scans to B-Rep structures",
    "end-to-end learning for B-Rep reconstruction",
    "handling unstructured point cloud input"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "unconditional B-Rep generation",
    "B-Rep feature recognition",
    "general 3D asset generation"
  ],
  "fallback_queries": [
    "B-Rep reconstruction from point cloud deep learning",
    "neural network for B-Rep from 3D scan",
    "point cloud to CAD B-Rep reconstruction"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2024",
      "reason": "Directly targets the reconstruction task from point clouds in a recent year, emphasizing the input-output mapping."
    },
    {
      "query": "B-Rep reconstruction from 3D scans deep learning",
      "reason": "Focuses on scan input and reconstruction, not unconditional generation."
    },
    {
      "query": "BRepNet point cloud reconstruction",
      "reason": "Targets a known seminal paper (BRepNet) that may address B-Rep reconstruction, verifying its input modality and year."
    }
  ],
  "assumptions": [
    "The user's primary focus is reconstruction from point clouds, not unconditional generation or generation from other modalities.",
    "If a paper's primary contribution is unconditional B-Rep generation but it also supports point cloud conditioning, it may be included only if point cloud input is a significant demonstrated application.",
    "The previous retrievals have yielded many B-Rep generation papers; this plan explicitly seeks reconstruction papers to fill the gap.",
    "The time range remains inclusive of 2021-2026."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must explicitly focus on reconstructing B-Reps from point clouds or 3D scans as a core task.",
    "Papers must employ modern neural architectures.",
    "No included paper should focus on reconstructing CAD modeling sequences, CSG trees, or program synthesis."
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
      "query": "point cloud to B-Rep reconstruction neural network 2021",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-Rep generation from 3D scans deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "neural implicit representation for B-Rep faces and edges",
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
      "title": "SolidGen: An Autoregressive Model for Direct B-rep Synthesis",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-03-26T00:00:45Z",
      "url": "http://arxiv.org/abs/2203.13944v2",
      "doi": "",
      "authors": [
        "Pradeep Kumar Jayaraman",
        "Joseph G. Lambourne",
        "Nishkrit Desai",
        "Karl D. D. Willis",
        "Aditya Sanghi",
        "Nigel J. W. Morris"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The Boundary representation (B-rep) format is the de-facto shape representation in computer-aided design (CAD) to model solid and sheet objects. Recent approaches to generating CAD models have focused on learning sketch-and-extrude modeling sequences that are executed by a solid modeling kernel in postprocess to recover a B-rep. In this paper we present a new approach that enables learning from and synthesizing B-reps without the need for supervision through CAD modeling sequence data. Our method SolidGen, is an autoregressive neural network that models the B-rep directly by predicting the vertices, edges, and faces using Transformer-based and pointer neural networks. Key to achieving this is our Indexed Boundary Representation that references B-rep vertices, edges and faces in a well-defined hierarchy to capture the geometric and topological relations suitable for use with machine learning. SolidGen can be easily conditioned on contexts e.g., class labels, images, and voxels thanks to its probabilistic modeling of the B-rep distribution. We demonstrate qualitatively, quantitatively, and through perceptual evaluation by human subjects that SolidGen can produce high quality, realistic CAD models."
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
      "title": "Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-09-21T08:43:06Z",
      "url": "http://arxiv.org/abs/2209.10191v1",
      "doi": "",
      "authors": [
        "Hao-Xiang Guo",
        "Yang Liu",
        "Hao Pan",
        "Baining Guo"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We present a novel implicit representation -- neural halfspace representation (NH-Rep), to convert manifold B-Rep solids to implicit representations. NH-Rep is a Boolean tree built on a set of implicit functions represented by the neural network, and the composite Boolean function is capable of representing solid geometry while preserving sharp features. We propose an efficient algorithm to extract the Boolean tree from a manifold B-Rep solid and devise a neural network-based optimization approach to compute the implicit functions. We demonstrate the high quality offered by our conversion algorithm on ten thousand manifold B-Rep CAD models that contain various curved patches including NURBS, and the superiority of our learning approach over other representative implicit conversion algorithms in terms of surface reconstruction, sharp feature preservation, signed distance field approximation, and robustness to various surface geometry, as well as a set of applications supported by NH-Rep."
      ]
    },
    {
      "title": "FINER++: Building a Family of Variable-periodic Functions for Activating Implicit Neural Representation",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-07-28T09:24:57Z",
      "url": "http://arxiv.org/abs/2407.19434v1",
      "doi": "",
      "authors": [
        "Hao Zhu",
        "Zhen Liu",
        "Qi Zhang",
        "Jingde Fu",
        "Weibing Deng",
        "Zhan Ma",
        "Yanwen Guo",
        "Xun Cao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Implicit Neural Representation (INR), which utilizes a neural network to map coordinate inputs to corresponding attributes, is causing a revolution in the field of signal processing. However, current INR techniques suffer from the \"frequency\"-specified spectral bias and capacity-convergence gap, resulting in imperfect performance when representing complex signals with multiple \"frequencies\". We have identified that both of these two characteristics could be handled by increasing the utilization of definition domain in current activation functions, for which we propose the FINER++ framework by extending existing periodic/non-periodic activation functions to variable-periodic ones. By initializing the bias of the neural network with different ranges, sub-functions with various frequencies in the variable-periodic function are selected for activation. Consequently, the supported frequency set can be flexibly tuned, leading to improved performance in signal representation. We demonstrate the generalization and capabilities of FINER++ with different activation function backbones (Sine, Gauss. and Wavelet) and various tasks (2D image fitting, 3D signed distance field representation, 5D neural radiance fields optimization and streamable INR transmission), and we show that it improves existing INRs. Project page: {https://liuzhen0212.github.io/finerpp/}"
      ]
    },
    {
      "title": "Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-04T17:55:01Z",
      "url": "http://arxiv.org/abs/2603.04337v1",
      "doi": "",
      "authors": [
        "Dacheng Qi",
        "Chenyu Wang",
        "Jingwei Xu",
        "Tianzhe Chu",
        "Zibo Zhao",
        "Wen Liu",
        "Wenrui Ding",
        "Yi Ma"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error."
      ]
    },
    {
      "title": "Fault Representation in Structural Modelling with Implicit Neural Representations",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-10-31",
      "url": "https://doi.org/10.31223/x5bq48",
      "doi": "10.31223/x5bq48",
      "authors": [
        "Kaifeng Gao",
        "Florian Wellmann"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Implicit neural representations have been demonstrated to provide a flexible and scalable framework for computer graphics and three-dimensional modelling and, consequently, have found their way also into geological modelling. These networks are feature-based and resolution-independent, making them effective for modelling geological structures from scattered interface points, units, and structural orientations. Despite the promising characteristics of existing implicit neural representation approaches, modelling faults within implicit neural representations remains a significant challenge. In this work, we present a fault feature encoding approach to represent faults in implicit neural representations, where the discontinuous information is concatenated as additional features of observation points and query points for network input. We apply this methodology first to a synthetic model to evaluate its efficacy, and subsequently to a real-world dataset from a part of the Gullfaks field in the northern North Sea. The modelling results demonstrate the method’s capacity to generate a well-defined implicit scalar field while preserving sharp transitions at fault locations. Moreover, this work mentions the advantages of the presented approach over using Boolean operations and discontinuous activation functions. Furthermore, we discuss the potential opportunity to integrate prior domain knowledge and geophysics datasets into structural modelling by embedding them as model input features or incorporating them as constraints by loss functions.</jats:p>"
      ]
    },
    {
      "title": "Implicit Neural Representation for Physics-driven Actuated Soft Bodies",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-01-26T13:42:12Z",
      "url": "http://arxiv.org/abs/2401.14861v1",
      "doi": "",
      "authors": [
        "Lingchen Yang",
        "Byungsoo Kim",
        "Gaspard Zoss",
        "Baran Gözcü",
        "Markus Gross",
        "Barbara Solenthaler"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Active soft bodies can affect their shape through an internal actuation mechanism that induces a deformation. Similar to recent work, this paper utilizes a differentiable, quasi-static, and physics-based simulation layer to optimize for actuation signals parameterized by neural networks. Our key contribution is a general and implicit formulation to control active soft bodies by defining a function that enables a continuous mapping from a spatial point in the material space to the actuation value. This property allows us to capture the signal's dominant frequencies, making the method discretization agnostic and widely applicable. We extend our implicit model to mandible kinematics for the particular case of facial animation and show that we can reliably reproduce facial expressions captured with high-quality capture systems. We apply the method to volumetric soft bodies, human poses, and facial expressions, demonstrating artist-friendly properties, such as simple control over the latent space and resolution invariance at test time."
      ]
    },
    {
      "title": "StructEIT: Realistic 3D EIT model generation from CT scans for deep learning applications",
      "source": "Crossref / Physiological Measurement",
      "year": 2026,
      "date": "2026-3-20",
      "url": "https://doi.org/10.1088/1361-6579/ae5587",
      "doi": "10.1088/1361-6579/ae5587",
      "authors": [
        "Zeyi Jiang",
        "Sirui Qiao",
        "Chuanbao Wu",
        "Hui Qin",
        "Yixin Ma"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title> <jats:p>Objective. Artificial intelligence (AI) has significantly improved image reconstruction quality across various medical imaging modalities. However, its application in electrical impedance tomography (EIT) reconstruction remains limited, mainly due to the absence of comprehensive in vivo datasets that incorporate realistic anatomical geometries and conductivity distributions. This limitation constrains the development of supervised and data-driven reconstruction methods. Approach. To address this bottleneck, we developed StructEIT, an integrated EIT modeling framework for generating anatomically and biophysically realistic EIT simulation models. The framework incorporates three key components: (1) a structure extraction module, which automatically processes human CT scans to extract body contours and organ boundaries, thereby providing high-fidelity spatial geometry for 3D finite element modeling; (2) a surface electrode attachment module, which enables flexible and accurate placement of electrodes on irregular body surfaces, supporting diverse configurations and ensuring precise definition of the electrode-tissue interface; and (3) a tissue property assignment module, which establishes frequency-dependent conductivity models for multiple organs, enabling physiologically realistic conductivity values across tissues. Main results and Significance. By bridging the gap between CT imaging and EIT, StructEIT facilitates flexible, realistic, and scalable generation of high-resolution EIT datasets. Using this this framework, we constructed Chest-EIT, a thoracic EIT simulation dataset comprising over 1,400 publicly available CT cases, with multiple electrode configurations provided for each case.</jats:p>"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."
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
      "point cloud to B-Rep deep learning"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2021",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2021",
      "direct B-Rep generation from 3D scans deep learning",
      "neural implicit representation for B-Rep faces and edges"
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
      "query": "point cloud to B-Rep neural network 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep generation from 3D scans transformer",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "SolidGen HoLa AutoBrep point cloud input",
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
      "title": "Hunyuan3D-Omni: A Unified Framework for Controllable Generation of 3D Assets",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-09-25T14:39:17Z",
      "url": "http://arxiv.org/abs/2509.21245v1",
      "doi": "",
      "authors": [
        "Team Hunyuan3D",
        ":",
        "Bowen Zhang",
        "Chunchao Guo",
        "Haolin Liu",
        "Hongyu Yan",
        "Huiwen Shi",
        "Jingwei Huang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent advances in 3D-native generative models have accelerated asset creation for games, film, and design. However, most methods still rely primarily on image or text conditioning and lack fine-grained, cross-modal controls, which limits controllability and practical adoption. To address this gap, we present Hunyuan3D-Omni, a unified framework for fine-grained, controllable 3D asset generation built on Hunyuan3D 2.1. In addition to images, Hunyuan3D-Omni accepts point clouds, voxels, bounding boxes, and skeletal pose priors as conditioning signals, enabling precise control over geometry, topology, and pose. Instead of separate heads for each modality, our model unifies all signals in a single cross-modal architecture. We train with a progressive, difficulty-aware sampling strategy that selects one control modality per example and biases sampling toward harder signals (e.g., skeletal pose) while downweighting easier ones (e.g., point clouds), encouraging robust multi-modal fusion and graceful handling of missing inputs. Experiments show that these additional controls improve generation accuracy, enable geometry-aware transformations, and increase robustness for production workflows."
      ]
    },
    {
      "title": "BRepFormer: Transformer-Based B-rep Geometric Feature Recognition",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-04-10T01:36:06Z",
      "url": "http://arxiv.org/abs/2504.07378v3",
      "doi": "",
      "authors": [
        "Yongkang Dai",
        "Xiaoshui Huang",
        "Yunpeng Bai",
        "Hao Guo",
        "Hongping Gan",
        "Ling Yang",
        "Yilei Shi"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recognizing geometric features on B-rep models is a cornerstone technique for multimedia content-based retrieval and has been widely applied in intelligent manufacturing. However, previous research often merely focused on Machining Feature Recognition (MFR), falling short in effectively capturing the intricate topological and geometric characteristics of complex geometry features. In this paper, we propose BRepFormer, a novel transformer-based model to recognize both machining feature and complex CAD models' features. BRepFormer encodes and fuses the geometric and topological features of the models. Afterwards, BRepFormer utilizes a transformer architecture for feature propagation and a recognition head to identify geometry features. During each iteration of the transformer, we incorporate a bias that combines edge features and topology features to reinforce geometric constraints on each face. In addition, we also proposed a dataset named Complex B-rep Feature Dataset (CBF), comprising 20,000 B-rep models. By covering more complex B-rep models, it is better aligned with industrial applications. The experimental results demonstrate that BRepFormer achieves state-of-the-art accuracy on the MFInstSeg, MFTRCAD, and our CBF datasets."
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural network B-Rep reconstruction from scans",
      "deep learning boundary representation generation point cloud",
      "3D scan to CAD B-Rep deep learning"
    ],
    "effective_query": "point cloud to B-Rep neural network 2023",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep neural network 2023",
      "B-Rep generation from 3D scans transformer",
      "SolidGen HoLa AutoBrep point cloud input"
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
      "query": "point cloud to B-Rep reconstruction neural network 2024",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from 3D scans deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "BRepNet point cloud reconstruction",
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
      "title": "BRep Boundary and Junction Detection for CAD Reverse Engineering",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-04-13",
      "url": "https://doi.org/10.1109/icmi60790.2024.10585950",
      "doi": "10.1109/icmi60790.2024.10585950",
      "authors": [
        "Sk Aziz Ali",
        "Mohammad Sadil Khan",
        "Didier Stricker"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "In machining process, 3D reverse engineering of mechanical system is an integral, highly important, and yet time consuming step to obtain parametric CAD models from 3D scans. Therefore, deep learning-based Scan-to-CAD modeling can offer designers enormous editability to quickly modify CAD model, being able to parse all its structural compositions and design steps. In this paper, we propose a supervised boundary representation (BRep) detection network BRepDetNet from 3D scans of CC3D and ABC dataset. We have carefully annotated the ~50K and ~45K scans of both the datasets with appropriate topological relations (e.g., next, mate, previous) between the geometrical primitives (i.e., boundaries, junctions, loops, faces) of their BRep data structures. The proposed solution decomposes the Scan-to-CAD problem in Scan-to-BRep ensuring the right step towards feature-based modeling, and therefore, leveraging other existing BRep-to-CAD modeling methods. Our proposed Scan-to-BRep neural network learns to detect BRep boundaries and junctions by minimizing focal-loss and non-maximal sup-pression (NMS) during training time. Experimental results show that our BRepDetNet with NMS-Loss achieves impressive results."
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-11-07",
      "url": "http://arxiv.org/abs/2411.04954",
      "doi": "10.48550/arxiv.2411.04954",
      "authors": [
        "Jiasheng Xu",
        "Chenyu Wang",
        "Zheng Zhao",
        "Wenyu Liu",
        "Yi Ma",
        "S. M. Gao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in decreased recognition accuracy. In this paper, we propose a novel deep learning model called the boundary representation graph attention network (BRepGAT) to segment faces in an original boundary representation (B-rep) model containing machining features. We define descriptors that represent information about the faces and edges of the B-rep model from the perspective of feature recognition. These descriptors are extracted from the B-rep model and transformed into homogeneous graph data, which are then passed to graph networks. BRepGAT recognizes machining features from the graph data input. Our experimental results using the MFCAD18++ dataset showed that BRepGAT achieved state-of-the-art recognition accuracy (99.1%). Furthermore, BRepGAT showed relatively robust performance on other datasets besides MFCAD18++."
      ]
    },
    {
      "title": "Extending Point-Based Deep Learning Approaches for Better Semantic Segmentation in CAD",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-10-10",
      "url": "https://doi.org/10.1016/j.cad.2023.103629",
      "doi": "10.1016/j.cad.2023.103629",
      "authors": [
        "Gerico Vidanes",
        "David J. J. Toal",
        "Xu Zhang",
        "Andy J. Keane",
        "Jon Gregory",
        "Marco Nuñez"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Geometry understanding is a core concept of computer-aided design and engineering (CAD/CAE). Deep neural networks have increasingly shown success as a method of processing complex inputs to achieve abstract tasks. This work revisits a generic and relatively simple approach to 3D deep learning - a point-based graph neural network - and develops best-practices and modifications to alleviate traditional drawbacks. It is shown that these methods should not be discounted for CAD tasks; with proper implementation, they can be competitive with more specifically designed approaches. Through an additive study, this work investigates how the boundary representation data can be fully utilised by leveraging the flexibility of point-based graph networks. The final configuration significantly improves on the predictive accuracy of a standard PointNet++ network across multiple CAD model segmentation datasets and achieves state-of-the-art performance on the MFCAD++ machining features dataset. The proposed modifications leave the core neural network unchanged and results also suggest that they can be applied to other point-based approaches."
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
      "title": "3d reconstruction of mine environment based on two-step point cloud alignment algorithm",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6391565",
      "doi": "10.2139/ssrn.6391565",
      "authors": [
        "Ying Zhou",
        "Nan Zhou"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>A two-step point cloud registration algorithm based on improved sampling consistency and iterative nearest neighbors is proposed to meet the daily work needs of coal mine production robots and the rapid rescue needs of post disaster rescue robots. This algorithm helps to obtain a three-dimensional environment reconstruction model of restricted scenes in coal mines. Firstly, align the depth map and color map captured by the Kinect-2 camera, generate a 3D point cloud, and perform preprocessing operations including point cloud simplification, outlier removal, and establishing a 3D topology structure; Then, in response to the unstable geometric features of randomly sampled points and the high computational cost of FPFH features in the sampling consistency algorithm, the point cloud data is simplified using average curvature, combined with two constraints of distance threshold and point cloud average density, to generate feature point sets and matching point sets with richer geometric features. The transformation relationship between corresponding points in the point sets is calculated for point cloud coarse registration; Finally, in response to the problem of the iterative nearest neighbor algorithm easily falling into local optimal solutions due to inaccurate initial values, the iterative nearest neighbor algorithm is combined with the initial transformation matrix generated by coarse registration for precise registration. The proposed algorithm has high reconstruction model realism and better point cloud registration accuracy than mainstream models in unstructured simulation environments and mine tunnel simulation environments, and its feasibility has been verified.</jats:p>"
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
      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",
      "source": "Crossref / Crossref",
      "year": 2025,
      "date": "2025-3-3",
      "url": "https://doi.org/10.20944/preprints202502.2231.v1",
      "doi": "10.20944/preprints202502.2231.v1",
      "authors": [
        "Wen Xie"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstruction accuracy with an average L2 norm error reduction of 18.7% compared to traditional methods. The algorithm shows particular promise for virtual reality applications, especially for placing interactive virtual objects at corners and edges to facilitate user interaction.</jats:p>"
      ]
    },
    {
      "title": "Predicting cranial MRI anatomy from 3D optical surface scans using deep learning for radiation therapy treatment planning",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-9-13",
      "url": "https://doi.org/10.21203/rs.3.rs-2013729/v1",
      "doi": "10.21203/rs.3.rs-2013729/v1",
      "authors": [
        "Michael Douglass",
        "Peter Gorayski",
        "Sandy Patel",
        "Alexandre Santos"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p><bold>Background</bold> Optical scanning technologies are increasingly being utilised to supplement treatment workflows in radiation oncology, such as surface-guided radiotherapy or 3D printing custom bolus. One limitation of optical scanning devices is the absence of internal anatomical information of the patient being scanned. As a result, conventional radiation therapy treatment planning using this imaging modality is not feasible. Deep learning is useful for automating various manual tasks in radiation oncology, most notably, organ segmentation and treatment planning. Deep learning models have also been used to transform MRI datasets into synthetic CT datasets, facilitating the development of MRI-only radiation therapy planning. <bold>Aims</bold> To train a pix2pix generative adversarial network was trained to transform 3D optical scan data into estimated MRI datasets for a given patient to provide additional anatomical data for a select few radiation therapy treatment sites. The proposed network may provide useful anatomical information for treatment planning of surface mould brachytherapy, total body irradiation, and total skin electron therapy, for example, without delivering any imaging dose. <bold>Methods</bold> A 2D pix2pix GAN was trained on 15,000 axial MRI slices of healthy adult brains paired with corresponding external mask slices. The model was validated on a further 5000 previously unseen external mask slices. The predictions were compared with the “ground-truth” MRI slices using the multi-scale structural similarity index (MSSI) metric. A certified neuro-radiologist was subsequently consulted to provide an independent review of the model’s performance in terms of anatomical accuracy and consistency. The network was then applied to a 3D photogrammetry scan of a test subject to demonstrate the feasibility of this novel technique. <bold>Results</bold> The trained pix2pix network predicted MRI slices with a mean MSSI of 0.831 ± 0.057 for the 5000 validation images indicating that it is possible to estimate a significant proportion of a patient’s gross cranial anatomy from a patient’s exterior contour. When independently reviewed by a certified neuro-radiologist, the model’s performance was described as “quite amazing, but there are limitations in the regions where there is wide variation within the normal population.” When the trained network was applied to a 3D model of a human subject acquired using optical photogrammetry, the network could estimate the corresponding MRI volume for that subject with good qualitative accuracy. However, a ground-truth MRI baseline was not available for quantitative comparison. <bold>Conclusions</bold> A deep learning model was developed, to transform 3D optical scan data of a patient into an estimated MRI volume, potentially increasing the usefulness of optical scanning in radiation therapy planning. This work has demonstrated that much of the human cranial anatomy can be predicted from the external shape of the head and may provide an additional source of valuable imaging data. Further research is required to investigate the feasibility of this approach for use in a clinical setting and further improve the model’s accuracy.</p>"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 8 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "B-Rep reconstruction from point cloud deep learning",
      "neural network for B-Rep from 3D scan",
      "point cloud to CAD B-Rep reconstruction"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2024",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2024",
      "B-Rep reconstruction from 3D scans deep learning",
      "BRepNet point cloud reconstruction"
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
  "review_summary": "The retrieval output contains several relevant papers on direct B-Rep generation, but critical gaps exist. The set lacks sufficient evidence of point cloud or 3D scan as the primary input, which is a core user requirement. Several papers appear to focus on generation from other modalities (e.g., text, images) or conversion from B-Rep to implicit representations, not the reverse. The evidence snippets are insufficient to confirm strict exclusion of CAD operation sequences for all candidates. Source coverage is adequate, but the relevance and query fit are not satisfactorily met.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 2-3 are clearly aligned with the user's topic of direct B-Rep generation from point clouds/3D scans. Many papers (e.g., FINER++, Fault Representation, Implicit Neural Representation for Physics-driven Actuated Soft Bodies, StructEIT) are about implicit representations or other applications, not direct B-Rep output from point clouds. The evidence snippets do not strongly confirm the required input-output mapping."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly required methods where the primary input is unstructured point clouds or 3D scans, with multimodal inputs only as a secondary priority for breakthroughs. The retrieved set includes papers that generate B-Reps from images, text, or latent spaces without clear evidence of point cloud input. The strict exclusions (CAD operation sequences, CSG trees) are not verifiably avoided for all papers based on the provided evidence snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be confidently identified as core candidates for direct B-Rep generation from point clouds after inspecting titles and evidence. Papers like SolidGen, HoLa, and AutoBrep are promising but their evidence snippets do not explicitly mention point cloud input. Others are off-topic (implicit representation papers)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: neural methods that take point clouds as input and output B-Reps. The retrieval seems to have captured B-Rep generation papers but not specifically those focused on point cloud input, which is the user's highest priority."
    }
  },
  "key_risks": [
    "The evidence snippets are from abstracts and may not confirm the critical input (point clouds) or the strict exclusion of operation sequences.",
    "Several papers appear to be about implicit neural representations (INR) in general, not B-Rep generation, indicating potential retrieval drift.",
    "The set may mislead the final report by including adjacent work that does not meet the user's strict criteria."
  ],
  "next_actions": [
    "Execute a new query explicitly targeting 'point cloud to B-Rep neural network 2023 2024 2025' to prioritize the required input modality.",
    "Search for known seminal papers in this niche (e.g., 'Point2Cyl', 'BRepNet', 'DeepCAD' but exclude if operation sequence) using specific titles/DOIs to ensure coverage.",
    "Review the abstracts or full texts of the promising candidates (SolidGen, HoLa, AutoBrep, BrepARG) to confirm point cloud input capability and absence of operation sequence output. If evidence is lacking, seek alternative papers."
  ]
}
```

### Review 13

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows improved focus on B-Rep generation with modern neural architectures, but the critical requirement of point cloud or 3D scan as the primary input is still not reliably met. While some papers (e.g., HoLa, BrepGPT) mention point clouds as one of many conditional inputs, the evidence does not establish it as the primary focus. Several papers appear to be about unconditional generation or other tasks (e.g., feature recognition, 3D asset generation). The set lacks clear evidence that the methods are designed for reconstruction from unstructured point clouds, which is the user's highest priority. The exclusion of CAD operation sequences is also not verifiable from the abstracts alone.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Only 2-3 papers (HoLa, BrepGPT) mention point clouds as a possible input, but the evidence snippets do not confirm that point cloud to B-Rep is the primary task. Others are about unconditional generation (BrepGen, DTGBrepGen, AutoBrep, GraphBrep), feature recognition (BRepFormer), or general 3D asset generation (Hunyuan3D-Omni, Neural Point Cloud Diffusion) without clear B-Rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly required methods where the primary input is unstructured point clouds or 3D scans. The retrieved set includes many papers that do not mention point cloud input at all or treat it as one of many conditional inputs. The strict exclusions (CAD operation sequences) are not verifiably avoided based on the provided evidence snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be confidently identified as core candidates for direct B-Rep generation from point clouds. Papers like BrepGen, DTGBrepGen, AutoBrep, GraphBrep appear to be unconditional or multi-modal generators. BRepFormer is a recognition model, not a generator. The evidence is insufficient to confirm core fit."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: neural methods specifically designed for reconstructing B-Reps from point clouds or 3D scans. The retrieval has drifted towards general B-Rep generation and other tasks."
    }
  },
  "key_risks": [
    "The evidence snippets are from abstracts and may not confirm the primary input modality or the strict exclusion of operation sequences.",
    "Many papers appear to be about unconditional B-Rep generation or generation from other modalities, not reconstruction from point clouds.",
    "Including papers like BRepFormer (feature recognition) and Hunyuan3D-Omni (general 3D asset generation) could mislead the final report."
  ],
  "next_actions": [
    "Execute a targeted query for 'point cloud to B-Rep reconstruction neural network 2024' to specifically seek reconstruction papers, not just generation.",
    "Search for known papers that explicitly tackle 'B-Rep reconstruction from point clouds' using specific phrases, possibly including 'BRepNet' or 'Point2Cyl' (though check year and exclusion criteria).",
    "For the most promising candidates (HoLa, BrepGPT), retrieve full abstracts or introduction snippets to confirm point cloud input capability and absence of operation sequence output. If evidence is lacking, exclude them."
  ]
}
```

### Review 19

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output has shifted towards point cloud reconstruction and segmentation tasks, but it now largely misses the core requirement of direct B-Rep generation. Most papers are about point cloud processing, feature recognition, or general 3D reconstruction, not about outputting a B-Rep data structure (faces, edges, vertices, topology). Only one paper (BRep Boundary and Junction Detection) explicitly mentions B-Rep detection from scans, but it appears to be a detection/segmentation step, not full B-Rep reconstruction. The set fails to capture the frontier research on neural B-Rep generation from point clouds. The evidence snippets are insufficient to confirm B-Rep output for most candidates.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 1 (BRep Boundary and Junction Detection) is clearly aligned with B-Rep from point clouds, and even that is a detection network, not a full reconstruction/generation model. The others are about point cloud reconstruction, segmentation, or other applications without B-Rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user required papers that directly output B-Rep data structures from point clouds. The retrieved set includes papers on point cloud reconstruction (PC^2, mine environment reconstruction, partial missing reconstruction, depth-first search coordinate reconstruction) that do not mention B-Rep output. Others are about CAD generation from multimodal inputs (CAD-MLLM) or B-Rep feature segmentation (BRepGAT, Extending Point-Based Deep Learning). These do not fit the strict criteria."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be identified as core candidates for direct B-Rep reconstruction from point clouds. The only candidate (BRep Boundary and Junction Detection) is a detection network, not a full generator. The evidence snippets do not support that any paper outputs a complete B-Rep data structure."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a massive missing core: papers that directly reconstruct/generate B-Reps from point clouds using neural networks. The retrieval has over-corrected and now captures general point cloud reconstruction and CAD segmentation, missing the target topic entirely."
    }
  },
  "key_risks": [
    "The retrieval has drifted away from B-Rep generation/reconstruction and into general point cloud processing and CAD segmentation.",
    "Including papers like PC^2 (single-image 3D reconstruction), mine environment reconstruction, and medical imaging prediction would severely mislead the final report.",
    "The evidence snippets do not confirm B-Rep output for any paper except possibly the BRep detection paper, which is not a full reconstruction model."
  ],
  "next_actions": [
    "Return to the previous retrieval's promising B-Rep generation papers (SolidGen, HoLa, AutoBrep, BrepGen) and explicitly verify their input modalities by retrieving full abstracts or introduction sections. If they support point cloud conditioning, they may be acceptable.",
    "Execute a hybrid query: 'B-Rep generation from point clouds transformer 2023 2024 2025' to bridge generation and reconstruction.",
    "Search for specific known papers that combine point clouds and B-Reps, such as 'Point2Cyl' or 'BRepNet', but ensure they are within the time range and do not output operation sequences."
  ]
}
```

## Tool Activity

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_lwmzFo63M5fXZdNLdLBf66aY', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2021",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-Rep generation from 3D scans deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "neural implicit representation for B-Rep faces and edges",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "SolidGen: An Autoregressive Model for Direct B-rep Synthesis",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-03-26T00:00:45Z",\n      "url": "http://arxiv.org/abs/2203.13944v2",\n      "doi": "",\n      "authors": [\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Nishkrit Desai",\n        "Karl D. D. Willis",\n        "Aditya Sanghi",\n        "Nigel J. W. Morris"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The Boundary representation (B-rep) format is the de-facto shape representation in computer-aided design (CAD) to model solid and sheet objects. Recent approaches to generating CAD models have focused on learning sketch-and-extrude modeling sequences that are executed by a solid modeling kernel in postprocess to recover a B-rep. In this paper we present a new approach that enables learning from and synthesizing B-reps without the need for supervision through CAD modeling sequence data. Our method SolidGen, is an autoregressive neural network that models the B-rep directly by predicting the vertices, edges, and faces using Transformer-based and pointer neural networks. Key to achieving this is our Indexed Boundary Representation that references B-rep vertices, edges and faces in a well-defined hierarchy to capture the geometric and topological relations suitable for use with machine learning. SolidGen can be easily conditioned on contexts e.g., class labels, images, and voxels thanks to its probabilistic modeling of the B-rep distribution. We demonstrate qualitatively, quantitatively, and through perceptual evaluation by human subjects that SolidGen can produce high quality, realistic CAD models."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-09-21T08:43:06Z",\n      "url": "http://arxiv.org/abs/2209.10191v1",\n      "doi": "",\n      "authors": [\n        "Hao-Xiang Guo",\n        "Yang Liu",\n        "Hao Pan",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We present a novel implicit representation -- neural halfspace representation (NH-Rep), to convert manifold B-Rep solids to implicit representations. NH-Rep is a Boolean tree built on a set of implicit functions represented by the neural network, and the composite Boolean function is capable of representing solid geometry while preserving sharp features. We propose an efficient algorithm to extract the Boolean tree from a manifold B-Rep solid and devise a neural network-based optimization approach to compute the implicit functions. We demonstrate the high quality offered by our conversion algorithm on ten thousand manifold B-Rep CAD models that contain various curved patches including NURBS, and the superiority of our learning approach over other representative implicit conversion algorithms in terms of surface reconstruction, sharp feature preservation, signed distance field approximation, and robustness to various surface geometry, as well as a set of applications supported by NH-Rep."\n      ]\n    },\n    {\n      "title": "FINER++: Building a Family of Variable-periodic Functions for Activating Implicit Neural Representation",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-28T09:24:57Z",\n      "url": "http://arxiv.org/abs/2407.19434v1",\n      "doi": "",\n      "authors": [\n        "Hao Zhu",\n        "Zhen Liu",\n        "Qi Zhang",\n        "Jingde Fu",\n        "Weibing Deng",\n        "Zhan Ma",\n        "Yanwen Guo",\n        "Xun Cao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Implicit Neural Representation (INR), which utilizes a neural network to map coordinate inputs to corresponding attributes, is causing a revolution in the field of signal processing. However, current INR techniques suffer from the \\"frequency\\"-specified spectral bias and capacity-convergence gap, resulting in imperfect performance when representing complex signals with multiple \\"frequencies\\". We have identified that both of these two characteristics could be handled by increasing the utilization of definition domain in current activation functions, for which we propose the FINER++ framework by extending existing periodic/non-periodic activation functions to variable-periodic ones. By initializing the bias of the neural network with different ranges, sub-functions with various frequencies in the variable-periodic function are selected for activation. Consequently, the supported frequency set can be flexibly tuned, leading to improved performance in signal representation. We demonstrate the generalization and capabilities of FINER++ with different activation function backbones (Sine, Gauss. and Wavelet) and various tasks (2D image fitting, 3D signed distance field representation, 5D neural radiance fields optimization and streamable INR transmission), and we show that it improves existing INRs. Project page: {https://liuzhen0212.github.io/finerpp/}"\n      ]\n    },\n    {\n      "title": "Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-04T17:55:01Z",\n      "url": "http://arxiv.org/abs/2603.04337v1",\n      "doi": "",\n      "authors": [\n        "Dacheng Qi",\n        "Chenyu Wang",\n        "Jingwei Xu",\n        "Tianzhe Chu",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Wenrui Ding",\n        "Yi Ma"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error."\n      ]\n    },\n    {\n      "title": "Fault Representation in Structural Modelling with Implicit Neural Representations",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-10-31",\n      "url": "https://doi.org/10.31223/x5bq48",\n      "doi": "10.31223/x5bq48",\n      "authors": [\n        "Kaifeng Gao",\n        "Florian Wellmann"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Implicit neural representations have been demonstrated to provide a flexible and scalable framework for computer graphics and three-dimensional modelling and, consequently, have found their way also into geological modelling. These networks are feature-based and resolution-independent, making them effective for modelling geological structures from scattered interface points, units, and structural orientations. Despite the promising characteristics of existing implicit neural representation approaches, modelling faults within implicit neural representations remains a significant challenge. In this work, we present a fault feature encoding approach to represent faults in implicit neural representations, where the discontinuous information is concatenated as additional features of observation points and query points for network input. We apply this methodology first to a synthetic model to evaluate its efficacy, and subsequently to a real-world dataset from a part of the Gullfaks field in the northern North Sea. The modelling results demonstrate the method’s capacity to generate a well-defined implicit scalar field while preserving sharp transitions at fault locations. Moreover, this work mentions the advantages of the presented approach over using Boolean operations and discontinuous activation functions. Furthermore, we discuss the potential opportunity to integrate prior domain knowledge and geophysics datasets into structural modelling by embedding them as model input features or incorporating them as constraints by loss functions.</jats:p>"\n      ]\n    },\n    {\n      "title": "Implicit Neural Representation for Physics-driven Actuated Soft Bodies",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-26T13:42:12Z",\n      "url": "http://arxiv.org/abs/2401.14861v1",\n      "doi": "",\n      "authors": [\n        "Lingchen Yang",\n        "Byungsoo Kim",\n        "Gaspard Zoss",\n        "Baran Gözcü",\n        "Markus Gross",\n        "Barbara Solenthaler"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Active soft bodies can affect their shape through an internal actuation mechanism that induces a deformation. Similar to recent work, this paper utilizes a differentiable, quasi-static, and physics-based simulation layer to optimize for actuation signals parameterized by neural networks. Our key contribution is a general and implicit formulation to control active soft bodies by defining a function that enables a continuous mapping from a spatial point in the material space to the actuation value. This property allows us to capture the signal\'s dominant frequencies, making the method discretization agnostic and widely applicable. We extend our implicit model to mandible kinematics for the particular case of facial animation and show that we can reliably reproduce facial expressions captured with high-quality capture systems. We apply the method to volumetric soft bodies, human poses, and facial expressions, demonstrating artist-friendly properties, such as simple control over the latent space and resolution invariance at test time."\n      ]\n    },\n    {\n      "title": "StructEIT: Realistic 3D EIT model generation from CT scans for deep learning applications",\n      "source": "Crossref / Physiological Measurement",\n      "year": 2026,\n      "date": "2026-3-20",\n      "url": "https://doi.org/10.1088/1361-6579/ae5587",\n      "doi": "10.1088/1361-6579/ae5587",\n      "authors": [\n        "Zeyi Jiang",\n        "Sirui Qiao",\n        "Chuanbao Wu",\n        "Hui Qin",\n        "Yixin Ma"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title> <jats:p>Objective. Artificial intelligence (AI) has significantly improved image reconstruction quality across various medical imaging modalities. However, its application in electrical impedance tomography (EIT) reconstruction remains limited, mainly due to the absence of comprehensive in vivo datasets that incorporate realistic anatomical geometries and conductivity distributions. This limitation constrains the development of supervised and data-driven reconstruction methods. Approach. To address this bottleneck, we developed StructEIT, an integrated EIT modeling framework for generating anatomically and biophysically realistic EIT simulation models. The framework incorporates three key components: (1) a structure extraction module, which automatically processes human CT scans to extract body contours and organ boundaries, thereby providing high-fidelity spatial geometry for 3D finite element modeling; (2) a surface electrode attachment module, which enables flexible and accurate placement of electrodes on irregular body surfaces, supporting diverse configurations and ensuring precise definition of the electrode-tissue interface; and (3) a tissue property assignment module, which establishes frequency-dependent conductivity models for multiple organs, enabling physiologically realistic conductivity values across tissues. Main results and Significance. By bridging the gap between CT imaging and EIT, StructEIT facilitates flexible, realistic, and scalable generation of high-resolution EIT datasets. Using this this framework, we constructed Chest-EIT, a thoracic EIT simulation dataset comprising over 1,400 publicly available CT cases, with multiple electrode configurations provided for each case.</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction",\n      "deep learning boundary representation generation",\n      "point cloud to B-Rep deep learning"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2021",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2021",\n      "direct B-Rep generation from 3D scans deep learning",\n      "neural implicit representation for B-Rep faces and edges"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_lwmzFo63M5fXZdNLdLBf66aY' is_error=False
```

### Tool Event 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_UDbNOv8i0JXc7VBvFmB00Tx0', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-Rep neural network 2023"}', name='retrieve_candidates_from_plan')
```

### Tool Event 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep neural network 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep generation from 3D scans transformer",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "SolidGen HoLa AutoBrep point cloud input",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    },\n    {\n      "title": "Hunyuan3D-Omni: A Unified Framework for Controllable Generation of 3D Assets",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-09-25T14:39:17Z",\n      "url": "http://arxiv.org/abs/2509.21245v1",\n      "doi": "",\n      "authors": [\n        "Team Hunyuan3D",\n        ":",\n        "Bowen Zhang",\n        "Chunchao Guo",\n        "Haolin Liu",\n        "Hongyu Yan",\n        "Huiwen Shi",\n        "Jingwei Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent advances in 3D-native generative models have accelerated asset creation for games, film, and design. However, most methods still rely primarily on image or text conditioning and lack fine-grained, cross-modal controls, which limits controllability and practical adoption. To address this gap, we present Hunyuan3D-Omni, a unified framework for fine-grained, controllable 3D asset generation built on Hunyuan3D 2.1. In addition to images, Hunyuan3D-Omni accepts point clouds, voxels, bounding boxes, and skeletal pose priors as conditioning signals, enabling precise control over geometry, topology, and pose. Instead of separate heads for each modality, our model unifies all signals in a single cross-modal architecture. We train with a progressive, difficulty-aware sampling strategy that selects one control modality per example and biases sampling toward harder signals (e.g., skeletal pose) while downweighting easier ones (e.g., point clouds), encouraging robust multi-modal fusion and graceful handling of missing inputs. Experiments show that these additional controls improve generation accuracy, enable geometry-aware transformations, and increase robustness for production workflows."\n      ]\n    },\n    {\n      "title": "BRepFormer: Transformer-Based B-rep Geometric Feature Recognition",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-10T01:36:06Z",\n      "url": "http://arxiv.org/abs/2504.07378v3",\n      "doi": "",\n      "authors": [\n        "Yongkang Dai",\n        "Xiaoshui Huang",\n        "Yunpeng Bai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Ling Yang",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recognizing geometric features on B-rep models is a cornerstone technique for multimedia content-based retrieval and has been widely applied in intelligent manufacturing. However, previous research often merely focused on Machining Feature Recognition (MFR), falling short in effectively capturing the intricate topological and geometric characteristics of complex geometry features. In this paper, we propose BRepFormer, a novel transformer-based model to recognize both machining feature and complex CAD models\' features. BRepFormer encodes and fuses the geometric and topological features of the models. Afterwards, BRepFormer utilizes a transformer architecture for feature propagation and a recognition head to identify geometry features. During each iteration of the transformer, we incorporate a bias that combines edge features and topology features to reinforce geometric constraints on each face. In addition, we also proposed a dataset named Complex B-rep Feature Dataset (CBF), comprising 20,000 B-rep models. By covering more complex B-rep models, it is better aligned with industrial applications. The experimental results demonstrate that BRepFormer achieves state-of-the-art accuracy on the MFInstSeg, MFTRCAD, and our CBF datasets."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction from scans",\n      "deep learning boundary representation generation point cloud",\n      "3D scan to CAD B-Rep deep learning"\n    ],\n    "effective_query": "point cloud to B-Rep neural network 2023",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep neural network 2023",\n      "B-Rep generation from 3D scans transformer",\n      "SolidGen HoLa AutoBrep point cloud input"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_UDbNOv8i0JXc7VBvFmB00Tx0' is_error=False
```

### Tool Event 16

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_HBxMwhjDTfeFpDIaoc1bHEE0', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-Rep reconstruction neural network 2024"}', name='retrieve_candidates_from_plan')
```

### Tool Event 17

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from 3D scans deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "BRepNet point cloud reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BRep Boundary and Junction Detection for CAD Reverse Engineering",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-04-13",\n      "url": "https://doi.org/10.1109/icmi60790.2024.10585950",\n      "doi": "10.1109/icmi60790.2024.10585950",\n      "authors": [\n        "Sk Aziz Ali",\n        "Mohammad Sadil Khan",\n        "Didier Stricker"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "In machining process, 3D reverse engineering of mechanical system is an integral, highly important, and yet time consuming step to obtain parametric CAD models from 3D scans. Therefore, deep learning-based Scan-to-CAD modeling can offer designers enormous editability to quickly modify CAD model, being able to parse all its structural compositions and design steps. In this paper, we propose a supervised boundary representation (BRep) detection network BRepDetNet from 3D scans of CC3D and ABC dataset. We have carefully annotated the ~50K and ~45K scans of both the datasets with appropriate topological relations (e.g., next, mate, previous) between the geometrical primitives (i.e., boundaries, junctions, loops, faces) of their BRep data structures. The proposed solution decomposes the Scan-to-CAD problem in Scan-to-BRep ensuring the right step towards feature-based modeling, and therefore, leveraging other existing BRep-to-CAD modeling methods. Our proposed Scan-to-BRep neural network learns to detect BRep boundaries and junctions by minimizing focal-loss and non-maximal sup-pression (NMS) during training time. Experimental results show that our BRepDetNet with NMS-Loss achieves impressive results."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-11-07",\n      "url": "http://arxiv.org/abs/2411.04954",\n      "doi": "10.48550/arxiv.2411.04954",\n      "authors": [\n        "Jiasheng Xu",\n        "Chenyu Wang",\n        "Zheng Zhao",\n        "Wenyu Liu",\n        "Yi Ma",\n        "S. M. Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-11-03",\n      "url": "https://doi.org/10.1093/jcde/qwad106",\n      "doi": "10.1093/jcde/qwad106",\n      "authors": [\n        "Jinwon Lee",\n        "Changmo Yeo",\n        "Sang-Uk Cheon",\n        "Jun Hwan Park",\n        "Duhwan Mun"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in decreased recognition accuracy. In this paper, we propose a novel deep learning model called the boundary representation graph attention network (BRepGAT) to segment faces in an original boundary representation (B-rep) model containing machining features. We define descriptors that represent information about the faces and edges of the B-rep model from the perspective of feature recognition. These descriptors are extracted from the B-rep model and transformed into homogeneous graph data, which are then passed to graph networks. BRepGAT recognizes machining features from the graph data input. Our experimental results using the MFCAD18++ dataset showed that BRepGAT achieved state-of-the-art recognition accuracy (99.1%). Furthermore, BRepGAT showed relatively robust performance on other datasets besides MFCAD18++."\n      ]\n    },\n    {\n      "title": "Extending Point-Based Deep Learning Approaches for Better Semantic Segmentation in CAD",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-10-10",\n      "url": "https://doi.org/10.1016/j.cad.2023.103629",\n      "doi": "10.1016/j.cad.2023.103629",\n      "authors": [\n        "Gerico Vidanes",\n        "David J. J. Toal",\n        "Xu Zhang",\n        "Andy J. Keane",\n        "Jon Gregory",\n        "Marco Nuñez"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Geometry understanding is a core concept of computer-aided design and engineering (CAD/CAE). Deep neural networks have increasingly shown success as a method of processing complex inputs to achieve abstract tasks. This work revisits a generic and relatively simple approach to 3D deep learning - a point-based graph neural network - and develops best-practices and modifications to alleviate traditional drawbacks. It is shown that these methods should not be discounted for CAD tasks; with proper implementation, they can be competitive with more specifically designed approaches. Through an additive study, this work investigates how the boundary representation data can be fully utilised by leveraging the flexibility of point-based graph networks. The final configuration significantly improves on the predictive accuracy of a standard PointNet++ network across multiple CAD model segmentation datasets and achieves state-of-the-art performance on the MFCAD++ machining features dataset. The proposed modifications leave the core neural network unchanged and results also suggest that they can be applied to other point-based approaches."\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    },\n    {\n      "title": "3d reconstruction of mine environment based on two-step point cloud alignment algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6391565",\n      "doi": "10.2139/ssrn.6391565",\n      "authors": [\n        "Ying Zhou",\n        "Nan Zhou"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>A two-step point cloud registration algorithm based on improved sampling consistency and iterative nearest neighbors is proposed to meet the daily work needs of coal mine production robots and the rapid rescue needs of post disaster rescue robots. This algorithm helps to obtain a three-dimensional environment reconstruction model of restricted scenes in coal mines. Firstly, align the depth map and color map captured by the Kinect-2 camera, generate a 3D point cloud, and perform preprocessing operations including point cloud simplification, outlier removal, and establishing a 3D topology structure; Then, in response to the unstable geometric features of randomly sampled points and the high computational cost of FPFH features in the sampling consistency algorithm, the point cloud data is simplified using average curvature, combined with two constraints of distance threshold and point cloud average density, to generate feature point sets and matching point sets with richer geometric features. The transformation relationship between corresponding points in the point sets is calculated for point cloud coarse registration; Finally, in response to the problem of the iterative nearest neighbor algorithm easily falling into local optimal solutions due to inaccurate initial values, the iterative nearest neighbor algorithm is combined with the initial transformation matrix generated by coarse registration for precise registration. The proposed algorithm has high reconstruction model realism and better point cloud registration accuracy than mainstream models in unstructured simulation environments and mine tunnel simulation environments, and its feasibility has been verified.</jats:p>"\n      ]\n    },\n    {\n      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-06-23T02:21:48Z",\n      "url": "http://arxiv.org/abs/2406.15982v1",\n      "doi": "",\n      "authors": [\n        "Yangdi Lu",\n        "Wenbo He"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."\n      ]\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"\n      ]\n    },\n    {\n      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2025,\n      "date": "2025-3-3",\n      "url": "https://doi.org/10.20944/preprints202502.2231.v1",\n      "doi": "10.20944/preprints202502.2231.v1",\n      "authors": [\n        "Wen Xie"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstruction accuracy with an average L2 norm error reduction of 18.7% compared to traditional methods. The algorithm shows particular promise for virtual reality applications, especially for placing interactive virtual objects at corners and edges to facilitate user interaction.</jats:p>"\n      ]\n    },\n    {\n      "title": "Predicting cranial MRI anatomy from 3D optical surface scans using deep learning for radiation therapy treatment planning",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-9-13",\n      "url": "https://doi.org/10.21203/rs.3.rs-2013729/v1",\n      "doi": "10.21203/rs.3.rs-2013729/v1",\n      "authors": [\n        "Michael Douglass",\n        "Peter Gorayski",\n        "Sandy Patel",\n        "Alexandre Santos"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p><bold>Background</bold> Optical scanning technologies are increasingly being utilised to supplement treatment workflows in radiation oncology, such as surface-guided radiotherapy or 3D printing custom bolus. One limitation of optical scanning devices is the absence of internal anatomical information of the patient being scanned. As a result, conventional radiation therapy treatment planning using this imaging modality is not feasible. Deep learning is useful for automating various manual tasks in radiation oncology, most notably, organ segmentation and treatment planning. Deep learning models have also been used to transform MRI datasets into synthetic CT datasets, facilitating the development of MRI-only radiation therapy planning. <bold>Aims</bold> To train a pix2pix generative adversarial network was trained to transform 3D optical scan data into estimated MRI datasets for a given patient to provide additional anatomical data for a select few radiation therapy treatment sites. The proposed network may provide useful anatomical information for treatment planning of surface mould brachytherapy, total body irradiation, and total skin electron therapy, for example, without delivering any imaging dose. <bold>Methods</bold> A 2D pix2pix GAN was trained on 15,000 axial MRI slices of healthy adult brains paired with corresponding external mask slices. The model was validated on a further 5000 previously unseen external mask slices. The predictions were compared with the “ground-truth” MRI slices using the multi-scale structural similarity index (MSSI) metric. A certified neuro-radiologist was subsequently consulted to provide an independent review of the model’s performance in terms of anatomical accuracy and consistency. The network was then applied to a 3D photogrammetry scan of a test subject to demonstrate the feasibility of this novel technique. <bold>Results</bold> The trained pix2pix network predicted MRI slices with a mean MSSI of 0.831 ± 0.057 for the 5000 validation images indicating that it is possible to estimate a significant proportion of a patient’s gross cranial anatomy from a patient’s exterior contour. When independently reviewed by a certified neuro-radiologist, the model’s performance was described as “quite amazing, but there are limitations in the regions where there is wide variation within the normal population.” When the trained network was applied to a 3D model of a human subject acquired using optical photogrammetry, the network could estimate the corresponding MRI volume for that subject with good qualitative accuracy. However, a ground-truth MRI baseline was not available for quantitative comparison. <bold>Conclusions</bold> A deep learning model was developed, to transform 3D optical scan data of a patient into an estimated MRI volume, potentially increasing the usefulness of optical scanning in radiation therapy planning. This work has demonstrated that much of the human cranial anatomy can be predicted from the external shape of the head and may provide an additional source of valuable imaging data. Further research is required to investigate the feasibility of this approach for use in a clinical setting and further improve the model’s accuracy.</p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 8 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "B-Rep reconstruction from point cloud deep learning",\n      "neural network for B-Rep from 3D scan",\n      "point cloud to CAD B-Rep reconstruction"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2024",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2024",\n      "B-Rep reconstruction from 3D scans deep learning",\n      "BRepNet point cloud reconstruction"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_HBxMwhjDTfeFpDIaoc1bHEE0' is_error=False
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
  "user_intent": "Find 8-10 state-of-the-art papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry",
    "latent space representations for B-Reps",
    "end-to-end learning from point clouds to B-Reps",
    "variational methods for B-Rep generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "step-by-step modeling history output"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction",
    "deep learning boundary representation generation",
    "point cloud to B-Rep deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2021",
      "reason": "Targets the core task with a focus on neural methods and anchors the start of the time range."
    },
    {
      "query": "direct B-Rep generation from 3D scans deep learning",
      "reason": "Emphasizes direct output of the B-Rep structure, excluding intermediate representations like sequences."
    },
    {
      "query": "neural implicit representation for B-Rep faces and edges",
      "reason": "Focuses on modern architectural approaches for representing continuous B-Rep geometry and topology."
    }
  ],
  "assumptions": [
    "The user wants frontier research, so the search should prioritize top-tier venues (CVPR, SIGGRAPH, NeurIPS, etc.).",
    "The phrase 'between 2021-2026' is interpreted as inclusive of both years.",
    "Methods that output a B-Rep mesh (with topological adjacency) qualify, even if they use intermediate neural fields, as long as the final output is the B-Rep data structure.",
    "If fewer than 8-10 papers perfectly match the strict criteria within the time range, the retrieval should include the most relevant ones, and the report will note the scarcity."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must use point clouds or 3D scans as a primary or acceptable input.",
    "Papers must employ modern neural architectures (e.g., transformers, graph networks, implicit functions).",
    "No included paper should focus on reconstructing CAD modeling sequences or CSG trees."
  ]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute the search plan to find papers on 3D B-Rep reconstruction and generation from point clouds using neural networks, focusing on the 2021-2026 timeframe.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_lwmzFo63M5fXZdNLdLBf66aY', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2021",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "direct B-Rep generation from 3D scans deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "neural implicit representation for B-Rep faces and edges",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "SolidGen: An Autoregressive Model for Direct B-rep Synthesis",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-03-26T00:00:45Z",\n      "url": "http://arxiv.org/abs/2203.13944v2",\n      "doi": "",\n      "authors": [\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Nishkrit Desai",\n        "Karl D. D. Willis",\n        "Aditya Sanghi",\n        "Nigel J. W. Morris"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The Boundary representation (B-rep) format is the de-facto shape representation in computer-aided design (CAD) to model solid and sheet objects. Recent approaches to generating CAD models have focused on learning sketch-and-extrude modeling sequences that are executed by a solid modeling kernel in postprocess to recover a B-rep. In this paper we present a new approach that enables learning from and synthesizing B-reps without the need for supervision through CAD modeling sequence data. Our method SolidGen, is an autoregressive neural network that models the B-rep directly by predicting the vertices, edges, and faces using Transformer-based and pointer neural networks. Key to achieving this is our Indexed Boundary Representation that references B-rep vertices, edges and faces in a well-defined hierarchy to capture the geometric and topological relations suitable for use with machine learning. SolidGen can be easily conditioned on contexts e.g., class labels, images, and voxels thanks to its probabilistic modeling of the B-rep distribution. We demonstrate qualitatively, quantitatively, and through perceptual evaluation by human subjects that SolidGen can produce high quality, realistic CAD models."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation",\n      "source": "arXiv",\n      "year": 2022,\n      "date": "2022-09-21T08:43:06Z",\n      "url": "http://arxiv.org/abs/2209.10191v1",\n      "doi": "",\n      "authors": [\n        "Hao-Xiang Guo",\n        "Yang Liu",\n        "Hao Pan",\n        "Baining Guo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We present a novel implicit representation -- neural halfspace representation (NH-Rep), to convert manifold B-Rep solids to implicit representations. NH-Rep is a Boolean tree built on a set of implicit functions represented by the neural network, and the composite Boolean function is capable of representing solid geometry while preserving sharp features. We propose an efficient algorithm to extract the Boolean tree from a manifold B-Rep solid and devise a neural network-based optimization approach to compute the implicit functions. We demonstrate the high quality offered by our conversion algorithm on ten thousand manifold B-Rep CAD models that contain various curved patches including NURBS, and the superiority of our learning approach over other representative implicit conversion algorithms in terms of surface reconstruction, sharp feature preservation, signed distance field approximation, and robustness to various surface geometry, as well as a set of applications supported by NH-Rep."\n      ]\n    },\n    {\n      "title": "FINER++: Building a Family of Variable-periodic Functions for Activating Implicit Neural Representation",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-07-28T09:24:57Z",\n      "url": "http://arxiv.org/abs/2407.19434v1",\n      "doi": "",\n      "authors": [\n        "Hao Zhu",\n        "Zhen Liu",\n        "Qi Zhang",\n        "Jingde Fu",\n        "Weibing Deng",\n        "Zhan Ma",\n        "Yanwen Guo",\n        "Xun Cao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Implicit Neural Representation (INR), which utilizes a neural network to map coordinate inputs to corresponding attributes, is causing a revolution in the field of signal processing. However, current INR techniques suffer from the \\"frequency\\"-specified spectral bias and capacity-convergence gap, resulting in imperfect performance when representing complex signals with multiple \\"frequencies\\". We have identified that both of these two characteristics could be handled by increasing the utilization of definition domain in current activation functions, for which we propose the FINER++ framework by extending existing periodic/non-periodic activation functions to variable-periodic ones. By initializing the bias of the neural network with different ranges, sub-functions with various frequencies in the variable-periodic function are selected for activation. Consequently, the supported frequency set can be flexibly tuned, leading to improved performance in signal representation. We demonstrate the generalization and capabilities of FINER++ with different activation function backbones (Sine, Gauss. and Wavelet) and various tasks (2D image fitting, 3D signed distance field representation, 5D neural radiance fields optimization and streamable INR transmission), and we show that it improves existing INRs. Project page: {https://liuzhen0212.github.io/finerpp/}"\n      ]\n    },\n    {\n      "title": "Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-03-04T17:55:01Z",\n      "url": "http://arxiv.org/abs/2603.04337v1",\n      "doi": "",\n      "authors": [\n        "Dacheng Qi",\n        "Chenyu Wang",\n        "Jingwei Xu",\n        "Tianzhe Chu",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Wenrui Ding",\n        "Yi Ma"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error."\n      ]\n    },\n    {\n      "title": "Fault Representation in Structural Modelling with Implicit Neural Representations",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-10-31",\n      "url": "https://doi.org/10.31223/x5bq48",\n      "doi": "10.31223/x5bq48",\n      "authors": [\n        "Kaifeng Gao",\n        "Florian Wellmann"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>Implicit neural representations have been demonstrated to provide a flexible and scalable framework for computer graphics and three-dimensional modelling and, consequently, have found their way also into geological modelling. These networks are feature-based and resolution-independent, making them effective for modelling geological structures from scattered interface points, units, and structural orientations. Despite the promising characteristics of existing implicit neural representation approaches, modelling faults within implicit neural representations remains a significant challenge. In this work, we present a fault feature encoding approach to represent faults in implicit neural representations, where the discontinuous information is concatenated as additional features of observation points and query points for network input. We apply this methodology first to a synthetic model to evaluate its efficacy, and subsequently to a real-world dataset from a part of the Gullfaks field in the northern North Sea. The modelling results demonstrate the method’s capacity to generate a well-defined implicit scalar field while preserving sharp transitions at fault locations. Moreover, this work mentions the advantages of the presented approach over using Boolean operations and discontinuous activation functions. Furthermore, we discuss the potential opportunity to integrate prior domain knowledge and geophysics datasets into structural modelling by embedding them as model input features or incorporating them as constraints by loss functions.</jats:p>"\n      ]\n    },\n    {\n      "title": "Implicit Neural Representation for Physics-driven Actuated Soft Bodies",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-26T13:42:12Z",\n      "url": "http://arxiv.org/abs/2401.14861v1",\n      "doi": "",\n      "authors": [\n        "Lingchen Yang",\n        "Byungsoo Kim",\n        "Gaspard Zoss",\n        "Baran Gözcü",\n        "Markus Gross",\n        "Barbara Solenthaler"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Active soft bodies can affect their shape through an internal actuation mechanism that induces a deformation. Similar to recent work, this paper utilizes a differentiable, quasi-static, and physics-based simulation layer to optimize for actuation signals parameterized by neural networks. Our key contribution is a general and implicit formulation to control active soft bodies by defining a function that enables a continuous mapping from a spatial point in the material space to the actuation value. This property allows us to capture the signal\'s dominant frequencies, making the method discretization agnostic and widely applicable. We extend our implicit model to mandible kinematics for the particular case of facial animation and show that we can reliably reproduce facial expressions captured with high-quality capture systems. We apply the method to volumetric soft bodies, human poses, and facial expressions, demonstrating artist-friendly properties, such as simple control over the latent space and resolution invariance at test time."\n      ]\n    },\n    {\n      "title": "StructEIT: Realistic 3D EIT model generation from CT scans for deep learning applications",\n      "source": "Crossref / Physiological Measurement",\n      "year": 2026,\n      "date": "2026-3-20",\n      "url": "https://doi.org/10.1088/1361-6579/ae5587",\n      "doi": "10.1088/1361-6579/ae5587",\n      "authors": [\n        "Zeyi Jiang",\n        "Sirui Qiao",\n        "Chuanbao Wu",\n        "Hui Qin",\n        "Yixin Ma"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:title>Abstract</jats:title> <jats:p>Objective. Artificial intelligence (AI) has significantly improved image reconstruction quality across various medical imaging modalities. However, its application in electrical impedance tomography (EIT) reconstruction remains limited, mainly due to the absence of comprehensive in vivo datasets that incorporate realistic anatomical geometries and conductivity distributions. This limitation constrains the development of supervised and data-driven reconstruction methods. Approach. To address this bottleneck, we developed StructEIT, an integrated EIT modeling framework for generating anatomically and biophysically realistic EIT simulation models. The framework incorporates three key components: (1) a structure extraction module, which automatically processes human CT scans to extract body contours and organ boundaries, thereby providing high-fidelity spatial geometry for 3D finite element modeling; (2) a surface electrode attachment module, which enables flexible and accurate placement of electrodes on irregular body surfaces, supporting diverse configurations and ensuring precise definition of the electrode-tissue interface; and (3) a tissue property assignment module, which establishes frequency-dependent conductivity models for multiple organs, enabling physiologically realistic conductivity values across tissues. Main results and Significance. By bridging the gap between CT imaging and EIT, StructEIT facilitates flexible, realistic, and scalable generation of high-resolution EIT datasets. Using this this framework, we constructed Chest-EIT, a thoracic EIT simulation dataset comprising over 1,400 publicly available CT cases, with multiple electrode configurations provided for each case.</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction",\n      "deep learning boundary representation generation",\n      "point cloud to B-Rep deep learning"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2021",\n    "used_override_query": false,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2021",\n      "direct B-Rep generation from 3D scans deep learning",\n      "neural implicit representation for B-Rep faces and edges"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_lwmzFo63M5fXZdNLdLBf66aY' is_error=False
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
      "query": "point cloud to B-Rep reconstruction neural network 2021",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "direct B-Rep generation from 3D scans deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "neural implicit representation for B-Rep faces and edges",
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
      "title": "SolidGen: An Autoregressive Model for Direct B-rep Synthesis",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-03-26T00:00:45Z",
      "url": "http://arxiv.org/abs/2203.13944v2",
      "doi": "",
      "authors": [
        "Pradeep Kumar Jayaraman",
        "Joseph G. Lambourne",
        "Nishkrit Desai",
        "Karl D. D. Willis",
        "Aditya Sanghi",
        "Nigel J. W. Morris"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The Boundary representation (B-rep) format is the de-facto shape representation in computer-aided design (CAD) to model solid and sheet objects. Recent approaches to generating CAD models have focused on learning sketch-and-extrude modeling sequences that are executed by a solid modeling kernel in postprocess to recover a B-rep. In this paper we present a new approach that enables learning from and synthesizing B-reps without the need for supervision through CAD modeling sequence data. Our method SolidGen, is an autoregressive neural network that models the B-rep directly by predicting the vertices, edges, and faces using Transformer-based and pointer neural networks. Key to achieving this is our Indexed Boundary Representation that references B-rep vertices, edges and faces in a well-defined hierarchy to capture the geometric and topological relations suitable for use with machine learning. SolidGen can be easily conditioned on contexts e.g., class labels, images, and voxels thanks to its probabilistic modeling of the B-rep distribution. We demonstrate qualitatively, quantitatively, and through perceptual evaluation by human subjects that SolidGen can produce high quality, realistic CAD models."
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
      "title": "Implicit Conversion of Manifold B-Rep Solids by Neural Halfspace Representation",
      "source": "arXiv",
      "year": 2022,
      "date": "2022-09-21T08:43:06Z",
      "url": "http://arxiv.org/abs/2209.10191v1",
      "doi": "",
      "authors": [
        "Hao-Xiang Guo",
        "Yang Liu",
        "Hao Pan",
        "Baining Guo"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "We present a novel implicit representation -- neural halfspace representation (NH-Rep), to convert manifold B-Rep solids to implicit representations. NH-Rep is a Boolean tree built on a set of implicit functions represented by the neural network, and the composite Boolean function is capable of representing solid geometry while preserving sharp features. We propose an efficient algorithm to extract the Boolean tree from a manifold B-Rep solid and devise a neural network-based optimization approach to compute the implicit functions. We demonstrate the high quality offered by our conversion algorithm on ten thousand manifold B-Rep CAD models that contain various curved patches including NURBS, and the superiority of our learning approach over other representative implicit conversion algorithms in terms of surface reconstruction, sharp feature preservation, signed distance field approximation, and robustness to various surface geometry, as well as a set of applications supported by NH-Rep."
      ]
    },
    {
      "title": "FINER++: Building a Family of Variable-periodic Functions for Activating Implicit Neural Representation",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-07-28T09:24:57Z",
      "url": "http://arxiv.org/abs/2407.19434v1",
      "doi": "",
      "authors": [
        "Hao Zhu",
        "Zhen Liu",
        "Qi Zhang",
        "Jingde Fu",
        "Weibing Deng",
        "Zhan Ma",
        "Yanwen Guo",
        "Xun Cao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Implicit Neural Representation (INR), which utilizes a neural network to map coordinate inputs to corresponding attributes, is causing a revolution in the field of signal processing. However, current INR techniques suffer from the \"frequency\"-specified spectral bias and capacity-convergence gap, resulting in imperfect performance when representing complex signals with multiple \"frequencies\". We have identified that both of these two characteristics could be handled by increasing the utilization of definition domain in current activation functions, for which we propose the FINER++ framework by extending existing periodic/non-periodic activation functions to variable-periodic ones. By initializing the bias of the neural network with different ranges, sub-functions with various frequencies in the variable-periodic function are selected for activation. Consequently, the supported frequency set can be flexibly tuned, leading to improved performance in signal representation. We demonstrate the generalization and capabilities of FINER++ with different activation function backbones (Sine, Gauss. and Wavelet) and various tasks (2D image fitting, 3D signed distance field representation, 5D neural radiance fields optimization and streamable INR transmission), and we show that it improves existing INRs. Project page: {https://liuzhen0212.github.io/finerpp/}"
      ]
    },
    {
      "title": "Pointer-CAD: Unifying B-Rep and Command Sequences via Pointer-based Edges & Faces Selection",
      "source": "arXiv",
      "year": 2026,
      "date": "2026-03-04T17:55:01Z",
      "url": "http://arxiv.org/abs/2603.04337v1",
      "doi": "",
      "authors": [
        "Dacheng Qi",
        "Chenyu Wang",
        "Jingwei Xu",
        "Tianzhe Chu",
        "Zibo Zhao",
        "Wen Liu",
        "Wenrui Ding",
        "Yi Ma"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Constructing computer-aided design (CAD) models is labor-intensive but essential for engineering and manufacturing. Recent advances in Large Language Models (LLMs) have inspired the LLM-based CAD generation by representing CAD as command sequences. But these methods struggle in practical scenarios because command sequence representation does not support entity selection (e.g. faces or edges), limiting its ability to support complex editing operations such as chamfer or fillet. Further, the discretization of a continuous variable during sketch and extrude operations may result in topological errors. To address these limitations, we present Pointer-CAD, a novel LLM-based CAD generation framework that leverages a pointer-based command sequence representation to explicitly incorporate the geometric information of B-rep models into sequential modeling. In particular, Pointer-CAD decomposes CAD model generation into steps, conditioning the generation of each subsequent step on both the textual description and the B-rep generated from previous steps. Whenever an operation requires the selection of a specific geometric entity, the LLM predicts a Pointer that selects the most feature-consistent candidate from the available set. Such a selection operation also reduces the quantization error in the command sequence-based representation. To support the training of Pointer-CAD, we develop a data annotation pipeline that produces expert-level natural language descriptions and apply it to build a dataset of approximately 575K CAD models. Extensive experimental results demonstrate that Pointer-CAD effectively supports the generation of complex geometric structures and reduces segmentation error to an extremely low level, achieving a significant improvement over prior command sequence methods, thereby significantly mitigating the topological inaccuracies introduced by quantization error."
      ]
    },
    {
      "title": "Fault Representation in Structural Modelling with Implicit Neural Representations",
      "source": "Crossref / Crossref",
      "year": 2024,
      "date": "2024-10-31",
      "url": "https://doi.org/10.31223/x5bq48",
      "doi": "10.31223/x5bq48",
      "authors": [
        "Kaifeng Gao",
        "Florian Wellmann"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>Implicit neural representations have been demonstrated to provide a flexible and scalable framework for computer graphics and three-dimensional modelling and, consequently, have found their way also into geological modelling. These networks are feature-based and resolution-independent, making them effective for modelling geological structures from scattered interface points, units, and structural orientations. Despite the promising characteristics of existing implicit neural representation approaches, modelling faults within implicit neural representations remains a significant challenge. In this work, we present a fault feature encoding approach to represent faults in implicit neural representations, where the discontinuous information is concatenated as additional features of observation points and query points for network input. We apply this methodology first to a synthetic model to evaluate its efficacy, and subsequently to a real-world dataset from a part of the Gullfaks field in the northern North Sea. The modelling results demonstrate the method’s capacity to generate a well-defined implicit scalar field while preserving sharp transitions at fault locations. Moreover, this work mentions the advantages of the presented approach over using Boolean operations and discontinuous activation functions. Furthermore, we discuss the potential opportunity to integrate prior domain knowledge and geophysics datasets into structural modelling by embedding them as model input features or incorporating them as constraints by loss functions.</jats:p>"
      ]
    },
    {
      "title": "Implicit Neural Representation for Physics-driven Actuated Soft Bodies",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-01-26T13:42:12Z",
      "url": "http://arxiv.org/abs/2401.14861v1",
      "doi": "",
      "authors": [
        "Lingchen Yang",
        "Byungsoo Kim",
        "Gaspard Zoss",
        "Baran Gözcü",
        "Markus Gross",
        "Barbara Solenthaler"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Active soft bodies can affect their shape through an internal actuation mechanism that induces a deformation. Similar to recent work, this paper utilizes a differentiable, quasi-static, and physics-based simulation layer to optimize for actuation signals parameterized by neural networks. Our key contribution is a general and implicit formulation to control active soft bodies by defining a function that enables a continuous mapping from a spatial point in the material space to the actuation value. This property allows us to capture the signal's dominant frequencies, making the method discretization agnostic and widely applicable. We extend our implicit model to mandible kinematics for the particular case of facial animation and show that we can reliably reproduce facial expressions captured with high-quality capture systems. We apply the method to volumetric soft bodies, human poses, and facial expressions, demonstrating artist-friendly properties, such as simple control over the latent space and resolution invariance at test time."
      ]
    },
    {
      "title": "StructEIT: Realistic 3D EIT model generation from CT scans for deep learning applications",
      "source": "Crossref / Physiological Measurement",
      "year": 2026,
      "date": "2026-3-20",
      "url": "https://doi.org/10.1088/1361-6579/ae5587",
      "doi": "10.1088/1361-6579/ae5587",
      "authors": [
        "Zeyi Jiang",
        "Sirui Qiao",
        "Chuanbao Wu",
        "Hui Qin",
        "Yixin Ma"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:title>Abstract</jats:title> <jats:p>Objective. Artificial intelligence (AI) has significantly improved image reconstruction quality across various medical imaging modalities. However, its application in electrical impedance tomography (EIT) reconstruction remains limited, mainly due to the absence of comprehensive in vivo datasets that incorporate realistic anatomical geometries and conductivity distributions. This limitation constrains the development of supervised and data-driven reconstruction methods. Approach. To address this bottleneck, we developed StructEIT, an integrated EIT modeling framework for generating anatomically and biophysically realistic EIT simulation models. The framework incorporates three key components: (1) a structure extraction module, which automatically processes human CT scans to extract body contours and organ boundaries, thereby providing high-fidelity spatial geometry for 3D finite element modeling; (2) a surface electrode attachment module, which enables flexible and accurate placement of electrodes on irregular body surfaces, supporting diverse configurations and ensuring precise definition of the electrode-tissue interface; and (3) a tissue property assignment module, which establishes frequency-dependent conductivity models for multiple organs, enabling physiologically realistic conductivity values across tissues. Main results and Significance. By bridging the gap between CT imaging and EIT, StructEIT facilitates flexible, realistic, and scalable generation of high-resolution EIT datasets. Using this this framework, we constructed Chest-EIT, a thoracic EIT simulation dataset comprising over 1,400 publicly available CT cases, with multiple electrode configurations provided for each case.</jats:p>"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."
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
      "point cloud to B-Rep deep learning"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2021",
    "used_override_query": false,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2021",
      "direct B-Rep generation from 3D scans deep learning",
      "neural implicit representation for B-Rep faces and edges"
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
  "review_summary": "The retrieval output contains several relevant papers on direct B-Rep generation, but critical gaps exist. The set lacks sufficient evidence of point cloud or 3D scan as the primary input, which is a core user requirement. Several papers appear to focus on generation from other modalities (e.g., text, images) or conversion from B-Rep to implicit representations, not the reverse. The evidence snippets are insufficient to confirm strict exclusion of CAD operation sequences for all candidates. Source coverage is adequate, but the relevance and query fit are not satisfactorily met.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 2-3 are clearly aligned with the user's topic of direct B-Rep generation from point clouds/3D scans. Many papers (e.g., FINER++, Fault Representation, Implicit Neural Representation for Physics-driven Actuated Soft Bodies, StructEIT) are about implicit representations or other applications, not direct B-Rep output from point clouds. The evidence snippets do not strongly confirm the required input-output mapping."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly required methods where the primary input is unstructured point clouds or 3D scans, with multimodal inputs only as a secondary priority for breakthroughs. The retrieved set includes papers that generate B-Reps from images, text, or latent spaces without clear evidence of point cloud input. The strict exclusions (CAD operation sequences, CSG trees) are not verifiably avoided for all papers based on the provided evidence snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be confidently identified as core candidates for direct B-Rep generation from point clouds after inspecting titles and evidence. Papers like SolidGen, HoLa, and AutoBrep are promising but their evidence snippets do not explicitly mention point cloud input. Others are off-topic (implicit representation papers)."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: neural methods that take point clouds as input and output B-Reps. The retrieval seems to have captured B-Rep generation papers but not specifically those focused on point cloud input, which is the user's highest priority."
    }
  },
  "key_risks": [
    "The evidence snippets are from abstracts and may not confirm the critical input (point clouds) or the strict exclusion of operation sequences.",
    "Several papers appear to be about implicit neural representations (INR) in general, not B-Rep generation, indicating potential retrieval drift.",
    "The set may mislead the final report by including adjacent work that does not meet the user's strict criteria."
  ],
  "next_actions": [
    "Execute a new query explicitly targeting 'point cloud to B-Rep neural network 2023 2024 2025' to prioritize the required input modality.",
    "Search for known seminal papers in this niche (e.g., 'Point2Cyl', 'BRepNet', 'DeepCAD' but exclude if operation sequence) using specific titles/DOIs to ensure coverage.",
    "Review the abstracts or full texts of the promising candidates (SolidGen, HoLa, AutoBrep, BrepARG) to confirm point cloud input capability and absence of operation sequence output. If evidence is lacking, seek alternative papers."
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
  "user_intent": "Find 8-10 state-of-the-art papers (2021-2026) that directly output B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans, using modern neural architectures, while strictly excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "direct neural generation of B-Rep topology and geometry from point clouds",
    "latent space representations for B-Reps",
    "end-to-end learning from unstructured 3D scans to B-Reps",
    "variational and autoregressive models for B-Rep generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "step-by-step modeling history output",
    "implicit neural representations for non-B-Rep tasks"
  ],
  "fallback_queries": [
    "neural network B-Rep reconstruction from scans",
    "deep learning boundary representation generation point cloud",
    "3D scan to CAD B-Rep deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep neural network 2023",
      "reason": "Directly targets the core input modality (point cloud) and the output (B-Rep) within a recent year to capture state-of-the-art."
    },
    {
      "query": "B-Rep generation from 3D scans transformer",
      "reason": "Focuses on modern neural architectures (transformer) for the specific task, emphasizing scan input."
    },
    {
      "query": "SolidGen HoLa AutoBrep point cloud input",
      "reason": "Targets known promising papers from the previous retrieval to verify their input modality and ensure they meet the strict criteria."
    }
  ],
  "assumptions": [
    "The user's highest priority is point cloud or 3D scan input. Papers using only images, text, or latent codes as input are secondary and should only be included if they represent a major breakthrough in B-Rep generation.",
    "The previous retrieval captured relevant B-Rep generation papers, but their abstracts did not explicitly confirm point cloud input. This revised plan seeks to verify that or find alternatives.",
    "If fewer than 8-10 papers perfectly match the strict criteria, the final report will note the scarcity and focus on the most relevant ones.",
    "The time range remains inclusive of 2021-2026."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must explicitly mention point clouds or 3D scans as a primary or supported input modality.",
    "Papers must employ modern neural architectures (e.g., transformers, graph networks, diffusion models).",
    "No included paper should focus on reconstructing CAD modeling sequences, CSG trees, or program synthesis."
  ]
}
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a revised search plan focusing specifically on point cloud to B-Rep neural networks to better match the user's requirements.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_UDbNOv8i0JXc7VBvFmB00Tx0', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-Rep neural network 2023"}', name='retrieve_candidates_from_plan')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep neural network 2023",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep generation from 3D scans transformer",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "SolidGen HoLa AutoBrep point cloud input",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-11-27T07:16:53Z",\n      "url": "http://arxiv.org/abs/2511.22171v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Weize Quan",\n        "Biao Zhang",\n        "Peter Wonka",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) is the de facto standard for CAD model representation in modern industrial design. The intricate coupling between geometric and topological elements in B-rep structures has forced existing generative methods to rely on cascaded multi-stage networks, resulting in error accumulation and computational inefficiency. We present BrepGPT, a single-stage autoregressive framework for B-rep generation. Our key innovation lies in the Voronoi Half-Patch (VHP) representation, which decomposes B-reps into unified local units by assigning geometry to nearest half-edges and sampling their next pointers. Unlike hierarchical representations that require multiple distinct encodings for different structural levels, our VHP representation facilitates unifying geometric attributes and topological relations in a single, coherent format. We further leverage dual VQ-VAEs to encode both vertex topology and Voronoi Half-Patches into vertex-based tokens, achieving a more compact sequential encoding. A decoder-only Transformer is then trained to autoregressively predict these tokens, which are subsequently mapped to vertex-based features and decoded into complete B-rep models. Experiments demonstrate that BrepGPT achieves state-of-the-art performance in unconditional B-rep generation. The framework also exhibits versatility in various applications, including conditional generation from category labels, point clouds, text descriptions, and images, as well as B-rep autocompletion and interpolation."\n      ]\n    },\n    {\n      "title": "BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-01-28T04:07:59Z",\n      "url": "http://arxiv.org/abs/2401.15563v3",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Joseph G. Lambourne",\n        "Pradeep Kumar Jayaraman",\n        "Zhengqing Wang",\n        "Karl D. D. Willis",\n        "Yasutaka Furukawa"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper presents BrepGen, a diffusion-based generative approach that directly outputs a Boundary representation (B-rep) Computer-Aided Design (CAD) model. BrepGen represents a B-rep model as a novel structured latent geometry in a hierarchical tree. With the root node representing a whole CAD solid, each element of a B-rep model (i.e., a face, an edge, or a vertex) progressively turns into a child-node from top to bottom. B-rep geometry information goes into the nodes as the global bounding box of each primitive along with a latent code describing the local geometric shape. The B-rep topology information is implicitly represented by node duplication. When two faces share an edge, the edge curve will appear twice in the tree, and a T-junction vertex with three incident edges appears six times in the tree with identical node features. Starting from the root and progressing to the leaf, BrepGen employs Transformer-based diffusion models to sequentially denoise node features while duplicated nodes are detected and merged, recovering the B-Rep topology information. Extensive experiments show that BrepGen advances the task of CAD B-rep generation, surpassing existing methods on various benchmarks. Results on our newly collected furniture dataset further showcase its exceptional capability in generating complicated geometry. While previous methods were limited to generating simple prismatic shapes, BrepGen incorporates free-form and doubly-curved surfaces for the first time. Additional applications of BrepGen include CAD autocomplete and design interpolation. The code, pretrained models, and dataset are available at https://github.com/samxuxiang/BrepGen."\n      ]\n    },\n    {\n      "title": "DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-17T12:34:14Z",\n      "url": "http://arxiv.org/abs/2503.13110v1",\n      "doi": "",\n      "authors": [\n        "Jing Li",\n        "Yihang Fu",\n        "Falai Chen"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Boundary representation (B-rep) of geometric models is a fundamental format in Computer-Aided Design (CAD). However, automatically generating valid and high-quality B-rep models remains challenging due to the complex interdependence between the topology and geometry of the models. Existing methods tend to prioritize geometric representation while giving insufficient attention to topological constraints, making it difficult to maintain structural validity and geometric accuracy. In this paper, we propose DTGBrepGen, a novel topology-geometry decoupled framework for B-rep generation that explicitly addresses both aspects. Our approach first generates valid topological structures through a two-stage process that independently models edge-face and edge-vertex adjacency relationships. Subsequently, we employ Transformer-based diffusion models for sequential geometry generation, progressively generating vertex coordinates, followed by edge geometries and face geometries which are represented as B-splines. Extensive experiments on diverse CAD datasets show that DTGBrepGen significantly outperforms existing methods in both topological validity and geometric accuracy, achieving higher validity rates and producing more diverse and realistic B-reps. Our code is publicly available at https://github.com/jinli99/DTGBrepGen."\n      ]\n    },\n    {\n      "title": "AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-12-02T18:46:25Z",\n      "url": "http://arxiv.org/abs/2512.03018v1",\n      "doi": "",\n      "authors": [\n        "Xiang Xu",\n        "Pradeep Kumar Jayaraman",\n        "Joseph G. Lambourne",\n        "Yilin Liu",\n        "Durvesh Malpure",\n        "Pete Meltzer"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The boundary representation (B-Rep) is the standard data structure used in Computer-Aided Design (CAD) for defining solid models. Despite recent progress, directly generating B-Reps end-to-end with precise geometry and watertight topology remains a challenge. This paper presents AutoBrep, a novel Transformer model that autoregressively generates B-Reps with high quality and validity. AutoBrep employs a unified tokenization scheme that encodes both geometric and topological characteristics of a B-Rep model as a sequence of discrete tokens. Geometric primitives (i.e., surfaces and curves) are encoded as latent geometry tokens, and their structural relationships are defined as special topological reference tokens. Sequence order in AutoBrep naturally follows a breadth first traversal of the B-Rep face adjacency graph. At inference time, neighboring faces and edges along with their topological structure are progressively generated. Extensive experiments demonstrate the advantages of our unified representation when coupled with next-token prediction for B-Rep generation. AutoBrep outperforms baselines with better quality and watertightness. It is also highly scalable to complex solids with good fidelity and inference speed. We further show that autocompleting B-Reps is natively supported through our unified tokenization, enabling user-controllable CAD generation with minimal changes. Code is available at https://github.com/AutodeskAILab/AutoBrep."\n      ]\n    },\n    {\n      "title": "HoLa: B-Rep Generation using a Holistic Latent Representation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-19T10:34:24Z",\n      "url": "http://arxiv.org/abs/2504.14257v3",\n      "doi": "",\n      "authors": [\n        "Yilin Liu",\n        "Duoteng Xu",\n        "Xingyao Yu",\n        "Xiang Xu",\n        "Daniel Cohen-Or",\n        "Hao Zhang",\n        "Hui Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "We introduce a novel representation for learning and generating Computer-Aided Design (CAD) models in the form of $\\\\textit{boundary representations}$ (B-Reps). Our representation unifies the continuous geometric properties of B-Rep primitives in different orders (e.g., surfaces and curves) and their discrete topological relations in a $\\\\textit{holistic latent}$ (HoLa) space. This is based on the simple observation that the topological connection between two surfaces is intrinsically tied to the geometry of their intersecting curve. Such a prior allows us to reformulate topology learning in B-Reps as a geometric reconstruction problem in Euclidean space. Specifically, we eliminate the presence of curves, vertices, and all the topological connections in the latent space by learning to distinguish and derive curve geometries from a pair of surface primitives via a neural intersection network. To this end, our holistic latent space is only defined on surfaces but encodes a full B-Rep model, including the geometry of surfaces, curves, vertices, and their topological relations. Our compact and holistic latent space facilitates the design of a first diffusion-based generator to take on a large variety of inputs including point clouds, single/multi-view images, 2D sketches, and text prompts. Our method significantly reduces ambiguities, redundancies, and incoherences among the generated B-Rep primitives, as well as training complexities inherent in prior multi-step B-Rep learning pipelines, while achieving greatly improved validity rate over current state of the art: 82% vs. $\\\\approx$50%."\n      ]\n    },\n    {\n      "title": "AutoRegressive Generation with B-rep Holistic Token Sequence Representation",\n      "source": "arXiv",\n      "year": 2026,\n      "date": "2026-01-23T14:15:02Z",\n      "url": "http://arxiv.org/abs/2601.16771v1",\n      "doi": "",\n      "authors": [\n        "Jiahao Li",\n        "Yunpeng Bai",\n        "Yongkang Dai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Previous representation and generation approaches for the B-rep relied on graph-based representations that disentangle geometric and topological features through decoupled computational pipelines, thereby precluding the application of sequence-based generative frameworks, such as transformer architectures that have demonstrated remarkable performance. In this paper, we propose BrepARG, the first attempt to encode B-rep\'s geometry and topology into a holistic token sequence representation, enabling sequence-based B-rep generation with an autoregressive architecture. Specifically, BrepARG encodes B-rep into 3 types of tokens: geometry and position tokens representing geometric features, and face index tokens representing topology. Then the holistic token sequence is constructed hierarchically, starting with constructing the geometry blocks (i.e., faces and edges) using the above tokens, followed by geometry block sequencing. Finally, we assemble the holistic sequence representation for the entire B-rep. We also construct a transformer-based autoregressive model that learns the distribution over holistic token sequences via next-token prediction, using a multi-layer decoder-only architecture with causal masking. Experiments demonstrate that BrepARG achieves state-of-the-art (SOTA) performance. BrepARG validates the feasibility of representing B-rep as holistic token sequences, opening new directions for B-rep generation."\n      ]\n    },\n    {\n      "title": "GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-07-07T08:43:46Z",\n      "url": "http://arxiv.org/abs/2507.04765v1",\n      "doi": "",\n      "authors": [\n        "Weilin Lai",\n        "Tie Xu",\n        "Hu Wang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Direct B-Rep generation is increasingly important in CAD workflows, eliminating costly modeling sequence data and supporting complex features. A key challenge is modeling joint distribution of the misaligned geometry and topology. Existing methods tend to implicitly embed topology into the geometric features of edges. Although this integration ensures feature alignment, it also causes edge geometry to carry more redundant structural information compared to the original B-Rep, leading to significantly higher computational cost. To reduce redundancy, we propose GraphBrep, a B-Rep generation model that explicitly represents and learns compact topology. Following the original structure of B-Rep, we construct an undirected weighted graph to represent surface topology. A graph diffusion model is employed to learn topology conditioned on surface features, serving as the basis for determining connectivity between primitive surfaces. The explicit representation ensures a compact data structure, effectively reducing computational cost during both training and inference. Experiments on two large-scale unconditional datasets and one category-conditional dataset demonstrate the proposed method significantly reduces training and inference times (up to 31.3% and 56.3% for given datasets, respectively) while maintaining high-quality CAD generation compared with SOTA."\n      ]\n    },\n    {\n      "title": "Hunyuan3D-Omni: A Unified Framework for Controllable Generation of 3D Assets",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-09-25T14:39:17Z",\n      "url": "http://arxiv.org/abs/2509.21245v1",\n      "doi": "",\n      "authors": [\n        "Team Hunyuan3D",\n        ":",\n        "Bowen Zhang",\n        "Chunchao Guo",\n        "Haolin Liu",\n        "Hongyu Yan",\n        "Huiwen Shi",\n        "Jingwei Huang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent advances in 3D-native generative models have accelerated asset creation for games, film, and design. However, most methods still rely primarily on image or text conditioning and lack fine-grained, cross-modal controls, which limits controllability and practical adoption. To address this gap, we present Hunyuan3D-Omni, a unified framework for fine-grained, controllable 3D asset generation built on Hunyuan3D 2.1. In addition to images, Hunyuan3D-Omni accepts point clouds, voxels, bounding boxes, and skeletal pose priors as conditioning signals, enabling precise control over geometry, topology, and pose. Instead of separate heads for each modality, our model unifies all signals in a single cross-modal architecture. We train with a progressive, difficulty-aware sampling strategy that selects one control modality per example and biases sampling toward harder signals (e.g., skeletal pose) while downweighting easier ones (e.g., point clouds), encouraging robust multi-modal fusion and graceful handling of missing inputs. Experiments show that these additional controls improve generation accuracy, enable geometry-aware transformations, and increase robustness for production workflows."\n      ]\n    },\n    {\n      "title": "BRepFormer: Transformer-Based B-rep Geometric Feature Recognition",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-04-10T01:36:06Z",\n      "url": "http://arxiv.org/abs/2504.07378v3",\n      "doi": "",\n      "authors": [\n        "Yongkang Dai",\n        "Xiaoshui Huang",\n        "Yunpeng Bai",\n        "Hao Guo",\n        "Hongping Gan",\n        "Ling Yang",\n        "Yilei Shi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recognizing geometric features on B-rep models is a cornerstone technique for multimedia content-based retrieval and has been widely applied in intelligent manufacturing. However, previous research often merely focused on Machining Feature Recognition (MFR), falling short in effectively capturing the intricate topological and geometric characteristics of complex geometry features. In this paper, we propose BRepFormer, a novel transformer-based model to recognize both machining feature and complex CAD models\' features. BRepFormer encodes and fuses the geometric and topological features of the models. Afterwards, BRepFormer utilizes a transformer architecture for feature propagation and a recognition head to identify geometry features. During each iteration of the transformer, we incorporate a bias that combines edge features and topology features to reinforce geometric constraints on each face. In addition, we also proposed a dataset named Complex B-rep Feature Dataset (CBF), comprising 20,000 B-rep models. By covering more complex B-rep models, it is better aligned with industrial applications. The experimental results demonstrate that BRepFormer achieves state-of-the-art accuracy on the MFInstSeg, MFTRCAD, and our CBF datasets."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "neural network B-Rep reconstruction from scans",\n      "deep learning boundary representation generation point cloud",\n      "3D scan to CAD B-Rep deep learning"\n    ],\n    "effective_query": "point cloud to B-Rep neural network 2023",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep neural network 2023",\n      "B-Rep generation from 3D scans transformer",\n      "SolidGen HoLa AutoBrep point cloud input"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_UDbNOv8i0JXc7VBvFmB00Tx0' is_error=False
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
      "query": "point cloud to B-Rep neural network 2023",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep generation from 3D scans transformer",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "SolidGen HoLa AutoBrep point cloud input",
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
      "title": "Hunyuan3D-Omni: A Unified Framework for Controllable Generation of 3D Assets",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-09-25T14:39:17Z",
      "url": "http://arxiv.org/abs/2509.21245v1",
      "doi": "",
      "authors": [
        "Team Hunyuan3D",
        ":",
        "Bowen Zhang",
        "Chunchao Guo",
        "Haolin Liu",
        "Hongyu Yan",
        "Huiwen Shi",
        "Jingwei Huang"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent advances in 3D-native generative models have accelerated asset creation for games, film, and design. However, most methods still rely primarily on image or text conditioning and lack fine-grained, cross-modal controls, which limits controllability and practical adoption. To address this gap, we present Hunyuan3D-Omni, a unified framework for fine-grained, controllable 3D asset generation built on Hunyuan3D 2.1. In addition to images, Hunyuan3D-Omni accepts point clouds, voxels, bounding boxes, and skeletal pose priors as conditioning signals, enabling precise control over geometry, topology, and pose. Instead of separate heads for each modality, our model unifies all signals in a single cross-modal architecture. We train with a progressive, difficulty-aware sampling strategy that selects one control modality per example and biases sampling toward harder signals (e.g., skeletal pose) while downweighting easier ones (e.g., point clouds), encouraging robust multi-modal fusion and graceful handling of missing inputs. Experiments show that these additional controls improve generation accuracy, enable geometry-aware transformations, and increase robustness for production workflows."
      ]
    },
    {
      "title": "BRepFormer: Transformer-Based B-rep Geometric Feature Recognition",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-04-10T01:36:06Z",
      "url": "http://arxiv.org/abs/2504.07378v3",
      "doi": "",
      "authors": [
        "Yongkang Dai",
        "Xiaoshui Huang",
        "Yunpeng Bai",
        "Hao Guo",
        "Hongping Gan",
        "Ling Yang",
        "Yilei Shi"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recognizing geometric features on B-rep models is a cornerstone technique for multimedia content-based retrieval and has been widely applied in intelligent manufacturing. However, previous research often merely focused on Machining Feature Recognition (MFR), falling short in effectively capturing the intricate topological and geometric characteristics of complex geometry features. In this paper, we propose BRepFormer, a novel transformer-based model to recognize both machining feature and complex CAD models' features. BRepFormer encodes and fuses the geometric and topological features of the models. Afterwards, BRepFormer utilizes a transformer architecture for feature propagation and a recognition head to identify geometry features. During each iteration of the transformer, we incorporate a bias that combines edge features and topology features to reinforce geometric constraints on each face. In addition, we also proposed a dataset named Complex B-rep Feature Dataset (CBF), comprising 20,000 B-rep models. By covering more complex B-rep models, it is better aligned with industrial applications. The experimental results demonstrate that BRepFormer achieves state-of-the-art accuracy on the MFInstSeg, MFTRCAD, and our CBF datasets."
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 12 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "neural network B-Rep reconstruction from scans",
      "deep learning boundary representation generation point cloud",
      "3D scan to CAD B-Rep deep learning"
    ],
    "effective_query": "point cloud to B-Rep neural network 2023",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep neural network 2023",
      "B-Rep generation from 3D scans transformer",
      "SolidGen HoLa AutoBrep point cloud input"
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
  "review_summary": "The retrieval output shows improved focus on B-Rep generation with modern neural architectures, but the critical requirement of point cloud or 3D scan as the primary input is still not reliably met. While some papers (e.g., HoLa, BrepGPT) mention point clouds as one of many conditional inputs, the evidence does not establish it as the primary focus. Several papers appear to be about unconditional generation or other tasks (e.g., feature recognition, 3D asset generation). The set lacks clear evidence that the methods are designed for reconstruction from unstructured point clouds, which is the user's highest priority. The exclusion of CAD operation sequences is also not verifiable from the abstracts alone.",
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
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Only 2-3 papers (HoLa, BrepGPT) mention point clouds as a possible input, but the evidence snippets do not confirm that point cloud to B-Rep is the primary task. Others are about unconditional generation (BrepGen, DTGBrepGen, AutoBrep, GraphBrep), feature recognition (BRepFormer), or general 3D asset generation (Hunyuan3D-Omni, Neural Point Cloud Diffusion) without clear B-Rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly required methods where the primary input is unstructured point clouds or 3D scans. The retrieved set includes many papers that do not mention point cloud input at all or treat it as one of many conditional inputs. The strict exclusions (CAD operation sequences) are not verifiably avoided based on the provided evidence snippets."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be confidently identified as core candidates for direct B-Rep generation from point clouds. Papers like BrepGen, DTGBrepGen, AutoBrep, GraphBrep appear to be unconditional or multi-modal generators. BRepFormer is a recognition model, not a generator. The evidence is insufficient to confirm core fit."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: neural methods specifically designed for reconstructing B-Reps from point clouds or 3D scans. The retrieval has drifted towards general B-Rep generation and other tasks."
    }
  },
  "key_risks": [
    "The evidence snippets are from abstracts and may not confirm the primary input modality or the strict exclusion of operation sequences.",
    "Many papers appear to be about unconditional B-Rep generation or generation from other modalities, not reconstruction from point clouds.",
    "Including papers like BRepFormer (feature recognition) and Hunyuan3D-Omni (general 3D asset generation) could mislead the final report."
  ],
  "next_actions": [
    "Execute a targeted query for 'point cloud to B-Rep reconstruction neural network 2024' to specifically seek reconstruction papers, not just generation.",
    "Search for known papers that explicitly tackle 'B-Rep reconstruction from point clouds' using specific phrases, possibly including 'BRepNet' or 'Point2Cyl' (though check year and exclusion criteria).",
    "For the most promising candidates (HoLa, BrepGPT), retrieve full abstracts or introduction snippets to confirm point cloud input capability and absence of operation sequence output. If evidence is lacking, exclude them."
  ]
}
```

### Message 14

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=3D Boundary Representation (B-Rep) reconstruction from point clouds using neural networks, queries=3, years=2021-2026

```text
{
  "topic": "3D Boundary Representation (B-Rep) reconstruction from point clouds using neural networks",
  "user_intent": "Find state-of-the-art papers (2021-2026) that directly reconstruct B-Rep data structures (faces, edges, vertices, topology) from unstructured point clouds or 3D scans using modern neural architectures, excluding methods that output CAD operation sequences, CSG trees, or program synthesis.",
  "time_range": {
    "start_year": 2021,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "published between 2021-2026",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "explicit years"
  },
  "focus_areas": [
    "neural reconstruction of B-Rep topology and geometry from point clouds",
    "direct mapping from 3D scans to B-Rep structures",
    "end-to-end learning for B-Rep reconstruction",
    "handling unstructured point cloud input"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch-and-extrude history modeling",
    "Constructive Solid Geometry (CSG) trees",
    "CAD program synthesis",
    "unconditional B-Rep generation",
    "B-Rep feature recognition",
    "general 3D asset generation"
  ],
  "fallback_queries": [
    "B-Rep reconstruction from point cloud deep learning",
    "neural network for B-Rep from 3D scan",
    "point cloud to CAD B-Rep reconstruction"
  ],
  "queries": [
    {
      "query": "point cloud to B-Rep reconstruction neural network 2024",
      "reason": "Directly targets the reconstruction task from point clouds in a recent year, emphasizing the input-output mapping."
    },
    {
      "query": "B-Rep reconstruction from 3D scans deep learning",
      "reason": "Focuses on scan input and reconstruction, not unconditional generation."
    },
    {
      "query": "BRepNet point cloud reconstruction",
      "reason": "Targets a known seminal paper (BRepNet) that may address B-Rep reconstruction, verifying its input modality and year."
    }
  ],
  "assumptions": [
    "The user's primary focus is reconstruction from point clouds, not unconditional generation or generation from other modalities.",
    "If a paper's primary contribution is unconditional B-Rep generation but it also supports point cloud conditioning, it may be included only if point cloud input is a significant demonstrated application.",
    "The previous retrievals have yielded many B-Rep generation papers; this plan explicitly seeks reconstruction papers to fill the gap.",
    "The time range remains inclusive of 2021-2026."
  ],
  "success_criteria": [
    "Retrieved papers must have the primary output be a B-Rep data structure.",
    "Papers must explicitly focus on reconstructing B-Reps from point clouds or 3D scans as a core task.",
    "Papers must employ modern neural architectures.",
    "No included paper should focus on reconstructing CAD modeling sequences, CSG trees, or program synthesis."
  ]
}
```

### Message 15

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`
- Summary: Agent thought/reasoning event

```text
I'll execute a more targeted search focusing specifically on point cloud to B-Rep reconstruction to better match the user's requirements.
```

### Message 16

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_HBxMwhjDTfeFpDIaoc1bHEE0', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-Rep reconstruction neural network 2024"}', name='retrieve_candidates_from_plan')
```

### Message 17

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-Rep reconstruction neural network 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "B-Rep reconstruction from 3D scans deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "BRepNet point cloud reconstruction",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "BRep Boundary and Junction Detection for CAD Reverse Engineering",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-04-13",\n      "url": "https://doi.org/10.1109/icmi60790.2024.10585950",\n      "doi": "10.1109/icmi60790.2024.10585950",\n      "authors": [\n        "Sk Aziz Ali",\n        "Mohammad Sadil Khan",\n        "Didier Stricker"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "In machining process, 3D reverse engineering of mechanical system is an integral, highly important, and yet time consuming step to obtain parametric CAD models from 3D scans. Therefore, deep learning-based Scan-to-CAD modeling can offer designers enormous editability to quickly modify CAD model, being able to parse all its structural compositions and design steps. In this paper, we propose a supervised boundary representation (BRep) detection network BRepDetNet from 3D scans of CC3D and ABC dataset. We have carefully annotated the ~50K and ~45K scans of both the datasets with appropriate topological relations (e.g., next, mate, previous) between the geometrical primitives (i.e., boundaries, junctions, loops, faces) of their BRep data structures. The proposed solution decomposes the Scan-to-CAD problem in Scan-to-BRep ensuring the right step towards feature-based modeling, and therefore, leveraging other existing BRep-to-CAD modeling methods. Our proposed Scan-to-BRep neural network learns to detect BRep boundaries and junctions by minimizing focal-loss and non-maximal sup-pression (NMS) during training time. Experimental results show that our BRepDetNet with NMS-Loss achieves impressive results."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-11-07",\n      "url": "http://arxiv.org/abs/2411.04954",\n      "doi": "10.48550/arxiv.2411.04954",\n      "authors": [\n        "Jiasheng Xu",\n        "Chenyu Wang",\n        "Zheng Zhao",\n        "Wenyu Liu",\n        "Yi Ma",\n        "S. M. Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "BRepGAT: Graph neural network to segment machining feature faces in a B-rep model",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-11-03",\n      "url": "https://doi.org/10.1093/jcde/qwad106",\n      "doi": "10.1093/jcde/qwad106",\n      "authors": [\n        "Jinwon Lee",\n        "Changmo Yeo",\n        "Sang-Uk Cheon",\n        "Jun Hwan Park",\n        "Duhwan Mun"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in decreased recognition accuracy. In this paper, we propose a novel deep learning model called the boundary representation graph attention network (BRepGAT) to segment faces in an original boundary representation (B-rep) model containing machining features. We define descriptors that represent information about the faces and edges of the B-rep model from the perspective of feature recognition. These descriptors are extracted from the B-rep model and transformed into homogeneous graph data, which are then passed to graph networks. BRepGAT recognizes machining features from the graph data input. Our experimental results using the MFCAD18++ dataset showed that BRepGAT achieved state-of-the-art recognition accuracy (99.1%). Furthermore, BRepGAT showed relatively robust performance on other datasets besides MFCAD18++."\n      ]\n    },\n    {\n      "title": "Extending Point-Based Deep Learning Approaches for Better Semantic Segmentation in CAD",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-10-10",\n      "url": "https://doi.org/10.1016/j.cad.2023.103629",\n      "doi": "10.1016/j.cad.2023.103629",\n      "authors": [\n        "Gerico Vidanes",\n        "David J. J. Toal",\n        "Xu Zhang",\n        "Andy J. Keane",\n        "Jon Gregory",\n        "Marco Nuñez"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Geometry understanding is a core concept of computer-aided design and engineering (CAD/CAE). Deep neural networks have increasingly shown success as a method of processing complex inputs to achieve abstract tasks. This work revisits a generic and relatively simple approach to 3D deep learning - a point-based graph neural network - and develops best-practices and modifications to alleviate traditional drawbacks. It is shown that these methods should not be discounted for CAD tasks; with proper implementation, they can be competitive with more specifically designed approaches. Through an additive study, this work investigates how the boundary representation data can be fully utilised by leveraging the flexibility of point-based graph networks. The final configuration significantly improves on the predictive accuracy of a standard PointNet++ network across multiple CAD model segmentation datasets and achieves state-of-the-art performance on the MFCAD++ machining features dataset. The proposed modifications leave the core neural network unchanged and results also suggest that they can be applied to other point-based approaches."\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    },\n    {\n      "title": "3d reconstruction of mine environment based on two-step point cloud alignment algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2026,\n      "date": "2026",\n      "url": "https://doi.org/10.2139/ssrn.6391565",\n      "doi": "10.2139/ssrn.6391565",\n      "authors": [\n        "Ying Zhou",\n        "Nan Zhou"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>A two-step point cloud registration algorithm based on improved sampling consistency and iterative nearest neighbors is proposed to meet the daily work needs of coal mine production robots and the rapid rescue needs of post disaster rescue robots. This algorithm helps to obtain a three-dimensional environment reconstruction model of restricted scenes in coal mines. Firstly, align the depth map and color map captured by the Kinect-2 camera, generate a 3D point cloud, and perform preprocessing operations including point cloud simplification, outlier removal, and establishing a 3D topology structure; Then, in response to the unstable geometric features of randomly sampled points and the high computational cost of FPFH features in the sampling consistency algorithm, the point cloud data is simplified using average curvature, combined with two constraints of distance threshold and point cloud average density, to generate feature point sets and matching point sets with richer geometric features. The transformation relationship between corresponding points in the point sets is calculated for point cloud coarse registration; Finally, in response to the problem of the iterative nearest neighbor algorithm easily falling into local optimal solutions due to inaccurate initial values, the iterative nearest neighbor algorithm is combined with the initial transformation matrix generated by coarse registration for precise registration. The proposed algorithm has high reconstruction model realism and better point cloud registration accuracy than mainstream models in unstructured simulation environments and mine tunnel simulation environments, and its feasibility has been verified.</jats:p>"\n      ]\n    },\n    {\n      "title": "Learning with Noisy Ground Truth: From 2D Classification to 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-06-23T02:21:48Z",\n      "url": "http://arxiv.org/abs/2406.15982v1",\n      "doi": "",\n      "authors": [\n        "Yangdi Lu",\n        "Wenbo He"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Deep neural networks has been highly successful in data-intense computer vision applications, while such success relies heavily on the massive and clean data. In real-world scenarios, clean data sometimes is difficult to obtain. For example, in image classification and segmentation tasks, precise annotations of millions samples are generally very expensive and time-consuming. In 3D static scene reconstruction task, most NeRF related methods require the foundational assumption of the static scene (e.g. consistent lighting condition and persistent object positions), which is often violated in real-world scenarios. To address these problem, learning with noisy ground truth (LNGT) has emerged as an effective learning method and shows great potential. In this short survey, we propose a formal definition unify the analysis of LNGT LNGT in the context of different machine learning tasks (classification and regression). Based on this definition, we propose a novel taxonomy to classify the existing work according to the error decomposition with the fundamental definition of machine learning. Further, we provide in-depth analysis on memorization effect and insightful discussion about potential future research opportunities from 2D classification to 3D reconstruction, in the hope of providing guidance to follow-up research."\n      ]\n    },\n    {\n      "title": "Research on Partial Missing Reconstruction of 3D Point Cloud Model Based on Point Fractal Network",\n      "source": "Crossref / Crossref",\n      "year": 2024,\n      "date": "2024-5-2",\n      "url": "https://doi.org/10.22541/au.171462597.77668952/v1",\n      "doi": "10.22541/au.171462597.77668952/v1",\n      "authors": [\n        "jian wang",\n        "Zhenglin LI",\n        "Zhijie FANG",\n        "Yuan MA",\n        "Binjie SHI",\n        "Qingqing FAN",\n        "Zhiwen WANG"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p id=\\"p1\\">In order to solve the problem of partial loss of data information and structure of 3D point cloud model due to subjective and objective factors such as occlusion and noise, a partial deletion reconstruction method of 3D point cloud model based on PF-Net was proposed, and a model deletion reconstruction system was developed. Based on the deep learning PF-Net network architecture, the Batch Normal layer and the Dropout layer are introduced to normalize the original datasets in batches, which further improves the reconstruction efficiency and accuracy of some missing point cloud models. In this paper, 11 point cloud models are selected to carry out reconstruction experiments with some missing data information and structural features, and the experiments show that the proposed method has higher reconstruction efficiency than the L-Gan and PCN methods when the same dataset is used for training and testing. In the eleven test categories, the average improvement of the refactoring method in this paper is 12%-27%. The proposed method has a significant effect in dealing with the partial deletion reconstruction of small-scale models, and at the same time improves the efficiency and accuracy of reconstruction, which has good application value.</jats:p>"\n      ]\n    },\n    {\n      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",\n      "source": "Crossref / Crossref",\n      "year": 2025,\n      "date": "2025-3-3",\n      "url": "https://doi.org/10.20944/preprints202502.2231.v1",\n      "doi": "10.20944/preprints202502.2231.v1",\n      "authors": [\n        "Wen Xie"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstruction accuracy with an average L2 norm error reduction of 18.7% compared to traditional methods. The algorithm shows particular promise for virtual reality applications, especially for placing interactive virtual objects at corners and edges to facilitate user interaction.</jats:p>"\n      ]\n    },\n    {\n      "title": "Predicting cranial MRI anatomy from 3D optical surface scans using deep learning for radiation therapy treatment planning",\n      "source": "Crossref / Crossref",\n      "year": 2022,\n      "date": "2022-9-13",\n      "url": "https://doi.org/10.21203/rs.3.rs-2013729/v1",\n      "doi": "10.21203/rs.3.rs-2013729/v1",\n      "authors": [\n        "Michael Douglass",\n        "Peter Gorayski",\n        "Sandy Patel",\n        "Alexandre Santos"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<title>Abstract</title> <p><bold>Background</bold> Optical scanning technologies are increasingly being utilised to supplement treatment workflows in radiation oncology, such as surface-guided radiotherapy or 3D printing custom bolus. One limitation of optical scanning devices is the absence of internal anatomical information of the patient being scanned. As a result, conventional radiation therapy treatment planning using this imaging modality is not feasible. Deep learning is useful for automating various manual tasks in radiation oncology, most notably, organ segmentation and treatment planning. Deep learning models have also been used to transform MRI datasets into synthetic CT datasets, facilitating the development of MRI-only radiation therapy planning. <bold>Aims</bold> To train a pix2pix generative adversarial network was trained to transform 3D optical scan data into estimated MRI datasets for a given patient to provide additional anatomical data for a select few radiation therapy treatment sites. The proposed network may provide useful anatomical information for treatment planning of surface mould brachytherapy, total body irradiation, and total skin electron therapy, for example, without delivering any imaging dose. <bold>Methods</bold> A 2D pix2pix GAN was trained on 15,000 axial MRI slices of healthy adult brains paired with corresponding external mask slices. The model was validated on a further 5000 previously unseen external mask slices. The predictions were compared with the “ground-truth” MRI slices using the multi-scale structural similarity index (MSSI) metric. A certified neuro-radiologist was subsequently consulted to provide an independent review of the model’s performance in terms of anatomical accuracy and consistency. The network was then applied to a 3D photogrammetry scan of a test subject to demonstrate the feasibility of this novel technique. <bold>Results</bold> The trained pix2pix network predicted MRI slices with a mean MSSI of 0.831 ± 0.057 for the 5000 validation images indicating that it is possible to estimate a significant proportion of a patient’s gross cranial anatomy from a patient’s exterior contour. When independently reviewed by a certified neuro-radiologist, the model’s performance was described as “quite amazing, but there are limitations in the regions where there is wide variation within the normal population.” When the trained network was applied to a 3D model of a human subject acquired using optical photogrammetry, the network could estimate the corresponding MRI volume for that subject with good qualitative accuracy. However, a ground-truth MRI baseline was not available for quantitative comparison. <bold>Conclusions</bold> A deep learning model was developed, to transform 3D optical scan data of a patient into an estimated MRI volume, potentially increasing the usefulness of optical scanning in radiation therapy planning. This work has demonstrated that much of the human cranial anatomy can be predicted from the external shape of the head and may provide an additional source of valuable imaging data. Further research is required to investigate the feasibility of this approach for use in a clinical setting and further improve the model’s accuracy.</p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 8 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "B-Rep reconstruction from point cloud deep learning",\n      "neural network for B-Rep from 3D scan",\n      "point cloud to CAD B-Rep reconstruction"\n    ],\n    "effective_query": "point cloud to B-Rep reconstruction neural network 2024",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-Rep reconstruction neural network 2024",\n      "B-Rep reconstruction from 3D scans deep learning",\n      "BRepNet point cloud reconstruction"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_HBxMwhjDTfeFpDIaoc1bHEE0' is_error=False
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
      "query": "point cloud to B-Rep reconstruction neural network 2024",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "B-Rep reconstruction from 3D scans deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "BRepNet point cloud reconstruction",
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
      "title": "BRep Boundary and Junction Detection for CAD Reverse Engineering",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-04-13",
      "url": "https://doi.org/10.1109/icmi60790.2024.10585950",
      "doi": "10.1109/icmi60790.2024.10585950",
      "authors": [
        "Sk Aziz Ali",
        "Mohammad Sadil Khan",
        "Didier Stricker"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "In machining process, 3D reverse engineering of mechanical system is an integral, highly important, and yet time consuming step to obtain parametric CAD models from 3D scans. Therefore, deep learning-based Scan-to-CAD modeling can offer designers enormous editability to quickly modify CAD model, being able to parse all its structural compositions and design steps. In this paper, we propose a supervised boundary representation (BRep) detection network BRepDetNet from 3D scans of CC3D and ABC dataset. We have carefully annotated the ~50K and ~45K scans of both the datasets with appropriate topological relations (e.g., next, mate, previous) between the geometrical primitives (i.e., boundaries, junctions, loops, faces) of their BRep data structures. The proposed solution decomposes the Scan-to-CAD problem in Scan-to-BRep ensuring the right step towards feature-based modeling, and therefore, leveraging other existing BRep-to-CAD modeling methods. Our proposed Scan-to-BRep neural network learns to detect BRep boundaries and junctions by minimizing focal-loss and non-maximal sup-pression (NMS) during training time. Experimental results show that our BRepDetNet with NMS-Loss achieves impressive results."
      ]
    },
    {
      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-11-07",
      "url": "http://arxiv.org/abs/2411.04954",
      "doi": "10.48550/arxiv.2411.04954",
      "authors": [
        "Jiasheng Xu",
        "Chenyu Wang",
        "Zheng Zhao",
        "Wenyu Liu",
        "Yi Ma",
        "S. M. Gao"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract In recent years, there have been many studies using artificial intelligence to recognize machining features in three-dimensional models in the computer-aided design (CAD)/computer-aided manufacturing field. Most of these studies converted the original CAD data into images, point clouds, or voxels for recognition. This led to information loss during the conversion process, resulting in decreased recognition accuracy. In this paper, we propose a novel deep learning model called the boundary representation graph attention network (BRepGAT) to segment faces in an original boundary representation (B-rep) model containing machining features. We define descriptors that represent information about the faces and edges of the B-rep model from the perspective of feature recognition. These descriptors are extracted from the B-rep model and transformed into homogeneous graph data, which are then passed to graph networks. BRepGAT recognizes machining features from the graph data input. Our experimental results using the MFCAD18++ dataset showed that BRepGAT achieved state-of-the-art recognition accuracy (99.1%). Furthermore, BRepGAT showed relatively robust performance on other datasets besides MFCAD18++."
      ]
    },
    {
      "title": "Extending Point-Based Deep Learning Approaches for Better Semantic Segmentation in CAD",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-10-10",
      "url": "https://doi.org/10.1016/j.cad.2023.103629",
      "doi": "10.1016/j.cad.2023.103629",
      "authors": [
        "Gerico Vidanes",
        "David J. J. Toal",
        "Xu Zhang",
        "Andy J. Keane",
        "Jon Gregory",
        "Marco Nuñez"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Geometry understanding is a core concept of computer-aided design and engineering (CAD/CAE). Deep neural networks have increasingly shown success as a method of processing complex inputs to achieve abstract tasks. This work revisits a generic and relatively simple approach to 3D deep learning - a point-based graph neural network - and develops best-practices and modifications to alleviate traditional drawbacks. It is shown that these methods should not be discounted for CAD tasks; with proper implementation, they can be competitive with more specifically designed approaches. Through an additive study, this work investigates how the boundary representation data can be fully utilised by leveraging the flexibility of point-based graph networks. The final configuration significantly improves on the predictive accuracy of a standard PointNet++ network across multiple CAD model segmentation datasets and achieves state-of-the-art performance on the MFCAD++ machining features dataset. The proposed modifications leave the core neural network unchanged and results also suggest that they can be applied to other point-based approaches."
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
      "title": "3d reconstruction of mine environment based on two-step point cloud alignment algorithm",
      "source": "Crossref / Crossref",
      "year": 2026,
      "date": "2026",
      "url": "https://doi.org/10.2139/ssrn.6391565",
      "doi": "10.2139/ssrn.6391565",
      "authors": [
        "Ying Zhou",
        "Nan Zhou"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>A two-step point cloud registration algorithm based on improved sampling consistency and iterative nearest neighbors is proposed to meet the daily work needs of coal mine production robots and the rapid rescue needs of post disaster rescue robots. This algorithm helps to obtain a three-dimensional environment reconstruction model of restricted scenes in coal mines. Firstly, align the depth map and color map captured by the Kinect-2 camera, generate a 3D point cloud, and perform preprocessing operations including point cloud simplification, outlier removal, and establishing a 3D topology structure; Then, in response to the unstable geometric features of randomly sampled points and the high computational cost of FPFH features in the sampling consistency algorithm, the point cloud data is simplified using average curvature, combined with two constraints of distance threshold and point cloud average density, to generate feature point sets and matching point sets with richer geometric features. The transformation relationship between corresponding points in the point sets is calculated for point cloud coarse registration; Finally, in response to the problem of the iterative nearest neighbor algorithm easily falling into local optimal solutions due to inaccurate initial values, the iterative nearest neighbor algorithm is combined with the initial transformation matrix generated by coarse registration for precise registration. The proposed algorithm has high reconstruction model realism and better point cloud registration accuracy than mainstream models in unstructured simulation environments and mine tunnel simulation environments, and its feasibility has been verified.</jats:p>"
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
      "title": "Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm",
      "source": "Crossref / Crossref",
      "year": 2025,
      "date": "2025-3-3",
      "url": "https://doi.org/10.20944/preprints202502.2231.v1",
      "doi": "10.20944/preprints202502.2231.v1",
      "authors": [
        "Wen Xie"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>This paper presents a novel approach for three-dimensional point cloud coordinate reconstruction using a depth-first search algorithm combined with rotational convex hull gift wrapping. The proposed method searches for optimal convex hulls by maximizing both the number of faces and the sum of squared face areas. Experimental results demonstrate that our algorithm achieves superior reconstruction accuracy with an average L2 norm error reduction of 18.7% compared to traditional methods. The algorithm shows particular promise for virtual reality applications, especially for placing interactive virtual objects at corners and edges to facilitate user interaction.</jats:p>"
      ]
    },
    {
      "title": "Predicting cranial MRI anatomy from 3D optical surface scans using deep learning for radiation therapy treatment planning",
      "source": "Crossref / Crossref",
      "year": 2022,
      "date": "2022-9-13",
      "url": "https://doi.org/10.21203/rs.3.rs-2013729/v1",
      "doi": "10.21203/rs.3.rs-2013729/v1",
      "authors": [
        "Michael Douglass",
        "Peter Gorayski",
        "Sandy Patel",
        "Alexandre Santos"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<title>Abstract</title> <p><bold>Background</bold> Optical scanning technologies are increasingly being utilised to supplement treatment workflows in radiation oncology, such as surface-guided radiotherapy or 3D printing custom bolus. One limitation of optical scanning devices is the absence of internal anatomical information of the patient being scanned. As a result, conventional radiation therapy treatment planning using this imaging modality is not feasible. Deep learning is useful for automating various manual tasks in radiation oncology, most notably, organ segmentation and treatment planning. Deep learning models have also been used to transform MRI datasets into synthetic CT datasets, facilitating the development of MRI-only radiation therapy planning. <bold>Aims</bold> To train a pix2pix generative adversarial network was trained to transform 3D optical scan data into estimated MRI datasets for a given patient to provide additional anatomical data for a select few radiation therapy treatment sites. The proposed network may provide useful anatomical information for treatment planning of surface mould brachytherapy, total body irradiation, and total skin electron therapy, for example, without delivering any imaging dose. <bold>Methods</bold> A 2D pix2pix GAN was trained on 15,000 axial MRI slices of healthy adult brains paired with corresponding external mask slices. The model was validated on a further 5000 previously unseen external mask slices. The predictions were compared with the “ground-truth” MRI slices using the multi-scale structural similarity index (MSSI) metric. A certified neuro-radiologist was subsequently consulted to provide an independent review of the model’s performance in terms of anatomical accuracy and consistency. The network was then applied to a 3D photogrammetry scan of a test subject to demonstrate the feasibility of this novel technique. <bold>Results</bold> The trained pix2pix network predicted MRI slices with a mean MSSI of 0.831 ± 0.057 for the 5000 validation images indicating that it is possible to estimate a significant proportion of a patient’s gross cranial anatomy from a patient’s exterior contour. When independently reviewed by a certified neuro-radiologist, the model’s performance was described as “quite amazing, but there are limitations in the regions where there is wide variation within the normal population.” When the trained network was applied to a 3D model of a human subject acquired using optical photogrammetry, the network could estimate the corresponding MRI volume for that subject with good qualitative accuracy. However, a ground-truth MRI baseline was not available for quantitative comparison. <bold>Conclusions</bold> A deep learning model was developed, to transform 3D optical scan data of a patient into an estimated MRI volume, potentially increasing the usefulness of optical scanning in radiation therapy planning. This work has demonstrated that much of the human cranial anatomy can be predicted from the external shape of the head and may provide an additional source of valuable imaging data. Further research is required to investigate the feasibility of this approach for use in a clinical setting and further improve the model’s accuracy.</p>"
      ]
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 8 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "B-Rep reconstruction from point cloud deep learning",
      "neural network for B-Rep from 3D scan",
      "point cloud to CAD B-Rep reconstruction"
    ],
    "effective_query": "point cloud to B-Rep reconstruction neural network 2024",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-Rep reconstruction neural network 2024",
      "B-Rep reconstruction from 3D scans deep learning",
      "BRepNet point cloud reconstruction"
    ],
    "fallback_used": false
  }
}
```

### Message 19

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=6

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output has shifted towards point cloud reconstruction and segmentation tasks, but it now largely misses the core requirement of direct B-Rep generation. Most papers are about point cloud processing, feature recognition, or general 3D reconstruction, not about outputting a B-Rep data structure (faces, edges, vertices, topology). Only one paper (BRep Boundary and Junction Detection) explicitly mentions B-Rep detection from scans, but it appears to be a detection/segmentation step, not full B-Rep reconstruction. The set fails to capture the frontier research on neural B-Rep generation from point clouds. The evidence snippets are insufficient to confirm B-Rep output for most candidates.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 0,
    "metadata_score": 2,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Three distinct sources were used: Crossref, OpenAlex, arXiv."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "10 non-duplicate candidate papers remain."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 1 (BRep Boundary and Junction Detection) is clearly aligned with B-Rep from point clouds, and even that is a detection network, not a full reconstruction/generation model. The others are about point cloud reconstruction, segmentation, or other applications without B-Rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user required papers that directly output B-Rep data structures from point clouds. The retrieved set includes papers on point cloud reconstruction (PC^2, mine environment reconstruction, partial missing reconstruction, depth-first search coordinate reconstruction) that do not mention B-Rep output. Others are about CAD generation from multimodal inputs (CAD-MLLM) or B-Rep feature segmentation (BRepGAT, Extending Point-Based Deep Learning). These do not fit the strict criteria."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "Fewer than 3 retained papers can be identified as core candidates for direct B-Rep reconstruction from point clouds. The only candidate (BRep Boundary and Junction Detection) is a detection network, not a full generator. The evidence snippets do not support that any paper outputs a complete B-Rep data structure."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are within the 2021-2026 range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a massive missing core: papers that directly reconstruct/generate B-Reps from point clouds using neural networks. The retrieval has over-corrected and now captures general point cloud reconstruction and CAD segmentation, missing the target topic entirely."
    }
  },
  "key_risks": [
    "The retrieval has drifted away from B-Rep generation/reconstruction and into general point cloud processing and CAD segmentation.",
    "Including papers like PC^2 (single-image 3D reconstruction), mine environment reconstruction, and medical imaging prediction would severely mislead the final report.",
    "The evidence snippets do not confirm B-Rep output for any paper except possibly the BRep detection paper, which is not a full reconstruction model."
  ],
  "next_actions": [
    "Return to the previous retrieval's promising B-Rep generation papers (SolidGen, HoLa, AutoBrep, BrepGen) and explicitly verify their input modalities by retrieving full abstracts or introduction sections. If they support point cloud conditioning, they may be acceptable.",
    "Execute a hybrid query: 'B-Rep generation from point clouds transformer 2023 2024 2025' to bridge generation and reconstruction.",
    "Search for specific known papers that combine point clouds and B-Reps, such as 'Point2Cyl' or 'BRepNet', but ensure they are within the time range and do not output operation sequences."
  ]
}
```

### Message 20

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The goal was to find state-of-the-art research papers (2021-2026) focused on the direct neural generation or reconstruction of 3D Boundary Representation (B-Rep) data structures. The core requirement is a method that takes an unstructured point cloud or 3D scan as input and outputs a complete B-Rep (faces, edges, vertices, and their topological relationships). The search strictly excluded work on CAD operation sequences, CSG trees, or program synthesis, prioritizing modern neural architectures like transformers, diffusion models, and autoregressive networks.

## Search Strategy
The search was conducted in three iterative phases using Crossref, OpenAlex, and arXiv:
1.  **Initial Broad Search:** Queries focused on "B-Rep generation" and "neural implicit representation" to capture the target output. This returned many relevant generative models but lacked confirmation of point cloud input.
2.  **Refined Focus on Input Modality:** Queries were sharpened to explicitly include "point cloud to B-Rep" and "3D scans". This improved the set but still yielded papers where point clouds were one of many conditional inputs, not the primary focus.
3.  **Over-Correction to Reconstruction:** A final phase targeted "B-Rep reconstruction from point clouds". This retrieved papers on point cloud processing and segmentation but largely missed the core task of direct B-Rep generation.

The reviewer halted the process after three revisions, concluding the search did not meet the quality bar. The primary failure was an inability to reliably identify a sufficient number of papers that demonstrably use point clouds as the *primary* input for direct B-Rep synthesis, based on abstract-level evidence.

## Candidate Papers
**The search did not clear the quality bar.** No papers were found that could be fully verified as meeting all strict user criteria (primary point cloud input, direct B-Rep output, exclusion of operation sequences). The results are split into two categories based on partial evidence.

### Verified Candidates
Papers with `verification_status` of `partial` that show strong relevance to B-Rep generation, though point cloud input is not confirmed as primary.
*   **HoLa: B-Rep Generation using a Holistic Latent Representation (2025, arXiv)**
    *   **Core Contribution:** Proposes a holistic latent space that unifies B-Rep geometry and topology, enabling a diffusion-based generator. It explicitly lists point clouds as a supported input modality alongside images and text.
    *   **Relevance Note:** Aims for direct B-Rep generation and claims high validity rates. The abstract confirms it accepts point cloud input, but does not specify if it is the primary focus.
*   **BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch (2025, arXiv)**
    *   **Core Contribution:** Introduces a single-stage autoregressive framework using a Voronoi Half-Patch representation for B-Rep generation.
    *   **Relevance Note:** The abstract states the framework supports conditional generation from point clouds (among other modalities). It is a direct B-Rep generator, but point cloud input appears as one of several conditions.
*   **BRep Boundary and Junction Detection for CAD Reverse Engineering (2024, OpenAlex)**
    *   **Core Contribution:** Presents BRepDetNet, a supervised network to detect B-Rep boundaries and junctions from 3D scans as a step towards Scan-to-CAD.
    *   **Relevance Note:** Directly tackles B-Rep element detection from scans. However, it is a detection/segmentation model, not a full B-Rep reconstruction or generator.

### Unverified Leads
The following are high-potential titles from the search that appear to be about direct B-Rep generation but lack evidence in the retrieved snippets to verify point cloud input or exclude operation sequences. They are suggested as leads for follow-up manual investigation.
1.  **SolidGen: An Autoregressive Model for Direct B-rep Synthesis (2022, arXiv)** – A seminal direct B-Rep generation model. The abstract does not mention input modality.
2.  **AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025, arXiv)** – A transformer-based model for autoregressive B-Rep generation. Input modality is not specified in the snippet.
3.  **BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024, arXiv)** – A diffusion model that directly outputs B-Reps. The abstract discusses unconditional generation and conditioning, but not specifically on point clouds.

## Notes and Gaps
*   **Evidence Limitation:** Verification relied on abstract snippets, which often omit detailed descriptions of input modalities and training paradigms, making it impossible to confirm strict exclusion criteria.
*   **Search Drift:** The search struggled to balance the dual constraints of "direct B-Rep output" and "point cloud as primary input." Queries for generation retrieved multi-modal works, while queries for reconstruction retrieved non-B-Rep point cloud methods.
*   **Scarcity of Perfect Matches:** The niche of *neural, point-cloud-to-B-Rep* reconstruction appears to be very specialized. Many state-of-the-art B-Rep generation papers (e.g., SolidGen, BrepGen) focus on unconditional generation or multi-modal conditioning, with point clouds as a secondary option.
*   **Potential Seminal Works Missed:** Known models like **BRepNet** (likely pre-2021) or **Point2Cyl** were not retrieved, possibly due to year-range filters or because they do not frame their task as "generation."

## Recommended Next Steps
1.  **Manual Verification of Leads:** Investigate the full text of the "Unverified Leads" (SolidGen, AutoBrep, BrepGen) and the "Verified Candidates" to definitively confirm their input modalities and output specifications.
2.  **Citation-Chain Exploration:** Use the promising papers (e.g., HoLa, SolidGen) as seeds. Examine papers that cite them or that they cite to find related work specifically focused on point cloud input.
3.  **Venue-Specific Search:** Manually search proceedings of top-tier venues (SIGGRAPH, CVPR, NeurIPS) from 2021-2026 for keywords like "B-Rep", "boundary representation", and "CAD" to identify papers that may have been missed by generic queries.
4.  **Broaden Input Definition:** If the user's priority is the *direct B-Rep output* breakthrough, consider accepting papers that use point clouds as one of several valid conditional inputs, noting this as a current trend in the field.

TERMINATE
```
