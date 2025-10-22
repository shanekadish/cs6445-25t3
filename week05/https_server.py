#!/usr/bin/env python3
# https_server.py
from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import argparse
import pathlib

parser = argparse.ArgumentParser()
parser.add_argument('--bind', default='127.0.0.1', help='Bind address (default 127.0.0.1)')
parser.add_argument('--port', type=int, default=8443, help='Port (default 8443)')
parser.add_argument('--cert', default='cert.pem', help='Cert file (default cert.pem)')
parser.add_argument('--key', default='key.pem', help='Key file (default key.pem)')
args = parser.parse_args()

# Check that index.html exists
if not pathlib.Path('index.html').exists():
    raise SystemExit("Put index.html in same directory as https_server.py")

httpd = HTTPServer((args.bind, args.port), SimpleHTTPRequestHandler)

# Modern TLS configuration using SSLContext
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile=args.cert, keyfile=args.key)
# Optionally tighten security
# context.options |= ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_1

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print(f"Serving HTTPS on https://{args.bind}:{args.port}/ (CTRL-C to stop)")
httpd.serve_forever()
