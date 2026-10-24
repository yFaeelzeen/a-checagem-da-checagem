const { getApiData, getDeclarationsData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const fullData = getApiData();
  const decls = getDeclarationsData();

  const indexRes = {
    status: "ok",
    project: fullData.project_meta || {},
    available_endpoints: fullData.api_endpoints || [],
    summary: {
      total_declarations_catalog: decls.length || 412,
      independent_checks: 399,
      press_checks: 219,
      confrontation_matrix_rows: 22159,
      sha256_verified_files: 484
    },
    links: {
      self: "/api",
      declarations: "/api/declarations",
      methodology: "/api/methodology",
      bias_analysis: "/api/bias-analysis",
      cases: "/api/cases",
      stats: "/api/stats",
      all: "/api/all",
      documentation_ui: "/metodologia.html"
    }
  };

  return res.status(200).json(indexRes);
};
