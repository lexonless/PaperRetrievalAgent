# Paper Search Debug Trace

**Query:** Search frontier research from the last 5 years on B-rep generation, reconstruction, and recovery.

Focus on papers that generate, reconstruct, or recover B-rep or CAD boundary representations as a primary modeling target.

Prioritize papers that are broadly relevant to general B-rep generation and structured CAD model generation, including methods based on point clouds, scans, images, sketches, text, multimodal inputs, or other representations when they make a meaningful contribution to B-rep generation itself.

Still rank papers especially high when they use point clouds or scans as a major input, but do not exclude strong general B-rep generation papers merely because they are not point-cloud-only methods.

Exclude papers that are clearly unrelated to B-rep or CAD generation/reconstruction.

Do not include papers whose main goal is to reconstruct CAD operation sequences, CAD programs, design history, sketch-extrude commands, or other reverse-engineering representations instead of B-rep generation itself.

Return 8-10 relevant papers with:
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

Rank the most relevant general B-rep generation papers first, while still highlighting point-cloud-based methods when they are strong.
**Generated At:** 2026-03-25T10:34:19
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

- Topic: `B-rep generation, reconstruction, and recovery (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep generation, reconstruction, and recovery",
  "user_intent": "Identify frontier research from the last five years on methods that generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output, with a focus on general B-rep generation techniques and a secondary emphasis on point-cloud/scanned-data inputs.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "B-rep generation from point clouds",
    "B-rep reconstruction from scans",
    "B-rep recovery from images",
    "B-rep generation from sketches",
    "B-rep generation from text",
    "multimodal input to B-rep",
    "structured CAD model synthesis",
    "surface and solid model reconstruction"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "CAD program reverse engineering",
    "design history recovery",
    "sketch-extrude command parsing",
    "procedural modeling not outputting B-rep"
  ],
  "fallback_queries": [
    "CAD model reconstruction recent",
    "boundary representation generation survey",
    "3D solid model from data deep learning"
  ],
  "queries": [
    {
      "query": "B-rep generation from point cloud deep learning",
      "reason": "Directly targets the prioritized input modality (point clouds/scans) for B-rep output."
    },
    {
      "query": "boundary representation reconstruction neural network",
      "reason": "Focuses on modern learning-based methods for B-rep reconstruction from various inputs."
    },
    {
      "query": "CAD model generation from sketch or image",
      "reason": "Captures B-rep generation from alternative, non-point-cloud inputs as requested."
    }
  ],
  "assumptions": [
    "The term 'B-rep generation' in academic literature may also appear as 'CAD model reconstruction', 'solid model recovery', or 'boundary representation synthesis'.",
    "Papers from 2022-2026 are the primary target, but highly relevant late 2021 papers may be included if results are sparse.",
    "The request for 'general B-rep generation' includes methods that produce structured CAD models with faces, edges, and vertices, not just mesh or implicit surfaces."
  ],
  "success_criteria": [
    "Retrieve 8-10 papers where the primary contribution is generating or reconstructing a B-rep model.",
    "Clearly distinguish direct B-rep output papers from those focused on intermediate representations like CAD sequences.",
    "Identify major methodological categories (e.g., neural direct prediction, optimization-based fitting, hybrid approaches).",
    "Highlight trends such as the use of transformers, diffusion models, or program synthesis for B-rep generation."
  ]
}
```

### Planner Output 7

- Topic: `B-rep generation, reconstruction, and recovery from point clouds, scans, and multimodal inputs (3 queries, 2022-2026)`

```json
{
  "topic": "B-rep generation, reconstruction, and recovery from point clouds, scans, and multimodal inputs",
  "user_intent": "Identify frontier research (2022-2026) on methods that directly generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output, with a strong emphasis on general B-rep generation techniques and a prioritized focus on point-cloud/scan-based inputs.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "B-rep generation from point clouds",
    "B-rep reconstruction from 3D scans",
    "CAD model recovery from LiDAR",
    "boundary representation synthesis from multimodal data",
    "structured solid model generation"
  ],
  "exclude_areas": [
    "CAD operation sequence reconstruction",
    "sketch or command sequence generation without B-rep output",
    "mesh or implicit surface reconstruction not producing B-rep",
    "LiDAR data generation for object detection"
  ],
  "fallback_queries": [
    "CAD model from point cloud reconstruction",
    "boundary representation generation recent",
    "3D scan to CAD model deep learning"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2023 2024",
      "reason": "Directly targets the highest-priority gap identified by the reviewer: B-rep generation specifically from point clouds/scans within the core time range."
    },
    {
      "query": "CAD model reconstruction from scan deep learning",
      "reason": "Broadens the search for scan-based methods that output CAD/B-rep models, using terminology common in literature."
    },
    {
      "query": "boundary representation generation from point cloud",
      "reason": "Uses precise terminology ('boundary representation') to find papers that explicitly target B-rep output from point cloud data."
    }
  ],
  "assumptions": [
    "The term 'B-rep generation' may be synonymous with 'CAD model reconstruction' or 'solid model recovery' in relevant papers.",
    "Papers that generate parametric CAD models via sketches or text are considered relevant if they ultimately produce a B-rep, but point-cloud-based methods are the primary target for this retrieval round.",
    "If evidence is insufficient to confirm B-rep output, the paper will be considered lower priority."
  ],
  "success_criteria": [
    "Retrieve at least 3-5 new papers where the primary contribution is B-rep generation/reconstruction from point clouds or 3D scans.",
    "Verify that candidate papers output B-rep geometry, not just intermediate representations like command sequences.",
    "Build a candidate set that allows ranking general B-rep generation papers first while highlighting strong point-cloud methods."
  ]
}
```

## Retrieval Outputs

### Retrieval Output 5

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
      "query": "B-rep generation from point cloud deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation reconstruction neural network",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model generation from sketch or image",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
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
      "title": "Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-05-23T10:11:19Z",
      "url": "http://arxiv.org/abs/2505.17702v3",
      "doi": "",
      "authors": [
        "Xueyang Li",
        "Jiahao Li",
        "Yu Song",
        "Yunzhong Lou",
        "Xiangdong Zhou"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The advent of Computer-Aided Design (CAD) generative modeling will significantly transform the design of industrial products. The recent research endeavor has extended into the realm of Large Language Models (LLMs). In contrast to fine-tuning methods, training-free approaches typically utilize the advanced closed-source LLMs, thereby offering enhanced flexibility and efficiency in the development of AI agents for generating CAD parametric models. However, the substantial cost and limitations of local deployment of the top-tier closed-source LLMs pose challenges in practical applications. The Seek-CAD is the pioneer exploration of locally deployed open-source inference LLM DeepSeek-R1 for CAD parametric model generation with a training-free methodology. This study is the first investigation to incorporate both visual and Chain-of-Thought (CoT) feedback within the self-refinement mechanism for generating CAD models. Specifically, the initial generated parametric CAD model is rendered into a sequence of step-wise perspective images, which are subsequently processed by a Vision Language Model (VLM) alongside the corresponding CoTs derived from DeepSeek-R1 to assess the CAD model generation. Then, the feedback is utilized by DeepSeek-R1 to refine the initial generated model for the next round of generation. Moreover, we present an innovative 3D CAD model dataset structured around the SSR (Sketch, Sketch-based feature, and Refinements) triple design paradigm. This dataset encompasses a wide range of CAD commands, thereby aligning effectively with industrial application requirements and proving suitable for the generation of LLMs. Extensive experiments validate the effectiveness of Seek-CAD under various metrics."
      ]
    },
    {
      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",
      "source": "Crossref / Proceedings of the AAAI Conference on Artificial Intelligence",
      "year": 2025,
      "date": "2025-4-11",
      "url": "https://doi.org/10.1609/aaai.v39i5.32515",
      "doi": "10.1609/aaai.v39i5.32515",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Jianwei Guo",
        "Jinglu Chen",
        "Dong-Ming Yan"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing.</jats:p>"
      ]
    },
    {
      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-03-02T15:11:35Z",
      "url": "http://arxiv.org/abs/2503.00928v1",
      "doi": "",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Jianwei Guo",
        "Jinglu Chen",
        "Dong-Ming Yan"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing."
      ]
    },
    {
      "title": "CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-09-26T01:22:29Z",
      "url": "http://arxiv.org/abs/2409.17457v1",
      "doi": "",
      "authors": [
        "Sifan Wu",
        "Amir Khasahmadi",
        "Mor Katz",
        "Pradeep Kumar Jayaraman",
        "Yewen Pu",
        "Karl Willis",
        "Bang Liu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Parametric Computer-Aided Design (CAD) is central to contemporary mechanical design. However, it encounters challenges in achieving precise parametric sketch modeling and lacks practical evaluation metrics suitable for mechanical design. We harness the capabilities of pre-trained foundation models, renowned for their successes in natural language processing and computer vision, to develop generative models specifically for CAD. These models are adept at understanding complex geometries and design reasoning, a crucial advancement in CAD technology. In this paper, we propose CadVLM, an end-to-end vision language model for CAD generation. Our approach involves adapting pre-trained foundation models to manipulate engineering sketches effectively, integrating both sketch primitive sequences and sketch images. Extensive experiments demonstrate superior performance on multiple CAD sketch generation tasks such as CAD autocompletion, CAD autoconstraint, and image conditional generation. To our knowledge, this is the first instance of a multimodal Large Language Model (LLM) being successfully applied to parametric CAD generation, representing a pioneering step in the field of computer-aided mechanical design."
      ]
    },
    {
      "title": "Large Language Models for Computer-Aided Design Fine Tuned: Dataset and Experiments",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-01-23",
      "url": "https://doi.org/10.1115/1.4067713",
      "doi": "10.1115/1.4067713",
      "authors": [
        "Yuewan Sun",
        "Xinggang Li",
        "Zhenghui Sha"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Despite the power of large language models (LLMs) in various cross-modal generation tasks, their ability to generate 3D computer-aided design (CAD) models from text remains underexplored due to the scarcity of suitable datasets. Additionally, there is a lack of multimodal CAD datasets that include both reconstruction parameters and text descriptions, which are essential for the quantitative evaluation of the CAD generation capabilities of multimodal LLMs. To address these challenges, we developed a dataset of CAD models, sketches, and image data for representative mechanical components such as gears, shafts, and springs, along with natural language descriptions collected via Amazon Mechanical Turk. By using CAD programs as a bridge, we facilitate the conversion of textual output from LLMs into precise 3D CAD designs. To enhance the text-to-CAD generation capabilities of GPT models and demonstrate the utility of our dataset, we developed a pipeline to generate fine-tuning training data for GPT-3.5. We fine-tuned four GPT-3.5 models with various data sampling strategies based on the length of a CAD program. We evaluated these models using parsing rate and intersection over union (IoU) metrics, comparing their performance to that of GPT-4 without fine-tuning. The new knowledge gained from the comparative study on the four different fine-tuned models provided us with guidance on the selection of sampling strategies to build training datasets in fine-tuning practices of LLMs for text-to-CAD generation, considering the trade-off between part complexity, model performance, and cost."
      ]
    },
    {
      "title": "GridFormer: Point-Grid Transformer for Surface Reconstruction",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-03-24",
      "url": "https://doi.org/10.1609/aaai.v38i4.28100",
      "doi": "10.1609/aaai.v38i4.28100",
      "authors": [
        "Shengtao Li",
        "Ge Gao",
        "Yudong Liu",
        "Yu-Shen Liu",
        "Ming Gu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Implicit neural networks have emerged as a crucial technology in 3D surface reconstruction. To reconstruct continuous surfaces from discrete point clouds, encoding the input points into regular grid features (plane or volume) has been commonly employed in existing approaches. However, these methods typically use the grid as an index for uniformly scattering point features. Compared with the irregular point features, the regular grid features may sacrifice some reconstruction details but improve efficiency. To take full advantage of these two types of features, we introduce a novel and high-efficiency attention mechanism between the grid and point features named Point-Grid Transformer (GridFormer). This mechanism treats the grid as a transfer point connecting the space and point cloud. Our method maximizes the spatial expressiveness of grid features and maintains computational efficiency. Furthermore, optimizing predictions over the entire space could potentially result in blurred boundaries. To address this issue, we further propose a boundary optimization strategy incorporating margin binary cross-entropy loss and boundary sampling. This approach enables us to achieve a more precise representation of the object structure. Our experiments validate that our method is effective and outperforms the state-of-the-art approaches under widely used benchmarks by producing more precise geometry reconstructions. The code is available at https://github.com/list17/GridFormer."
      ]
    },
    {
      "title": "Reference-based Image Composition with Sketch via Structure-aware Diffusion Model",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-03-31T06:12:58Z",
      "url": "http://arxiv.org/abs/2304.09748v1",
      "doi": "",
      "authors": [
        "Kangyeol Kim",
        "Sunghyun Park",
        "Junsoo Lee",
        "Jaegul Choo"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent remarkable improvements in large-scale text-to-image generative models have shown promising results in generating high-fidelity images. To further enhance editability and enable fine-grained generation, we introduce a multi-input-conditioned image composition model that incorporates a sketch as a novel modal, alongside a reference image. Thanks to the edge-level controllability using sketches, our method enables a user to edit or complete an image sub-part with a desired structure (i.e., sketch) and content (i.e., reference image). Our framework fine-tunes a pre-trained diffusion model to complete missing regions using the reference image while maintaining sketch guidance. Albeit simple, this leads to wide opportunities to fulfill user needs for obtaining the in-demand images. Through extensive experiments, we demonstrate that our proposed method offers unique use cases for image manipulation, enabling user-driven modifications of arbitrary scenes."
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;div class=\"section abstract\"&gt;&lt;div class=\"htmlview paragraph\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are essential for safer self-driving. We address the unmet need for abundant, high-quality LiDAR data with the development of a synthetic LiDAR point cloud generation tool and validate this tool’s performance using the KITTI-trained PIXOR object detection model. The tool uses a single camera raycasting process and filtering techniques to generate segmented and annotated class specific datasets. This approach will support low-cost bulk generation of accurate data for training advanced selfdriving algorithms, with configurability to simulate existing and upcoming LiDAR configurations possessing varied channels, range, vertical and horizontal fields of view, and angular resolution. In comparison with virtual LiDAR solutions like CARLA [1], this tool requires no game development knowledge and is faster to set up: sensor customization can be done in a front-end panel enabling users to focus more on data generation. The simulator is developed using the Unity Game Engine in conjunction with free and open-source assets, and a build will be shared with the AV community before an open-source release.&lt;/div&gt;&lt;/div&gt;</jats:p>"
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
      "CAD model reconstruction recent",
      "boundary representation generation survey",
      "3D solid model from data deep learning"
    ],
    "effective_query": "B-rep generation from point cloud deep learning",
    "used_override_query": false,
    "executed_queries": [
      "B-rep generation from point cloud deep learning",
      "boundary representation reconstruction neural network",
      "CAD model generation from sketch or image"
    ],
    "fallback_used": false
  }
}
```

### Retrieval Output 10

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
      "query": "point cloud to B-rep reconstruction 2023 2024",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model reconstruction from scan deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation generation from point cloud",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
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
      "title": "BPNet: Bézier Primitive Segmentation on 3D Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-08-01",
      "url": "https://doi.org/10.24963/ijcai.2023/84",
      "doi": "10.24963/ijcai.2023/84",
      "authors": [
        "Rao Fu",
        "Wen Cheng",
        "Qian Li",
        "Xiao Xiao",
        "Pierre Alliez"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper proposes BPNet, a novel end-to-end deep learning framework to learn Bézier primitive segmentation on 3D point clouds. The existing works treat different primitive types separately, thus limiting them to finite shape categories. To address this issue, we seek a generalized primitive segmentation on point clouds. Taking inspiration from Bézier decomposition on NURBS models, we transfer it to guide point cloud segmentation casting off primitive types. A joint optimization framework is proposed to learn Bézier primitive segmentation and geometric fitting simultaneously on a cascaded architecture. Specifically, we introduce a soft voting regularizer to improve primitive segmentation and propose an auto-weight embedding module to cluster point features, making the network more robust and generic. We also introduce a reconstruction module where we successfully process multiple CAD models with different primitives simultaneously. We conducted extensive experiments on the synthetic ABC dataset and real-scan datasets to validate and compare our approach with different baseline methods. Experiments show superior performance over previous work in terms of segmentation, with a substantially faster inference speed."
      ]
    },
    {
      "title": "Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-10-18",
      "url": "https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024",
      "doi": "10.5194/isprs-annals-x-4-2024-287-2024",
      "authors": [
        "O. V. Roman",
        "G. Mazzacca",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Maarten Bassier",
        "Giorgio Agugiaro"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In many countries, recent boosts in the construction and renovation sectors and energy efficiency directives are driving a growing interest in the built environment among designers and maintainers. In this context, customized software solutions tailored for Building Information Modelling (BIM) and Building Energy Modelling (BEM) are proving to be indispensable for optimizing operational efficiency within the Architecture, Engineering, Construction, Owner, and Operator (AECOO) sector and for facilitating the generation of buildings' Digital Twins (DTs). These DTs rely on accurate geometry and ancillary information (semantics, sensors, etc.) to define properties of single elements, enabling crucial simulations in structural conditions or energy needs. However, BIM and BEM model creation and their enrichment with semantic information are highly time-consuming and prone to manual errors. Hence, there is an increasing demand for automatic methods featuring a high level of geometric accuracy to reconstruct building elements, such as walls, floors, and openings captured via 3D reality-based surveying. This paper introduces an automated method for creating Boundary Representation (B-Rep) models from 3D surveying data for the generation of digital building replicas. The method is based on the detection and computation of topological elements from 3D reality-based point clouds. It proves valuable for architectural or design workflows and for conducting energy or quality system simulations."
      ]
    },
    {
      "title": "Topology-Aware Flow-Based Point Cloud Generation",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-08",
      "url": "https://doi.org/10.1109/tcsvt.2022.3181212",
      "doi": "10.1109/tcsvt.2022.3181212",
      "authors": [
        "Takumi Kimura",
        "Takashi Matsubara",
        "Kuniaki Uehara"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Point clouds have attracted attention as a representation of an object’s surface. Deep generative models have typically used a continuous map from a dense set in a latent space to express their variations. However, a continuous map cannot adequately express the varying numbers of holes. That is, previous approaches disregarded the topological structure of point clouds. Furthermore, a point cloud comprises several subparts, making it difficult to express it using a continuous map. This paper proposes ChartPointFlow, a flow-based deep generative model that forms a map conditioned on a label. Similar to a manifold chart, a map conditioned on a label is assigned to a continuous subset of a point cloud. Thus, ChartPointFlow is able to maintain the topological structure with clear boundaries and holes, whereas previous approaches generated blurry point clouds with fuzzy holes. The experimental results show that ChartPointFlow achieves state-of-the-art performance in various tasks, including generation, reconstruction, upsampling, and segmentation."
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
    },
    {
      "title": "Semantic Enrichment of Architectural Heritage Point Clouds Using Artificial Intelligence: The Palacio de Sástago in Zaragoza, Spain",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-12-09",
      "url": "https://doi.org/10.3390/heritage7120321",
      "doi": "10.3390/heritage7120321",
      "authors": [
        "Michele Buldo",
        "Luis Agustín Hernández",
        "Cesare Verdoscia"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "In the current landscape dominated by Artificial Intelligence, the integration of Machine Learning and Deep Learning within the realm of Cultural Heritage, particularly within architectural contexts, is paramount for the efficient processing and interpretation of point clouds. These advanced methods facilitate automated segmentation and classification, significantly improving both the clarity and practical use of data acquired from laser scanning and photogrammetry. The present study investigates the Palacio de Sástago—a prominent Renaissance palace in Zaragoza, Spain—and introduces a cutting-edge modus operandi for the automated recognition of architectural elements within the palace’s inner courtyard. Employing the well-established Random Forest algorithm, implemented in a Python environment, the framework begins with a comprehensive evaluation of the geometric features identified in the LiDAR point cloud. This process employs the Mean Decrease in Impurity metric to evaluate the relevance of each variable. To boost the accuracy and efficiency of the final classifications, the features are refined post-assessment, enhancing both the training phase and the algorithm’s later evaluation. The research’s findings demonstrate significant potential, supporting advancements in CAD systems and HBIM that will enable more precise, automated modelling of architectural elements, thereby enhancing the accuracy of digital reconstructions and improving conservation planning for heritage sites."
      ]
    },
    {
      "title": "Simurgh: A Framework for Cad-Driven Deep Learning Based X-Ray CT Reconstruction",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-10-16",
      "url": "https://doi.org/10.1109/icip46576.2022.9898017",
      "doi": "10.1109/icip46576.2022.9898017",
      "authors": [
        "Amirkoushyar Ziabari",
        "Singanallur Venkatakrishnan",
        "Abhishek Dubey",
        "Alex Lisovich",
        "Paul Brackman",
        "Curtis Frederick",
        "Pradeep Bhattad",
        "Philip R. Bingham"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "High-resolution X-ray computed tomography (XCT) is an important technique for the inspection of additively manufactured (AM) parts. While XCT is typically used off-line to inspect a subset of manufactured parts, significantly accelerating measurement speed while retaining accuracy would enable use of XCT for in-line inspection to rapidly identify defects in each part as it is manufactured. Here, we propose a deep learning (DL) based approach that uses computer aided design (CAD) models of the AM parts and physics-based information to rapidly produce high-quality reconstructions from sparse XCT measurements without high quality ground truth data. Our approach uses a generative adversarial neural network (GAN) to produced realistic training data from the CAD-based simulations and a deep neural network that is trained using data from the first stage to produce accurate 3D reconstructions. Using experimental XCT data of metal parts, we demonstrate enhanced defect detection capabilities while dramatically reducing the scan time."
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 7 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "CAD model from point cloud reconstruction",
      "boundary representation generation recent",
      "3D scan to CAD model deep learning"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2023 2024",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2023 2024",
      "CAD model reconstruction from scan deep learning",
      "boundary representation generation from point cloud"
    ],
    "fallback_used": false
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
  "review_summary": "The retrieval output contains several relevant papers on CAD/B-rep generation from the last five years, but it fails to meet key hard requirements. Most critically, the set lacks sufficient papers that directly target B-rep generation from point clouds or scans, which was a prioritized input modality. Several papers focus on sketch, text, or image inputs, and one paper (GridFormer) is about general surface reconstruction, not B-rep. The evidence snippets are insufficient to confirm that the papers output B-rep as a primary target, and the candidate depth is borderline. The set does not reflect the user's explicit constraint to rank general B-rep generation papers first while highlighting strong point-cloud methods.",
  "scores": {
    "coverage_score": 1,
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
      "passed": false,
      "reason": "After merging duplicates, only 8 unique candidate papers remain. The requirement is at least 5, which is met, but the depth is borderline for the requested 8-10 range and several are not core B-rep generation."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 1-2 are clearly aligned with the user's topic of B-rep generation/reconstruction as a primary target. Papers like 'GridFormer' are about surface reconstruction (likely mesh/implicit), not B-rep. 'Reference-based Image Composition with Sketch' is about image editing, not CAD/B-rep generation. 'End-to-End Synthetic LiDAR Point Cloud Data Generation' is about data generation for object detection, not B-rep reconstruction."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly requested to prioritize papers that generate/reconstruct B-rep, with a secondary emphasis on point-cloud/scanned-data inputs. The retrieved set is skewed towards sketch, text, and image inputs, with only one paper (Brep2Seq) mentioning point cloud reconstruction in its abstract. The set does not reflect the ranking instruction to put general B-rep generation first and highlight point-cloud methods."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 retained papers must plausibly look like core candidates for B-rep generation. Based on evidence snippets, only Brep2Seq, CAD-MLLM, and Seek-CAD appear to target parametric CAD/B-rep generation. RECAD and CadVLM focus on sketches, which may be a step towards B-rep but are not confirmed to output full B-rep models. The others are not core B-rep generation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the resolved time range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: B-rep generation specifically from point clouds or scans. The retrieval over-relies on sketch/text/image methods and includes off-topic papers (surface reconstruction, image composition, LiDAR data generation)."
    }
  },
  "key_risks": [
    "The evidence snippets are at the abstract level and may not confirm that the papers output B-rep (vs. procedural sequences or intermediate sketches).",
    "The set is missing key recent works on point-cloud to B-rep reconstruction, which is a major frontier area.",
    "Several papers may be about generating CAD command sequences or sketches, not the B-rep geometry itself, which the user wanted to exclude."
  ],
  "next_actions": [
    "Execute a targeted search for 'point cloud to B-rep reconstruction 2022 2023 2024 2025' using Crossref and OpenAlex to fill the major gap.",
    "Search for 'boundary representation generation from scan' or 'CAD model reconstruction from point cloud' to capture scan-based methods.",
    "Verify the core contribution of candidate papers like RECAD and CadVLM by retrieving full abstracts or introductions to confirm they output B-rep models, not just sketches or command sequences."
  ]
}
```

### Review 11

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output shows improved coverage of point-cloud-related papers, but it still fails to meet several hard requirements. While the set includes more papers mentioning point clouds, most are not about B-rep generation. Key papers like BPNet, Topology-Aware Flow-Based Point Cloud Generation, Masked Clustering Prediction, Neural Point Cloud Diffusion, and PC^2 are about point cloud generation, segmentation, or reconstruction to point clouds/meshes, not to B-rep or CAD models. The evidence snippets do not confirm B-rep output. Only Brep2Seq and the BIM/BEM paper explicitly mention B-rep, and CAD-MLLM mentions parametric CAD. The candidate depth is insufficient for core B-rep generation, and the relevance is weak. The set does not satisfy the user's intent for frontier research on B-rep generation from point clouds.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 0,
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
      "passed": false,
      "reason": "After merging duplicates, there are 10 unique candidates, but most are not about B-rep generation. The effective depth of relevant papers is far below 5."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only Brep2Seq and 'Towards Automated BIM and BEM Model Generation using a B-Rep-based Method' are clearly aligned with B-rep generation. CAD-MLLM may be relevant but its evidence snippet focuses on command sequences. The other 7 papers are about point cloud processing, generation, segmentation, or reconstruction to point clouds/neural fields, not B-rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly prioritized point-cloud/scan-based inputs for B-rep generation. The retrieved set includes many point cloud papers, but they do not generate B-rep; they generate other representations (point clouds, neural radiance fields, segmentations). The set does not reflect the core requirement of B-rep as the output."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 retained papers must plausibly look like core candidates for B-rep generation. Based on evidence snippets, only Brep2Seq and the BIM/BEM paper are clear. CAD-MLLM is ambiguous (may output command sequences). The others are not core B-rep generation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the resolved time range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence hole: the retrieved papers lack confirmation that they output B-rep. The set is over-reliant on point cloud processing papers that are adjacent but not on-topic. Missing are core papers on learning-based B-rep reconstruction from point clouds (e.g., 'Point2CAD', 'DeepCAD', 'BRepNet'-like approaches for generation)."
    }
  },
  "key_risks": [
    "The evidence snippets are abstract-level and do not confirm B-rep output; many papers are likely about point cloud generation or segmentation, not B-rep synthesis.",
    "The retrieval is biased towards point cloud papers in general, not filtering for B-rep as the target representation.",
    "Critical frontier papers on B-rep generation from scans may be missing because the queries are too broad or the terminology mismatch."
  ],
  "next_actions": [
    "Execute a precise search for 'B-rep generation from point cloud' and 'boundary representation reconstruction from scan' using exact phrase matching in titles/abstracts via Crossref and OpenAlex.",
    "Search for known seminal papers in the area (e.g., 'BRepNet', 'Point2CAD', 'DeepCAD') and retrieve their recent citations (2022-2026) to find frontier follow-ups.",
    "Verify the output representation of ambiguous candidates (e.g., CAD-MLLM, BPNet) by retrieving full abstracts or method sections to confirm they produce B-rep geometry, not just command sequences or point labels."
  ]
}
```

## Tool Activity

### Tool Event 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_iW4aLv6v8ol1ZCGSdSoh5QRX', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep generation from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation reconstruction neural network",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model generation from sketch or image",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-23T10:11:19Z",\n      "url": "http://arxiv.org/abs/2505.17702v3",\n      "doi": "",\n      "authors": [\n        "Xueyang Li",\n        "Jiahao Li",\n        "Yu Song",\n        "Yunzhong Lou",\n        "Xiangdong Zhou"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The advent of Computer-Aided Design (CAD) generative modeling will significantly transform the design of industrial products. The recent research endeavor has extended into the realm of Large Language Models (LLMs). In contrast to fine-tuning methods, training-free approaches typically utilize the advanced closed-source LLMs, thereby offering enhanced flexibility and efficiency in the development of AI agents for generating CAD parametric models. However, the substantial cost and limitations of local deployment of the top-tier closed-source LLMs pose challenges in practical applications. The Seek-CAD is the pioneer exploration of locally deployed open-source inference LLM DeepSeek-R1 for CAD parametric model generation with a training-free methodology. This study is the first investigation to incorporate both visual and Chain-of-Thought (CoT) feedback within the self-refinement mechanism for generating CAD models. Specifically, the initial generated parametric CAD model is rendered into a sequence of step-wise perspective images, which are subsequently processed by a Vision Language Model (VLM) alongside the corresponding CoTs derived from DeepSeek-R1 to assess the CAD model generation. Then, the feedback is utilized by DeepSeek-R1 to refine the initial generated model for the next round of generation. Moreover, we present an innovative 3D CAD model dataset structured around the SSR (Sketch, Sketch-based feature, and Refinements) triple design paradigm. This dataset encompasses a wide range of CAD commands, thereby aligning effectively with industrial application requirements and proving suitable for the generation of LLMs. Extensive experiments validate the effectiveness of Seek-CAD under various metrics."\n      ]\n    },\n    {\n      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",\n      "source": "Crossref / Proceedings of the AAAI Conference on Artificial Intelligence",\n      "year": 2025,\n      "date": "2025-4-11",\n      "url": "https://doi.org/10.1609/aaai.v39i5.32515",\n      "doi": "10.1609/aaai.v39i5.32515",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Jianwei Guo",\n        "Jinglu Chen",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing.</jats:p>"\n      ]\n    },\n    {\n      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-02T15:11:35Z",\n      "url": "http://arxiv.org/abs/2503.00928v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Jianwei Guo",\n        "Jinglu Chen",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing."\n      ]\n    },\n    {\n      "title": "CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-09-26T01:22:29Z",\n      "url": "http://arxiv.org/abs/2409.17457v1",\n      "doi": "",\n      "authors": [\n        "Sifan Wu",\n        "Amir Khasahmadi",\n        "Mor Katz",\n        "Pradeep Kumar Jayaraman",\n        "Yewen Pu",\n        "Karl Willis",\n        "Bang Liu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Parametric Computer-Aided Design (CAD) is central to contemporary mechanical design. However, it encounters challenges in achieving precise parametric sketch modeling and lacks practical evaluation metrics suitable for mechanical design. We harness the capabilities of pre-trained foundation models, renowned for their successes in natural language processing and computer vision, to develop generative models specifically for CAD. These models are adept at understanding complex geometries and design reasoning, a crucial advancement in CAD technology. In this paper, we propose CadVLM, an end-to-end vision language model for CAD generation. Our approach involves adapting pre-trained foundation models to manipulate engineering sketches effectively, integrating both sketch primitive sequences and sketch images. Extensive experiments demonstrate superior performance on multiple CAD sketch generation tasks such as CAD autocompletion, CAD autoconstraint, and image conditional generation. To our knowledge, this is the first instance of a multimodal Large Language Model (LLM) being successfully applied to parametric CAD generation, representing a pioneering step in the field of computer-aided mechanical design."\n      ]\n    },\n    {\n      "title": "Large Language Models for Computer-Aided Design Fine Tuned: Dataset and Experiments",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-01-23",\n      "url": "https://doi.org/10.1115/1.4067713",\n      "doi": "10.1115/1.4067713",\n      "authors": [\n        "Yuewan Sun",\n        "Xinggang Li",\n        "Zhenghui Sha"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Despite the power of large language models (LLMs) in various cross-modal generation tasks, their ability to generate 3D computer-aided design (CAD) models from text remains underexplored due to the scarcity of suitable datasets. Additionally, there is a lack of multimodal CAD datasets that include both reconstruction parameters and text descriptions, which are essential for the quantitative evaluation of the CAD generation capabilities of multimodal LLMs. To address these challenges, we developed a dataset of CAD models, sketches, and image data for representative mechanical components such as gears, shafts, and springs, along with natural language descriptions collected via Amazon Mechanical Turk. By using CAD programs as a bridge, we facilitate the conversion of textual output from LLMs into precise 3D CAD designs. To enhance the text-to-CAD generation capabilities of GPT models and demonstrate the utility of our dataset, we developed a pipeline to generate fine-tuning training data for GPT-3.5. We fine-tuned four GPT-3.5 models with various data sampling strategies based on the length of a CAD program. We evaluated these models using parsing rate and intersection over union (IoU) metrics, comparing their performance to that of GPT-4 without fine-tuning. The new knowledge gained from the comparative study on the four different fine-tuned models provided us with guidance on the selection of sampling strategies to build training datasets in fine-tuning practices of LLMs for text-to-CAD generation, considering the trade-off between part complexity, model performance, and cost."\n      ]\n    },\n    {\n      "title": "GridFormer: Point-Grid Transformer for Surface Reconstruction",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-03-24",\n      "url": "https://doi.org/10.1609/aaai.v38i4.28100",\n      "doi": "10.1609/aaai.v38i4.28100",\n      "authors": [\n        "Shengtao Li",\n        "Ge Gao",\n        "Yudong Liu",\n        "Yu-Shen Liu",\n        "Ming Gu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Implicit neural networks have emerged as a crucial technology in 3D surface reconstruction. To reconstruct continuous surfaces from discrete point clouds, encoding the input points into regular grid features (plane or volume) has been commonly employed in existing approaches. However, these methods typically use the grid as an index for uniformly scattering point features. Compared with the irregular point features, the regular grid features may sacrifice some reconstruction details but improve efficiency. To take full advantage of these two types of features, we introduce a novel and high-efficiency attention mechanism between the grid and point features named Point-Grid Transformer (GridFormer). This mechanism treats the grid as a transfer point connecting the space and point cloud. Our method maximizes the spatial expressiveness of grid features and maintains computational efficiency. Furthermore, optimizing predictions over the entire space could potentially result in blurred boundaries. To address this issue, we further propose a boundary optimization strategy incorporating margin binary cross-entropy loss and boundary sampling. This approach enables us to achieve a more precise representation of the object structure. Our experiments validate that our method is effective and outperforms the state-of-the-art approaches under widely used benchmarks by producing more precise geometry reconstructions. The code is available at https://github.com/list17/GridFormer."\n      ]\n    },\n    {\n      "title": "Reference-based Image Composition with Sketch via Structure-aware Diffusion Model",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-03-31T06:12:58Z",\n      "url": "http://arxiv.org/abs/2304.09748v1",\n      "doi": "",\n      "authors": [\n        "Kangyeol Kim",\n        "Sunghyun Park",\n        "Junsoo Lee",\n        "Jaegul Choo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent remarkable improvements in large-scale text-to-image generative models have shown promising results in generating high-fidelity images. To further enhance editability and enable fine-grained generation, we introduce a multi-input-conditioned image composition model that incorporates a sketch as a novel modal, alongside a reference image. Thanks to the edge-level controllability using sketches, our method enables a user to edit or complete an image sub-part with a desired structure (i.e., sketch) and content (i.e., reference image). Our framework fine-tunes a pre-trained diffusion model to complete missing regions using the reference image while maintaining sketch guidance. Albeit simple, this leads to wide opportunities to fulfill user needs for obtaining the in-demand images. Through extensive experiments, we demonstrate that our proposed method offers unique use cases for image manipulation, enabling user-driven modifications of arbitrary scenes."\n      ]\n    },\n    {\n      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",\n      "source": "Crossref / SAE Technical Paper Series",\n      "year": 2022,\n      "date": "2022-3-29",\n      "url": "https://doi.org/10.4271/2022-01-0164",\n      "doi": "10.4271/2022-01-0164",\n      "authors": [\n        "Karthik Karur",\n        "Georgios Pappas",\n        "Joshua Siegel",\n        "Mi Zhang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;div class=\\"section abstract\\"&gt;&lt;div class=\\"htmlview paragraph\\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are essential for safer self-driving. We address the unmet need for abundant, high-quality LiDAR data with the development of a synthetic LiDAR point cloud generation tool and validate this tool’s performance using the KITTI-trained PIXOR object detection model. The tool uses a single camera raycasting process and filtering techniques to generate segmented and annotated class specific datasets. This approach will support low-cost bulk generation of accurate data for training advanced selfdriving algorithms, with configurability to simulate existing and upcoming LiDAR configurations possessing varied channels, range, vertical and horizontal fields of view, and angular resolution. In comparison with virtual LiDAR solutions like CARLA [1], this tool requires no game development knowledge and is faster to set up: sensor customization can be done in a front-end panel enabling users to focus more on data generation. The simulator is developed using the Unity Game Engine in conjunction with free and open-source assets, and a build will be shared with the AV community before an open-source release.&lt;/div&gt;&lt;/div&gt;</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "CAD model reconstruction recent",\n      "boundary representation generation survey",\n      "3D solid model from data deep learning"\n    ],\n    "effective_query": "B-rep generation from point cloud deep learning",\n    "used_override_query": false,\n    "executed_queries": [\n      "B-rep generation from point cloud deep learning",\n      "boundary representation reconstruction neural network",\n      "CAD model generation from sketch or image"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_iW4aLv6v8ol1ZCGSdSoh5QRX' is_error=False
```

### Tool Event 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_iKe16xHqYt5VnAGizZCyK5rh', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-rep reconstruction 2023 2024"}', name='retrieve_candidates_from_plan')
```

### Tool Event 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2023 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model reconstruction from scan deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation generation from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "BPNet: Bézier Primitive Segmentation on 3D Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-08-01",\n      "url": "https://doi.org/10.24963/ijcai.2023/84",\n      "doi": "10.24963/ijcai.2023/84",\n      "authors": [\n        "Rao Fu",\n        "Wen Cheng",\n        "Qian Li",\n        "Xiao Xiao",\n        "Pierre Alliez"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper proposes BPNet, a novel end-to-end deep learning framework to learn Bézier primitive segmentation on 3D point clouds. The existing works treat different primitive types separately, thus limiting them to finite shape categories. To address this issue, we seek a generalized primitive segmentation on point clouds. Taking inspiration from Bézier decomposition on NURBS models, we transfer it to guide point cloud segmentation casting off primitive types. A joint optimization framework is proposed to learn Bézier primitive segmentation and geometric fitting simultaneously on a cascaded architecture. Specifically, we introduce a soft voting regularizer to improve primitive segmentation and propose an auto-weight embedding module to cluster point features, making the network more robust and generic. We also introduce a reconstruction module where we successfully process multiple CAD models with different primitives simultaneously. We conducted extensive experiments on the synthetic ABC dataset and real-scan datasets to validate and compare our approach with different baseline methods. Experiments show superior performance over previous work in terms of segmentation, with a substantially faster inference speed."\n      ]\n    },\n    {\n      "title": "Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-10-18",\n      "url": "https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024",\n      "doi": "10.5194/isprs-annals-x-4-2024-287-2024",\n      "authors": [\n        "O. V. Roman",\n        "G. Mazzacca",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Maarten Bassier",\n        "Giorgio Agugiaro"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In many countries, recent boosts in the construction and renovation sectors and energy efficiency directives are driving a growing interest in the built environment among designers and maintainers. In this context, customized software solutions tailored for Building Information Modelling (BIM) and Building Energy Modelling (BEM) are proving to be indispensable for optimizing operational efficiency within the Architecture, Engineering, Construction, Owner, and Operator (AECOO) sector and for facilitating the generation of buildings\' Digital Twins (DTs). These DTs rely on accurate geometry and ancillary information (semantics, sensors, etc.) to define properties of single elements, enabling crucial simulations in structural conditions or energy needs. However, BIM and BEM model creation and their enrichment with semantic information are highly time-consuming and prone to manual errors. Hence, there is an increasing demand for automatic methods featuring a high level of geometric accuracy to reconstruct building elements, such as walls, floors, and openings captured via 3D reality-based surveying. This paper introduces an automated method for creating Boundary Representation (B-Rep) models from 3D surveying data for the generation of digital building replicas. The method is based on the detection and computation of topological elements from 3D reality-based point clouds. It proves valuable for architectural or design workflows and for conducting energy or quality system simulations."\n      ]\n    },\n    {\n      "title": "Topology-Aware Flow-Based Point Cloud Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-08",\n      "url": "https://doi.org/10.1109/tcsvt.2022.3181212",\n      "doi": "10.1109/tcsvt.2022.3181212",\n      "authors": [\n        "Takumi Kimura",\n        "Takashi Matsubara",\n        "Kuniaki Uehara"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Point clouds have attracted attention as a representation of an object’s surface. Deep generative models have typically used a continuous map from a dense set in a latent space to express their variations. However, a continuous map cannot adequately express the varying numbers of holes. That is, previous approaches disregarded the topological structure of point clouds. Furthermore, a point cloud comprises several subparts, making it difficult to express it using a continuous map. This paper proposes ChartPointFlow, a flow-based deep generative model that forms a map conditioned on a label. Similar to a manifold chart, a map conditioned on a label is assigned to a continuous subset of a point cloud. Thus, ChartPointFlow is able to maintain the topological structure with clear boundaries and holes, whereas previous approaches generated blurry point clouds with fuzzy holes. The experimental results show that ChartPointFlow achieves state-of-the-art performance in various tasks, including generation, reconstruction, upsampling, and segmentation."\n      ]\n    },\n    {\n      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-08-12T12:58:44Z",\n      "url": "http://arxiv.org/abs/2508.08910v1",\n      "doi": "",\n      "authors": [\n        "Bin Ren",\n        "Xiaoshui Huang",\n        "Mengyuan Liu",\n        "Hong Liu",\n        "Fabio Poiesi",\n        "Nicu Sebe",\n        "Guofeng Mei"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."\n      ]\n    },\n    {\n      "title": "Semantic Enrichment of Architectural Heritage Point Clouds Using Artificial Intelligence: The Palacio de Sástago in Zaragoza, Spain",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-12-09",\n      "url": "https://doi.org/10.3390/heritage7120321",\n      "doi": "10.3390/heritage7120321",\n      "authors": [\n        "Michele Buldo",\n        "Luis Agustín Hernández",\n        "Cesare Verdoscia"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "In the current landscape dominated by Artificial Intelligence, the integration of Machine Learning and Deep Learning within the realm of Cultural Heritage, particularly within architectural contexts, is paramount for the efficient processing and interpretation of point clouds. These advanced methods facilitate automated segmentation and classification, significantly improving both the clarity and practical use of data acquired from laser scanning and photogrammetry. The present study investigates the Palacio de Sástago—a prominent Renaissance palace in Zaragoza, Spain—and introduces a cutting-edge modus operandi for the automated recognition of architectural elements within the palace’s inner courtyard. Employing the well-established Random Forest algorithm, implemented in a Python environment, the framework begins with a comprehensive evaluation of the geometric features identified in the LiDAR point cloud. This process employs the Mean Decrease in Impurity metric to evaluate the relevance of each variable. To boost the accuracy and efficiency of the final classifications, the features are refined post-assessment, enhancing both the training phase and the algorithm’s later evaluation. The research’s findings demonstrate significant potential, supporting advancements in CAD systems and HBIM that will enable more precise, automated modelling of architectural elements, thereby enhancing the accuracy of digital reconstructions and improving conservation planning for heritage sites."\n      ]\n    },\n    {\n      "title": "Simurgh: A Framework for Cad-Driven Deep Learning Based X-Ray CT Reconstruction",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-10-16",\n      "url": "https://doi.org/10.1109/icip46576.2022.9898017",\n      "doi": "10.1109/icip46576.2022.9898017",\n      "authors": [\n        "Amirkoushyar Ziabari",\n        "Singanallur Venkatakrishnan",\n        "Abhishek Dubey",\n        "Alex Lisovich",\n        "Paul Brackman",\n        "Curtis Frederick",\n        "Pradeep Bhattad",\n        "Philip R. Bingham"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "High-resolution X-ray computed tomography (XCT) is an important technique for the inspection of additively manufactured (AM) parts. While XCT is typically used off-line to inspect a subset of manufactured parts, significantly accelerating measurement speed while retaining accuracy would enable use of XCT for in-line inspection to rapidly identify defects in each part as it is manufactured. Here, we propose a deep learning (DL) based approach that uses computer aided design (CAD) models of the AM parts and physics-based information to rapidly produce high-quality reconstructions from sparse XCT measurements without high quality ground truth data. Our approach uses a generative adversarial neural network (GAN) to produced realistic training data from the CAD-based simulations and a deep neural network that is trained using data from the first stage to produce accurate 3D reconstructions. Using experimental XCT data of metal parts, we demonstrate enhanced defect detection capabilities while dramatically reducing the scan time."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 7 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "CAD model from point cloud reconstruction",\n      "boundary representation generation recent",\n      "3D scan to CAD model deep learning"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2023 2024",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2023 2024",\n      "CAD model reconstruction from scan deep learning",\n      "boundary representation generation from point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_iKe16xHqYt5VnAGizZCyK5rh' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search frontier research from the last 5 years on B-rep generation, reconstruction, and recovery.

```text
Search frontier research from the last 5 years on B-rep generation, reconstruction, and recovery.

Focus on papers that generate, reconstruct, or recover B-rep or CAD boundary representations as a primary modeling target.

Prioritize papers that are broadly relevant to general B-rep generation and structured CAD model generation, including methods based on point clouds, scans, images, sketches, text, multimodal inputs, or other representations when they make a meaningful contribution to B-rep generation itself.

Still rank papers especially high when they use point clouds or scans as a major input, but do not exclude strong general B-rep generation papers merely because they are not point-cloud-only methods.

Exclude papers that are clearly unrelated to B-rep or CAD generation/reconstruction.

Do not include papers whose main goal is to reconstruct CAD operation sequences, CAD programs, design history, sketch-extrude commands, or other reverse-engineering representations instead of B-rep generation itself.

Return 8-10 relevant papers with:
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

Rank the most relevant general B-rep generation papers first, while still highlighting point-cloud-based methods when they are strong.

[Runtime Search Context]
Today's date for this run is 2026-03-25.
- Resolve "last 5 years" as the inclusive year window 2022-2026.
- Treat that resolved year window as authoritative unless a later agent explicitly labels a broader range as an extra.
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep generation, reconstruction, and recovery, queries=3, years=2022-2026

```text
{
  "topic": "B-rep generation, reconstruction, and recovery",
  "user_intent": "Identify frontier research from the last five years on methods that generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output, with a focus on general B-rep generation techniques and a secondary emphasis on point-cloud/scanned-data inputs.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep generation from point clouds", "B-rep reconstruction from scans", "B-rep recovery from images", "B-rep generation from sketches", "B-rep generation from text", "multimodal input to B-rep", "structured CAD model synthesis", "surface and solid model reconstruction"],
  "exclude_areas": ["CAD operation sequence reconstruction", "CAD program reverse engineering", "design history recovery", "sketch-extrude command parsing", "procedural modeling not outputting B-rep"],
  "fallback_queries": ["CAD model reconstruction recent", "boundary representation generation survey", "3D solid model from data deep learning"],
  "queries": [
    {
      "query": "B-rep generation from point cloud deep learning",
      "reason": "Directly targets the prioritized input modality (point clouds/scans) for B-rep output."
    },
    {
      "query": "boundary representation reconstruction neural network",
      "reason": "Focuses on modern learning-based methods for B-rep reconstruction from various inputs."
    },
    {
      "query": "CAD model generation from sketch or image",
      "reason": "Captures B-rep generation from alternative, non-point-cloud inputs as requested."
    }
  ],
  "assumptions": ["The term 'B-rep generation' in academic literature may also appear as 'CAD model reconstruction', 'solid model recovery', or 'boundary representation synthesis'.", "Papers from 2022-2026 are the primary target, but highly relevant late 2021 papers may be included if results are sparse.", "The request for 'general B-rep generation' includes methods that produce structured CAD models with faces, edges, and vertices, not just mesh or implicit surfaces."],
  "success_criteria": ["Retrieve 8-10 papers where the primary contribution is generating or reconstructing a B-rep model.", "Clearly distinguish direct B-rep output papers from those focused on intermediate representations like CAD sequences.", "Identify major methodological categories (e.g., neural direct prediction, optimization-based fitting, hybrid approaches).", "Highlight trends such as the use of transformers, diffusion models, or program synthesis for B-rep generation."]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_iW4aLv6v8ol1ZCGSdSoh5QRX', arguments='{"top_k": 10, "max_results_per_source": 20}', name='retrieve_candidates_from_plan')
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "B-rep generation from point cloud deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation reconstruction neural network",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model generation from sketch or image",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-05-23T10:11:19Z",\n      "url": "http://arxiv.org/abs/2505.17702v3",\n      "doi": "",\n      "authors": [\n        "Xueyang Li",\n        "Jiahao Li",\n        "Yu Song",\n        "Yunzhong Lou",\n        "Xiangdong Zhou"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The advent of Computer-Aided Design (CAD) generative modeling will significantly transform the design of industrial products. The recent research endeavor has extended into the realm of Large Language Models (LLMs). In contrast to fine-tuning methods, training-free approaches typically utilize the advanced closed-source LLMs, thereby offering enhanced flexibility and efficiency in the development of AI agents for generating CAD parametric models. However, the substantial cost and limitations of local deployment of the top-tier closed-source LLMs pose challenges in practical applications. The Seek-CAD is the pioneer exploration of locally deployed open-source inference LLM DeepSeek-R1 for CAD parametric model generation with a training-free methodology. This study is the first investigation to incorporate both visual and Chain-of-Thought (CoT) feedback within the self-refinement mechanism for generating CAD models. Specifically, the initial generated parametric CAD model is rendered into a sequence of step-wise perspective images, which are subsequently processed by a Vision Language Model (VLM) alongside the corresponding CoTs derived from DeepSeek-R1 to assess the CAD model generation. Then, the feedback is utilized by DeepSeek-R1 to refine the initial generated model for the next round of generation. Moreover, we present an innovative 3D CAD model dataset structured around the SSR (Sketch, Sketch-based feature, and Refinements) triple design paradigm. This dataset encompasses a wide range of CAD commands, thereby aligning effectively with industrial application requirements and proving suitable for the generation of LLMs. Extensive experiments validate the effectiveness of Seek-CAD under various metrics."\n      ]\n    },\n    {\n      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",\n      "source": "Crossref / Proceedings of the AAAI Conference on Artificial Intelligence",\n      "year": 2025,\n      "date": "2025-4-11",\n      "url": "https://doi.org/10.1609/aaai.v39i5.32515",\n      "doi": "10.1609/aaai.v39i5.32515",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Jianwei Guo",\n        "Jinglu Chen",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing.</jats:p>"\n      ]\n    },\n    {\n      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-03-02T15:11:35Z",\n      "url": "http://arxiv.org/abs/2503.00928v1",\n      "doi": "",\n      "authors": [\n        "Pu Li",\n        "Wenhao Zhang",\n        "Jianwei Guo",\n        "Jinglu Chen",\n        "Dong-Ming Yan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing."\n      ]\n    },\n    {\n      "title": "CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-09-26T01:22:29Z",\n      "url": "http://arxiv.org/abs/2409.17457v1",\n      "doi": "",\n      "authors": [\n        "Sifan Wu",\n        "Amir Khasahmadi",\n        "Mor Katz",\n        "Pradeep Kumar Jayaraman",\n        "Yewen Pu",\n        "Karl Willis",\n        "Bang Liu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Parametric Computer-Aided Design (CAD) is central to contemporary mechanical design. However, it encounters challenges in achieving precise parametric sketch modeling and lacks practical evaluation metrics suitable for mechanical design. We harness the capabilities of pre-trained foundation models, renowned for their successes in natural language processing and computer vision, to develop generative models specifically for CAD. These models are adept at understanding complex geometries and design reasoning, a crucial advancement in CAD technology. In this paper, we propose CadVLM, an end-to-end vision language model for CAD generation. Our approach involves adapting pre-trained foundation models to manipulate engineering sketches effectively, integrating both sketch primitive sequences and sketch images. Extensive experiments demonstrate superior performance on multiple CAD sketch generation tasks such as CAD autocompletion, CAD autoconstraint, and image conditional generation. To our knowledge, this is the first instance of a multimodal Large Language Model (LLM) being successfully applied to parametric CAD generation, representing a pioneering step in the field of computer-aided mechanical design."\n      ]\n    },\n    {\n      "title": "Large Language Models for Computer-Aided Design Fine Tuned: Dataset and Experiments",\n      "source": "OpenAlex",\n      "year": 2025,\n      "date": "2025-01-23",\n      "url": "https://doi.org/10.1115/1.4067713",\n      "doi": "10.1115/1.4067713",\n      "authors": [\n        "Yuewan Sun",\n        "Xinggang Li",\n        "Zhenghui Sha"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Despite the power of large language models (LLMs) in various cross-modal generation tasks, their ability to generate 3D computer-aided design (CAD) models from text remains underexplored due to the scarcity of suitable datasets. Additionally, there is a lack of multimodal CAD datasets that include both reconstruction parameters and text descriptions, which are essential for the quantitative evaluation of the CAD generation capabilities of multimodal LLMs. To address these challenges, we developed a dataset of CAD models, sketches, and image data for representative mechanical components such as gears, shafts, and springs, along with natural language descriptions collected via Amazon Mechanical Turk. By using CAD programs as a bridge, we facilitate the conversion of textual output from LLMs into precise 3D CAD designs. To enhance the text-to-CAD generation capabilities of GPT models and demonstrate the utility of our dataset, we developed a pipeline to generate fine-tuning training data for GPT-3.5. We fine-tuned four GPT-3.5 models with various data sampling strategies based on the length of a CAD program. We evaluated these models using parsing rate and intersection over union (IoU) metrics, comparing their performance to that of GPT-4 without fine-tuning. The new knowledge gained from the comparative study on the four different fine-tuned models provided us with guidance on the selection of sampling strategies to build training datasets in fine-tuning practices of LLMs for text-to-CAD generation, considering the trade-off between part complexity, model performance, and cost."\n      ]\n    },\n    {\n      "title": "GridFormer: Point-Grid Transformer for Surface Reconstruction",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-03-24",\n      "url": "https://doi.org/10.1609/aaai.v38i4.28100",\n      "doi": "10.1609/aaai.v38i4.28100",\n      "authors": [\n        "Shengtao Li",\n        "Ge Gao",\n        "Yudong Liu",\n        "Yu-Shen Liu",\n        "Ming Gu"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Implicit neural networks have emerged as a crucial technology in 3D surface reconstruction. To reconstruct continuous surfaces from discrete point clouds, encoding the input points into regular grid features (plane or volume) has been commonly employed in existing approaches. However, these methods typically use the grid as an index for uniformly scattering point features. Compared with the irregular point features, the regular grid features may sacrifice some reconstruction details but improve efficiency. To take full advantage of these two types of features, we introduce a novel and high-efficiency attention mechanism between the grid and point features named Point-Grid Transformer (GridFormer). This mechanism treats the grid as a transfer point connecting the space and point cloud. Our method maximizes the spatial expressiveness of grid features and maintains computational efficiency. Furthermore, optimizing predictions over the entire space could potentially result in blurred boundaries. To address this issue, we further propose a boundary optimization strategy incorporating margin binary cross-entropy loss and boundary sampling. This approach enables us to achieve a more precise representation of the object structure. Our experiments validate that our method is effective and outperforms the state-of-the-art approaches under widely used benchmarks by producing more precise geometry reconstructions. The code is available at https://github.com/list17/GridFormer."\n      ]\n    },\n    {\n      "title": "Reference-based Image Composition with Sketch via Structure-aware Diffusion Model",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-03-31T06:12:58Z",\n      "url": "http://arxiv.org/abs/2304.09748v1",\n      "doi": "",\n      "authors": [\n        "Kangyeol Kim",\n        "Sunghyun Park",\n        "Junsoo Lee",\n        "Jaegul Choo"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Recent remarkable improvements in large-scale text-to-image generative models have shown promising results in generating high-fidelity images. To further enhance editability and enable fine-grained generation, we introduce a multi-input-conditioned image composition model that incorporates a sketch as a novel modal, alongside a reference image. Thanks to the edge-level controllability using sketches, our method enables a user to edit or complete an image sub-part with a desired structure (i.e., sketch) and content (i.e., reference image). Our framework fine-tunes a pre-trained diffusion model to complete missing regions using the reference image while maintaining sketch guidance. Albeit simple, this leads to wide opportunities to fulfill user needs for obtaining the in-demand images. Through extensive experiments, we demonstrate that our proposed method offers unique use cases for image manipulation, enabling user-driven modifications of arbitrary scenes."\n      ]\n    },\n    {\n      "title": "End-to-End Synthetic LiDAR Point Cloud Data Generation and Deep Learning Validation",\n      "source": "Crossref / SAE Technical Paper Series",\n      "year": 2022,\n      "date": "2022-3-29",\n      "url": "https://doi.org/10.4271/2022-01-0164",\n      "doi": "10.4271/2022-01-0164",\n      "authors": [\n        "Karthik Karur",\n        "Georgios Pappas",\n        "Joshua Siegel",\n        "Mi Zhang"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "<jats:p>&lt;div class=\\"section abstract\\"&gt;&lt;div class=\\"htmlview paragraph\\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are essential for safer self-driving. We address the unmet need for abundant, high-quality LiDAR data with the development of a synthetic LiDAR point cloud generation tool and validate this tool’s performance using the KITTI-trained PIXOR object detection model. The tool uses a single camera raycasting process and filtering techniques to generate segmented and annotated class specific datasets. This approach will support low-cost bulk generation of accurate data for training advanced selfdriving algorithms, with configurability to simulate existing and upcoming LiDAR configurations possessing varied channels, range, vertical and horizontal fields of view, and angular resolution. In comparison with virtual LiDAR solutions like CARLA [1], this tool requires no game development knowledge and is faster to set up: sensor customization can be done in a front-end panel enabling users to focus more on data generation. The simulator is developed using the Unity Game Engine in conjunction with free and open-source assets, and a build will be shared with the AV community before an open-source release.&lt;/div&gt;&lt;/div&gt;</jats:p>"\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 3 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "CAD model reconstruction recent",\n      "boundary representation generation survey",\n      "3D solid model from data deep learning"\n    ],\n    "effective_query": "B-rep generation from point cloud deep learning",\n    "used_override_query": false,\n    "executed_queries": [\n      "B-rep generation from point cloud deep learning",\n      "boundary representation reconstruction neural network",\n      "CAD model generation from sketch or image"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_iW4aLv6v8ol1ZCGSdSoh5QRX' is_error=False
```

### Message 5

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
      "query": "B-rep generation from point cloud deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation reconstruction neural network",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model generation from sketch or image",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
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
      "title": "Seek-CAD: A Self-refined Generative Modeling for 3D Parametric CAD Using Local Inference via DeepSeek",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-05-23T10:11:19Z",
      "url": "http://arxiv.org/abs/2505.17702v3",
      "doi": "",
      "authors": [
        "Xueyang Li",
        "Jiahao Li",
        "Yu Song",
        "Yunzhong Lou",
        "Xiangdong Zhou"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The advent of Computer-Aided Design (CAD) generative modeling will significantly transform the design of industrial products. The recent research endeavor has extended into the realm of Large Language Models (LLMs). In contrast to fine-tuning methods, training-free approaches typically utilize the advanced closed-source LLMs, thereby offering enhanced flexibility and efficiency in the development of AI agents for generating CAD parametric models. However, the substantial cost and limitations of local deployment of the top-tier closed-source LLMs pose challenges in practical applications. The Seek-CAD is the pioneer exploration of locally deployed open-source inference LLM DeepSeek-R1 for CAD parametric model generation with a training-free methodology. This study is the first investigation to incorporate both visual and Chain-of-Thought (CoT) feedback within the self-refinement mechanism for generating CAD models. Specifically, the initial generated parametric CAD model is rendered into a sequence of step-wise perspective images, which are subsequently processed by a Vision Language Model (VLM) alongside the corresponding CoTs derived from DeepSeek-R1 to assess the CAD model generation. Then, the feedback is utilized by DeepSeek-R1 to refine the initial generated model for the next round of generation. Moreover, we present an innovative 3D CAD model dataset structured around the SSR (Sketch, Sketch-based feature, and Refinements) triple design paradigm. This dataset encompasses a wide range of CAD commands, thereby aligning effectively with industrial application requirements and proving suitable for the generation of LLMs. Extensive experiments validate the effectiveness of Seek-CAD under various metrics."
      ]
    },
    {
      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",
      "source": "Crossref / Proceedings of the AAAI Conference on Artificial Intelligence",
      "year": 2025,
      "date": "2025-4-11",
      "url": "https://doi.org/10.1609/aaai.v39i5.32515",
      "doi": "10.1609/aaai.v39i5.32515",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Jianwei Guo",
        "Jinglu Chen",
        "Dong-Ming Yan"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing.</jats:p>"
      ]
    },
    {
      "title": "Revisiting CAD Model Generation by Learning Raster Sketch",
      "source": "arXiv",
      "year": 2025,
      "date": "2025-03-02T15:11:35Z",
      "url": "http://arxiv.org/abs/2503.00928v1",
      "doi": "",
      "authors": [
        "Pu Li",
        "Wenhao Zhang",
        "Jianwei Guo",
        "Jinglu Chen",
        "Dong-Ming Yan"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "The integration of deep generative networks into generating Computer-Aided Design (CAD) models has garnered increasing attention over recent years. Traditional methods often rely on discrete sequences of parametric line/curve segments to represent sketches. Differently, we introduce RECAD, a novel framework that generates Raster sketches and 3D Extrusions for CAD models. Representing sketches as raster images offers several advantages over discrete sequences: 1) it breaks the limitations on the types and numbers of lines/curves, providing enhanced geometric representation capabilities; 2) it enables interpolation within a continuous latent space; and 3) it allows for more intuitive user control over the output. Technically, RECAD employs two diffusion networks: the first network generates extrusion boxes conditioned on the number and types of extrusions, while the second network produces sketch images conditioned on these extrusion boxes. By combining these two networks, RECAD effectively generates sketch-and-extrude CAD models, offering a more robust and intuitive approach to CAD model generation. Experimental results indicate that RECAD achieves strong performance in unconditional generation, while also demonstrating effectiveness in conditional generation and output editing."
      ]
    },
    {
      "title": "CadVLM: Bridging Language and Vision in the Generation of Parametric CAD Sketches",
      "source": "arXiv",
      "year": 2024,
      "date": "2024-09-26T01:22:29Z",
      "url": "http://arxiv.org/abs/2409.17457v1",
      "doi": "",
      "authors": [
        "Sifan Wu",
        "Amir Khasahmadi",
        "Mor Katz",
        "Pradeep Kumar Jayaraman",
        "Yewen Pu",
        "Karl Willis",
        "Bang Liu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Parametric Computer-Aided Design (CAD) is central to contemporary mechanical design. However, it encounters challenges in achieving precise parametric sketch modeling and lacks practical evaluation metrics suitable for mechanical design. We harness the capabilities of pre-trained foundation models, renowned for their successes in natural language processing and computer vision, to develop generative models specifically for CAD. These models are adept at understanding complex geometries and design reasoning, a crucial advancement in CAD technology. In this paper, we propose CadVLM, an end-to-end vision language model for CAD generation. Our approach involves adapting pre-trained foundation models to manipulate engineering sketches effectively, integrating both sketch primitive sequences and sketch images. Extensive experiments demonstrate superior performance on multiple CAD sketch generation tasks such as CAD autocompletion, CAD autoconstraint, and image conditional generation. To our knowledge, this is the first instance of a multimodal Large Language Model (LLM) being successfully applied to parametric CAD generation, representing a pioneering step in the field of computer-aided mechanical design."
      ]
    },
    {
      "title": "Large Language Models for Computer-Aided Design Fine Tuned: Dataset and Experiments",
      "source": "OpenAlex",
      "year": 2025,
      "date": "2025-01-23",
      "url": "https://doi.org/10.1115/1.4067713",
      "doi": "10.1115/1.4067713",
      "authors": [
        "Yuewan Sun",
        "Xinggang Li",
        "Zhenghui Sha"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Despite the power of large language models (LLMs) in various cross-modal generation tasks, their ability to generate 3D computer-aided design (CAD) models from text remains underexplored due to the scarcity of suitable datasets. Additionally, there is a lack of multimodal CAD datasets that include both reconstruction parameters and text descriptions, which are essential for the quantitative evaluation of the CAD generation capabilities of multimodal LLMs. To address these challenges, we developed a dataset of CAD models, sketches, and image data for representative mechanical components such as gears, shafts, and springs, along with natural language descriptions collected via Amazon Mechanical Turk. By using CAD programs as a bridge, we facilitate the conversion of textual output from LLMs into precise 3D CAD designs. To enhance the text-to-CAD generation capabilities of GPT models and demonstrate the utility of our dataset, we developed a pipeline to generate fine-tuning training data for GPT-3.5. We fine-tuned four GPT-3.5 models with various data sampling strategies based on the length of a CAD program. We evaluated these models using parsing rate and intersection over union (IoU) metrics, comparing their performance to that of GPT-4 without fine-tuning. The new knowledge gained from the comparative study on the four different fine-tuned models provided us with guidance on the selection of sampling strategies to build training datasets in fine-tuning practices of LLMs for text-to-CAD generation, considering the trade-off between part complexity, model performance, and cost."
      ]
    },
    {
      "title": "GridFormer: Point-Grid Transformer for Surface Reconstruction",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-03-24",
      "url": "https://doi.org/10.1609/aaai.v38i4.28100",
      "doi": "10.1609/aaai.v38i4.28100",
      "authors": [
        "Shengtao Li",
        "Ge Gao",
        "Yudong Liu",
        "Yu-Shen Liu",
        "Ming Gu"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Implicit neural networks have emerged as a crucial technology in 3D surface reconstruction. To reconstruct continuous surfaces from discrete point clouds, encoding the input points into regular grid features (plane or volume) has been commonly employed in existing approaches. However, these methods typically use the grid as an index for uniformly scattering point features. Compared with the irregular point features, the regular grid features may sacrifice some reconstruction details but improve efficiency. To take full advantage of these two types of features, we introduce a novel and high-efficiency attention mechanism between the grid and point features named Point-Grid Transformer (GridFormer). This mechanism treats the grid as a transfer point connecting the space and point cloud. Our method maximizes the spatial expressiveness of grid features and maintains computational efficiency. Furthermore, optimizing predictions over the entire space could potentially result in blurred boundaries. To address this issue, we further propose a boundary optimization strategy incorporating margin binary cross-entropy loss and boundary sampling. This approach enables us to achieve a more precise representation of the object structure. Our experiments validate that our method is effective and outperforms the state-of-the-art approaches under widely used benchmarks by producing more precise geometry reconstructions. The code is available at https://github.com/list17/GridFormer."
      ]
    },
    {
      "title": "Reference-based Image Composition with Sketch via Structure-aware Diffusion Model",
      "source": "arXiv",
      "year": 2023,
      "date": "2023-03-31T06:12:58Z",
      "url": "http://arxiv.org/abs/2304.09748v1",
      "doi": "",
      "authors": [
        "Kangyeol Kim",
        "Sunghyun Park",
        "Junsoo Lee",
        "Jaegul Choo"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Recent remarkable improvements in large-scale text-to-image generative models have shown promising results in generating high-fidelity images. To further enhance editability and enable fine-grained generation, we introduce a multi-input-conditioned image composition model that incorporates a sketch as a novel modal, alongside a reference image. Thanks to the edge-level controllability using sketches, our method enables a user to edit or complete an image sub-part with a desired structure (i.e., sketch) and content (i.e., reference image). Our framework fine-tunes a pre-trained diffusion model to complete missing regions using the reference image while maintaining sketch guidance. Albeit simple, this leads to wide opportunities to fulfill user needs for obtaining the in-demand images. Through extensive experiments, we demonstrate that our proposed method offers unique use cases for image manipulation, enabling user-driven modifications of arbitrary scenes."
      ]
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "<jats:p>&lt;div class=\"section abstract\"&gt;&lt;div class=\"htmlview paragraph\"&gt;LiDAR sensors are common in automated driving due to their high accuracy. However, LiDAR processing algorithm development suffers from lack of diverse training data, partly due to sensors’ high cost and rapid development cycles. Public datasets (e.g. KITTI) offer poor coverage of edge cases, whereas these samples are essential for safer self-driving. We address the unmet need for abundant, high-quality LiDAR data with the development of a synthetic LiDAR point cloud generation tool and validate this tool’s performance using the KITTI-trained PIXOR object detection model. The tool uses a single camera raycasting process and filtering techniques to generate segmented and annotated class specific datasets. This approach will support low-cost bulk generation of accurate data for training advanced selfdriving algorithms, with configurability to simulate existing and upcoming LiDAR configurations possessing varied channels, range, vertical and horizontal fields of view, and angular resolution. In comparison with virtual LiDAR solutions like CARLA [1], this tool requires no game development knowledge and is faster to set up: sensor customization can be done in a front-end panel enabling users to focus more on data generation. The simulator is developed using the Unity Game Engine in conjunction with free and open-source assets, and a build will be shared with the AV community before an open-source release.&lt;/div&gt;&lt;/div&gt;</jats:p>"
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
      "CAD model reconstruction recent",
      "boundary representation generation survey",
      "3D solid model from data deep learning"
    ],
    "effective_query": "B-rep generation from point cloud deep learning",
    "used_override_query": false,
    "executed_queries": [
      "B-rep generation from point cloud deep learning",
      "boundary representation reconstruction neural network",
      "CAD model generation from sketch or image"
    ],
    "fallback_used": false
  }
}
```

### Message 6

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=6

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval output contains several relevant papers on CAD/B-rep generation from the last five years, but it fails to meet key hard requirements. Most critically, the set lacks sufficient papers that directly target B-rep generation from point clouds or scans, which was a prioritized input modality. Several papers focus on sketch, text, or image inputs, and one paper (GridFormer) is about general surface reconstruction, not B-rep. The evidence snippets are insufficient to confirm that the papers output B-rep as a primary target, and the candidate depth is borderline. The set does not reflect the user's explicit constraint to rank general B-rep generation papers first while highlighting strong point-cloud methods.",
  "scores": {
    "coverage_score": 1,
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
      "passed": false,
      "reason": "After merging duplicates, only 8 unique candidate papers remain. The requirement is at least 5, which is met, but the depth is borderline for the requested 8-10 range and several are not core B-rep generation."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only 1-2 are clearly aligned with the user's topic of B-rep generation/reconstruction as a primary target. Papers like 'GridFormer' are about surface reconstruction (likely mesh/implicit), not B-rep. 'Reference-based Image Composition with Sketch' is about image editing, not CAD/B-rep generation. 'End-to-End Synthetic LiDAR Point Cloud Data Generation' is about data generation for object detection, not B-rep reconstruction."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly requested to prioritize papers that generate/reconstruct B-rep, with a secondary emphasis on point-cloud/scanned-data inputs. The retrieved set is skewed towards sketch, text, and image inputs, with only one paper (Brep2Seq) mentioning point cloud reconstruction in its abstract. The set does not reflect the ranking instruction to put general B-rep generation first and highlight point-cloud methods."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 retained papers must plausibly look like core candidates for B-rep generation. Based on evidence snippets, only Brep2Seq, CAD-MLLM, and Seek-CAD appear to target parametric CAD/B-rep generation. RECAD and CadVLM focus on sketches, which may be a step towards B-rep but are not confirmed to output full B-rep models. The others are not core B-rep generation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the resolved time range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is an obvious missing core subtopic: B-rep generation specifically from point clouds or scans. The retrieval over-relies on sketch/text/image methods and includes off-topic papers (surface reconstruction, image composition, LiDAR data generation)."
    }
  },
  "key_risks": [
    "The evidence snippets are at the abstract level and may not confirm that the papers output B-rep (vs. procedural sequences or intermediate sketches).",
    "The set is missing key recent works on point-cloud to B-rep reconstruction, which is a major frontier area.",
    "Several papers may be about generating CAD command sequences or sketches, not the B-rep geometry itself, which the user wanted to exclude."
  ],
  "next_actions": [
    "Execute a targeted search for 'point cloud to B-rep reconstruction 2022 2023 2024 2025' using Crossref and OpenAlex to fill the major gap.",
    "Search for 'boundary representation generation from scan' or 'CAD model reconstruction from point cloud' to capture scan-based methods.",
    "Verify the core contribution of candidate papers like RECAD and CadVLM by retrieving full abstracts or introductions to confirm they output B-rep models, not just sketches or command sequences."
  ]
}
```

### Message 7

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep generation, reconstruction, and recovery from point clouds, scans, and multimodal inputs, queries=3, years=2022-2026

```text
{
  "topic": "B-rep generation, reconstruction, and recovery from point clouds, scans, and multimodal inputs",
  "user_intent": "Identify frontier research (2022-2026) on methods that directly generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output, with a strong emphasis on general B-rep generation techniques and a prioritized focus on point-cloud/scan-based inputs.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-25",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep generation from point clouds", "B-rep reconstruction from 3D scans", "CAD model recovery from LiDAR", "boundary representation synthesis from multimodal data", "structured solid model generation"],
  "exclude_areas": ["CAD operation sequence reconstruction", "sketch or command sequence generation without B-rep output", "mesh or implicit surface reconstruction not producing B-rep", "LiDAR data generation for object detection"],
  "fallback_queries": ["CAD model from point cloud reconstruction", "boundary representation generation recent", "3D scan to CAD model deep learning"],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction 2023 2024",
      "reason": "Directly targets the highest-priority gap identified by the reviewer: B-rep generation specifically from point clouds/scans within the core time range."
    },
    {
      "query": "CAD model reconstruction from scan deep learning",
      "reason": "Broadens the search for scan-based methods that output CAD/B-rep models, using terminology common in literature."
    },
    {
      "query": "boundary representation generation from point cloud",
      "reason": "Uses precise terminology ('boundary representation') to find papers that explicitly target B-rep output from point cloud data."
    }
  ],
  "assumptions": ["The term 'B-rep generation' may be synonymous with 'CAD model reconstruction' or 'solid model recovery' in relevant papers.", "Papers that generate parametric CAD models via sketches or text are considered relevant if they ultimately produce a B-rep, but point-cloud-based methods are the primary target for this retrieval round.", "If evidence is insufficient to confirm B-rep output, the paper will be considered lower priority."],
  "success_criteria": ["Retrieve at least 3-5 new papers where the primary contribution is B-rep generation/reconstruction from point clouds or 3D scans.", "Verify that candidate papers output B-rep geometry, not just intermediate representations like command sequences.", "Build a candidate set that allows ranking general B-rep generation papers first while highlighting strong point-cloud methods."]
}
```

### Message 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 1 tool call(s): retrieve_candidates_from_plan

```text
FunctionCall(id='call_00_iKe16xHqYt5VnAGizZCyK5rh', arguments='{"top_k": 10, "max_results_per_source": 20, "query": "point cloud to B-rep reconstruction 2023 2024"}', name='retrieve_candidates_from_plan')
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 1 tool call(s): retrieve_candidates_from_plan

```text
content='{\n  "sources_used": [\n    "Crossref",\n    "OpenAlex",\n    "arXiv"\n  ],\n  "queries_executed": [\n    {\n      "query": "point cloud to B-rep reconstruction 2023 2024",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "CAD model reconstruction from scan deep learning",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    },\n    {\n      "query": "boundary representation generation from point cloud",\n      "sources": [\n        "arXiv",\n        "Crossref",\n        "OpenAlex"\n      ],\n      "notes": "Planner query executed in the primary retrieval phase."\n    }\n  ],\n  "papers": [\n    {\n      "title": "Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-12-28",\n      "url": "https://doi.org/10.1093/jcde/qwae005",\n      "doi": "10.1093/jcde/qwae005",\n      "authors": [\n        "Shuming Zhang",\n        "Zhidong Guan",\n        "Hao Jiang",\n        "Ning Tao",\n        "Xiaodong Wang",\n        "Pingan Tan"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."\n      ]\n    },\n    {\n      "title": "CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM",\n      "source": "arXiv",\n      "year": 2024,\n      "date": "2024-11-07T18:31:08Z",\n      "url": "http://arxiv.org/abs/2411.04954v3",\n      "doi": "",\n      "authors": [\n        "Jingwei Xu",\n        "Chenyu Wang",\n        "Zibo Zhao",\n        "Wen Liu",\n        "Yi Ma",\n        "Shenghua Gao"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user\'s inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models\' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/"\n      ]\n    },\n    {\n      "title": "BPNet: Bézier Primitive Segmentation on 3D Point Clouds",\n      "source": "OpenAlex",\n      "year": 2023,\n      "date": "2023-08-01",\n      "url": "https://doi.org/10.24963/ijcai.2023/84",\n      "doi": "10.24963/ijcai.2023/84",\n      "authors": [\n        "Rao Fu",\n        "Wen Cheng",\n        "Qian Li",\n        "Xiao Xiao",\n        "Pierre Alliez"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "This paper proposes BPNet, a novel end-to-end deep learning framework to learn Bézier primitive segmentation on 3D point clouds. The existing works treat different primitive types separately, thus limiting them to finite shape categories. To address this issue, we seek a generalized primitive segmentation on point clouds. Taking inspiration from Bézier decomposition on NURBS models, we transfer it to guide point cloud segmentation casting off primitive types. A joint optimization framework is proposed to learn Bézier primitive segmentation and geometric fitting simultaneously on a cascaded architecture. Specifically, we introduce a soft voting regularizer to improve primitive segmentation and propose an auto-weight embedding module to cluster point features, making the network more robust and generic. We also introduce a reconstruction module where we successfully process multiple CAD models with different primitives simultaneously. We conducted extensive experiments on the synthetic ABC dataset and real-scan datasets to validate and compare our approach with different baseline methods. Experiments show superior performance over previous work in terms of segmentation, with a substantially faster inference speed."\n      ]\n    },\n    {\n      "title": "Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-10-18",\n      "url": "https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024",\n      "doi": "10.5194/isprs-annals-x-4-2024-287-2024",\n      "authors": [\n        "O. V. Roman",\n        "G. Mazzacca",\n        "Elisa Mariarosaria Farella",\n        "Fabio Remondino",\n        "Maarten Bassier",\n        "Giorgio Agugiaro"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Abstract. In many countries, recent boosts in the construction and renovation sectors and energy efficiency directives are driving a growing interest in the built environment among designers and maintainers. In this context, customized software solutions tailored for Building Information Modelling (BIM) and Building Energy Modelling (BEM) are proving to be indispensable for optimizing operational efficiency within the Architecture, Engineering, Construction, Owner, and Operator (AECOO) sector and for facilitating the generation of buildings\' Digital Twins (DTs). These DTs rely on accurate geometry and ancillary information (semantics, sensors, etc.) to define properties of single elements, enabling crucial simulations in structural conditions or energy needs. However, BIM and BEM model creation and their enrichment with semantic information are highly time-consuming and prone to manual errors. Hence, there is an increasing demand for automatic methods featuring a high level of geometric accuracy to reconstruct building elements, such as walls, floors, and openings captured via 3D reality-based surveying. This paper introduces an automated method for creating Boundary Representation (B-Rep) models from 3D surveying data for the generation of digital building replicas. The method is based on the detection and computation of topological elements from 3D reality-based point clouds. It proves valuable for architectural or design workflows and for conducting energy or quality system simulations."\n      ]\n    },\n    {\n      "title": "Topology-Aware Flow-Based Point Cloud Generation",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-06-08",\n      "url": "https://doi.org/10.1109/tcsvt.2022.3181212",\n      "doi": "10.1109/tcsvt.2022.3181212",\n      "authors": [\n        "Takumi Kimura",\n        "Takashi Matsubara",\n        "Kuniaki Uehara"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Point clouds have attracted attention as a representation of an object’s surface. Deep generative models have typically used a continuous map from a dense set in a latent space to express their variations. However, a continuous map cannot adequately express the varying numbers of holes. That is, previous approaches disregarded the topological structure of point clouds. Furthermore, a point cloud comprises several subparts, making it difficult to express it using a continuous map. This paper proposes ChartPointFlow, a flow-based deep generative model that forms a map conditioned on a label. Similar to a manifold chart, a map conditioned on a label is assigned to a continuous subset of a point cloud. Thus, ChartPointFlow is able to maintain the topological structure with clear boundaries and holes, whereas previous approaches generated blurry point clouds with fuzzy holes. The experimental results show that ChartPointFlow achieves state-of-the-art performance in various tasks, including generation, reconstruction, upsampling, and segmentation."\n      ]\n    },\n    {\n      "title": "Masked Clustering Prediction for Unsupervised Point Cloud Pre-training",\n      "source": "arXiv",\n      "year": 2025,\n      "date": "2025-08-12T12:58:44Z",\n      "url": "http://arxiv.org/abs/2508.08910v1",\n      "doi": "",\n      "authors": [\n        "Bin Ren",\n        "Xiaoshui Huang",\n        "Mengyuan Liu",\n        "Hong Liu",\n        "Fabio Poiesi",\n        "Nicu Sebe",\n        "Guofeng Mei"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Vision transformers (ViTs) have recently been widely applied to 3D point cloud understanding, with masked autoencoding as the predominant pre-training paradigm. However, the challenge of learning dense and informative semantic features from point clouds via standard ViTs remains underexplored. We propose MaskClu, a novel unsupervised pre-training method for ViTs on 3D point clouds that integrates masked point modeling with clustering-based learning. MaskClu is designed to reconstruct both cluster assignments and cluster centers from masked point clouds, thus encouraging the model to capture dense semantic information. Additionally, we introduce a global contrastive learning mechanism that enhances instance-level feature learning by contrasting different masked views of the same point cloud. By jointly optimizing these complementary objectives, i.e., dense semantic reconstruction, and instance-level contrastive learning. MaskClu enables ViTs to learn richer and more semantically meaningful representations from 3D point clouds. We validate the effectiveness of our method via multiple 3D tasks, including part segmentation, semantic segmentation, object detection, and classification, where MaskClu sets new competitive results. The code and models will be released at:https://github.com/Amazingren/maskclu."\n      ]\n    },\n    {\n      "title": "Semantic Enrichment of Architectural Heritage Point Clouds Using Artificial Intelligence: The Palacio de Sástago in Zaragoza, Spain",\n      "source": "OpenAlex",\n      "year": 2024,\n      "date": "2024-12-09",\n      "url": "https://doi.org/10.3390/heritage7120321",\n      "doi": "10.3390/heritage7120321",\n      "authors": [\n        "Michele Buldo",\n        "Luis Agustín Hernández",\n        "Cesare Verdoscia"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "In the current landscape dominated by Artificial Intelligence, the integration of Machine Learning and Deep Learning within the realm of Cultural Heritage, particularly within architectural contexts, is paramount for the efficient processing and interpretation of point clouds. These advanced methods facilitate automated segmentation and classification, significantly improving both the clarity and practical use of data acquired from laser scanning and photogrammetry. The present study investigates the Palacio de Sástago—a prominent Renaissance palace in Zaragoza, Spain—and introduces a cutting-edge modus operandi for the automated recognition of architectural elements within the palace’s inner courtyard. Employing the well-established Random Forest algorithm, implemented in a Python environment, the framework begins with a comprehensive evaluation of the geometric features identified in the LiDAR point cloud. This process employs the Mean Decrease in Impurity metric to evaluate the relevance of each variable. To boost the accuracy and efficiency of the final classifications, the features are refined post-assessment, enhancing both the training phase and the algorithm’s later evaluation. The research’s findings demonstrate significant potential, supporting advancements in CAD systems and HBIM that will enable more precise, automated modelling of architectural elements, thereby enhancing the accuracy of digital reconstructions and improving conservation planning for heritage sites."\n      ]\n    },\n    {\n      "title": "Simurgh: A Framework for Cad-Driven Deep Learning Based X-Ray CT Reconstruction",\n      "source": "OpenAlex",\n      "year": 2022,\n      "date": "2022-10-16",\n      "url": "https://doi.org/10.1109/icip46576.2022.9898017",\n      "doi": "10.1109/icip46576.2022.9898017",\n      "authors": [\n        "Amirkoushyar Ziabari",\n        "Singanallur Venkatakrishnan",\n        "Abhishek Dubey",\n        "Alex Lisovich",\n        "Paul Brackman",\n        "Curtis Frederick",\n        "Pradeep Bhattad",\n        "Philip R. Bingham"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "High-resolution X-ray computed tomography (XCT) is an important technique for the inspection of additively manufactured (AM) parts. While XCT is typically used off-line to inspect a subset of manufactured parts, significantly accelerating measurement speed while retaining accuracy would enable use of XCT for in-line inspection to rapidly identify defects in each part as it is manufactured. Here, we propose a deep learning (DL) based approach that uses computer aided design (CAD) models of the AM parts and physics-based information to rapidly produce high-quality reconstructions from sparse XCT measurements without high quality ground truth data. Our approach uses a generative adversarial neural network (GAN) to produced realistic training data from the CAD-based simulations and a deep neural network that is trained using data from the first stage to produce accurate 3D reconstructions. Using experimental XCT data of metal parts, we demonstrate enhanced defect detection capabilities while dramatically reducing the scan time."\n      ]\n    },\n    {\n      "title": "Neural Point Cloud Diffusion for Disentangled 3D Shape and Appearance Generation",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-12-21T18:46:27Z",\n      "url": "http://arxiv.org/abs/2312.14124v2",\n      "doi": "",\n      "authors": [\n        "Philipp Schröppel",\n        "Christopher Wewer",\n        "Jan Eric Lenssen",\n        "Eddy Ilg",\n        "Thomas Brox"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Controllable generation of 3D assets is important for many practical applications like content creation in movies, games and engineering, as well as in AR/VR. Recently, diffusion models have shown remarkable results in generation quality of 3D objects. However, none of the existing models enable disentangled generation to control the shape and appearance separately. For the first time, we present a suitable representation for 3D diffusion models to enable such disentanglement by introducing a hybrid point cloud and neural radiance field approach. We model a diffusion process over point positions jointly with a high-dimensional feature space for a local density and radiance decoder. While the point positions represent the coarse shape of the object, the point features allow modeling the geometry and appearance details. This disentanglement enables us to sample both independently and therefore to control both separately. Our approach sets a new state of the art in generation compared to previous disentanglement-capable methods by reduced FID scores of 30-90% and is on-par with other non disentanglement-capable state-of-the art methods."\n      ]\n    },\n    {\n      "title": "$PC^2$: Projection-Conditioned Point Cloud Diffusion for Single-Image 3D Reconstruction",\n      "source": "arXiv",\n      "year": 2023,\n      "date": "2023-02-21T13:37:07Z",\n      "url": "http://arxiv.org/abs/2302.10668v2",\n      "doi": "",\n      "authors": [\n        "Luke Melas-Kyriazi",\n        "Christian Rupprecht",\n        "Andrea Vedaldi"\n      ],\n      "verification_status": "partial",\n      "evidence_level": "abstract",\n      "time_range_status": "in_range",\n      "evidence_snippets": [\n        "Reconstructing the 3D shape of an object from a single RGB image is a long-standing and highly challenging problem in computer vision. In this paper, we propose a novel method for single-image 3D reconstruction which generates a sparse point cloud via a conditional denoising diffusion process. Our method takes as input a single RGB image along with its camera pose and gradually denoises a set of 3D points, whose positions are initially sampled randomly from a three-dimensional Gaussian distribution, into the shape of an object. The key to our method is a geometrically-consistent conditioning process which we call projection conditioning: at each step in the diffusion process, we project local image features onto the partially-denoised point cloud from the given camera pose. This projection conditioning process enables us to generate high-resolution sparse geometries that are well-aligned with the input image, and can additionally be used to predict point colors after shape reconstruction. Moreover, due to the probabilistic nature of the diffusion process, our method is naturally capable of generating multiple different shapes consistent with a single input image. In contrast to prior work, our approach not only performs well on synthetic benchmarks, but also gives large qualitative improvements on complex real-world data."\n      ]\n    }\n  ],\n  "dedup_notes": [\n    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 7 duplicate entries were merged."\n  ],\n  "missing_metadata": [\n    "Title-only candidates remain weak until abstract or excerpt evidence is available."\n  ],\n  "coverage_gaps": [],\n  "source_errors": [],\n  "planner_query_source": {\n    "fallback_queries": [\n      "CAD model from point cloud reconstruction",\n      "boundary representation generation recent",\n      "3D scan to CAD model deep learning"\n    ],\n    "effective_query": "point cloud to B-rep reconstruction 2023 2024",\n    "used_override_query": true,\n    "executed_queries": [\n      "point cloud to B-rep reconstruction 2023 2024",\n      "CAD model reconstruction from scan deep learning",\n      "boundary representation generation from point cloud"\n    ],\n    "fallback_used": false\n  }\n}' name='retrieve_candidates_from_plan' call_id='call_00_iKe16xHqYt5VnAGizZCyK5rh' is_error=False
```

### Message 10

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
      "query": "point cloud to B-rep reconstruction 2023 2024",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "CAD model reconstruction from scan deep learning",
      "sources": [
        "arXiv",
        "Crossref",
        "OpenAlex"
      ],
      "notes": "Planner query executed in the primary retrieval phase."
    },
    {
      "query": "boundary representation generation from point cloud",
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
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract Three-dimensional (3D) reconstruction is a significant research topic in the field of computer-aided design (CAD), which is used to recover editable CAD models from original shapes, including point clouds, voxels, meshes, and boundary representations (B-rep). Recently, there has been considerable research interest in deep model generation due to the increasing potential of deep learning methods. To address the challenges of 3D reconstruction and generation, we propose Brep2Seq, a novel deep neural network designed to transform the B-rep model into a sequence of editable parametrized feature-based modeling operations comprising principal primitives and detailed features. Brep2Seq employs an encoder-decoder architecture based on the transformer, leveraging geometry and topological information within B-rep models to extract the feature representation of the original 3D shape. Due to its hierarchical network architecture and training strategy, Brep2Seq achieved improved model reconstruction and controllable model generation by distinguishing between the primary shape and detailed features of CAD models. To train Brep2Seq, a large-scale dataset comprising 1 million CAD designs is established through an automatic geometry synthesis method. Extensive experiments on both DeepCAD and Fusion 360 datasets demonstrate the effectiveness of Brep2Seq, and show its applicability to simple mechanical components in real-world scenarios. We further apply Brep2Seq to various downstream applications, including point cloud reconstruction, model interpolation, shape constraint generation, and CAD feature recognition."
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
      "title": "BPNet: Bézier Primitive Segmentation on 3D Point Clouds",
      "source": "OpenAlex",
      "year": 2023,
      "date": "2023-08-01",
      "url": "https://doi.org/10.24963/ijcai.2023/84",
      "doi": "10.24963/ijcai.2023/84",
      "authors": [
        "Rao Fu",
        "Wen Cheng",
        "Qian Li",
        "Xiao Xiao",
        "Pierre Alliez"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "This paper proposes BPNet, a novel end-to-end deep learning framework to learn Bézier primitive segmentation on 3D point clouds. The existing works treat different primitive types separately, thus limiting them to finite shape categories. To address this issue, we seek a generalized primitive segmentation on point clouds. Taking inspiration from Bézier decomposition on NURBS models, we transfer it to guide point cloud segmentation casting off primitive types. A joint optimization framework is proposed to learn Bézier primitive segmentation and geometric fitting simultaneously on a cascaded architecture. Specifically, we introduce a soft voting regularizer to improve primitive segmentation and propose an auto-weight embedding module to cluster point features, making the network more robust and generic. We also introduce a reconstruction module where we successfully process multiple CAD models with different primitives simultaneously. We conducted extensive experiments on the synthetic ABC dataset and real-scan datasets to validate and compare our approach with different baseline methods. Experiments show superior performance over previous work in terms of segmentation, with a substantially faster inference speed."
      ]
    },
    {
      "title": "Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-10-18",
      "url": "https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024",
      "doi": "10.5194/isprs-annals-x-4-2024-287-2024",
      "authors": [
        "O. V. Roman",
        "G. Mazzacca",
        "Elisa Mariarosaria Farella",
        "Fabio Remondino",
        "Maarten Bassier",
        "Giorgio Agugiaro"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Abstract. In many countries, recent boosts in the construction and renovation sectors and energy efficiency directives are driving a growing interest in the built environment among designers and maintainers. In this context, customized software solutions tailored for Building Information Modelling (BIM) and Building Energy Modelling (BEM) are proving to be indispensable for optimizing operational efficiency within the Architecture, Engineering, Construction, Owner, and Operator (AECOO) sector and for facilitating the generation of buildings' Digital Twins (DTs). These DTs rely on accurate geometry and ancillary information (semantics, sensors, etc.) to define properties of single elements, enabling crucial simulations in structural conditions or energy needs. However, BIM and BEM model creation and their enrichment with semantic information are highly time-consuming and prone to manual errors. Hence, there is an increasing demand for automatic methods featuring a high level of geometric accuracy to reconstruct building elements, such as walls, floors, and openings captured via 3D reality-based surveying. This paper introduces an automated method for creating Boundary Representation (B-Rep) models from 3D surveying data for the generation of digital building replicas. The method is based on the detection and computation of topological elements from 3D reality-based point clouds. It proves valuable for architectural or design workflows and for conducting energy or quality system simulations."
      ]
    },
    {
      "title": "Topology-Aware Flow-Based Point Cloud Generation",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-06-08",
      "url": "https://doi.org/10.1109/tcsvt.2022.3181212",
      "doi": "10.1109/tcsvt.2022.3181212",
      "authors": [
        "Takumi Kimura",
        "Takashi Matsubara",
        "Kuniaki Uehara"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "Point clouds have attracted attention as a representation of an object’s surface. Deep generative models have typically used a continuous map from a dense set in a latent space to express their variations. However, a continuous map cannot adequately express the varying numbers of holes. That is, previous approaches disregarded the topological structure of point clouds. Furthermore, a point cloud comprises several subparts, making it difficult to express it using a continuous map. This paper proposes ChartPointFlow, a flow-based deep generative model that forms a map conditioned on a label. Similar to a manifold chart, a map conditioned on a label is assigned to a continuous subset of a point cloud. Thus, ChartPointFlow is able to maintain the topological structure with clear boundaries and holes, whereas previous approaches generated blurry point clouds with fuzzy holes. The experimental results show that ChartPointFlow achieves state-of-the-art performance in various tasks, including generation, reconstruction, upsampling, and segmentation."
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
    },
    {
      "title": "Semantic Enrichment of Architectural Heritage Point Clouds Using Artificial Intelligence: The Palacio de Sástago in Zaragoza, Spain",
      "source": "OpenAlex",
      "year": 2024,
      "date": "2024-12-09",
      "url": "https://doi.org/10.3390/heritage7120321",
      "doi": "10.3390/heritage7120321",
      "authors": [
        "Michele Buldo",
        "Luis Agustín Hernández",
        "Cesare Verdoscia"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "In the current landscape dominated by Artificial Intelligence, the integration of Machine Learning and Deep Learning within the realm of Cultural Heritage, particularly within architectural contexts, is paramount for the efficient processing and interpretation of point clouds. These advanced methods facilitate automated segmentation and classification, significantly improving both the clarity and practical use of data acquired from laser scanning and photogrammetry. The present study investigates the Palacio de Sástago—a prominent Renaissance palace in Zaragoza, Spain—and introduces a cutting-edge modus operandi for the automated recognition of architectural elements within the palace’s inner courtyard. Employing the well-established Random Forest algorithm, implemented in a Python environment, the framework begins with a comprehensive evaluation of the geometric features identified in the LiDAR point cloud. This process employs the Mean Decrease in Impurity metric to evaluate the relevance of each variable. To boost the accuracy and efficiency of the final classifications, the features are refined post-assessment, enhancing both the training phase and the algorithm’s later evaluation. The research’s findings demonstrate significant potential, supporting advancements in CAD systems and HBIM that will enable more precise, automated modelling of architectural elements, thereby enhancing the accuracy of digital reconstructions and improving conservation planning for heritage sites."
      ]
    },
    {
      "title": "Simurgh: A Framework for Cad-Driven Deep Learning Based X-Ray CT Reconstruction",
      "source": "OpenAlex",
      "year": 2022,
      "date": "2022-10-16",
      "url": "https://doi.org/10.1109/icip46576.2022.9898017",
      "doi": "10.1109/icip46576.2022.9898017",
      "authors": [
        "Amirkoushyar Ziabari",
        "Singanallur Venkatakrishnan",
        "Abhishek Dubey",
        "Alex Lisovich",
        "Paul Brackman",
        "Curtis Frederick",
        "Pradeep Bhattad",
        "Philip R. Bingham"
      ],
      "verification_status": "partial",
      "evidence_level": "abstract",
      "time_range_status": "in_range",
      "evidence_snippets": [
        "High-resolution X-ray computed tomography (XCT) is an important technique for the inspection of additively manufactured (AM) parts. While XCT is typically used off-line to inspect a subset of manufactured parts, significantly accelerating measurement speed while retaining accuracy would enable use of XCT for in-line inspection to rapidly identify defects in each part as it is manufactured. Here, we propose a deep learning (DL) based approach that uses computer aided design (CAD) models of the AM parts and physics-based information to rapidly produce high-quality reconstructions from sparse XCT measurements without high quality ground truth data. Our approach uses a generative adversarial neural network (GAN) to produced realistic training data from the CAD-based simulations and a deep neural network that is trained using data from the first stage to produce accurate 3D reconstructions. Using experimental XCT data of metal parts, we demonstrate enhanced defect detection capabilities while dramatically reducing the scan time."
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
    }
  ],
  "dedup_notes": [
    "Retrieved papers were deduplicated by DOI, URL, or normalized title; 7 duplicate entries were merged."
  ],
  "missing_metadata": [
    "Title-only candidates remain weak until abstract or excerpt evidence is available."
  ],
  "coverage_gaps": [],
  "source_errors": [],
  "planner_query_source": {
    "fallback_queries": [
      "CAD model from point cloud reconstruction",
      "boundary representation generation recent",
      "3D scan to CAD model deep learning"
    ],
    "effective_query": "point cloud to B-rep reconstruction 2023 2024",
    "used_override_query": true,
    "executed_queries": [
      "point cloud to B-rep reconstruction 2023 2024",
      "CAD model reconstruction from scan deep learning",
      "boundary representation generation from point cloud"
    ],
    "fallback_used": false
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
  "review_summary": "The retrieval output shows improved coverage of point-cloud-related papers, but it still fails to meet several hard requirements. While the set includes more papers mentioning point clouds, most are not about B-rep generation. Key papers like BPNet, Topology-Aware Flow-Based Point Cloud Generation, Masked Clustering Prediction, Neural Point Cloud Diffusion, and PC^2 are about point cloud generation, segmentation, or reconstruction to point clouds/meshes, not to B-rep or CAD models. The evidence snippets do not confirm B-rep output. Only Brep2Seq and the BIM/BEM paper explicitly mention B-rep, and CAD-MLLM mentions parametric CAD. The candidate depth is insufficient for core B-rep generation, and the relevance is weak. The set does not satisfy the user's intent for frontier research on B-rep generation from point clouds.",
  "scores": {
    "coverage_score": 1,
    "relevance_score": 0,
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
      "passed": false,
      "reason": "After merging duplicates, there are 10 unique candidates, but most are not about B-rep generation. The effective depth of relevant papers is far below 5."
    },
    "relevance": {
      "passed": false,
      "reason": "Among the top candidates, only Brep2Seq and 'Towards Automated BIM and BEM Model Generation using a B-Rep-based Method' are clearly aligned with B-rep generation. CAD-MLLM may be relevant but its evidence snippet focuses on command sequences. The other 7 papers are about point cloud processing, generation, segmentation, or reconstruction to point clouds/neural fields, not B-rep output."
    },
    "metadata": {
      "passed": true,
      "reason": "Each retained candidate has title, source, year/date, and URL where available."
    },
    "query_fit": {
      "passed": false,
      "reason": "The user explicitly prioritized point-cloud/scan-based inputs for B-rep generation. The retrieved set includes many point cloud papers, but they do not generate B-rep; they generate other representations (point clouds, neural radiance fields, segmentations). The set does not reflect the core requirement of B-rep as the output."
    },
    "core_method_fit": {
      "passed": false,
      "reason": "At least 3 retained papers must plausibly look like core candidates for B-rep generation. Based on evidence snippets, only Brep2Seq and the BIM/BEM paper are clear. CAD-MLLM is ambiguous (may output command sequences). The others are not core B-rep generation."
    },
    "time_consistency": {
      "passed": true,
      "reason": "All papers are from 2022-2026, respecting the resolved time range."
    },
    "gaps": {
      "passed": false,
      "reason": "There is a major evidence hole: the retrieved papers lack confirmation that they output B-rep. The set is over-reliant on point cloud processing papers that are adjacent but not on-topic. Missing are core papers on learning-based B-rep reconstruction from point clouds (e.g., 'Point2CAD', 'DeepCAD', 'BRepNet'-like approaches for generation)."
    }
  },
  "key_risks": [
    "The evidence snippets are abstract-level and do not confirm B-rep output; many papers are likely about point cloud generation or segmentation, not B-rep synthesis.",
    "The retrieval is biased towards point cloud papers in general, not filtering for B-rep as the target representation.",
    "Critical frontier papers on B-rep generation from scans may be missing because the queries are too broad or the terminology mismatch."
  ],
  "next_actions": [
    "Execute a precise search for 'B-rep generation from point cloud' and 'boundary representation reconstruction from scan' using exact phrase matching in titles/abstracts via Crossref and OpenAlex.",
    "Search for known seminal papers in the area (e.g., 'BRepNet', 'Point2CAD', 'DeepCAD') and retrieve their recent citations (2022-2026) to find frontier follow-ups.",
    "Verify the output representation of ambiguous candidates (e.g., CAD-MLLM, BPNet) by retrieving full abstracts or method sections to confirm they produce B-rep geometry, not just command sequences or point labels."
  ]
}
```

### Message 12

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
# Paper Search Report

## Query Understanding
The search aimed to identify frontier research (2022–2026) on methods that generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output. The focus was on general B-rep generation techniques, with a secondary priority on methods using point clouds or scans as input. Papers focused on reconstructing CAD operation sequences, programs, or design history were to be excluded.

## Search Strategy
The search was conducted in two rounds using Crossref, OpenAlex, and arXiv. Initial queries targeted "B-rep generation from point cloud deep learning" and related terms. A second round used more targeted queries like "point cloud to B-rep reconstruction 2023 2024" to address identified gaps. The reviewer assessed the results twice, finding that the retrieved papers largely did not confirm B-rep as the output representation, with many focusing on point cloud processing, segmentation, or other intermediate representations instead of direct B-rep generation.

## Candidate Papers
**The search did not clear the quality bar.** The retrieval process failed to gather a sufficient set of papers where the primary contribution is the generation or reconstruction of a B-rep model, as required. The final set contains mostly adjacent work on point cloud processing or CAD sequence generation.

### Verified Candidates
*Papers with partial or verified evidence of targeting B-rep output.*

*   **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** OpenAlex
    *   **Link:** https://doi.org/10.1093/jcde/qwae005
    *   **Core Contribution:** Proposes a transformer-based encoder-decoder to transform B-rep models into sequences of editable parametric features, with applications including point cloud reconstruction.
    *   **Relevance Note:** Direct match. Explicitly addresses B-rep reconstruction and generation from various inputs, including point clouds.

*   **Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map** (2024)
    *   **Source:** OpenAlex
    *   **Link:** https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024
    *   **Core Contribution:** Introduces an automated method for creating Boundary Representation (B-Rep) models from 3D reality-based point clouds for digital building replicas.
    *   **Relevance Note:** Direct match. Focuses on B-rep generation specifically from scanned point cloud data for architectural applications.

### Unverified Leads
*Title-strong but unverified papers suggested as potential follow-up leads, not as verified recommendations.*

*   **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** (2024)
*   **BPNet: Bézier Primitive Segmentation on 3D Point Clouds** (2023)
*   **Revisiting CAD Model Generation by Learning Raster Sketch** (2025)

## Notes and Gaps
*   **Evidence Gap:** Most retrieved papers only had abstract-level evidence, which was insufficient to confirm that B-rep is the primary output. Many focused on point cloud generation, segmentation, or neural field reconstruction.
*   **Core Topic Gap:** The search failed to retrieve a critical mass of recent papers (2022-2026) whose central contribution is learning-based B-rep reconstruction from point clouds or scans.
*   **Terminology Mismatch:** Queries for "point cloud to B-rep" may not align with the terminology used in relevant literature, which might use phrases like "CAD model reconstruction from scan" or "solid model recovery."
*   **Adjacent Work:** The retrieval was biased towards general point cloud deep learning and CAD sequence generation, which are related but do not satisfy the user's specific requirement for B-rep output.

## Recommended Next Steps
1.  **Precise Phrase Search:** Execute searches using exact phrases like `"boundary representation" reconstruction point cloud` or `"B-rep" generation` in titles and abstracts to filter for papers explicitly targeting B-rep.
2.  **Citation Chaining:** Identify known seminal papers in B-rep learning (e.g., BRepNet, Point2CAD) and search for recent works (2022-2026) that cite them to find frontier follow-ups.
3.  **Venue-Targeted Search:** Focus retrieval on conferences and journals known for CAD/geometry processing research (e.g., CAD, Computer-Aided Design, SGP, SIGGRAPH Asia) to improve relevance.
4.  **Full-Text Verification:** For promising candidate titles, retrieve full introductions or method sections to definitively confirm whether the output is a B-rep model.

TERMINATE
```
