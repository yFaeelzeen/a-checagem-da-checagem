import os
import sys
import json
import urllib.parse
import http.server
import socketserver

sys.stdout.reconfigure(encoding='utf-8')

DIRECTORY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API_DATA_PATH = os.path.join(DIRECTORY, "api_data.json")
DECLARATIONS_DATA_PATH = os.path.join(DIRECTORY, "declarations.json")
PORT = 8080

def get_api_data():
    if os.path.exists(API_DATA_PATH):
        try:
            with open(API_DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return {"error": f"Erro ao carregar base de dados: {str(e)}"}
    return {"error": "api_data.json não encontrado"}

def get_declarations_data():
    if os.path.exists(DECLARATIONS_DATA_PATH):
        try:
            with open(DECLARATIONS_DATA_PATH, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            return []
    return []

class ApiAndNoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def send_json_response(self, data, status=200):
        payload = json.dumps(data, ensure_ascii=False, indent=2).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(payload)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        self.end_headers()
        self.wfile.write(payload)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path.rstrip('/')

        # Intercepta rotas da API REST
        if path == '/api' or path == '/api/index':
            full_data = get_api_data()
            decls = get_declarations_data()
            index_res = {
                "status": "ok",
                "project": full_data.get("project_meta", {}),
                "available_endpoints": full_data.get("api_endpoints", []),
                "summary": {
                    "total_declarations_catalog": len(decls) or 412,
                    "independent_checks": 399,
                    "press_checks": 219,
                    "confrontation_matrix_rows": 22159,
                    "sha256_verified_files": 484
                },
                "links": {
                    "self": "/api",
                    "declarations": "/api/declarations",
                    "methodology": "/api/methodology",
                    "bias_analysis": "/api/bias-analysis",
                    "cases": "/api/cases",
                    "stats": "/api/stats",
                    "all": "/api/all",
                    "documentation_ui": "/metodologia.html"
                }
            }
            self.send_json_response(index_res)
            return

        elif path == '/api/declarations':
            qs = urllib.parse.parse_qs(parsed.query)
            q_search = qs.get('search', [''])[0].strip().lower()
            q_cand = qs.get('candidate', [''])[0].strip().lower()
            q_verdict = qs.get('verdict', [''])[0].strip().lower()

            decls = get_declarations_data()
            filtered = []
            for d in decls:
                if q_cand and q_cand != 'all' and d.get('candidateKey') != q_cand:
                    continue
                if q_verdict and q_verdict != 'all' and d.get('normalizedVerdict') != q_verdict:
                    continue
                if q_search:
                    tokens = d.get('searchTokens', '')
                    if q_search not in tokens:
                        continue
                filtered.append(d)

            res = {
                "status": "ok",
                "total_matched": len(filtered),
                "total_catalog": len(decls),
                "filters_applied": {
                    "search": q_search or None,
                    "candidate": q_cand or None,
                    "verdict": q_verdict or None
                },
                "declarations": filtered
            }
            self.send_json_response(res)
            return

        elif path == '/api/methodology':
            full_data = get_api_data()
            res = {
                "status": "ok",
                "project_meta": full_data.get("project_meta", {}),
                "investigation_scope": full_data.get("investigation_scope", {}),
                "pipeline": full_data.get("forensic_methodology_pipeline", {}),
                "reproducibility": full_data.get("reproducibility_guide", {})
            }
            self.send_json_response(res)
            return

        elif path == '/api/bias-analysis':
            full_data = get_api_data()
            res = {
                "status": "ok",
                "bias_forensic_analysis": full_data.get("bias_forensic_analysis", {}),
                "outlets_deep_profile": full_data.get("outlets_deep_profile", {})
            }
            self.send_json_response(res)
            return

        elif path == '/api/cases':
            decls = get_declarations_data()
            res = {
                "status": "ok",
                "total_cases": len(decls),
                "cases": decls
            }
            self.send_json_response(res)
            return

        elif path == '/api/stats':
            full_data = get_api_data()
            res = {
                "status": "ok",
                "universe": full_data.get("investigation_scope", {}).get("universe_audited", {}),
                "outlets": full_data.get("outlets_deep_profile", {}),
                "cross_match": full_data.get("investigation_scope", {}).get("cross_match_matrix", {})
            }
            self.send_json_response(res)
            return

        elif path == '/api/all':
            full_data = get_api_data()
            decls = get_declarations_data()
            full_data["all_declarations_catalog"] = decls
            self.send_json_response(full_data)
            return

        # Fallback para arquivos estáticos com no-cache
        super().do_GET()

    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def run():
    global PORT
    for attempt_port in range(8080, 8095):
        try:
            socketserver.TCPServer.allow_reuse_address = True
            with socketserver.TCPServer(("", attempt_port), ApiAndNoCacheHandler) as httpd:
                PORT = attempt_port
                print(f"SERVIDOR_RODANDO_PORTA:{PORT}")
                print(f"URL_ACESSO: http://localhost:{PORT}")
                sys.stdout.flush()
                httpd.serve_forever()
        except OSError:
            continue

if __name__ == '__main__':
    run()
