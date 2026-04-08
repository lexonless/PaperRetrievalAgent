# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-22T23:23:40
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The user seeks frontier research from the last 5 years (2020–2025) on converting raw point clouds into structured Boundary Representations (B-rep) or CAD models. The focus is explicitly on methods that output parametric surfaces (e.g., NURBS), recover topology (wireframes, connectivity), or enforce geometric constraints. Mesh-only reconstruction methods and generic point cloud processing tasks (classification/segmentation) are excluded.

## Search Strategy
The search strategy evolved through three phases:
1.  **Broad Deep Learning Search:** Initial queries targeted "point cloud to B-rep" and "deep learning CAD," identifying high-impact papers like *ComplexGen*.
2.  **Parametric & Topology Refinement:** Specific queries were added to capture "parametric surface reconstruction," "topology recovery," and "CSG (Constructive Solid Geometry) reconstruction" to balance neural methods with geometric/topological approaches.
3.  **Gap Filling:** Attempts were made to retrieve traditional optimization-based methods using keywords like "NURBS fitting" and "geometry-constrained modeling" to mitigate the bias toward purely data-driven approaches.

Despite multiple queries across arXiv, Crossref, IEEE, and Elsevier, significant gaps remain in retrieving abstracts for several parametric papers due to access restrictions or script-based redirects during the retrieval phase.

## Candidate Papers

### 1. ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation
*   **Year:** 2022
*   **Source:** arXiv
*   **Link:** http://arxiv.org/abs/2205.14573v1
*   **Core Contribution:** Proposes modeling B-rep reconstruction as a chain complex generation problem. It uses a sparse CNN encoder and tri-path transformer to predict vertices, edges, and faces, followed by a global optimization to ensure structural validness.
*   **Relevance Note:** Highly relevant. Explicitly targets B-rep topology (vertices/edges/faces) rather than just surface geometry.

### 2. D²CSG: Unsupervised Learning of Compact CSG Trees
*   **Year:** 2023
*   **Source:** arXiv
*   **Link:** http://arxiv.org/abs/2301.11497v2
*   **Core Contribution:** Introduces a dual-branch neural network (cover and residual) to learn compact CSG trees without supervision. It handles complex CAD shapes by decomposing them into quadric primitives and Boolean operations.
*   **Relevance Note:** High. Represents the "CSG reconstruction" sub-field, producing structured CAD-compatible primitives from point clouds/occupancy data.

### 3. UCSG-Net -- Unsupervised Discovering of Constructive Solid Geometry Tree
*   **Year:** 2020
*   **Source:** arXiv
*   **Link:** http://arxiv.org/abs/2006.09102v3
*   **Core Contribution:** An early unsupervised method that predicts primitive parameters and discovers the Boolean operator tree structure dynamically to reconstruct shapes from SDF inputs.
*   **Relevance Note:** High. Establishes the trend of unsupervised CSG tree discovery for CAD reconstruction.

### 4. Parametric Point Cloud Completion for Polygonal Surface Reconstruction (PaCo)
*   **Year:** 2025
*   **Source:** arXiv
*   **Link:** http://arxiv.org/abs/2503.08363v1
*   **Core Contribution:** Introduces "parametric completion," recovering plane proxies (parameters + inliers) instead of raw points to assist polygonal surface reconstruction in incomplete data scenarios.
*   **Relevance Note:** Medium-High. Focuses on parametric primitives, though the output is polygonal surfaces rather than explicit B-rep/NURBS CAD models.

### 5. Topology‐Aware Surface Reconstruction for Point Clouds
*   **Year:** 2020
*   **Source:** Computer Graphics Forum
*   **Link:** https://doi.org/10.1111/cgf.14079
*   **Core Contribution:** Uses topological priors (persistence diagrams) within an optimization framework to reconstruct surfaces that strictly adhere to topological constraints, filtering out topological noise.
*   **Relevance Note:** Medium. Focuses heavily on topology recovery, but typically outputs implicit surfaces or meshes rather than explicit CAD B-reps.

### 6. Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds
*   **Year:** 2026 (SSRN Pre-print)
*   **Source:** SSRN / Crossref
*   **Link:** https://doi.org/10.2139/ssrn.6172545
*   **Core Contribution:** A two-stage framework integrating learning-guided region growing for surface patching and geometric reasoning for edge/vertex recovery to build topologically consistent B-reps.
*   **Relevance Note:** High (Title match). However, the 2026 date suggests it may be a future publication or in-press work; verification required.

### 7. Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction
*   **Year:** 2021
*   **Source:** Computer-Aided Design
*   **Link:** https://doi.org/10.1016/j.cad.2021.103090
*   **Core Contribution:** [Abstract retrieval failed]. Likely covers fitting parametric surfaces to Lidar data for buildings based on the title.
*   **Relevance Note:** High Potential. Directly addresses "parametric surface fitting," but lack of abstract prevents confirming if B-rep topology is recovered.

### 8. PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds
*   **Year:** 2024
*   **Source:** CVPR
*   **Link:** https://doi.org/10.1109/cvpr52733.2024.02624
*   **Core Contribution:** [Abstract retrieval failed]. Likely focuses on extracting wireframe topology from LiDAR for buildings based on the title.
*   **Relevance Note:** High Potential. Addresses "wireframe" (topology) and "parametric" aspects, which is critical for CAD reconstruction.

## Notes and Gaps
*   **Evidence Quality (Abstracts):** A significant limitation in this search is the failure to retrieve abstracts for high-value traditional/parametric papers, specifically Coiffier et al. (2021) and Huang et al. (2024). The retriever encountered HTML scripts/redirects rather than text content. Consequently, it is unconfirmed if these methods produce full B-reps or just surface patches.
*   **Methodology Bias:** The successfully retrieved full-text papers lean heavily toward Deep Learning (ComplexGen, CSG-Nets). There is a gap in "classical" optimization methods (e.g., RANSAC-based primitive fitting with hard constraints) due to the retrieval issues mentioned above.
*   **Mesh vs. B-rep Ambiguity:** Some papers, like *PaCo* (2025) and *Topology-Aware Surface Reconstruction* (2020), focus on "polygonal surfaces." While they use parametric or topological reasoning, their final output may not be a standard CAD B-rep (with trimmed NURBS/solid topology), requiring further investigation.
*   **Future-Dated Publication:** *Point2Brep* is dated 2026, which may be a data error or a pre-publication draft; this requires verification before citing as current state-of-the-art.

## Recommended Next Steps
1.  **Retry Abstract Retrieval:** Use text-mode extraction or alternative sources (e.g., Semantic Scholar, direct PDF lookup) to obtain abstracts for Coiffier (2021) and Huang (2024) to verify their B-rep output capabilities.
2.  **Verify Metadata:** Confirm the publication date and status of *Point2Brep* (SSRN 6172545).
3.  **Classical Methods Search:** Explicitly target CAD-specific journals (e.g., *Computer-Aided Design*, *CAD/Graphics*) with keywords like "NURBS reverse engineering," "constrained fitting," and "primitive segmentation" to fill the gap in traditional non-DL methods.
4.  **Filter Polygonal Methods:** Distinguish between papers that reconstruct "polygonal meshes" vs. those that explicitly construct "B-Rep topology graphs" to strictly adhere to the user's exclusion of mesh-only methods.

TERMINATE
