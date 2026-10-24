const { getApiData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const fullData = getApiData();
  return res.status(200).json({
    status: "ok",
    bias_forensic_analysis: fullData.bias_forensic_analysis || {},
    outlets_deep_profile: fullData.outlets_deep_profile || {}
  });
};
