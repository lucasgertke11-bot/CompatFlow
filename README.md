# 🔍 CRYPy - Verificador de Compatibilidade Windows → Linux

**CRYPy** é um aplicativo que ajuda usuários vindos do Windows a encontrar versões nativas de seus programas favoritos no Linux.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 💡 Ideia Fundamental

Você está migrando do Windows para o Linux e encontrou um `.exe` que quer instalar?

O CRYPy verifica automaticamente:
- ✅ Se existe versão **nativa Linux** desse programa
- 🎮 Se existe **port via Lutris** (para jogos)
- 🍷 Se pode rodar com **Wine**

**Tudo em um clique!**

---

## ✨ Funcionalidades

| Recurso | Descrição |
|---------|-----------|
| 🔍 **Detecção automática** | Identifica qualquer arquivo `.exe` |
| 🐧 **275+ apps nativos** | Firefox, Discord, VS Code, Steam e muito mais |
| 🎮 **Ports via Lutris** | Instalação automática de jogos Windows |
| 🍷 **Wine integrado** | Executa programas que não têm alternativa |
| 📤 **Sistema de reports** | Solicite suporte para apps não encontrados |
| 🔄 **Atualização automática** | Banco de dados sempre atualizado |
| 🌐 **Multi-distro** | Arch, Ubuntu, Fedora, openSUSE... |

---

## 📦 Instalação

### Método 1: Clone e instale
```bash
git clone https://github.com/lucasgertke11-bot/crypy.git
cd crypy
sudo bash install-crypy.sh
```

### Método 2: Apenas configure o token
```bash
# Configure seu token GitHub
echo "SEU_TOKEN" > ~/.config/crypy/token

# Atualize o banco de dados
crypy --update
```

---

## 🎮 Como Usar

1. **Clique com botão direito** em qualquer arquivo `.exe`
2. Selecione **"🔍 Verificar Disponibilidade"**
3. O CRYPy detecta automaticamente:

```
✅ Nativo Linux disponível
   → Clique "Instalar Nativo"

🎮 Port via Lutris disponível
   → Clique "Instalar Port"

❌ Não encontrado
   → Clique "Solicitar Suporte"
```

---

## 📁 Estrutura do Projeto

```
crypy/
├── crypy.py              # Aplicativo principal
├── install-crypy.sh     # Script de instalação
├── uninstall-crypy.sh    # Script de desinstalação
├── backups/              # Backups de versões
├── README_DEV.md         # Documentação para desenvolvedores
└── version.json         # Controle de versão
```

---

## 🌐 Banco de Dados

O banco de dados de ports está em: [distroforge-database](https://github.com/lucasgertke11-bot/distroforge-database)

### Adicionar um novo jogo/port

Consulte o [README_DEV.md](README_DEV.md) para documentação completa.

---

## 🔧 Comandos

```bash
crypy --update        # Atualizar banco de dados
crypy --check-update  # Verificar nova versão
crypy --upgrade       # Atualizar próprio CRYPy
crypy --test arquivo.exe  # Testar detecção
```

---

## 🎯 Para Quem é?

- **Usuários migrating do Windows** para Linux
- **Iniciantes** em Linux que querem facilitar
- **Gamers** que querem jogar no Linux
- **Profissionais** que precisam de compatibilidade

---

## 🔄 Atualização de Banco

O banco de dados é atualizado automaticamente quando você abre o CRYPy. Para forçar atualização:

```bash
crypy --update
```

---

## 📝 Contribuir

Encontrou um programa que não está no banco?

1. Abra o `.exe` com o CRYPy
2. Clique em **"Solicitar Suporte"**
3. Escreva por que você quer esse programa
4. O desenvolvedor será notificado!

---

## 📄 Licença

MIT License - Livre para usar, modificar e distribuir.

---

**Feito com ❤️ para ajudar na migração Windows → Linux**

**Desenvolvido por:** lucasgertke11-bot
