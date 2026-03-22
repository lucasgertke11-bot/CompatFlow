# 🔍 CRYPy

**Verificador de Compatibilidade Windows → Linux**

CRYPy é um aplicativo que detecta programas Windows (.exe) e verifica se existe versão nativa Linux ou port disponível (via Lutris).

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Funcionalidades

- 🔍 Detecta programas Windows
- 🐧 Verifica versão nativa Linux
- 🎮 Suporte a ports via Lutris
- 🍷 Opção de executar com Wine
- 📤 Sistema de solicitações (reports)

## 📦 Instalação

```bash
git clone https://github.com/lucasgertke11-bot/crypy.git
cd crypy
sudo bash install-crypy.sh
```

## 🔧 Configuração

Após instalar, configure o token GitHub:

```bash
echo "SEU_TOKEN" > ~/.config/crypy/token
crypy --update
```

## 🎮 Uso

1. Clique com **botão direito** em qualquer arquivo `.exe`
2. Selecione **"🔍 Verificar Disponibilidade"**
3. O CRYPy detecta automaticamente:
   - ✅ Versão nativa Linux disponível
   - 🎮 Port via Lutris disponível
   - ❌ Não encontrado

## 📁 Estrutura do Projeto

```
crypy/
├── crypy.py              # Aplicativo principal
├── install-crypy.sh      # Script de instalação
├── uninstall-crypy.sh    # Script de desinstalação
├── README_DEV.md         # Documentação para desenvolvedores
└── version.json         # Controle de versão
```

## 🔄 Atualização

```bash
# Atualizar cache de ports
crypy --update

# Verificar atualizações
crypy --check-update

# Atualizar próprio CRYPy
crypy --upgrade
```

## 📝 Adicionar Novos Ports

Consulte o [README_DEV.md](README_DEV.md) para documentação completa sobre como adicionar novos jogos/programas.

## 🌐 Banco de Dados

O banco de dados de ports está em: [distroforge-database](https://github.com/lucasgertke11-bot/distroforge-database)

## 📄 Licença

MIT License - Veja [LICENSE](LICENSE)

---

Desenvolvido por [lucasgertke11-bot](https://github.com/lucasgertke11-bot)
