#!/usr/bin/env python3
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
import cgi

# Define the Absolute path to uploads
UPLOAD_DIR = "/opt/cheats/uploads"

# Ensure it's always served from /opt/cheats (not from cwd)
BASE_DIR = "/opt/cheats/uploads"
os.chdir(BASE_DIR)

class UploadHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/upload':
            ctype, pdict = cgi.parse_header(self.headers['content-type'])
            if ctype == 'multipart/form-data':
                form = cgi.FieldStorage(
                    fp=self.rfile,
                    headers=self.headers,
                    environ={'REQUEST_METHOD': 'POST'}
                )
                if 'file' in form:
                    uploaded_file = form['file']
                    filename = os.path.basename(uploaded_file.filename)
                    filepath = os.path.join(UPLOAD_DIR, filename)

                    try:
                        os.makedirs(UPLOAD_DIR, exist_ok=True)
                        with open (filepath, 'wb') as f:
                            f.write(uploaded_file.file.read())

                            self.send_response(200)
                            self.end_headers()
                            self.wfile.write(f"File uploaded: {filename}".encode("utf-8"))
                            print(f"[UPLOAD] Saved: {filename} to {filepath}")
                            return
                        
                    except Exception as e:
                        self.send_response(500)
                        self.end_headers()
                        self.wfile.write(f"Server error: {str(e)}".encode("utf-8"))
                        print(f"[ERROR] Failed to save upload: {e}")
                        return
        self.send_response(400)
        self.end_headers()                    
        self.wfile.write("Upload failed or unsupported endpoint.".encode("utf-8"))

def run():
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    server_address = ("0.0.0.0", 8888)
    httpd = HTTPServer(server_address, UploadHandler)
    print("Serving on http://0.0.0.0:8888")
    print(f"Uploads directory: {UPLOAD_DIR}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()