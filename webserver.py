#!/usr/bin/env python
# coding: utf-8

#Web server
import http.server
import socketserver

PORT = 9090
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
