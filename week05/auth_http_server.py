#!/usr/bin/env python3
# auth_http_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import base64
import argparse

class BasicAuthHTTPRequestHandler(SimpleHTTPRequestHandler):
    # Set these to your desired username/password
    USERNAME = "demo"
    PASSWORD = "some_password"

    def do_AUTHHEAD(self):
        self.send_response(401)
        self.send_header('WWW-Authenticate', 'Basic realm="Wireshark Lab"')
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def is_authenticated(self):
        auth_header = self.headers.get('Authorization')
        if not auth_header:
            return False
        try:
            scheme, encoded = auth_header.split(' ', 1)
            if scheme.lower() != 'basic':
                return False
            decoded = base64.b64decode(encoded.strip()).decode('utf-8')
            user, pwd = decoded.split(':', 1)
            return user == self.USERNAME and pwd == self.PASSWORD
        except Exception:
            return False

    def do_GET(self):
        if not self.is_authenticated():
            self.do_AUTHHEAD()
            self.wfile.write(b'401 Unauthorized\n')
            return
        return super().do_GET()

    def do_HEAD(self):
        if not self.is_authenticated():
            self.do_AUTHHEAD()
            return
        return super().do_HEAD()

    def do_POST(self):
        if not self.is_authenticated():
            self.do_AUTHHEAD()
            self.wfile.write(b'401 Unauthorized\n')
            return
        return super().do_POST()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bind', default='127.0.0.1', help='Address to bind to (default 127.0.0.1)')
    parser.add_argument('--port', default=8000, type=int, help='Port (default 8000)')
    parser.add_argument('--user', default='demo', help='Username')
    parser.add_argument('--pass', dest='password', default='some_password', help='Password')
    args = parser.parse_args()

    BasicAuthHTTPRequestHandler.USERNAME = args.user
    BasicAuthHTTPRequestHandler.PASSWORD = args.password

    server = HTTPServer((args.bind, args.port), BasicAuthHTTPRequestHandler)
    print(f"Serving HTTP with BasicAuth on http://{args.bind}:{args.port}/ (user={args.user})")
    server.serve_forever()
