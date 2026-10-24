const { getApiData, getDeclarationsData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const fullData = getApiData();
  const decls = getDeclarationsData();
  const result = {
    ...fullData,
    all_declarations_catalog: decls
  };

  return res.status(200).json(result);
};
