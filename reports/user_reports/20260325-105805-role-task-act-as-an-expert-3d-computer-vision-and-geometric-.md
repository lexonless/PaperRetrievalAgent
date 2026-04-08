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
**Generated At:** 2026-03-25T10:58:05
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to find state-of-the-art research papers (2021-2026) focused on the direct neural generation or reconstruction of 3D Boundary Representation (B-Rep) data structures. The core requirement is a method that takes an unstructured point cloud or 3D scan as input and outputs a complete B-Rep (faces, edges, vertices, and their topological relationships). The search strictly excluded work on CAD operation sequences, CSG trees, or program synthesis, prioritizing modern neural architectures like transformers, diffusion models, and autoregressive networks.

## Search Strategy
The search was conducted in three iterative phases using Crossref, OpenAlex, and arXiv:
1.  **Initial Broad Search:** Queries focused on "B-Rep generation" and "neural implicit representation" to capture the target output. This returned many relevant generative models but lacked confirmation of point cloud input.
2.  **Refined Focus on Input Modality:** Queries were sharpened to explicitly include "point cloud to B-Rep" and "3D scans". This improved the set but still yielded papers where point clouds were one of many conditional inputs, not the primary focus.
3.  **Over-Correction to Reconstruction:** A final phase targeted "B-Rep reconstruction from point clouds". This retrieved papers on point cloud processing and segmentation but largely missed the core task of direct B-Rep generation.

The reviewer halted the process after three revisions, concluding the search did not meet the quality bar. The primary failure was an inability to reliably identify a sufficient number of papers that demonstrably use point clouds as the *primary* input for direct B-Rep synthesis, based on abstract-level evidence.

## Candidate Papers
**The search did not clear the quality bar.** No papers were found that could be fully verified as meeting all strict user criteria (primary point cloud input, direct B-Rep output, exclusion of operation sequences). The results are split into two categories based on partial evidence.

### Verified Candidates
Papers with `verification_status` of `partial` that show strong relevance to B-Rep generation, though point cloud input is not confirmed as primary.
*   **HoLa: B-Rep Generation using a Holistic Latent Representation (2025, arXiv)**
    *   **Core Contribution:** Proposes a holistic latent space that unifies B-Rep geometry and topology, enabling a diffusion-based generator. It explicitly lists point clouds as a supported input modality alongside images and text.
    *   **Relevance Note:** Aims for direct B-Rep generation and claims high validity rates. The abstract confirms it accepts point cloud input, but does not specify if it is the primary focus.
*   **BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch (2025, arXiv)**
    *   **Core Contribution:** Introduces a single-stage autoregressive framework using a Voronoi Half-Patch representation for B-Rep generation.
    *   **Relevance Note:** The abstract states the framework supports conditional generation from point clouds (among other modalities). It is a direct B-Rep generator, but point cloud input appears as one of several conditions.
*   **BRep Boundary and Junction Detection for CAD Reverse Engineering (2024, OpenAlex)**
    *   **Core Contribution:** Presents BRepDetNet, a supervised network to detect B-Rep boundaries and junctions from 3D scans as a step towards Scan-to-CAD.
    *   **Relevance Note:** Directly tackles B-Rep element detection from scans. However, it is a detection/segmentation model, not a full B-Rep reconstruction or generator.

### Unverified Leads
The following are high-potential titles from the search that appear to be about direct B-Rep generation but lack evidence in the retrieved snippets to verify point cloud input or exclude operation sequences. They are suggested as leads for follow-up manual investigation.
1.  **SolidGen: An Autoregressive Model for Direct B-rep Synthesis (2022, arXiv)** – A seminal direct B-Rep generation model. The abstract does not mention input modality.
2.  **AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025, arXiv)** – A transformer-based model for autoregressive B-Rep generation. Input modality is not specified in the snippet.
3.  **BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024, arXiv)** – A diffusion model that directly outputs B-Reps. The abstract discusses unconditional generation and conditioning, but not specifically on point clouds.

## Notes and Gaps
*   **Evidence Limitation:** Verification relied on abstract snippets, which often omit detailed descriptions of input modalities and training paradigms, making it impossible to confirm strict exclusion criteria.
*   **Search Drift:** The search struggled to balance the dual constraints of "direct B-Rep output" and "point cloud as primary input." Queries for generation retrieved multi-modal works, while queries for reconstruction retrieved non-B-Rep point cloud methods.
*   **Scarcity of Perfect Matches:** The niche of *neural, point-cloud-to-B-Rep* reconstruction appears to be very specialized. Many state-of-the-art B-Rep generation papers (e.g., SolidGen, BrepGen) focus on unconditional generation or multi-modal conditioning, with point clouds as a secondary option.
*   **Potential Seminal Works Missed:** Known models like **BRepNet** (likely pre-2021) or **Point2Cyl** were not retrieved, possibly due to year-range filters or because they do not frame their task as "generation."

## Recommended Next Steps
1.  **Manual Verification of Leads:** Investigate the full text of the "Unverified Leads" (SolidGen, AutoBrep, BrepGen) and the "Verified Candidates" to definitively confirm their input modalities and output specifications.
2.  **Citation-Chain Exploration:** Use the promising papers (e.g., HoLa, SolidGen) as seeds. Examine papers that cite them or that they cite to find related work specifically focused on point cloud input.
3.  **Venue-Specific Search:** Manually search proceedings of top-tier venues (SIGGRAPH, CVPR, NeurIPS) from 2021-2026 for keywords like "B-Rep", "boundary representation", and "CAD" to identify papers that may have been missed by generic queries.
4.  **Broaden Input Definition:** If the user's priority is the *direct B-Rep output* breakthrough, consider accepting papers that use point clouds as one of several valid conditional inputs, noting this as a current trend in the field.

TERMINATE
