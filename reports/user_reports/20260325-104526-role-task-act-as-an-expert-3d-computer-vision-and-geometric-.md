# Paper Search Report

**Query:** **Role & Task:**
Act as an expert 3D computer vision and geometric deep learning researcher. Your task is to search for and analyze 8-10 state-of-the-art frontier research papers (published between 2021-2026) focused explicitly on 3D Boundary Representation (B-Rep) reconstruction and generation. 

**Primary Focus (What to INCLUDE):**
* **Target Output:** The primary output of the model MUST be the B-Rep data structure itself (faces, edges, vertices, and their topological relationships).
* **Target Input:** Unstructured Point Clouds or 3D scans are the highest priority. Multimodal or sketch/image inputs are acceptable only if the method is a major breakthrough in B-Rep generation.
* **Methodology:** Highly prioritize modern neural architectures, including latent space representations, variational approaches, or end-to-end direct neural generation of continuous B-Rep geometry and topology.

**CRITICAL EXCLUSIONS (What to strictly AVOID):**
You MUST STRICTLY EXCLUDE any paper that falls into these categories:
1.  **NO CAD Operation Sequences:** Do not include papers where the goal is to reconstruct CAD construction trees, sketch-and-extrude histories, or sequential modeling steps (e.g., DeepCAD, Sketex).
2.  **NO CSG Trees:** Exclude papers focusing on Constructive Solid Geometry (CSG) primitive combinations.
3.  **NO Program Synthesis:** Exclude papers that generate CAD programs or macros.
*If the model outputs a step-by-step modeling history rather than directly outputting the final B-Rep topological/geometric data structure, it is a hard fail. Discard it.*

**Output Format:**
For each of the 8-10 selected papers, provide:
* **Title & Year:**
* **Source/Venue:** (e.g., CVPR, SIGGRAPH, NeurIPS)
* **Link:**
* **Core Contribution:** (1-2 sentences on their specific technical breakthrough)
* **Relevance Note:** (Explain exactly how it tackles direct B-Rep generation from point clouds, and confirm it does not rely on step-by-step operation sequences).

**Synthesis Report:**
After listing the papers, provide a concise summary covering:
1.  **Major Method Categories:** (How are current models representing B-Rep natively for neural networks?)
2.  **Recent Trends:** (e.g., shifts in handling topology vs. geometry)
3.  **Open Challenges:** (Specific bottlenecks in point-cloud-to-B-Rep tasks)
**Generated At:** 2026-03-25T10:45:26
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to find 8-10 state-of-the-art research papers (2021-2026) focused on the direct neural generation or reconstruction of 3D Boundary Representation (B-Rep) data structures. The core requirement is that the model's primary output is the B-Rep itself (faces, edges, vertices, and topology), not a sequence of modeling operations. The highest-priority input is unstructured point clouds or 3D scans. The search strictly excluded methods based on CAD operation sequences, CSG trees, or program synthesis.

## Search Strategy
The search was conducted in multiple phases using sources including Crossref, OpenAlex, and arXiv. Initial queries targeted "neural network direct B-Rep generation from point clouds." A subsequent revision, prompted by reviewer feedback, employed more precise queries like "direct B-Rep generation neural network point cloud" and "diffusion model B-Rep generation" to better capture recent generative architectures. The strategy prioritized high-impact venues (CVPR, SIGGRAPH) and aimed to verify that each candidate's method avoided the excluded categories. Despite these efforts, the final retrieval did not yield a sufficient number of verified, on-topic papers that met all hard constraints.

## Candidate Papers
**The search did not clear the quality bar.** The reviewer's final decision was REVISE, indicating the retrieved set did not meet critical requirements: insufficient candidate depth, high risk of including papers that violate exclusion criteria (e.g., generating CAD operation sequences), and a lack of focus on the prioritized task of point-cloud-to-B-Rep reconstruction. Below is a breakdown of the findings.

### Verified Candidates
Based on the evidence snippets, no papers achieved a `verified` status. The following papers have `partial` verification and are the strongest leads that appear to align with the core topic, though their compliance with all exclusion criteria could not be fully confirmed.

*   **Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)**
    *   **Source:** Crossref
    *   **Link:** https://doi.org/10.2139/ssrn.6172545
    *   **Core Contribution:** A two-stage framework that segments point clouds into surface patches and then predicts geometric distance fields to recover B-Rep edges, vertices, and connectivity, integrating learning with explicit geometric reasoning.
    *   **Relevance Note:** Directly targets B-Rep reconstruction from unstructured point clouds. The abstract describes outputting "complete and topologically consistent B-rep models," with no mention of operation sequences.

*   **BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch (2025)**
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2511.22171v1
    *   **Core Contribution:** Proposes a single-stage autoregressive framework using a novel Voronoi Half-Patch representation and a decoder-only Transformer to generate B-Rep tokens, which are decoded into complete models.
    *   **Relevance Note:** Describes direct B-Rep generation. The framework supports conditional generation from point clouds, among other inputs. The method appears to output the B-Rep structure directly.

*   **HoLa: B-Rep Generation using a Holistic Latent Representation (2025)**
    *   **Source:** arXiv
    *   **Link:** http://arxiv.org/abs/2504.14257v3
    *   **Core Contribution:** Introduces a holistic latent space that unifies B-Rep geometry and topology, enabling a diffusion-based generator to produce B-Reps from various inputs, including point clouds.
    *   **Relevance Note:** Focuses on generating the full B-Rep data structure. The method learns to derive curve geometry from surface pairs, implicitly encoding topology without reconstructing a modeling history.

### Unverified Leads
The following papers have titles strongly related to B-Rep generation but lack sufficient evidence in the provided snippets to confirm they avoid CAD operation sequences or prioritize point cloud input. They are presented as potential leads for follow-up investigation, not as verified recommendations.

1.  **BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024)** - A diffusion model that directly outputs a B-Rep using a hierarchical tree representation. (Needs verification that it does not use CSG or operation sequences).
2.  **AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025)** - A Transformer model that tokenizes B-Rep geometry and topology for autoregressive generation. (Input modality and exclusion compliance need verification).
3.  **B-Rep Distance Functions (BR-DF): How to Represent a B-Rep Model by Volumetric Distance Functions? (2025)** - Proposes a volumetric distance function representation for B-Reps and a diffusion model for generation. (Application to point cloud input is unclear).

## Notes and Gaps
*   **Evidence Gap:** The search relied primarily on paper abstracts. This level of evidence is insufficient to conclusively verify that a method does **not** rely on CAD operation sequences, CSG, or program synthesis, which was a critical user requirement.
*   **Topic Skew:** The retrieved set is skewed towards **unconditional B-Rep generation** or **image-conditioned generation**. There is a notable shortage of papers specifically addressing **reconstruction from point clouds**, which was the user's highest priority.
*   **Exclusion Risks:** Several promising papers (e.g., `Brep2Seq`) were identified but their abstracts contained terms like "parametrized feature-based modeling operations," which strongly suggest a violation of the exclusion criteria. These were therefore not included as verified candidates.
*   **Venue Coverage:** The search successfully identified relevant pre-prints (arXiv) but found fewer papers from major computer vision/geometry conferences (CVPR, SIGGRAPH, etc.) within the 2021-2024 period that strictly met all criteria.

## Recommended Next Steps
1.  **Manual Verification:** The most critical step is to manually review the full text of the "Verified Candidates" (`Point2Brep`, `BrepGPT`, `HoLa`) to definitively confirm they output B-Reps directly and do not use any prohibited methodologies.
2.  **Targeted Search:** Conduct a new, highly targeted search using queries that combine reconstruction and exclusion terms, such as:
    *   `"B-rep reconstruction" point cloud -"operation sequence" -CSG -"program synthesis"`
    *   `"boundary representation" "point cloud" neural network -sketch -extrude`
3.  **Citation Tracking:** Use the "Verified Candidates" as seeds for backward and forward citation analysis to discover related work that may have been missed.
4.  **Venue-Specific Search:** Manually browse the proceedings of key conferences (SIGGRAPH, SIGGRAPH Asia, CVPR, ICCV, ECCV) from 2022-2025 for sessions related to 3D reconstruction, geometric deep learning, and CAD.

TERMINATE
