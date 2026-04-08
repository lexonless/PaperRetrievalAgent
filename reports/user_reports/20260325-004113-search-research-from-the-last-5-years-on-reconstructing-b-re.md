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
**Generated At:** 2026-03-25T00:41:13
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The search aimed to find recent research (2022–2026) on methods for reconstructing, generating, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data. The focus was on core technical contributions where a point cloud is the primary input and a structured, often parametric, CAD model is the output.

## Search Strategy
The search was conducted in three phases using Crossref, OpenAlex, and arXiv.
1.  **Initial Phase:** Direct queries like "reconstruct B-rep from point cloud" were executed, yielding a preliminary set that was overly focused on BIM/building reconstruction.
2.  **Revision Phase:** Based on reviewer feedback, the search was broadened with queries such as "point cloud to CAD model reconstruction" and "deep learning for B-rep generation" to capture a more diverse and technically focused literature on general CAD reconstruction.
3.  **Final Set:** The revised retrieval successfully identified a strong set of papers spanning neural, hybrid, and optimization-based methods, all within the specified timeframe and with clear evidence of the point-cloud-to-B-rep mapping.

## Candidate Papers
The following papers represent the strongest and most directly relevant candidates from the search.

*   **Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds** (2024)
    *   **Source:** 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
    *   **Link:** https://doi.org/10.1109/cvpr52733.2024.00361
    *   **Core Contribution:** Proposes a hybrid analytic-neural reconstruction scheme that bridges segmented point clouds to structured CAD models.
    *   **Relevance:** Direct match. Explicitly targets CAD model reconstruction from point clouds with a structured output.

*   **An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds** (2025)
    *   **Source:** Engineering Applications of Artificial Intelligence
    *   **Link:** https://doi.org/10.1016/j.engappai.2025.113107
    *   **Core Contribution:** Presents a framework that directly maps point clouds to CAD modeling sequences for automated, parametric reconstruction.
    *   **Relevance:** Direct match. Focuses on generating editable, parametric CAD models compatible with standard software from point cloud input.

*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2412.14042v2
    *   **Core Contribution:** Translates a point cloud into executable Python code that reconstructs the corresponding CAD model.
    *   **Relevance:** Direct match. Addresses the core problem of reverse engineering CAD construction sequences from point clouds.

*   **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2310.02638v1
    *   **Core Contribution:** An end-to-end network to reconstruct featured CAD models from point clouds in an autoregressive manner.
    *   **Relevance:** Direct match. An early end-to-end deep learning approach for this task.

*   **Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction** (2025)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2505.02043v3
    *   **Core Contribution:** Learns to directly predict the explicit, parametric primitives (sketch-based extrusion) of CAD models from point clouds.
    *   **Relevance:** Direct match. Focuses on recovering topology and primitives through direct prediction.

*   **CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2402.17678v1
    *   **Core Contribution:** Recovers a CAD model's full design history (sketch-and-extrusion sequence) from an input point cloud.
    *   **Relevance:** Direct match. Targets the inference of the complete, editable construction sequence.

*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   **Source:** ACM SIGGRAPH / arXiv
    *   **Link:** https://doi.org/10.1145/3528223.3530078
    *   **Core Contribution:** Frames B-rep reconstruction as the detection of geometric primitives (vertices, edges, surfaces) and their correspondence, solved via global optimization.
    *   **Relevance:** Direct match. A foundational learning-based method that explicitly targets B-rep reconstruction.

*   **Draw Step by Step: Reconstructing CAD Construction Sequences from Point Clouds via Multimodal Diffusion** (2024)
    *   **Source:** 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
    *   **Link:** https://doi.org/10.1109/cvpr52733.2024.02564
    *   **Core Contribution:** Unifies CAD point clouds and construction sequences at the token level using a multimodal diffusion approach.
    *   **Relevance:** Closely related. Focuses on sequence reconstruction, a key step towards editable B-rep output.

*   **Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds** (2025)
    *   **Source:** Journal of Electronic Research and Application
    *   **Link:** https://doi.org/10.26689/jera.v9i6.13185
    *   **Core Contribution:** Reconstructs high-accuracy, editable parametric CAD models from multi-view RGB-D point clouds.
    *   **Relevance:** Direct match. Specifically addresses parametric model recovery from point cloud data.

*   **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** Journal of Computational Design and Engineering
    *   **Link:** https://doi.org/10.1093/jcde/qwae005
    *   **Core Contribution:** Introduces a dataset and a network that transforms B-rep models into editable modeling sequences, applicable to point cloud reconstruction.
    *   **Relevance:** Closely related. While primarily a dataset and model for sequence generation, it is applied to point cloud reconstruction as a downstream task.

## Notes and Gaps
*   **Methodological Diversity:** The retrieved papers cover a spectrum of approaches: hybrid analytic-neural (Point2CAD), autoregressive sequence-to-sequence learning (P2CADNet, autoregressive framework), direct primitive prediction (Point2Primitive), and optimization-based B-rep assembly (ComplexGen).
*   **Evidence Level:** All papers are supported by abstract-level evidence confirming the point-cloud-to-CAD/B-rep mapping. Full-text review would be needed for deeper methodological details and evaluation.
*   **Potential Gaps:** The search was highly effective for recent data-driven methods. There may be fewer purely geometric or optimization-based approaches from the last two years, as the field has shifted toward deep learning. Literature on reconstructing complex, highly organic B-rep shapes (e.g., Class-A automotive surfaces) from point clouds appears less represented.

## Recommended Next Steps
1.  **Detailed Review:** Examine the full text of the top direct matches (e.g., Point2CAD, the 2025 autoregressive framework, CAD-Recode) to understand their architectures, datasets, and limitations.
2.  **Trend Analysis:** The literature shows clear trends: the dominance of autoregressive and sequence-based models, the integration of large language/multimodal models (CAD-MLLM, Seek-CAD), and a strong focus on recovering **editable parametric history** rather than just static B-rep geometry.
3.  **Challenge Identification:** Key open challenges highlighted across these works include: handling complex topological variations, robustness to noisy and incomplete point clouds, generalizing to diverse CAD domains beyond primitives, and achieving true, lossless reconstruction of original design intent.
4.  **Follow-up Search:** To explore adjacent areas, consider searching for "sketch reconstruction from point clouds" or "geometric constraint solving for CAD reconstruction."

TERMINATE
