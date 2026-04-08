# Paper Search Report

**Query:** Papers about 3d reconstruction specifically constructing brep model from point cloud
**Generated At:** 2026-03-22T22:10:07
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The user seeks academic literature on **3D reconstruction** techniques that convert **point clouds** specifically into **Boundary Representation (B-Rep)** models.
*   **Key Requirements:** The output must be a B-Rep (vertices, edges, faces, topology), not just a triangle mesh or point cloud surface.
*   **Context:** This task is often referred to as "Reverse Engineering" or "CAD Reconstruction."
*   **Target Domain:** Computer-Aided Design (CAD), Computer Graphics, and Computer Vision.

## Search Strategy
The team executed a two-pronged search strategy to cover both modern data-driven methods and classical geometric approaches:

1.  **Modern Neural Approaches (ArXiv):**
    *   **Queries:** `point cloud to B-Rep boundary representation CAD reconstruction`
    *   **Filters:** Attempted to exclude atmospheric and astronomical terms (`-atmospheric -cosmic -weather`).
    *   **Goal:** Identify deep learning models (Transformers, GNNs) that generate structured CAD solids or B-Reps directly from unstructured inputs.

2.  **Classical Geometric Approaches (Crossref):**
    *   **Queries:** `point cloud B-Rep boundary representation CAD reconstruction` (and variations).
    *   **Goal:** Locate foundational papers on geometric primitive fitting (RANSAC), surface segmentation, and topology recovery (pre-2015 era).

## Candidate Papers
*Note: The search results were heavily contaminated by false positives regarding atmospheric science. The following list contains only the verified relevant papers found in the transcript.*

### Deep Learning & Data-Driven Approaches
*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   *Source:* arXiv
    *   *Focus:* Models B-Rep reconstruction as a chain complex problem (vertices, edges, faces).
    *   *Method:* Uses a sparse CNN encoder and a tri-path transformer decoder to predict geometric primitives and relationships, followed by global optimization for validity.
*   **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   *Source:* arXiv
    *   *Focus:* Reconstructs feature-based parametric CAD models directly from point clouds.
    *   *Method:* Autoregressive reconstruction using two transformer decoders and a cross-attention parameter optimizer.
*   **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** (2024)
    *   *Source:* arXiv
    *   *Focus:* A unified system for generating CAD models from text, images, *or point clouds*.
    *   *Method:* Leverages Large Language Models (LLMs) to align multimodal inputs (including point clouds) with CAD construction sequences.
*   **Towards High-Fidelity CAD Generation via LLM-Driven Program Generation... (FutureCAD)** (2026)
    *   *Source:* arXiv
    *   *Focus:* Text-to-CAD generation using LLMs and B-Rep grounding transformers.
    *   *Relevance:* While primarily text-to-CAD, it discusses the interaction between parametric operations and B-Rep primitives.

### Related & Datasets
*   **B-rep Matching for Collaborating Across CAD Systems** (2023)
    *   *Source:* arXiv
    *   *Focus:* Finding correspondences between B-Reps. Relevant for understanding B-Rep topology handling, though not a reconstruction paper.
*   **CAD-Estate: Large-scale CAD Model Annotation in RGB Videos** (2023)
    *   *Source:* arXiv
    *   *Focus:* Dataset creation for CAD model retrieval from video. Relevant for the context of CAD in real-world scenes.

### Classical / Limited Metadata
*   **Adaptive approach for point cloud based CAD model reconstruction** (2013)
    *   *Source:* Journal of Computer Applications (Crossref)
    *   *Limitation:* No abstract available; title suggests relevance but content could not be verified.
*   **Segmentation and Local Reconstruction of Turbine Blade Point Cloud** (2020)
    *   *Source:* CAD'20 (Crossref)
    *   *Limitation:* No abstract available; likely relevant to the "segmentation" step of B-Rep reconstruction.
*   **A Computational Framework for the Boundary Representation of Solid Sweeps** (2014)
    *   *Source:* CAD'14 (Crossref)
    *   *Limitation:* No abstract available; focuses on "Solid Sweeps," which is a specific B-Rep operation.

## Notes and Gaps
The search process encountered critical limitations that prevent a comprehensive report at this time:

1.  **Severe Keyword Contamination:**
    *   The term "point cloud" and "CLOUD" caused major interference. The top results consistently returned papers on the **CERN CLOUD experiment** (cosmic rays and cloud formation) and **Taurus Molecular Clouds** (astrophysics).
    *   Negative keywords failed to filter these out because the papers are titled "CLOUD" or contain the specific acronym.

2.  **Missing Foundational Literature:**
    *   The "Classical" search strand (pre-2015 geometric methods) failed to return retrievable results with abstracts.
    *   There is a complete absence of papers on **RANSAC primitive fitting**, **geometric surface segmentation**, and **topology recovery algorithms**, which are the standard traditional methods for B-Rep reconstruction.

3.  **Metadata Incompleteness:**
    *   Crossref results for classical papers did not include abstracts, making it impossible to verify if they actually target B-Rep output or just generic surface reconstruction (meshing).

## Recommended Next Steps
To complete this search successfully, the following actions are required:

1.  **Keyword Substitution:**
    *   Abandon the term "point cloud" in the classical search to avoid atmospheric noise. Use synonyms like **"laser scanning data"**, **"3D scan data"**, or **"range data"**.
    *   Use the domain term **"Reverse Engineering"** as the primary keyword for classical searches (e.g., `"Reverse Engineering" AND "CAD Model" AND "B-Rep"`).

2.  **Category Filtering:**
    *   Explicitly exclude arXiv categories `astro-ph`, `physics.atmos-ph`, and `physics.geo-ph`.

3.  **Targeted Classical Queries:**
    *   Query for specific sub-tasks known in B-Rep reconstruction: `"primitive fitting" AND "CAD"`, `"surface segmentation" AND "topology"`, `"feature extraction" AND "solid modeling"`.

TERMINATE

## Trace

### Message 1

- Source: `user`
- Type: `TextMessage`

```text
Papers about 3d reconstruction specifically constructing brep model from point cloud
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`

```text
**Plan Analysis**

*   **User Intent:** The user is interested in the intersection of computer vision, graphics, and CAD. Specifically, they want methods that go beyond simple mesh generation (polygons) to create boundary representations (B-Rep)—which include vertices, edges, faces, and topological connectivity—from unstructured 3D point clouds.
*   **Specific Focus:** Reverse engineering, primitive fitting, surface segmentation, and topology generation.
*   **Assumptions:**
    *   The user is interested in algorithms for man-made objects (CAD-like) rather than organic shapes (though some methods apply to both).
    *   "B-Rep" implies parametric surfaces (planes, cylinders, NURBS) and topological validity, not just watertight meshes.
    *   Both classical geometric approaches and modern deep learning approaches are relevant.

**Retrieval Plan**

*   **Scope:** Academic conferences and journals related to Computer-Aided Design (CAD), Computer Graphics (SIGGRAPH/EG), and Computer Vision (CVPR/ICCV).
*   **Keywords:** "Point cloud to B-rep", "CAD reconstruction", "Reverse engineering", "Primitive detection", "Surface segmentation", "Topology recovery", "Parametric fitting", "Solid modeling", "Point cloud processing".
*   **Year Range:** 2000–Present (Covering foundational RANSAC/fitting papers up to modern neural B-Rep reconstruction).
*   **Verification Actions:**
    *   Ensure papers explicitly target B-Rep, solids, or parametric models, not just mesh triangulation (e.g., Poisson Surface Reconstruction).
    *   Confirm the output involves topological structures (edges, loops, faces) rather than just depth maps or voxel grids.

**Handoff to RetrievalAgent**

Execute a search for papers focused on converting point clouds into Boundary Representation (B-Rep) models. Prioritize literature that discusses geometric primitive fitting, surface segmentation, and topology inference. Filter out standard surface reconstruction methods that only generate triangle meshes. Return a list of high-impact papers including both classical geometric algorithms and recent deep learning approaches.
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`

```text
I'll search for papers on B-Rep reconstruction from point clouds, focusing on methods that generate boundary representations rather than just meshes.
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`

```text
FunctionCall(id='call_6f0c00b3944e4342b5f4e045', arguments='{"query":"point cloud to B-Rep boundary representation CAD reconstruction","max_results_per_source":"10","from_year":"2000"}', name='search_all_sources')
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`

```text
content="Combined search results\n\nQuery: point cloud to B-Rep boundary representation CAD reconstruction\n\narXiv results for query: point cloud to B-Rep boundary representation CAD reconstruction\n\n[1]\nTitle: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-16T19:12:19Z\nURL: http://arxiv.org/abs/physics/0104048v1\nSummary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth's climate seems to be remarkably sensitive to solar activity, but variations of the Sun's electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.\n\n[2]\nTitle: CLOUD: an atmospheric research facility at CERN\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-24T07:30:14Z\nURL: http://arxiv.org/abs/physics/0104076v1\nSummary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.\n\n[3]\nTitle: Addendum to the CLOUD proposal\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-23T13:58:48Z\nURL: http://arxiv.org/abs/physics/0104068v1\nSummary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.\n\n[4]\nTitle: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation\nSource: arXiv\nAuthors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong\nPublished: 2022-05-29T05:30:33Z\nURL: http://arxiv.org/abs/2205.14573v1\nSummary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.\n\n[5]\nTitle: CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM\nSource: arXiv\nAuthors: Jingwei Xu, Chenyu Wang, Zibo Zhao, Wen Liu, Yi Ma\nPublished: 2024-11-07T18:31:08Z\nURL: http://arxiv.org/abs/2411.04954v3\nSummary: This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/\n\n[6]\nTitle: A U-band survey of brown dwarfs in the Taurus Molecular Cloud with the XMM-Newton Optical/UV Monitor\nSource: arXiv\nAuthors: Nicolas Grosso, Marc Audard, Jérôme Bouvier, Kevin R. Briggs, Manuel Güdel\nPublished: 2006-09-01T13:24:57Z\nURL: http://arxiv.org/abs/astro-ph/0609027v1\nSummary: We aim to characterize the U-band variability of young brown dwarfs in the Taurus Molecular Cloud and discuss its origin. We used the XMM-Newton Extended Survey of the Taurus Molecular Cloud, where a sample of 11 young bona fide brown dwarfs (spectral type later than M6) were observed simultaneously in X-rays with XMM-Newton and in the U-band with the XMM-Newton Optical/UV Monitor (OM). We obtained upper limits to the U-band emission of 10 brown dwarfs (U>19.6-20.6 mag), whereas 2MASSJ04141188+2811535 was detected in the U-band. Remarkably, the magnitude of this brown dwarf increased regularly from U~19.5 mag at the beginning of the observation, peaked 6h later at U~18.4 mag, and then decreased to U~18.65 mag in the next 2h. The first OM U-band measurement is consistent with the quiescent level observed about one year later thanks to ground follow-up observations. This brown dwarf was not detected in X-rays by XMM-Newton during the OM observation. We discuss the possible sources of U-band variability for this young brown dwarf, namely a magnetic flare, non-steady accretion onto the substellar surface, and rotational modulation of a hot spot. We conclude that this event is related to accretion from a circumsubstellar disk, where the mass accretion rate was about a factor of 3 higher than during the quiescent level.\n\n[7]\nTitle: B-rep Matching for Collaborating Across CAD Systems\nSource: arXiv\nAuthors: Benjamin Jones, James Noeckel, Milin Kodnongbua, Ilya Baran, Adriana Schulz\nPublished: 2023-06-05T18:23:41Z\nURL: http://arxiv.org/abs/2306.03169v1\nSummary: Large Computer-Aided Design (CAD) projects usually require collaboration across many different CAD systems as well as applications that interoperate with them for manufacturing, visualization, or simulation. A fundamental barrier to such collaborations is the ability to refer to parts of the geometry (such as a specific face) robustly under geometric and/or topological changes to the model. Persistent referencing schemes are a fundamental aspect of most CAD tools, but models that are shared across systems cannot generally make use of these internal referencing mechanisms, creating a challenge for collaboration. In this work, we address this issue by developing a novel learning-based algorithm that can automatically find correspondences between two CAD models using the standard representation used for sharing models across CAD systems: the Boundary-Representation (B-rep). Because our method works directly on B-reps it can be generalized across different CAD applications enabling collaboration.\n\n[8]\nTitle: Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding\nSource: arXiv\nAuthors: Jiahao Li, Qingwang Zhang, Qiuyu Chen, Guozhan Qiu, Yunzhong Lou\nPublished: 2026-03-12T11:54:29Z\nURL: http://arxiv.org/abs/2603.11831v1\nSummary: The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations. Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design. This paper present FutureCAD, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (BRepGround) for high-fidelity CAD generation. Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which BRepGround then grounds to the target primitives. To train our framework, we construct a new dataset comprising real-world CAD models. For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization. Experiments show that FutureCAD achieves state-of-the-art CAD generation performance.\n\n[9]\nTitle: P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds\nSource: arXiv\nAuthors: Zhihao Zong, Fazhi He, Rubin Fan, Yuxin Liu\nPublished: 2023-10-04T08:00:05Z\nURL: http://arxiv.org/abs/2310.02638v1\nSummary: Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet architecture combines a point cloud feature extractor, a CAD sequence reconstructor and a parameter optimizer. Subsequently, in order to reconstruct the featured CAD model in an autoregressive way, the CAD sequence reconstructor applies two transformer decoders, one with target mask and the other without mask. Finally, for predicting parameters more precisely, we design a parameter optimizer with cross-attention mechanism to further refine the CAD feature parameters. We evaluate P2CADNet on the public dataset, and the experimental results show that P2CADNet has excellent reconstruction quality and accuracy. To our best knowledge, P2CADNet is the first end-to-end network to reconstruct featured CAD model from point cloud, and can be regarded as baseline for future works. Therefore, we open the source code at https://github.com/Blice0415/P2CADNet.\n\n[10]\nTitle: CAD-Estate: Large-scale CAD Model Annotation in RGB Videos\nSource: arXiv\nAuthors: Kevis-Kokitsi Maninis, Stefan Popov, Matthias Nießner, Vittorio Ferrari\nPublished: 2023-06-15T10:12:02Z\nURL: http://arxiv.org/abs/2306.09011v2\nSummary: We propose a method for annotating videos of complex multi-object scenes with a globally-consistent 3D representation of the objects. We annotate each object with a CAD model from a database, and place it in the 3D coordinate frame of the scene with a 9-DoF pose transformation. Our method is semi-automatic and works on commonly-available RGB videos, without requiring a depth sensor. Many steps are performed automatically, and the tasks performed by humans are simple, well-specified, and require only limited reasoning in 3D. This makes them feasible for crowd-sourcing and has allowed us to construct a large-scale dataset by annotating real-estate videos from YouTube. Our dataset CAD-Estate offers 101k instances of 12k unique CAD models placed in the 3D representations of 20k videos. In comparison to Scan2CAD, the largest existing dataset with CAD model annotations on real scenes, CAD-Estate has 7x more instances and 4x more unique CAD models. We showcase the benefits of pre-training a Mask2CAD model on CAD-Estate for the task of automatic 3D object reconstruction and pose estimation, demonstrating that it leads to performance improvements on the popular Scan2CAD benchmark. The dataset is available at https://github.com/google-research/cad-estate.\n\nCrossref results for query: point cloud to B-Rep boundary representation CAD reconstruction\n\n[1]\nTitle: Adaptive approach for point cloud based CAD model reconstruction\nSource: Crossref / Journal of Computer Applications\nAuthors: Jin LIU\nPublished: 2013-11-6\nURL: https://doi.org/10.3724/sp.j.1087.2013.02617\nDOI: 10.3724/sp.j.1087.2013.02617\nSummary: No abstract/summary available.\n\n[2]\nTitle: Segmentation and Local Reconstruction of Turbine Blade Point Cloud\nSource: Crossref / CAD'20\nAuthors: Wei Wang, ZhenYu Guo, JiaMing Yang, Pai Zheng\nPublished: 2020-5-25\nURL: https://doi.org/10.14733/cadconfp.2020.193-198\nDOI: 10.14733/cadconfp.2020.193-198\nSummary: No abstract/summary available.\n\n[3]\nTitle: Direct Rapid Prototyping from Point Cloud Data without Surface Reconstruction\nSource: Crossref / Proceedings of CAD'17\nAuthors: Tianyun Yuan, Xiaobo Peng, Dongdong Zhang\nPublished: 2017-8-10\nURL: https://doi.org/10.14733/cadconfp.2017.27-31\nDOI: 10.14733/cadconfp.2017.27-31\nSummary: No abstract/summary available.\n\n[4]\nTitle: Partial contrastive point cloud self-supervised representation learning\nSource: Crossref / Scientific Reports\nAuthors: Zijun Cheng, Yiguo Wang\nPublished: 2025-5-9\nURL: https://doi.org/10.1038/s41598-025-98521-y\nDOI: 10.1038/s41598-025-98521-y\nSummary: No abstract/summary available.\n\n[5]\nTitle: Core: Contrast and Reconstruction Combination Self-Supervised Point Cloud Representation Learning\nSource: Crossref / Crossref\nAuthors: Changyu Zeng, Jimin Xiao, Anh Nguyen, Xuming Hu, Wei Wang\nPublished: 2024\nURL: https://doi.org/10.2139/ssrn.4994872\nDOI: 10.2139/ssrn.4994872\nSummary: No abstract/summary available.\n\n[6]\nTitle: Building Facade Acquisition and Restoration Generation Method Based on Point Cloud Plane Boundary Extraction Algorithm\nSource: Crossref / Computer-Aided Design and Applications\nAuthors: Yulin Ma\nPublished: 2024-7-13\nURL: https://doi.org/10.14733/cadaps.2025.s2.71-86\nDOI: 10.14733/cadaps.2025.s2.71-86\nSummary: No abstract/summary available.\n\n[7]\nTitle: Gaussian Point Cloud Autoencoder for Partial Point Cloud Reconstruction\nSource: Crossref / Crossref\nAuthors: Jonathan Then Sien Phang, King Hann Lim\nPublished: 2024\nURL: https://doi.org/10.2139/ssrn.4728672\nDOI: 10.2139/ssrn.4728672\nSummary: No abstract/summary available.\n\n[8]\nTitle: Representation Learning via Parallel Subset Reconstruction for 3D Point Cloud Generation\nSource: Crossref / 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)\nAuthors: Kohei Matsuzaki, Kazuyuki Tasaka\nPublished: 2019-11\nURL: https://doi.org/10.1109/iros40897.2019.8967842\nDOI: 10.1109/iros40897.2019.8967842\nSummary: No abstract/summary available.\n\n[9]\nTitle: A Computational Framework for the Boundary Representation of Solid Sweeps\nSource: Crossref / CAD'14\nAuthors: Bharat Adsul\nPublished: 2014-12-16\nURL: https://doi.org/10.14733/cadconfp.2014.35-37\nDOI: 10.14733/cadconfp.2014.35-37\nSummary: No abstract/summary available.\n\n[10]\nTitle: Functional Surface Reconstruction from Unorganized Noisy Point Clouds\nSource: Crossref / CAD'14\nAuthors: Xueshu Liu\nPublished: 2014-12-16\nURL: https://doi.org/10.14733/cadconfp.2014.85-87\nDOI: 10.14733/cadconfp.2014.85-87\nSummary: No abstract/summary available." name='search_all_sources' call_id='call_6f0c00b3944e4342b5f4e045' is_error=False
```

### Message 6

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`

```text
Combined search results

Query: point cloud to B-Rep boundary representation CAD reconstruction

arXiv results for query: point cloud to B-Rep boundary representation CAD reconstruction

[1]
Title: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-16T19:12:19Z
URL: http://arxiv.org/abs/physics/0104048v1
Summary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth's climate seems to be remarkably sensitive to solar activity, but variations of the Sun's electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.

[2]
Title: CLOUD: an atmospheric research facility at CERN
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-24T07:30:14Z
URL: http://arxiv.org/abs/physics/0104076v1
Summary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.

[3]
Title: Addendum to the CLOUD proposal
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-23T13:58:48Z
URL: http://arxiv.org/abs/physics/0104068v1
Summary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.

[4]
Title: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation
Source: arXiv
Authors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong
Published: 2022-05-29T05:30:33Z
URL: http://arxiv.org/abs/2205.14573v1
Summary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.

[5]
Title: CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM
Source: arXiv
Authors: Jingwei Xu, Chenyu Wang, Zibo Zhao, Wen Liu, Yi Ma
Published: 2024-11-07T18:31:08Z
URL: http://arxiv.org/abs/2411.04954v3
Summary: This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/

[6]
Title: A U-band survey of brown dwarfs in the Taurus Molecular Cloud with the XMM-Newton Optical/UV Monitor
Source: arXiv
Authors: Nicolas Grosso, Marc Audard, Jérôme Bouvier, Kevin R. Briggs, Manuel Güdel
Published: 2006-09-01T13:24:57Z
URL: http://arxiv.org/abs/astro-ph/0609027v1
Summary: We aim to characterize the U-band variability of young brown dwarfs in the Taurus Molecular Cloud and discuss its origin. We used the XMM-Newton Extended Survey of the Taurus Molecular Cloud, where a sample of 11 young bona fide brown dwarfs (spectral type later than M6) were observed simultaneously in X-rays with XMM-Newton and in the U-band with the XMM-Newton Optical/UV Monitor (OM). We obtained upper limits to the U-band emission of 10 brown dwarfs (U>19.6-20.6 mag), whereas 2MASSJ04141188+2811535 was detected in the U-band. Remarkably, the magnitude of this brown dwarf increased regularly from U~19.5 mag at the beginning of the observation, peaked 6h later at U~18.4 mag, and then decreased to U~18.65 mag in the next 2h. The first OM U-band measurement is consistent with the quiescent level observed about one year later thanks to ground follow-up observations. This brown dwarf was not detected in X-rays by XMM-Newton during the OM observation. We discuss the possible sources of U-band variability for this young brown dwarf, namely a magnetic flare, non-steady accretion onto the substellar surface, and rotational modulation of a hot spot. We conclude that this event is related to accretion from a circumsubstellar disk, where the mass accretion rate was about a factor of 3 higher than during the quiescent level.

[7]
Title: B-rep Matching for Collaborating Across CAD Systems
Source: arXiv
Authors: Benjamin Jones, James Noeckel, Milin Kodnongbua, Ilya Baran, Adriana Schulz
Published: 2023-06-05T18:23:41Z
URL: http://arxiv.org/abs/2306.03169v1
Summary: Large Computer-Aided Design (CAD) projects usually require collaboration across many different CAD systems as well as applications that interoperate with them for manufacturing, visualization, or simulation. A fundamental barrier to such collaborations is the ability to refer to parts of the geometry (such as a specific face) robustly under geometric and/or topological changes to the model. Persistent referencing schemes are a fundamental aspect of most CAD tools, but models that are shared across systems cannot generally make use of these internal referencing mechanisms, creating a challenge for collaboration. In this work, we address this issue by developing a novel learning-based algorithm that can automatically find correspondences between two CAD models using the standard representation used for sharing models across CAD systems: the Boundary-Representation (B-rep). Because our method works directly on B-reps it can be generalized across different CAD applications enabling collaboration.

[8]
Title: Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding
Source: arXiv
Authors: Jiahao Li, Qingwang Zhang, Qiuyu Chen, Guozhan Qiu, Yunzhong Lou
Published: 2026-03-12T11:54:29Z
URL: http://arxiv.org/abs/2603.11831v1
Summary: The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations. Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design. This paper present FutureCAD, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (BRepGround) for high-fidelity CAD generation. Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which BRepGround then grounds to the target primitives. To train our framework, we construct a new dataset comprising real-world CAD models. For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization. Experiments show that FutureCAD achieves state-of-the-art CAD generation performance.

[9]
Title: P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds
Source: arXiv
Authors: Zhihao Zong, Fazhi He, Rubin Fan, Yuxin Liu
Published: 2023-10-04T08:00:05Z
URL: http://arxiv.org/abs/2310.02638v1
Summary: Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet architecture combines a point cloud feature extractor, a CAD sequence reconstructor and a parameter optimizer. Subsequently, in order to reconstruct the featured CAD model in an autoregressive way, the CAD sequence reconstructor applies two transformer decoders, one with target mask and the other without mask. Finally, for predicting parameters more precisely, we design a parameter optimizer with cross-attention mechanism to further refine the CAD feature parameters. We evaluate P2CADNet on the public dataset, and the experimental results show that P2CADNet has excellent reconstruction quality and accuracy. To our best knowledge, P2CADNet is the first end-to-end network to reconstruct featured CAD model from point cloud, and can be regarded as baseline for future works. Therefore, we open the source code at https://github.com/Blice0415/P2CADNet.

[10]
Title: CAD-Estate: Large-scale CAD Model Annotation in RGB Videos
Source: arXiv
Authors: Kevis-Kokitsi Maninis, Stefan Popov, Matthias Nießner, Vittorio Ferrari
Published: 2023-06-15T10:12:02Z
URL: http://arxiv.org/abs/2306.09011v2
Summary: We propose a method for annotating videos of complex multi-object scenes with a globally-consistent 3D representation of the objects. We annotate each object with a CAD model from a database, and place it in the 3D coordinate frame of the scene with a 9-DoF pose transformation. Our method is semi-automatic and works on commonly-available RGB videos, without requiring a depth sensor. Many steps are performed automatically, and the tasks performed by humans are simple, well-specified, and require only limited reasoning in 3D. This makes them feasible for crowd-sourcing and has allowed us to construct a large-scale dataset by annotating real-estate videos from YouTube. Our dataset CAD-Estate offers 101k instances of 12k unique CAD models placed in the 3D representations of 20k videos. In comparison to Scan2CAD, the largest existing dataset with CAD model annotations on real scenes, CAD-Estate has 7x more instances and 4x more unique CAD models. We showcase the benefits of pre-training a Mask2CAD model on CAD-Estate for the task of automatic 3D object reconstruction and pose estimation, demonstrating that it leads to performance improvements on the popular Scan2CAD benchmark. The dataset is available at https://github.com/google-research/cad-estate.

Crossref results for query: point cloud to B-Rep boundary representation CAD reconstruction

[1]
Title: Adaptive approach for point cloud based CAD model reconstruction
Source: Crossref / Journal of Computer Applications
Authors: Jin LIU
Published: 2013-11-6
URL: https://doi.org/10.3724/sp.j.1087.2013.02617
DOI: 10.3724/sp.j.1087.2013.02617
Summary: No abstract/summary available.

[2]
Title: Segmentation and Local Reconstruction of Turbine Blade Point Cloud
Source: Crossref / CAD'20
Authors: Wei Wang, ZhenYu Guo, JiaMing Yang, Pai Zheng
Published: 2020-5-25
URL: https://doi.org/10.14733/cadconfp.2020.193-198
DOI: 10.14733/cadconfp.2020.193-198
Summary: No abstract/summary available.

[3]
Title: Direct Rapid Prototyping from Point Cloud Data without Surface Reconstruction
Source: Crossref / Proceedings of CAD'17
Authors: Tianyun Yuan, Xiaobo Peng, Dongdong Zhang
Published: 2017-8-10
URL: https://doi.org/10.14733/cadconfp.2017.27-31
DOI: 10.14733/cadconfp.2017.27-31
Summary: No abstract/summary available.

[4]
Title: Partial contrastive point cloud self-supervised representation learning
Source: Crossref / Scientific Reports
Authors: Zijun Cheng, Yiguo Wang
Published: 2025-5-9
URL: https://doi.org/10.1038/s41598-025-98521-y
DOI: 10.1038/s41598-025-98521-y
Summary: No abstract/summary available.

[5]
Title: Core: Contrast and Reconstruction Combination Self-Supervised Point Cloud Representation Learning
Source: Crossref / Crossref
Authors: Changyu Zeng, Jimin Xiao, Anh Nguyen, Xuming Hu, Wei Wang
Published: 2024
URL: https://doi.org/10.2139/ssrn.4994872
DOI: 10.2139/ssrn.4994872
Summary: No abstract/summary available.

[6]
Title: Building Facade Acquisition and Restoration Generation Method Based on Point Cloud Plane Boundary Extraction Algorithm
Source: Crossref / Computer-Aided Design and Applications
Authors: Yulin Ma
Published: 2024-7-13
URL: https://doi.org/10.14733/cadaps.2025.s2.71-86
DOI: 10.14733/cadaps.2025.s2.71-86
Summary: No abstract/summary available.

[7]
Title: Gaussian Point Cloud Autoencoder for Partial Point Cloud Reconstruction
Source: Crossref / Crossref
Authors: Jonathan Then Sien Phang, King Hann Lim
Published: 2024
URL: https://doi.org/10.2139/ssrn.4728672
DOI: 10.2139/ssrn.4728672
Summary: No abstract/summary available.

[8]
Title: Representation Learning via Parallel Subset Reconstruction for 3D Point Cloud Generation
Source: Crossref / 2019 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS)
Authors: Kohei Matsuzaki, Kazuyuki Tasaka
Published: 2019-11
URL: https://doi.org/10.1109/iros40897.2019.8967842
DOI: 10.1109/iros40897.2019.8967842
Summary: No abstract/summary available.

[9]
Title: A Computational Framework for the Boundary Representation of Solid Sweeps
Source: Crossref / CAD'14
Authors: Bharat Adsul
Published: 2014-12-16
URL: https://doi.org/10.14733/cadconfp.2014.35-37
DOI: 10.14733/cadconfp.2014.35-37
Summary: No abstract/summary available.

[10]
Title: Functional Surface Reconstruction from Unorganized Noisy Point Clouds
Source: Crossref / CAD'14
Authors: Xueshu Liu
Published: 2014-12-16
URL: https://doi.org/10.14733/cadconfp.2014.85-87
DOI: 10.14733/cadconfp.2014.85-87
Summary: No abstract/summary available.
```

### Message 7

- Source: `ReviewerAgent`
- Type: `TextMessage`

```text
REVIEW_DECISION: REVISE

REVIEW_SUMMARY
The retrieval found relevant deep learning papers (e.g., ComplexGen, P2CADNet) but suffered from significant noise, with the top results being unrelated physics papers about atmospheric "clouds" rather than 3D point clouds. Additionally, the results are skewed toward very recent neural approaches (2022-2024), missing the foundational literature on classical geometric primitive fitting and reverse engineering. The Crossref results also lack abstracts, making relevance assessment difficult. To ensure a comprehensive report, the search must eliminate the keyword ambiguity and include older, geometric approaches.

THRESHOLD_CHECKS:
- coverage: Insufficient. Heavily skewed toward deep learning; missing classical geometric methods (e.g., RANSAC, primitive fitting) which are core to B-Rep reconstruction.
- relevance: Mixed. The top 3 results are false positives (atmospheric physics). While items 4, 5, and 9 are highly relevant, the high position of noise lowers the quality.
- metadata: Partial. ArXiv results are good, but Crossref results lack abstracts, hindering verification of B-Rep specific content.
- gaps: Missing classical algorithms for primitive detection and topology recovery (pre-2020 era).

NEXT_ACTIONS:
1. Re-run the search with negative keywords to exclude atmospheric physics (e.g., "point cloud to B-Rep" -atmospheric -cosmic -"galactic") and ensure "3D" is explicit.
2. Add specific queries for classical geometric reconstruction methods to ensure coverage of non-deep learning techniques (keywords: "reverse engineering", "primitive fitting", "RANSAC CAD", "segmentation topology").
3. Prioritize sources that provide abstracts or summaries to verify the B-Rep output claim (not just generic surface reconstruction).
```

### Message 8

- Source: `PlannerAgent`
- Type: `TextMessage`

```text
**Plan Analysis**

*   **Revision Rationale:** The previous search failed due to keyword ambiguity ("cloud" retrieving atmospheric science) and a temporal gap ignoring decades of classical geometric processing. The user needs a complete picture ranging from foundational reverse engineering techniques to modern neural networks.
*   **Assumptions:**
    *   Classical B-Rep reconstruction is often framed as "Reverse Engineering" or "Feature Recognition" in older literature.
    *   Standard mesh reconstruction papers (e.g., Poisson, Ball Pivoting) should be excluded unless they explicitly convert to CAD/B-Rep.
    *   We must use negative keywords to filter out the atmospheric noise that plagued the first attempt.

**Retrieval Plan**

*   **Strategy A: Modern Neural & Data-Driven Approaches (2015–Present)**
    *   *Focus:* Deep learning, graph neural networks, and transformers for direct B-Rep generation.
    *   *Query Logic:* `(point cloud) AND (B-Rep OR "Boundary Representation") AND (CAD OR reconstruction) -atmospheric -cosmic -weather -physics`
    *   *Keywords:* "Neural B-Rep", "CAD reconstruction deep learning", "Point cloud to CAD", "Solid generation".
*   **Strategy B: Classical Geometric & Reverse Engineering (1990–2020)**
    *   *Focus:* Primitive fitting (RANSAC), surface segmentation, topology recovery, and feature-based reconstruction.
    *   *Query Logic:* `(point cloud) AND ("reverse engineering" OR "CAD model" OR "primitive fitting") AND (B-Rep OR topology OR segmentation) -atmospheric -cosmic`
    *   *Keywords:* "Reverse engineering", "Geometric primitive fitting", "RANSAC CAD", "Surface segmentation", "Topology recovery", "Feature extraction".
*   **Verification Actions:**
    *   **Strict Filtering:** Reject any paper regarding "cosmic rays," "condensation," or "weather chambers."
    *   **Abstract Check:** Ensure the paper explicitly mentions vertices, edges, faces, or topology. Discard papers that only output a polygon soup or mesh (STL/OBJ) without higher-level structure.
    *   **Date Spread:** Ensure the results cover both the foundational pre-2010 work and the post-2020 neural methods.

**Handoff to RetrievalAgent**

Execute two distinct search strands to correct for noise and coverage gaps.

1.  **Strand 1 (Neural):** Search for "point cloud to B-Rep CAD reconstruction -atmospheric -cosmic". Target arXiv and recent CS conference proceedings (CVPR/SIGGRAPH).
2.  **Strand 2 (Classical):** Search for "reverse engineering point cloud primitive fitting RANSAC topology -atmospheric". Target older engineering journals (Computer-Aided Design) and geometric processing conferences.

Verify that every result includes an abstract and focuses on creating structured CAD/B-Rep models (faces, edges, parameters) rather than unstructured meshes or atmospheric phenomena. Provide a list sorted chronologically or by impact to show the evolution of the field.
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ThoughtEvent`

```text
I'll execute two distinct search strands to correct for noise and coverage gaps. Let me search for modern neural approaches and classical geometric methods separately.
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`

```text
FunctionCall(id='call_6e3198c3c4e94c2a95866e55', arguments='{"query":"point cloud B-Rep boundary representation CAD reconstruction -atmospheric -cosmic -weather -physics","max_results":"15"}', name='search_arxiv')
```

### Message 11

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`

```text
content="arXiv results for query: point cloud B-Rep boundary representation CAD reconstruction -atmospheric -cosmic -weather -physics\n\n[1]\nTitle: CLOUD: an atmospheric research facility at CERN\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-24T07:30:14Z\nURL: http://arxiv.org/abs/physics/0104076v1\nSummary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.\n\n[2]\nTitle: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-16T19:12:19Z\nURL: http://arxiv.org/abs/physics/0104048v1\nSummary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth's climate seems to be remarkably sensitive to solar activity, but variations of the Sun's electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.\n\n[3]\nTitle: Addendum to the CLOUD proposal\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-23T13:58:48Z\nURL: http://arxiv.org/abs/physics/0104068v1\nSummary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.\n\n[4]\nTitle: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation\nSource: arXiv\nAuthors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong\nPublished: 2022-05-29T05:30:33Z\nURL: http://arxiv.org/abs/2205.14573v1\nSummary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.\n\n[5]\nTitle: CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM\nSource: arXiv\nAuthors: Jingwei Xu, Chenyu Wang, Zibo Zhao, Wen Liu, Yi Ma\nPublished: 2024-11-07T18:31:08Z\nURL: http://arxiv.org/abs/2411.04954v3\nSummary: This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/\n\n[6]\nTitle: A U-band survey of brown dwarfs in the Taurus Molecular Cloud with the XMM-Newton Optical/UV Monitor\nSource: arXiv\nAuthors: Nicolas Grosso, Marc Audard, Jérôme Bouvier, Kevin R. Briggs, Manuel Güdel\nPublished: 2006-09-01T13:24:57Z\nURL: http://arxiv.org/abs/astro-ph/0609027v1\nSummary: We aim to characterize the U-band variability of young brown dwarfs in the Taurus Molecular Cloud and discuss its origin. We used the XMM-Newton Extended Survey of the Taurus Molecular Cloud, where a sample of 11 young bona fide brown dwarfs (spectral type later than M6) were observed simultaneously in X-rays with XMM-Newton and in the U-band with the XMM-Newton Optical/UV Monitor (OM). We obtained upper limits to the U-band emission of 10 brown dwarfs (U>19.6-20.6 mag), whereas 2MASSJ04141188+2811535 was detected in the U-band. Remarkably, the magnitude of this brown dwarf increased regularly from U~19.5 mag at the beginning of the observation, peaked 6h later at U~18.4 mag, and then decreased to U~18.65 mag in the next 2h. The first OM U-band measurement is consistent with the quiescent level observed about one year later thanks to ground follow-up observations. This brown dwarf was not detected in X-rays by XMM-Newton during the OM observation. We discuss the possible sources of U-band variability for this young brown dwarf, namely a magnetic flare, non-steady accretion onto the substellar surface, and rotational modulation of a hot spot. We conclude that this event is related to accretion from a circumsubstellar disk, where the mass accretion rate was about a factor of 3 higher than during the quiescent level.\n\n[7]\nTitle: B-rep Matching for Collaborating Across CAD Systems\nSource: arXiv\nAuthors: Benjamin Jones, James Noeckel, Milin Kodnongbua, Ilya Baran, Adriana Schulz\nPublished: 2023-06-05T18:23:41Z\nURL: http://arxiv.org/abs/2306.03169v1\nSummary: Large Computer-Aided Design (CAD) projects usually require collaboration across many different CAD systems as well as applications that interoperate with them for manufacturing, visualization, or simulation. A fundamental barrier to such collaborations is the ability to refer to parts of the geometry (such as a specific face) robustly under geometric and/or topological changes to the model. Persistent referencing schemes are a fundamental aspect of most CAD tools, but models that are shared across systems cannot generally make use of these internal referencing mechanisms, creating a challenge for collaboration. In this work, we address this issue by developing a novel learning-based algorithm that can automatically find correspondences between two CAD models using the standard representation used for sharing models across CAD systems: the Boundary-Representation (B-rep). Because our method works directly on B-reps it can be generalized across different CAD applications enabling collaboration.\n\n[8]\nTitle: Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding\nSource: arXiv\nAuthors: Jiahao Li, Qingwang Zhang, Qiuyu Chen, Guozhan Qiu, Yunzhong Lou\nPublished: 2026-03-12T11:54:29Z\nURL: http://arxiv.org/abs/2603.11831v1\nSummary: The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations. Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design. This paper present FutureCAD, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (BRepGround) for high-fidelity CAD generation. Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which BRepGround then grounds to the target primitives. To train our framework, we construct a new dataset comprising real-world CAD models. For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization. Experiments show that FutureCAD achieves state-of-the-art CAD generation performance.\n\n[9]\nTitle: P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds\nSource: arXiv\nAuthors: Zhihao Zong, Fazhi He, Rubin Fan, Yuxin Liu\nPublished: 2023-10-04T08:00:05Z\nURL: http://arxiv.org/abs/2310.02638v1\nSummary: Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet architecture combines a point cloud feature extractor, a CAD sequence reconstructor and a parameter optimizer. Subsequently, in order to reconstruct the featured CAD model in an autoregressive way, the CAD sequence reconstructor applies two transformer decoders, one with target mask and the other without mask. Finally, for predicting parameters more precisely, we design a parameter optimizer with cross-attention mechanism to further refine the CAD feature parameters. We evaluate P2CADNet on the public dataset, and the experimental results show that P2CADNet has excellent reconstruction quality and accuracy. To our best knowledge, P2CADNet is the first end-to-end network to reconstruct featured CAD model from point cloud, and can be regarded as baseline for future works. Therefore, we open the source code at https://github.com/Blice0415/P2CADNet.\n\n[10]\nTitle: CAD-Estate: Large-scale CAD Model Annotation in RGB Videos\nSource: arXiv\nAuthors: Kevis-Kokitsi Maninis, Stefan Popov, Matthias Nießner, Vittorio Ferrari\nPublished: 2023-06-15T10:12:02Z\nURL: http://arxiv.org/abs/2306.09011v2\nSummary: We propose a method for annotating videos of complex multi-object scenes with a globally-consistent 3D representation of the objects. We annotate each object with a CAD model from a database, and place it in the 3D coordinate frame of the scene with a 9-DoF pose transformation. Our method is semi-automatic and works on commonly-available RGB videos, without requiring a depth sensor. Many steps are performed automatically, and the tasks performed by humans are simple, well-specified, and require only limited reasoning in 3D. This makes them feasible for crowd-sourcing and has allowed us to construct a large-scale dataset by annotating real-estate videos from YouTube. Our dataset CAD-Estate offers 101k instances of 12k unique CAD models placed in the 3D representations of 20k videos. In comparison to Scan2CAD, the largest existing dataset with CAD model annotations on real scenes, CAD-Estate has 7x more instances and 4x more unique CAD models. We showcase the benefits of pre-training a Mask2CAD model on CAD-Estate for the task of automatic 3D object reconstruction and pose estimation, demonstrating that it leads to performance improvements on the popular Scan2CAD benchmark. The dataset is available at https://github.com/google-research/cad-estate." name='search_arxiv' call_id='call_6e3198c3c4e94c2a95866e55' is_error=False
```

### Message 12

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`

```text
arXiv results for query: point cloud B-Rep boundary representation CAD reconstruction -atmospheric -cosmic -weather -physics

[1]
Title: CLOUD: an atmospheric research facility at CERN
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-24T07:30:14Z
URL: http://arxiv.org/abs/physics/0104076v1
Summary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.

[2]
Title: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-16T19:12:19Z
URL: http://arxiv.org/abs/physics/0104048v1
Summary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth's climate seems to be remarkably sensitive to solar activity, but variations of the Sun's electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.

[3]
Title: Addendum to the CLOUD proposal
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-23T13:58:48Z
URL: http://arxiv.org/abs/physics/0104068v1
Summary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.

[4]
Title: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation
Source: arXiv
Authors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong
Published: 2022-05-29T05:30:33Z
URL: http://arxiv.org/abs/2205.14573v1
Summary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.

[5]
Title: CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM
Source: arXiv
Authors: Jingwei Xu, Chenyu Wang, Zibo Zhao, Wen Liu, Yi Ma
Published: 2024-11-07T18:31:08Z
URL: http://arxiv.org/abs/2411.04954v3
Summary: This paper aims to design a unified Computer-Aided Design (CAD) generation system that can easily generate CAD models based on the user's inputs in the form of textual description, images, point clouds, or even a combination of them. Towards this goal, we introduce the CAD-MLLM, the first system capable of generating parametric CAD models conditioned on the multimodal input. Specifically, within the CAD-MLLM framework, we leverage the command sequences of CAD models and then employ advanced large language models (LLMs) to align the feature space across these diverse multi-modalities data and CAD models' vectorized representations. To facilitate the model training, we design a comprehensive data construction and annotation pipeline that equips each CAD model with corresponding multimodal data. Our resulting dataset, named Omni-CAD, is the first multimodal CAD dataset that contains textual description, multi-view images, points, and command sequence for each CAD model. It contains approximately 450K instances and their CAD construction sequences. To thoroughly evaluate the quality of our generated CAD models, we go beyond current evaluation metrics that focus on reconstruction quality by introducing additional metrics that assess topology quality and surface enclosure extent. Extensive experimental results demonstrate that CAD-MLLM significantly outperforms existing conditional generative methods and remains highly robust to noises and missing points. The project page and more visualizations can be found at: https://cad-mllm.github.io/

[6]
Title: A U-band survey of brown dwarfs in the Taurus Molecular Cloud with the XMM-Newton Optical/UV Monitor
Source: arXiv
Authors: Nicolas Grosso, Marc Audard, Jérôme Bouvier, Kevin R. Briggs, Manuel Güdel
Published: 2006-09-01T13:24:57Z
URL: http://arxiv.org/abs/astro-ph/0609027v1
Summary: We aim to characterize the U-band variability of young brown dwarfs in the Taurus Molecular Cloud and discuss its origin. We used the XMM-Newton Extended Survey of the Taurus Molecular Cloud, where a sample of 11 young bona fide brown dwarfs (spectral type later than M6) were observed simultaneously in X-rays with XMM-Newton and in the U-band with the XMM-Newton Optical/UV Monitor (OM). We obtained upper limits to the U-band emission of 10 brown dwarfs (U>19.6-20.6 mag), whereas 2MASSJ04141188+2811535 was detected in the U-band. Remarkably, the magnitude of this brown dwarf increased regularly from U~19.5 mag at the beginning of the observation, peaked 6h later at U~18.4 mag, and then decreased to U~18.65 mag in the next 2h. The first OM U-band measurement is consistent with the quiescent level observed about one year later thanks to ground follow-up observations. This brown dwarf was not detected in X-rays by XMM-Newton during the OM observation. We discuss the possible sources of U-band variability for this young brown dwarf, namely a magnetic flare, non-steady accretion onto the substellar surface, and rotational modulation of a hot spot. We conclude that this event is related to accretion from a circumsubstellar disk, where the mass accretion rate was about a factor of 3 higher than during the quiescent level.

[7]
Title: B-rep Matching for Collaborating Across CAD Systems
Source: arXiv
Authors: Benjamin Jones, James Noeckel, Milin Kodnongbua, Ilya Baran, Adriana Schulz
Published: 2023-06-05T18:23:41Z
URL: http://arxiv.org/abs/2306.03169v1
Summary: Large Computer-Aided Design (CAD) projects usually require collaboration across many different CAD systems as well as applications that interoperate with them for manufacturing, visualization, or simulation. A fundamental barrier to such collaborations is the ability to refer to parts of the geometry (such as a specific face) robustly under geometric and/or topological changes to the model. Persistent referencing schemes are a fundamental aspect of most CAD tools, but models that are shared across systems cannot generally make use of these internal referencing mechanisms, creating a challenge for collaboration. In this work, we address this issue by developing a novel learning-based algorithm that can automatically find correspondences between two CAD models using the standard representation used for sharing models across CAD systems: the Boundary-Representation (B-rep). Because our method works directly on B-reps it can be generalized across different CAD applications enabling collaboration.

[8]
Title: Towards High-Fidelity CAD Generation via LLM-Driven Program Generation and Text-Based B-Rep Primitive Grounding
Source: arXiv
Authors: Jiahao Li, Qingwang Zhang, Qiuyu Chen, Guozhan Qiu, Yunzhong Lou
Published: 2026-03-12T11:54:29Z
URL: http://arxiv.org/abs/2603.11831v1
Summary: The field of Computer-Aided Design (CAD) generation has made significant progress in recent years. Existing methods typically fall into two separate categorie: parametric CAD modeling and direct boundary representation (B-Rep) synthesis. In modern feature-based CAD systems, parametric modeling and B-Rep are inherently intertwined, as advanced parametric operations (e.g., fillet and chamfer) require explicit selection of B-Rep geometric primitives, and the B-Rep itself is derived from parametric operations. Consequently, this paradigm gap remains a critical factor limiting AI-driven CAD modeling for complex industrial product design. This paper present FutureCAD, a novel text-to-CAD framework that leverages large language models (LLMs) and a B-Rep grounding transformer (BRepGround) for high-fidelity CAD generation. Our method generates executable CadQuery scripts, and introduces a text-based query mechanism that enables the LLM to specify geometric selections via natural language, which BRepGround then grounds to the target primitives. To train our framework, we construct a new dataset comprising real-world CAD models. For the LLM, we apply supervised fine-tuning (SFT) to establish fundamental CAD generation capabilities, followed by reinforcement learning (RL) to improve generalization. Experiments show that FutureCAD achieves state-of-the-art CAD generation performance.

[9]
Title: P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds
Source: arXiv
Authors: Zhihao Zong, Fazhi He, Rubin Fan, Yuxin Liu
Published: 2023-10-04T08:00:05Z
URL: http://arxiv.org/abs/2310.02638v1
Summary: Computer Aided Design (CAD), especially the feature-based parametric CAD, plays an important role in modern industry and society. However, the reconstruction of featured CAD model is more challenging than the reconstruction of other CAD models. To this end, this paper proposes an end-to-end network to reconstruct featured CAD model from point cloud (P2CADNet). Initially, the proposed P2CADNet architecture combines a point cloud feature extractor, a CAD sequence reconstructor and a parameter optimizer. Subsequently, in order to reconstruct the featured CAD model in an autoregressive way, the CAD sequence reconstructor applies two transformer decoders, one with target mask and the other without mask. Finally, for predicting parameters more precisely, we design a parameter optimizer with cross-attention mechanism to further refine the CAD feature parameters. We evaluate P2CADNet on the public dataset, and the experimental results show that P2CADNet has excellent reconstruction quality and accuracy. To our best knowledge, P2CADNet is the first end-to-end network to reconstruct featured CAD model from point cloud, and can be regarded as baseline for future works. Therefore, we open the source code at https://github.com/Blice0415/P2CADNet.

[10]
Title: CAD-Estate: Large-scale CAD Model Annotation in RGB Videos
Source: arXiv
Authors: Kevis-Kokitsi Maninis, Stefan Popov, Matthias Nießner, Vittorio Ferrari
Published: 2023-06-15T10:12:02Z
URL: http://arxiv.org/abs/2306.09011v2
Summary: We propose a method for annotating videos of complex multi-object scenes with a globally-consistent 3D representation of the objects. We annotate each object with a CAD model from a database, and place it in the 3D coordinate frame of the scene with a 9-DoF pose transformation. Our method is semi-automatic and works on commonly-available RGB videos, without requiring a depth sensor. Many steps are performed automatically, and the tasks performed by humans are simple, well-specified, and require only limited reasoning in 3D. This makes them feasible for crowd-sourcing and has allowed us to construct a large-scale dataset by annotating real-estate videos from YouTube. Our dataset CAD-Estate offers 101k instances of 12k unique CAD models placed in the 3D representations of 20k videos. In comparison to Scan2CAD, the largest existing dataset with CAD model annotations on real scenes, CAD-Estate has 7x more instances and 4x more unique CAD models. We showcase the benefits of pre-training a Mask2CAD model on CAD-Estate for the task of automatic 3D object reconstruction and pose estimation, demonstrating that it leads to performance improvements on the popular Scan2CAD benchmark. The dataset is available at https://github.com/google-research/cad-estate.
```

### Message 13

- Source: `ReviewerAgent`
- Type: `TextMessage`

```text
REVIEW_DECISION: REVISE

REVIEW_SUMMARY
The retrieval has failed to resolve two critical issues. First, the negative keywords failed to filter out atmospheric physics papers (the CERN CLOUD experiment and astronomical molecular clouds), which still dominate the top 5 results of the arXiv search. Second, the "Classical/Geometric" search strand (Strategy B) requested in the plan is missing entirely from the output, meaning there is zero coverage of foundational reverse engineering methods (RANSAC, primitive fitting, geometric segmentation). The current list only provides ~2 relevant deep learning papers.

THRESHOLD_CHECKS:
- coverage: Insufficient. Missing the entire body of classical geometric literature (pre-2015) and the second search strand did not appear in results.
- relevance: Poor. The top 3 results are false positives (atmospheric/astronomical). Only items 4 and 9 are strong matches for "point cloud to B-Rep".
- metadata: Good for existing entries, but useless for irrelevant entries.
- gaps: Missing classical algorithms for geometric primitive detection, surface segmentation, and topology inference.

NEXT_ACTIONS:
1.  **Re-run ArXiv Search (Neural):** Abandon the query "point cloud B-Rep" due to the persistent conflict with the "CLOUD" experiment name. Instead, use specific methodological keywords like "Neural CAD reconstruction", "Deep learning solid modeling", "Parametric CAD generation", or "Graph neural network B-Rep".
2.  **Execute Classical Search (Crossref):** Run the missing "Strategy B" search. Focus on "Reverse engineering" and "CAD model reconstruction" using "Laser scanning" or "3D scan data" instead of "point cloud" to avoid atmospheric noise. Target terms: "Reverse engineering primitive fitting", "Geometric segmentation CAD", "Topology recovery scan data".
3.  **Filter:** Explicitly exclude any result where the source category is "Astrophysics" or "Atmospheric Physics".
```

### Message 14

- Source: `WriterAgent`
- Type: `TextMessage`

```text
# Paper Search Report

## Query Understanding
The user seeks academic literature on **3D reconstruction** techniques that convert **point clouds** specifically into **Boundary Representation (B-Rep)** models.
*   **Key Requirements:** The output must be a B-Rep (vertices, edges, faces, topology), not just a triangle mesh or point cloud surface.
*   **Context:** This task is often referred to as "Reverse Engineering" or "CAD Reconstruction."
*   **Target Domain:** Computer-Aided Design (CAD), Computer Graphics, and Computer Vision.

## Search Strategy
The team executed a two-pronged search strategy to cover both modern data-driven methods and classical geometric approaches:

1.  **Modern Neural Approaches (ArXiv):**
    *   **Queries:** `point cloud to B-Rep boundary representation CAD reconstruction`
    *   **Filters:** Attempted to exclude atmospheric and astronomical terms (`-atmospheric -cosmic -weather`).
    *   **Goal:** Identify deep learning models (Transformers, GNNs) that generate structured CAD solids or B-Reps directly from unstructured inputs.

2.  **Classical Geometric Approaches (Crossref):**
    *   **Queries:** `point cloud B-Rep boundary representation CAD reconstruction` (and variations).
    *   **Goal:** Locate foundational papers on geometric primitive fitting (RANSAC), surface segmentation, and topology recovery (pre-2015 era).

## Candidate Papers
*Note: The search results were heavily contaminated by false positives regarding atmospheric science. The following list contains only the verified relevant papers found in the transcript.*

### Deep Learning & Data-Driven Approaches
*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   *Source:* arXiv
    *   *Focus:* Models B-Rep reconstruction as a chain complex problem (vertices, edges, faces).
    *   *Method:* Uses a sparse CNN encoder and a tri-path transformer decoder to predict geometric primitives and relationships, followed by global optimization for validity.
*   **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   *Source:* arXiv
    *   *Focus:* Reconstructs feature-based parametric CAD models directly from point clouds.
    *   *Method:* Autoregressive reconstruction using two transformer decoders and a cross-attention parameter optimizer.
*   **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** (2024)
    *   *Source:* arXiv
    *   *Focus:* A unified system for generating CAD models from text, images, *or point clouds*.
    *   *Method:* Leverages Large Language Models (LLMs) to align multimodal inputs (including point clouds) with CAD construction sequences.
*   **Towards High-Fidelity CAD Generation via LLM-Driven Program Generation... (FutureCAD)** (2026)
    *   *Source:* arXiv
    *   *Focus:* Text-to-CAD generation using LLMs and B-Rep grounding transformers.
    *   *Relevance:* While primarily text-to-CAD, it discusses the interaction between parametric operations and B-Rep primitives.

### Related & Datasets
*   **B-rep Matching for Collaborating Across CAD Systems** (2023)
    *   *Source:* arXiv
    *   *Focus:* Finding correspondences between B-Reps. Relevant for understanding B-Rep topology handling, though not a reconstruction paper.
*   **CAD-Estate: Large-scale CAD Model Annotation in RGB Videos** (2023)
    *   *Source:* arXiv
    *   *Focus:* Dataset creation for CAD model retrieval from video. Relevant for the context of CAD in real-world scenes.

### Classical / Limited Metadata
*   **Adaptive approach for point cloud based CAD model reconstruction** (2013)
    *   *Source:* Journal of Computer Applications (Crossref)
    *   *Limitation:* No abstract available; title suggests relevance but content could not be verified.
*   **Segmentation and Local Reconstruction of Turbine Blade Point Cloud** (2020)
    *   *Source:* CAD'20 (Crossref)
    *   *Limitation:* No abstract available; likely relevant to the "segmentation" step of B-Rep reconstruction.
*   **A Computational Framework for the Boundary Representation of Solid Sweeps** (2014)
    *   *Source:* CAD'14 (Crossref)
    *   *Limitation:* No abstract available; focuses on "Solid Sweeps," which is a specific B-Rep operation.

## Notes and Gaps
The search process encountered critical limitations that prevent a comprehensive report at this time:

1.  **Severe Keyword Contamination:**
    *   The term "point cloud" and "CLOUD" caused major interference. The top results consistently returned papers on the **CERN CLOUD experiment** (cosmic rays and cloud formation) and **Taurus Molecular Clouds** (astrophysics).
    *   Negative keywords failed to filter these out because the papers are titled "CLOUD" or contain the specific acronym.

2.  **Missing Foundational Literature:**
    *   The "Classical" search strand (pre-2015 geometric methods) failed to return retrievable results with abstracts.
    *   There is a complete absence of papers on **RANSAC primitive fitting**, **geometric surface segmentation**, and **topology recovery algorithms**, which are the standard traditional methods for B-Rep reconstruction.

3.  **Metadata Incompleteness:**
    *   Crossref results for classical papers did not include abstracts, making it impossible to verify if they actually target B-Rep output or just generic surface reconstruction (meshing).

## Recommended Next Steps
To complete this search successfully, the following actions are required:

1.  **Keyword Substitution:**
    *   Abandon the term "point cloud" in the classical search to avoid atmospheric noise. Use synonyms like **"laser scanning data"**, **"3D scan data"**, or **"range data"**.
    *   Use the domain term **"Reverse Engineering"** as the primary keyword for classical searches (e.g., `"Reverse Engineering" AND "CAD Model" AND "B-Rep"`).

2.  **Category Filtering:**
    *   Explicitly exclude arXiv categories `astro-ph`, `physics.atmos-ph`, and `physics.geo-ph`.

3.  **Targeted Classical Queries:**
    *   Query for specific sub-tasks known in B-Rep reconstruction: `"primitive fitting" AND "CAD"`, `"surface segmentation" AND "topology"`, `"feature extraction" AND "solid modeling"`.

TERMINATE
```
