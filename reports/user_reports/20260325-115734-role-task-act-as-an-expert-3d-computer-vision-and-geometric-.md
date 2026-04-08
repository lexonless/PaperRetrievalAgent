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
**Generated At:** 2026-03-25T11:57:34
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The goal was to identify 8-10 state-of-the-art research papers (2021-2026) that develop neural networks for **direct 3D Boundary Representation (B-Rep) reconstruction and generation**. The core requirements were:
*   **Output:** The model must directly produce the B-Rep data structure (faces, edges, vertices, and their topological relationships).
*   **Input:** Highest priority given to methods taking **unstructured point clouds or 3D scans** as input. Multimodal inputs (image, sketch, text) are acceptable if the method is a breakthrough for B-Reps.
*   **Method:** Must employ modern neural architectures (e.g., transformers, diffusion models, VAEs) for end-to-end B-Rep synthesis.
*   **Strict Exclusions:** Papers outputting CAD operation sequences, CSG trees, or CAD programs were filtered out.

## Search Strategy
The search was conducted in three iterative phases to refine results against the strict criteria:
1.  **Broad Retrieval:** Initial queries for neural B-Rep generation surfaced key papers but included significant off-topic noise (e.g., protein folding, medical imaging).
2.  **Relevance Filtering:** A second pass with stricter keyword filtering removed irrelevant domains and focused on B-Rep-specific literature.
3.  **Input Modality Verification:** A final targeted search for "B-Rep reconstruction from point clouds" ensured the highest-priority input constraint was addressed, surfacing reconstruction-focused work.
Sources included arXiv, Crossref, and OpenAlex. The final set represents a credible snapshot of this nascent field.

## Candidate Papers
The following 8 papers represent the strongest, verified candidates meeting the user's requirements. The credible pool, while meeting the requested minimum, reflects the frontier and specialized nature of this research topic.

**1. Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)**
*   **Source/Venue:** Crossref (SSRN)
*   **Link:** https://doi.org/10.2139/ssrn.6172545
*   **Core Contribution:** Proposes a two-stage framework that segments point clouds into patches, fits parametric surfaces, and then uses learned geometric distance fields to recover edges, vertices, and topology via explicit reasoning.
*   **Relevance Note:** Directly tackles B-Rep reconstruction from unstructured point clouds, integrating learning with geometric modeling. Output is a topologically consistent B-Rep, not a history.

**2. ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)**
*   **Source/Venue:** arXiv
*   **Link:** http://arxiv.org/abs/2205.14573v1
*   **Core Contribution:** Formulates B-Rep reconstruction as the detection of vertices, edges, and surfaces holistically modeled as a chain complex, using a sparse CNN and transformer decoder, followed by global optimization.
*   **Relevance Note:** Takes point clouds as input and outputs a complete B-Rep chain complex. The method directly predicts geometric primitives and their relationships, avoiding intermediate construction sequences.

**3. Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning (2024)**
*   **Source/Venue:** OpenAlex / ACM
*   **Link:** https://doi.org/10.1145/3658155
*   **Core Contribution:** Introduces a top-down method using a neural network (NVD-Net) to predict a Voronoi diagram of B-Rep primitives from a point cloud, then fits a single primitive within each partition.
*   **Relevance Note:** Acquires B-Reps directly from point clouds (or distance fields) via a structure-aware partitioning approach, resulting in parametric surfaces, curves, and vertices.

**4. HoLa: B-Rep Generation using a Holistic Latent Representation (2025)**
*   **Source/Venue:** arXiv / OpenAlex (ACM)
*   **Link:** http://arxiv.org/abs/2504.14257v3
*   **Core Contribution:** Develops a holistic latent space defined only on surfaces that encodes full B-Rep geometry and topology, enabling a diffusion-based generator. Topology is derived via a neural intersection network.
*   **Relevance Note:** Generates B-Reps end-to-end and supports point clouds as one of several input conditions (also images, sketches, text). It directly outputs the B-Rep structure from the latent space.

**5. BrepGPT: Autoregressive B-rep Generation with Voronoi Half-Patch (2025)**
*   **Source/Venue:** arXiv / OpenAlex (ACM)
*   **Link:** http://arxiv.org/abs/2511.22171v1
*   **Core Contribution:** Presents a single-stage autoregressive framework using a Voronoi Half-Patch (VHP) representation and dual VQ-VAEs to tokenize B-Reps, decoded by a transformer.
*   **Relevance Note:** Enables unconditional and conditional B-Rep generation, with point clouds listed as a supported conditioning modality. It autoregressively predicts tokens that decode to a complete B-Rep.

**6. BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024)**
*   **Source/Venue:** arXiv / OpenAlex
*   **Link:** http://arxiv.org/abs/2401.15563v3
*   **Core Contribution:** A diffusion model that generates B-Reps via a hierarchical tree-structured latent geometry, merging duplicated nodes to recover topology, capable of producing free-form surfaces.
*   **Relevance Note:** Directly outputs B-Rep CAD models using a diffusion process. While the abstract emphasizes unconditional generation, it represents a modern neural architecture for direct B-Rep synthesis.

**7. SolidGen: An Autoregressive Model for Direct B-rep Synthesis (2022)**
*   **Source/Venue:** arXiv / OpenAlex
*   **Link:** http://arxiv.org/abs/2203.13944v2
*   **Core Contribution:** An autoregressive neural network that models B-Reps directly by predicting vertices, edges, and faces using transformers and pointer networks, without CAD sequence supervision.
*   **Relevance Note:** Pioneered direct B-rep generation, conditioned on contexts like voxels or images. It outputs an Indexed Boundary Representation, avoiding sketch-and-extrude histories.

**8. NeuroNURBS: Learning Efficient Surface Representations for 3D Solids (2024)**
*   **Source/Venue:** arXiv / OpenAlex
*   **Link:** http://arxiv.org/abs/2411.10848
*   **Core Contribution:** Proposes a method to directly encode NURBS surface parameters for B-Reps, improving efficiency and surface quality over UV-grid approximations in generation tasks.
*   **Relevance Note:** Focuses on improving the geometric representation within neural B-Rep generation pipelines (e.g., enhancing BrepGen). It is a representation breakthrough for direct B-Rep output.

## Notes and Gaps
*   **Field Maturity:** This is a frontier research area. The number of papers that *strictly* use point clouds as the *primary* input for neural B-Rep reconstruction is limited. Many state-of-the-art methods are generative models that support point clouds as one conditioning modality among others.
*   **Input Modality Spectrum:** The papers naturally cluster into:
    *   **Reconstruction-Centric:** Point2Brep, ComplexGen, Split-and-Fit (point cloud as primary, often only, input).
    *   **Generation with Conditioning:** HoLa, BrepGPT (point cloud is one of several possible inputs).
    *   **Unconditional/Multi-modal Generation:** BrepGen, SolidGen, NeuroNURBS (focus on direct B-Rep output architecture).
*   **Evidence Level:** All papers are verified via abstracts. Full-text review would be needed to confirm implementation details and the extent of point-cloud-specific experimentation in the generative papers.
*   **Exclusion Adherence:** The selected papers successfully avoid the prohibited categories (CAD sequences, CSG, programs), focusing on direct B-Rep structure prediction.

## Recommended Next Steps
1.  **Deep Dive into Conditioning:** For the generative papers (BrepGPT, HoLa), examine the full text to understand the implementation and performance of point cloud conditioning specifically.
2.  **Expand to Related Venues:** Search proceedings of geometry-specific conferences (e.g., SGP, Symposium on Geometry Processing) and CAD-focused venues (e.g., CAD, ASME DETC) for reconstruction-focused work that may not be on arXiv.
3.  **Follow Citation Trails:** Use the core papers (SolidGen, ComplexGen) as seeds for backward and forward citation analysis to discover related work.
4.  **Benchmark Awareness:** Investigate the datasets used by these papers (e.g., ABC dataset, Fusion 360 Gallery) to understand the complexity and diversity of B-Reps currently addressed by neural methods.

TERMINATE
