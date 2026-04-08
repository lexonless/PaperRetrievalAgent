# Paper Search Report

**Query:** Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

Return 5-10 relevant papers with:
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
**Generated At:** 2026-03-24T23:25:25
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify recent research (2022–2026) on methods that reconstruct or generate Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on works where point clouds are the primary input and a structured B-rep is the explicit output, encompassing reverse engineering and geometric deep learning approaches.

## Search Strategy
The search was conducted in three phases:
1.  **Initial Broad Search:** Queries like "B-rep reconstruction from point clouds" and "CAD reverse engineering from scanned point cloud" were used to capture a wide candidate set from Crossref, OpenAlex, and arXiv.
2.  **Targeted Verification:** A second round used precise queries (e.g., `"point cloud" "B-rep" reconstruction`) to force co-occurrence of key terms and verify the input modality of promising candidates.
3.  **Review & Filtering:** Papers were assessed against hard requirements: publication within 2022-2026, point cloud as a main input, and B-rep/CAD model as the target output. Ambiguous candidates were filtered out.

## Candidate Papers
The following papers represent the strongest, verified candidates for point-cloud-to-B-rep reconstruction from the last five years.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref / SSRN
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Core Contribution:** Proposes a geometry-aware framework that integrates learning-based inference with explicit parametric fitting to reconstruct complete, topologically consistent B-rep models from unstructured point clouds.
    *   **Relevance Note:** **Direct match.** The abstract explicitly states the method reconstructs B-reps "from unstructured point clouds."

*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022)
    *   **Source:** ACM TOG / arXiv
    *   **Link:** https://doi.org/10.1145/3528223.3530078
    *   **Core Contribution:** Frames B-rep reconstruction as the detection of vertices, edges, and surfaces, holistically modeled as a chain complex. Presents an end-to-end network that directly predicts the structured B-rep from an input point cloud.
    *   **Relevance Note:** **Direct match.** The paper's introduction and figures explicitly demonstrate reconstruction "from point clouds."

*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2412.14042v2
    *   **Core Contribution:** Addresses CAD reverse engineering by reconstructing parametric sketch and operation sequences from 3D representations, explicitly including point clouds.
    *   **Relevance Note:** **Direct match.** The abstract defines the problem as reconstructing CAD sequences "from 3D representations such as point clouds."

*   **CAD-SIGNet: CAD Language Inference from Point Clouds using Layer-wise Sketch Instance Guided Attention** (2024)
    *   **Source:** CVPR / arXiv
    *   **Link:** https://arxiv.org/abs/2402.17678v1
    *   **Core Contribution:** An end-to-end, autoregressive architecture designed to recover a CAD model's design history (sketch-and-extrusion sequence) from a 3D scan/point cloud.
    *   **Relevance Note:** **Direct match.** The abstract states the aim is to uncover the CAD process "given its 3D scan."

*   **TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** https://arxiv.org/abs/2407.12702v2
    *   **Core Contribution:** An end-to-end transformer-based architecture that predicts a CAD construction sequence directly from an input point cloud, using a hierarchical refinement strategy.
    *   **Relevance Note:** **Direct match.** The paper's core task is predicting "the CAD sequence from a point cloud" for 3D reverse engineering.

## Notes and Gaps
*   **Methodological Focus:** The state-of-the-art is dominated by deep learning approaches, particularly transformer-based and graph-based networks that predict structured outputs (sequences, graphs, or complex hierarchies).
*   **Trend:** A clear shift from classic geometric fitting to data-driven, holistic reconstruction that jointly reasons about geometry and topology.
*   **Evidence Gaps:** Several initially retrieved papers (e.g., Split-and-Fit, GraphBrep, Brep2Seq) were excluded from the final list because their provided abstracts did not explicitly confirm point cloud as the primary input, highlighting a gap in easily verifiable metadata for this niche.
*   **Scope:** The search focused on academic literature. Patents or industry-specific techniques may not be covered.

## Recommended Next Steps
1.  **Explore Hybrid Methods:** Investigate recent works that combine the robustness of classical geometric processing with the high-level reasoning of learning-based models.
2.  **Benchmark Datasets:** Examine the datasets used by these papers (e.g., ABC dataset, Fusion 360 Gallery) to understand the scope and limitations of current evaluation.
3.  **Downstream Applications:** Look for research applying these reconstruction methods to specific domains like digital twins, legacy part redesign, or additive manufacturing preparation.
4.  **Follow-up on Leads:** Papers like **HoLa: B-Rep Generation using a Holistic Latent Representation** (2025) and **BrepGPT** (2025) appeared relevant by title but lacked explicit point-cloud input confirmation in snippets; they represent strong leads for manual follow-up.

TERMINATE
