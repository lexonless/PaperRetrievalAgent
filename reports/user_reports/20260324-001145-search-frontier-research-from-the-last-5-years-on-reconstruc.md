# Paper Search Report

**Query:** Search frontier research from the last 5 years on reconstruction of B-rep/CAD representations from point clouds.

Focus only on papers where the main task is to take point clouds or scanned 3D geometry as input and directly reconstruct B-rep/CAD outputs as the final representation.

Prioritize methods that explicitly address the full reconstruction pipeline.

Exclude papers whose main contribution is only a subproblem, intermediate representation, auxiliary module, downstream application, or alternative task rather than end-to-end point-cloud-to-B-rep reconstruction.

A paper should not be treated as a core candidate unless reconstructing B-rep/CAD from point clouds is the primary task and final output.

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
**Generated At:** 2026-03-24T00:11:45
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) where the primary task is the **end-to-end reconstruction of B-rep or parametric CAD models directly from point clouds or 3D scans**. The search strictly excluded works focused only on subproblems (e.g., preprocessing, alignment, segmentation, feature recognition) or intermediate representations (e.g., meshes, implicit surfaces).

## Search Strategy
The search was conducted in two phases:
1.  **Initial Broad Search:** Used queries like "point cloud to CAD reconstruction" and "B-rep reconstruction from 3D scans" across Crossref, OpenAlex, and arXiv. This returned many papers focused on adjacent tasks (preprocessing, alignment, specific applications) but no verified, core end-to-end reconstruction methods.
2.  **Refined Learning-Based Search:** Based on reviewer feedback, subsequent queries targeted "neural CAD reconstruction from point clouds" and "point cloud to B-rep deep learning" to capture recent data-driven pipelines. This phase failed to return relevant results, with search engines retrieving off-topic papers (e.g., on medical imaging, federated learning). arXiv API errors further limited source coverage.

The automated search strategy ultimately failed to retrieve any papers that could be verified as meeting the strict, core user criteria.

## Candidate Papers
**No qualifying papers were identified.**

The retrieval process returned 20 unique papers (10 from each phase), but none could be confirmed as core candidates. Based on titles alone, the results fell into irrelevant or excluded categories:
*   **Applications & Subproblems:** Building component extraction, blade damage assessment, machining feature recognition, scan-to-CAD alignment.
*   **Alternative Representations:** Sketch-and-extrude parsing, surface reconstruction, CSG model conversion surveys.
*   **Completely Off-Topic Domains:** Federated learning, medical CT reconstruction, UAV surveys.

**Selection Rule:** All retrieved papers were omitted because their titles (the only available evidence) strongly indicated they did not have "end-to-end B-rep/CAD reconstruction from point clouds" as their primary contribution. Without abstract or full-text verification, they could not be confirmed as relevant.

## Notes and Gaps
*   **Critical Evidence Gap:** The search was conducted with "title-only" evidence. Without access to abstracts or excerpts, it was impossible to verify if any potentially relevant-sounding papers (e.g., "SMA-Net: Deep learning-based identification and fitting of CAD models from point clouds") truly described an end-to-end pipeline.
*   **Search Strategy Failure:** Automated queries on general academic APIs appear ineffective for this highly niche, interdisciplinary topic. The queries were likely matched against isolated terms ("CAD," "reconstruction," "point cloud") in vastly different contexts.
*   **Source Limitation:** arXiv, a key source for recent pre-prints in computer vision and graphics, returned server errors (502 Bad Gateway), crippling the search for frontier learning-based methods.
*   **Possible Field Scarcity:** The strict criteria (point cloud → B-rep/CAD) may define a very small research area. Many works in "CAD reconstruction" start from meshes, images, or sketches, not raw point clouds.

## Recommended Next Steps
1.  **Manual Venue Search:** Conduct a targeted, manual search of recent proceedings from key conferences:
    *   **Computer Vision & Graphics:** CVPR, ICCV, ECCV, SIGGRAPH, Eurographics.
    *   **CAD & Geometric Modeling:** ACM SIGGRAPH / Eurographics Symposium on Geometry Processing, CAD, Computer-Aided Design journal.
    *   **Search Terms:** Look for sessions on "3D reconstruction," "reverse engineering," "geometric learning," and "shape generation."
2.  **Known Paper Verification:** Investigate specific papers that are seminal in *CAD generation* to see if they have been adapted for *point cloud input*:
    *   *DeepCAD* (CVPR 2021), *BRepNet* (SIGGRAPH 2021), *Point2Cyl* (CVPR 2022), *CADTransformer* (arXiv 2023). Check their problem statements for point cloud input variants.
3.  **Broaden Input Definition:** If the core task is sparse, consider including works that take **oriented point clouds** or **depth maps** as input, as these are common outputs from 3D scanners.
4.  **Iterate with Human-in-the-Loop:** Use the initial, broad set of papers (e.g., "SMA-Net," "Building CAD Model Reconstruction from Point Clouds...") as leads. Manually retrieve and read their abstracts to determine if any genuinely satisfy the end-to-end requirement before a final revision.

TERMINATE
