from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set response headers
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        
        # Send "Hello, World!" message
        self.wfile.write(b"Hello, World!")

def run():
    # Set server to run on localhost:8080
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, HelloWorldHandler)
    print("Starting server on port 8080...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
