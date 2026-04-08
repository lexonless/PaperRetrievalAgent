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
**Generated At:** 2026-03-24T01:34:16
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify frontier research (2022–2026) where the **primary task** is an end-to-end pipeline that takes **point clouds as input** and directly outputs **B-rep (boundary representation)** as the final representation. The search strictly excludes works focused on subproblems (e.g., segmentation, fitting), intermediate representations (e.g., mesh, voxel), downstream applications, or alternative tasks (e.g., generation from images, classification of existing B-reps).

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv using refined queries targeting the intersection of "point cloud," "B-rep," and "reconstruction." Initial broad queries yielded many off-topic results (e.g., SLAM, robotics, point cloud registration). Subsequent queries were narrowed to phrases like `"B-rep" reconstruction point cloud` and `point cloud to CAD B-rep`. Despite these efforts, the retrieval process did not yield a sufficient number of papers that could be verified as meeting all strict criteria, particularly the confirmation of point cloud as the primary input.

## Candidate Papers
The search did not clear the quality bar. After two retrieval and review cycles, an insufficient number of papers were verified to satisfy the strict end-to-end, point-cloud-to-B-rep requirement. Below is a split of the findings.

### Verified Candidates
*No papers were fully verified.* The evidence snippets available were partial and did not explicitly confirm the required input/output pipeline for any candidate.

### Unverified Leads
The following papers have titles suggesting relevance but lack verified evidence confirming point cloud as the primary input and B-rep as the direct, final output. They are presented as potential leads for follow-up investigation, not as recommendations.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title strongly suggests relevance. The abstract snippet mentions "reconstructing accurate boundary representations (B-reps) from unstructured point clouds," but the full context and methodology are unverified.
*   **ComplexGen / ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)** – Presents a method for B-rep reconstruction. The abstract discusses reconstructing CAD models in B-rep, but the specified input ("original shapes, including point clouds...") is broad, and it is unclear if point clouds are the primary focus.
*   **P2CADNet: An End-to-End Reconstruction Network for Parametric 3D CAD Model from Point Clouds (2023)** – From the first retrieval round. The title explicitly mentions point clouds. The abstract suggests an end-to-end network for featured CAD models, making it a promising lead, but full verification is needed.

## Notes and Gaps
*   **Nascent Field:** The strict criteria define a highly specialized research niche. The low yield suggests that truly end-to-end point-cloud-to-B-rep reconstruction is a frontier area with limited published work.
*   **Evidence Gap:** The primary gap was the inability to verify the core input/output pipeline from available abstract snippets. Many papers use "B-rep" or "CAD" but do not specify point clouds as the input in the retrieved evidence.
*   **Off-Topic Retrievals:** Searches frequently returned papers on related but excluded topics, such as B-rep segmentation (BRepGAT), image-to-CAD (BrepGaussian), dataset creation, and annotation pipelines.
*   **Venue Focus:** A targeted search within specific computer vision (CVPR, ICCV), graphics (SIGGRAPH), and CAD journal/conference proceedings may be necessary to find relevant work.

## Recommended Next Steps
1.  **Manual Verification:** For the leads above (Point2Brep, ComplexGen, P2CADNet), manually inspect the full paper to definitively confirm if point cloud is the primary input and B-rep is the final output.
2.  **Venue-Specific Search:** Conduct a focused search within the proceedings of key venues (ACM TOG, Computer-Aided Design, CVPR, ICCV) using advanced search tools.
3.  **Broaden Terminology:** Consider searching for synonyms like "parametric CAD reconstruction from scan" or "boundary representation recovery from 3D points," while manually filtering for the required pipeline.
4.  **Adjust Scope:** If the strict criteria prove too limiting, consider defining a broader scope that includes hybrid methods or pipelines where B-rep is a key, explicit output stage from point cloud data.

TERMINATE
