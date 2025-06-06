from http.server import SimpleHTTPRequestHandler, HTTPServer
from datetime import datetime

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = f'{{"message": "test", "time": "{datetime.utcnow().isoformat()}"}}'
            self.wfile.write(response.encode("utf-8"))
        else:
            self.send_error(404, "Not Found")

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 5000), CustomHandler)
    print("Starting server on port 5000...")
    server.serve_forever()
