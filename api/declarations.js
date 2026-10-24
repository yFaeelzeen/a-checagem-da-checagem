const { getDeclarationsData, setCors } = require('./_utils');

module.exports = (req, res) => {
  setCors(res);
  if (req.method === 'OPTIONS') {
    return res.status(204).end();
  }

  const query = req.query || {};
  const qSearch = (query.search || '').trim().toLowerCase();
  const qCand = (query.candidate || '').trim().toLowerCase();
  const qVerdict = (query.verdict || '').trim().toLowerCase();

  const decls = getDeclarationsData();
  const filtered = [];

  for (const d of decls) {
    if (qCand && qCand !== 'all' && d.candidateKey !== qCand) {
      continue;
    }
    if (qVerdict && qVerdict !== 'all' && d.normalizedVerdict !== qVerdict) {
      continue;
    }
    if (qSearch) {
      const tokens = d.searchTokens || '';
      if (!tokens.includes(qSearch)) {
        continue;
      }
    }
    filtered.push(d);
  }

  return res.status(200).json({
    status: "ok",
    total_matched: filtered.length,
    total_catalog: decls.length,
    filters_applied: {
      search: qSearch || null,
      candidate: qCand || null,
      verdict: qVerdict || null
    },
    declarations: filtered
  });
};
