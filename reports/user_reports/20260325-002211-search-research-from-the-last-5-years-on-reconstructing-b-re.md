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
**Generated At:** 2026-03-25T00:22:11
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to find recent research (2022–2026) on methods for reconstructing, generating, or recovering Boundary Representation (B-rep) CAD models directly from point cloud data. The focus was on core contributions where point clouds are the primary input and a structured B-rep or parametric CAD model is the output.

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv using a series of targeted queries:
*   `point cloud to B-rep reconstruction 2022 2026`
*   `B-rep generation from scanned point cloud`
*   `parametric CAD reconstruction point cloud`

The strategy aimed to capture a diverse set of methods, including deep learning, geometric reasoning, and traditional fitting approaches, while verifying that point clouds were a central input.

## Candidate Papers
The following papers represent the strongest, verified candidates for point-cloud-to-B-rep reconstruction from the last five years.

| Title | Year | Source | Link | Core Contribution | Relevance Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** | 2026 | Crossref (SSRN) | [Link](https://doi.org/10.2139/ssrn.6172545) | A two-stage framework integrating learning-based segmentation with explicit parametric surface fitting and geometric reasoning to produce topologically consistent B-reps. | **Direct match.** Explicitly reconstructs B-rep models from unstructured point clouds. |
| **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** | 2023 | arXiv / OpenAlex | [Link](http://arxiv.org/abs/2310.02638v1) | An end-to-end transformer-based network that maps point clouds directly to sequences of CAD modeling operations (feature-based parametric CAD). | **Direct match.** Focuses on reconstructing editable, featured CAD models from point clouds. |
| **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** | 2024 | arXiv | [Link](http://arxiv.org/abs/2412.14042v2) | Translates a point cloud into executable Python code that represents the CAD sketch-extrude sequence, leveraging a pre-trained LLM as a decoder. | **Direct match.** Outputs parametric CAD code (which defines a B-rep) directly from point clouds. |
| **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** | 2022 | arXiv | [Link](http://arxiv.org/abs/2205.14573v1) | A neural framework that detects vertices, edges, and surfaces from a point cloud and models their relationships as a chain complex to recover a regularized B-rep. | **Direct match.** Holistically reconstructs B-rep structure from point clouds. |
| **Point2Primitive: CAD Reconstruction from Point Cloud by Direct Primitive Prediction** | 2025 | arXiv | [Link](http://arxiv.org/abs/2505.02043v3) | A transformer-based framework that treats sketch reconstruction as a set prediction problem, directly outputting explicit, parametric primitives from a point cloud. | **Direct match.** Aims for precise, editable CAD models by directly predicting sketch curves and extrusion parameters. |
| **An autoregressive framework for reconstructing editable parametric computer-aided design models from point clouds (RenCAD)** | 2025 | *Engineering Applications of Artificial Intelligence* (OpenAlex) | [Link](https://doi.org/10.1016/j.engappai.2025.113107) | An end-to-end autoregressive transformer that maps point cloud representations directly to parametric CAD modeling sequences. | **Direct match.** Focuses on automated, editable parametric reconstruction from point clouds. |
| **NeurCADRecon: Neural Representation for Reconstructing CAD Surfaces by Enforcing Zero Gaussian Curvature** | 2024 | *ACM Transactions on Graphics* (OpenAlex) | [Link](https://doi.org/10.1145/3658171) | A self-supervised neural method that reconstructs CAD surfaces from point clouds by encouraging developability (near-zero Gaussian curvature). | **Closely related.** Reconstructs CAD-quality surfaces (a key component of B-reps) from low-quality point clouds. |
| **Surface and Edge Detection for Primitive Fitting of Point Clouds (SED-Net)** | 2023 | *SIGGRAPH* (OpenAlex) | [Link](https://doi.org/10.1145/3588432.3591522) | A network that jointly learns parametric surfaces (including B-spline patches) and edges from point clouds for assembly into a regularized CAD model. | **Closely related.** Outputs parametric surfaces and edges, which are fundamental to constructing a B-rep. |

## Notes and Gaps
*   **Methodological Focus:** The retrieved literature is heavily dominated by data-driven, deep learning approaches (transformers, CNNs). There is less emphasis on purely optimization-based or classical geometric fitting pipelines in the most recent core papers.
*   **Output Representation:** There is a clear trend towards generating not just static B-reps but **editable, parametric CAD sequences** (e.g., sketch-extrude operations or Python code), which is a higher-level, more usable output for CAD workflows.
*   **Application-Specific Work:** Some relevant papers focus on niche applications (e.g., steel structures, marine propellers). While they contribute to the reverse engineering theme, their methods may be less generalizable.
*   **Dataset Dependency:** Many learning-based methods rely on specific datasets of synthetic CAD models (e.g., ABC dataset), which may affect performance on noisy, real-world scanned data.

## Recommended Next Steps
1.  **Explore Hybrid Methods:** Investigate research that more tightly couples learned initial guesses with rigorous geometric optimization and constraint solving to improve robustness and precision.
2.  **Benchmark Traditional vs. Learned:** Conduct a comparative review of classical primitive fitting benchmarks (like SHREC tracks) against newer deep learning methods to identify strengths and failure modes.
3.  **Focus on Real-World Data:** Look for papers that specifically address challenges like severe occlusion, noise, and incomplete data from real-world laser scans, which may be more prevalent in applied journals (e.g., *Automation in Construction*, *Journal of Computing in Civil Engineering*).
4.  **Review Foundational Datasets:** Examine papers introducing key datasets (e.g., ABC, Fusion 360 Gallery) to understand the data landscape that drives current model development.

TERMINATE
