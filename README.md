# Cyber Lab Practice: 

## This will be saved locally - test with PowerShell - it will also live locally on LAN using a Raspberry Pie
<img width="945" height="658" alt="Mid-Term-Help" src="https://github.com/user-attachments/assets/10a9e91b-8e3b-4b45-97ae-d01a56d0d0d4" />

<img width="1919" height="1012" alt="1" src="https://github.com/user-attachments/assets/5318f7b7-f84e-47dd-9a9a-01ea4dd0015b" />
<img width="1922" height="1010" alt="2" src="https://github.com/user-attachments/assets/cdd23c58-fe9c-413a-97ba-94bee299a598" />
<img width="1921" height="1008" alt="3" src="https://github.com/user-attachments/assets/841a19da-51ca-4a51-951f-5ddd086c29d2" />
<img width="1935" height="1009" alt="Start" src="https://github.com/user-attachments/assets/e28a651a-58e7-4a08-9d3e-923da5ce966c" />
<img width="1938" height="1005" alt="4" src="https://github.com/user-attachments/assets/1d5e7c7c-3183-455f-93f0-1599b33e4a7b" />
<img width="1933" height="1002" alt="5" src="https://github.com/user-attachments/assets/ff3f320f-a235-4452-99c6-7dfa74b4ec6c" />


## 10-13-2025: Moving this project to home server adding python logic below.

```Python
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
```

> Image: Local terminal

>  Internal use only —  Toolkit for hands on practical use and part of my hands Cyber Security studies 

This repository is for use across VMs. We  can `curl` or `wget` any `.txt` or `.md` file directly from this GitHub repo using raw HTTPS links.

---

## Usage

To pull a raw text into training environment VM:

```bash
# Template Below
curl -O https://raw.githubusercontent.com/<your-username>/<repo-name>/main/cheats/txt/nmap.txt
```

Or:

```bash
# Template Below
wget https://raw.githubusercontent.com/<your-username>/<repo-name>/main/cheats/txt/nmap.txt
```

---

## Directory Structure

```
/cheats/
├── index.html            # Cheat launcher interface
├── tools/
│   ├── nmap.html
│   ├── hydra.html
│   └── ...
├── txt/
│   ├── nmap.txt
│   ├── hydra.txt
│   └── ...
```

---

##  Available Cheats

| Tool       | Raw Link |
|------------|----------|
| Nmap       | [`nmap.txt`](cheats/txt/nmap.txt) |
| Hydra      | [`hydra.txt`](cheats/txt/hydra.txt) |
| FFUF       | [`ffuf.txt`](cheats/txt/ffuf.txt) |
| Gobuster   | [`gobuster.txt`](cheats/txt/gobuster.txt) |

---

## Keep Building 

Host the repo on GitHub and keep it **Private**. Use the "Raw" button on any file to get direct HTTPS links for usage inside labs or over isolated subnets.
