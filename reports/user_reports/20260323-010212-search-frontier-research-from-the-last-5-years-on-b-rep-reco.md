# Paper Search Report

**Query:** Search frontier research from the last 5 years on B-rep reconstruction from point clouds.
Focus on point-cloud-to-CAD/B-rep methods, parametric surface reconstruction, topology recovery, and geometry-constrained modeling.
Exclude mesh-only reconstruction methods that do not produce B-rep or CAD representations.
Return 5-10 highly relevant papers with title, year, source, link, core contribution, and relevance note.
Then summarize method categories, recent trends, and open challenges.
**Generated At:** 2026-03-23T01:02:12
**Stop Reason:** Maximum number of messages 20 reached, current message count: 20

## Final Response

{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Identify frontier research from 2022-2026 on converting raw 3D point clouds directly into Boundary Representation (B-rep) or CAD models, focusing on parametric surfaces, topology recovery, and geometry-constrained modeling.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-23",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": [
    "point-cloud-to-CAD/B-rep methods",
    "parametric surface reconstruction",
    "topology recovery",
    "geometry-constrained modeling"
  ],
  "exclude_areas": [
    "mesh-only reconstruction",
    "non-parametric point cloud processing without CAD output"
  ],
  "queries": [
    {
      "query": "\"B-rep reconstruction\" point cloud",
      "reason": "Targets literature explicitly using the Boundary Representation term, ensuring high relevance to the core topic.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    },
    {
      "query": "\"parametric surface reconstruction\" point cloud CAD",
      "reason": "Focuses on the geometric fitting aspect of generating CAD geometry (primitives, NURBS, planes) from unstructured points.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    },
    {
      "query": "\"point cloud\" topology recovery CAD",
      "reason": "Aims to find methods solving the topological inference problem (connectivity, face adjacency) required for valid solid/B-rep models.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    },
    {
      "query": "\"reverse engineering\" point cloud CAD model",
      "reason": "Broadens the search to include industrial reverse engineering terminology often used in applied CAD reconstruction contexts.",
      "sources": [
        "arXiv",
        "Crossref"
      ]
    }
  ],
  "assumptions": [
    "The term 'CAD reconstruction' is often used interchangeably with 'B-rep reconstruction' in recent literature.",
    "Deep learning approaches likely dominate the 'frontier', but geometric/optimization methods are still relevant for constraints.",
    "Excluding 'mesh-only' requires verifying that the output includes B-rep, solid, or parametric features (sketches, extrusions) rather than just polygonal meshes."
  ],
  "success_criteria": [
    "5-10 highly relevant papers identified within the 2022-2026 window.",
    "Selected papers cover both parametric surface fitting and topology recovery.",
    "Papers explicitly produce B-rep, CAD, or solid representations rather than just meshes."
  ]
}
