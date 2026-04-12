**Generated At:** 2026-04-13T00:49:36
**Stop Reason:** Text 'TERMINATE' mentioned

# Paper Search Report

## Query Understanding

The user requested 8-10 state-of-the-art research papers (2021-2026) focused on 3D Boundary Representation (B-Rep) reconstruction and generation. The core requirement is that the model's primary output must be the B-Rep data structure itself (faces, edges, vertices, topology), generated directly from unstructured point clouds or 3D scans using modern neural architectures. The search must strictly exclude methods that output CAD operation sequences, CSG trees, or program synthesis.

## Search Strategy

- Initial queries targeted neural direct B-Rep generation and end-to-end learning of B-Rep topology.
- Subsequent revisions aimed to improve source diversity and focus on point-cloud-to-B-Rep reconstruction.
- Final queries attempted to balance generative models with reconstruction papers, but the retrieval was misled by broad point cloud topics.

## Candidate Papers

The search did not clear the quality bar. After three review cycles, the team could not assemble a robust set of 8-10 distinct, credible papers that strictly meet the user's inclusion and exclusion criteria. The latest retrieval, while having adequate source coverage, was dominated by papers irrelevant to direct B-Rep generation (e.g., point cloud compression, completion, general surveys). Only a handful of verified candidates were identified.

### Verified Candidates

### 1. BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024)

- **Source:** `arXiv / OpenAlex`
- **Link:** [Open paper](http://arxiv.org/abs/2401.15563v3)
- **Summary:** A diffusion-based generative model that directly outputs a B-Rep CAD model using a hierarchical tree-structured latent representation. It employs Transformer-based diffusion to denoise node features and recovers topology by merging duplicated nodes, enabling the generation of shapes with free-form surfaces.
- **Why Included:** Directly outputs a B-Rep data structure using a modern neural architecture (diffusion model). It is a core, highly cited paper in neural B-Rep generation, strictly avoiding operation sequences.

### 2. ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)

- **Source:** `arXiv / OpenAlex`
- **Link:** [Open paper](http://arxiv.org/abs/2205.14573v1)
- **Summary:** Reconstructs CAD models in B-Rep by detecting geometric primitives (vertices, edges, surfaces) and their correspondences, modeled as a chain complex. It uses a sparse CNN encoder for point cloud processing and a transformer decoder, followed by global optimization to recover a valid B-Rep.
- **Why Included:** Directly reconstructs B-Rep models from point clouds using a neural framework, outputting the topological and geometric structure without a construction history.

### Unverified Leads

### 1. Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds (2026)

- **Source:** `Crossref`
- **Link:** [Open paper](https://doi.org/10.2139/ssrn.6172545)
- **Summary:** A framework that reconstructs complete and topologically consistent B-rep models from noisy point clouds by integrating learning-based surface patch segmentation with geometric reasoning to recover edges and vertices.
- **Why Included:** Title and abstract strongly suggest direct B-Rep reconstruction from point clouds, aligning perfectly with the primary input requirement. However, full verification of its neural architecture and exclusion of operation sequences is needed.

### 2. HoLa: B-Rep Generation using a Holistic Latent Representation (2025)

- **Source:** `arXiv`
- **Link:** [Open paper](http://arxiv.org/abs/2504.14257v3)
- **Summary:** Introduces a holistic latent space that unifies B-Rep geometry and topology, learning to derive curve geometries from surface pairs via a neural intersection network, enabling diffusion-based generation from various inputs.
- **Why Included:** Proposes a novel neural representation for B-Reps and a diffusion-based generator, indicating direct B-Rep output. Its input includes point clouds, but full verification against exclusion criteria is pending.

### 3. AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025)

- **Source:** `arXiv`
- **Link:** [Open paper](http://arxiv.org/abs/2512.03018v1)
- **Summary:** An autoregressive Transformer model that tokenizes B-Rep geometry and topology into a unified sequence, generating watertight B-Reps via next-token prediction.
- **Why Included:** Represents a state-of-the-art neural approach for direct B-Rep generation. The abstract confirms output is a B-Rep, but its primary input modality requires verification to ensure alignment with point cloud focus.

## Notes and Gaps

- The search consistently struggled to find a sufficient volume of papers specifically on point-cloud-to-B-Rep reconstruction. The field appears niche, with many neural CAD papers focusing on operation sequences or CSG, which were excluded.
- Recent trends are strongly towards generative models (diffusion, autoregressive) for B-Rep synthesis, but these often use category labels or latent codes as input, not strictly point clouds.
- Source diversity was achieved in the final attempt, but at the cost of relevance, indicating a trade-off between broad sourcing and precise topic filtering.
- The exclusion of 'neural implicit surface reconstruction' papers was necessary but may have removed some relevant work that bridges to B-Rep output.

## Recommended Next Steps

- Conduct a targeted search using precise Boolean queries in academic databases (e.g., "B-Rep" AND "point cloud" AND (reconstruction OR generation) NOT "CSG" NOT "operation sequence").
- Manually examine proceedings of key venues (SIGGRAPH, CVPR, NeurIPS) from 2021-2026 for sessions on 3D reconstruction and CAD learning.
- Verify the unverified leads by reading their full texts to confirm they output B-Rep data structures and use point clouds as a primary input.
- Consider expanding the input scope slightly to include multimodal inputs if the method represents a major breakthrough in direct B-Rep generation, as per the user's original allowance.
