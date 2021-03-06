#!/usr/bin/python3

from IO import *
from NetHandler import NetHandler
from http.server import HTTPServer, BaseHTTPRequestHandler


class IHttpRequestHandler(BaseHTTPRequestHandler, NetHandler):
    def do_GET(self):
        code, content = parseGetRequest()

        self.send_response(code)
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        code, content = parsePostRequest(body)

        self.send_response(code)
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    ip = 'localhost'
    port = 80
    httpd = HTTPServer((ip, port), IHttpRequestHandler)
    print(f"Https server starting on {ip}:{port}")
    httpd.serve_forever()

