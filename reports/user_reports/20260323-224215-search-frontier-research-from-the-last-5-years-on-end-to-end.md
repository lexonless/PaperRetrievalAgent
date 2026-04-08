# Paper Search Report

**Query:** Search frontier research from the last 5 years on end-to-end reconstruction of B-rep/CAD representations from point clouds.

Focus only on papers where the main task is to take point clouds or scanned 3D geometry as input and directly reconstruct B-rep/CAD outputs as the final representation.

Prioritize methods that explicitly address the full reconstruction pipeline, including geometric primitive recovery, parametric surface fitting, topology recovery, and geometry-constrained reconstruction, when these are part of an end-to-end point-cloud-to-B-rep objective.

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
**Generated At:** 2026-03-23T22:42:15
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) where the **primary task** is to take point clouds or scanned 3D geometry as input and directly output a B‑rep/CAD model as the final representation. The focus is on the full reconstruction pipeline, including geometric primitive recovery, parametric surface fitting, topology recovery, and geometry‑constrained reconstruction.

**Key constraints:**
*   **Time window:** 2022–2026 (inclusive).
*   **Core task:** End‑to‑end point‑cloud‑to‑B‑rep/CAD reconstruction.
*   **Exclusions:** Papers that only address sub‑problems (e.g., segmentation), produce intermediate representations (e.g., mesh, implicit surface) as final output, or focus on auxiliary modules or downstream applications.

## Search Strategy
The search attempted to execute multiple query variants derived from the planner, targeting sources including arXiv, OpenAlex, Crossref, and DBLP. The strategy evolved through two review cycles:

1.  **Initial Queries:** Focused on precise phrases like `"point cloud" "B-rep" reconstruction end-to-end`. DBLP returned server errors, and other sources returned zero results.
2.  **Revised Queries:** Broadened to include terms like `"scan to CAD" reconstruction` and `reverse engineering CAD from point cloud deep learning` to capture pipeline‑oriented work, with the intent to filter results post‑retrieval for strict adherence to the end‑to‑end B‑rep output requirement.

**Execution Outcome:** Despite multiple attempts, the retrieval system failed to return any candidate papers. Source coverage was hampered by persistent DBLP server errors, and executed queries yielded zero results from other sources. Consequently, no papers could be assessed for relevance or metadata completeness.

## Candidate Papers
**No papers were retrieved.** The search failed to return any candidates for evaluation. Therefore, a list of core papers meeting the strict end‑to‑end point‑cloud‑to‑B‑rep reconstruction criteria cannot be provided.

## Notes and Gaps
The search process encountered significant limitations:

*   **Retrieval Failure:** The system executed queries but returned zero papers. This may indicate:
    *   The queries were still too narrow for a nascent research field.
    *   Technical issues with query execution or source APIs.
    *   A genuine scarcity of papers that explicitly frame their primary contribution as an end‑to‑end point‑cloud‑to‑B‑rep reconstruction pipeline within the last five years.
*   **Source Reliability:** The DBLP source consistently returned server errors (`500 Internal Server Error`), reducing coverage for potential conference publications.
*   **Missing Evidence:** Without retrieved papers, it is impossible to:
    *   Verify the existence or count of relevant publications.
    *   Identify major methodological categories (e.g., optimization‑based, learning‑based, hybrid).
    *   Discern recent trends or open challenges specific to this precise task.

## Recommended Next Steps
Given the complete retrieval failure, the following actions are recommended to obtain a meaningful result:

1.  **Debug Retrieval Execution:** Ensure the system executes **all** query variants from the planner's list, not just the first one. Prioritize arXiv and OpenAlex for their reliability with recent preprints.
2.  **Broaden Search with Post‑Filtering:** Use significantly broader initial queries (e.g., `"CAD from scan"`, `"reverse engineering" point cloud`, `"B-rep" reconstruction`) to capture a larger candidate set. Then, implement a strict post‑retrieval filter based on abstract/snippet analysis to select only papers where the **primary task and final output** is a B‑rep/CAD model from point cloud input.
3.  **Manual or Semi‑Automated Search:** Given the apparent difficulty, a manual search of top computer vision/graphics conferences (CVPR, ICCV, ECCV, SIGGRAPH) and journals (CAD, Computer‑Aided Design) from 2022‑2026 using the above broad terms may be necessary to seed the process.
4.  **Verify Time Range:** Ensure year filters are correctly applied both in queries and during post‑processing.

TERMINATE
