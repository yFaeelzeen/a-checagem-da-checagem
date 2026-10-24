import os
from http.server import BaseHTTPRequestHandler

HTML_FILE = os.path.join(os.path.dirname(__file__), "interface", "index.html")

def get_content():
    if os.path.exists(HTML_FILE):
        with open(HTML_FILE, "rb") as f:
            return f.read()
    return b"<!DOCTYPE html><html><body><h1>A Checagem da Checagem</h1></body></html>"

# WSGI Handler (compatibilidade com Vercel WSGI / Flask / Django)
def app(environ, start_response):
    content = get_content()
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
        ('Content-Length', str(len(content)))
    ]
    start_response(status, response_headers)
    return [content]

application = app

# BaseHTTPRequestHandler (compatibilidade com Vercel Serverless Function)
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        content = get_content()
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)
        return
