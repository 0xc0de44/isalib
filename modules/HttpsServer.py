#!/usr/bin/python3

from IO import *
from http.server import HTTPServer, BaseHTTPRequestHandler

class IHttpRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        code,content=parseGetrequest()

        self.send_response(code)
        self.end_headers()
        self.wfile.write(content)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        code,content=parsePostRequest(body)

        self.send_response(code)
        self.end_headers()
        self.wfile.write(content)

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 1337), IHttpRequestHandler)
    httpd.serve_forever()
