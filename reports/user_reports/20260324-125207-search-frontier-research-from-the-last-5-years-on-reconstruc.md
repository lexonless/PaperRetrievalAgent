w# Paper Search Report

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
**Generated At:** 2026-03-24T12:52:07
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify frontier research (2022–2026) where the **primary task** is an **end-to-end pipeline** that takes **point clouds as input** and directly outputs **B-rep (Boundary Representation) models** as the final result. The search strictly excludes work focused only on subproblems (e.g., segmentation, fitting), intermediate representations (e.g., mesh, CSG), auxiliary modules, or alternative tasks.

## Search Strategy
The search was conducted in two phases:
1.  **Initial Phase:** Queries focused on general "point cloud to B-rep" terms, which returned many off-topic results (e.g., point cloud generation, detection, FE modeling).
2.  **Revised Phase:** Queries were refined to target the CAD and geometry processing community explicitly, using terms like "B-rep reconstruction from point clouds deep learning" and "point cloud to boundary representation CAD reconstruction." Sources included Crossref, OpenAlex, and arXiv.

## Candidate Papers
**The search did not clear the quality bar.** The retrieval process identified several promising leads, but the reviewer determined that the evidence was insufficient to verify that these papers meet the strict, end-to-end B-rep reconstruction criteria. The team hit the review budget without achieving a passing verification status.

### Verified Candidates
*No papers were verified as core candidates meeting all user criteria.*

### Unverified Leads
The following papers appear highly relevant based on titles and partial abstracts but require full-text verification to confirm they are strictly end-to-end point-cloud-to-B-rep reconstruction methods. They are presented as follow-up leads, not recommendations.

1.  **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref / SSRN
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Note:** Title and abstract snippet explicitly mention reconstructing "complete and topologically consistent B-rep models" from point clouds, making it a very strong candidate for verification.

2.  **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2310.02638v1
    *   **Note:** Described as an "end-to-end network to reconstruct featured CAD model from point cloud." Requires verification that the output is a B-rep and not another CAD representation.

3.  **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans** (2025)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2510.23429v1
    *   **Note:** Focuses on "converting 3D scans into parametric CAD representations," a core task in CAD reverse engineering. Needs confirmation of B-rep output.

## Notes and Gaps
*   **Evidence Gap:** The primary gap is a lack of conclusive, full-text evidence for the most promising papers. Verification was limited to partial abstracts, which often do not explicitly confirm the output format as a B-rep versus other CAD representations (e.g., a construction sequence, CSG tree).
*   **Field Nascent:** The strict definition of "end-to-end point-cloud-to-B-rep" appears to be a very specialized and emerging niche. Many related works reconstruct parametric CAD models or primitives, but the final representation may not always be a strict B-rep.
*   **Off-Topic Retrieval:** Initial searches were noisy, retrieving papers on point cloud generation, annotation, and detection, highlighting the need for precise terminology.

## Recommended Next Steps
1.  **Manual Verification:** For the leads above (especially Point2Brep and P2CADNet), obtain and review the full text to confirm:
    *   Input is explicitly a raw point cloud.
    *   Final output is explicitly a B-rep model.
    *   The paper's primary contribution is the reconstruction pipeline itself.
2.  **Venue-Specific Search:** Conduct targeted searches in key conferences and journals such as ACM Transactions on Graphics, Computer-Aided Design, SIGGRAPH, and CVPR using advanced search filters.
3.  **Citation Tracking:** Use the identified leads as seed papers for backward and forward citation analysis to find related work.
4.  **Broaden Definition (If Allowed):** If the strict B-rep requirement can be relaxed to "editable parametric CAD model," the pool of relevant, verified literature would likely be larger.

TERMINATE
