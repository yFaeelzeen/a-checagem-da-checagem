const path = require('path');
const fs = require('fs');

let cachedApiData = null;
let cachedDeclarations = null;

function getApiData() {
  if (cachedApiData) return cachedApiData;
  const possiblePaths = [
    path.join(__dirname, '..', 'api_data.json'),
    path.join(process.cwd(), 'api_data.json'),
    path.join(__dirname, 'api_data.json')
  ];

  for (const p of possiblePaths) {
    if (fs.existsSync(p)) {
      try {
        cachedApiData = JSON.parse(fs.readFileSync(p, 'utf-8'));
        return cachedApiData;
      } catch (e) {
        return { error: `Erro ao decodificar api_data.json: ${e.message}` };
      }
    }
  }
  return { error: 'api_data.json não encontrado' };
}

function getDeclarationsData() {
  if (cachedDeclarations) return cachedDeclarations;
  const possiblePaths = [
    path.join(__dirname, '..', 'declarations.json'),
    path.join(process.cwd(), 'declarations.json'),
    path.join(__dirname, 'declarations.json')
  ];

  for (const p of possiblePaths) {
    if (fs.existsSync(p)) {
      try {
        cachedDeclarations = JSON.parse(fs.readFileSync(p, 'utf-8'));
        return cachedDeclarations;
      } catch (e) {
        return [];
      }
    }
  }
  return [];
}

function setCors(res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Cache-Control', 'public, max-age=300, s-maxage=3600');
}

module.exports = {
  getApiData,
  getDeclarationsData,
  setCors
};
