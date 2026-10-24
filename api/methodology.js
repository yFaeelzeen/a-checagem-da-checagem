const { getApiData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const fullData = getApiData();
  return res.status(200).json({
    status: "ok",
    project_meta: fullData.project_meta || {},
    investigation_scope: fullData.investigation_scope || {},
    pipeline: fullData.forensic_methodology_pipeline || {},
    reproducibility: fullData.reproducibility_guide || {}
  });
};
