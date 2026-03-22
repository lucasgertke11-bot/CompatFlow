# 🔍 CompatFlow

<div align="center">
  <img src="https://raw.githubusercontent.com/lucasgertke11-bot/CompatFlow/master/compatflow.svg" width="128" height="128">
  <br><br>
  <b>Verificador de compatibilidade e ports Windows → Linux</b>
</div>

---

## 🎯 O que é o CompatFlow?

O CompatFlow é um aplicativo que ajuda usuários Linux a encontrar alternativas nativas, ports de jogos (via Lutris) ou executar programas Windows com Wine.

**Ideal para quem está começando no Linux e não quer usar terminal.**

## ✨ Recursos

- ✅ Verifica se programas Windows têm alternativas nativas Linux
- ✅ Encontra ports de jogos via Lutris
- ✅ Executa apps com Wine
- ✅ Menu de contexto nos principais gerenciadores de arquivos
- ✅ Banco de dados com +200 apps Linux nativos
- ✅ Atualizações automáticas de ports

## 🛡️ Segurança e Transparência

### Código Aberto
- Todo o código está disponível aqui no GitHub
- Você pode verificar exatamente o que o app faz

### Como solicitamos dados?
- **Nunca coletamos dados pessoais desnecessários**
- Quando você solicita suporte para um programa, apenas armazenamos:
  - Nome do programa
  - Sua mensagem (opcional)
  - Data da solicitação
- Os dados são armazenados no Supabase (banco de dados seguro)

### Posso contribuir?
Sim! Você pode:
1. Reportar programas que não estão no banco de dados
2. Solicitar ports para jogos/apps específicos
3. Contribuir com código no GitHub

## 📦 Instalação

```bash
git clone https://github.com/lucasgertke11-bot/CompatFlow.git
cd CompatFlow
sudo bash install-compatflow.sh
```

Após instalar, reinicie o gerenciador de arquivos.

## 🚀 Como usar

1. **Clique com botão direito** em um arquivo .exe ou .msi
2. Selecione "🔍 Verificar com CompatFlow"
3. O app mostra se existe:
   - Alternativa nativa Linux
   - Port disponível (Lutris)
   - Ou opção de rodar com Wine

### Comandos

```bash
compatflow                    # Abrir interface
compatflow --update          # Atualizar banco de ports
compatflow --check-update    # Verificar atualizações do app
compatflow --upgrade         # Atualizar o app
```

## 🖥️ Gerenciadores suportados

- KDE Dolphin ✓
- GNOME Nautilus ✓
- XFCE Thunar ✓
- Files (Nemo/Caja) ✓

## 📋 Requisitos

- Python 3
- PySide6
- requests
- curl

## 📄 Licença

MIT License - Livre para usar e modificar.

---

**Feito com ❤️ para ajudar quem está migrando para o Linux**