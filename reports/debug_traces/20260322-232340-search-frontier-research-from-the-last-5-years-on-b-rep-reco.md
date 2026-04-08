# Paper Search Debug Trace

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-22T23:23:40
**Stop Reason:** Text 'TERMINATE' mentioned

## Run Summary

- Stop reason: `Text 'TERMINATE' mentioned`
- Total messages: `12`
- Planner JSON messages: `2`
- Retrieval JSON messages: `0`
- Review decisions seen: `2`
- Tool activity events: `4`

## Planner Outputs

### Planner Output 2

- Topic: `B-rep reconstruction from point clouds (3 queries)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research papers (2020-2025) that convert raw point clouds into structured Boundary Representations (B-rep) or CAD models, specifically focusing on parametric surface fitting, topology recovery, and geometry constraints.",
  "time_range": {
    "start_year": 2020,
    "end_year": 2025,
    "is_explicit": false
  },
  "focus_areas": [
    "point-cloud-to-CAD",
    "parametric surface reconstruction",
    "B-rep topology recovery",
    "geometry-constrained modeling",
    "reverse engineering"
  ],
  "exclude_areas": [
    "mesh-only reconstruction (e.g., Poisson, Delaunay)",
    "non-parametric implicit representations without B-rep extraction",
    "general point cloud processing (e.g., classification, segmentation without reconstruction)"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction deep learning CAD",
      "reason": "Captures the primary pipeline of converting unstructured points to structured Boundary Representations using modern learning-based methods.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    },
    {
      "query": "parametric surface reconstruction topology recovery point clouds",
      "reason": "Targets the specific geometric challenge of fitting parametric surfaces (NURBS, primitives) and recovering the correct topological graph structure.",
      "sources": [
        "Crossref",
        "arXiv"
      ]
    },
    {
      "query": "geometry constrained modeling reverse engineering CAD point cloud",
      "reason": "Focuses on traditional or hybrid optimization methods that enforce geometric constraints during the reconstruction process.",
      "sources": [
        "Crossref"
      ]
    }
  ],
  "assumptions": [
    "User defines 'frontier' as high-quality research from the last 5 years (2020-2025).",
    "B-rep implies topological connectivity (faces, edges, vertices) is recovered, not just surface geometry.",
    "Sources include both Computer Vision (CVPR, ECCV) and Computer Graphics (SIGGRAPH, Eurographics) venues."
  ],
  "success_criteria": [
    "Retrieve 5-10 papers explicitly dealing with B-rep or CAD output.",
    "Exclude papers where the final output is solely a mesh or point cloud.",
    "Identify papers discussing the recovery of topology (wireframes/curves) alongside surfaces."
  ]
}
```

### Planner Output 7

- Topic: `B-rep reconstruction from point clouds (3 queries)`

```json
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Revise the retrieval to cover missing traditional/optimization methods (geometry-constrained, NURBS fitting) and verify the relevance of previous hits by retrieving their abstracts, ensuring a balanced mix of deep learning and classical CAD reconstruction techniques.",
  "time_range": {
    "start_year": 2020,
    "end_year": 2025,
    "is_explicit": false
  },
  "focus_areas": [
    "geometry-constrained modeling",
    "NURBS and parametric surface fitting",
    "Constructive Solid Geometry (CSG) reconstruction",
    "B-rep topology graph extraction",
    "primitive fitting"
  ],
  "exclude_areas": [
    "mesh-only reconstruction",
    "implicit reconstruction without B-rep extraction"
  ],
  "queries": [
    {
      "query": "NURBS surface fitting point clouds reverse engineering constraints",
      "reason": "Addresses the 'geometry-constrained modeling' and parametric surface gap by targeting traditional optimization-based fitting methods often published in CAD journals.",
      "sources": [
        "Crossref",
        "arXiv"
      ]
    },
    {
      "query": "constructive solid geometry CSG reconstruction point clouds primitives",
      "reason": "Captures the CSG and primitive-based reconstruction subfield, which generates B-reps via geometric primitives and is distinct from mesh-based methods.",
      "sources": [
        "Crossref",
        "arXiv"
      ]
    },
    {
      "query": "B-Rep topology graph recovery point clouds deep learning",
      "reason": "Refines the deep learning search to focus specifically on topological graph extraction (wires, edges, faces) rather than generic surface reconstruction, ensuring B-rep output.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    }
  ],
  "assumptions": [
    "The previous HTTP 429 error was transient; re-issuing optimized queries will succeed.",
    "Searching for specific methodologies (NURBS, CSG) will yield papers with accessible abstracts."
  ],
  "success_criteria": [
    "Retrieve at least 2 papers focusing on traditional optimization or constraint-based fitting.",
    "Retrieve abstracts for previously identified ambiguous hits (e.g., Coiffier et al. 2021).",
    "Ensure representation of CSG/Primitive-based reconstruction methods."
  ]
}
```

## Retrieval Outputs

_No retrieval JSON outputs found._

## Review Decisions

### Review 6

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval successfully identified high-impact deep learning papers like ComplexGen, PBWR, and PaCo, which strongly align with the B-rep reconstruction topic. However, the retrieval failed to execute the 'geometry constrained modeling' query due to API rate limiting, creating a significant gap in traditional optimization-based reverse engineering methods. Furthermore, several promising candidates (e.g., Coiffier et al. 2021) lack abstracts in the retrieved results, making it impossible to verify if they produce true B-reps or just surfaces. The set is currently biased towards neural implicit/polygonal methods and needs to be balanced with explicit parametric/constraint-based approaches.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Both arXiv and Crossref were searched."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "At least 5 distinct candidates were identified (ComplexGen, PBWR, PaCo, Topology-Aware, Parametric Fitting)."
    },
    "relevance": {
      "passed": true,
      "reason": "Top candidates (ComplexGen, PBWR) are highly relevant to B-rep and wireframe reconstruction."
    },
    "metadata": {
      "passed": false,
      "reason": "Several candidates (e.g., Huang et al. 2024, Coiffier et al. 2021) are missing abstracts, hindering verification of B-rep output."
    },
    "query_fit": {
      "passed": false,
      "reason": "The explicit user constraint for 'geometry-constrained modeling' was not successfully executed due to a 429 error, missing a key methodological category."
    },
    "gaps": {
      "passed": false,
      "reason": "Missing traditional/non-learning optimization methods for parametric fitting (e.g., RANSAC-based primitive fitting with constraints) often found in CAD journals."
    }
  },
  "key_risks": [
    "Methodology bias: Results skew heavily toward Deep Learning/Neural methods, ignoring classical geometric optimization.",
    "Ambiguous output: 'Topology-Aware Surface Reconstruction' and 'Polygonal Surface Reconstruction' may not strictly produce CAD B-reps (NURBS/Primitives).",
    "Missing abstracts prevent accurate filtering of mesh-only vs. B-rep methods in the Crossref set."
  ],
  "next_actions": [
    "Retry the failed query for 'geometry constrained modeling reverse engineering CAD' using a different source (e.g., Semantic Scholar or direct search of 'Computer-Aided Design' journal) to capture non-DL methods.",
    "Expand search terms to include 'primitive fitting', 'constructive solid geometry (CSG) reconstruction', and 'CAD segmentation' to find parametric approaches.",
    "Filter for papers explicitly mentioning 'NURBS', 'solids', or 'topology graph' in titles/abstracts to ensure B-rep fidelity.",
    "Locate and retrieve abstracts for the Crossref candidates (Coiffier 2021, Huang 2024) to confirm they are not mesh-only."
  ]
}
```

### Review 11

- Source: `ReviewerAgent`
- Decision: `REVISE`

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval successfully identified several high-impact papers (ComplexGen, D^2CSG, UCSG-Net, Point2Brep) that strongly align with the B-rep and CSG reconstruction topics. However, critical papers matching the 'parametric surface' and 'topology recovery' constraints—specifically Coiffier et al. (2021) on Parametric Surface Fitting and Huang et al. (2024) on Parametric-Building-Wireframe Reconstruction—failed to return abstracts, providing only HTML/redirect scripts. This lack of evidence quality for key parametric methods, combined with the questionable 2026 date for Point2Brep, renders the current output insufficient for a high-quality report.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 1,
    "diversity_score": 2,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Both arXiv and Crossref (including IEEE, Elsevier, Springer) were used."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "Identified >5 distinct candidates including ComplexGen, D^2CSG, UCSG-Net, Coiffier, and Huang."
    },
    "relevance": {
      "passed": true,
      "reason": "Top candidates (D^2CSG, UCSG-Net, Point2Brep) are directly relevant to B-rep/CSG reconstruction."
    },
    "metadata": {
      "passed": false,
      "reason": "Several high-relevance papers (Coiffier 2021, Huang 2024, Gao 2023) are missing abstracts due to fetching errors."
    },
    "query_fit": {
      "passed": true,
      "reason": "The mix of papers covers Deep Learning (ComplexGen), CSG (D^2CSG), and Parametric/Building topics (Coiffier, Huang)."
    },
    "gaps": {
      "passed": false,
      "reason": "While titles suggest coverage of parametric surface fitting, the missing abstracts for Coiffier and Huang create a verification gap in this sub-area."
    }
  },
  "key_risks": [
    "Missing Abstracts: Critical papers on parametric fitting and wireframes are unusable for content generation.",
    "Future Date: Point2Brep is dated 2026, which may be an error or 'in-press', requiring verification.",
    "Verification Gap: Cannot confirm if 'Topology-Aware' or 'Hybrid Approach' papers produce B-reps vs. meshes without text."
  ],
  "next_actions": [
    "Retry fetching abstracts for Coiffier (DOI: 10.1016/j.cad.2021.103090) and Huang/PBWR (DOI: 10.1109/cvpr52733.2024.02624) using text-mode extraction.",
    "Verify the publication date and status of Point2Brep (SSRN: 10.2139/ssrn.6172545).",
    "Attempt to retrieve abstract for 'A Hybrid Approach for Segmenting and Fitting Solid Primitives' (DOI: 10.5220/0008870600380048) to confirm B-rep output.",
    "Filter out 'Sequential Point Clouds: A Survey' and 'ShapeAdv' if they appear in the final set."
  ]
}
```

## Tool Activity

### Tool Event 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 3 tool call(s): search_all_sources, search_all_sources, search_all_sources

```text
FunctionCall(id='call_e1eb596cd1af49abbab0dba8', arguments='{"query":"point cloud to B-rep reconstruction deep learning CAD","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
FunctionCall(id='call_e2fb58414c944b69b0c06d2b', arguments='{"query":"parametric surface reconstruction topology recovery point clouds","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
FunctionCall(id='call_6f6ca4e2c1c04c7183f69439', arguments='{"query":"geometry constrained modeling reverse engineering CAD point cloud","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
```

### Tool Event 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 3 tool call(s): search_all_sources, search_all_sources, search_all_sources

```text
content='Combined search results\n\nQuery: point cloud to B-rep reconstruction deep learning CAD\n\narXiv results for query: point cloud to B-rep reconstruction deep learning CAD\n\n[1]\nTitle: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-16T19:12:19Z\nURL: http://arxiv.org/abs/physics/0104048v1\nSummary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth\'s climate seems to be remarkably sensitive to solar activity, but variations of the Sun\'s electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.\n\n[2]\nTitle: CLOUD: an atmospheric research facility at CERN\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-24T07:30:14Z\nURL: http://arxiv.org/abs/physics/0104076v1\nSummary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.\n\n[3]\nTitle: Addendum to the CLOUD proposal\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-23T13:58:48Z\nURL: http://arxiv.org/abs/physics/0104068v1\nSummary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.\n\n[4]\nTitle: Learn to Accumulate Evidence from All Training Samples: Theory and Practice\nSource: arXiv\nAuthors: Deep Pandey, Qi Yu\nPublished: 2023-06-19T18:27:12Z\nURL: http://arxiv.org/abs/2306.11113v2\nSummary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.\n\n[5]\nTitle: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation\nSource: arXiv\nAuthors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong\nPublished: 2022-05-29T05:30:33Z\nURL: http://arxiv.org/abs/2205.14573v1\nSummary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.\n\n[6]\nTitle: The Modern Mathematics of Deep Learning\nSource: arXiv\nAuthors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen\nPublished: 2021-05-09T21:30:42Z\nURL: http://arxiv.org/abs/2105.04026v2\nSummary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.\n\n[7]\nTitle: Physics-informed self-supervised deep learning reconstruction for accelerated first-pass perfusion cardiac MRI\nSource: arXiv\nAuthors: Elena Martín-González, Ebraham Alskaf, Amedeo Chiribiri, Pablo Casaseca-de-la-Higuera, Carlos Alberola-López\nPublished: 2023-01-05T12:11:17Z\nURL: http://arxiv.org/abs/2301.02033v1\nSummary: First-pass perfusion cardiac magnetic resonance (FPP-CMR) is becoming an essential non-invasive imaging method for detecting deficits of myocardial blood flow, allowing the assessment of coronary heart disease. Nevertheless, acquisitions suffer from relatively low spatial resolution and limited heart coverage. Compressed sensing (CS) methods have been proposed to accelerate FPP-CMR and achieve higher spatial resolution. However, the long reconstruction times have limited the widespread clinical use of CS in FPP-CMR. Deep learning techniques based on supervised learning have emerged as alternatives for speeding up reconstructions. However, these approaches require fully sampled data for training, which is not possible to obtain, particularly high-resolution FPP-CMR images. Here, we propose a physics-informed self-supervised deep learning FPP-CMR reconstruction approach for accelerating FPP-CMR scans and hence facilitate high spatial resolution imaging. The proposed method provides high-quality FPP-CMR images from 10x undersampled data without using fully sampled reference data.\n\n[8]\nTitle: Deep Learning for 3D Point Clouds: A Survey\nSource: arXiv\nAuthors: Yulan Guo, Hanyun Wang, Qingyong Hu, Hao Liu, Li Liu\nPublished: 2019-12-27T09:15:54Z\nURL: http://arxiv.org/abs/1912.12033v2\nSummary: Point cloud learning has lately attracted increasing attention due to its wide applications in many areas, such as computer vision, autonomous driving, and robotics. As a dominating technique in AI, deep learning has been successfully used to solve various 2D vision problems. However, deep learning on point clouds is still in its infancy due to the unique challenges faced by the processing of point clouds with deep neural networks. Recently, deep learning on point clouds has become even thriving, with numerous methods being proposed to address different problems in this area. To stimulate future research, this paper presents a comprehensive review of recent progress in deep learning methods for point clouds. It covers three major tasks, including 3D shape classification, 3D object detection and tracking, and 3D point cloud segmentation. It also presents comparative results on several publicly available datasets, together with insightful observations and inspiring future research directions.\n\n[9]\nTitle: Deep MRI Reconstruction: Unrolled Optimization Algorithms Meet Neural Networks\nSource: arXiv\nAuthors: Dong Liang, Jing Cheng, Ziwen Ke, Leslie Ying\nPublished: 2019-07-26T08:22:53Z\nURL: http://arxiv.org/abs/1907.11711v1\nSummary: Image reconstruction from undersampled k-space data has been playing an important role for fast MRI. Recently, deep learning has demonstrated tremendous success in various fields and also shown potential to significantly speed up MR reconstruction with reduced measurements. This article gives an overview of deep learning-based image reconstruction methods for MRI. Three types of deep learning-based approaches are reviewed, the data-driven, model-driven and integrated approaches. The main structure of each network in three approaches is explained and the analysis of common parts of reviewed networks and differences in-between are highlighted. Based on the review, a number of signal processing issues are discussed for maximizing the potential of deep reconstruction for fast MRI. the discussion may facilitate further development of "optimal" network and performance analysis from a theoretical point of view.\n\n[10]\nTitle: Deep Learning and Computational Physics (Lecture Notes)\nSource: arXiv\nAuthors: Deep Ray, Orazio Pinti, Assad A. Oberai\nPublished: 2023-01-03T03:56:19Z\nURL: http://arxiv.org/abs/2301.00942v1\nSummary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.\n\nCrossref results for query: point cloud to B-rep reconstruction deep learning CAD\n\n[1]\nTitle: Deep Learning-Based Point Cloud Reconstruction Method for CAD Models\nSource: Crossref / 2025 10th International Conference on Intelligent Computing and Signal Processing (ICSP)\nAuthors: Hongliang Zhang, Deyuan Wang, Pengpei Gao, Chunhe Song\nPublished: 2025-5-16\nURL: https://doi.org/10.1109/icsp65755.2025.11087181\nDOI: 10.1109/icsp65755.2025.11087181\nSummary: No abstract/summary available.\n\n[2]\nTitle: Point Cloud Upsampling and Normal Estimation using Deep Learning for Robust Surface Reconstruction\nSource: Crossref / Proceedings of the 16th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications\nAuthors: Rajat Sharma, Tobias Schwandt, Christian Kunert, Steffen Urban, Wolfgang Broll\nPublished: 2021\nURL: https://doi.org/10.5220/0010211600700079\nDOI: 10.5220/0010211600700079\nSummary: No abstract/summary available.\n\n[3]\nTitle: Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models\nSource: Crossref / Electronics\nAuthors: Seyyedbehrad Emadi, Marco Limongiello\nPublished: 2025-1-20\nURL: https://doi.org/10.3390/electronics14020399\nDOI: 10.3390/electronics14020399\nSummary: <jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models to assess and mitigate noise in the point clouds. This study evaluates four clustering methods—k-means, agglomerative clustering, Spectral clustering, and Gaussian mixture model—based on photogrammetric parameters, reprojection error, projection accuracy, angles of intersection, distance, and the number of cameras used in tie point calculations. The approach is validated using point cloud data from the Temple of Neptune in Paestum, Italy. The results show that the proposed method significantly improves 3D reconstruction quality, with k-means outperforming other clustering techniques based on three evaluation metrics. This method offers superior versatility and performance compared to traditional and machine learning techniques, demonstrating its potential to enhance UAV-based surveying and inspection practices.</jats:p>\n\n[4]\nTitle: Deep Learning-Based Point Cloud Analysis\nSource: Crossref / 3D Point Cloud Analysis\nAuthors: Shan Liu, Min Zhang, Pranav Kadam, C.-C. Jay Kuo\nPublished: 2021\nURL: https://doi.org/10.1007/978-3-030-89180-0_3\nDOI: 10.1007/978-3-030-89180-0_3\nSummary: No abstract/summary available.\n\n[5]\nTitle: Deep-Learning-Based Point Cloud Analysis I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_5\nDOI: 10.1007/978-981-97-9570-3_5\nSummary: No abstract/summary available.\n\n[6]\nTitle: Deep-Learning-Based Point Cloud Analysis II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_6\nDOI: 10.1007/978-981-97-9570-3_6\nSummary: No abstract/summary available.\n\n[7]\nTitle: Segmentation and Local Reconstruction of Turbine Blade Point Cloud\nSource: Crossref / CAD\'20\nAuthors: Wei Wang, ZhenYu Guo, JiaMing Yang, Pai Zheng\nPublished: 2020-5-25\nURL: https://doi.org/10.14733/cadconfp.2020.193-198\nDOI: 10.14733/cadconfp.2020.193-198\nSummary: No abstract/summary available.\n\n[8]\nTitle: Deep-Learning-based Point Cloud Enhancement I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_3\nDOI: 10.1007/978-981-97-9570-3_3\nSummary: No abstract/summary available.\n\n[9]\nTitle: Deep-Learning-Based Point Cloud Enhancement II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_4\nDOI: 10.1007/978-981-97-9570-3_4\nSummary: No abstract/summary available.\n\n[10]\nTitle: Point Cloud Dataset Creation for Machine Learning on CAD Models\nSource: Crossref / CAD\'20\nAuthors: Andrew Colligan, Trevor Robinson, Declan Nolan, Yang Hua\nPublished: 2020-5-25\nURL: https://doi.org/10.14733/cadconfp.2020.152-156\nDOI: 10.14733/cadconfp.2020.152-156\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_e1eb596cd1af49abbab0dba8' is_error=False
content='Combined search results\n\nQuery: parametric surface reconstruction topology recovery point clouds\n\narXiv results for query: parametric surface reconstruction topology recovery point clouds\n\n[1]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[2]\nTitle: Parametric Point Cloud Completion for Polygonal Surface Reconstruction\nSource: arXiv\nAuthors: Zhaiyu Chen, Yuqing Wang, Liangliang Nan, Xiao Xiang Zhu\nPublished: 2025-03-11T12:20:24Z\nURL: http://arxiv.org/abs/2503.08363v1\nSummary: Existing polygonal surface reconstruction methods heavily depend on input completeness and struggle with incomplete point clouds. We argue that while current point cloud completion techniques may recover missing points, they are not optimized for polygonal surface reconstruction, where the parametric representation of underlying surfaces remains overlooked. To address this gap, we introduce parametric completion, a novel paradigm for point cloud completion, which recovers parametric primitives instead of individual points to convey high-level geometric structures. Our presented approach, PaCo, enables high-quality polygonal surface reconstruction by leveraging plane proxies that encapsulate both plane parameters and inlier points, proving particularly effective in challenging scenarios with highly incomplete data. Comprehensive evaluations of our approach on the ABC dataset establish its effectiveness with superior performance and set a new standard for polygonal surface reconstruction from incomplete data. Project page: https://parametric-completion.github.io.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Topological spaces of persistence modules and their properties\nSource: arXiv\nAuthors: Peter Bubenik, Tane Vergili\nPublished: 2018-02-22T15:56:39Z\nURL: http://arxiv.org/abs/1802.08117v2\nSummary: Persistence modules are a central algebraic object arising in topological data analysis. The notion of interleaving provides a natural way to measure distances between persistence modules. We consider various classes of persistence modules, including many of those that have been previously studied, and describe the relationships between them. In the cases where these classes are sets, interleaving distance induces a topology. We undertake a systematic study the resulting topological spaces and their basic topological properties.\n\n[5]\nTitle: On Hawaiian Groups of Some Topological Spaces\nSource: arXiv\nAuthors: Ameneh Babaee, Behrooz Mashayekhy, Hanieh Mirebrahimi\nPublished: 2011-11-03T05:39:39Z\nURL: http://arxiv.org/abs/1111.0731v2\nSummary: The paper is devoted to study the structure of Hawaiian groups of some topological spaces. We present some behaviors of Hawaiian groups with respect to product spaces, weak join spaces, cone spaces, covering spaces and locally trivial bundles. In particular, we determine the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space, for all $1\\leq m\\leq n$.\n\n[6]\nTitle: A class of tight contact structures on Sigma_2 x I\nSource: arXiv\nAuthors: Tanya Cofer\nPublished: 2004-11-09T17:49:14Z\nURL: http://arxiv.org/abs/math/0411208v1\nSummary: We employ cut and paste contact topological techniques to classify some tight contact structures on the closed, oriented genus-2 surface times the interval. A boundary condition is specified so that the Euler class of the of the contact structure vanishes when evaluated on each boundary component. We prove that there exists a unique, non-product tight contact structure in this case.\n\n[7]\nTitle: Neural RGB-D Surface Reconstruction\nSource: arXiv\nAuthors: Dejan Azinović, Ricardo Martin-Brualla, Dan B Goldman, Matthias Nießner, Justus Thies\nPublished: 2021-04-09T18:00:01Z\nURL: http://arxiv.org/abs/2104.04532v3\nSummary: Obtaining high-quality 3D reconstructions of room-scale scenes is of paramount importance for upcoming applications in AR or VR. These range from mixed reality applications for teleconferencing, virtual measuring, virtual room planing, to robotic applications. While current volume-based view synthesis methods that use neural radiance fields (NeRFs) show promising results in reproducing the appearance of an object or scene, they do not reconstruct an actual surface. The volumetric representation of the surface based on densities leads to artifacts when a surface is extracted using Marching Cubes, since during optimization, densities are accumulated along the ray and are not used at a single sample point in isolation. Instead of this volumetric representation of the surface, we propose to represent the surface using an implicit function (truncated signed distance function). We show how to incorporate this representation in the NeRF framework, and extend it to use depth measurements from a commodity RGB-D sensor, such as a Kinect. In addition, we propose a pose and camera refinement technique which improves the overall reconstruction quality. In contrast to concurrent work on integrating depth priors in NeRF which concentrates on novel view synthesis, our approach is able to reconstruct high-quality, metrical 3D reconstructions.\n\n[8]\nTitle: The homotopy invariance of the string topology loop product and string bracket\nSource: arXiv\nAuthors: Ralph L. Cohen, John Klein, Dennis Sullivan\nPublished: 2005-09-28T17:06:23Z\nURL: http://arxiv.org/abs/math/0509667v2\nSummary: Let M be a closed, oriented, n -manifold, and LM its free loop space. Chas and Sullivan defined a commutative algebra structure in the homology of LM, and a Lie algebra structure in its equivariant homology. These structures are known as the string topology loop product and string bracket, respectively. In this paper we prove that these structures are homotopy invariants in the following sense. Let f : M_1 \\to M_2 be a homotopy equivalence of closed, oriented n -manifolds. Then the induced equivalence, Lf : LM_1 \\to LM_2 induces a ring isomorphism in homology, and an isomorphism of Lie algebras in equivariant homology. The analogous statement also holds true for any generalized homology theory h_* that supports an orientation of the M_i \'s.\n\n[9]\nTitle: On subgroups of minimal topological groups\nSource: arXiv\nAuthors: V. V. Uspenskij\nPublished: 2000-04-19T00:36:47Z\nURL: http://arxiv.org/abs/math/0004119v2\nSummary: A topological group is minimal if it does not admit a strictly coarser Hausdorff group topology. The Roelcke uniformity (or lower uniformity) on a topological group is the greatest lower bound of the left and right uniformities. A group is Roelcke-precompact if it is precompact with respect to the Roelcke uniformity. Many naturally arising non-Abelian topological groups are Roelcke-precompact and hence have a natural compactification. We use such compactifications to prove that some groups of isometries are minimal. In particular, if U_1 is the Urysohn universal metric space of diameter 1, the group Iso(U_1) of all self-isometries of U_1 is Roelcke-precompact, topologically simple and minimal. We also show that every topological group is a subgroup of a minimal topologically simple Roelcke-precompact group of the form Iso(M), where M is an appropriate non-separable version of the Urysohn space.\n\n[10]\nTitle: Extended Bloch group and the Cheeger-Chern-Simons class\nSource: arXiv\nAuthors: Walter D Neumann\nPublished: 2003-07-08T16:26:37Z\nURL: http://arxiv.org/abs/math/0307092v2\nSummary: We define an extended Bloch group and show it is naturally isomorphic to H_3(PSL(2,C)^δ;Z). Using the Rogers dilogarithm function this leads to an exact simplicial formula for the universal Cheeger-Chern-Simons class on this homology group. It also leads to an independent proof of the analytic relationship between volume and Chern-Simons invariant of hyperbolic 3-manifolds conjectured by Neumann and Zagier [Topology 1985] and proved by Yoshida [Invent. Math. 1985] as well as effective formulae for the Chern-Simons invariant of a hyperbolic 3-manifold.\n\nCrossref results for query: parametric surface reconstruction topology recovery point clouds\n\n[1]\nTitle: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\nSource: Crossref / Computer-Aided Design\nAuthors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov\nPublished: 2021-11\nURL: https://doi.org/10.1016/j.cad.2021.103090\nDOI: 10.1016/j.cad.2021.103090\nSummary: No abstract/summary available.\n\n[2]\nTitle: Deep Learning-Based Surface Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2024-12-6\nURL: https://doi.org/10.52843/cassyni.cj5jq2\nDOI: 10.52843/cassyni.cj5jq2\nSummary: No abstract/summary available.\n\n[3]\nTitle: Surface Reconstruction of Point Clouds with Noises\nSource: Crossref / Crossref\nAuthors: Zhengxuan Yi, Maohua Du, Yongjun Cao, Jianan Liang\nPublished: 2024\nURL: https://doi.org/10.2139/ssrn.5042514\nDOI: 10.2139/ssrn.5042514\nSummary: No abstract/summary available.\n\n[4]\nTitle: Topology‐Aware Surface Reconstruction for Point Clouds\nSource: Crossref / Computer Graphics Forum\nAuthors: Rickard Brüel‐Gabrielsson, Vignesh Ganapathi‐Subramanian, Primoz Skraba, Leonidas J. Guibas\nPublished: 2020-8\nURL: https://doi.org/10.1111/cgf.14079\nDOI: 10.1111/cgf.14079\nSummary: <jats:title>Abstract</jats:title><jats:p>We present an approach to incorporate topological priors in the reconstruction of a surface from a point scan. We base the reconstruction on basis functions which are optimized to provide a good fit to the point scan while satisfying predefined topological constraints. We optimize the parameters of a model to obtain a likelihood function over the reconstruction domain. The topological constraints are captured by persistence diagrams which are incorporated within the optimization algorithm to promote the correct topology. The result is a novel topology‐aware technique which can (i) weed out topological noise from point scans, and (ii) capture certain nuanced properties of the underlying shape which could otherwise be lost while performing surface reconstruction. We show results reconstructing shapes with multiple potential topologies, compare to other classical surface construction techniques, and show the completion of real scan data.</jats:p>\n\n[5]\nTitle: PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds\nSource: Crossref / 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)\nAuthors: Shangfeng Huang, Ruisheng Wang, Bo Guo, Hongxin Yang\nPublished: 2024-6-16\nURL: https://doi.org/10.1109/cvpr52733.2024.02624\nDOI: 10.1109/cvpr52733.2024.02624\nSummary: No abstract/summary available.\n\n[6]\nTitle: Monocular Non-Rigid Surface Reconstruction with Learned Deformation Model\nSource: Crossref / Robust Methods for Dense Monocular Non-Rigid 3D Reconstruction and Alignment of Point Clouds\nAuthors: Vladislav Golyanik\nPublished: 2020\nURL: https://doi.org/10.1007/978-3-658-30567-3_7\nDOI: 10.1007/978-3-658-30567-3_7\nSummary: No abstract/summary available.\n\n[7]\nTitle: NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: Ruikai Cui, Shi Qiu, Jiawei Liu, Saeed Anwar, Nick Barnes\nPublished: 2024-12-17\nURL: https://doi.org/10.32388/q45a8j\nDOI: 10.32388/q45a8j\nSummary: <jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this paper, we introduce NumGrad-Pull, leveraging the representation capability of tri-plane structures to accelerate the learning of signed distance functions and enhance the fidelity of local details in surface reconstruction. To further improve the training stability of grid-based tri-planes, we propose to exploit numerical gradients, replacing conventional analytical computations. Additionally, we present a progressive plane expansion strategy to facilitate faster signed distance function convergence and design a data sampling strategy to mitigate reconstruction artifacts. Our extensive experiments across a variety of benchmarks demonstrate the effectiveness and robustness of our approach. Code is available at https://github.com/CuiRuikai/NumGrad-Pull. </jats:p>\n\n[8]\nTitle: PointNeuron: 3D Neuron Reconstruction via Geometry and Topology Learning of Point Clouds\nSource: Crossref / 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)\nAuthors: Runkai Zhao, Heng Wang, Chaoyi Zhang, Weidong Cai\nPublished: 2023-1\nURL: https://doi.org/10.1109/wacv56688.2023.00574\nDOI: 10.1109/wacv56688.2023.00574\nSummary: No abstract/summary available.\n\n[9]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-3-31\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1\nDOI: 10.1109/tgrs.2025.3608325/v1/review1\nSummary: No abstract/summary available.\n\n[10]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-4-16\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2\nDOI: 10.1109/tgrs.2025.3608325/v1/review2\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_e2fb58414c944b69b0c06d2b' is_error=False
content="Error: Client error '429 Too Many Requests' for url 'https://api.crossref.org/works?query=geometry+constrained+modeling+reverse+engineering+CAD+point+cloud&rows=10&select=title%2Cauthor%2CDOI%2CURL%2Cpublished-print%2Cpublished-online%2Cissued%2Ccontainer-title%2Cabstract&filter=from-pub-date%3A2020-01-01'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429" name='search_all_sources' call_id='call_6f6ca4e2c1c04c7183f69439' is_error=True
```

### Tool Event 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 5 tool call(s): search_all_sources, search_all_sources, search_all_sources, fetch_webpage_excerpt, fetch_webpage_excerpt

```text
FunctionCall(id='call_d8f34cf2bed14d719dace290', arguments='{"from_year":"2020","max_results_per_source":"8","query":"NURBS surface fitting point clouds reverse engineering constraints"}', name='search_all_sources')
FunctionCall(id='call_f6f71dd8ffbd4442a1be086c', arguments='{"from_year":"2020","max_results_per_source":"8","query":"constructive solid geometry CSG reconstruction point clouds primitives"}', name='search_all_sources')
FunctionCall(id='call_5d59209b4efa4ccb84a34758', arguments='{"from_year":"2020","max_results_per_source":"8","query":"B-Rep topology graph recovery point clouds deep learning"}', name='search_all_sources')
FunctionCall(id='call_0a2a62c6754845f5b8dc37a3', arguments='{"url":"https://doi.org/10.1016/j.cad.2021.103090","max_chars":2000}', name='fetch_webpage_excerpt')
FunctionCall(id='call_3080290fa2014cebb412ee9b', arguments='{"url":"https://doi.org/10.1109/cvpr52733.2024.02624","max_chars":2000}', name='fetch_webpage_excerpt')
```

### Tool Event 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 5 tool call(s): search_all_sources, search_all_sources, search_all_sources, fetch_webpage_excerpt, fetch_webpage_excerpt

```text
content='Combined search results\n\nQuery: NURBS surface fitting point clouds reverse engineering constraints\n\narXiv results for query: NURBS surface fitting point clouds reverse engineering constraints\n\n[1]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[2]\nTitle: Reverse Engineering Point Clouds to Fit Tensor Product B-Spline Surfaces by Blending Local Fits\nSource: arXiv\nAuthors: Lavanya Sita Tekumalla, Elaine Cohen\nPublished: 2014-11-21T19:37:27Z\nURL: http://arxiv.org/abs/1411.5993v1\nSummary: Being able to reverse engineer from point cloud data to obtain 3D models is important in modeling. As our main contribution, we present a new method to obtain a tensor product B-spline representation from point cloud data by fitting surfaces to appropriately segmented data. By blending multiple local fits our method is more efficient than existing techniques, with the ability to deal with more detail by efficiently introducing a high number of knots. Further point cloud data obtained by digitizing 3D data, typically presents many associated complications like noise and missing data. As our second contribution, we propose an end-to-end framework for smoothing, hole filling, parameterization, knot selection and B-spline fitting that addresses these issues, works robustly with large irregularly shaped data containing holes and is straightforward to implement.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Empirical Studies on Adversarial Reverse Engineering with Students\nSource: arXiv\nAuthors: Tab, Zhang, Bjorn De Sutter, Christian Collberg, Bart Coppens\nPublished: 2026-03-04T09:27:46Z\nURL: http://arxiv.org/abs/2603.03875v1\nSummary: Empirical research in reverse engineering and software protection is crucial for evaluating the efficacy of methods designed to protect software against unauthorized access and tampering. However, conducting such studies with professional reverse engineers presents significant challenges, including access to professionals and affordability. This paper explores the use of students as participants in empirical reverse engineering experiments, examining their suitability and the necessary training; the design of appropriate challenges; strategies for ensuring the rigor and validity of the research and its results; ways to maintain students\' privacy, motivation, and voluntary participation; and data collection methods. We present a systematic literature review of existing reverse engineering experiments and user studies, a discussion of related work from the broader domain of software engineering that applies to reverse engineering experiments, an extensive discussion of our own experience running experiments ourselves in the context of a master-level software hacking and protection course, and recommendations based on this experience. Our findings aim to guide future empirical studies in RE, balancing practical constraints with the need for meaningful, reproducible results.\n\n[5]\nTitle: Non-Invasive Reverse Engineering of Finite State Machines Using Power Analysis and Boolean Satisfiability\nSource: arXiv\nAuthors: Harsh Vamja, Richa Agrawal, Ranga Vemuri\nPublished: 2019-08-06T06:47:37Z\nURL: http://arxiv.org/abs/1908.01979v1\nSummary: In this paper, we present a non-invasive reverse engineering attack based on a novel approach that combines functional and power analysis to recover finite state machines from their synchronous sequential circuit implementations. The proposed technique formulates the machine exploration and state identification problem as a Boolean constraint satisfaction problem and solves it using a SMT (Satisfiability Modulo Theories) solver. It uses power measurements to achieve fast convergence. Experimental results using the LGSynth\'91 benchmark suite show that the satisfiability-based approach is several times faster compared to existing techniques and can successfully recover 90%-100% of the transitions of a target machine.\n\n[6]\nTitle: Algorithms for geometrical operations with NURBS surfaces\nSource: arXiv\nAuthors: Gernot Beer\nPublished: 2022-10-24T12:23:57Z\nURL: http://arxiv.org/abs/2210.13160v1\nSummary: The aim of the paper is to show algorithms for geometrical manipulations on NURBS surfaces. These include generating NURBS surfaces that pass through given points, calculating the minimum distance to a point and include line to surface and surface to surface intersections.\n\n[7]\nTitle: Morescient GAI for Software Engineering (Extended Version)\nSource: arXiv\nAuthors: Marcus Kessel, Colin Atkinson\nPublished: 2024-06-07T07:38:33Z\nURL: http://arxiv.org/abs/2406.04710v2\nSummary: The ability of Generative AI (GAI) technology to automatically check, synthesize and modify software engineering artifacts promises to revolutionize all aspects of software engineering. Using GAI for software engineering tasks is consequently one of the most rapidly expanding fields of software engineering research, with over a hundred LLM-based code models having been published since 2021. However, the overwhelming majority of existing code models share a major weakness - they are exclusively trained on the syntactic facet of software, significantly lowering their trustworthiness in tasks dependent on software semantics. To address this problem, a new class of "Morescient" GAI is needed that is "aware" of (i.e., trained on) both the semantic and static facets of software. This, in turn, will require a new generation of software observation platforms capable of generating large quantities of execution observations in a structured and readily analyzable way. In this paper, we present a vision and roadmap for how such "Morescient" GAI models can be engineered, evolved and disseminated according to the principles of open science.\n\n[8]\nTitle: Database Reverse Engineering based on Association Rule Mining\nSource: arXiv\nAuthors: Nattapon Pannurat, Nittaya Kerdprasop, Kittisak Kerdprasop\nPublished: 2010-04-19T18:18:43Z\nURL: http://arxiv.org/abs/1004.3272v1\nSummary: Maintaining a legacy database is a difficult task especially when system documentation is poor written or even missing. Database reverse engineering is an attempt to recover high-level conceptual design from the existing database instances. In this paper, we propose a technique to discover conceptual schema using the association mining technique. The discovered schema corresponds to the normalization at the third normal form, which is a common practice in many business organizations. Our algorithm also includes the rule filtering heuristic to solve the problem of exponential growth of discovered rules inherited with the association mining technique.\n\nCrossref results for query: NURBS surface fitting point clouds reverse engineering constraints\n\n[1]\nTitle: NURBS-Based Surface Reconstruction from Point Clouds for Electromagnetic Target Modeling\nSource: Crossref / 2025 Photonics &amp;amp; Electromagnetics Research Symposium - Fall (PIERS-Fall)\nAuthors: Qianyan Shen, Ruoming Zhang, Hai Lin\nPublished: 2025-11-4\nURL: https://doi.org/10.23919/piers-fall62445.2025.11394360\nDOI: 10.23919/piers-fall62445.2025.11394360\nSummary: No abstract/summary available.\n\n[2]\nTitle: NURBS surface fitting from scattered point cloud combining patch growing and PSO\nSource: Crossref / Third International Computing Imaging Conference (CITA 2023)\nAuthors: Shangbo Gao, Chen Ma, Qingxin Yang, Yue Shen, Deming Kong\nPublished: 2023-11-6\nURL: https://doi.org/10.1117/12.2691763\nDOI: 10.1117/12.2691763\nSummary: No abstract/summary available.\n\n[3]\nTitle: MST Based Ordering of Point Clouds and Curve Fitting\nSource: Crossref / Proceedings of the 21st International Conference on Computer Vision Theory and Applications\nAuthors: Christoph Dalitz, Alexander Jongbloed\nPublished: 2026\nURL: https://doi.org/10.5220/0014152000004084\nDOI: 10.5220/0014152000004084\nSummary: No abstract/summary available.\n\n[4]\nTitle: Reverse Engineering: Investigation of Optimization Techniques in Point Clouds Registration\nSource: Crossref / SSRN Electronic Journal\nAuthors: George Yacout\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5297053\nDOI: 10.2139/ssrn.5297053\nSummary: No abstract/summary available.\n\n[5]\nTitle: Adaptive Surface Fitting with Local Refinement: LR B-Spline Surfaces\nSource: Crossref / SpringerBriefs in Earth System Sciences\nAuthors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken\nPublished: 2023\nURL: https://doi.org/10.1007/978-3-031-16954-0_3\nDOI: 10.1007/978-3-031-16954-0_3\nSummary: <jats:title>Abstract</jats:title><jats:p>A locally refined (LR) B-spline surface is a piecewise polynomial surface for which the distribution of the surface coefficients can be locally adapted. Such a mathematical representation is interesting for fitting scattered and noisy data, as the local behaviour of a real point cloud may require more degrees of freedom only locally. The number of redundant surface coefficients is minimized, which avoids the fitting of the point cloud’s noise. The surface approximation is performed iteratively either by solving a least squares system or by a local approximation method. This procedure allows for mesh refinement in domains where the distance between a current surface and the point cloud exceeds a prescribed tolerance. In this way, parts of the LR B-spline surface obtained at previous steps may be kept unchanged. This chapter aims at explaining the adaptive fitting using local refinement with LR B-splines. We present two examples with simulated point clouds to illustrate the methodology.</jats:p>\n\n[6]\nTitle: Application of Poisson Surface Reconstruction with Envelope Constraints to TLS Point Clouds of Scenes with Complex Objects\nSource: Crossref / CAD\'25\nAuthors: Daiki Koyama, Hiroaki Date, Satoshi Kanai\nPublished: 2025-5-9\nURL: https://doi.org/10.14733/cadconfp.2025.205-210\nDOI: 10.14733/cadconfp.2025.205-210\nSummary: No abstract/summary available.\n\n[7]\nTitle: Optimal Surface Fitting of Point Clouds Using Local Refinement\nSource: Crossref / SpringerBriefs in Earth System Sciences\nAuthors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken\nPublished: 2023\nURL: https://doi.org/10.1007/978-3-031-16954-0\nDOI: 10.1007/978-3-031-16954-0\nSummary: No abstract/summary available.\n\n[8]\nTitle: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\nSource: Crossref / Computer-Aided Design\nAuthors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov\nPublished: 2021-11\nURL: https://doi.org/10.1016/j.cad.2021.103090\nDOI: 10.1016/j.cad.2021.103090\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_d8f34cf2bed14d719dace290' is_error=False
content='Combined search results\n\nQuery: constructive solid geometry CSG reconstruction point clouds primitives\n\narXiv results for query: constructive solid geometry CSG reconstruction point clouds primitives\n\n[1]\nTitle: Point containment algorithms for constructive solid geometry with unbounded primitives\nSource: arXiv\nAuthors: Paul K. Romano, Patrick A. Myers, Seth R. Johnson, Aljaž Kolšek, Patrick C. Shriwise\nPublished: 2024-06-18T19:50:37Z\nURL: http://arxiv.org/abs/2406.13030v1\nSummary: We present several algorithms for evaluating point containment in constructive solid geometry (CSG) trees with unbounded primitives. Three algorithms are presented based on postfix, prefix, and infix notations of the CSG binary expression tree. We show that prefix and infix notations enable short-circuiting logic, which reduces the number of primitives that must be checked during point containment. To evaluate the performance of the algorithms, each algorithm was implemented in the OpenMC Monte Carlo particle transport code, which relies on CSG to represent solid bodies through which subatomic particles travel. Two sets of tests were carried out. First, the execution time to generate a high-resolution rasterized image of a 2D slice of a detailed CSG model of the ITER tokamak was measured. Use of both prefix and infix notations offered significant speedup over the postfix notation that has traditionally been used in particle transport codes, with infix resulting in a 6$\\times$ reduction in execution time relative to postfix. We then measured the execution time of neutron transport simulations of the same ITER model using each of the algorithms. The results and performance improvements reveal the same trends as for the rasterization test, with a 4.59$\\times$ overall speedup using the infix notation relative to the original postfix notation in OpenMC.\n\n[2]\nTitle: The CCube reconstruction algorithm for the SoLid experiment\nSource: arXiv\nAuthors: The SoLid collaboration\nPublished: 2024-04-04T16:42:41Z\nURL: http://arxiv.org/abs/2404.03580v5\nSummary: The SoLid experiment is a very-short-baseline experiment aimed at searching for nuclear reactor-produced active to sterile antineutrino oscillations. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$LiF:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented (the basic detection unit is a 5 cm side cube). High segmentation provides numerous advantages, including the precise location of Inverse Beta Decay (IBD) products, the derivation of the considerate antineutrino energy estimator, and a powerful background reduction tool based on the topological signature of the signal. Finally, the system is read out by a network of wavelength-shifting fibres coupled to a photodetector (MPPC). This paper describes the design of the reconstruction algorithm that allows maximum use of the granularity of the detector. The goal of the algorithm is to convert the output of the optical-fibre readout to the list of the detection units from which it originated. This paper provides a performance comparison for three methods and concludes with a choice of the baseline approach for the experiment.\n\n[3]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[4]\nTitle: UCSG-Net -- Unsupervised Discovering of Constructive Solid Geometry Tree\nSource: arXiv\nAuthors: Kacper Kania, Maciej Zięba, Tomasz Kajdanowicz\nPublished: 2020-06-16T12:13:37Z\nURL: http://arxiv.org/abs/2006.09102v3\nSummary: Signed distance field (SDF) is a prominent implicit representation of 3D meshes. Methods that are based on such representation achieved state-of-the-art 3D shape reconstruction quality. However, these methods struggle to reconstruct non-convex shapes. One remedy is to incorporate a constructive solid geometry framework (CSG) that represents a shape as a decomposition into primitives. It allows to embody a 3D shape of high complexity and non-convexity with a simple tree representation of Boolean operations. Nevertheless, existing approaches are supervised and require the entire CSG parse tree that is given upfront during the training process. On the contrary, we propose a model that extracts a CSG parse tree without any supervision - UCSG-Net. Our model predicts parameters of primitives and binarizes their SDF representation through differentiable indicator function. It is achieved jointly with discovering the structure of a Boolean operators tree. The model selects dynamically which operator combination over primitives leads to the reconstruction of high fidelity. We evaluate our method on 2D and 3D autoencoding tasks. We show that the predicted parse tree representation is interpretable and can be used in CAD software.\n\n[5]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[6]\nTitle: Electromagnetic energy calibration of the SoLid detector with horizontal muons\nSource: arXiv\nAuthors: SoLid collaboration\nPublished: 2025-07-07T16:35:32Z\nURL: http://arxiv.org/abs/2507.05180v4\nSummary: SoLid is a neutrino experiment at very-short baseline searching for active-to-sterile oscillations of reactor antineutrinos. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$Li:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented; the basic detection unit is a 5 cm cube. High segmentation provides numerous advantages including precise localisation of the Inverse Beta Decay (IBD) products, the derivation of an antineutrino energy estimator based on the isolated positron energy, and a powerful background reduction tool that relies on the topological signature of the signal. Finally, the system is read out by a network of WLS fibres coupled to photosensors. A relative electromagnetic calibration is performed with horizontal cosmic muons. This source poses the simplest calibration problem in which a single detection unit is involved. In addition, large muon energy deposits allow us to perform a calibration at the most detailed level (i.e. per fibre) and to accurately define the fraction of energy escaping to neighbouring detection cells. A statistical precision at the sub-percent level is reached. The paper also discusses two methods to calibrate the absolute energy scale. The first method relies on horizontal muons, though the precision is limited to around 10\\% because of the uncertainty in the energy distribution of such muons. A novel, alternative method based on the radioactive AmBe source is proposed. It takes advantage of the electron-positron pair-production process and provides a calibration point at 3.4 MeV (i.e. in the core of the IBD positron spectrum). The paper is concluded with various cross-check including a determination of the energy spectrum of the standard cosmogenic background candle: $^{12}$B.\n\n[7]\nTitle: Constructive Projective Geometry\nSource: arXiv\nAuthors: Mark Mandelkern\nPublished: 2024-02-01T03:29:31Z\nURL: http://arxiv.org/abs/2402.00301v1\nSummary: Of the great theories of classical mathematics, projective geometry, with its powerful concepts of symmetry and duality, has been exceptional in continuing to intrigue investigators. The challenge put forth by Errett Bishop (1928-1983), "Every theorem proved with nonconstructive methods presents a challenge: to find a constructive version, and to give it a constructive proof", motivates a large portion of current constructive work. This challenge can be answered by discovering the hidden constructive content of classical projective geometry. Here we briefly outline, with few details, recent constructive work on the real projective plane, and projective extensions of affine planes. Special note is taken of a number of interesting open problems that remain; these show that constructive projective geometry is still a theory very much in need of further effort. The Bishop-type constructive mathematics discussed in the present paper proceeds from a viewpoint well-nigh opposite that of either formal logic or recursive function theory.\n\n[8]\nTitle: D$^2$CSG: Unsupervised Learning of Compact CSG Trees with Dual Complements and Dropouts\nSource: arXiv\nAuthors: Fenggen Yu, Qimin Chen, Maham Tanveer, Ali Mahdavi Amiri, Hao Zhang\nPublished: 2023-01-27T02:13:14Z\nURL: http://arxiv.org/abs/2301.11497v2\nSummary: We present D$^2$CSG, a neural model composed of two dual and complementary network branches, with dropouts, for unsupervised learning of compact constructive solid geometry (CSG) representations of 3D CAD shapes. Our network is trained to reconstruct a 3D shape by a fixed-order assembly of quadric primitives, with both branches producing a union of primitive intersections or inverses. A key difference between D$^2$CSG and all prior neural CSG models is its dedicated residual branch to assemble the potentially complex shape complement, which is subtracted from an overall shape modeled by the cover branch. With the shape complements, our network is provably general, while the weight dropout further improves compactness of the CSG tree by removing redundant primitives. We demonstrate both quantitatively and qualitatively that D$^2$CSG produces compact CSG reconstructions with superior quality and more natural primitives than all existing alternatives, especially over complex and high-genus CAD shapes.\n\nCrossref results for query: constructive solid geometry CSG reconstruction point clouds primitives\n\n[1]\nTitle: Constructive Solid Geometry (CSG)\nSource: Crossref / Encyclopedia of Ocean Engineering\nAuthors: Unknown authors\nPublished: 2022\nURL: https://doi.org/10.1007/978-981-10-6946-8_300122\nDOI: 10.1007/978-981-10-6946-8_300122\nSummary: No abstract/summary available.\n\n[2]\nTitle: A Hybrid Approach for Segmenting and Fitting Solid Primitives to 3D Point Clouds\nSource: Crossref / Proceedings of the 15th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications\nAuthors: Markus Friedrich, Steffen Illium, Pierre-Alain Fayolle, Claudia Linnhoff-Popien\nPublished: 2020\nURL: https://doi.org/10.5220/0008870600380048\nDOI: 10.5220/0008870600380048\nSummary: No abstract/summary available.\n\n[3]\nTitle: Exploring Constructive Solid Geometry for Building Reconstruction from Point Clouds: Preliminary Results\nSource: Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences\nAuthors: Muataz S. A. Albadri, Patricia González-Cabaleiro, Antonio Fernández, Lucía Díaz-Vilariño\nPublished: 2025-9-18\nURL: https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-1-2025\nDOI: 10.5194/isprs-archives-xlviii-4-w15-2025-1-2025\nSummary: <jats:p>Abstract. As-built BIM reconstruction supports building digitalization, enabling efficient management and maintenance of existing buildings. Manual reconstruction from point clouds is both error-prone and cost-intensive, while automatic reconstruction remains challenging despite recent advancements. This paper explores the use of Constructive Solid Geometry (CSG) for automatically reconstructing IFC-compatible models from indoor point clouds of existing buildings. The proposed approach starts with segmented point clouds corresponding to rooms, doors, and windows, then CSG operations are used to reconstruct key building components as solids, including slabs, walls, doors, windows, and interior spaces. These solids are subsequently converted into corresponding IFC entities. The method is evaluated using two case studies, achieving a centimetre-level accuracy and a runtime of approximately 9 seconds per case study. The proposed method provides a promising ability to advance the Scan-to-BIM pipeline, as it enables accurate reconstruction of building components while preserving topological relationships during an efficient runtime. </jats:p>\n\n[4]\nTitle: Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: yihang fu, jing li, Falai Chen\nPublished: 2026\nURL: https://doi.org/10.2139/ssrn.6172545\nDOI: 10.2139/ssrn.6172545\nSummary: <jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>\n\n[5]\nTitle: Integration of Constructive Solid Geometry and Boundary Representation (CSG-BRep) for 3D Modeling of Underground Cable Wells from Point Clouds\nSource: Crossref / Remote Sensing\nAuthors: Ming Huang, Xueyu Wu, Xianglei Liu, Tianhang Meng, Peiyuan Zhu\nPublished: 2020-5-4\nURL: https://doi.org/10.3390/rs12091452\nDOI: 10.3390/rs12091452\nSummary: <jats:p>The preference of three-dimensional representation of underground cable wells from two-dimensional symbols is a developing trend, and three-dimensional (3D) point cloud data is widely used due to its high precision. In this study, we utilize the characteristics of 3D terrestrial lidar point cloud data to build a CSG-BRep 3D model of underground cable wells, whose spatial topological relationship is fully considered. In order to simplify the modeling process, first, point cloud simplification is performed; then, the point cloud main axis is extracted by OBB bounding box, and lastly the point cloud orientation correction is realized by quaternion rotation. Furthermore, employing the adaptive method, the top point cloud is extracted, and it is projected for boundary extraction. Thereupon, utilizing the boundary information, we design the 3D cable well model. Finally, the cable well component model is generated by scanning the original point cloud. The experiments demonstrate that, along with the algorithm being fast, the proposed model is effective at displaying the 3D information of the actual cable wells and meets the current production demands.</jats:p>\n\n[6]\nTitle: A Modular Framework for Geometry-Aware Mesh Reconstruction from Sparse Point Clouds\nSource: Crossref / Crossref\nAuthors: Ying Chen, Hui Chen, Yuzhu Zhou, Lianyu Gao, Ying Hu\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5258954\nDOI: 10.2139/ssrn.5258954\nSummary: No abstract/summary available.\n\n[7]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-3-31\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1\nDOI: 10.1109/tgrs.2025.3608325/v1/review1\nSummary: No abstract/summary available.\n\n[8]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-4-16\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2\nDOI: 10.1109/tgrs.2025.3608325/v1/review2\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_f6f71dd8ffbd4442a1be086c' is_error=False
content='Combined search results\n\nQuery: B-Rep topology graph recovery point clouds deep learning\n\narXiv results for query: B-Rep topology graph recovery point clouds deep learning\n\n[1]\nTitle: Learn to Accumulate Evidence from All Training Samples: Theory and Practice\nSource: arXiv\nAuthors: Deep Pandey, Qi Yu\nPublished: 2023-06-19T18:27:12Z\nURL: http://arxiv.org/abs/2306.11113v2\nSummary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.\n\n[2]\nTitle: The Modern Mathematics of Deep Learning\nSource: arXiv\nAuthors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen\nPublished: 2021-05-09T21:30:42Z\nURL: http://arxiv.org/abs/2105.04026v2\nSummary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Deep Learning and Computational Physics (Lecture Notes)\nSource: arXiv\nAuthors: Deep Ray, Orazio Pinti, Assad A. Oberai\nPublished: 2023-01-03T03:56:19Z\nURL: http://arxiv.org/abs/2301.00942v1\nSummary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.\n\n[5]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[6]\nTitle: A multitask deep learning model for real-time deployment in embedded systems\nSource: arXiv\nAuthors: Miquel Martí, Atsuto Maki\nPublished: 2017-10-31T23:59:23Z\nURL: http://arxiv.org/abs/1711.00146v1\nSummary: We propose an approach to Multitask Learning (MTL) to make deep learning models faster and lighter for applications in which multiple tasks need to be solved simultaneously, which is particularly useful in embedded, real-time systems. We develop a multitask model for both Object Detection and Semantic Segmentation and analyze the challenges that appear during its training. Our multitask network is 1.6x faster, lighter and uses less memory than deploying the single-task models in parallel. We conclude that MTL has the potential to give superior performance in exchange of a more complex training process that introduces challenges not present in single-task models.\n\n[7]\nTitle: Deep learning observables in computational fluid dynamics\nSource: arXiv\nAuthors: Kjetil O. Lye, Siddhartha Mishra, Deep Ray\nPublished: 2019-03-07T16:57:52Z\nURL: http://arxiv.org/abs/1903.03040v2\nSummary: Many large scale problems in computational fluid dynamics such as uncertainty quantification, Bayesian inversion, data assimilation and PDE constrained optimization are considered very challenging computationally as they require a large number of expensive (forward) numerical solutions of the corresponding PDEs. We propose a machine learning algorithm, based on deep artificial neural networks, that predicts the underlying \\emph{input parameters to observable} map from a few training samples (computed realizations of this map). By a judicious combination of theoretical arguments and empirical observations, we find suitable network architectures and training hyperparameters that result in robust and efficient neural network approximations of the parameters to observable map. Numerical experiments are presented to demonstrate low prediction errors for the trained network networks, even when the network has been trained with a few samples, at a computational cost which is several orders of magnitude lower than the underlying PDE solver. Moreover, we combine the proposed deep learning algorithm with Monte Carlo (MC) and Quasi-Monte Carlo (QMC) methods to efficiently compute uncertainty propagation for nonlinear PDEs. Under the assumption that the underlying neural networks generalize well, we prove that the deep learning MC and QMC algorithms are guaranteed to be faster than the baseline (quasi-) Monte Carlo methods. Numerical experiments demonstrating one to two orders of magnitude speed up over baseline QMC and MC algorithms, for the intricate problem of computing probability distributions of the observable, are also presented.\n\n[8]\nTitle: DILIE: Deep Internal Learning for Image Enhancement\nSource: arXiv\nAuthors: Indra Deep Mastan, Shanmuganathan Raman\nPublished: 2020-12-11T16:39:44Z\nURL: http://arxiv.org/abs/2012.06469v1\nSummary: We consider the generic deep image enhancement problem where an input image is transformed into a perceptually better-looking image. Recent methods for image enhancement consider the problem by performing style transfer and image restoration. The methods mostly fall into two categories: training data-based and training data-independent (deep internal learning methods). We perform image enhancement in the deep internal learning framework. Our Deep Internal Learning for Image Enhancement framework enhances content features and style features and uses contextual content loss for preserving image context in the enhanced image. We show results on both hazy and noisy image enhancement. To validate the results, we use structure similarity and perceptual error, which is efficient in measuring the unrealistic deformation present in the images. We show that the proposed framework outperforms the relevant state-of-the-art works for image enhancement.\n\nCrossref results for query: B-Rep topology graph recovery point clouds deep learning\n\n[1]\nTitle: Deep Unsupervised Learning of 3D Point Clouds via Graph Topology Inference and Filtering\nSource: Crossref / IEEE Transactions on Image Processing\nAuthors: Siheng Chen, Chaojing Duan, Yaoqing Yang, Duanshun Li, Chen Feng\nPublished: 2020\nURL: https://doi.org/10.1109/tip.2019.2957935\nDOI: 10.1109/tip.2019.2957935\nSummary: No abstract/summary available.\n\n[2]\nTitle: Learning Basics for 3D Point Clouds\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_2\nDOI: 10.1007/978-981-97-9570-3_2\nSummary: No abstract/summary available.\n\n[3]\nTitle: Deep-Learning-Based Point Cloud Analysis I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_5\nDOI: 10.1007/978-981-97-9570-3_5\nSummary: No abstract/summary available.\n\n[4]\nTitle: Deep-Learning-Based Point Cloud Analysis II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_6\nDOI: 10.1007/978-981-97-9570-3_6\nSummary: No abstract/summary available.\n\n[5]\nTitle: Deep-Learning-Based Point Cloud Enhancement II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_4\nDOI: 10.1007/978-981-97-9570-3_4\nSummary: No abstract/summary available.\n\n[6]\nTitle: Deep-Learning-based Point Cloud Enhancement I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_3\nDOI: 10.1007/978-981-97-9570-3_3\nSummary: No abstract/summary available.\n\n[7]\nTitle: Open-Source Projects for 3D Point Clouds\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_9\nDOI: 10.1007/978-981-97-9570-3_9\nSummary: No abstract/summary available.\n\n[8]\nTitle: Deep Learning Architectures for 3D Point Clouds\nSource: Crossref / Proceedings of the 18th International Conference on Agents and Artificial Intelligence\nAuthors: Nour Neifar, Achraf Ben-Hamadou, Ahmed Rekik\nPublished: 2026\nURL: https://doi.org/10.5220/0014440900004052\nDOI: 10.5220/0014440900004052\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_5d59209b4efa4ccb84a34758' is_error=False
content='Fetched excerpt from https://doi.org/10.1016/j.cad.2021.103090:\nRedirecting var timerStart = Date.now(); var pageName = ""; if (pageName == "") { pageName = "Auto Article Locator"; } function autoRedirectToURL() { var url = \'/retrieve/\'+document.getElementById(\'resultName\').value+\'?Redirect=\'+document.getElementById(\'redirectURL\').value+\'&key=\'+document.getElementById(\'key\').value window.location = url; } siteCatalyst.pageDataLoad({ businessUnit : \'ELS:RP:ST\', environment : \'prod\', language : \'en\', loadTime : (Date.now() - timerStart).toString(), loadTimestamp : Date.now().toString(), name : pageName, productName : \'IH\', type : \'ih:article\', detail : \'sciencedirect\', format :"MIME-XHTML", accessType : \'ih:anon_guest\', ipAddress : \'67.209.191.166\', identifierType : \'PII\', identifierValue : \'S0010448521001019\', articleName : \'Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\', location : "Linking Hub" });' name='fetch_webpage_excerpt' call_id='call_0a2a62c6754845f5b8dc37a3' is_error=False
content='Fetched excerpt from https://doi.org/10.1109/cvpr52733.2024.02624:\n(function(){ window.FPCS=!!window.FPCS;try{(function(){(function iS(){var I=!1;function l(I){for(var l=0;I--;)l+=z(document.documentElement,null);return l}function z(I,l){var s="vi";l=l||new Z;return jS(I,function(I){I.setAttribute("data-"+s,l._1());return z(I,l)},null)}function Z(){this.z_=1;this._S=0;this.ZO=this.z_;this.oZ=null;this._1=function(){this.oZ=this._S+this.ZO;if(!isFinite(this.oZ))return this.reset(),this._1();this._S=this.ZO;this.ZO=this.oZ;this.oZ=null;return this.ZO};this.reset=function(){this.z_++;this._S=0;this.ZO=this.z_}}var s=!1; function SS(I,l){var z=document.createElement(I);l=l||document.body;l.appendChild(z);z&&z.style&&(z.style.display="none")}function _S(l,z){z=z||l;var Z="|";function SS(I){I=I.split(Z);var l=[];for(var z=0;z Si&&(_(455)?6E5:491710)>S-_i)return o_(!1);var I=o_(Ii&&!ji&&_i+oi Si&&(_(803)?6E5:648862)>I-_i?l=o_(!1):(l=o_(Ii&&!ji&&_i+oi S}(function JI(I){return I?0:JI(I)*JI(I)})(!0);})();}catch(x){}finally{ie9rgb4=void(0);};function ie9rgb4(a,b){return a>>b>>0}; })(); var home = { metadata:{ searchCount: \'7,180,385\', logoRelPath: \'/xploreAssets/images/customer_logos/\', thirdParthAuth: false, currentPage: \'document\', xploreVirtual:\'https://ieeexplore.ieee.org\', isWebAccount: false, isProvisioned: false, globalNotification:{}, cart: { count: 0 } } }; PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds | IEEE Conference Publication | IEEE Xplore var googletag = googletag || {}; googletag.cmd = googletag.cmd || []; (function() { var gads = document.createElement(\'script\'); gads.async = true; gads.type = \'text/javascript\'; var useSSL = \'https:\' == document.location.protocol; gads.src = (useSSL ? \'https:\' : \'http:\') + \'//securepubads.g.doubleclick.net/tag/js/gpt.js\'; var node = document.getElementsByTagName(\'script\')[0]; node.parentNode.insertBefore(gads, node); })(); document.write(\' \'); var body_rightsLink ="", body_publisher = ""; var recordId = ""; var AUTHOR_PROFILE = \'ON\'; if (AUTHOR_PROFILE.toU' name='fetch_webpage_excerpt' call_id='call_3080290fa2014cebb412ee9b' is_error=False
```

## Message Trace

### Message 1

- Source: `user`
- Type: `TextMessage`
- Summary: Search frontier research from the last 5 years on B-rep reconstruction from point clouds.

```text
Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
```

### Message 2

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research papers (2020-2025) that convert raw point clouds into structured Boundary Representations (B-rep) or CAD models, specifically focusing on parametric surface fitting, topology recovery, and geometry constraints.",
  "time_range": {
    "start_year": 2020,
    "end_year": 2025,
    "is_explicit": false
  },
  "focus_areas": [
    "point-cloud-to-CAD",
    "parametric surface reconstruction",
    "B-rep topology recovery",
    "geometry-constrained modeling",
    "reverse engineering"
  ],
  "exclude_areas": [
    "mesh-only reconstruction (e.g., Poisson, Delaunay)",
    "non-parametric implicit representations without B-rep extraction",
    "general point cloud processing (e.g., classification, segmentation without reconstruction)"
  ],
  "queries": [
    {
      "query": "point cloud to B-rep reconstruction deep learning CAD",
      "reason": "Captures the primary pipeline of converting unstructured points to structured Boundary Representations using modern learning-based methods.",
      "sources": ["arXiv", "Crossref"]
    },
    {
      "query": "parametric surface reconstruction topology recovery point clouds",
      "reason": "Targets the specific geometric challenge of fitting parametric surfaces (NURBS, primitives) and recovering the correct topological graph structure.",
      "sources": ["Crossref", "arXiv"]
    },
    {
      "query": "geometry constrained modeling reverse engineering CAD point cloud",
      "reason": "Focuses on traditional or hybrid optimization methods that enforce geometric constraints during the reconstruction process.",
      "sources": ["Crossref"]
    }
  ],
  "assumptions": [
    "User defines 'frontier' as high-quality research from the last 5 years (2020-2025).",
    "B-rep implies topological connectivity (faces, edges, vertices) is recovered, not just surface geometry.",
    "Sources include both Computer Vision (CVPR, ECCV) and Computer Graphics (SIGGRAPH, Eurographics) venues."
  ],
  "success_criteria": [
    "Retrieve 5-10 papers explicitly dealing with B-rep or CAD output.",
    "Exclude papers where the final output is solely a mesh or point cloud.",
    "Identify papers discussing the recovery of topology (wireframes/curves) alongside surfaces."
  ]
}
```

### Message 3

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 3 tool call(s): search_all_sources, search_all_sources, search_all_sources

```text
FunctionCall(id='call_e1eb596cd1af49abbab0dba8', arguments='{"query":"point cloud to B-rep reconstruction deep learning CAD","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
FunctionCall(id='call_e2fb58414c944b69b0c06d2b', arguments='{"query":"parametric surface reconstruction topology recovery point clouds","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
FunctionCall(id='call_6f6ca4e2c1c04c7183f69439', arguments='{"query":"geometry constrained modeling reverse engineering CAD point cloud","from_year":"2020","max_results_per_source":"10"}', name='search_all_sources')
```

### Message 4

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 3 tool call(s): search_all_sources, search_all_sources, search_all_sources

```text
content='Combined search results\n\nQuery: point cloud to B-rep reconstruction deep learning CAD\n\narXiv results for query: point cloud to B-rep reconstruction deep learning CAD\n\n[1]\nTitle: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-16T19:12:19Z\nURL: http://arxiv.org/abs/physics/0104048v1\nSummary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth\'s climate seems to be remarkably sensitive to solar activity, but variations of the Sun\'s electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.\n\n[2]\nTitle: CLOUD: an atmospheric research facility at CERN\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-24T07:30:14Z\nURL: http://arxiv.org/abs/physics/0104076v1\nSummary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.\n\n[3]\nTitle: Addendum to the CLOUD proposal\nSource: arXiv\nAuthors: The Cloud Collaboration\nPublished: 2001-04-23T13:58:48Z\nURL: http://arxiv.org/abs/physics/0104068v1\nSummary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.\n\n[4]\nTitle: Learn to Accumulate Evidence from All Training Samples: Theory and Practice\nSource: arXiv\nAuthors: Deep Pandey, Qi Yu\nPublished: 2023-06-19T18:27:12Z\nURL: http://arxiv.org/abs/2306.11113v2\nSummary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.\n\n[5]\nTitle: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation\nSource: arXiv\nAuthors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong\nPublished: 2022-05-29T05:30:33Z\nURL: http://arxiv.org/abs/2205.14573v1\nSummary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.\n\n[6]\nTitle: The Modern Mathematics of Deep Learning\nSource: arXiv\nAuthors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen\nPublished: 2021-05-09T21:30:42Z\nURL: http://arxiv.org/abs/2105.04026v2\nSummary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.\n\n[7]\nTitle: Physics-informed self-supervised deep learning reconstruction for accelerated first-pass perfusion cardiac MRI\nSource: arXiv\nAuthors: Elena Martín-González, Ebraham Alskaf, Amedeo Chiribiri, Pablo Casaseca-de-la-Higuera, Carlos Alberola-López\nPublished: 2023-01-05T12:11:17Z\nURL: http://arxiv.org/abs/2301.02033v1\nSummary: First-pass perfusion cardiac magnetic resonance (FPP-CMR) is becoming an essential non-invasive imaging method for detecting deficits of myocardial blood flow, allowing the assessment of coronary heart disease. Nevertheless, acquisitions suffer from relatively low spatial resolution and limited heart coverage. Compressed sensing (CS) methods have been proposed to accelerate FPP-CMR and achieve higher spatial resolution. However, the long reconstruction times have limited the widespread clinical use of CS in FPP-CMR. Deep learning techniques based on supervised learning have emerged as alternatives for speeding up reconstructions. However, these approaches require fully sampled data for training, which is not possible to obtain, particularly high-resolution FPP-CMR images. Here, we propose a physics-informed self-supervised deep learning FPP-CMR reconstruction approach for accelerating FPP-CMR scans and hence facilitate high spatial resolution imaging. The proposed method provides high-quality FPP-CMR images from 10x undersampled data without using fully sampled reference data.\n\n[8]\nTitle: Deep Learning for 3D Point Clouds: A Survey\nSource: arXiv\nAuthors: Yulan Guo, Hanyun Wang, Qingyong Hu, Hao Liu, Li Liu\nPublished: 2019-12-27T09:15:54Z\nURL: http://arxiv.org/abs/1912.12033v2\nSummary: Point cloud learning has lately attracted increasing attention due to its wide applications in many areas, such as computer vision, autonomous driving, and robotics. As a dominating technique in AI, deep learning has been successfully used to solve various 2D vision problems. However, deep learning on point clouds is still in its infancy due to the unique challenges faced by the processing of point clouds with deep neural networks. Recently, deep learning on point clouds has become even thriving, with numerous methods being proposed to address different problems in this area. To stimulate future research, this paper presents a comprehensive review of recent progress in deep learning methods for point clouds. It covers three major tasks, including 3D shape classification, 3D object detection and tracking, and 3D point cloud segmentation. It also presents comparative results on several publicly available datasets, together with insightful observations and inspiring future research directions.\n\n[9]\nTitle: Deep MRI Reconstruction: Unrolled Optimization Algorithms Meet Neural Networks\nSource: arXiv\nAuthors: Dong Liang, Jing Cheng, Ziwen Ke, Leslie Ying\nPublished: 2019-07-26T08:22:53Z\nURL: http://arxiv.org/abs/1907.11711v1\nSummary: Image reconstruction from undersampled k-space data has been playing an important role for fast MRI. Recently, deep learning has demonstrated tremendous success in various fields and also shown potential to significantly speed up MR reconstruction with reduced measurements. This article gives an overview of deep learning-based image reconstruction methods for MRI. Three types of deep learning-based approaches are reviewed, the data-driven, model-driven and integrated approaches. The main structure of each network in three approaches is explained and the analysis of common parts of reviewed networks and differences in-between are highlighted. Based on the review, a number of signal processing issues are discussed for maximizing the potential of deep reconstruction for fast MRI. the discussion may facilitate further development of "optimal" network and performance analysis from a theoretical point of view.\n\n[10]\nTitle: Deep Learning and Computational Physics (Lecture Notes)\nSource: arXiv\nAuthors: Deep Ray, Orazio Pinti, Assad A. Oberai\nPublished: 2023-01-03T03:56:19Z\nURL: http://arxiv.org/abs/2301.00942v1\nSummary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.\n\nCrossref results for query: point cloud to B-rep reconstruction deep learning CAD\n\n[1]\nTitle: Deep Learning-Based Point Cloud Reconstruction Method for CAD Models\nSource: Crossref / 2025 10th International Conference on Intelligent Computing and Signal Processing (ICSP)\nAuthors: Hongliang Zhang, Deyuan Wang, Pengpei Gao, Chunhe Song\nPublished: 2025-5-16\nURL: https://doi.org/10.1109/icsp65755.2025.11087181\nDOI: 10.1109/icsp65755.2025.11087181\nSummary: No abstract/summary available.\n\n[2]\nTitle: Point Cloud Upsampling and Normal Estimation using Deep Learning for Robust Surface Reconstruction\nSource: Crossref / Proceedings of the 16th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications\nAuthors: Rajat Sharma, Tobias Schwandt, Christian Kunert, Steffen Urban, Wolfgang Broll\nPublished: 2021\nURL: https://doi.org/10.5220/0010211600700079\nDOI: 10.5220/0010211600700079\nSummary: No abstract/summary available.\n\n[3]\nTitle: Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models\nSource: Crossref / Electronics\nAuthors: Seyyedbehrad Emadi, Marco Limongiello\nPublished: 2025-1-20\nURL: https://doi.org/10.3390/electronics14020399\nDOI: 10.3390/electronics14020399\nSummary: <jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models to assess and mitigate noise in the point clouds. This study evaluates four clustering methods—k-means, agglomerative clustering, Spectral clustering, and Gaussian mixture model—based on photogrammetric parameters, reprojection error, projection accuracy, angles of intersection, distance, and the number of cameras used in tie point calculations. The approach is validated using point cloud data from the Temple of Neptune in Paestum, Italy. The results show that the proposed method significantly improves 3D reconstruction quality, with k-means outperforming other clustering techniques based on three evaluation metrics. This method offers superior versatility and performance compared to traditional and machine learning techniques, demonstrating its potential to enhance UAV-based surveying and inspection practices.</jats:p>\n\n[4]\nTitle: Deep Learning-Based Point Cloud Analysis\nSource: Crossref / 3D Point Cloud Analysis\nAuthors: Shan Liu, Min Zhang, Pranav Kadam, C.-C. Jay Kuo\nPublished: 2021\nURL: https://doi.org/10.1007/978-3-030-89180-0_3\nDOI: 10.1007/978-3-030-89180-0_3\nSummary: No abstract/summary available.\n\n[5]\nTitle: Deep-Learning-Based Point Cloud Analysis I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_5\nDOI: 10.1007/978-981-97-9570-3_5\nSummary: No abstract/summary available.\n\n[6]\nTitle: Deep-Learning-Based Point Cloud Analysis II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_6\nDOI: 10.1007/978-981-97-9570-3_6\nSummary: No abstract/summary available.\n\n[7]\nTitle: Segmentation and Local Reconstruction of Turbine Blade Point Cloud\nSource: Crossref / CAD\'20\nAuthors: Wei Wang, ZhenYu Guo, JiaMing Yang, Pai Zheng\nPublished: 2020-5-25\nURL: https://doi.org/10.14733/cadconfp.2020.193-198\nDOI: 10.14733/cadconfp.2020.193-198\nSummary: No abstract/summary available.\n\n[8]\nTitle: Deep-Learning-based Point Cloud Enhancement I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_3\nDOI: 10.1007/978-981-97-9570-3_3\nSummary: No abstract/summary available.\n\n[9]\nTitle: Deep-Learning-Based Point Cloud Enhancement II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_4\nDOI: 10.1007/978-981-97-9570-3_4\nSummary: No abstract/summary available.\n\n[10]\nTitle: Point Cloud Dataset Creation for Machine Learning on CAD Models\nSource: Crossref / CAD\'20\nAuthors: Andrew Colligan, Trevor Robinson, Declan Nolan, Yang Hua\nPublished: 2020-5-25\nURL: https://doi.org/10.14733/cadconfp.2020.152-156\nDOI: 10.14733/cadconfp.2020.152-156\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_e1eb596cd1af49abbab0dba8' is_error=False
content='Combined search results\n\nQuery: parametric surface reconstruction topology recovery point clouds\n\narXiv results for query: parametric surface reconstruction topology recovery point clouds\n\n[1]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[2]\nTitle: Parametric Point Cloud Completion for Polygonal Surface Reconstruction\nSource: arXiv\nAuthors: Zhaiyu Chen, Yuqing Wang, Liangliang Nan, Xiao Xiang Zhu\nPublished: 2025-03-11T12:20:24Z\nURL: http://arxiv.org/abs/2503.08363v1\nSummary: Existing polygonal surface reconstruction methods heavily depend on input completeness and struggle with incomplete point clouds. We argue that while current point cloud completion techniques may recover missing points, they are not optimized for polygonal surface reconstruction, where the parametric representation of underlying surfaces remains overlooked. To address this gap, we introduce parametric completion, a novel paradigm for point cloud completion, which recovers parametric primitives instead of individual points to convey high-level geometric structures. Our presented approach, PaCo, enables high-quality polygonal surface reconstruction by leveraging plane proxies that encapsulate both plane parameters and inlier points, proving particularly effective in challenging scenarios with highly incomplete data. Comprehensive evaluations of our approach on the ABC dataset establish its effectiveness with superior performance and set a new standard for polygonal surface reconstruction from incomplete data. Project page: https://parametric-completion.github.io.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Topological spaces of persistence modules and their properties\nSource: arXiv\nAuthors: Peter Bubenik, Tane Vergili\nPublished: 2018-02-22T15:56:39Z\nURL: http://arxiv.org/abs/1802.08117v2\nSummary: Persistence modules are a central algebraic object arising in topological data analysis. The notion of interleaving provides a natural way to measure distances between persistence modules. We consider various classes of persistence modules, including many of those that have been previously studied, and describe the relationships between them. In the cases where these classes are sets, interleaving distance induces a topology. We undertake a systematic study the resulting topological spaces and their basic topological properties.\n\n[5]\nTitle: On Hawaiian Groups of Some Topological Spaces\nSource: arXiv\nAuthors: Ameneh Babaee, Behrooz Mashayekhy, Hanieh Mirebrahimi\nPublished: 2011-11-03T05:39:39Z\nURL: http://arxiv.org/abs/1111.0731v2\nSummary: The paper is devoted to study the structure of Hawaiian groups of some topological spaces. We present some behaviors of Hawaiian groups with respect to product spaces, weak join spaces, cone spaces, covering spaces and locally trivial bundles. In particular, we determine the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space, for all $1\\leq m\\leq n$.\n\n[6]\nTitle: A class of tight contact structures on Sigma_2 x I\nSource: arXiv\nAuthors: Tanya Cofer\nPublished: 2004-11-09T17:49:14Z\nURL: http://arxiv.org/abs/math/0411208v1\nSummary: We employ cut and paste contact topological techniques to classify some tight contact structures on the closed, oriented genus-2 surface times the interval. A boundary condition is specified so that the Euler class of the of the contact structure vanishes when evaluated on each boundary component. We prove that there exists a unique, non-product tight contact structure in this case.\n\n[7]\nTitle: Neural RGB-D Surface Reconstruction\nSource: arXiv\nAuthors: Dejan Azinović, Ricardo Martin-Brualla, Dan B Goldman, Matthias Nießner, Justus Thies\nPublished: 2021-04-09T18:00:01Z\nURL: http://arxiv.org/abs/2104.04532v3\nSummary: Obtaining high-quality 3D reconstructions of room-scale scenes is of paramount importance for upcoming applications in AR or VR. These range from mixed reality applications for teleconferencing, virtual measuring, virtual room planing, to robotic applications. While current volume-based view synthesis methods that use neural radiance fields (NeRFs) show promising results in reproducing the appearance of an object or scene, they do not reconstruct an actual surface. The volumetric representation of the surface based on densities leads to artifacts when a surface is extracted using Marching Cubes, since during optimization, densities are accumulated along the ray and are not used at a single sample point in isolation. Instead of this volumetric representation of the surface, we propose to represent the surface using an implicit function (truncated signed distance function). We show how to incorporate this representation in the NeRF framework, and extend it to use depth measurements from a commodity RGB-D sensor, such as a Kinect. In addition, we propose a pose and camera refinement technique which improves the overall reconstruction quality. In contrast to concurrent work on integrating depth priors in NeRF which concentrates on novel view synthesis, our approach is able to reconstruct high-quality, metrical 3D reconstructions.\n\n[8]\nTitle: The homotopy invariance of the string topology loop product and string bracket\nSource: arXiv\nAuthors: Ralph L. Cohen, John Klein, Dennis Sullivan\nPublished: 2005-09-28T17:06:23Z\nURL: http://arxiv.org/abs/math/0509667v2\nSummary: Let M be a closed, oriented, n -manifold, and LM its free loop space. Chas and Sullivan defined a commutative algebra structure in the homology of LM, and a Lie algebra structure in its equivariant homology. These structures are known as the string topology loop product and string bracket, respectively. In this paper we prove that these structures are homotopy invariants in the following sense. Let f : M_1 \\to M_2 be a homotopy equivalence of closed, oriented n -manifolds. Then the induced equivalence, Lf : LM_1 \\to LM_2 induces a ring isomorphism in homology, and an isomorphism of Lie algebras in equivariant homology. The analogous statement also holds true for any generalized homology theory h_* that supports an orientation of the M_i \'s.\n\n[9]\nTitle: On subgroups of minimal topological groups\nSource: arXiv\nAuthors: V. V. Uspenskij\nPublished: 2000-04-19T00:36:47Z\nURL: http://arxiv.org/abs/math/0004119v2\nSummary: A topological group is minimal if it does not admit a strictly coarser Hausdorff group topology. The Roelcke uniformity (or lower uniformity) on a topological group is the greatest lower bound of the left and right uniformities. A group is Roelcke-precompact if it is precompact with respect to the Roelcke uniformity. Many naturally arising non-Abelian topological groups are Roelcke-precompact and hence have a natural compactification. We use such compactifications to prove that some groups of isometries are minimal. In particular, if U_1 is the Urysohn universal metric space of diameter 1, the group Iso(U_1) of all self-isometries of U_1 is Roelcke-precompact, topologically simple and minimal. We also show that every topological group is a subgroup of a minimal topologically simple Roelcke-precompact group of the form Iso(M), where M is an appropriate non-separable version of the Urysohn space.\n\n[10]\nTitle: Extended Bloch group and the Cheeger-Chern-Simons class\nSource: arXiv\nAuthors: Walter D Neumann\nPublished: 2003-07-08T16:26:37Z\nURL: http://arxiv.org/abs/math/0307092v2\nSummary: We define an extended Bloch group and show it is naturally isomorphic to H_3(PSL(2,C)^δ;Z). Using the Rogers dilogarithm function this leads to an exact simplicial formula for the universal Cheeger-Chern-Simons class on this homology group. It also leads to an independent proof of the analytic relationship between volume and Chern-Simons invariant of hyperbolic 3-manifolds conjectured by Neumann and Zagier [Topology 1985] and proved by Yoshida [Invent. Math. 1985] as well as effective formulae for the Chern-Simons invariant of a hyperbolic 3-manifold.\n\nCrossref results for query: parametric surface reconstruction topology recovery point clouds\n\n[1]\nTitle: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\nSource: Crossref / Computer-Aided Design\nAuthors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov\nPublished: 2021-11\nURL: https://doi.org/10.1016/j.cad.2021.103090\nDOI: 10.1016/j.cad.2021.103090\nSummary: No abstract/summary available.\n\n[2]\nTitle: Deep Learning-Based Surface Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2024-12-6\nURL: https://doi.org/10.52843/cassyni.cj5jq2\nDOI: 10.52843/cassyni.cj5jq2\nSummary: No abstract/summary available.\n\n[3]\nTitle: Surface Reconstruction of Point Clouds with Noises\nSource: Crossref / Crossref\nAuthors: Zhengxuan Yi, Maohua Du, Yongjun Cao, Jianan Liang\nPublished: 2024\nURL: https://doi.org/10.2139/ssrn.5042514\nDOI: 10.2139/ssrn.5042514\nSummary: No abstract/summary available.\n\n[4]\nTitle: Topology‐Aware Surface Reconstruction for Point Clouds\nSource: Crossref / Computer Graphics Forum\nAuthors: Rickard Brüel‐Gabrielsson, Vignesh Ganapathi‐Subramanian, Primoz Skraba, Leonidas J. Guibas\nPublished: 2020-8\nURL: https://doi.org/10.1111/cgf.14079\nDOI: 10.1111/cgf.14079\nSummary: <jats:title>Abstract</jats:title><jats:p>We present an approach to incorporate topological priors in the reconstruction of a surface from a point scan. We base the reconstruction on basis functions which are optimized to provide a good fit to the point scan while satisfying predefined topological constraints. We optimize the parameters of a model to obtain a likelihood function over the reconstruction domain. The topological constraints are captured by persistence diagrams which are incorporated within the optimization algorithm to promote the correct topology. The result is a novel topology‐aware technique which can (i) weed out topological noise from point scans, and (ii) capture certain nuanced properties of the underlying shape which could otherwise be lost while performing surface reconstruction. We show results reconstructing shapes with multiple potential topologies, compare to other classical surface construction techniques, and show the completion of real scan data.</jats:p>\n\n[5]\nTitle: PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds\nSource: Crossref / 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)\nAuthors: Shangfeng Huang, Ruisheng Wang, Bo Guo, Hongxin Yang\nPublished: 2024-6-16\nURL: https://doi.org/10.1109/cvpr52733.2024.02624\nDOI: 10.1109/cvpr52733.2024.02624\nSummary: No abstract/summary available.\n\n[6]\nTitle: Monocular Non-Rigid Surface Reconstruction with Learned Deformation Model\nSource: Crossref / Robust Methods for Dense Monocular Non-Rigid 3D Reconstruction and Alignment of Point Clouds\nAuthors: Vladislav Golyanik\nPublished: 2020\nURL: https://doi.org/10.1007/978-3-658-30567-3_7\nDOI: 10.1007/978-3-658-30567-3_7\nSummary: No abstract/summary available.\n\n[7]\nTitle: NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: Ruikai Cui, Shi Qiu, Jiawei Liu, Saeed Anwar, Nick Barnes\nPublished: 2024-12-17\nURL: https://doi.org/10.32388/q45a8j\nDOI: 10.32388/q45a8j\nSummary: <jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this paper, we introduce NumGrad-Pull, leveraging the representation capability of tri-plane structures to accelerate the learning of signed distance functions and enhance the fidelity of local details in surface reconstruction. To further improve the training stability of grid-based tri-planes, we propose to exploit numerical gradients, replacing conventional analytical computations. Additionally, we present a progressive plane expansion strategy to facilitate faster signed distance function convergence and design a data sampling strategy to mitigate reconstruction artifacts. Our extensive experiments across a variety of benchmarks demonstrate the effectiveness and robustness of our approach. Code is available at https://github.com/CuiRuikai/NumGrad-Pull. </jats:p>\n\n[8]\nTitle: PointNeuron: 3D Neuron Reconstruction via Geometry and Topology Learning of Point Clouds\nSource: Crossref / 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)\nAuthors: Runkai Zhao, Heng Wang, Chaoyi Zhang, Weidong Cai\nPublished: 2023-1\nURL: https://doi.org/10.1109/wacv56688.2023.00574\nDOI: 10.1109/wacv56688.2023.00574\nSummary: No abstract/summary available.\n\n[9]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-3-31\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1\nDOI: 10.1109/tgrs.2025.3608325/v1/review1\nSummary: No abstract/summary available.\n\n[10]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-4-16\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2\nDOI: 10.1109/tgrs.2025.3608325/v1/review2\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_e2fb58414c944b69b0c06d2b' is_error=False
content="Error: Client error '429 Too Many Requests' for url 'https://api.crossref.org/works?query=geometry+constrained+modeling+reverse+engineering+CAD+point+cloud&rows=10&select=title%2Cauthor%2CDOI%2CURL%2Cpublished-print%2Cpublished-online%2Cissued%2Ccontainer-title%2Cabstract&filter=from-pub-date%3A2020-01-01'\nFor more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429" name='search_all_sources' call_id='call_6f6ca4e2c1c04c7183f69439' is_error=True
```

### Message 5

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Combined search results

```text
Combined search results

Query: point cloud to B-rep reconstruction deep learning CAD

arXiv results for query: point cloud to B-rep reconstruction deep learning CAD

[1]
Title: A study of the link between cosmic rays and clouds with a cloud chamber at the CERN PS
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-16T19:12:19Z
URL: http://arxiv.org/abs/physics/0104048v1
Summary: Recent satellite data have revealed a surprising correlation between galactic cosmic ray (GCR) intensity and the fraction of the Earth covered by clouds. If this correlation were to be established by a causal mechanism, it could provide a crucial step in understanding the long-sought mechanism connecting solar and climate variability. The Earth's climate seems to be remarkably sensitive to solar activity, but variations of the Sun's electromagnetic radiation appear to be too small to account for the observed climate variability. However, since the GCR intensity is strongly modulated by the solar wind, a GCR-cloud link may provide a sufficient amplifying mechanism. Moreover if this connection were to be confirmed, it could have profound consequences for our understanding of the solar contributions to the current global warming. The CLOUD (Cosmics Leaving OUtdoor Droplets) project proposes to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. CLOUD plans to perform detailed laboratory measurements in a particle beam at CERN, where all the parameters can be precisely controlled and measured. The beam will pass through an expansion cloud chamber and a reactor chamber where the atmosphere is to be duplicated by moist air charged with selected aerosols and trace condensable vapours. An array of external detectors and mass spectrometers is used to analyse the physical and chemical characteristics of the aerosols and trace gases during beam exposure. Where beam effects are found, the experiment will seek to evaluate their significance in the atmosphere by incorporating them into aerosol and cloud models.

[2]
Title: CLOUD: an atmospheric research facility at CERN
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-24T07:30:14Z
URL: http://arxiv.org/abs/physics/0104076v1
Summary: This report is the second of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document places CLOUD in the framework of a CERN facility for atmospheric research, and provides further details on the particle beam requirements.

[3]
Title: Addendum to the CLOUD proposal
Source: arXiv
Authors: The Cloud Collaboration
Published: 2001-04-23T13:58:48Z
URL: http://arxiv.org/abs/physics/0104068v1
Summary: This report is the first of two addenda to the CLOUD proposal at CERN (physics/0104048), which aims to test experimentally the existence a link between cosmic rays and cloud formation, and to understand the microphysical mechanism. The document provides further details on the detector design, scientific motivation and experimental programme.

[4]
Title: Learn to Accumulate Evidence from All Training Samples: Theory and Practice
Source: arXiv
Authors: Deep Pandey, Qi Yu
Published: 2023-06-19T18:27:12Z
URL: http://arxiv.org/abs/2306.11113v2
Summary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.

[5]
Title: ComplexGen: CAD Reconstruction by B-Rep Chain Complex Generation
Source: arXiv
Authors: Haoxiang Guo, Shilin Liu, Hao Pan, Yang Liu, Xin Tong
Published: 2022-05-29T05:30:33Z
URL: http://arxiv.org/abs/2205.14573v1
Summary: We view the reconstruction of CAD models in the boundary representation (B-Rep) as the detection of geometric primitives of different orders, i.e. vertices, edges and surface patches, and the correspondence of primitives, which are holistically modeled as a chain complex, and show that by modeling such comprehensive structures more complete and regularized reconstructions can be achieved. We solve the complex generation problem in two steps. First, we propose a novel neural framework that consists of a sparse CNN encoder for input point cloud processing and a tri-path transformer decoder for generating geometric primitives and their mutual relationships with estimated probabilities. Second, given the probabilistic structure predicted by the neural network, we recover a definite B-Rep chain complex by solving a global optimization maximizing the likelihood under structural validness constraints and applying geometric refinements. Extensive tests on large scale CAD datasets demonstrate that the modeling of B-Rep chain complex structure enables more accurate detection for learning and more constrained reconstruction for optimization, leading to structurally more faithful and complete CAD B-Rep models than previous results.

[6]
Title: The Modern Mathematics of Deep Learning
Source: arXiv
Authors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen
Published: 2021-05-09T21:30:42Z
URL: http://arxiv.org/abs/2105.04026v2
Summary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.

[7]
Title: Physics-informed self-supervised deep learning reconstruction for accelerated first-pass perfusion cardiac MRI
Source: arXiv
Authors: Elena Martín-González, Ebraham Alskaf, Amedeo Chiribiri, Pablo Casaseca-de-la-Higuera, Carlos Alberola-López
Published: 2023-01-05T12:11:17Z
URL: http://arxiv.org/abs/2301.02033v1
Summary: First-pass perfusion cardiac magnetic resonance (FPP-CMR) is becoming an essential non-invasive imaging method for detecting deficits of myocardial blood flow, allowing the assessment of coronary heart disease. Nevertheless, acquisitions suffer from relatively low spatial resolution and limited heart coverage. Compressed sensing (CS) methods have been proposed to accelerate FPP-CMR and achieve higher spatial resolution. However, the long reconstruction times have limited the widespread clinical use of CS in FPP-CMR. Deep learning techniques based on supervised learning have emerged as alternatives for speeding up reconstructions. However, these approaches require fully sampled data for training, which is not possible to obtain, particularly high-resolution FPP-CMR images. Here, we propose a physics-informed self-supervised deep learning FPP-CMR reconstruction approach for accelerating FPP-CMR scans and hence facilitate high spatial resolution imaging. The proposed method provides high-quality FPP-CMR images from 10x undersampled data without using fully sampled reference data.

[8]
Title: Deep Learning for 3D Point Clouds: A Survey
Source: arXiv
Authors: Yulan Guo, Hanyun Wang, Qingyong Hu, Hao Liu, Li Liu
Published: 2019-12-27T09:15:54Z
URL: http://arxiv.org/abs/1912.12033v2
Summary: Point cloud learning has lately attracted increasing attention due to its wide applications in many areas, such as computer vision, autonomous driving, and robotics. As a dominating technique in AI, deep learning has been successfully used to solve various 2D vision problems. However, deep learning on point clouds is still in its infancy due to the unique challenges faced by the processing of point clouds with deep neural networks. Recently, deep learning on point clouds has become even thriving, with numerous methods being proposed to address different problems in this area. To stimulate future research, this paper presents a comprehensive review of recent progress in deep learning methods for point clouds. It covers three major tasks, including 3D shape classification, 3D object detection and tracking, and 3D point cloud segmentation. It also presents comparative results on several publicly available datasets, together with insightful observations and inspiring future research directions.

[9]
Title: Deep MRI Reconstruction: Unrolled Optimization Algorithms Meet Neural Networks
Source: arXiv
Authors: Dong Liang, Jing Cheng, Ziwen Ke, Leslie Ying
Published: 2019-07-26T08:22:53Z
URL: http://arxiv.org/abs/1907.11711v1
Summary: Image reconstruction from undersampled k-space data has been playing an important role for fast MRI. Recently, deep learning has demonstrated tremendous success in various fields and also shown potential to significantly speed up MR reconstruction with reduced measurements. This article gives an overview of deep learning-based image reconstruction methods for MRI. Three types of deep learning-based approaches are reviewed, the data-driven, model-driven and integrated approaches. The main structure of each network in three approaches is explained and the analysis of common parts of reviewed networks and differences in-between are highlighted. Based on the review, a number of signal processing issues are discussed for maximizing the potential of deep reconstruction for fast MRI. the discussion may facilitate further development of "optimal" network and performance analysis from a theoretical point of view.

[10]
Title: Deep Learning and Computational Physics (Lecture Notes)
Source: arXiv
Authors: Deep Ray, Orazio Pinti, Assad A. Oberai
Published: 2023-01-03T03:56:19Z
URL: http://arxiv.org/abs/2301.00942v1
Summary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.

Crossref results for query: point cloud to B-rep reconstruction deep learning CAD

[1]
Title: Deep Learning-Based Point Cloud Reconstruction Method for CAD Models
Source: Crossref / 2025 10th International Conference on Intelligent Computing and Signal Processing (ICSP)
Authors: Hongliang Zhang, Deyuan Wang, Pengpei Gao, Chunhe Song
Published: 2025-5-16
URL: https://doi.org/10.1109/icsp65755.2025.11087181
DOI: 10.1109/icsp65755.2025.11087181
Summary: No abstract/summary available.

[2]
Title: Point Cloud Upsampling and Normal Estimation using Deep Learning for Robust Surface Reconstruction
Source: Crossref / Proceedings of the 16th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications
Authors: Rajat Sharma, Tobias Schwandt, Christian Kunert, Steffen Urban, Wolfgang Broll
Published: 2021
URL: https://doi.org/10.5220/0010211600700079
DOI: 10.5220/0010211600700079
Summary: No abstract/summary available.

[3]
Title: Optimizing 3D Point Cloud Reconstruction Through Integrating Deep Learning and Clustering Models
Source: Crossref / Electronics
Authors: Seyyedbehrad Emadi, Marco Limongiello
Published: 2025-1-20
URL: https://doi.org/10.3390/electronics14020399
DOI: 10.3390/electronics14020399
Summary: <jats:p>Noise in 3D photogrammetric point clouds—both close-range and UAV-generated—poses a significant challenge to the accuracy and usability of digital models. This study presents a novel deep learning-based approach to improve the quality of point clouds by addressing this issue. We propose a two-step methodology: first, a variational autoencoder reduces features, followed by clustering models to assess and mitigate noise in the point clouds. This study evaluates four clustering methods—k-means, agglomerative clustering, Spectral clustering, and Gaussian mixture model—based on photogrammetric parameters, reprojection error, projection accuracy, angles of intersection, distance, and the number of cameras used in tie point calculations. The approach is validated using point cloud data from the Temple of Neptune in Paestum, Italy. The results show that the proposed method significantly improves 3D reconstruction quality, with k-means outperforming other clustering techniques based on three evaluation metrics. This method offers superior versatility and performance compared to traditional and machine learning techniques, demonstrating its potential to enhance UAV-based surveying and inspection practices.</jats:p>

[4]
Title: Deep Learning-Based Point Cloud Analysis
Source: Crossref / 3D Point Cloud Analysis
Authors: Shan Liu, Min Zhang, Pranav Kadam, C.-C. Jay Kuo
Published: 2021
URL: https://doi.org/10.1007/978-3-030-89180-0_3
DOI: 10.1007/978-3-030-89180-0_3
Summary: No abstract/summary available.

[5]
Title: Deep-Learning-Based Point Cloud Analysis I
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_5
DOI: 10.1007/978-981-97-9570-3_5
Summary: No abstract/summary available.

[6]
Title: Deep-Learning-Based Point Cloud Analysis II
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_6
DOI: 10.1007/978-981-97-9570-3_6
Summary: No abstract/summary available.

[7]
Title: Segmentation and Local Reconstruction of Turbine Blade Point Cloud
Source: Crossref / CAD'20
Authors: Wei Wang, ZhenYu Guo, JiaMing Yang, Pai Zheng
Published: 2020-5-25
URL: https://doi.org/10.14733/cadconfp.2020.193-198
DOI: 10.14733/cadconfp.2020.193-198
Summary: No abstract/summary available.

[8]
Title: Deep-Learning-based Point Cloud Enhancement I
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_3
DOI: 10.1007/978-981-97-9570-3_3
Summary: No abstract/summary available.

[9]
Title: Deep-Learning-Based Point Cloud Enhancement II
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_4
DOI: 10.1007/978-981-97-9570-3_4
Summary: No abstract/summary available.

[10]
Title: Point Cloud Dataset Creation for Machine Learning on CAD Models
Source: Crossref / CAD'20
Authors: Andrew Colligan, Trevor Robinson, Declan Nolan, Yang Hua
Published: 2020-5-25
URL: https://doi.org/10.14733/cadconfp.2020.152-156
DOI: 10.14733/cadconfp.2020.152-156
Summary: No abstract/summary available.
Combined search results

Query: parametric surface reconstruction topology recovery point clouds

arXiv results for query: parametric surface reconstruction topology recovery point clouds

[1]
Title: Sequential Point Clouds: A Survey
Source: arXiv
Authors: Haiyan Wang, Yingli Tian
Published: 2022-04-20T09:14:20Z
URL: http://arxiv.org/abs/2204.09337v2
Summary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.

[2]
Title: Parametric Point Cloud Completion for Polygonal Surface Reconstruction
Source: arXiv
Authors: Zhaiyu Chen, Yuqing Wang, Liangliang Nan, Xiao Xiang Zhu
Published: 2025-03-11T12:20:24Z
URL: http://arxiv.org/abs/2503.08363v1
Summary: Existing polygonal surface reconstruction methods heavily depend on input completeness and struggle with incomplete point clouds. We argue that while current point cloud completion techniques may recover missing points, they are not optimized for polygonal surface reconstruction, where the parametric representation of underlying surfaces remains overlooked. To address this gap, we introduce parametric completion, a novel paradigm for point cloud completion, which recovers parametric primitives instead of individual points to convey high-level geometric structures. Our presented approach, PaCo, enables high-quality polygonal surface reconstruction by leveraging plane proxies that encapsulate both plane parameters and inlier points, proving particularly effective in challenging scenarios with highly incomplete data. Comprehensive evaluations of our approach on the ABC dataset establish its effectiveness with superior performance and set a new standard for polygonal surface reconstruction from incomplete data. Project page: https://parametric-completion.github.io.

[3]
Title: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds
Source: arXiv
Authors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer
Published: 2020-05-24T00:03:27Z
URL: http://arxiv.org/abs/2005.11626v1
Summary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.

[4]
Title: Topological spaces of persistence modules and their properties
Source: arXiv
Authors: Peter Bubenik, Tane Vergili
Published: 2018-02-22T15:56:39Z
URL: http://arxiv.org/abs/1802.08117v2
Summary: Persistence modules are a central algebraic object arising in topological data analysis. The notion of interleaving provides a natural way to measure distances between persistence modules. We consider various classes of persistence modules, including many of those that have been previously studied, and describe the relationships between them. In the cases where these classes are sets, interleaving distance induces a topology. We undertake a systematic study the resulting topological spaces and their basic topological properties.

[5]
Title: On Hawaiian Groups of Some Topological Spaces
Source: arXiv
Authors: Ameneh Babaee, Behrooz Mashayekhy, Hanieh Mirebrahimi
Published: 2011-11-03T05:39:39Z
URL: http://arxiv.org/abs/1111.0731v2
Summary: The paper is devoted to study the structure of Hawaiian groups of some topological spaces. We present some behaviors of Hawaiian groups with respect to product spaces, weak join spaces, cone spaces, covering spaces and locally trivial bundles. In particular, we determine the structure of the $n$-dimensional Hawaiian group of the $m$-dimensional Hawaiian earring space, for all $1\leq m\leq n$.

[6]
Title: A class of tight contact structures on Sigma_2 x I
Source: arXiv
Authors: Tanya Cofer
Published: 2004-11-09T17:49:14Z
URL: http://arxiv.org/abs/math/0411208v1
Summary: We employ cut and paste contact topological techniques to classify some tight contact structures on the closed, oriented genus-2 surface times the interval. A boundary condition is specified so that the Euler class of the of the contact structure vanishes when evaluated on each boundary component. We prove that there exists a unique, non-product tight contact structure in this case.

[7]
Title: Neural RGB-D Surface Reconstruction
Source: arXiv
Authors: Dejan Azinović, Ricardo Martin-Brualla, Dan B Goldman, Matthias Nießner, Justus Thies
Published: 2021-04-09T18:00:01Z
URL: http://arxiv.org/abs/2104.04532v3
Summary: Obtaining high-quality 3D reconstructions of room-scale scenes is of paramount importance for upcoming applications in AR or VR. These range from mixed reality applications for teleconferencing, virtual measuring, virtual room planing, to robotic applications. While current volume-based view synthesis methods that use neural radiance fields (NeRFs) show promising results in reproducing the appearance of an object or scene, they do not reconstruct an actual surface. The volumetric representation of the surface based on densities leads to artifacts when a surface is extracted using Marching Cubes, since during optimization, densities are accumulated along the ray and are not used at a single sample point in isolation. Instead of this volumetric representation of the surface, we propose to represent the surface using an implicit function (truncated signed distance function). We show how to incorporate this representation in the NeRF framework, and extend it to use depth measurements from a commodity RGB-D sensor, such as a Kinect. In addition, we propose a pose and camera refinement technique which improves the overall reconstruction quality. In contrast to concurrent work on integrating depth priors in NeRF which concentrates on novel view synthesis, our approach is able to reconstruct high-quality, metrical 3D reconstructions.

[8]
Title: The homotopy invariance of the string topology loop product and string bracket
Source: arXiv
Authors: Ralph L. Cohen, John Klein, Dennis Sullivan
Published: 2005-09-28T17:06:23Z
URL: http://arxiv.org/abs/math/0509667v2
Summary: Let M be a closed, oriented, n -manifold, and LM its free loop space. Chas and Sullivan defined a commutative algebra structure in the homology of LM, and a Lie algebra structure in its equivariant homology. These structures are known as the string topology loop product and string bracket, respectively. In this paper we prove that these structures are homotopy invariants in the following sense. Let f : M_1 \to M_2 be a homotopy equivalence of closed, oriented n -manifolds. Then the induced equivalence, Lf : LM_1 \to LM_2 induces a ring isomorphism in homology, and an isomorphism of Lie algebras in equivariant homology. The analogous statement also holds true for any generalized homology theory h_* that supports an orientation of the M_i 's.

[9]
Title: On subgroups of minimal topological groups
Source: arXiv
Authors: V. V. Uspenskij
Published: 2000-04-19T00:36:47Z
URL: http://arxiv.org/abs/math/0004119v2
Summary: A topological group is minimal if it does not admit a strictly coarser Hausdorff group topology. The Roelcke uniformity (or lower uniformity) on a topological group is the greatest lower bound of the left and right uniformities. A group is Roelcke-precompact if it is precompact with respect to the Roelcke uniformity. Many naturally arising non-Abelian topological groups are Roelcke-precompact and hence have a natural compactification. We use such compactifications to prove that some groups of isometries are minimal. In particular, if U_1 is the Urysohn universal metric space of diameter 1, the group Iso(U_1) of all self-isometries of U_1 is Roelcke-precompact, topologically simple and minimal. We also show that every topological group is a subgroup of a minimal topologically simple Roelcke-precompact group of the form Iso(M), where M is an appropriate non-separable version of the Urysohn space.

[10]
Title: Extended Bloch group and the Cheeger-Chern-Simons class
Source: arXiv
Authors: Walter D Neumann
Published: 2003-07-08T16:26:37Z
URL: http://arxiv.org/abs/math/0307092v2
Summary: We define an extended Bloch group and show it is naturally isomorphic to H_3(PSL(2,C)^δ;Z). Using the Rogers dilogarithm function this leads to an exact simplicial formula for the universal Cheeger-Chern-Simons class on this homology group. It also leads to an independent proof of the analytic relationship between volume and Chern-Simons invariant of hyperbolic 3-manifolds conjectured by Neumann and Zagier [Topology 1985] and proved by Yoshida [Invent. Math. 1985] as well as effective formulae for the Chern-Simons invariant of a hyperbolic 3-manifold.

Crossref results for query: parametric surface reconstruction topology recovery point clouds

[1]
Title: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction
Source: Crossref / Computer-Aided Design
Authors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov
Published: 2021-11
URL: https://doi.org/10.1016/j.cad.2021.103090
DOI: 10.1016/j.cad.2021.103090
Summary: No abstract/summary available.

[2]
Title: Deep Learning-Based Surface Reconstruction from Point Clouds
Source: Crossref / Crossref
Authors: Unknown authors
Published: 2024-12-6
URL: https://doi.org/10.52843/cassyni.cj5jq2
DOI: 10.52843/cassyni.cj5jq2
Summary: No abstract/summary available.

[3]
Title: Surface Reconstruction of Point Clouds with Noises
Source: Crossref / Crossref
Authors: Zhengxuan Yi, Maohua Du, Yongjun Cao, Jianan Liang
Published: 2024
URL: https://doi.org/10.2139/ssrn.5042514
DOI: 10.2139/ssrn.5042514
Summary: No abstract/summary available.

[4]
Title: Topology‐Aware Surface Reconstruction for Point Clouds
Source: Crossref / Computer Graphics Forum
Authors: Rickard Brüel‐Gabrielsson, Vignesh Ganapathi‐Subramanian, Primoz Skraba, Leonidas J. Guibas
Published: 2020-8
URL: https://doi.org/10.1111/cgf.14079
DOI: 10.1111/cgf.14079
Summary: <jats:title>Abstract</jats:title><jats:p>We present an approach to incorporate topological priors in the reconstruction of a surface from a point scan. We base the reconstruction on basis functions which are optimized to provide a good fit to the point scan while satisfying predefined topological constraints. We optimize the parameters of a model to obtain a likelihood function over the reconstruction domain. The topological constraints are captured by persistence diagrams which are incorporated within the optimization algorithm to promote the correct topology. The result is a novel topology‐aware technique which can (i) weed out topological noise from point scans, and (ii) capture certain nuanced properties of the underlying shape which could otherwise be lost while performing surface reconstruction. We show results reconstructing shapes with multiple potential topologies, compare to other classical surface construction techniques, and show the completion of real scan data.</jats:p>

[5]
Title: PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds
Source: Crossref / 2024 IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)
Authors: Shangfeng Huang, Ruisheng Wang, Bo Guo, Hongxin Yang
Published: 2024-6-16
URL: https://doi.org/10.1109/cvpr52733.2024.02624
DOI: 10.1109/cvpr52733.2024.02624
Summary: No abstract/summary available.

[6]
Title: Monocular Non-Rigid Surface Reconstruction with Learned Deformation Model
Source: Crossref / Robust Methods for Dense Monocular Non-Rigid 3D Reconstruction and Alignment of Point Clouds
Authors: Vladislav Golyanik
Published: 2020
URL: https://doi.org/10.1007/978-3-658-30567-3_7
DOI: 10.1007/978-3-658-30567-3_7
Summary: No abstract/summary available.

[7]
Title: NumGrad-Pull: Numerical Gradient Guided Tri-plane Representation for Surface Reconstruction from Point Clouds
Source: Crossref / Crossref
Authors: Ruikai Cui, Shi Qiu, Jiawei Liu, Saeed Anwar, Nick Barnes
Published: 2024-12-17
URL: https://doi.org/10.32388/q45a8j
DOI: 10.32388/q45a8j
Summary: <jats:p>Reconstructing continuous surfaces from unoriented and unordered 3D points is a fundamental challenge in computer vision and graphics. Recent advancements address this problem by training neural signed distance functions to pull 3D location queries to their closest points on a surface, following the predicted signed distances and the analytical gradients computed by the network. In this paper, we introduce NumGrad-Pull, leveraging the representation capability of tri-plane structures to accelerate the learning of signed distance functions and enhance the fidelity of local details in surface reconstruction. To further improve the training stability of grid-based tri-planes, we propose to exploit numerical gradients, replacing conventional analytical computations. Additionally, we present a progressive plane expansion strategy to facilitate faster signed distance function convergence and design a data sampling strategy to mitigate reconstruction artifacts. Our extensive experiments across a variety of benchmarks demonstrate the effectiveness and robustness of our approach. Code is available at https://github.com/CuiRuikai/NumGrad-Pull. </jats:p>

[8]
Title: PointNeuron: 3D Neuron Reconstruction via Geometry and Topology Learning of Point Clouds
Source: Crossref / 2023 IEEE/CVF Winter Conference on Applications of Computer Vision (WACV)
Authors: Runkai Zhao, Heng Wang, Chaoyi Zhang, Weidong Cai
Published: 2023-1
URL: https://doi.org/10.1109/wacv56688.2023.00574
DOI: 10.1109/wacv56688.2023.00574
Summary: No abstract/summary available.

[9]
Title: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"
Source: Crossref / Crossref
Authors: Unknown authors
Published: 2025-3-31
URL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1
DOI: 10.1109/tgrs.2025.3608325/v1/review1
Summary: No abstract/summary available.

[10]
Title: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"
Source: Crossref / Crossref
Authors: Unknown authors
Published: 2025-4-16
URL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2
DOI: 10.1109/tgrs.2025.3608325/v1/review2
Summary: No abstract/summary available.
Error: Client error '429 Too Many Requests' for url 'https://api.crossref.org/works?query=geometry+constrained+modeling+reverse+engineering+CAD+point+cloud&rows=10&select=title%2Cauthor%2CDOI%2CURL%2Cpublished-print%2Cpublished-online%2Cissued%2Ccontainer-title%2Cabstract&filter=from-pub-date%3A2020-01-01'
For more information check: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429
```

### Message 6

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=6

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval successfully identified high-impact deep learning papers like ComplexGen, PBWR, and PaCo, which strongly align with the B-rep reconstruction topic. However, the retrieval failed to execute the 'geometry constrained modeling' query due to API rate limiting, creating a significant gap in traditional optimization-based reverse engineering methods. Furthermore, several promising candidates (e.g., Coiffier et al. 2021) lack abstracts in the retrieved results, making it impossible to verify if they produce true B-reps or just surfaces. The set is currently biased towards neural implicit/polygonal methods and needs to be balanced with explicit parametric/constraint-based approaches.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 1,
    "metadata_score": 1,
    "diversity_score": 1,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Both arXiv and Crossref were searched."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "At least 5 distinct candidates were identified (ComplexGen, PBWR, PaCo, Topology-Aware, Parametric Fitting)."
    },
    "relevance": {
      "passed": true,
      "reason": "Top candidates (ComplexGen, PBWR) are highly relevant to B-rep and wireframe reconstruction."
    },
    "metadata": {
      "passed": false,
      "reason": "Several candidates (e.g., Huang et al. 2024, Coiffier et al. 2021) are missing abstracts, hindering verification of B-rep output."
    },
    "query_fit": {
      "passed": false,
      "reason": "The explicit user constraint for 'geometry-constrained modeling' was not successfully executed due to a 429 error, missing a key methodological category."
    },
    "gaps": {
      "passed": false,
      "reason": "Missing traditional/non-learning optimization methods for parametric fitting (e.g., RANSAC-based primitive fitting with constraints) often found in CAD journals."
    }
  },
  "key_risks": [
    "Methodology bias: Results skew heavily toward Deep Learning/Neural methods, ignoring classical geometric optimization.",
    "Ambiguous output: 'Topology-Aware Surface Reconstruction' and 'Polygonal Surface Reconstruction' may not strictly produce CAD B-reps (NURBS/Primitives).",
    "Missing abstracts prevent accurate filtering of mesh-only vs. B-rep methods in the Crossref set."
  ],
  "next_actions": [
    "Retry the failed query for 'geometry constrained modeling reverse engineering CAD' using a different source (e.g., Semantic Scholar or direct search of 'Computer-Aided Design' journal) to capture non-DL methods.",
    "Expand search terms to include 'primitive fitting', 'constructive solid geometry (CSG) reconstruction', and 'CAD segmentation' to find parametric approaches.",
    "Filter for papers explicitly mentioning 'NURBS', 'solids', or 'topology graph' in titles/abstracts to ensure B-rep fidelity.",
    "Locate and retrieve abstracts for the Crossref candidates (Coiffier 2021, Huang 2024) to confirm they are not mesh-only."
  ]
}
```

### Message 7

- Source: `PlannerAgent`
- Type: `TextMessage`
- Summary: Structured planner output: topic=B-rep reconstruction from point clouds, queries=3

```text
{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Revise the retrieval to cover missing traditional/optimization methods (geometry-constrained, NURBS fitting) and verify the relevance of previous hits by retrieving their abstracts, ensuring a balanced mix of deep learning and classical CAD reconstruction techniques.",
  "time_range": {
    "start_year": 2020,
    "end_year": 2025,
    "is_explicit": false
  },
  "focus_areas": [
    "geometry-constrained modeling",
    "NURBS and parametric surface fitting",
    "Constructive Solid Geometry (CSG) reconstruction",
    "B-rep topology graph extraction",
    "primitive fitting"
  ],
  "exclude_areas": [
    "mesh-only reconstruction",
    "implicit reconstruction without B-rep extraction"
  ],
  "queries": [
    {
      "query": "NURBS surface fitting point clouds reverse engineering constraints",
      "reason": "Addresses the 'geometry-constrained modeling' and parametric surface gap by targeting traditional optimization-based fitting methods often published in CAD journals.",
      "sources": ["Crossref", "arXiv"]
    },
    {
      "query": "constructive solid geometry CSG reconstruction point clouds primitives",
      "reason": "Captures the CSG and primitive-based reconstruction subfield, which generates B-reps via geometric primitives and is distinct from mesh-based methods.",
      "sources": ["Crossref", "arXiv"]
    },
    {
      "query": "B-Rep topology graph recovery point clouds deep learning",
      "reason": "Refines the deep learning search to focus specifically on topological graph extraction (wires, edges, faces) rather than generic surface reconstruction, ensuring B-rep output.",
      "sources": ["arXiv", "Crossref"]
    }
  ],
  "assumptions": [
    "The previous HTTP 429 error was transient; re-issuing optimized queries will succeed.",
    "Searching for specific methodologies (NURBS, CSG) will yield papers with accessible abstracts."
  ],
  "success_criteria": [
    "Retrieve at least 2 papers focusing on traditional optimization or constraint-based fitting.",
    "Retrieve abstracts for previously identified ambiguous hits (e.g., Coiffier et al. 2021).",
    "Ensure representation of CSG/Primitive-based reconstruction methods."
  ]
}
```

### Message 8

- Source: `RetrievalAgent`
- Type: `ToolCallRequestEvent`
- Summary: Requested 5 tool call(s): search_all_sources, search_all_sources, search_all_sources, fetch_webpage_excerpt, fetch_webpage_excerpt

```text
FunctionCall(id='call_d8f34cf2bed14d719dace290', arguments='{"from_year":"2020","max_results_per_source":"8","query":"NURBS surface fitting point clouds reverse engineering constraints"}', name='search_all_sources')
FunctionCall(id='call_f6f71dd8ffbd4442a1be086c', arguments='{"from_year":"2020","max_results_per_source":"8","query":"constructive solid geometry CSG reconstruction point clouds primitives"}', name='search_all_sources')
FunctionCall(id='call_5d59209b4efa4ccb84a34758', arguments='{"from_year":"2020","max_results_per_source":"8","query":"B-Rep topology graph recovery point clouds deep learning"}', name='search_all_sources')
FunctionCall(id='call_0a2a62c6754845f5b8dc37a3', arguments='{"url":"https://doi.org/10.1016/j.cad.2021.103090","max_chars":2000}', name='fetch_webpage_excerpt')
FunctionCall(id='call_3080290fa2014cebb412ee9b', arguments='{"url":"https://doi.org/10.1109/cvpr52733.2024.02624","max_chars":2000}', name='fetch_webpage_excerpt')
```

### Message 9

- Source: `RetrievalAgent`
- Type: `ToolCallExecutionEvent`
- Summary: Executed 5 tool call(s): search_all_sources, search_all_sources, search_all_sources, fetch_webpage_excerpt, fetch_webpage_excerpt

```text
content='Combined search results\n\nQuery: NURBS surface fitting point clouds reverse engineering constraints\n\narXiv results for query: NURBS surface fitting point clouds reverse engineering constraints\n\n[1]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[2]\nTitle: Reverse Engineering Point Clouds to Fit Tensor Product B-Spline Surfaces by Blending Local Fits\nSource: arXiv\nAuthors: Lavanya Sita Tekumalla, Elaine Cohen\nPublished: 2014-11-21T19:37:27Z\nURL: http://arxiv.org/abs/1411.5993v1\nSummary: Being able to reverse engineer from point cloud data to obtain 3D models is important in modeling. As our main contribution, we present a new method to obtain a tensor product B-spline representation from point cloud data by fitting surfaces to appropriately segmented data. By blending multiple local fits our method is more efficient than existing techniques, with the ability to deal with more detail by efficiently introducing a high number of knots. Further point cloud data obtained by digitizing 3D data, typically presents many associated complications like noise and missing data. As our second contribution, we propose an end-to-end framework for smoothing, hole filling, parameterization, knot selection and B-spline fitting that addresses these issues, works robustly with large irregularly shaped data containing holes and is straightforward to implement.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Empirical Studies on Adversarial Reverse Engineering with Students\nSource: arXiv\nAuthors: Tab, Zhang, Bjorn De Sutter, Christian Collberg, Bart Coppens\nPublished: 2026-03-04T09:27:46Z\nURL: http://arxiv.org/abs/2603.03875v1\nSummary: Empirical research in reverse engineering and software protection is crucial for evaluating the efficacy of methods designed to protect software against unauthorized access and tampering. However, conducting such studies with professional reverse engineers presents significant challenges, including access to professionals and affordability. This paper explores the use of students as participants in empirical reverse engineering experiments, examining their suitability and the necessary training; the design of appropriate challenges; strategies for ensuring the rigor and validity of the research and its results; ways to maintain students\' privacy, motivation, and voluntary participation; and data collection methods. We present a systematic literature review of existing reverse engineering experiments and user studies, a discussion of related work from the broader domain of software engineering that applies to reverse engineering experiments, an extensive discussion of our own experience running experiments ourselves in the context of a master-level software hacking and protection course, and recommendations based on this experience. Our findings aim to guide future empirical studies in RE, balancing practical constraints with the need for meaningful, reproducible results.\n\n[5]\nTitle: Non-Invasive Reverse Engineering of Finite State Machines Using Power Analysis and Boolean Satisfiability\nSource: arXiv\nAuthors: Harsh Vamja, Richa Agrawal, Ranga Vemuri\nPublished: 2019-08-06T06:47:37Z\nURL: http://arxiv.org/abs/1908.01979v1\nSummary: In this paper, we present a non-invasive reverse engineering attack based on a novel approach that combines functional and power analysis to recover finite state machines from their synchronous sequential circuit implementations. The proposed technique formulates the machine exploration and state identification problem as a Boolean constraint satisfaction problem and solves it using a SMT (Satisfiability Modulo Theories) solver. It uses power measurements to achieve fast convergence. Experimental results using the LGSynth\'91 benchmark suite show that the satisfiability-based approach is several times faster compared to existing techniques and can successfully recover 90%-100% of the transitions of a target machine.\n\n[6]\nTitle: Algorithms for geometrical operations with NURBS surfaces\nSource: arXiv\nAuthors: Gernot Beer\nPublished: 2022-10-24T12:23:57Z\nURL: http://arxiv.org/abs/2210.13160v1\nSummary: The aim of the paper is to show algorithms for geometrical manipulations on NURBS surfaces. These include generating NURBS surfaces that pass through given points, calculating the minimum distance to a point and include line to surface and surface to surface intersections.\n\n[7]\nTitle: Morescient GAI for Software Engineering (Extended Version)\nSource: arXiv\nAuthors: Marcus Kessel, Colin Atkinson\nPublished: 2024-06-07T07:38:33Z\nURL: http://arxiv.org/abs/2406.04710v2\nSummary: The ability of Generative AI (GAI) technology to automatically check, synthesize and modify software engineering artifacts promises to revolutionize all aspects of software engineering. Using GAI for software engineering tasks is consequently one of the most rapidly expanding fields of software engineering research, with over a hundred LLM-based code models having been published since 2021. However, the overwhelming majority of existing code models share a major weakness - they are exclusively trained on the syntactic facet of software, significantly lowering their trustworthiness in tasks dependent on software semantics. To address this problem, a new class of "Morescient" GAI is needed that is "aware" of (i.e., trained on) both the semantic and static facets of software. This, in turn, will require a new generation of software observation platforms capable of generating large quantities of execution observations in a structured and readily analyzable way. In this paper, we present a vision and roadmap for how such "Morescient" GAI models can be engineered, evolved and disseminated according to the principles of open science.\n\n[8]\nTitle: Database Reverse Engineering based on Association Rule Mining\nSource: arXiv\nAuthors: Nattapon Pannurat, Nittaya Kerdprasop, Kittisak Kerdprasop\nPublished: 2010-04-19T18:18:43Z\nURL: http://arxiv.org/abs/1004.3272v1\nSummary: Maintaining a legacy database is a difficult task especially when system documentation is poor written or even missing. Database reverse engineering is an attempt to recover high-level conceptual design from the existing database instances. In this paper, we propose a technique to discover conceptual schema using the association mining technique. The discovered schema corresponds to the normalization at the third normal form, which is a common practice in many business organizations. Our algorithm also includes the rule filtering heuristic to solve the problem of exponential growth of discovered rules inherited with the association mining technique.\n\nCrossref results for query: NURBS surface fitting point clouds reverse engineering constraints\n\n[1]\nTitle: NURBS-Based Surface Reconstruction from Point Clouds for Electromagnetic Target Modeling\nSource: Crossref / 2025 Photonics &amp;amp; Electromagnetics Research Symposium - Fall (PIERS-Fall)\nAuthors: Qianyan Shen, Ruoming Zhang, Hai Lin\nPublished: 2025-11-4\nURL: https://doi.org/10.23919/piers-fall62445.2025.11394360\nDOI: 10.23919/piers-fall62445.2025.11394360\nSummary: No abstract/summary available.\n\n[2]\nTitle: NURBS surface fitting from scattered point cloud combining patch growing and PSO\nSource: Crossref / Third International Computing Imaging Conference (CITA 2023)\nAuthors: Shangbo Gao, Chen Ma, Qingxin Yang, Yue Shen, Deming Kong\nPublished: 2023-11-6\nURL: https://doi.org/10.1117/12.2691763\nDOI: 10.1117/12.2691763\nSummary: No abstract/summary available.\n\n[3]\nTitle: MST Based Ordering of Point Clouds and Curve Fitting\nSource: Crossref / Proceedings of the 21st International Conference on Computer Vision Theory and Applications\nAuthors: Christoph Dalitz, Alexander Jongbloed\nPublished: 2026\nURL: https://doi.org/10.5220/0014152000004084\nDOI: 10.5220/0014152000004084\nSummary: No abstract/summary available.\n\n[4]\nTitle: Reverse Engineering: Investigation of Optimization Techniques in Point Clouds Registration\nSource: Crossref / SSRN Electronic Journal\nAuthors: George Yacout\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5297053\nDOI: 10.2139/ssrn.5297053\nSummary: No abstract/summary available.\n\n[5]\nTitle: Adaptive Surface Fitting with Local Refinement: LR B-Spline Surfaces\nSource: Crossref / SpringerBriefs in Earth System Sciences\nAuthors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken\nPublished: 2023\nURL: https://doi.org/10.1007/978-3-031-16954-0_3\nDOI: 10.1007/978-3-031-16954-0_3\nSummary: <jats:title>Abstract</jats:title><jats:p>A locally refined (LR) B-spline surface is a piecewise polynomial surface for which the distribution of the surface coefficients can be locally adapted. Such a mathematical representation is interesting for fitting scattered and noisy data, as the local behaviour of a real point cloud may require more degrees of freedom only locally. The number of redundant surface coefficients is minimized, which avoids the fitting of the point cloud’s noise. The surface approximation is performed iteratively either by solving a least squares system or by a local approximation method. This procedure allows for mesh refinement in domains where the distance between a current surface and the point cloud exceeds a prescribed tolerance. In this way, parts of the LR B-spline surface obtained at previous steps may be kept unchanged. This chapter aims at explaining the adaptive fitting using local refinement with LR B-splines. We present two examples with simulated point clouds to illustrate the methodology.</jats:p>\n\n[6]\nTitle: Application of Poisson Surface Reconstruction with Envelope Constraints to TLS Point Clouds of Scenes with Complex Objects\nSource: Crossref / CAD\'25\nAuthors: Daiki Koyama, Hiroaki Date, Satoshi Kanai\nPublished: 2025-5-9\nURL: https://doi.org/10.14733/cadconfp.2025.205-210\nDOI: 10.14733/cadconfp.2025.205-210\nSummary: No abstract/summary available.\n\n[7]\nTitle: Optimal Surface Fitting of Point Clouds Using Local Refinement\nSource: Crossref / SpringerBriefs in Earth System Sciences\nAuthors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken\nPublished: 2023\nURL: https://doi.org/10.1007/978-3-031-16954-0\nDOI: 10.1007/978-3-031-16954-0\nSummary: No abstract/summary available.\n\n[8]\nTitle: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\nSource: Crossref / Computer-Aided Design\nAuthors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov\nPublished: 2021-11\nURL: https://doi.org/10.1016/j.cad.2021.103090\nDOI: 10.1016/j.cad.2021.103090\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_d8f34cf2bed14d719dace290' is_error=False
content='Combined search results\n\nQuery: constructive solid geometry CSG reconstruction point clouds primitives\n\narXiv results for query: constructive solid geometry CSG reconstruction point clouds primitives\n\n[1]\nTitle: Point containment algorithms for constructive solid geometry with unbounded primitives\nSource: arXiv\nAuthors: Paul K. Romano, Patrick A. Myers, Seth R. Johnson, Aljaž Kolšek, Patrick C. Shriwise\nPublished: 2024-06-18T19:50:37Z\nURL: http://arxiv.org/abs/2406.13030v1\nSummary: We present several algorithms for evaluating point containment in constructive solid geometry (CSG) trees with unbounded primitives. Three algorithms are presented based on postfix, prefix, and infix notations of the CSG binary expression tree. We show that prefix and infix notations enable short-circuiting logic, which reduces the number of primitives that must be checked during point containment. To evaluate the performance of the algorithms, each algorithm was implemented in the OpenMC Monte Carlo particle transport code, which relies on CSG to represent solid bodies through which subatomic particles travel. Two sets of tests were carried out. First, the execution time to generate a high-resolution rasterized image of a 2D slice of a detailed CSG model of the ITER tokamak was measured. Use of both prefix and infix notations offered significant speedup over the postfix notation that has traditionally been used in particle transport codes, with infix resulting in a 6$\\times$ reduction in execution time relative to postfix. We then measured the execution time of neutron transport simulations of the same ITER model using each of the algorithms. The results and performance improvements reveal the same trends as for the rasterization test, with a 4.59$\\times$ overall speedup using the infix notation relative to the original postfix notation in OpenMC.\n\n[2]\nTitle: The CCube reconstruction algorithm for the SoLid experiment\nSource: arXiv\nAuthors: The SoLid collaboration\nPublished: 2024-04-04T16:42:41Z\nURL: http://arxiv.org/abs/2404.03580v5\nSummary: The SoLid experiment is a very-short-baseline experiment aimed at searching for nuclear reactor-produced active to sterile antineutrino oscillations. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$LiF:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented (the basic detection unit is a 5 cm side cube). High segmentation provides numerous advantages, including the precise location of Inverse Beta Decay (IBD) products, the derivation of the considerate antineutrino energy estimator, and a powerful background reduction tool based on the topological signature of the signal. Finally, the system is read out by a network of wavelength-shifting fibres coupled to a photodetector (MPPC). This paper describes the design of the reconstruction algorithm that allows maximum use of the granularity of the detector. The goal of the algorithm is to convert the output of the optical-fibre readout to the list of the detection units from which it originated. This paper provides a performance comparison for three methods and concludes with a choice of the baseline approach for the experiment.\n\n[3]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[4]\nTitle: UCSG-Net -- Unsupervised Discovering of Constructive Solid Geometry Tree\nSource: arXiv\nAuthors: Kacper Kania, Maciej Zięba, Tomasz Kajdanowicz\nPublished: 2020-06-16T12:13:37Z\nURL: http://arxiv.org/abs/2006.09102v3\nSummary: Signed distance field (SDF) is a prominent implicit representation of 3D meshes. Methods that are based on such representation achieved state-of-the-art 3D shape reconstruction quality. However, these methods struggle to reconstruct non-convex shapes. One remedy is to incorporate a constructive solid geometry framework (CSG) that represents a shape as a decomposition into primitives. It allows to embody a 3D shape of high complexity and non-convexity with a simple tree representation of Boolean operations. Nevertheless, existing approaches are supervised and require the entire CSG parse tree that is given upfront during the training process. On the contrary, we propose a model that extracts a CSG parse tree without any supervision - UCSG-Net. Our model predicts parameters of primitives and binarizes their SDF representation through differentiable indicator function. It is achieved jointly with discovering the structure of a Boolean operators tree. The model selects dynamically which operator combination over primitives leads to the reconstruction of high fidelity. We evaluate our method on 2D and 3D autoencoding tasks. We show that the predicted parse tree representation is interpretable and can be used in CAD software.\n\n[5]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[6]\nTitle: Electromagnetic energy calibration of the SoLid detector with horizontal muons\nSource: arXiv\nAuthors: SoLid collaboration\nPublished: 2025-07-07T16:35:32Z\nURL: http://arxiv.org/abs/2507.05180v4\nSummary: SoLid is a neutrino experiment at very-short baseline searching for active-to-sterile oscillations of reactor antineutrinos. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$Li:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented; the basic detection unit is a 5 cm cube. High segmentation provides numerous advantages including precise localisation of the Inverse Beta Decay (IBD) products, the derivation of an antineutrino energy estimator based on the isolated positron energy, and a powerful background reduction tool that relies on the topological signature of the signal. Finally, the system is read out by a network of WLS fibres coupled to photosensors. A relative electromagnetic calibration is performed with horizontal cosmic muons. This source poses the simplest calibration problem in which a single detection unit is involved. In addition, large muon energy deposits allow us to perform a calibration at the most detailed level (i.e. per fibre) and to accurately define the fraction of energy escaping to neighbouring detection cells. A statistical precision at the sub-percent level is reached. The paper also discusses two methods to calibrate the absolute energy scale. The first method relies on horizontal muons, though the precision is limited to around 10\\% because of the uncertainty in the energy distribution of such muons. A novel, alternative method based on the radioactive AmBe source is proposed. It takes advantage of the electron-positron pair-production process and provides a calibration point at 3.4 MeV (i.e. in the core of the IBD positron spectrum). The paper is concluded with various cross-check including a determination of the energy spectrum of the standard cosmogenic background candle: $^{12}$B.\n\n[7]\nTitle: Constructive Projective Geometry\nSource: arXiv\nAuthors: Mark Mandelkern\nPublished: 2024-02-01T03:29:31Z\nURL: http://arxiv.org/abs/2402.00301v1\nSummary: Of the great theories of classical mathematics, projective geometry, with its powerful concepts of symmetry and duality, has been exceptional in continuing to intrigue investigators. The challenge put forth by Errett Bishop (1928-1983), "Every theorem proved with nonconstructive methods presents a challenge: to find a constructive version, and to give it a constructive proof", motivates a large portion of current constructive work. This challenge can be answered by discovering the hidden constructive content of classical projective geometry. Here we briefly outline, with few details, recent constructive work on the real projective plane, and projective extensions of affine planes. Special note is taken of a number of interesting open problems that remain; these show that constructive projective geometry is still a theory very much in need of further effort. The Bishop-type constructive mathematics discussed in the present paper proceeds from a viewpoint well-nigh opposite that of either formal logic or recursive function theory.\n\n[8]\nTitle: D$^2$CSG: Unsupervised Learning of Compact CSG Trees with Dual Complements and Dropouts\nSource: arXiv\nAuthors: Fenggen Yu, Qimin Chen, Maham Tanveer, Ali Mahdavi Amiri, Hao Zhang\nPublished: 2023-01-27T02:13:14Z\nURL: http://arxiv.org/abs/2301.11497v2\nSummary: We present D$^2$CSG, a neural model composed of two dual and complementary network branches, with dropouts, for unsupervised learning of compact constructive solid geometry (CSG) representations of 3D CAD shapes. Our network is trained to reconstruct a 3D shape by a fixed-order assembly of quadric primitives, with both branches producing a union of primitive intersections or inverses. A key difference between D$^2$CSG and all prior neural CSG models is its dedicated residual branch to assemble the potentially complex shape complement, which is subtracted from an overall shape modeled by the cover branch. With the shape complements, our network is provably general, while the weight dropout further improves compactness of the CSG tree by removing redundant primitives. We demonstrate both quantitatively and qualitatively that D$^2$CSG produces compact CSG reconstructions with superior quality and more natural primitives than all existing alternatives, especially over complex and high-genus CAD shapes.\n\nCrossref results for query: constructive solid geometry CSG reconstruction point clouds primitives\n\n[1]\nTitle: Constructive Solid Geometry (CSG)\nSource: Crossref / Encyclopedia of Ocean Engineering\nAuthors: Unknown authors\nPublished: 2022\nURL: https://doi.org/10.1007/978-981-10-6946-8_300122\nDOI: 10.1007/978-981-10-6946-8_300122\nSummary: No abstract/summary available.\n\n[2]\nTitle: A Hybrid Approach for Segmenting and Fitting Solid Primitives to 3D Point Clouds\nSource: Crossref / Proceedings of the 15th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications\nAuthors: Markus Friedrich, Steffen Illium, Pierre-Alain Fayolle, Claudia Linnhoff-Popien\nPublished: 2020\nURL: https://doi.org/10.5220/0008870600380048\nDOI: 10.5220/0008870600380048\nSummary: No abstract/summary available.\n\n[3]\nTitle: Exploring Constructive Solid Geometry for Building Reconstruction from Point Clouds: Preliminary Results\nSource: Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences\nAuthors: Muataz S. A. Albadri, Patricia González-Cabaleiro, Antonio Fernández, Lucía Díaz-Vilariño\nPublished: 2025-9-18\nURL: https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-1-2025\nDOI: 10.5194/isprs-archives-xlviii-4-w15-2025-1-2025\nSummary: <jats:p>Abstract. As-built BIM reconstruction supports building digitalization, enabling efficient management and maintenance of existing buildings. Manual reconstruction from point clouds is both error-prone and cost-intensive, while automatic reconstruction remains challenging despite recent advancements. This paper explores the use of Constructive Solid Geometry (CSG) for automatically reconstructing IFC-compatible models from indoor point clouds of existing buildings. The proposed approach starts with segmented point clouds corresponding to rooms, doors, and windows, then CSG operations are used to reconstruct key building components as solids, including slabs, walls, doors, windows, and interior spaces. These solids are subsequently converted into corresponding IFC entities. The method is evaluated using two case studies, achieving a centimetre-level accuracy and a runtime of approximately 9 seconds per case study. The proposed method provides a promising ability to advance the Scan-to-BIM pipeline, as it enables accurate reconstruction of building components while preserving topological relationships during an efficient runtime. </jats:p>\n\n[4]\nTitle: Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds\nSource: Crossref / Crossref\nAuthors: yihang fu, jing li, Falai Chen\nPublished: 2026\nURL: https://doi.org/10.2139/ssrn.6172545\nDOI: 10.2139/ssrn.6172545\nSummary: <jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>\n\n[5]\nTitle: Integration of Constructive Solid Geometry and Boundary Representation (CSG-BRep) for 3D Modeling of Underground Cable Wells from Point Clouds\nSource: Crossref / Remote Sensing\nAuthors: Ming Huang, Xueyu Wu, Xianglei Liu, Tianhang Meng, Peiyuan Zhu\nPublished: 2020-5-4\nURL: https://doi.org/10.3390/rs12091452\nDOI: 10.3390/rs12091452\nSummary: <jats:p>The preference of three-dimensional representation of underground cable wells from two-dimensional symbols is a developing trend, and three-dimensional (3D) point cloud data is widely used due to its high precision. In this study, we utilize the characteristics of 3D terrestrial lidar point cloud data to build a CSG-BRep 3D model of underground cable wells, whose spatial topological relationship is fully considered. In order to simplify the modeling process, first, point cloud simplification is performed; then, the point cloud main axis is extracted by OBB bounding box, and lastly the point cloud orientation correction is realized by quaternion rotation. Furthermore, employing the adaptive method, the top point cloud is extracted, and it is projected for boundary extraction. Thereupon, utilizing the boundary information, we design the 3D cable well model. Finally, the cable well component model is generated by scanning the original point cloud. The experiments demonstrate that, along with the algorithm being fast, the proposed model is effective at displaying the 3D information of the actual cable wells and meets the current production demands.</jats:p>\n\n[6]\nTitle: A Modular Framework for Geometry-Aware Mesh Reconstruction from Sparse Point Clouds\nSource: Crossref / Crossref\nAuthors: Ying Chen, Hui Chen, Yuzhu Zhou, Lianyu Gao, Ying Hu\nPublished: 2025\nURL: https://doi.org/10.2139/ssrn.5258954\nDOI: 10.2139/ssrn.5258954\nSummary: No abstract/summary available.\n\n[7]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-3-31\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1\nDOI: 10.1109/tgrs.2025.3608325/v1/review1\nSummary: No abstract/summary available.\n\n[8]\nTitle: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"\nSource: Crossref / Crossref\nAuthors: Unknown authors\nPublished: 2025-4-16\nURL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2\nDOI: 10.1109/tgrs.2025.3608325/v1/review2\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_f6f71dd8ffbd4442a1be086c' is_error=False
content='Combined search results\n\nQuery: B-Rep topology graph recovery point clouds deep learning\n\narXiv results for query: B-Rep topology graph recovery point clouds deep learning\n\n[1]\nTitle: Learn to Accumulate Evidence from All Training Samples: Theory and Practice\nSource: arXiv\nAuthors: Deep Pandey, Qi Yu\nPublished: 2023-06-19T18:27:12Z\nURL: http://arxiv.org/abs/2306.11113v2\nSummary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.\n\n[2]\nTitle: The Modern Mathematics of Deep Learning\nSource: arXiv\nAuthors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen\nPublished: 2021-05-09T21:30:42Z\nURL: http://arxiv.org/abs/2105.04026v2\nSummary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.\n\n[3]\nTitle: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds\nSource: arXiv\nAuthors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer\nPublished: 2020-05-24T00:03:27Z\nURL: http://arxiv.org/abs/2005.11626v1\nSummary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.\n\n[4]\nTitle: Deep Learning and Computational Physics (Lecture Notes)\nSource: arXiv\nAuthors: Deep Ray, Orazio Pinti, Assad A. Oberai\nPublished: 2023-01-03T03:56:19Z\nURL: http://arxiv.org/abs/2301.00942v1\nSummary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.\n\n[5]\nTitle: Sequential Point Clouds: A Survey\nSource: arXiv\nAuthors: Haiyan Wang, Yingli Tian\nPublished: 2022-04-20T09:14:20Z\nURL: http://arxiv.org/abs/2204.09337v2\nSummary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \\& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.\n\n[6]\nTitle: A multitask deep learning model for real-time deployment in embedded systems\nSource: arXiv\nAuthors: Miquel Martí, Atsuto Maki\nPublished: 2017-10-31T23:59:23Z\nURL: http://arxiv.org/abs/1711.00146v1\nSummary: We propose an approach to Multitask Learning (MTL) to make deep learning models faster and lighter for applications in which multiple tasks need to be solved simultaneously, which is particularly useful in embedded, real-time systems. We develop a multitask model for both Object Detection and Semantic Segmentation and analyze the challenges that appear during its training. Our multitask network is 1.6x faster, lighter and uses less memory than deploying the single-task models in parallel. We conclude that MTL has the potential to give superior performance in exchange of a more complex training process that introduces challenges not present in single-task models.\n\n[7]\nTitle: Deep learning observables in computational fluid dynamics\nSource: arXiv\nAuthors: Kjetil O. Lye, Siddhartha Mishra, Deep Ray\nPublished: 2019-03-07T16:57:52Z\nURL: http://arxiv.org/abs/1903.03040v2\nSummary: Many large scale problems in computational fluid dynamics such as uncertainty quantification, Bayesian inversion, data assimilation and PDE constrained optimization are considered very challenging computationally as they require a large number of expensive (forward) numerical solutions of the corresponding PDEs. We propose a machine learning algorithm, based on deep artificial neural networks, that predicts the underlying \\emph{input parameters to observable} map from a few training samples (computed realizations of this map). By a judicious combination of theoretical arguments and empirical observations, we find suitable network architectures and training hyperparameters that result in robust and efficient neural network approximations of the parameters to observable map. Numerical experiments are presented to demonstrate low prediction errors for the trained network networks, even when the network has been trained with a few samples, at a computational cost which is several orders of magnitude lower than the underlying PDE solver. Moreover, we combine the proposed deep learning algorithm with Monte Carlo (MC) and Quasi-Monte Carlo (QMC) methods to efficiently compute uncertainty propagation for nonlinear PDEs. Under the assumption that the underlying neural networks generalize well, we prove that the deep learning MC and QMC algorithms are guaranteed to be faster than the baseline (quasi-) Monte Carlo methods. Numerical experiments demonstrating one to two orders of magnitude speed up over baseline QMC and MC algorithms, for the intricate problem of computing probability distributions of the observable, are also presented.\n\n[8]\nTitle: DILIE: Deep Internal Learning for Image Enhancement\nSource: arXiv\nAuthors: Indra Deep Mastan, Shanmuganathan Raman\nPublished: 2020-12-11T16:39:44Z\nURL: http://arxiv.org/abs/2012.06469v1\nSummary: We consider the generic deep image enhancement problem where an input image is transformed into a perceptually better-looking image. Recent methods for image enhancement consider the problem by performing style transfer and image restoration. The methods mostly fall into two categories: training data-based and training data-independent (deep internal learning methods). We perform image enhancement in the deep internal learning framework. Our Deep Internal Learning for Image Enhancement framework enhances content features and style features and uses contextual content loss for preserving image context in the enhanced image. We show results on both hazy and noisy image enhancement. To validate the results, we use structure similarity and perceptual error, which is efficient in measuring the unrealistic deformation present in the images. We show that the proposed framework outperforms the relevant state-of-the-art works for image enhancement.\n\nCrossref results for query: B-Rep topology graph recovery point clouds deep learning\n\n[1]\nTitle: Deep Unsupervised Learning of 3D Point Clouds via Graph Topology Inference and Filtering\nSource: Crossref / IEEE Transactions on Image Processing\nAuthors: Siheng Chen, Chaojing Duan, Yaoqing Yang, Duanshun Li, Chen Feng\nPublished: 2020\nURL: https://doi.org/10.1109/tip.2019.2957935\nDOI: 10.1109/tip.2019.2957935\nSummary: No abstract/summary available.\n\n[2]\nTitle: Learning Basics for 3D Point Clouds\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_2\nDOI: 10.1007/978-981-97-9570-3_2\nSummary: No abstract/summary available.\n\n[3]\nTitle: Deep-Learning-Based Point Cloud Analysis I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_5\nDOI: 10.1007/978-981-97-9570-3_5\nSummary: No abstract/summary available.\n\n[4]\nTitle: Deep-Learning-Based Point Cloud Analysis II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_6\nDOI: 10.1007/978-981-97-9570-3_6\nSummary: No abstract/summary available.\n\n[5]\nTitle: Deep-Learning-Based Point Cloud Enhancement II\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_4\nDOI: 10.1007/978-981-97-9570-3_4\nSummary: No abstract/summary available.\n\n[6]\nTitle: Deep-Learning-based Point Cloud Enhancement I\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_3\nDOI: 10.1007/978-981-97-9570-3_3\nSummary: No abstract/summary available.\n\n[7]\nTitle: Open-Source Projects for 3D Point Clouds\nSource: Crossref / Deep Learning for 3D Point Clouds\nAuthors: Wei Gao, Ge Li\nPublished: 2025\nURL: https://doi.org/10.1007/978-981-97-9570-3_9\nDOI: 10.1007/978-981-97-9570-3_9\nSummary: No abstract/summary available.\n\n[8]\nTitle: Deep Learning Architectures for 3D Point Clouds\nSource: Crossref / Proceedings of the 18th International Conference on Agents and Artificial Intelligence\nAuthors: Nour Neifar, Achraf Ben-Hamadou, Ahmed Rekik\nPublished: 2026\nURL: https://doi.org/10.5220/0014440900004052\nDOI: 10.5220/0014440900004052\nSummary: No abstract/summary available.' name='search_all_sources' call_id='call_5d59209b4efa4ccb84a34758' is_error=False
content='Fetched excerpt from https://doi.org/10.1016/j.cad.2021.103090:\nRedirecting var timerStart = Date.now(); var pageName = ""; if (pageName == "") { pageName = "Auto Article Locator"; } function autoRedirectToURL() { var url = \'/retrieve/\'+document.getElementById(\'resultName\').value+\'?Redirect=\'+document.getElementById(\'redirectURL\').value+\'&key=\'+document.getElementById(\'key\').value window.location = url; } siteCatalyst.pageDataLoad({ businessUnit : \'ELS:RP:ST\', environment : \'prod\', language : \'en\', loadTime : (Date.now() - timerStart).toString(), loadTimestamp : Date.now().toString(), name : pageName, productName : \'IH\', type : \'ih:article\', detail : \'sciencedirect\', format :"MIME-XHTML", accessType : \'ih:anon_guest\', ipAddress : \'67.209.191.166\', identifierType : \'PII\', identifierValue : \'S0010448521001019\', articleName : \'Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction\', location : "Linking Hub" });' name='fetch_webpage_excerpt' call_id='call_0a2a62c6754845f5b8dc37a3' is_error=False
content='Fetched excerpt from https://doi.org/10.1109/cvpr52733.2024.02624:\n(function(){ window.FPCS=!!window.FPCS;try{(function(){(function iS(){var I=!1;function l(I){for(var l=0;I--;)l+=z(document.documentElement,null);return l}function z(I,l){var s="vi";l=l||new Z;return jS(I,function(I){I.setAttribute("data-"+s,l._1());return z(I,l)},null)}function Z(){this.z_=1;this._S=0;this.ZO=this.z_;this.oZ=null;this._1=function(){this.oZ=this._S+this.ZO;if(!isFinite(this.oZ))return this.reset(),this._1();this._S=this.ZO;this.ZO=this.oZ;this.oZ=null;return this.ZO};this.reset=function(){this.z_++;this._S=0;this.ZO=this.z_}}var s=!1; function SS(I,l){var z=document.createElement(I);l=l||document.body;l.appendChild(z);z&&z.style&&(z.style.display="none")}function _S(l,z){z=z||l;var Z="|";function SS(I){I=I.split(Z);var l=[];for(var z=0;z Si&&(_(455)?6E5:491710)>S-_i)return o_(!1);var I=o_(Ii&&!ji&&_i+oi Si&&(_(803)?6E5:648862)>I-_i?l=o_(!1):(l=o_(Ii&&!ji&&_i+oi S}(function JI(I){return I?0:JI(I)*JI(I)})(!0);})();}catch(x){}finally{ie9rgb4=void(0);};function ie9rgb4(a,b){return a>>b>>0}; })(); var home = { metadata:{ searchCount: \'7,180,385\', logoRelPath: \'/xploreAssets/images/customer_logos/\', thirdParthAuth: false, currentPage: \'document\', xploreVirtual:\'https://ieeexplore.ieee.org\', isWebAccount: false, isProvisioned: false, globalNotification:{}, cart: { count: 0 } } }; PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds | IEEE Conference Publication | IEEE Xplore var googletag = googletag || {}; googletag.cmd = googletag.cmd || []; (function() { var gads = document.createElement(\'script\'); gads.async = true; gads.type = \'text/javascript\'; var useSSL = \'https:\' == document.location.protocol; gads.src = (useSSL ? \'https:\' : \'http:\') + \'//securepubads.g.doubleclick.net/tag/js/gpt.js\'; var node = document.getElementsByTagName(\'script\')[0]; node.parentNode.insertBefore(gads, node); })(); document.write(\' \'); var body_rightsLink ="", body_publisher = ""; var recordId = ""; var AUTHOR_PROFILE = \'ON\'; if (AUTHOR_PROFILE.toU' name='fetch_webpage_excerpt' call_id='call_3080290fa2014cebb412ee9b' is_error=False
```

### Message 10

- Source: `RetrievalAgent`
- Type: `ToolCallSummaryMessage`
- Summary: Combined search results

```text
Combined search results

Query: NURBS surface fitting point clouds reverse engineering constraints

arXiv results for query: NURBS surface fitting point clouds reverse engineering constraints

[1]
Title: Sequential Point Clouds: A Survey
Source: arXiv
Authors: Haiyan Wang, Yingli Tian
Published: 2022-04-20T09:14:20Z
URL: http://arxiv.org/abs/2204.09337v2
Summary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.

[2]
Title: Reverse Engineering Point Clouds to Fit Tensor Product B-Spline Surfaces by Blending Local Fits
Source: arXiv
Authors: Lavanya Sita Tekumalla, Elaine Cohen
Published: 2014-11-21T19:37:27Z
URL: http://arxiv.org/abs/1411.5993v1
Summary: Being able to reverse engineer from point cloud data to obtain 3D models is important in modeling. As our main contribution, we present a new method to obtain a tensor product B-spline representation from point cloud data by fitting surfaces to appropriately segmented data. By blending multiple local fits our method is more efficient than existing techniques, with the ability to deal with more detail by efficiently introducing a high number of knots. Further point cloud data obtained by digitizing 3D data, typically presents many associated complications like noise and missing data. As our second contribution, we propose an end-to-end framework for smoothing, hole filling, parameterization, knot selection and B-spline fitting that addresses these issues, works robustly with large irregularly shaped data containing holes and is straightforward to implement.

[3]
Title: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds
Source: arXiv
Authors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer
Published: 2020-05-24T00:03:27Z
URL: http://arxiv.org/abs/2005.11626v1
Summary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.

[4]
Title: Empirical Studies on Adversarial Reverse Engineering with Students
Source: arXiv
Authors: Tab, Zhang, Bjorn De Sutter, Christian Collberg, Bart Coppens
Published: 2026-03-04T09:27:46Z
URL: http://arxiv.org/abs/2603.03875v1
Summary: Empirical research in reverse engineering and software protection is crucial for evaluating the efficacy of methods designed to protect software against unauthorized access and tampering. However, conducting such studies with professional reverse engineers presents significant challenges, including access to professionals and affordability. This paper explores the use of students as participants in empirical reverse engineering experiments, examining their suitability and the necessary training; the design of appropriate challenges; strategies for ensuring the rigor and validity of the research and its results; ways to maintain students' privacy, motivation, and voluntary participation; and data collection methods. We present a systematic literature review of existing reverse engineering experiments and user studies, a discussion of related work from the broader domain of software engineering that applies to reverse engineering experiments, an extensive discussion of our own experience running experiments ourselves in the context of a master-level software hacking and protection course, and recommendations based on this experience. Our findings aim to guide future empirical studies in RE, balancing practical constraints with the need for meaningful, reproducible results.

[5]
Title: Non-Invasive Reverse Engineering of Finite State Machines Using Power Analysis and Boolean Satisfiability
Source: arXiv
Authors: Harsh Vamja, Richa Agrawal, Ranga Vemuri
Published: 2019-08-06T06:47:37Z
URL: http://arxiv.org/abs/1908.01979v1
Summary: In this paper, we present a non-invasive reverse engineering attack based on a novel approach that combines functional and power analysis to recover finite state machines from their synchronous sequential circuit implementations. The proposed technique formulates the machine exploration and state identification problem as a Boolean constraint satisfaction problem and solves it using a SMT (Satisfiability Modulo Theories) solver. It uses power measurements to achieve fast convergence. Experimental results using the LGSynth'91 benchmark suite show that the satisfiability-based approach is several times faster compared to existing techniques and can successfully recover 90%-100% of the transitions of a target machine.

[6]
Title: Algorithms for geometrical operations with NURBS surfaces
Source: arXiv
Authors: Gernot Beer
Published: 2022-10-24T12:23:57Z
URL: http://arxiv.org/abs/2210.13160v1
Summary: The aim of the paper is to show algorithms for geometrical manipulations on NURBS surfaces. These include generating NURBS surfaces that pass through given points, calculating the minimum distance to a point and include line to surface and surface to surface intersections.

[7]
Title: Morescient GAI for Software Engineering (Extended Version)
Source: arXiv
Authors: Marcus Kessel, Colin Atkinson
Published: 2024-06-07T07:38:33Z
URL: http://arxiv.org/abs/2406.04710v2
Summary: The ability of Generative AI (GAI) technology to automatically check, synthesize and modify software engineering artifacts promises to revolutionize all aspects of software engineering. Using GAI for software engineering tasks is consequently one of the most rapidly expanding fields of software engineering research, with over a hundred LLM-based code models having been published since 2021. However, the overwhelming majority of existing code models share a major weakness - they are exclusively trained on the syntactic facet of software, significantly lowering their trustworthiness in tasks dependent on software semantics. To address this problem, a new class of "Morescient" GAI is needed that is "aware" of (i.e., trained on) both the semantic and static facets of software. This, in turn, will require a new generation of software observation platforms capable of generating large quantities of execution observations in a structured and readily analyzable way. In this paper, we present a vision and roadmap for how such "Morescient" GAI models can be engineered, evolved and disseminated according to the principles of open science.

[8]
Title: Database Reverse Engineering based on Association Rule Mining
Source: arXiv
Authors: Nattapon Pannurat, Nittaya Kerdprasop, Kittisak Kerdprasop
Published: 2010-04-19T18:18:43Z
URL: http://arxiv.org/abs/1004.3272v1
Summary: Maintaining a legacy database is a difficult task especially when system documentation is poor written or even missing. Database reverse engineering is an attempt to recover high-level conceptual design from the existing database instances. In this paper, we propose a technique to discover conceptual schema using the association mining technique. The discovered schema corresponds to the normalization at the third normal form, which is a common practice in many business organizations. Our algorithm also includes the rule filtering heuristic to solve the problem of exponential growth of discovered rules inherited with the association mining technique.

Crossref results for query: NURBS surface fitting point clouds reverse engineering constraints

[1]
Title: NURBS-Based Surface Reconstruction from Point Clouds for Electromagnetic Target Modeling
Source: Crossref / 2025 Photonics &amp;amp; Electromagnetics Research Symposium - Fall (PIERS-Fall)
Authors: Qianyan Shen, Ruoming Zhang, Hai Lin
Published: 2025-11-4
URL: https://doi.org/10.23919/piers-fall62445.2025.11394360
DOI: 10.23919/piers-fall62445.2025.11394360
Summary: No abstract/summary available.

[2]
Title: NURBS surface fitting from scattered point cloud combining patch growing and PSO
Source: Crossref / Third International Computing Imaging Conference (CITA 2023)
Authors: Shangbo Gao, Chen Ma, Qingxin Yang, Yue Shen, Deming Kong
Published: 2023-11-6
URL: https://doi.org/10.1117/12.2691763
DOI: 10.1117/12.2691763
Summary: No abstract/summary available.

[3]
Title: MST Based Ordering of Point Clouds and Curve Fitting
Source: Crossref / Proceedings of the 21st International Conference on Computer Vision Theory and Applications
Authors: Christoph Dalitz, Alexander Jongbloed
Published: 2026
URL: https://doi.org/10.5220/0014152000004084
DOI: 10.5220/0014152000004084
Summary: No abstract/summary available.

[4]
Title: Reverse Engineering: Investigation of Optimization Techniques in Point Clouds Registration
Source: Crossref / SSRN Electronic Journal
Authors: George Yacout
Published: 2025
URL: https://doi.org/10.2139/ssrn.5297053
DOI: 10.2139/ssrn.5297053
Summary: No abstract/summary available.

[5]
Title: Adaptive Surface Fitting with Local Refinement: LR B-Spline Surfaces
Source: Crossref / SpringerBriefs in Earth System Sciences
Authors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken
Published: 2023
URL: https://doi.org/10.1007/978-3-031-16954-0_3
DOI: 10.1007/978-3-031-16954-0_3
Summary: <jats:title>Abstract</jats:title><jats:p>A locally refined (LR) B-spline surface is a piecewise polynomial surface for which the distribution of the surface coefficients can be locally adapted. Such a mathematical representation is interesting for fitting scattered and noisy data, as the local behaviour of a real point cloud may require more degrees of freedom only locally. The number of redundant surface coefficients is minimized, which avoids the fitting of the point cloud’s noise. The surface approximation is performed iteratively either by solving a least squares system or by a local approximation method. This procedure allows for mesh refinement in domains where the distance between a current surface and the point cloud exceeds a prescribed tolerance. In this way, parts of the LR B-spline surface obtained at previous steps may be kept unchanged. This chapter aims at explaining the adaptive fitting using local refinement with LR B-splines. We present two examples with simulated point clouds to illustrate the methodology.</jats:p>

[6]
Title: Application of Poisson Surface Reconstruction with Envelope Constraints to TLS Point Clouds of Scenes with Complex Objects
Source: Crossref / CAD'25
Authors: Daiki Koyama, Hiroaki Date, Satoshi Kanai
Published: 2025-5-9
URL: https://doi.org/10.14733/cadconfp.2025.205-210
DOI: 10.14733/cadconfp.2025.205-210
Summary: No abstract/summary available.

[7]
Title: Optimal Surface Fitting of Point Clouds Using Local Refinement
Source: Crossref / SpringerBriefs in Earth System Sciences
Authors: Gaël Kermarrec, Vibeke Skytt, Tor Dokken
Published: 2023
URL: https://doi.org/10.1007/978-3-031-16954-0
DOI: 10.1007/978-3-031-16954-0
Summary: No abstract/summary available.

[8]
Title: Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction
Source: Crossref / Computer-Aided Design
Authors: Guillaume Coiffier, Justine Basselin, Nicolas Ray, Dmitry Sokolov
Published: 2021-11
URL: https://doi.org/10.1016/j.cad.2021.103090
DOI: 10.1016/j.cad.2021.103090
Summary: No abstract/summary available.
Combined search results

Query: constructive solid geometry CSG reconstruction point clouds primitives

arXiv results for query: constructive solid geometry CSG reconstruction point clouds primitives

[1]
Title: Point containment algorithms for constructive solid geometry with unbounded primitives
Source: arXiv
Authors: Paul K. Romano, Patrick A. Myers, Seth R. Johnson, Aljaž Kolšek, Patrick C. Shriwise
Published: 2024-06-18T19:50:37Z
URL: http://arxiv.org/abs/2406.13030v1
Summary: We present several algorithms for evaluating point containment in constructive solid geometry (CSG) trees with unbounded primitives. Three algorithms are presented based on postfix, prefix, and infix notations of the CSG binary expression tree. We show that prefix and infix notations enable short-circuiting logic, which reduces the number of primitives that must be checked during point containment. To evaluate the performance of the algorithms, each algorithm was implemented in the OpenMC Monte Carlo particle transport code, which relies on CSG to represent solid bodies through which subatomic particles travel. Two sets of tests were carried out. First, the execution time to generate a high-resolution rasterized image of a 2D slice of a detailed CSG model of the ITER tokamak was measured. Use of both prefix and infix notations offered significant speedup over the postfix notation that has traditionally been used in particle transport codes, with infix resulting in a 6$\times$ reduction in execution time relative to postfix. We then measured the execution time of neutron transport simulations of the same ITER model using each of the algorithms. The results and performance improvements reveal the same trends as for the rasterization test, with a 4.59$\times$ overall speedup using the infix notation relative to the original postfix notation in OpenMC.

[2]
Title: The CCube reconstruction algorithm for the SoLid experiment
Source: arXiv
Authors: The SoLid collaboration
Published: 2024-04-04T16:42:41Z
URL: http://arxiv.org/abs/2404.03580v5
Summary: The SoLid experiment is a very-short-baseline experiment aimed at searching for nuclear reactor-produced active to sterile antineutrino oscillations. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$LiF:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented (the basic detection unit is a 5 cm side cube). High segmentation provides numerous advantages, including the precise location of Inverse Beta Decay (IBD) products, the derivation of the considerate antineutrino energy estimator, and a powerful background reduction tool based on the topological signature of the signal. Finally, the system is read out by a network of wavelength-shifting fibres coupled to a photodetector (MPPC). This paper describes the design of the reconstruction algorithm that allows maximum use of the granularity of the detector. The goal of the algorithm is to convert the output of the optical-fibre readout to the list of the detection units from which it originated. This paper provides a performance comparison for three methods and concludes with a choice of the baseline approach for the experiment.

[3]
Title: Sequential Point Clouds: A Survey
Source: arXiv
Authors: Haiyan Wang, Yingli Tian
Published: 2022-04-20T09:14:20Z
URL: http://arxiv.org/abs/2204.09337v2
Summary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.

[4]
Title: UCSG-Net -- Unsupervised Discovering of Constructive Solid Geometry Tree
Source: arXiv
Authors: Kacper Kania, Maciej Zięba, Tomasz Kajdanowicz
Published: 2020-06-16T12:13:37Z
URL: http://arxiv.org/abs/2006.09102v3
Summary: Signed distance field (SDF) is a prominent implicit representation of 3D meshes. Methods that are based on such representation achieved state-of-the-art 3D shape reconstruction quality. However, these methods struggle to reconstruct non-convex shapes. One remedy is to incorporate a constructive solid geometry framework (CSG) that represents a shape as a decomposition into primitives. It allows to embody a 3D shape of high complexity and non-convexity with a simple tree representation of Boolean operations. Nevertheless, existing approaches are supervised and require the entire CSG parse tree that is given upfront during the training process. On the contrary, we propose a model that extracts a CSG parse tree without any supervision - UCSG-Net. Our model predicts parameters of primitives and binarizes their SDF representation through differentiable indicator function. It is achieved jointly with discovering the structure of a Boolean operators tree. The model selects dynamically which operator combination over primitives leads to the reconstruction of high fidelity. We evaluate our method on 2D and 3D autoencoding tasks. We show that the predicted parse tree representation is interpretable and can be used in CAD software.

[5]
Title: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds
Source: arXiv
Authors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer
Published: 2020-05-24T00:03:27Z
URL: http://arxiv.org/abs/2005.11626v1
Summary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.

[6]
Title: Electromagnetic energy calibration of the SoLid detector with horizontal muons
Source: arXiv
Authors: SoLid collaboration
Published: 2025-07-07T16:35:32Z
URL: http://arxiv.org/abs/2507.05180v4
Summary: SoLid is a neutrino experiment at very-short baseline searching for active-to-sterile oscillations of reactor antineutrinos. The detection principle is based on the pairing of two types of solid scintillators: polyvinyl toluene and $^6$Li:ZnS(Ag), which is a new technology used in this field of Physics. In addition to good neutron-gamma discrimination, this setup allows the detector to be highly segmented; the basic detection unit is a 5 cm cube. High segmentation provides numerous advantages including precise localisation of the Inverse Beta Decay (IBD) products, the derivation of an antineutrino energy estimator based on the isolated positron energy, and a powerful background reduction tool that relies on the topological signature of the signal. Finally, the system is read out by a network of WLS fibres coupled to photosensors. A relative electromagnetic calibration is performed with horizontal cosmic muons. This source poses the simplest calibration problem in which a single detection unit is involved. In addition, large muon energy deposits allow us to perform a calibration at the most detailed level (i.e. per fibre) and to accurately define the fraction of energy escaping to neighbouring detection cells. A statistical precision at the sub-percent level is reached. The paper also discusses two methods to calibrate the absolute energy scale. The first method relies on horizontal muons, though the precision is limited to around 10\% because of the uncertainty in the energy distribution of such muons. A novel, alternative method based on the radioactive AmBe source is proposed. It takes advantage of the electron-positron pair-production process and provides a calibration point at 3.4 MeV (i.e. in the core of the IBD positron spectrum). The paper is concluded with various cross-check including a determination of the energy spectrum of the standard cosmogenic background candle: $^{12}$B.

[7]
Title: Constructive Projective Geometry
Source: arXiv
Authors: Mark Mandelkern
Published: 2024-02-01T03:29:31Z
URL: http://arxiv.org/abs/2402.00301v1
Summary: Of the great theories of classical mathematics, projective geometry, with its powerful concepts of symmetry and duality, has been exceptional in continuing to intrigue investigators. The challenge put forth by Errett Bishop (1928-1983), "Every theorem proved with nonconstructive methods presents a challenge: to find a constructive version, and to give it a constructive proof", motivates a large portion of current constructive work. This challenge can be answered by discovering the hidden constructive content of classical projective geometry. Here we briefly outline, with few details, recent constructive work on the real projective plane, and projective extensions of affine planes. Special note is taken of a number of interesting open problems that remain; these show that constructive projective geometry is still a theory very much in need of further effort. The Bishop-type constructive mathematics discussed in the present paper proceeds from a viewpoint well-nigh opposite that of either formal logic or recursive function theory.

[8]
Title: D$^2$CSG: Unsupervised Learning of Compact CSG Trees with Dual Complements and Dropouts
Source: arXiv
Authors: Fenggen Yu, Qimin Chen, Maham Tanveer, Ali Mahdavi Amiri, Hao Zhang
Published: 2023-01-27T02:13:14Z
URL: http://arxiv.org/abs/2301.11497v2
Summary: We present D$^2$CSG, a neural model composed of two dual and complementary network branches, with dropouts, for unsupervised learning of compact constructive solid geometry (CSG) representations of 3D CAD shapes. Our network is trained to reconstruct a 3D shape by a fixed-order assembly of quadric primitives, with both branches producing a union of primitive intersections or inverses. A key difference between D$^2$CSG and all prior neural CSG models is its dedicated residual branch to assemble the potentially complex shape complement, which is subtracted from an overall shape modeled by the cover branch. With the shape complements, our network is provably general, while the weight dropout further improves compactness of the CSG tree by removing redundant primitives. We demonstrate both quantitatively and qualitatively that D$^2$CSG produces compact CSG reconstructions with superior quality and more natural primitives than all existing alternatives, especially over complex and high-genus CAD shapes.

Crossref results for query: constructive solid geometry CSG reconstruction point clouds primitives

[1]
Title: Constructive Solid Geometry (CSG)
Source: Crossref / Encyclopedia of Ocean Engineering
Authors: Unknown authors
Published: 2022
URL: https://doi.org/10.1007/978-981-10-6946-8_300122
DOI: 10.1007/978-981-10-6946-8_300122
Summary: No abstract/summary available.

[2]
Title: A Hybrid Approach for Segmenting and Fitting Solid Primitives to 3D Point Clouds
Source: Crossref / Proceedings of the 15th International Joint Conference on Computer Vision, Imaging and Computer Graphics Theory and Applications
Authors: Markus Friedrich, Steffen Illium, Pierre-Alain Fayolle, Claudia Linnhoff-Popien
Published: 2020
URL: https://doi.org/10.5220/0008870600380048
DOI: 10.5220/0008870600380048
Summary: No abstract/summary available.

[3]
Title: Exploring Constructive Solid Geometry for Building Reconstruction from Point Clouds: Preliminary Results
Source: Crossref / The International Archives of the Photogrammetry, Remote Sensing and Spatial Information Sciences
Authors: Muataz S. A. Albadri, Patricia González-Cabaleiro, Antonio Fernández, Lucía Díaz-Vilariño
Published: 2025-9-18
URL: https://doi.org/10.5194/isprs-archives-xlviii-4-w15-2025-1-2025
DOI: 10.5194/isprs-archives-xlviii-4-w15-2025-1-2025
Summary: <jats:p>Abstract. As-built BIM reconstruction supports building digitalization, enabling efficient management and maintenance of existing buildings. Manual reconstruction from point clouds is both error-prone and cost-intensive, while automatic reconstruction remains challenging despite recent advancements. This paper explores the use of Constructive Solid Geometry (CSG) for automatically reconstructing IFC-compatible models from indoor point clouds of existing buildings. The proposed approach starts with segmented point clouds corresponding to rooms, doors, and windows, then CSG operations are used to reconstruct key building components as solids, including slabs, walls, doors, windows, and interior spaces. These solids are subsequently converted into corresponding IFC entities. The method is evaluated using two case studies, achieving a centimetre-level accuracy and a runtime of approximately 9 seconds per case study. The proposed method provides a promising ability to advance the Scan-to-BIM pipeline, as it enables accurate reconstruction of building components while preserving topological relationships during an efficient runtime. </jats:p>

[4]
Title: Point2Brep: Geometry-Aware B-rep Reconstruction from Point Clouds
Source: Crossref / Crossref
Authors: yihang fu, jing li, Falai Chen
Published: 2026
URL: https://doi.org/10.2139/ssrn.6172545
DOI: 10.2139/ssrn.6172545
Summary: <jats:p>Reconstructing accurate boundary representations (B-reps) from unstructured point clouds remains challenging due to measurement noise and the intrinsic geometric and topological complexity of B-rep models. We present Point2Brep, a geometry-aware framework that reconstructs complete and topologically consistent B-rep models by tightly integrating learning-based inference with explicit parametric modeling and geometric reasoning. Point2Brep follows a two-stage pipeline. First, it segments noisy point clouds into surface patches via learning-guided region growing, prioritizing high-confidence interior points to fit reliable parametric surfaces. Second, conditioned on the reconstructed surfaces, Point2Brep predicts continuous geometric distance fields that encode spatial proximity to B-rep edges and vertices. These fields are subsequently resolved through explicit geometric reasoning to recover edge curves, vertex locations, and their connectivity. Extensive experiments demonstrate that Point2Brep significantly outperforms existing methods in both geometric accuracy and topological consistency.</jats:p>

[5]
Title: Integration of Constructive Solid Geometry and Boundary Representation (CSG-BRep) for 3D Modeling of Underground Cable Wells from Point Clouds
Source: Crossref / Remote Sensing
Authors: Ming Huang, Xueyu Wu, Xianglei Liu, Tianhang Meng, Peiyuan Zhu
Published: 2020-5-4
URL: https://doi.org/10.3390/rs12091452
DOI: 10.3390/rs12091452
Summary: <jats:p>The preference of three-dimensional representation of underground cable wells from two-dimensional symbols is a developing trend, and three-dimensional (3D) point cloud data is widely used due to its high precision. In this study, we utilize the characteristics of 3D terrestrial lidar point cloud data to build a CSG-BRep 3D model of underground cable wells, whose spatial topological relationship is fully considered. In order to simplify the modeling process, first, point cloud simplification is performed; then, the point cloud main axis is extracted by OBB bounding box, and lastly the point cloud orientation correction is realized by quaternion rotation. Furthermore, employing the adaptive method, the top point cloud is extracted, and it is projected for boundary extraction. Thereupon, utilizing the boundary information, we design the 3D cable well model. Finally, the cable well component model is generated by scanning the original point cloud. The experiments demonstrate that, along with the algorithm being fast, the proposed model is effective at displaying the 3D information of the actual cable wells and meets the current production demands.</jats:p>

[6]
Title: A Modular Framework for Geometry-Aware Mesh Reconstruction from Sparse Point Clouds
Source: Crossref / Crossref
Authors: Ying Chen, Hui Chen, Yuzhu Zhou, Lianyu Gao, Ying Hu
Published: 2025
URL: https://doi.org/10.2139/ssrn.5258954
DOI: 10.2139/ssrn.5258954
Summary: No abstract/summary available.

[7]
Title: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"
Source: Crossref / Crossref
Authors: Unknown authors
Published: 2025-3-31
URL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review1
DOI: 10.1109/tgrs.2025.3608325/v1/review1
Summary: No abstract/summary available.

[8]
Title: Review for "AdLeaf: Quantitative leaf reconstruction from TLS point clouds"
Source: Crossref / Crossref
Authors: Unknown authors
Published: 2025-4-16
URL: https://doi.org/10.1109/tgrs.2025.3608325/v1/review2
DOI: 10.1109/tgrs.2025.3608325/v1/review2
Summary: No abstract/summary available.
Combined search results

Query: B-Rep topology graph recovery point clouds deep learning

arXiv results for query: B-Rep topology graph recovery point clouds deep learning

[1]
Title: Learn to Accumulate Evidence from All Training Samples: Theory and Practice
Source: arXiv
Authors: Deep Pandey, Qi Yu
Published: 2023-06-19T18:27:12Z
URL: http://arxiv.org/abs/2306.11113v2
Summary: Evidential deep learning, built upon belief theory and subjective logic, offers a principled and computationally efficient way to turn a deterministic neural network uncertainty-aware. The resultant evidential models can quantify fine-grained uncertainty using the learned evidence. To ensure theoretically sound evidential models, the evidence needs to be non-negative, which requires special activation functions for model training and inference. This constraint often leads to inferior predictive performance compared to standard softmax models, making it challenging to extend them to many large-scale datasets. To unveil the real cause of this undesired behavior, we theoretically investigate evidential models and identify a fundamental limitation that explains the inferior performance: existing evidential activation functions create zero evidence regions, which prevent the model to learn from training samples falling into such regions. A deeper analysis of evidential activation functions based on our theoretical underpinning inspires the design of a novel regularizer that effectively alleviates this fundamental limitation. Extensive experiments over many challenging real-world datasets and settings confirm our theoretical findings and demonstrate the effectiveness of our proposed approach.

[2]
Title: The Modern Mathematics of Deep Learning
Source: arXiv
Authors: Julius Berner, Philipp Grohs, Gitta Kutyniok, Philipp Petersen
Published: 2021-05-09T21:30:42Z
URL: http://arxiv.org/abs/2105.04026v2
Summary: We describe the new field of mathematical analysis of deep learning. This field emerged around a list of research questions that were not answered within the classical framework of learning theory. These questions concern: the outstanding generalization power of overparametrized neural networks, the role of depth in deep architectures, the apparent absence of the curse of dimensionality, the surprisingly successful optimization performance despite the non-convexity of the problem, understanding what features are learned, why deep architectures perform exceptionally well in physical problems, and which fine aspects of an architecture affect the behavior of a learning task in which way. We present an overview of modern approaches that yield partial answers to these questions. For selected approaches, we describe the main ideas in more detail.

[3]
Title: ShapeAdv: Generating Shape-Aware Adversarial 3D Point Clouds
Source: arXiv
Authors: Kibok Lee, Zhuoyuan Chen, Xinchen Yan, Raquel Urtasun, Ersin Yumer
Published: 2020-05-24T00:03:27Z
URL: http://arxiv.org/abs/2005.11626v1
Summary: We introduce ShapeAdv, a novel framework to study shape-aware adversarial perturbations that reflect the underlying shape variations (e.g., geometric deformations and structural differences) in the 3D point cloud space. We develop shape-aware adversarial 3D point cloud attacks by leveraging the learned latent space of a point cloud auto-encoder where the adversarial noise is applied in the latent space. Specifically, we propose three different variants including an exemplar-based one by guiding the shape deformation with auxiliary data, such that the generated point cloud resembles the shape morphing between objects in the same category. Different from prior works, the resulting adversarial 3D point clouds reflect the shape variations in the 3D point cloud space while still being close to the original one. In addition, experimental evaluations on the ModelNet40 benchmark demonstrate that our adversaries are more difficult to defend with existing point cloud defense methods and exhibit a higher attack transferability across classifiers. Our shape-aware adversarial attacks are orthogonal to existing point cloud based attacks and shed light on the vulnerability of 3D deep neural networks.

[4]
Title: Deep Learning and Computational Physics (Lecture Notes)
Source: arXiv
Authors: Deep Ray, Orazio Pinti, Assad A. Oberai
Published: 2023-01-03T03:56:19Z
URL: http://arxiv.org/abs/2301.00942v1
Summary: These notes were compiled as lecture notes for a course developed and taught at the University of the Southern California. They should be accessible to a typical engineering graduate student with a strong background in Applied Mathematics. The main objective of these notes is to introduce a student who is familiar with concepts in linear algebra and partial differential equations to select topics in deep learning. These lecture notes exploit the strong connections between deep learning algorithms and the more conventional techniques of computational physics to achieve two goals. First, they use concepts from computational physics to develop an understanding of deep learning algorithms. Not surprisingly, many concepts in deep learning can be connected to similar concepts in computational physics, and one can utilize this connection to better understand these algorithms. Second, several novel deep learning algorithms can be used to solve challenging problems in computational physics. Thus, they offer someone who is interested in modeling a physical phenomena with a complementary set of tools.

[5]
Title: Sequential Point Clouds: A Survey
Source: arXiv
Authors: Haiyan Wang, Yingli Tian
Published: 2022-04-20T09:14:20Z
URL: http://arxiv.org/abs/2204.09337v2
Summary: Point cloud has drawn more and more research attention as well as real-world applications. However, many of these applications (e.g. autonomous driving and robotic manipulation) are actually based on sequential point clouds (i.e. four dimensions) because the information of the static point cloud data could provide is still limited. Recently, researchers put more and more effort into sequential point clouds. This paper presents an extensive review of the deep learning-based methods for sequential point cloud research including dynamic flow estimation, object detection \& tracking, point cloud segmentation, and point cloud forecasting. This paper further summarizes and compares the quantitative results of the reviewed methods over the public benchmark datasets. Finally, this paper is concluded by discussing the challenges in the current sequential point cloud research and pointing out insightful potential future research directions.

[6]
Title: A multitask deep learning model for real-time deployment in embedded systems
Source: arXiv
Authors: Miquel Martí, Atsuto Maki
Published: 2017-10-31T23:59:23Z
URL: http://arxiv.org/abs/1711.00146v1
Summary: We propose an approach to Multitask Learning (MTL) to make deep learning models faster and lighter for applications in which multiple tasks need to be solved simultaneously, which is particularly useful in embedded, real-time systems. We develop a multitask model for both Object Detection and Semantic Segmentation and analyze the challenges that appear during its training. Our multitask network is 1.6x faster, lighter and uses less memory than deploying the single-task models in parallel. We conclude that MTL has the potential to give superior performance in exchange of a more complex training process that introduces challenges not present in single-task models.

[7]
Title: Deep learning observables in computational fluid dynamics
Source: arXiv
Authors: Kjetil O. Lye, Siddhartha Mishra, Deep Ray
Published: 2019-03-07T16:57:52Z
URL: http://arxiv.org/abs/1903.03040v2
Summary: Many large scale problems in computational fluid dynamics such as uncertainty quantification, Bayesian inversion, data assimilation and PDE constrained optimization are considered very challenging computationally as they require a large number of expensive (forward) numerical solutions of the corresponding PDEs. We propose a machine learning algorithm, based on deep artificial neural networks, that predicts the underlying \emph{input parameters to observable} map from a few training samples (computed realizations of this map). By a judicious combination of theoretical arguments and empirical observations, we find suitable network architectures and training hyperparameters that result in robust and efficient neural network approximations of the parameters to observable map. Numerical experiments are presented to demonstrate low prediction errors for the trained network networks, even when the network has been trained with a few samples, at a computational cost which is several orders of magnitude lower than the underlying PDE solver. Moreover, we combine the proposed deep learning algorithm with Monte Carlo (MC) and Quasi-Monte Carlo (QMC) methods to efficiently compute uncertainty propagation for nonlinear PDEs. Under the assumption that the underlying neural networks generalize well, we prove that the deep learning MC and QMC algorithms are guaranteed to be faster than the baseline (quasi-) Monte Carlo methods. Numerical experiments demonstrating one to two orders of magnitude speed up over baseline QMC and MC algorithms, for the intricate problem of computing probability distributions of the observable, are also presented.

[8]
Title: DILIE: Deep Internal Learning for Image Enhancement
Source: arXiv
Authors: Indra Deep Mastan, Shanmuganathan Raman
Published: 2020-12-11T16:39:44Z
URL: http://arxiv.org/abs/2012.06469v1
Summary: We consider the generic deep image enhancement problem where an input image is transformed into a perceptually better-looking image. Recent methods for image enhancement consider the problem by performing style transfer and image restoration. The methods mostly fall into two categories: training data-based and training data-independent (deep internal learning methods). We perform image enhancement in the deep internal learning framework. Our Deep Internal Learning for Image Enhancement framework enhances content features and style features and uses contextual content loss for preserving image context in the enhanced image. We show results on both hazy and noisy image enhancement. To validate the results, we use structure similarity and perceptual error, which is efficient in measuring the unrealistic deformation present in the images. We show that the proposed framework outperforms the relevant state-of-the-art works for image enhancement.

Crossref results for query: B-Rep topology graph recovery point clouds deep learning

[1]
Title: Deep Unsupervised Learning of 3D Point Clouds via Graph Topology Inference and Filtering
Source: Crossref / IEEE Transactions on Image Processing
Authors: Siheng Chen, Chaojing Duan, Yaoqing Yang, Duanshun Li, Chen Feng
Published: 2020
URL: https://doi.org/10.1109/tip.2019.2957935
DOI: 10.1109/tip.2019.2957935
Summary: No abstract/summary available.

[2]
Title: Learning Basics for 3D Point Clouds
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_2
DOI: 10.1007/978-981-97-9570-3_2
Summary: No abstract/summary available.

[3]
Title: Deep-Learning-Based Point Cloud Analysis I
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_5
DOI: 10.1007/978-981-97-9570-3_5
Summary: No abstract/summary available.

[4]
Title: Deep-Learning-Based Point Cloud Analysis II
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_6
DOI: 10.1007/978-981-97-9570-3_6
Summary: No abstract/summary available.

[5]
Title: Deep-Learning-Based Point Cloud Enhancement II
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_4
DOI: 10.1007/978-981-97-9570-3_4
Summary: No abstract/summary available.

[6]
Title: Deep-Learning-based Point Cloud Enhancement I
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_3
DOI: 10.1007/978-981-97-9570-3_3
Summary: No abstract/summary available.

[7]
Title: Open-Source Projects for 3D Point Clouds
Source: Crossref / Deep Learning for 3D Point Clouds
Authors: Wei Gao, Ge Li
Published: 2025
URL: https://doi.org/10.1007/978-981-97-9570-3_9
DOI: 10.1007/978-981-97-9570-3_9
Summary: No abstract/summary available.

[8]
Title: Deep Learning Architectures for 3D Point Clouds
Source: Crossref / Proceedings of the 18th International Conference on Agents and Artificial Intelligence
Authors: Nour Neifar, Achraf Ben-Hamadou, Ahmed Rekik
Published: 2026
URL: https://doi.org/10.5220/0014440900004052
DOI: 10.5220/0014440900004052
Summary: No abstract/summary available.
Fetched excerpt from https://doi.org/10.1016/j.cad.2021.103090:
Redirecting var timerStart = Date.now(); var pageName = ""; if (pageName == "") { pageName = "Auto Article Locator"; } function autoRedirectToURL() { var url = '/retrieve/'+document.getElementById('resultName').value+'?Redirect='+document.getElementById('redirectURL').value+'&key='+document.getElementById('key').value window.location = url; } siteCatalyst.pageDataLoad({ businessUnit : 'ELS:RP:ST', environment : 'prod', language : 'en', loadTime : (Date.now() - timerStart).toString(), loadTimestamp : Date.now().toString(), name : pageName, productName : 'IH', type : 'ih:article', detail : 'sciencedirect', format :"MIME-XHTML", accessType : 'ih:anon_guest', ipAddress : '67.209.191.166', identifierType : 'PII', identifierValue : 'S0010448521001019', articleName : 'Parametric Surface Fitting on Airborne Lidar Point Clouds for Building Reconstruction', location : "Linking Hub" });
Fetched excerpt from https://doi.org/10.1109/cvpr52733.2024.02624:
(function(){ window.FPCS=!!window.FPCS;try{(function(){(function iS(){var I=!1;function l(I){for(var l=0;I--;)l+=z(document.documentElement,null);return l}function z(I,l){var s="vi";l=l||new Z;return jS(I,function(I){I.setAttribute("data-"+s,l._1());return z(I,l)},null)}function Z(){this.z_=1;this._S=0;this.ZO=this.z_;this.oZ=null;this._1=function(){this.oZ=this._S+this.ZO;if(!isFinite(this.oZ))return this.reset(),this._1();this._S=this.ZO;this.ZO=this.oZ;this.oZ=null;return this.ZO};this.reset=function(){this.z_++;this._S=0;this.ZO=this.z_}}var s=!1; function SS(I,l){var z=document.createElement(I);l=l||document.body;l.appendChild(z);z&&z.style&&(z.style.display="none")}function _S(l,z){z=z||l;var Z="|";function SS(I){I=I.split(Z);var l=[];for(var z=0;z Si&&(_(455)?6E5:491710)>S-_i)return o_(!1);var I=o_(Ii&&!ji&&_i+oi Si&&(_(803)?6E5:648862)>I-_i?l=o_(!1):(l=o_(Ii&&!ji&&_i+oi S}(function JI(I){return I?0:JI(I)*JI(I)})(!0);})();}catch(x){}finally{ie9rgb4=void(0);};function ie9rgb4(a,b){return a>>b>>0}; })(); var home = { metadata:{ searchCount: '7,180,385', logoRelPath: '/xploreAssets/images/customer_logos/', thirdParthAuth: false, currentPage: 'document', xploreVirtual:'https://ieeexplore.ieee.org', isWebAccount: false, isProvisioned: false, globalNotification:{}, cart: { count: 0 } } }; PBWR: Parametric-Building-Wireframe Reconstruction from Aerial LiDAR Point Clouds | IEEE Conference Publication | IEEE Xplore var googletag = googletag || {}; googletag.cmd = googletag.cmd || []; (function() { var gads = document.createElement('script'); gads.async = true; gads.type = 'text/javascript'; var useSSL = 'https:' == document.location.protocol; gads.src = (useSSL ? 'https:' : 'http:') + '//securepubads.g.doubleclick.net/tag/js/gpt.js'; var node = document.getElementsByTagName('script')[0]; node.parentNode.insertBefore(gads, node); })(); document.write(' '); var body_rightsLink ="", body_publisher = ""; var recordId = ""; var AUTHOR_PROFILE = 'ON'; if (AUTHOR_PROFILE.toU
```

### Message 11

- Source: `ReviewerAgent`
- Type: `TextMessage`
- Summary: Structured review decision: REVISE, total_score=8

```text
{
  "decision": "REVISE",
  "review_summary": "The retrieval successfully identified several high-impact papers (ComplexGen, D^2CSG, UCSG-Net, Point2Brep) that strongly align with the B-rep and CSG reconstruction topics. However, critical papers matching the 'parametric surface' and 'topology recovery' constraints—specifically Coiffier et al. (2021) on Parametric Surface Fitting and Huang et al. (2024) on Parametric-Building-Wireframe Reconstruction—failed to return abstracts, providing only HTML/redirect scripts. This lack of evidence quality for key parametric methods, combined with the questionable 2026 date for Point2Brep, renders the current output insufficient for a high-quality report.",
  "scores": {
    "coverage_score": 2,
    "relevance_score": 2,
    "metadata_score": 1,
    "diversity_score": 2,
    "evidence_score": 1
  },
  "hard_requirements": {
    "source_coverage": {
      "passed": true,
      "reason": "Both arXiv and Crossref (including IEEE, Elsevier, Springer) were used."
    },
    "candidate_depth": {
      "passed": true,
      "reason": "Identified >5 distinct candidates including ComplexGen, D^2CSG, UCSG-Net, Coiffier, and Huang."
    },
    "relevance": {
      "passed": true,
      "reason": "Top candidates (D^2CSG, UCSG-Net, Point2Brep) are directly relevant to B-rep/CSG reconstruction."
    },
    "metadata": {
      "passed": false,
      "reason": "Several high-relevance papers (Coiffier 2021, Huang 2024, Gao 2023) are missing abstracts due to fetching errors."
    },
    "query_fit": {
      "passed": true,
      "reason": "The mix of papers covers Deep Learning (ComplexGen), CSG (D^2CSG), and Parametric/Building topics (Coiffier, Huang)."
    },
    "gaps": {
      "passed": false,
      "reason": "While titles suggest coverage of parametric surface fitting, the missing abstracts for Coiffier and Huang create a verification gap in this sub-area."
    }
  },
  "key_risks": [
    "Missing Abstracts: Critical papers on parametric fitting and wireframes are unusable for content generation.",
    "Future Date: Point2Brep is dated 2026, which may be an error or 'in-press', requiring verification.",
    "Verification Gap: Cannot confirm if 'Topology-Aware' or 'Hybrid Approach' papers produce B-reps vs. meshes without text."
  ],
  "next_actions": [
    "Retry fetching abstracts for Coiffier (DOI: 10.1016/j.cad.2021.103090) and Huang/PBWR (DOI: 10.1109/cvpr52733.2024.02624) using text-mode extraction.",
    "Verify the publication date and status of Point2Brep (SSRN: 10.2139/ssrn.6172545).",
    "Attempt to retrieve abstract for 'A Hybrid Approach for Segmenting and Fitting Solid Primitives' (DOI: 10.5220/0008870600380048) to confirm B-rep output.",
    "Filter out 'Sequential Point Clouds: A Survey' and 'ShapeAdv' if they appear in the final set."
  ]
}
```

### Message 12

- Source: `WriterAgent`
- Type: `TextMessage`
- Summary: # Paper Search Report

```text
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
```
