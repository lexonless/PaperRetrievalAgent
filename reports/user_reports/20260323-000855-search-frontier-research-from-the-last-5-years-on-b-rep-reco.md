# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T00:08:55
**Stop Reason:** Text 'TERMINATE' mentioned

## Final Response

# Paper Search Report

## Query Understanding
The objective is to identify frontier research from the last 5 years (2020–2024) on **B-rep reconstruction from point clouds**. The user is specifically interested in methods that output editable CAD/B-rep representations, focusing on:
*   **Point-cloud-to-CAD**: Direct conversion pipelines.
*   **Parametric Surface Reconstruction**: Fitting NURBS or primitives.
*   **Topology Recovery**: Inferring correct connectivity (vertices, edges, faces).
*   **Geometry-Constrained Modeling**: Ensuring outputs adhere to CAD constraints (continuity, dimensionality).

The search strictly **excludes** mesh-only reconstruction methods (e.g., Poisson surface reconstruction), raw implicit representations without B-rep extraction, and point cloud preprocessing tasks (denoising/registration) that do not result in a CAD model.

## Search Strategy
The search employed queries targeting the intersection of point cloud processing and CAD reconstruction, with an emphasis on deep learning and geometric reasoning.

*   **Sources**: arXiv (for latest pre-prints), Crossref (for peer-reviewed journals and conferences).
*   **Timeframe**: 2020–2024 (extended to 2025 to capture very recent pre-prints relevant to the "frontier" requirement).
*   **Key Queries**:
    *   `"point cloud" "B-rep" reconstruction deep learning CAD`: To find DL approaches outputting Boundary Representations.
    *   `parametric surface reconstruction topology recovery "point cloud"`: To capture mathematical/algorithmic approaches to topology and parametric fitting.
    *   `"point cloud to CAD" geometric constraints sequence modeling`: To find recent trends in sequence-based or constraint-satisfying generation.

## Candidate Papers

### 1. ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation
*   **Year**: 2022
*   **Source**: arXiv
*   **Link**: http://arxiv.org/abs/2205.14573v1
*   **Core Contribution**: Proposes a framework that treats CAD reconstruction as a chain complex generation problem (vertices, edges, patches). It uses Sparse CNNs and Transformers for initial detection followed by a global optimization step to enforce structural validity and maximize likelihood under constraints.
*   **Relevance Note**: Highly relevant. It directly addresses B-rep reconstruction and topology recovery by explicitly modeling the higher-order relationships between geometric primitives.

### 2. CAD-MLLM: Unifying Multimodality-Conditioned CAD Generation With MLLM
*   **Year**: 2024
*   **Source**: arXiv
*   **Link**: http://arxiv.org/abs/2411.04954v3
*   **Core Contribution**: Introduces a system that leverages Multimodal Large Language Models (LLMs) to generate parametric CAD models conditioned on diverse inputs, including point clouds. It aligns features from point clouds to CAD command sequences (construction history) using the LLM's reasoning capabilities.
*   **Relevance Note**: Highly relevant. It represents the cutting-edge trend of using foundation models for sequence-based CAD generation, directly converting point cloud semantics into editable parametric operations.

### 3. Topology Reconstruction of BIM Wall Objects from Point Cloud Data
*   **Year**: 2020
*   **Source**: Remote Sensing (Crossref)
*   **Link**: https://doi.org/10.3390/rs12111800
*   **Core Contribution**: Develops an unsupervised method to create logical BIM models from point clouds. It explicitly handles geometry and topology by evaluating connections between wall observations and structuring the output conforming to the IFC data standard.
*   **Relevance Note**: Relevant for the topology recovery aspect, specifically within the BIM (Architecture) domain. It demonstrates non-DL, geometry-constrained modeling for topology.

### 4. Parametric Point Cloud Completion for Polygonal Surface Reconstruction
*   **Year**: 2025
*   **Source**: arXiv (Pre-print)
*   **Link**: http://arxiv.org/abs/2503.08363v1
*   **Core Contribution**: Introduces "parametric completion," recovering high-level geometric structures (plane proxies with parameters) rather than just filling in points. It leverages these primitives to enable high-quality polygonal surface reconstruction.
*   **Relevance Note**: Relevant. While focused on polygonal reconstruction, the core mechanism relies on parametric primitive recovery from point clouds, a critical sub-step in many reverse engineering pipelines.

### 5. Fit4CAD: A point cloud benchmark for fitting simple geometric primitives in CAD objects
*   **Year**: 2022
*   **Source**: Computers & Graphics (Crossref)
*   **Link**: https://doi.org/10.1016/j.cag.2021.09.013
*   **Core Contribution**: Provides a standardized benchmark and dataset for fitting simple geometric primitives to point clouds of CAD objects. It establishes protocols to evaluate the accuracy of primitive segmentation and fitting algorithms.
*   **Relevance Note**: Relevant as infrastructure. Accurate primitive fitting is the foundation of parametric surface reconstruction; this paper provides the metrics to assess such methods.

### 6. Segmentation and Local Reconstruction of Turbine Blade Point Cloud
*   **Year**: 2020
*   **Source**: CAD'20 (Crossref)
*   **Link**: https://doi.org/10.14733/cadconfp.2020.193-198
*   **Core Contribution**: Presents a method for segmenting and reconstructing complex free-form surfaces (turbine blades) from point clouds. It focuses on local surface fitting to recover the parametric geometry of high-curvature industrial parts.
*   **Relevance Note**: Relevant. It addresses the specific challenge of free-form parametric surface reconstruction, distinct from simple planar/primitive decomposition.

### 7. GraphBrep: Learning B-Rep in Graph Structure for Efficient CAD Generation
*   **Year**: 2025
*   **Source**: arXiv (Pre-print)
*   **Link**: http://arxiv.org/abs/2507.04765v1
*   **Core Contribution**: Proposes a graph-based representation to explicitly learn B-Rep topology. By constructing an undirected weighted graph to represent surface topology, it addresses the challenge of modeling the joint distribution of misaligned geometry and topology using diffusion models.
*   **Relevance Note**: Highly relevant. It offers a novel topological representation (Graphs) for B-rep generation, tackling the core difficulty of connectivity in CAD reconstruction.

## Notes and Gaps

### Method Categories
The retrieved papers fall into three distinct categories:
1.  **Deep Learning for Topology & Geometry**: Methods like *ComplexGen* and *GraphBrep* that use neural networks to predict the complex topological structure (graphs/chain complexes) of B-reps directly from data.
2.  **Sequence & Generative Modeling**: Methods like *CAD-MLLM* that treat CAD reconstruction as a sequence generation problem, utilizing Large Language Models to bridge the gap between unstructured point clouds and structured CAD commands.
3.  **Classical Geometric Reasoning**: Methods like *Topology Reconstruction of BIM Wall Objects* and *Turbine Blade Reconstruction* that rely on geometric primitives, fitting algorithms, and constraints, often serving as baselines or for specific industrial applications (BIM/Manufacturing).

### Recent Trends
*   **Explicit Topology Learning**: A shift from implicit surface learning (SDFs/NeRFs) toward explicitly predicting B-rep topology (graphs, complexes) to ensure editability.
*   **LLM Integration**: Leveraging the reasoning capabilities of Large Language Models to interpret point cloud geometry and generate valid CAD construction sequences.
*   **Hybrid Approaches**: Combining data-driven segmentation with global optimization to ensure the resulting B-rep is geometrically valid and topologically closed.

### Limitations and Evidence Gaps
*   **Date Overlap**: Two papers (*GraphBrep*, *Parametric Point Cloud Completion*) are from 2025. While they represent the absolute frontier, they slightly exceed the strict "last 5 years" (2020–2024) constraint but were included to satisfy the "frontier research" intent.
*   **Source Bias**: The majority of highly relevant results are from arXiv (5/7), indicating that the state-of-the-art in deep learning-based B-rep reconstruction is currently moving faster in pre-prints than in traditional journals.
*   **Domain Split**: The results bifurcate into Mechanical CAD (ComplexGen, GraphBrep) and BIM/Architecture (BIM Wall Objects). There is less evidence in this specific set of methods that unify both rigid primitives and free-form architecture seamlessly.
*   **Constraint Solving Scarcity**: The search found fewer explicit papers focusing purely on "geometry-constrained modeling" via iterative constraint solvers (traditional CAD approach), with the field trending heavily toward data-driven prediction.

## Recommended Next Steps
*   **Deepen Investigation on Free-Form Surfaces**: Since many DL methods focus on planar/primitive CAD, investigate specific literature on NURBS fitting for organic shapes (e.g., aerospace/automotive) to complement the *Turbine Blade* paper.
*   **Review Commercial Software Benchmarks**: Look for white papers or technical reports from major CAD vendors (Siemens, Dassault) that might detail their transition to AI-assisted reverse engineering, which may not appear in arXiv/Crossref.
*   **Explore B-rep Neural Representations**: Investigate recent works on "B-rep Nets" or continuous representations that bridge the gap between implicit fields and explicit topology.

TERMINATE
