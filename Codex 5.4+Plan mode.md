# Codex 5.4+Plan mode

1. **Title & Year:** *ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation* (2022)
   **Source/Venue:** ACM Transactions on Graphics (SIGGRAPH 2022)
   **Link:** [arXiv](https://arxiv.org/abs/2205.14573)
   **Core Contribution:** Models B-Rep reconstruction as generation of a **chain complex** over vertices, edges, and surface patches. It combines a sparse CNN encoder, tri-path transformer decoder, and global constrained optimization to recover a structurally valid B-Rep.
   **Relevance Note:** Input is a **point cloud**. The output is a direct **B-Rep chain complex / final CAD B-Rep**, not a construction history. It reconstructs topology and geometry jointly and does **not** rely on sketch-extrude or CAD programs.
2. **Title & Year:** *SolidGen: An Autoregressive Model for Direct B-rep Synthesis* (2023)
   **Source/Venue:** Transactions on Machine Learning Research (TMLR 2023)
   **Link:** [Autodesk page](https://www.research.autodesk.com/publications/solidgen/)
   **Core Contribution:** One of the earliest strong **direct neural B-Rep generators**, using transformers and pointer networks to autoregressively emit vertices, edges, and faces in an indexed B-Rep hierarchy.
   **Relevance Note:** Input can be unconditional or conditioned on labels/images/voxels. The model directly predicts the **final B-Rep elements and their relations**, with no CAD operation sequence, sketch tree, or program synthesis stage.
3. **Title & Year:** *Split-and-Fit: Learning B-Reps via Structure-Aware Voronoi Partitioning* (2024)
   **Source/Venue:** ACM Transactions on Graphics (2024)
   **Link:** [arXiv](https://arxiv.org/abs/2406.05261)
   **Core Contribution:** Introduces a top-down reconstruction pipeline where a network first predicts a **Voronoi-style partition** revealing primitive count and connectivity, then fits parametric primitives to obtain the B-Rep.
   **Relevance Note:** Input is a **point cloud or distance field**. Output is a direct B-Rep made of **parametric surfaces, curves, and vertices**. It reconstructs the final representation itself and does **not** infer modeling steps.
4. **Title & Year:** *BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry* (2024)
   **Source/Venue:** ACM Transactions on Graphics (SIGGRAPH 2024)
   **Link:** [Project page](https://brepgen.github.io/)
   **Core Contribution:** A hierarchical **diffusion model** over a structured latent tree, where geometry is stored in node features and topology is recovered through duplicated-node merging. It was a major step beyond prismatic-only CAD generation.
   **Relevance Note:** Typically unconditional/category-conditional generation. The target is the **full B-Rep** with faces, edges, vertices, and topology. It is explicitly proposed as an alternative to sequence-supervised CAD generation, so it does **not** depend on operation histories.
5. **Title & Year:** *DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry* (2025)
   **Source/Venue:** CVPR 2025
   **Link:** [CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Li_DTGBrepGen_A_Novel_B-rep_Generative_Model_through_Decoupling_Topology_and_CVPR_2025_paper.html)
   **Core Contribution:** Explicitly separates **topology generation** from **geometry generation**, first predicting valid edge-face and edge-vertex adjacencies, then generating vertices, curves, and faces with transformer-based diffusion.
   **Relevance Note:** Direct generative B-Rep model. Output is the final **topology + B-spline geometry**, not a CAD script. This is one of the clearest papers focused on joint validity of B-Rep topology and geometry without sequence supervision.
6. **Title & Year:** *CADDreamer: CAD Object Generation from Single-view Images* (2025)
   **Source/Venue:** CVPR 2025
   **Link:** [CVPR Open Access](https://openaccess.thecvf.com/content/CVPR2025/html/Li_CADDreamer_CAD_Object_Generation_from_Single-view_Images_CVPR_2025_paper.html)
   **Core Contribution:** Uses a primitive-aware multi-view diffusion pipeline plus geometric fitting/optimization to convert a **single RGB image** into a compact, watertight CAD **B-Rep**.
   **Relevance Note:** Input is a **single-view image**. Although it uses intermediate mesh and primitive reasoning, the target output is a **complete B-Rep CAD model**, not an operation sequence. It stays on the final representation side of the boundary you set.
7. **Title & Year:** *BrepDiff: Single-Stage B-rep Diffusion Model* (2025)
   **Source/Venue:** SIGGRAPH 2025 Conference Papers
   **Link:** [Project page](https://brepdiff.github.io/)
   **Core Contribution:** Proposes a simpler **single-stage diffusion** formulation using masked UV grids for faces, avoiding the multi-stage cascades common in earlier B-Rep generators.
   **Relevance Note:** The model generates a direct **B-Rep-oriented geometric representation** and then reconstructs a valid solid B-Rep through postprocessing. It does **not** output CAD programs or modeling histories; the final target remains the B-Rep.
8. **Title & Year:** *HoLa: B-Rep Generation using a Holistic Latent Representation* (2025)
   **Source/Venue:** ACM Transactions on Graphics (SIGGRAPH 2025)
   **Link:** [arXiv](https://arxiv.org/abs/2504.14257)
   **Core Contribution:** Introduces a **holistic latent space** that encodes the whole B-Rep primarily through surfaces, with a neural intersection network recovering curves, vertices, and topology. It enables diffusion-based generation from multiple modalities.
   **Relevance Note:** Supports **point clouds, images, sketches, and text** as inputs/conditions. The output is still a **full B-Rep**, not a modeling program. This is a strong example of latent-space-native B-Rep generation.
9. **Title & Year:** *AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry* (2025)
   **Source/Venue:** ACM Transactions on Graphics / SIGGRAPH Asia 2025 Proceedings
   **Link:** [Autodesk page](https://www.research.autodesk.com/publications/auto-brep-generation-unified-topology-geometry/)
   **Core Contribution:** Unifies topology and geometry as a **single discrete token stream** traversed over the face adjacency graph, showing that next-token prediction can scale to more complex watertight solids.
   **Relevance Note:** Direct B-Rep generation with no intermediate CAD program. The model outputs geometry tokens and topological references that decode into the **final B-Rep structure** rather than step-by-step editing operations.

1. **Title & Year:** *BRep-GD: a Graph Diffusion Model for CAD Boundary Representation Generation* (2026)
   **Source/Venue:** IEEE Transactions on Visualization and Computer Graphics (online ahead of print, 2026)
   **Link:** [PubMed record](https://pubmed.ncbi.nlm.nih.gov/41870942/)
   **Core Contribution:** Moves from tree-centric to **graph-centric diffusion**, treating faces as nodes and boundary/vertex elements as graph relations, with continuous topology decoupling for efficiency and consistency.
   **Relevance Note:** Direct generative B-Rep model. The output is the final **graph-structured B-Rep**, not a CAD command sequence or CSG tree. It is especially relevant for recent work that treats topology as a first-class diffusion target.



# gemini web + deep research

**Title & Year:** ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation (2022)

**Source/Venue:** ACM Transactions on Graphics (SIGGRAPH)

**Link:** https://doi.org/10.1145/3528223.3530076 

**Core Contribution:** ComplexGen formulates direct B-Rep reconstruction by modeling the continuous geometry as a rigorous B-Rep chain complex, utilizing a tri-path deep neural network architecture to predict a probabilistic structure, which is subsequently decoded into a definite, structurally valid CAD model via strict global optimization.

**Relevance Note:** ComplexGen serves as a landmark foundational paper in the domain of direct geometric reconstruction from unstructured point clouds. It completely avoids the paradigm of sequence prediction and heuristic CSG primitive combinations by treating B-Rep elements mathematically as a chain complex. The framework explicitly defines boundary operator constraints, such as ensuring that an edge is always adjacent to exactly two faces, and that a face maintains closed boundary loops without topological gaps. The architecture generates vertices, edges, and faces simultaneously with a high awareness of their co-occurrence. By applying geometric refinements globally rather than sequentially, the model directly outputs a native, watertight topological data structure. This framework proved that an end-to-end neural solver could handle the quadratic complexity of face-edge-vertex adjacency matrices and enforce rigorous manifold conditions without ever dropping into an intermediate sketch-and-extrude history modeling step.

**Title & Year:** SolidGen: An Autoregressive Model for Direct B-rep Synthesis (2023)

**Source/Venue:** Transactions on Machine Learning Research (TMLR) / ICLR 2024

**Link:** https://openreview.net/forum?id=ZR2CDgADRo 

**Core Contribution:** SolidGen introduces a novel Indexed Boundary Representation that encodes geometric parameters and topological relations into a well-defined sequence hierarchy, utilizing an autoregressive Transformer combined with pointer neural networks to explicitly synthesize B-Rep vertices, edges, and faces directly.

**Relevance Note:** This model provides the definitive proof that direct B-Rep synthesis can be framed as a next-element sequence prediction problem without defaulting to CAD construction histories. SolidGen does not predict modeling commands; rather, it predicts the explicit geometric elements of the final CAD file. The integrated pointer network acts as a strict topological referencing mechanism to construct the adjacency graph dynamically. For example, when an edge is generated, the pointer network selects the specific previously generated vertices that bound it, and when a face is generated, it points to the specific edges that constitute its trimming loops. This methodology directly outputs the continuous parameterizations and discrete interconnections of the B-Rep. It allows for highly flexible unconditional generation, as well as conditioning on images or unorganized voxel data, establishing a highly robust baseline for direct solid synthesis devoid of program synthesis constraints.

**Title & Year:** BrepGen: A B-rep Generative Diffusion Model with Structured Latent Geometry (2024)

**Source/Venue:** ACM SIGGRAPH

**Link:** https://arxiv.org/abs/2401.15563 

**Core Contribution:** BrepGen maps the B-rep model into a highly structured, hierarchical top-down tree of latent geometry nodes, applying a state-of-the-art Transformer-based diffusion model to progressively denoise node features while recovering topological graphs through the algorithmic detection and merging of duplicated boundary nodes.

**Relevance Note:** Representing a major leap beyond autoregressive next-token prediction, BrepGen introduces continuous diffusion modeling directly to B-Rep graph topologies. The architecture inherently supports the generation of free-form and doubly-curved surfaces, far surpassing the simplistic planar, cylindrical, or prismatic primitives that strictly constrain sequence-based sketch-and-extrude histories. The framework outputs direct, editable B-rep structures by encoding global boundary boxes and localized shape parameters directly into the nodes. Topology is implicitly reconstructed by matching complex boundary conditions across the tree. Specifically, because an edge shared by two faces exists as two identical leaf nodes within the generated hierarchical tree, a post-diffusion topological merging algorithm fuses these nodes to recover the true non-manifold B-Rep graph. BrepGen is highly versatile, tackling point cloud reconstruction, partial CAD autocompletion, latent design interpolation, and unconditional generation tasks directly.

**Title & Year:** BRep-GD: a Graph Diffusion Model for CAD Boundary Representation Generation (2024)

**Source/Venue:** Pre-print repository / Relevant CAD/Graphics Proceedings

**Link:** https://pubmed.ncbi.nlm.nih.gov/41870942/ 

**Core Contribution:** BRep-GD establishes a continuous topological graph diffusion model explicitly tailored for CAD data structures, generating faces and edges sequentially while implementing a continuous topology decoupling mechanism to successfully bypass the quadratic computational complexity inherent to global graph attention algorithms.

**Relevance Note:** Addressing the computational inefficiency of prior tree-hierarchy generators, BRep-GD treats B-reps intrinsically as interconnected graphs. The model directly generates the continuous graph data structure wherein nodes explicitly represent face elements and edges represent bounding and vertex elements. By decoupling the continuous topology generation from a massive, resource-heavy global attention calculation, it isolates localized geometric consistency checks. This algorithmic isolation allows for the direct generation of highly watertight, complex solid components, actively minimizing isolated or inconsistent geometric artifacts. The framework entirely avoids step-by-step operation histories, offering state-of-the-art performance in class-conditional direct B-Rep generation and demonstrating superior handling of highly complex solid modeling topologies.

**Title & Year:** DTGBrepGen: A Novel B-rep Generative Model through Decoupling Topology and Geometry (2025)

**Source/Venue:** IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)

**Link:** https://cvpr.thecvf.com/virtual/2025/poster/34428 

**Core Contribution:** DTGBrepGen forces a multi-stage, systematic disentanglement of CAD generation, deploying separate neural architectures to independently construct a mathematically valid topological adjacency structure prior to sequentially diffusing the corresponding continuous B-spline geometries onto that established framework.

**Relevance Note:** DTGBrepGen directly addresses a critical failure point in modern direct generation: models that attempt joint topology-geometry diffusion frequently produce structurally invalid, non-manifold solids. To guarantee watertightness, DTGBrepGen explicitly models discrete topology independently of spatial coordinates. It guarantees the generation of a perfectly valid boundary graph through a two-stage process (modeling edge-face adjacency, then edge-vertex adjacency). Following the generation of this rigid skeleton, a sequence of Transformer-based diffusion models progressively maps spatial coordinates and continuous parametric surfaces (specifically structured as B-splines) onto the pre-approved graph. This approach fundamentally avoids sequential construction logic, relying entirely on the native structural logic of mathematical B-reps, significantly raising the benchmark for the statistical validity rates of generated CAD solids.

**Title & Year:** BrepGiff: Lightweight Generation of Complex B-rep with 3D GAT Diffusion (2025)

**Source/Venue:** IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)

**Link:** https://cvpr.thecvf.com/virtual/2025/poster/35112 

**Core Contribution:** BrepGiff extracts complex geometric and topological features into a unified 3D centroid graph and executes a degree-guided Graph Attention Network (GAT) diffusion process to successfully denoise massively complex B-Reps with extreme computational efficiency.

**Relevance Note:** A persistent bottleneck in direct B-Rep generation is the exploding computational cost associated with generating industrial models possessing over 100 faces. BrepGiff solves this by projecting the entire boundary representation into a 3D graph where nodes explicitly correspond to face centroids, enriched heavily by sampling points across the UV parameter domains of the continuous surfaces. The model directly outputs massive B-reps by running a forward noise schedule on the graph and utilizing a sophisticated degree-guided Graph Attention Network to enforce strict topological adjacency constraints locally and globally during the reverse denoising phase. It demonstrates a purely native approach to synthesizing continuous geometry and discrete topology simultaneously, requiring a fraction of the GPU memory of previous approaches while entirely circumventing procedural macro sequences.

**Title & Year:** BrepDiff: Single-stage B-rep Diffusion Model (2025)

**Source/Venue:** ACM SIGGRAPH

**Link:** https://brepdiff.github.io/ 

**Core Contribution:** BrepDiff shifts away from cascaded, multi-stage topologies by introducing a highly streamlined, single-stage diffusion schedule that denoises flattened, masked UV grid tokens to generate accurate per-face continuous geometry, relying on an asynchronous denoising strategy to yield editable boundary representations.

**Relevance Note:** Positioned in direct philosophical contrast to the decoupled methodology of DTGBrepGen, BrepDiff argues for a holistic, single-stage generation paradigm. It represents B-rep faces as masked UV grids, discretizing the continuous parametric domains and flattening them into a linear sequence of tokens. The network inherently predicts the spatial boundary features simultaneously, utilizing an explicitly modified noise schedule that stabilizes the generation of plausible parametric geometry without explicitly predicting an intermediate discrete graph. While the model focuses intensely on generating high-fidelity local surfaces, it recovers the final valid solid B-rep geometry and topology through dedicated, sophisticated post-processing graph alignment algorithms. The framework avoids all CAD macros, offering highly intuitive direct solid editing, geometric completion, interpolations, and mesh-to-B-Rep reconstructions.

**Title & Year:** AutoBrep: Autoregressive B-Rep Generation with Unified Topology and Geometry (2025)

**Source/Venue:** OpenReview / Preprint Archives

**Link:** https://huggingface.co/papers (Indexed via Open Repository) 

**Core Contribution:** AutoBrep utilizes a single, highly scalable autoregressive Transformer to progressively co-generate B-rep continuous geometry and discrete topology by quantizing them into a unified token stream strictly ordered by a breadth-first traversal of the geometric face adjacency graph.

**Relevance Note:** Significantly expanding upon the autoregressive foundations laid by SolidGen, AutoBrep discards the complex, two-tier separate pointer network paradigm. Instead, it treats topological boundary relationships as discrete, explicit vocabulary tokens embedded alongside quantized geometric primitives within a single, unified latent sequence. By organizing the generation sequence not by operational history, but strictly by a spatial breadth-first traversal of the solid's actual structural graph, the transformer outputs the direct B-Rep data structure in a single deterministic pass. This architecture natively models the interconnected dependencies of CAD elements, ensuring high topological validity while inherently supporting geometric auto-completion based directly on partial face constraints rather than human modeling intent.

**Title & Year:** HoLa: B-Rep Generation using a Holistic Latent Representation (2025)

**Source/Venue:** ACM Transactions on Graphics (SIGGRAPH)

**Link:** https://arxiv.org/abs/2504.14257 

**Core Contribution:** HoLa successfully unifies the continuous geometrical features of highly differing polynomial orders (vertices, parametric curves, and surfaces) alongside their discrete topological adjacency networks into an ultra-compact, mathematically rigorous holistic latent space representation designed explicitly for seamless downstream generative modeling.

**Relevance Note:** HoLa serves as a capstone architectural argument against the decoupled topology/geometry framework trend. The research effectively proves that decoupling paradigms frequently force downstream synchronization errors—for instance, a generated independent bounding curve might not perfectly match the mathematically exact intersection curve of two adjacent generated surfaces. By enforcing a holistic, highly intertwined latent representation, HoLa guarantees that the decoded output strictly adheres to B-rep manifold topologies natively, yielding direct B-Rep generation free from sequential modeling constraints. The holistic embedding ensures that geometry perfectly respects its topological boundary definitions at the latent level, dramatically reducing the requirement for heuristic post-processing stitching.

**Title & Year:** HiDiGen: Hierarchical Diffusion for B-Rep Generation with Explicit Topological Constraints (2026)

**Source/Venue:** arXiv (Computer Vision and Pattern Recognition)

**Link:** https://arxiv.org/abs/2604.02847 

**Core Contribution:** HiDiGen architects an advanced, progressive hierarchical diffusion framework that strictly embeds explicit topological validity constraints across multiple stage-wise generation steps, allowing for highly diverse, organic B-Rep shapes to be hallucinated without violating rigid CAD graph boundary parameters.

**Relevance Note:** This 2026 framework directly addresses the fundamental structural weakness of applying generative artificial intelligence to solid modeling: generating novel, organic shapes frequently shatters the rigid mathematical topology necessary for downstream manufacturing and physical simulation. HiDiGen outputs accurate B-reps directly by applying a hierarchical structure to the diffusion forward and reverse processes. This structured framework acts as an impenetrable mathematical regularization layer that forces the aggressively denoised continuous geometry to perpetually align with explicit topological bounding limitations. It requires no program synthesis, directly transforming random noise vectors into watertight, manufacturable solid representations.