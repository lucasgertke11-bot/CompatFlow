#!/usr/bin/env python3
"""
CRYPy - Verificador de Compatibilidade + Ports
"""

import sys
import os
import json
import hashlib
from datetime import datetime
import subprocess

try:
    from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                                    QVBoxLayout, QHBoxLayout, QFrame, QMessageBox, QInputDialog)
    from PySide6.QtCore import Qt
except:
    print("PySide6 necessário: pip3 install PySide6")
    sys.exit(1)

API = "https://api.github.com/repos/lucasgertke11-bot/distroforge-database"
GITHUB_API = "https://api.github.com/repos/lucasgertke11-bot/crypy"
CACHE_DIR = os.path.expanduser("~/.config/crypy")
TOKEN_FILE = os.path.join(CACHE_DIR, "token")
CACHE_FILE = os.path.join(CACHE_DIR, "ports.json")
VERSIONS_FILE = os.path.join(CACHE_DIR, "version.json")


def get_token():
    os.makedirs(CACHE_DIR, exist_ok=True)
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE) as f:
            return f.read().strip()
    token = os.environ.get("GITHUB_TOKEN", "")
    if token:
        with open(TOKEN_FILE, "w") as f:
            f.write(token)
        return token
    return ""


def set_token(token):
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(TOKEN_FILE, "w") as f:
        f.write(token)


def github_get(url):
    token = get_token()
    if not token:
        return None
    import requests
    r = requests.get(url, headers={"Authorization": f"token {token}"}, timeout=10)
    return r


def github_put(url, data):
    token = get_token()
    if not token:
        return None
    import requests
    r = requests.put(url, json=data, headers={"Authorization": f"token {token}"}, timeout=10)
    return r


NATIVE = {
    "steam": ("Steam", "steam", "Plataforma de jogos"),
    "discord": ("Discord", "discord", "Chat para gamers"),
    "spotify": ("Spotify", "spotify", "Streaming de música"),
    "telegram": ("Telegram", "telegram-desktop", "Mensagens"),
    "firefox": ("Firefox", "firefox", "Navegador"),
    "chrome": ("Chrome", "google-chrome-stable", "Navegador"),
    "edge": ("Edge", "microsoft-edge-stable", "Navegador"),
    "opera": ("Opera", "opera", "Navegador"),
    "brave": ("Brave", "brave-browser", "Navegador"),
    "vlc": ("VLC", "vlc", "Reprodutor de mídia"),
    "gimp": ("GIMP", "gimp", "Editor de imagens"),
    "vscode": ("VS Code", "code", "Editor de código"),
    "code": ("VS Code", "code", "Editor de código"),
    "obs": ("OBS", "obs-studio", "Gravação"),
    "libreoffice": ("LibreOffice", "libreoffice", "Escritório"),
    "qbittorrent": ("qBittorrent", "qbittorrent", "Torrent"),
    "filezilla": ("FileZilla", "filezilla", "FTP"),
    "git": ("Git", "git", "Controle de versão"),
    "audacity": ("Audacity", "audacity", "Editor de áudio"),
    "virtualbox": ("VirtualBox", "virtualbox", "Virtualização"),
    "minecraft": ("Minecraft", "minecraft-launcher", "Jogo"),
    "epic": ("Epic Games", "heroic-games-launcher-bin", "Epic Games"),
    "gog": ("GOG Galaxy", "heroic-games-launcher-bin", "GOG"),
    "teamspeak": ("TeamSpeak", "teamspeak3", "Voz"),
    "skype": ("Skype", "skypeforlinux", "Videochamadas"),
    "zoom": ("Zoom", "zoom", "Videochamadas"),
    "winrar": ("7-Zip", "p7zip-full", "Compactador"),
    "7zip": ("7-Zip", "p7zip-full", "Compactador"),
}


def get_app_name(filename):
    name = os.path.basename(filename).lower()
    name = name.replace('.exe', '').replace('.msi', '')
    name = name.replace('setup', '').replace('installer', '').replace('install', '')
    name = name.replace('-', ' ').replace('_', ' ').strip()
    return name


def get_distro():
    if os.path.exists('/etc/arch-release'):
        return "arch"
    elif os.path.exists('/etc/fedora-release'):
        return "fedora"
    elif os.path.exists('/etc/opensuse-release'):
        return "opensuse"
    return "ubuntu"


def get_install_cmd(package):
    distro = get_distro()
    if distro == "arch":
        return f"sudo pacman -S {package}"
    elif distro == "fedora":
        return f"sudo dnf install {package}"
    elif distro == "opensuse":
        return f"sudo zypper install {package}"
    return f"sudo apt install {package}"


def update_cache():
    try:
        import requests
        import base64
        os.makedirs(CACHE_DIR, exist_ok=True)
        r = github_get(f"{API}/contents/data/ports/ports.json")
        if r and r.status_code == 200:
            content = r.json()["content"]
            data = base64.b64decode(content).decode()
            with open(CACHE_FILE, 'w') as f:
                f.write(data)
            print(f"✅ Cache atualizado! ({len(data)} bytes)")
            return True
        print(f"⚠️  Arquivo ports.json não encontrado")
        return False
    except Exception as e:
        print(f"❌ Erro ao atualizar cache: {e}")
        return False


def check_update():
    try:
        r = github_get(f"{GITHUB_API}/contents/version.json")
        if r and r.status_code == 200:
            import base64
            content = base64.b64decode(r.json()["content"]).decode()
            return json.loads(content)
        return None
    except:
        return None


def download_update():
    try:
        os.makedirs(CACHE_DIR, exist_ok=True)
        
        # Baixar arquivos do repo
        files = ["crypy.py", "install-crypy.sh", "uninstall-crypy.sh", "README_DEV.md"]
        
        for fname in files:
            r = github_get(f"{GITHUB_API}/contents/{fname}")
            if r and r.status_code == 200:
                import base64
                content = base64.b64decode(r.json()["content"]).decode()
                with open(os.path.join(CACHE_DIR, fname), 'w') as f:
                    f.write(content)
                print(f"✅ {fname} baixado")
        
        # Atualizar versão
        ver = check_update()
        if ver:
            with open(VERSIONS_FILE, 'w') as f:
                json.dump(ver, f)
        
        return True
    except Exception as e:
        print(f"❌ Erro ao baixar update: {e}")
        return False


def load_ports():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE) as f:
            data = json.load(f)
            if "_template" in data:
                del data["_template"]
            return data
    except:
        return {}


def check_port(clean_name):
    ports = load_ports()
    for port_id, port in ports.items():
        keywords = port.get("keywords", [])
        for kw in keywords:
            if kw in clean_name or clean_name in kw:
                return {"found": True, "port": port, "id": port_id}
    return {"found": False}


def check_native(clean_name):
    for keyword, (app, pkg, desc) in NATIVE.items():
        if keyword in clean_name or clean_name in keyword:
            return {"found": True, "app": app, "package": pkg, "desc": desc}
    return {"found": False}


def analyze(exe_path):
    clean_name = get_app_name(exe_path)
    result = {"original": os.path.basename(exe_path), "clean_name": clean_name}
    
    native = check_native(clean_name)
    if native["found"]:
        result["type"] = "native"
        result.update(native)
        return result
    
    port = check_port(clean_name)
    if port["found"]:
        result["type"] = "port"
        result.update(port)
        return result
    
    result["type"] = "unknown"
    result["app"] = clean_name.title() if clean_name else "Desconhecido"
    return result


def send_request(app_name, note=""):
    import requests, base64
    data = {"app": app_name, "note": note, "date": datetime.now().isoformat()}
    encoded = base64.b64encode(json.dumps(data, indent=2).encode()).decode()
    checksum = hashlib.md5(app_name.encode()).hexdigest()[:8]
    filename = f"{checksum}_{app_name}.json"
    url = f"{API}/contents/data/requests/{filename}"
    
    r = github_get(url)
    payload = {"message": f"Request: {app_name}", "content": encoded}
    if r and r.status_code == 200:
        payload["sha"] = r.json()["sha"]
    
    r = github_put(url, payload)
    return r.status_code in [200, 201, 204] if r else False


def check_installed(package):
    import subprocess
    distro = get_distro()
    try:
        if distro == "arch":
            cmd = ["pacman", "-Q", package]
        else:
            cmd = ["dpkg", "-s", package]
        r = subprocess.run(cmd, capture_output=True, timeout=5)
        return r.returncode == 0
    except:
        return False


def check_lutris():
    return check_installed("lutris") or os.path.exists("/usr/bin/lutris")


def check_wine():
    if os.path.exists("/usr/bin/wine") or os.path.exists("/usr/bin/wine64"):
        return True
    return check_installed("wine") or check_installed("winehq-stable") or check_installed("wine-stable")


class CRYPy(QWidget):
    def __init__(self, exe_path=None):
        super().__init__()
        self.exe = exe_path
        self.data = analyze(exe_path) if exe_path else None
        self.setWindowTitle("CRYPy")
        self.setFixedSize(420, 260)
        self.setStyleSheet(self.get_style())
        self.init_ui()
        if self.data:
            self.update_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(12)
        main_layout.setContentsMargins(15, 15, 15, 15)
        
        self.title = QLabel("🔍 CRYPy")
        self.title.setObjectName("title")
        self.title.setAlignment(Qt.AlignCenter)
        
        self.info_label = QLabel("Clique com botão direito em um .exe")
        self.info_label.setAlignment(Qt.AlignCenter)
        self.info_label.setWordWrap(True)
        
        btn_layout = QHBoxLayout()
        self.native_btn = QPushButton("🐧 Instalar Nativo")
        self.port_btn = QPushButton("🎮 Instalar Port")
        self.wine_btn = QPushButton("🍷 Rodar com Wine")
        
        btn_layout.addWidget(self.native_btn)
        btn_layout.addWidget(self.port_btn)
        btn_layout.addWidget(self.wine_btn)
        
        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        
        self.request_btn = QPushButton("📨 Solicitar Suporte")
        
        main_layout.addWidget(self.title)
        main_layout.addWidget(self.info_label)
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(line)
        main_layout.addWidget(self.request_btn)
        
        self.setLayout(main_layout)
        
        self.native_btn.clicked.connect(self.install_native)
        self.port_btn.clicked.connect(self.install_port)
        self.wine_btn.clicked.connect(self.run_wine)
        self.request_btn.clicked.connect(self.send_request_action)
    
    def update_ui(self):
        t = self.data["type"]
        
        if t == "native":
            self.info_label.setText(f"✅ {self.data['app']} - {self.data['desc']}\nNativo Linux disponível!")
            self.native_btn.setVisible(True)
            self.port_btn.setVisible(False)
            self.native_btn.setEnabled(True)
        elif t == "port":
            port = self.data["port"]
            port_type = port.get("type", "lutris").upper()
            self.info_label.setText(f"🎮 {port['name']}\nPort via {port_type} disponível!")
            self.native_btn.setVisible(False)
            self.port_btn.setVisible(True)
            self.port_btn.setEnabled(True)
        else:
            self.info_label.setText(f"❌ {self.data['app']}\nNão encontrado no banco de dados")
            self.native_btn.setVisible(False)
            self.port_btn.setVisible(False)
    
    def install_native(self):
        if self.data and self.data["type"] == "native":
            pkg = self.data["package"]
            os.system(f"xterm -e '{get_install_cmd(pkg)}'")
            self.close()
    
    def install_port(self):
        if self.data and self.data["type"] == "port":
            port = self.data["port"]
            distro = get_distro()
            port_type = port.get("type", "lutris")
            
            if port_type == "lutris":
                deps = port.get("dependencies", {}).get(distro, [])
                
                missing = []
                for dep in deps:
                    if not check_installed(dep):
                        missing.append(dep)
                
                if missing:
                    deps_cmd = " ".join(missing)
                    QMessageBox.information(self, "Instalando Dependências", f"Instalando: {deps_cmd}")
                    os.system(f"pkexec {get_install_cmd(deps_cmd)}")
                else:
                    QMessageBox.information(self, "Info", "Todas dependências já instaladas!")
                
                script_url = port.get("install", {}).get("script_url")
                if script_url and self.exe:
                    install_dir = "/tmp/crypy_install"
                    os.system(f"rm -rf {install_dir} && mkdir -p {install_dir}")
                    
                    dest_exe = os.path.join(install_dir, "setup.exe")
                    os.system(f"cp '{self.exe}' '{dest_exe}'")
                    
                    os.system(f"curl -sL '{script_url}' -o {install_dir}/installer.yml")
                    
                    with open(f"{install_dir}/installer.yml", "r") as f:
                        yml_content = f.read()
                    
                    yml_content = yml_content.replace("$SCRIPTDIR/VioletSetup.exe", "$SCRIPTDIR/setup.exe")
                    yml_content = yml_content.replace("N/A:Select the game setup file", "$SCRIPTDIR/setup.exe")
                    
                    with open(f"{install_dir}/installer.yml", "w") as f:
                        f.write(yml_content)
                    
                    QMessageBox.information(self, "Executando", f"Instalando: {os.path.basename(self.exe)}\n\nLutris vai abrir...")
                    
                    wrapper = f"""#!/bin/bash
cd {install_dir}
lutris -i {install_dir}/installer.yml &
"""
                    with open("/tmp/crypy_run.sh", "w") as f:
                        f.write(wrapper)
                    os.system("chmod +x /tmp/crypy_run.sh")
                    os.system("bash /tmp/crypy_run.sh &")
                else:
                    QMessageBox.warning(self, "Erro", "Script ou arquivo não disponível!")
            
            self.close()
    
    def run_wine(self):
        if self.exe:
            os.system(f"wine '{self.exe}' &")
            self.close()
    
    def send_request_action(self):
        if self.data:
            ok = send_request(self.data.get("app", self.data["clean_name"]))
            if ok:
                QMessageBox.information(self, "OK", "Solicitação enviada!")
            else:
                QMessageBox.warning(self, "Erro", "Configure o token GitHub em ~/.config/crypy/token")
    
    def get_style(self):
        return """
        QWidget {
            background-color: #1e1e2e;
            color: #ffffff;
            font-size: 13px;
        }
        #title {
            font-size: 16px;
            font-weight: bold;
        }
        QPushButton {
            background-color: #3a3a5a;
            border-radius: 6px;
            padding: 6px;
            min-width: 90px;
        }
        QPushButton:hover {
            background-color: #505080;
        }
        QPushButton:pressed {
            background-color: #2a2a4a;
        }
        QPushButton:disabled {
            background-color: #2a2a3a;
            color: #666;
        }
        QLabel {
            color: #dddddd;
        }
        """


if __name__ == "__main__":
    if "--update" in sys.argv:
        print("Atualizando cache de ports...")
        update_cache()
        sys.exit(0)
    
    if "--check-update" in sys.argv:
        ver = check_update()
        if ver:
            print(f"Versão disponível: {ver.get('version', '?')}")
        else:
            print("Não foi possível verificar atualizações.")
        sys.exit(0)
    
    if "--upgrade" in sys.argv:
        print("Baixando atualização...")
        if download_update():
            print("✅ Atualização baixada! Reinicie o CRYPy.")
        else:
            print("❌ Falha na atualização. Configure o token GitHub.")
            print("   echo 'seu_token' > ~/.config/crypy/token")
        sys.exit(0)
    
    if "--test" in sys.argv:
        print("Testando análise...")
        test_file = sys.argv[2] if len(sys.argv) > 2 else "/tmp/test.exe"
        result = analyze(test_file)
        print(json.dumps(result, indent=2))
        sys.exit(0)
    
    if "--set-token" in sys.argv:
        if len(sys.argv) > 2:
            set_token(sys.argv[2])
            print("✅ Token configurado!")
        else:
            print("Uso: crypy --set-token SEU_TOKEN")
        sys.exit(0)
    
    app = QApplication(sys.argv)
    exe = sys.argv[1] if len(sys.argv) > 1 else None
    w = CRYPy(exe)
    w.show()
    sys.exit(app.exec())
