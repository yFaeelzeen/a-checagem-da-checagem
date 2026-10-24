const { getApiData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const fullData = getApiData();
  const scope = fullData.investigation_scope || {};
  return res.status(200).json({
    status: "ok",
    universe: scope.universe_audited || {},
    outlets: fullData.outlets_deep_profile || {},
    cross_match: scope.cross_match_matrix || {}
  });
};
