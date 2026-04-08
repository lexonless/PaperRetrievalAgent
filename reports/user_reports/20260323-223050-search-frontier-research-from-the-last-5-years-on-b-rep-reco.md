# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T22:30:50
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to survey frontier research (2022–2026) on converting point clouds to CAD/B-rep models. The focus areas were:
*   **Point-cloud-to-CAD/B-rep methods**: Direct conversion to editable, parametric CAD models.
*   **Parametric surface reconstruction**: Fitting analytic surfaces (planes, cylinders, etc.) to point data.
*   **Topology recovery**: Inferring the connectivity between surfaces, edges, and vertices in a B-rep.
*   **Geometry-constrained modeling**: Applying geometric regularity constraints during reconstruction.

The search explicitly excluded mesh-only reconstruction, point cloud registration, dataset papers, and methods not producing a B-rep or CAD output.

## Search Strategy
The search was conducted in two phases:
1.  **Initial Broad Search**: Used queries like "point cloud to B-rep reconstruction" across arXiv, Crossref, and OpenAlex. This retrieved several relevant papers but also included off-topic results (e.g., registration, datasets).
2.  **Targeted Refinement**: A revised search used more specific queries like `"B-rep" reconstruction point cloud` to filter noise. However, the search remained limited primarily to OpenAlex and arXiv, missing broader coverage from specialized databases like DBLP and core conference proceedings (e.g., SIGGRAPH, CVPR, CAD). This limitation impacted the final set's diversity and relevance to "frontier research."

## Candidate Papers
The final retrieval contains **7 distinct papers** after merging duplicates. The following 5 are the strongest candidates that align with the query's focus on B-rep reconstruction from point clouds. Two papers were omitted: "Integrating Reverse Engineering for Digital Model Reconstruction..." (a review paper) and "A robust workflow for b-rep generation from image masks" (uses image input, not point clouds).

| Title | Year | Source | Link | Core Contribution | Relevance Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning** | 2024 | ACM TOG (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3658155) | Introduces a two-step method: a neural network learns to partition point clouds into Voronoi cells, each fitted with a single geometric primitive (plane, cylinder, etc.) to form a B-rep. | Directly addresses **parametric surface reconstruction** from point clouds. The "split-and-fit" paradigm is a clear example of a geometry-constrained, learning-based approach to B-rep generation. |
| **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** | 2022 | SIGGRAPH (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3528223.3530078) | Frames B-rep reconstruction as the joint detection of geometric primitives (surfaces, curves) and their topological relations, modeled holistically as a chain complex. | A foundational deep learning method for **topology-aware B-rep reconstruction**. It explicitly reasons about the connectivity between fitted primitives. |
| **HoLa: B-Rep Generation using a Holistic Latent Representation** | 2025 | ACM TOG (via OpenAlex) | [DOI](https://doi.org/10.1145/3730842) | Proposes a unified latent representation that jointly encodes the continuous geometry and discrete topology of B-rep primitives for generative modeling. | While the abstract does not explicitly mention point cloud input, the method is a state-of-the-art approach for **structured B-rep generation** and is highly relevant for topology recovery research. |
| **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** | 2023 | Journal of Computational Design and Engineering | [DOI](https://doi.org/10.1093/jcde/qwae005) | Presents a large-scale B-rep dataset and a sequence-based deep learning model for CAD reconstruction from various inputs, including point clouds. | Provides a **dataset and method** for learning-based CAD reconstruction. While not exclusively for point clouds, it is a relevant resource for data-driven B-rep research. |
| **A SEMI-AUTOMATED APPROACH TO MODEL ARCHITECTURAL ELEMENTS IN SCAN-TO-BIM PROCESSES** | 2023 | ISPRS Archives | [DOI](https://doi.org/10.5194/isprs-archives-xlviii-m-2-2023-1345-2023) | Describes a workflow for creating BIM models (which often use B-rep) from point cloud scans, focusing on architectural elements. | An applied example of **scan-to-B-rep (BIM)** in AEC. It highlights the practical challenges of reverse engineering from real-world scans. |

## Notes and Gaps
*   **Limited Scope & Source Diversity**: The search did not effectively cover core computer vision/graphics venues (CVPR, ICCV, ECCV, CAD conferences) via databases like DBLP. Consequently, several known frontier methods from 2022-2026 may be missing.
*   **Partial Focus Area Coverage**:
    *   **Parametric Surface Reconstruction**: Partially covered by "Split-and-Fit".
    *   **Topology Recovery**: Addressed by "ComplexGen" and "HoLa".
    *   **Geometry-Constrained Modeling**: Not explicitly covered by any retrieved paper. Methods that enforce geometric constraints (e.g., parallelism, orthogonality) during point cloud fitting are absent.
*   **Evidence Quality**: Relevance assessments were based on keyword matching in abstracts rather than a deep analysis of methodological contributions to the specified focus areas.
*   **Result Set**: The final set is small (5 core papers) and includes one applied BIM paper, indicating a gap in pure CAD geometry research from point clouds.

## Recommended Next Steps
1.  **Venue-Specific Search**: Conduct targeted searches on DBLP and conference websites using queries like:
    *   `"B-rep" point cloud site:cvpr.cc`
    *   `"CAD reconstruction" point cloud venue:"SIGGRAPH"`
    *   `"primitive fitting" point cloud "B-rep"`.
2.  **Expand Methodological Keywords**: Include terms like "geometric constraint solving," "regularization," "CSG reconstruction," and "feature recognition" to capture **geometry-constrained modeling** approaches.
3.  **Snowballing**: Use the citation lists of the core papers found ("Split-and-Fit," "ComplexGen") to identify related recent work.
4.  **Verify and Deepen**: For candidate papers, move beyond abstract keyword matching to review introductions and methodologies, ensuring they specifically address point cloud input and B-rep output.

TERMINATE
