# Cyber Lab Practice: 

## This will be saved locally are ran PowerShell - it will also live on locally on LAN using a Raspberry Pie
<img width="945" height="658" alt="Mid-Term-Help" src="https://github.com/user-attachments/assets/10a9e91b-8e3b-4b45-97ae-d01a56d0d0d4" />

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
