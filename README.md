# dash-launcher-vlan1

A small Windows launcher (**open-dash.exe**) you compile in **WSL** that opens a dashboard URL (e.g., your VLAN1 jumpbox web UI) and embeds a custom **.ico**. Includes an environment config file so you can quickly switch networks (VLANs) without recompiling.

> Primary use-case: Launch dashboards in a **Portfolio / Cyber Range** lab (e.g., dubz-vault.corp). Tested with a Lenovo ThinkCentre M700 Tiny running Windows 11 + Retail Plus, joined to AD domain, with father/son lab users.

---

## ✅ What you get

- `open-dash.exe` — Windows launcher that:
  - Optionally pings a host/gateway (to avoid opening a dead link)
  - Sleeps a moment (to let network settle)
  - Opens your dashboard URL in the default browser
  - **Embeds a custom icon** via Windows resource (`.rc` + `.ico`)

- `launch.env` — **Change your target IP/URL** here (VLAN1, Mgmt, Jumpbox, etc.)

- `build.sh` — Compile on **WSL** using MinGW (`x86_64-w64-mingw32-gcc` + `windres`).

- `assets/app.ico` — Your icon. (Use a real `.ico`; see troubleshooting if `windres` fails.)

---

## 🧰 Prerequisites (WSL / Ubuntu)

```bash
sudo apt update
sudo apt install -y mingw-w64 imagemagick python3-pip
```

> `mingw-w64` provides `x86_64-w64-mingw32-gcc` (compiler) and `x86_64-w64-mingw32-windres` (resource compiler).  
> `imagemagick` lets you convert a PNG to ICO quickly.

---

## 📁 Project structure

```
dash-launcher-vlan1/
├── open_dash.c      # C source for the launcher
├── icon.rc          # Resource script (links to assets/app.ico)
├── build.sh         # Build script for WSL (creates open-dash.exe)
├── launch.env       # Config: URL/IP + ping host + delay
└── assets/
    └── app.ico      # Your .ico file (convert from a .png)
```

---

## ⚙️ Configure (set your VLAN1 URL/IP)

Edit `launch.env` (plain text key=value):

```
DASH_URL=http://172.20.10.30:8000/
DASH_PING_HOST=172.20.10.1
DASH_PING_COUNT=2
DASH_SLEEP_MS=1500
DASH_DO_PING=1
```

- **Change `DASH_URL`** when you move to a new VLAN / jumpbox / host.  
- `DASH_DO_PING=1` lets the launcher quickly probe connectivity before opening the browser.  
- `DASH_SLEEP_MS` gives the NIC time to settle after login/network switch.

---

## 🛠 Build the EXE

```bash
cd ~/dash-launcher-vlan1
chmod +x build.sh
./build.sh
```

**Output:** `open-dash.exe` is copied to your Windows Desktop.

> If you see `x86_64-w64-mingw32-windres: command not found` — install `mingw-w64`.  
> If you see `unexpected EOF` — replace the placeholder icon with a **real .ico** (see below).

---

## 🖼 Make/replace the icon (.ico)

If you have a PNG you’d like to use:

```bash
convert /mnt/c/Users/<YOU>/OneDrive/Desktop/screenshot.png -resize 256x256 ./assets/app.ico
```

> Re-run `./build.sh` after updating the `.ico`.

---

## ▶️ Run with env config (Windows wrapper BAT)

Create `setenv-and-run.bat` **next to the EXE** (e.g., on your Desktop):

```
@echo off
setlocal
for /f "usebackq tokens=1,2 delims==" %%A in ("C:\Users\<YOU>\OneDrive\launch.env") do set %%A=%%B
start "" "%~dp0open-dash.exe"
endlocal
```

- Put your `launch.env` somewhere Windows can read it (e.g., `C:\Users\<YOU>\OneDrive\launch.env`).  
- Double-click the BAT → it loads env vars → launches the EXE → opens your dashboard URL.  
- **Change VLAN?** Edit `DASH_URL` in `launch.env`. No rebuild needed.

---

## 🧪 Awareness payloads (optional)

Inside `open_dash.c` you can toggle harmless demos:

```c
// system("start C:\\");   // Open C:\ in Explorer
// system("start calc.exe"); // Pop Calculator
```

Default behavior is to open `DASH_URL`.

> Use these only for **awareness training** inside your **lab environment**. Do not deploy to production.

---

## 🔐 Optional: code signing (Windows)

If you have a code-signing cert:

```
"C:\Program Files (x86)\Windows Kits\10\bin\x64\signtool.exe" sign ^
  /f yourcert.pfx ^
  /tr http://timestamp.digicert.com ^
  /td sha256 ^
  /fd sha256 ^
  "C:\Users\<YOU>\Desktop\open-dash.exe"
```

---

## 🩺 Troubleshooting

**1) `x86_64-w64-mingw32-windres: command not found`**  
Install MinGW cross-tools:
```bash
sudo apt update
sudo apt install -y mingw-w64
```

**2) `unexpected EOF` from `windres`**  
Your `app.ico` is a placeholder / invalid. Replace with a real `.ico`:
```bash
convert /path/to/image.png -resize 256x256 ./assets/app.ico
```

**3) Icon path issues in `icon.rc`**  
Make sure the path is relative to project root:
```
id ICON "./assets/app.ico"
```

**4) EXE builds but no browser opens**  
Confirm your env is loaded:
- Print env inside `open_dash.c` (temporary debug):
  ```c
  printf("URL=%s\n", url);
  ```
- Or hard-code a test:
  ```c
  const char* url = "http://127.0.0.1:8000/index.html";
  ```

**5) WSL can’t copy to Desktop**  
Set your Windows username in `build.sh`:
```
WIN_USER="jasdi"
DESKTOP="/mnt/c/Users/$WIN_USER/Desktop"
```

---

## 📎 Notes for Portfolio / AD Lab

- Target machine: **Lenovo ThinkCentre M700 Tiny** (Windows 11, Retail Plus, AD-joined to `dubz-vault.corp`).  
- Intended users: **you** and **your son** (Retail Plus) for learning audit/sales/losses workflows.  
- This launcher is part of a broader **Portfolio 2024 / Cyber Range** and can be duplicated per VLAN or purpose (e.g., `dash-launcher-mgmt`, `dash-launcher-vlan10`, etc.).

---

## 📜 License / Ethics

This project is built for **education and awareness** in a **controlled lab**.  
Do not deploy to production or use against systems without authorization.

---

## 📦 Next (optional)

- Add a GitHub `README.md` with screenshots (`assets/`) for polish.  
- Add a `.gitignore` to exclude `uploads/`, `__pycache__/`, `*.exe`, etc.  
- Create variant launchers for other VLANs by copying this folder and changing only `launch.env`.
