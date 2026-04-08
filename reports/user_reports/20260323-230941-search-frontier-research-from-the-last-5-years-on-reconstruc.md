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
**Generated At:** 2026-03-23T23:09:41
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) on **end-to-end methods** that take raw point clouds or 3D scans as input and directly output B‑rep or CAD models as the final representation. The search explicitly excluded works focused only on subproblems (e.g., surface fitting, segmentation), intermediate representations (e.g., meshes, implicit surfaces), or alternative tasks.

## Search Strategy
The planned strategy involved multi‑source queries (arXiv, Crossref, OpenAlex) using targeted phrases such as `"point cloud" "B‑rep" reconstruction`, `"CAD reconstruction" "point cloud" end‑to‑end`, and `"reverse engineering" CAD "point cloud"`. Boolean operators and year filters were applied to improve precision. However, the executed retrieval appears to have been limited primarily to Crossref, resulting in a critically insufficient result set.

## Candidate Papers
**Total papers retrieved:** 1  
**Selection rule:** All final papers from the latest retrieval JSON are shown below. No papers were omitted.

*   **Title:** Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds
*   **Year:** 2026
*   **Source:** Crossref / SSRN
*   **Link:** https://doi.org/10.2139/ssrn.6172545
*   **Core Contribution:** Proposes a geometry‑aware framework that integrates learning‑based inference with explicit parametric modeling to reconstruct complete, topologically consistent B‑rep models from unstructured point clouds.
*   **Relevance Note:** The abstract indicates the method takes point clouds as input and outputs B‑rep models, positioning it as an end‑to‑end reconstruction pipeline. Its verification status is marked as "partial" based on the available snippet.

## Notes and Gaps
The search failed to meet its objectives due to significant limitations:

1.  **Severe Under‑retrieval:** Only one candidate paper was found, far short of the target 5‑10. This suggests either a failure in query execution across multiple sources or an overly restrictive search strategy.
2.  **Lack of Source Diversity:** The retrieval appears to have been executed only on Crossref, ignoring planned queries to arXiv and OpenAlex. This severely limited coverage, especially for recent pre‑prints and conference papers.
3.  **Insufficient Evidence for a Frontier Review:** A single paper (a 2026 pre‑print with partial verification) cannot support a meaningful analysis of methodological categories, recent trends, or open challenges for a research frontier spanning five years.
4.  **Potential Topic Scarcity:** While the niche is specific, it is unlikely that only one relevant paper exists from 2022‑2026. The gap more likely indicates a retrieval system or strategy failure.

## Recommended Next Steps
1.  **Fix Source Execution:** Ensure the retrieval tool correctly queries all specified sources (arXiv, Crossref, OpenAlex) as per the planner's multi‑source strategy.
2.  **Broaden Search Queries:** If multi‑source queries still return sparse results, use more general terms (e.g., `"CAD from point cloud"`, `"B‑rep reconstruction"`) and explicitly search for known seminal works from the period (e.g., "Point2CAD", "BRepNet", "DeepCAD") to seed the results.
3.  **Manual Verification:** Check relevant conference proceedings (e.g., SIGGRAPH, CVPR, CAD conferences) and their digital libraries to confirm the existence of literature and identify appropriate search terms.
4.  **Re‑run with Corrected Strategy:** Once the source coverage and query breadth are addressed, execute a new search to build a representative corpus for analysis.

TERMINATE
