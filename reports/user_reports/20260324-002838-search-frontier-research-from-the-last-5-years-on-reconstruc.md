# Paper Search Report

**Query:** Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus only on papers where the main task is to take point clouds as input and directly reconstruct B-rep outputs as the final representation.

Prioritize methods that explicitly address the full reconstruction pipeline.

Exclude papers whose main contribution is only a subproblem, intermediate representation, auxiliary module, downstream application, or alternative task rather than end-to-end point-cloud-to-B-rep reconstruction.

A paper should not be treated as a core candidate unless reconstructing B-rep from point clouds is the primary task and final output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it is truly an end-to-end point-cloud-to-B-rep reconstruction method

Then summarize:
- major method categories
- recent trends
- open challenges

Be strict: prefer fewer but truly on-task papers over loosely related reconstruction, CAD, or geometric modeling papers.
**Generated At:** 2026-03-24T00:28:38
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) where the primary task is an end-to-end pipeline that takes a point cloud as input and directly outputs a Boundary Representation (B-rep) model as the final, reconstructed representation. The search strictly excluded work focused on subproblems (e.g., segmentation, fitting), intermediate representations (e.g., mesh, implicit surface, voxel), or alternative tasks (e.g., mesh-to-B-rep, sketch-based modeling).

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv. Initial broad queries (e.g., "point cloud B-rep reconstruction end-to-end") returned many irrelevant results concerning mesh reconstruction, plant modeling, and editorial documents. The strategy was revised to include more precise CAD and reverse engineering terminology (e.g., "point cloud to CAD B-rep reconstruction", "reverse engineering B-rep from point cloud"). Despite these adjustments, the automated retrieval lacked the necessary semantic filtering and abstract-level verification to confirm a paper's final output representation, resulting in a candidate pool with unverified relevance.

## Candidate Papers
**Total Papers Retrieved:** 10 (from the final retrieval JSON).
**Selection Rule:** The search did not yield any papers that could be verified as core candidates meeting the strict user criteria. All retrieved entries have an `evidence_level` of "title_only" and a `verification_status` of "weak," meaning their relevance to end-to-end point-cloud-to-B-rep reconstruction could not be confirmed. Below is a summary of the retrieved papers, illustrating the gap between the query and the results.

*   **Building CAD Model Reconstruction from Point Clouds via Instance Segmentation, Signed Distance Function, and Graph Cut** (2023, ICCVW)
    *   **Relevance Note:** The title is promising but lacks verification. The method uses a Signed Distance Function (SDF), which is typically an intermediate representation for surface or mesh reconstruction. Without abstract evidence, it is unclear if the final output is a B-rep model or a mesh.
*   **Deep learning-based 3D point cloud classification: A systematic survey and outlook** (2023)
    *   **Relevance Note:** Clearly off-topic. This is a survey on classification, not reconstruction.
*   **Deep Learning-Based Surface Reconstruction from Point Clouds** (2024)
    *   **Relevance Note:** The title indicates "surface reconstruction," which strongly suggests mesh or implicit surface output, not B-rep.
*   **Extraction and Reconstruction of Articulated Robots from Point Clouds of Manufacturing Plants** (2024, CAD'24 & CADAPS)
    *   **Relevance Note:** While related to CAD and manufacturing, the title does not specify the output representation. Reconstruction of "articulated robots" could result in a kinematic model or mesh, not necessarily a B-rep.
*   **Application of Poisson Surface Reconstruction with Envelope Constraints to TLS Point Clouds...** (2025, CAD'25)
    *   **Relevance Note:** Explicitly uses "Poisson Surface Reconstruction," a classic mesh generation technique. This is not a B-rep reconstruction method.
*   **Low-poly Mesh Generation from Low-quality Point Clouds Based on Projections** (2025, CAD'25)
    *   **Relevance Note:** Explicitly states "Mesh Generation" as the output, which violates the core requirement.
*   **Decision letters and reviews for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"** (2025)
    *   **Relevance Note:** Editorial documents for a paper on leaf reconstruction, which is entirely unrelated to CAD/B-rep modeling.

**Conclusion:** No verified, on-topic papers were found within the 2022-2026 window that satisfy the strict definition of end-to-end point-cloud-to-B-rep reconstruction.

## Notes and Gaps
*   **Evidence Gap:** The primary limitation is the lack of abstract or content-level evidence for candidate papers. For a niche task where the output representation is the defining characteristic, title-based retrieval is insufficient.
*   **Field Scarcity:** The search suggests the specific task of **direct, end-to-end B-rep reconstruction from point clouds** is a very nascent or narrowly defined research area within the 2022-2026 window. Much of the published work in "CAD reconstruction from scans" may focus on producing meshes, segmented point clouds, or CSG trees, not boundary representations.
*   **Semantic Noise:** Queries for "reconstruction" and "point clouds" naturally retrieve a vast literature on mesh and surface reconstruction, which dominates the search results and obscures the target niche.
*   **Venue Focus:** Relevant papers may be concentrated in specific venues (e.g., the *Computer-Aided Design* journal/conference, SIGGRAPH, SPM) and may not be effectively indexed by broad academic search queries without venue filtering.

## Recommended Next Steps
1.  **Manual Venue Search:** Conduct a targeted, manual search of recent proceedings (2022-2026) from key venues:
    *   *Computer-Aided Design* (CAD) journal and conference.
    *   ACM SIGGRAPH / SIGGRAPH Asia.
    *   Symposium on Solid and Physical Modeling (SPM).
    *   CVPR/ICCV/ECCV workshops on 3D Vision and Graphics.
2.  **Citation Tracking:** Identify seminal pre-2022 papers on B-rep reconstruction (e.g., from the early 2020s) and use forward citation tools (Google Scholar, Semantic Scholar) to find newer works that cite them.
3.  **Broaden Scope with Context:** If the strict 2022-2026 window yields no results, consider presenting a report that:
    *   Acknowledges the scarcity of recent, strictly compliant papers.
    *   Provides a brief overview of the closest related works (e.g., point cloud to CAD mesh, point cloud to CSG) as context.
    *   Highlights foundational or influential pre-2022 papers that define the problem space.
4.  **Refine Problem Definition:** Engage with the user to clarify if reconstructions that output a **CAD mesh** (which is a surface but not a boundary representation with topological edges and faces) would be of interest, as this is a more common output in recent learning-based "CAD reconstruction" literature.

TERMINATE
