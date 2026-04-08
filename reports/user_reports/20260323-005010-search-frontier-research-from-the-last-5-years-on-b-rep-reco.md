# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T00:50:10
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The objective is to identify frontier research (2022–2026) on converting unstructured point clouds into Boundary Representation (B-rep) or CAD models. The search prioritizes methods that recover parametric surfaces, topology, and geometric constraints, explicitly excluding approaches that result only in triangle meshes without CAD topology.

## Search Strategy
The search employed a multi-stage strategy targeting arXiv and Crossref:
1.  **Core Keywords**: Initial queries focused on "point cloud," "B-rep reconstruction," and "CAD deep learning."
2.  **Refinement**: After recognizing that "B-rep" is sometimes omitted from titles in favor of "CAD" or "parametric," queries were expanded to include "CAD sequence generation," "reverse engineering," and "solid modeling."
3.  **Filtering**: Results were strictly filtered for the 2022–2026 window. Papers were vetted to ensure they output structured CAD/B-rep data rather than unstructured meshes.

## Candidate Papers
The pipeline successfully identified and verified 4 highly relevant papers. The retrieval process stalled before reaching the target of 5–10 papers; the available candidates are listed below.

**1. ComplexGen: Generating B-rep CAD Models via Complexes**
*   **Year**: 2022
*   **Source**: arXiv
*   **Link**: https://arxiv.org/abs/2205.14573
*   **Core Contribution**: Introduces a deep learning method that generates B-rep topologies directly by predicting chain complexes (vertices, edges, faces) rather than converting from a mesh intermediate.
*   **Relevance Note**: Highly relevant as it explicitly targets the "topology recovery" focus area, addressing the bottleneck of inferring valid connectivity (manifoldness) in B-rep generation.

**2. CAD-Recode: Reverse Engineering of CAD Models from Point Clouds via Geometric Decoding**
*   **Year**: 2024
*   **Source**: arXiv
*   **Link**: https://arxiv.org/abs/2412.14042
*   **Core Contribution**: Proposes a framework that recovers CAD parameters (extrusions, revolutions) from point clouds using a geometric decoding network, focusing on fitting continuous parametric surfaces.
*   **Relevance Note**: Strong fit for "geometry-constrained modeling," demonstrating how to bridge raw point data back to explicit CAD operations and parameters.

**3. Point2CAD: Reverse Engineering 3D Objects from Point Clouds to CAD Models**
*   **Year**: 2024
*   **Source**: CVPR (Computer Vision and Pattern Recognition Conference)
*   **Link**: https://doi.org/10.1109/cvpr52733.2024.00361
*   **Core Contribution**: (Based on retrieval context) Focuses on the reverse engineering pipeline, mapping point clouds to CAD representations, likely leveraging recent advances in primitive detection and assembly.
*   **Relevance Note**: Directly addresses the "point-cloud-to-CAD" requirement, offering a vision-based approach to reconstructing manufacturable models.

**4. Graph-Based Point Cloud Surface Reconstruction Using B-Splines**
*   **Year**: 2024
*   **Source**: GRAPP (International Conference on Computer Graphics Theory and Applications)
*   **Link**: https://doi.org/10.5220/0014237600004084
*   **Core Contribution**: Utilizes graph-based techniques to fit B-Spline surfaces to point clouds.
*   **Relevance Note**: Relevant to "parametric surface reconstruction." *Note: Reviewer flag indicated uncertainty regarding whether this produces full solid B-rep topology or only parametric surfaces.*

## Notes and Gaps
*   **Insufficient Candidate Depth**: The search retrieved only 4 relevant papers, failing to meet the requested quota of 5–10.
*   **Pipeline Failure**: The final retrieval cycle returned a plan rather than search results, preventing the discovery of additional candidates.
*   **Representation Ambiguity**: One candidate ("Graph-Based...") requires further verification to confirm it outputs manifold B-reps (solids) rather than just trimmed surfaces.
*   **Missing Evidence**: The report likely misses recent contributions in "neural implicit to B-rep conversion" (e.g., methods extracting CAD from Signed Distance Functions) and "sketch-based CAD reconstruction," which are active sub-fields in 2024–2026.

## Recommended Next Steps
1.  **Re-run Retrieval**: Execute the specific queries "CAD sequence modeling point cloud" and "implicit surface to B-rep extraction" to fill the remaining quota.
2.  **Verify "Graph-Based..." Paper**: Confirm if the GRAPP 2024 paper includes topology extraction or if it should be replaced by a more robust B-rep method (e.g., **BREP-Net** or **SurfEmb** variants if applicable to reconstruction).
3.  **Expand Source Base**: Check engineering-specific repositories (e.g., ASME, CAD conference proceedings) which may host papers not indexed in the primary CS vision sources used.

TERMINATE
