# Paper Search Report

**Query:** Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

Return 5-10 relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining whether the paper is a direct match or a closely related paper, and why

Then summarize:
- major method categories
- recent trends
- open challenges

Rank the most directly relevant papers first, but do not over-filter papers merely because they use multi-stage pipelines or different wording for the same task.
**Generated At:** 2026-03-24T22:03:44
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify recent research (2022–2026) on methods that reconstruct or generate Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on the core task of point-cloud-to-B-rep reconstruction, including closely related works that make substantial contributions to this problem (e.g., primitive detection, parametric CAD sequence recovery). Papers that only address mesh reconstruction, pure segmentation, or use other primary inputs (e.g., images) are excluded.

## Search Strategy
The search was conducted in two phases using sources including arXiv, Crossref, and OpenAlex.
1.  **Initial Queries:** Targeted direct phrases like "point cloud to B-rep reconstruction" and "deep learning B-rep generation from point clouds."
2.  **Refined Queries:** Based on reviewer feedback, queries were adjusted to emphasize "reverse engineering CAD from point cloud" and "parametric CAD model reconstruction from 3D scan" to better capture core methods.
The process aimed to verify that each paper's abstract explicitly mentions point cloud input and B-rep/CAD model output.

## Candidate Papers
*The search did not clear the quality bar.* The review process identified unresolved issues: evidence snippets remained too brief to confirm core method fit for several papers, and the final list contained duplicates and entries that were not directly relevant to the specified task. Therefore, a definitive set of recommended papers cannot be provided.

### Verified Candidates
No papers reached a `verified` status. The following papers had `partial` verification, meaning their abstracts suggest relevance but full confirmation is lacking:
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds (2024)** – Abstract indicates reconstruction of CAD operation sequences from point clouds.
*   **ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)** – Abstract frames CAD model reconstruction in B-Rep as detection of geometric primitives.
*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title and snippet directly describe B-rep reconstruction from point clouds.

### Unverified Leads
The following papers have titles that appear strong for the topic but lack sufficient evidence in the retrieved snippets to confirm they are core methods for point-cloud-to-B-rep reconstruction. They are suggested as leads for follow-up investigation, not as recommendations.
1.  **MiCADangelo: Fine-Grained Reconstruction of Constrained CAD Models from 3D Scans (2025)** – Title mentions reconstruction from 3D scans.
2.  **Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning (2024)** – Title suggests a method for acquiring B-Reps.
3.  **HoLa: B-Rep Generation using a Holistic Latent Representation (2025)** – Title focuses on B-Rep generation.

## Notes and Gaps
*   **Evidence Insufficiency:** The primary gap was the inability to retrieve and present complete abstracts or introductory paragraphs for candidate papers, which is necessary to confirm the core task alignment (point cloud input, B-rep output).
*   **Result Contamination:** The final retrieval set contained duplicate entries (e.g., multiple instances of "ComplexGen") and papers clearly outside the scope (e.g., a broad review on AI in construction, a dataset paper).
*   **Methodological Clarity:** Without full paper details, it is impossible to reliably categorize major methods, identify recent trends, or list open challenges.

## Recommended Next Steps
1.  **Manual Abstract Retrieval:** For the leads listed above, directly access the provided URLs (e.g., arXiv links) to read the abstracts and confirm relevance.
2.  **Targeted Database Search:** Use academic databases (e.g., ACM Digital Library, IEEE Xplore) with precise queries like `"B-rep" AND "point cloud" AND reconstruction` and filter by publication date (2022-2026).
3.  **Citation Tracking:** Identify seminal papers in the area (e.g., "ComplexGen") and use citation tracking tools to find more recent works that build upon them.
4.  **Venue Focus:** Prioritize searching in relevant conference proceedings (e.g., SIGGRAPH, CVPR, CAD) and journals (e.g., Computer-Aided Design, IEEE Transactions on Visualization and Computer Graphics).

TERMINATE
