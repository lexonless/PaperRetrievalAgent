# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep generation, reconstruction, and recovery.

Focus on papers that generate, reconstruct, or recover B-rep or CAD boundary representations as a primary modeling target.

Prioritize papers that are broadly relevant to general B-rep generation and structured CAD model generation, including methods based on point clouds, scans, images, sketches, text, multimodal inputs, or other representations when they make a meaningful contribution to B-rep generation itself.

Still rank papers especially high when they use point clouds or scans as a major input, but do not exclude strong general B-rep generation papers merely because they are not point-cloud-only methods.

Exclude papers that are clearly unrelated to B-rep or CAD generation/reconstruction.

Do not include papers whose main goal is to reconstruct CAD operation sequences, CAD programs, design history, sketch-extrude commands, or other reverse-engineering representations instead of B-rep generation itself.

Return 8-10 relevant papers with:
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

Rank the most relevant general B-rep generation papers first, while still highlighting point-cloud-based methods when they are strong.
**Generated At:** 2026-03-25T10:34:19
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The search aimed to identify frontier research (2022–2026) on methods that generate, reconstruct, or recover Boundary Representation (B-rep) or CAD models as a primary output. The focus was on general B-rep generation techniques, with a secondary priority on methods using point clouds or scans as input. Papers focused on reconstructing CAD operation sequences, programs, or design history were to be excluded.

## Search Strategy
The search was conducted in two rounds using Crossref, OpenAlex, and arXiv. Initial queries targeted "B-rep generation from point cloud deep learning" and related terms. A second round used more targeted queries like "point cloud to B-rep reconstruction 2023 2024" to address identified gaps. The reviewer assessed the results twice, finding that the retrieved papers largely did not confirm B-rep as the output representation, with many focusing on point cloud processing, segmentation, or other intermediate representations instead of direct B-rep generation.

## Candidate Papers
**The search did not clear the quality bar.** The retrieval process failed to gather a sufficient set of papers where the primary contribution is the generation or reconstruction of a B-rep model, as required. The final set contains mostly adjacent work on point cloud processing or CAD sequence generation.

### Verified Candidates
*Papers with partial or verified evidence of targeting B-rep output.*

*   **Brep2Seq: a dataset and hierarchical deep learning network for reconstruction and generation of computer-aided design models** (2023)
    *   **Source:** OpenAlex
    *   **Link:** https://doi.org/10.1093/jcde/qwae005
    *   **Core Contribution:** Proposes a transformer-based encoder-decoder to transform B-rep models into sequences of editable parametric features, with applications including point cloud reconstruction.
    *   **Relevance Note:** Direct match. Explicitly addresses B-rep reconstruction and generation from various inputs, including point clouds.

*   **Towards Automated BIM and BEM Model Generation using a B-Rep-based Method with Topological Map** (2024)
    *   **Source:** OpenAlex
    *   **Link:** https://doi.org/10.5194/isprs-annals-x-4-2024-287-2024
    *   **Core Contribution:** Introduces an automated method for creating Boundary Representation (B-Rep) models from 3D reality-based point clouds for digital building replicas.
    *   **Relevance Note:** Direct match. Focuses on B-rep generation specifically from scanned point cloud data for architectural applications.

### Unverified Leads
*Title-strong but unverified papers suggested as potential follow-up leads, not as verified recommendations.*

*   **CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM** (2024)
*   **BPNet: Bézier Primitive Segmentation on 3D Point Clouds** (2023)
*   **Revisiting CAD Model Generation by Learning Raster Sketch** (2025)

## Notes and Gaps
*   **Evidence Gap:** Most retrieved papers only had abstract-level evidence, which was insufficient to confirm that B-rep is the primary output. Many focused on point cloud generation, segmentation, or neural field reconstruction.
*   **Core Topic Gap:** The search failed to retrieve a critical mass of recent papers (2022-2026) whose central contribution is learning-based B-rep reconstruction from point clouds or scans.
*   **Terminology Mismatch:** Queries for "point cloud to B-rep" may not align with the terminology used in relevant literature, which might use phrases like "CAD model reconstruction from scan" or "solid model recovery."
*   **Adjacent Work:** The retrieval was biased towards general point cloud deep learning and CAD sequence generation, which are related but do not satisfy the user's specific requirement for B-rep output.

## Recommended Next Steps
1.  **Precise Phrase Search:** Execute searches using exact phrases like `"boundary representation" reconstruction point cloud` or `"B-rep" generation` in titles and abstracts to filter for papers explicitly targeting B-rep.
2.  **Citation Chaining:** Identify known seminal papers in B-rep learning (e.g., BRepNet, Point2CAD) and search for recent works (2022-2026) that cite them to find frontier follow-ups.
3.  **Venue-Targeted Search:** Focus retrieval on conferences and journals known for CAD/geometry processing research (e.g., CAD, Computer-Aided Design, SGP, SIGGRAPH Asia) to improve relevance.
4.  **Full-Text Verification:** For promising candidate titles, retrieve full introductions or method sections to definitively confirm whether the output is a B-rep model.

TERMINATE
