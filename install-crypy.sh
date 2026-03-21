#!/bin/bash
# ============================================
# CRYPy - Instalador (Menu apenas)
# ============================================

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║    🔍 CRYPy - Instalador           ║"
echo "╚═══════════════════════════════════════╝"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo "Execute como root: sudo $0"
    exit 1
fi

# Copiar aplicativo
echo "[1/4] Copiando aplicativo..."
mkdir -p /opt/crypy
cp /home/cas1/distroforge_studio/crypy/crypy.py /opt/crypy/crypy.py

cat > /usr/bin/crypy << 'EOF'
#!/bin/bash
cd /opt/crypy
python3 crypy.py "$@"
EOF
chmod +x /usr/bin/crypy
echo "✓ Aplicativo instalado"

# KDE Dolphin
echo ""
echo "[2/4] Configurando menu Dolphin..."
mkdir -p ~/.local/share/kservices5

cat > ~/.local/share/kservices5/CRYPy.desktop << 'EOF'
[Desktop Entry]
Type=Service
ServiceTypes=KonqPopupMenu/Plugin
MimeType=application/octet-stream;application/x-executable;application/x-ms-executable;application/vnd.microsoft.portable-executable;
Actions=verificar

[Desktop Action verificar]
Name=🔍 Verificar Disponibilidade
Icon=system-software-update
Exec=/usr/bin/crypy %f
EOF
chmod +x ~/.local/share/kservices5/CRYPy.desktop
echo "✓ Menu Dolphin configurado"

# GNOME Nautilus
echo ""
echo "[3/4] Configurando menu Nautilus..."
mkdir -p ~/.local/share/nautilus/scripts
cat > ~/.local/share/nautilus/scripts/"🔍 Verificar Disponibilidade" << 'EOF'
#!/bin/bash
/usr/bin/crypy "$@"
EOF
chmod +x ~/.local/share/nautilus/scripts/"🔍 Verificar Disponibilidade"
echo "✓ Menu Nautilus configurado"

# XFCE Thunar
echo ""
echo "[4/4] Configurando menu Thunar..."
mkdir -p ~/.config/Thunar
if [ ! -f ~/.config/Thunar/uca.xml ]; then
    echo '<?xml version="1.0" encoding="UTF-8"?><actions>' > ~/.config/Thunar/uca.xml
fi
if ! grep -q "CRYPy" ~/.config/Thunar/uca.xml 2>/dev/null; then
    sed -i 's|</actions>||' ~/.config/Thunar/uca.xml
    cat >> ~/.config/Thunar/uca.xml << 'EOF'

  <action>
    <icon>system-software-update</icon>
    <name>🔍 Verificar Disponibilidade</name>
    <command>/usr/bin/crypy %f</command>
    <patterns>*</patterns>
    <other-files/>
  </action>
</actions>
EOF
fi
echo "✓ Menu Thunar configurado"

# Atualizar KDE
kbuildsycoca6 2>/dev/null || true
kbuildsycoca5 --noincremental 2>/dev/null || true

echo ""
echo "════════════════════════════════════════"
echo "  ✅ CRYPy INSTALADO!"
echo "════════════════════════════════════════"
echo ""
echo "Como usar:"
echo "  • Botão direito em .exe → '🔍 Verificar Disponibilidade'"
echo ""
echo "⚠️  Reinicie o Dolphin:"
echo "  killall dolphin; dolphin &"
echo ""
echo "Para desinstalar: sudo ./uninstall-crypy.sh"
