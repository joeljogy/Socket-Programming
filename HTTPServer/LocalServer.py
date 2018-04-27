import socketserver
import http.server
HPORT = 8008
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",HPORT),Handler)
print("Server at PORT ",HPORT)
httpd.serve_forever()
a=0
while a==0:
    None
