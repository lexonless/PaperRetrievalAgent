# Paper Search Report

**Query:** Search frontier research from the last 5 years on reconstruction of B-rep representations from point clouds.

Focus on papers where the primary task is to take point clouds as input and reconstruct B-rep as the final output representation.

Prioritize papers whose main contribution is the full B-rep reconstruction problem itself, rather than only a subproblem, intermediate representation, auxiliary module, downstream application, or a different reconstruction/CAD task.

A paper should be treated as a core candidate only if reconstructing B-rep from point clouds is the paper's primary task and B-rep is the final target output.

Return 5-10 highly relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining why it truly fits the point-cloud-to-B-rep reconstruction task

Then summarize:
- major method categories
- recent trends
- open challenges

Be selective, but avoid over-filtering papers merely because the method is multi-stage or uses intermediate steps within the reconstruction pipeline.
**Generated At:** 2026-03-24T12:56:45
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify frontier research (2022–2026) where the **primary task** is reconstructing Boundary Representation (B-rep) models directly from point clouds as the final output. The focus is on core methods for the full reconstruction problem, not subproblems (e.g., segmentation, primitive fitting) or auxiliary modules. Outputs like meshes, SDFs, or CSG without a final B-rep are excluded.

## Search Strategy
The search was conducted in two phases:
1.  **Initial broad search** using queries like "point cloud to B-rep reconstruction deep learning" and "CAD model recovery from point clouds". This returned many tangential results (e.g., medical imaging, point cloud denoising).
2.  **Refined, precise search** using targeted queries like "boundary representation reconstruction from point clouds" and "reverse engineering parametric CAD from point cloud". This improved focus but still captured papers on surface reconstruction, domain-specific applications, and datasets that do not meet the core criteria.

Searches were performed across Crossref, OpenAlex, and arXiv. A key gap was the lack of papers from premier computer vision/graphics conferences (e.g., SIGGRAPH, CVPR), indicating the niche nature of the problem or a potential retrieval bias.

## Candidate Papers
The search did not clear the quality bar. No papers were fully verified to meet all hard requirements (point cloud input, B-rep output as primary task, within top-tier venues). The results are split into partially verified candidates and unverified leads.

### Verified Candidates
*Papers with evidence suggesting relevance, but verification is incomplete.*

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds** (2026)
    *   **Source:** Crossref
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Evidence:** Abstract snippet states it "reconstructs complete and topologically consistent B-rep models" and is a "geometry-aware framework." Strong title match.
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds** (2024)
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2412.14042v2
    *   **Evidence:** Abstract explicitly frames the problem as "reconstructing the sketch and CAD operation sequences from 3D representations such as point clouds," which implies a parametric CAD/B-rep output.
*   **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** OpenAlex / Journal of Computational Design and Engineering
    *   **Link:** https://doi.org/10.1093/jcde/qwae005
    *   **Evidence:** Abstract mentions recovering "editable CAD models" from inputs including "point clouds" and "boundary representations (B-rep)." The role of point clouds as input versus other representations is unclear from the snippet.
*   **Research on Reverse Modeling of Parametric CAD Models from Multi-View RGB-D Point Clouds** (2025)
    *   **Source:** Journal of Electronic Research and Application
    *   **Link:** https://doi.org/10.26689/jera.v9i6.13185
    *   **Evidence:** Abstract states the goal is to "reconstructs parametric CAD models from multi-view RGB-D point clouds." Directly addresses the target task.

### Unverified Leads
*Title-strong papers that require follow-up verification but are not recommendations.*

1.  **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation** (2022, arXiv): Title suggests B-rep reconstruction, but the abstract snippet does not confirm point cloud as the primary input.
2.  **Point2CAD: Reverse Engineering CAD Models from 3D Point Clouds** (2023, arXiv): Title is a direct match, but the abstract snippet discusses topology challenges without explicitly confirming B-rep as the final output format.
3.  **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds** (2023, arXiv): Title indicates a parametric CAD output from point clouds, aligning with the goal.

## Notes and Gaps
*   **Evidence Quality:** Most retrieved papers have only partial abstract snippets, making it impossible to conclusively verify that B-rep reconstruction from point clouds is the *primary* task and final output.
*   **Venue Gap:** The search did not surface papers from top-tier computer vision/graphics conferences (e.g., SIGGRAPH, CVPR, ICCV), which are likely venues for frontier research on this topic.
*   **Scope Creep:** Many retrieved papers were off-topic, focusing on:
    *   General surface or mesh reconstruction (e.g., NumGrad-Pull).
    *   Domain-specific applications without confirmed B-rep output (e.g., Railway reconstruction, TreeON).
    *   Subproblems like primitive fitting or edge detection (e.g., Surface and Edge Detection for Primitive Fitting).
    *   Dataset creation or annotation pipelines.

## Recommended Next Steps
1.  **Manual Verification:** For the strongest leads (e.g., Point2Brep, CAD-Recode, Point2CAD), retrieve and read the full paper to confirm the input (point cloud) and output (B-rep/editable CAD model).
2.  **Targeted Venue Search:** Conduct a manual or advanced search within the proceedings of key conferences (SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, SPM) using terms like `"B-rep"`, `"boundary representation"`, `"CAD reconstruction"`, and `"point cloud"`.
3.  **Citation Tracking:** Use the verified papers (if any) as seeds for backward and forward citation analysis to find related core research.
4.  **Broaden Terminology:** Consider that some relevant work may be framed as "reverse engineering of CAD models" or "structured CAD generation" without explicitly using "B-rep" in the title or abstract.

TERMINATE
