# Paper Search Report

**Query:** Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

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

Rank the most directly relevant papers first, but do not over-filter papers merely because they use multi-stage pipelines or different wording for the same task.
**Generated At:** 2026-03-25T00:49:43
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
*   **Core Task:** Find recent research (2022–2026) on methods to reconstruct, generate, or recover Boundary Representation (B-rep) CAD models from 3D point cloud data.
*   **Input/Output Focus:** Point clouds as the primary input; editable, structured B-rep or parametric CAD models as the target output.
*   **Scope:** Includes multi-stage pipelines (e.g., primitive detection → B-rep assembly) and deep learning approaches. Excludes mesh-only reconstruction and surface fitting without B-rep structure.

## Search Strategy
*   **Sources:** Crossref, OpenAlex, and arXiv (after initial rate limits were resolved).
*   **Query Evolution:** Initial broad queries retrieved many off-topic papers. Refined queries targeted specific terminology: `"point cloud to B-rep reconstruction deep learning"`, `"reverse engineering CAD model from 3D scan point cloud"`, and `"primitive fitting B-rep reconstruction point cloud"`.
*   **Filtering:** Required evidence of B-rep/CAD output in abstracts to ensure relevance, excluding papers on garment CAD, human pose estimation, and pipe networks.

## Candidate Papers
The search successfully identified a strong set of core papers directly addressing the point-cloud-to-B-rep reconstruction problem.

1.  **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   **Source:** arXiv / OpenAlex
    *   **Link:** [http://arxiv.org/abs/2205.14573](http://arxiv.org/abs/2205.14573)
    *   **Core Contribution:** Proposes a neural framework that detects vertices, edges, and surfaces from a point cloud and models their relationships as a "chain complex," followed by global optimization to produce a valid, complete B-rep.
    *   **Relevance:** Direct match. Introduces a holistic structure-aware approach for B-rep reconstruction from point clouds.

2.  **HoLa: B-Rep Generation using a Holistic Latent Representation** (2025)
    *   **Source:** OpenAlex (ACM)
    *   **Link:** [https://doi.org/10.1145/3730842](https://doi.org/10.1145/3730842)
    *   **Core Contribution:** Introduces a compact latent space that encodes surface geometry and infers topological connections (curves, vertices) via a neural intersection network. Enables diffusion-based generation from point clouds and other inputs.
    *   **Relevance:** Direct match. Aims to simplify B-rep generation by reducing ambiguity and improving validity rates.

3.  **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** [http://arxiv.org/abs/2412.14042v2](http://arxiv.org/abs/2412.14042v2)
    *   **Core Contribution:** Translates a point cloud into executable Python code that reconstructs the CAD model via sketch-and-extrude sequences, leveraging a pre-trained Large Language Model (LLM) as a decoder.
    *   **Relevance:** Direct match. Focuses on recovering editable, parametric CAD construction sequences from point clouds.

4.  **CAD-SIGNet: CAD Language Inference from Point Clouds Using Layer-Wise Sketch Instance Guided Attention** (2024)
    *   **Source:** OpenAlex (CVPR)
    *   **Link:** [https://doi.org/10.1109/cvpr52733.2024.00451](https://doi.org/10.1109/cvpr52733.2024.00451)
    *   **Core Contribution:** An autoregressive, end-to-end network that recovers a full CAD design history (sketch-and-extrusion sequence) from a point cloud, offering multiple plausible next-step choices for interactive reverse engineering.
    *   **Relevance:** Direct match. Recovers the procedural modeling sequence, a key aspect of editable CAD.

5.  **GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation** (2025)
    *   **Source:** arXiv
    *   **Link:** [http://arxiv.org/abs/2507.04765v1](http://arxiv.org/abs/2507.04765v1)
    *   **Core Contribution:** Represents B-rep topology explicitly as a graph and uses a graph diffusion model to learn connectivity between surfaces, aiming for more computationally efficient generation.
    *   **Relevance:** Direct match. Proposes a novel structure-aware representation to improve the efficiency of direct B-rep generation.

6.  **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   **Source:** arXiv
    *   **Link:** [http://arxiv.org/abs/2310.02638v1](http://arxiv.org/abs/2310.02638v1)
    *   **Core Contribution:** Presents an end-to-end transformer-based network with a parameter optimizer to reconstruct featured, parametric CAD models directly from point clouds in an autoregressive manner.
    *   **Relevance:** Direct match. Positions itself as a baseline for end-to-end featured CAD reconstruction from points.

7.  **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** OpenAlex (Journal of Computational Design and Engineering)
    *   **Link:** [https://doi.org/10.1093/jcde/qwae005](https://doi.org/10.1093/jcde/qwae005)
    *   **Core Contribution:** Introduces a hierarchical transformer network that converts B-reps into sequences of modeling operations and applies it to point cloud reconstruction among other tasks.
    *   **Relevance:** Direct match. The method and large-scale dataset support CAD model recovery from point clouds.

8.  **FROM POINT CLOUD TO CAD-MODEL BASED ON AI** (2022)
    *   **Source:** Crossref (ICCAS)
    *   **Link:** [https://doi.org/10.3940/rina.iccas.2022.18](https://doi.org/10.3940/rina.iccas.2022.18)
    *   **Core Contribution:** Describes an applied industrial pipeline using AI for object recognition in point clouds (specifically piping components) to automatically generate native CAD models for shipbuilding.
    *   **Relevance:** Closely related. Demonstrates a practical, domain-specific application of the core problem.

9.  **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** (2024)
    *   **Source:** arXiv
    *   **Link:** [http://arxiv.org/abs/2411.04954v3](http://arxiv.org/abs/2411.04954v3)
    *   **Core Contribution:** A multimodal large language model system that can generate CAD models from text, images, point clouds, or combinations thereof.
    *   **Relevance:** Closely related. Point cloud is one supported input modality for a unified CAD generation system.

## Notes and Gaps
*   **Methodological Trends:** The field is dominated by deep learning. Key approaches include:
    *   **Sequence Generation:** Modeling CAD reconstruction as the prediction of a sequence of modeling operations or code (CAD-Recode, CAD-SIGNet, Brep2Seq).
    *   **Structure-Aware Networks:** Explicitly modeling B-rep topology through graphs (GraphBrep) or complex structures (ComplexGen).
    *   **Generative Models:** Using diffusion models (HoLa) and leveraging LLMs (CAD-MLLM, CAD-Recode) for generation and inference.
*   **Open Challenges:** Based on the papers, persistent challenges include:
    *   Handling real-world scan noise, outliers, and incompleteness.
    *   Reconstructing complex topological structures and high-level design intent.
    *   Ensuring the validity and manufacturability of generated B-rep models.
    *   Achieving interactive speeds and providing interpretable, editable outputs for designers.
*   **Coverage Gap:** The literature heavily relies on synthetic or clean CAD datasets (e.g., DeepCAD, Fusion 360). Papers evaluating performance on noisy, real-world scanned point clouds of arbitrary mechanical objects are less prominent.

## Recommended Next Steps
1.  **Explore Foundational Works:** Investigate highly cited predecessors to these papers (pre-2022) to understand the evolution from traditional geometric fitting to data-driven methods.
2.  **Focus on Real-World Data:** Search for papers that specifically address "noisy point cloud" or "real scan" B-rep reconstruction to address the identified gap.
3.  **Cross-Disciplinary Review:** Examine literature from the manufacturing and reverse engineering communities, which may use different terminology but address similar applied problems.
4.  **Track Emerging Venues:** Follow publications from top-tier computer vision/graphics conferences (CVPR, SIGGRAPH, ICCV) and CAD-specific journals (Computer-Aided Design) for the latest advances.

TERMINATE
