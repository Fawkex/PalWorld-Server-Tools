import os
import http.server
import socket
import urllib.parse

start_script = '/home/steam/start.sh'

def start_server():
    os.system(start_script)

class HTTPServerV6(http.server.HTTPServer):
    address_family = socket.AF_INET6

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_params = urllib.parse.urlparse(self.path)
        if parsed_params.path == '/startServer':
            start_server()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server started successfully.\n")
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Nothing here.\n")

if __name__ == '__main__':
    PORT = 18000
    server_socket = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server_address = ('::', PORT)  

    httpd = HTTPServerV6(server_address, CustomHTTPRequestHandler)

    print(f"Server started at port [::]:{PORT}")
    httpd.serve_forever()
