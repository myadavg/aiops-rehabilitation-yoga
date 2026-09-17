import boto3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT = 8090

class SNSHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        content_length = int(self.headers["Content-Length"])
        body = self.rfile.read(content_length)

        message = json.loads(body)

        print("\n=== SNS EVENT RECEIVED ===")
        print(json.dumps(message, indent=2))

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")


server = HTTPServer(("0.0.0.0", PORT), SNSHandler)

print(f"SNS listener running on port {PORT}")

server.serve_forever()
