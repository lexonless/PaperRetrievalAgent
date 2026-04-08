# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T22:09:38
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) on converting point clouds to CAD/B-rep models. The search specifically targeted methods for:
*   **Parametric surface reconstruction**
*   **Topology recovery**
*   **Geometry-constrained modeling**

A strict exclusion was applied to **mesh-only reconstruction methods** that do not produce B-rep or CAD representations.

## Search Strategy
The search was conducted across multiple academic sources (OpenAlex, Crossref, arXiv) using a series of targeted queries. The primary strategy involved phrase searches combining core concepts like `"B-rep" "point cloud" reconstruction` and `"CAD reconstruction" point cloud` to enforce relevance. Efforts were made to filter out papers focused solely on point cloud registration, alignment, dataset creation, or mesh generation. A technical error prevented querying the DBLP computer science bibliography.

## Candidate Papers
The final retrieval yielded **10 paper entries**. After merging obvious duplicates (e.g., multiple entries for "ComplexGen" and "Split-and-Fit"), **5 distinct and relevant papers** were identified as strong candidates that align with the user's request. The following table presents these core papers, which represent the most credible recent research on point-cloud-to-B-rep reconstruction.

| Title | Year | Source | Link | Core Contribution | Relevance Note |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning** | 2024 | ACM (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3658155) / [arXiv](http://arxiv.org/abs/2406.05261) | Introduces a two-step method: a "split" via learned spatial partitioning (Voronoi diagram) followed by a "fit" of a single geometric primitive within each partition to acquire B-Reps. | Directly addresses **parametric surface reconstruction** from point clouds to produce CAD B-Reps. A core, learning-based frontier method. |
| **HoLa: B-Rep Generation using a Holistic Latent Representation** | 2025 | ACM (via OpenAlex) | [DOI](https://doi.org/10.1145/3730842) | Proposes a unified latent representation that jointly models the continuous geometry (surfaces, curves) and discrete **topology** of B-Rep primitives for generative CAD modeling. | Focuses on **topology-aware reconstruction** and generation of CAD B-Reps. A recent learning-based approach for holistic structure recovery. |
| **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** | 2022 | ACM (via OpenAlex/arXiv) | [DOI](https://doi.org/10.1145/3528223.3530078) / [arXiv](http://arxiv.org/abs/2205.14573) | Frames B-Rep reconstruction as the detection of vertices, edges, and surfaces, holistically modeled as a chain complex to achieve regularized and complete CAD models. | A foundational deep learning method for **CAD/B-rep reconstruction**, explicitly handling different orders of geometric primitives and their relations. |
| **Integrating Reverse Engineering for Digital Model Reconstruction and Remanufacturing of Mechanical Components: A Systematic Review** | 2025 | MDPI Metrology | [DOI](https://doi.org/10.3390/metrology5040066) | A systematic review investigating the application, challenges, and future directions of reverse engineering (RE) for reconstructing mechanical components, discussing B-rep and CAD reconstruction. | Provides a high-level overview of the field, challenges, and trends. While not a primary method paper, it contextualizes the research area. |
| **Graph-Based Point Cloud Surface Reconstruction Using B-Splines** | 2026 | VISIGRAPP Proceedings | [DOI](https://doi.org/10.5220/0014237600004084) | Title suggests a method for surface reconstruction from point clouds using B-Splines within a graph-based framework. | The title aligns with **parametric surface reconstruction**, but the abstract was unavailable for verification, leaving its output format (B-rep vs. mesh) uncertain. |

**Omitted Papers:** Five other retrieved entries were excluded from the detailed list above. Three were duplicate records of "ComplexGen" and "Split-and-Fit." The remaining two ("Depth-First Search Based 3D Point Cloud Coordinate Reconstruction Algorithm" and "PC^2: Projection-Conditioned Point Cloud Diffusion") were excluded because their abstracts indicate they focus on point cloud generation/coordinate reconstruction without any mention of producing CAD or B-rep models, thus violating the core exclusion criteria.

## Notes and Gaps
*   **Limited Candidate Pool:** The search yielded a relatively small number of distinct, high-confidence papers that strictly satisfy the point-cloud-to-B-rep requirement. This suggests the topic remains a challenging, niche area of research.
*   **Evidence Gaps:** For some promising titles (e.g., "Graph-Based Point Cloud Surface Reconstruction Using B-Splines"), only metadata was available, making it impossible to verify if the output is a B-rep and not a mesh.
*   **Venue and Source Gaps:** The search was hindered by the inability to query DBLP, a key source for computer science literature. Consequently, there may be relevant papers from major graphics and CAD conferences (e.g., SIGGRAPH, SGP, CAD) that were not captured.
*   **Thematic Gaps:** While **parametric surface reconstruction** and **topology recovery** are represented by the core candidates, the specific subtopic of **geometry-constrained modeling** from point clouds is not clearly addressed by the retrieved set. Furthermore, most identified methods are data-driven/learning-based; there may be a gap in coverage of recent optimization-based or classical geometric fitting approaches.

## Recommended Next Steps
1.  **Targeted Venue Search:** Manually search the proceedings of key conferences (ACM SIGGRAPH, Symposium on Geometry Processing, ASME/ACM Design Automation Conference) from 2022-2026 for terms like "B-rep", "point cloud", and "reverse engineering."
2.  **Query Refinement:** Execute follow-up searches using more specific terms such as `"B-spline fitting" point cloud CAD` or `"constructive solid geometry" reconstruction point cloud` to target geometry-constrained and parametric methods.
3.  **Citation Tracking:** Use the strong candidate papers (Split-and-Fit, HoLa, ComplexGen) as seeds for forward and backward citation analysis to discover related recent work.
4.  **Source Diversification:** Attempt the DBLP search again at a later time or use alternative bibliographic databases like Scopus or Web of Science to improve coverage.

TERMINATE
