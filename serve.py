import http.server
import ssl

PORT = 8000
server_address = ('0.0.0.0', PORT)

httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# Wrap with SSL
httpd.socket = ssl.SSLContext(httpd.socket,
                               keyfile="key.pem",
                               certfile="cert.pem",
                               server_side=True)

print(f"Serving on https://0.0.0.0:{PORT}")
httpd.serve_forever()