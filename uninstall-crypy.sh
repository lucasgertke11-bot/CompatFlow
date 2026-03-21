#!/bin/bash
# ============================================
# CRYPy - Desinstalador
# ============================================

echo ""
echo "╔═══════════════════════════════════════╗"
echo "║    🗑️ CRYPy - Desinstalador       ║"
echo "╚═══════════════════════════════════════╝"
echo ""

if [ "$EUID" -ne 0 ]; then
    echo "Execute como root: sudo $0"
    exit 1
fi

echo "Removendo aplicativo..."
rm -rf /opt/crypy
rm -f /usr/bin/crypy

echo "Removendo menus KDE..."
rm -f ~/.local/share/kservices5/CRYPy.desktop
rm -f ~/.local/share/kservices5/Crypt*.desktop

echo "Removendo menus GNOME..."
rm -f ~/.local/share/nautilus/scripts/"🔍 Verificar Disponibilidade"

echo "Removendo menus XFCE..."
if [ -f ~/.config/Thunar/uca.xml ]; then
    sed -i '/Verificar Disponibilidade/d' ~/.config/Thunar/uca.xml
fi

echo "Removendo associações..."
rm -f /usr/share/applications/crypy.desktop
rm -f /usr/share/applications/crypt.desktop

echo ""
echo "════════════════════════════════════════"
echo "  ✅ CRYPy DESINSTALADO!"
echo "════════════════════════════════════════"
