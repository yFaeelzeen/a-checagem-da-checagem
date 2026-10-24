const { getDeclarationsData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const decls = getDeclarationsData();
  return res.status(200).json({
    status: "ok",
    total_cases: decls.length,
    cases: decls
  });
};
