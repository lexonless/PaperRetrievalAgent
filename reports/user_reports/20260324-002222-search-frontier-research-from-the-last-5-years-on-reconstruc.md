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
**Generated At:** 2026-03-24T00:22:22
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify frontier research (2022–2026) where the **primary task** is an end-to-end pipeline that takes point clouds or scanned 3D geometry as input and directly outputs a B‑rep (boundary representation) or CAD model as the final result. The search strictly excluded works focused only on sub‑problems (e.g., primitive detection, segmentation), intermediate representations, or alternative outputs like meshes.

## Search Strategy
Two rounds of search were executed using Crossref, OpenAlex, and arXiv APIs.
*   **Round 1:** Used broad queries like “point cloud to B‑rep reconstruction” and “end‑to‑end CAD reconstruction from point clouds.” Results were overwhelmingly off‑topic (e.g., assembly tasks, additive manufacturing, mesh reconstruction).
*   **Round 2:** Refined queries to enforce output representation, using terms like `"B‑rep" point cloud reconstruction` and `reverse engineering point cloud to B‑rep`. Results remained off‑topic, including point‑cloud classification surveys, generic surface/mesh reconstruction, and editorial decision letters.

The automated search failed to retrieve any papers that, based on title evidence, address the core task. The niche topic appears poorly served by broad bibliographic API queries.

## Candidate Papers
**No on‑topic papers were retrieved.** The final retrieval list contains 10 papers, all of which are irrelevant based on their titles. Below is a summary of the retrieved set, illustrating the mismatch:

| Title | Year | Source | Why It Is Not a Core Candidate |
| :--- | :--- | :--- | :--- |
| Deep learning‑based 3D point cloud classification: A systematic survey and outlook | 2023 | OpenAlex | Survey on classification, not reconstruction to CAD. |
| Deep Learning‑Based Surface Reconstruction from Point Clouds | 2024 | Crossref | Title suggests mesh/surface output, not B‑rep/CAD. |
| Extraction and Reconstruction of Articulated Robots from Point Clouds of Manufacturing Plants | 2024 | Crossref (CAD’24) | Likely outputs kinematic models or meshes, not a B‑rep CAD model. |
| A Modular Framework for Geometry‑Aware Mesh Reconstruction from Sparse Point Clouds | 2025 | Crossref | Explicitly outputs mesh, not B‑rep/CAD. |
| Decision/Review letters for “AdLeaf: Quantitative leaf reconstruction from TLS point clouds” (multiple) | 2025 | Crossref | Editorial content, not a research paper. |

**Total retrieved:** 10 papers. **Selection rule:** All papers are shown because none are core candidates; the set demonstrates the search failure.

## Notes and Gaps
*   **Complete Miss on Core Topic:** The automated search did not return a single paper that, even by title, addresses point‑cloud‑to‑B‑rep/CAD reconstruction. This indicates the topic is highly specialized and not easily captured by generic API queries.
*   **Evidence Limitation:** All retrieved papers have only title‑level metadata; no abstracts or excerpts were examined. However, titles provide strong negative signals (e.g., “mesh,” “classification,” “decision letter”).
*   **Potential Venue Mismatch:** Relevant work likely appears in specialized CAD/geometry venues (e.g., ACM SIGGRAPH, Symposium on Geometry Processing, Computer‑Aided Design journal) rather than in broad‑scope conferences/journals indexed by general APIs.
*   **Terminology Variants:** Authors may use “parametric CAD,” “feature‑based CAD,” or “boundary representation” without the acronym “B‑rep,” making keyword‑based retrieval challenging.

## Recommended Next Steps
1.  **Targeted Venue Search:** Manually search proceedings/journals of key venues (e.g., ACM Transactions on Graphics, Computer‑Aided Design, SIGGRAPH Asia, SGP) for the years 2022‑2026 using site‑specific search tools.
2.  **Citation‑Chaining:** Start from known seminal pre‑2022 papers on CAD reconstruction (e.g., Point2Cyl, BRepNet, DeepCAD) and use citation databases (Google Scholar, Semantic Scholar) to find recent follow‑ups (2022‑2026).
3.  **Expert‑Curated Lists:** Consult recent survey papers or tutorials on “CAD reconstruction” or “reverse engineering” that may include a section on point‑cloud input.
4.  **Broaden Output Representation Slightly:** If the strict B‑rep requirement can be relaxed to include **constructive solid geometry (CSG)** or **parametric CAD models** (not just boundary representations), the search may yield more results. However, this would deviate from the original query intent.

TERMINATE
