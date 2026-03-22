# 🔍 CompatFlow - Verificador de Compatibilidade Windows → Linux

![CompatFlow](compatflow.svg)

**CompatFlow** é um aplicativo que ajuda usuários vindos do Windows a encontrar versões nativas de seus programas favoritos no Linux.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-GPL--3.0-green)
![Platform](https://img.shields.io/badge/Platform-Linux-blue)

---

## 💡 Ideia Fundamental

Você está migrando do Windows para o Linux e encontrou um `.exe` que quer instalar?

O CompatFlow verifica automaticamente:
- ✅ Se existe versão **nativa Linux** desse programa
- 🎮 Se existe **port via Lutris** (para jogos)
- 🍷 Se pode rodar com **Wine**

**Tudo em um clique!**

---

## ✨ Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| 🔍 **Detecção automática** | Identifica qualquer arquivo `.exe` ou `.msi` |
| 🐧 **275+ apps nativos** | Firefox, Discord, VS Code, Steam e muito mais |
| 🎮 **Ports via Lutris** | Instalação automática de jogos Windows |
| 🍷 **Wine integrado** | Executa programas que não têm alternativa |
| 📤 **Sistema de reports** | Solicite suporte para apps não encontrados |
| 🔄 **Atualização automática** | Banco de dados sempre atualizado |
| 🌐 **Multi-distro** | Arch, Ubuntu, Fedora, openSUSE... |
| 🖥️ **Multi-ambiente** | Suporta Dolphin, Nautilus, Thunar, Files |

---

## 📦 Instalação

### Instalação rápida

```bash
git clone https://github.com/lucasgertke11-bot/CompatFlow.git
cd CompatFlow
sudo bash install-compatflow.sh
```

Depois reinicie o gerenciador de arquivos:
```bash
# KDE Dolphin
killall dolphin; dolphin &

# GNOME Nautilus
nautilus -q

# XFCE Thunar
thunar -q
```

---

## 🎮 Como Usar

1. **Clique com botão direito** em qualquer arquivo `.exe` ou `.msi`
2. Selecione **"🔍 Verificar com CompatFlow"**
3. O CompatFlow detecta automaticamente:

```
┌─────────────────────────────────────┐
│ ✅ Nativo Linux disponível          │
│    → Clique "🐧 Instalar Nativo"     │
├─────────────────────────────────────┤
│ 🎮 Port via Lutris disponível       │
│    → Clique "🎮 Instalar Port"      │
├─────────────────────────────────────┤
│ ❌ Não encontrado                    │
│    → Clique "📨 Solicitar Suporte"   │
└─────────────────────────────────────┘
```

---

## 📁 Estrutura do Projeto

```
CompatFlow/
├── compatflow.py              # Aplicativo principal (Python/PySide6)
├── compatflow.svg             # Ícone do aplicativo
├── compatflow.desktop         # Entrada no menu do sistema
├── install-compatflow.sh      # Script de instalação
├── uninstall-compatflow.sh    # Script de desinstalação
├── README.md                  # Documentação
├── README_DEV.md              # Documentação para desenvolvedores
├── version.json               # Controle de versão
└── backups_compatflow/        # Backups de versões
```

---

## 🌐 Banco de Dados

O banco de dados de ports está em: [distroforge-database](https://github.com/lucasgertke11-bot/distroforge-database)

### Gerenciadores de arquivos suportados

| Ambiente | Gerenciador | Status |
|----------|-------------|--------|
| 🐧 KDE | Dolphin | ✅ |
| 🎨 GNOME | Nautilus | ✅ |
| ⚡ XFCE | Thunar | ✅ |
| 🖥️ GTK | Files (Nemo, Caja, PCManFM) | ✅ |

---

## 🔧 Comandos

```bash
compatflow                    # Abrir interface gráfica
compatflow arquivo.exe       # Verificar arquivo específico
compatflow --update           # Atualizar banco de dados
compatflow --check-update    # Verificar nova versão
compatflow --upgrade         # Atualizar próprio CompatFlow
```

---

## 🎯 Para Quem é?

- **Usuários migrando do Windows** para Linux
- **Iniciantes** em Linux que querem facilitar
- **Gamers** que querem jogar no Linux
- **Profissionais** que precisam de compatibilidade Windows

---

## 🔄 Atualização

O CompatFlow atualiza o banco de dados automaticamente. Para forçar atualização:

```bash
compatflow --update
```

---

## 📝 Contribuir

Encontrou um programa que não está no banco?

1. Abra o `.exe` com o CompatFlow
2. Clique em **"📨 Solicitar Suporte"**
3. Escreva por que você quer esse programa
4. O desenvolvedor será notificado!

---

## 📄 Licença

GPL-3.0 License - Livre para usar, modificar e distribuir.

---

<div align="center">

**Feito com ❤️ para ajudar na migração Windows → Linux**

**Desenvolvido por:** [lucasgertke11-bot](https://github.com/lucasgertke11-bot)

</div>
