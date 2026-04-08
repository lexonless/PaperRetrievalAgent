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
**Generated At:** 2026-03-24T22:52:40
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal is to identify recent research (2022–2026) on methods that reconstruct Boundary Representation (B-rep) CAD models directly from point cloud data. The focus is on core techniques for generating, recovering, or reconstructing editable, parametric CAD models from scanned point clouds, excluding work that outputs only meshes or deals with unrelated CAD applications.

## Search Strategy
The search was conducted across Crossref, OpenAlex, and arXiv using queries targeting:
*   Direct point-cloud-to-B-rep reconstruction.
*   Parametric CAD model generation from point clouds.
*   Reverse engineering of CAD from scanned point cloud data.
The search was refined over two cycles to improve relevance and evidence quality, focusing on retrieving full abstracts to verify the core method and fit.

## Candidate Papers
The search did not clear the quality bar. The evidence gathered from retrieved abstracts is insufficient to confidently verify that a sufficient number of papers are direct matches for the specific task of B-rep reconstruction from point clouds. The final list is split into verified candidates and unverified leads.

### Verified Candidates
Based on the available evidence, no papers could be fully verified as direct matches. The `verification_status` for all retrieved papers remained "partial," with truncated abstract snippets that prevent definitive confirmation of the core method's alignment with the user's request.

### Unverified Leads
The following papers appear title-strong and are within the correct timeframe, but their relevance could not be verified due to incomplete evidence. They are presented as potential leads for follow-up investigation, not as recommendations.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)** – Title directly mentions B-rep reconstruction from point clouds; abstract snippet indicates a learning-based framework.
*   **CAD-Recode: Reverse Engineering CAD Code from Point Clouds (2024)** – Title suggests reverse engineering of CAD operations from point clouds; abstract snippet mentions reconstructing sketch and operation sequences.
*   **TransCAD: A Hierarchical Transformer for CAD Sequence Inference from Point Clouds (2024)** – Title indicates an end-to-end method for predicting CAD sequences from point clouds.

## Notes and Gaps
*   **Evidence Gap:** The primary failure reason is insufficient evidence. Retrieved abstract snippets were consistently truncated, making it impossible to verify the core contribution, methodology, and whether point clouds are the primary input for B-rep output.
*   **Relevance Uncertainty:** Several papers in the retrieved set (e.g., "SHREC 2022: Fitting and recognition of simple geometric primitives") appear to be benchmark or primitive-fitting studies, not direct B-rep reconstruction methods. Without full abstracts, these could not be confidently filtered out.
*   **Metadata Incompleteness:** Several arXiv entries lacked DOIs, and some author lists appeared incomplete or duplicated.

## Recommended Next Steps
1.  **Manual Abstract Retrieval:** Directly visit the source links (e.g., arXiv, DOI links) for the top candidate papers to read full abstracts and confirm relevance.
2.  **Citation Chaining:** Use the most promising leads (e.g., "Point2Brep," "CAD-Recode") as seed papers to search for citing and related work in Google Scholar or Semantic Scholar.
3.  **Focused Database Search:** Conduct a targeted search in engineering and computer graphics databases (e.g., ACM Digital Library, IEEE Xplore) using combined keywords like `("B-rep" OR "boundary representation") AND ("point cloud" AND reconstruction)`.
4.  **Conference Focus:** Prioritize searching proceedings from top-tier conferences in computer graphics (SIGGRAPH, SIGGRAPH Asia) and CAD (CAD/Graphics, SPM) from the 2022-2026 period.

TERMINATE
