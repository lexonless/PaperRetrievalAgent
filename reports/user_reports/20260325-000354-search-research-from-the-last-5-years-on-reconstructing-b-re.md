# Paper Search Report

**Query:** Search research from the last 5 years on reconstructing B-rep models from point clouds.

Focus on papers related to generating, reconstructing, or recovering B-rep or CAD boundary representations from point clouds.

Prioritize papers where point clouds are the main input and B-rep is the target output, but also include closely related papers if they make a substantial contribution to the overall point-cloud-to-B-rep reconstruction problem.

Exclude papers that are clearly unrelated to B-rep or CAD reconstruction from point clouds.

Return 5-10 relevant papers with:
- title
- year
- source
- link
- core contribution
- relevance note explaining whether the paper is a direct match or a closely related paper, and why

Then summarize:
- major method categories
- recent trends
- open challenges

Rank the most directly relevant papers first, but do not over-filter papers merely because they use multi-stage pipelines or different wording for the same task.
**Generated At:** 2026-03-25T00:03:54
**Stop Reason:** Maximum number of messages 20 reached, current message count: 20

## Final Response

{
  "topic": "B-rep reconstruction from point clouds",
  "user_intent": "Find recent research on methods to reconstruct or generate Boundary Representation (B-rep) CAD models directly from point cloud data, with a focus on direct approaches and substantial contributions to the overall problem.",
  "time_range": {
    "start_year": 2022,
    "end_year": 2026,
    "is_explicit": true,
    "original_expression": "last 5 years",
    "resolution_basis_date": "2026-03-24",
    "resolved_by_rule": "inclusive relative-year rule"
  },
  "focus_areas": ["B-rep reconstruction from point clouds", "point cloud to CAD", "boundary representation generation", "geometric deep learning for CAD", "reverse engineering from scans"],
  "exclude_areas": ["papers unrelated to B-rep or CAD output", "papers where point cloud is not the primary input", "pure mesh or surface reconstruction without B-rep intent", "crack path reconstruction", "general point cloud pre-training", "BIM generation without explicit B-rep focus"],
  "fallback_queries": ["point cloud to CAD reconstruction", "B-rep generation from 3D scans", "reverse engineering CAD from point clouds"],
  "queries": [
    {
      "query": "point cloud to CAD reconstruction B-rep",
      "reason": "Combines core terms to directly target the user's topic, excluding unrelated areas like crack paths or pre-training."
    },
    {
      "query": "reverse engineering B-rep from point cloud",
      "reason": "Uses traditional terminology to capture optimization and fitting-based methods that may not appear in deep learning queries."
    },
    {
      "query": "boundary representation generation point cloud deep learning",
      "reason": "Focuses on recent learning-based approaches, a key trend within the time range."
    }
  ],
  "assumptions": ["The term 'B-rep' is used interchangeably with 'boundary representation' in CAD literature.", "Papers on 'CAD reconstruction from scans' are relevant if they produce a B-rep model.", "Multi-stage pipelines (e.g., point cloud -> mesh -> B-rep) are included if the final output is a B-rep.", "We are broadening the search slightly to ensure sufficient core candidates, but will filter for direct relevance based on abstracts."],
  "success_criteria": ["Retrieve at least 5-8 distinct, directly relevant papers where point cloud is the primary input and B-rep/CAD is the explicit output.", "Exclude papers not about CAD/B-rep reconstruction (e.g., crack paths, general pre-training).", "Identify major methodological categories (e.g., optimization-based, learning-based, hybrid) from the relevant set."]
}
