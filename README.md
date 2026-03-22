# CompatFlow

Verificador de compatibilidade e ports Windows → Linux

## Recursos

- Verifica se programas Windows têm alternativas nativas Linux
- Encontra ports de jogos via Lutris
- Executa apps com Wine
- Menu de contexto nos principais gerenciadores de arquivos
- Banco de dados com +200 apps Linux nativos
- Atualizações automáticas via Supabase

## Instalação

### Método 1: Download direto

```bash
mkdir -p ~/compatflow-temp
cd ~/compatflow-temp
curl -sL "https://github.com/lucasgertke11-bot/CompatFlow/raw/master/install-compatflow.sh" -o install.sh
chmod +x install.sh
sudo bash install.sh
```

### Método 2:克隆 do Git

```bash
git clone https://github.com/lucasgertke11-bot/CompatFlow.git
cd CompatFlow
sudo bash install-compatflow.sh
```

### Método 3: via CompatFlow (se já instalado)

```bash
compatflow --upgrade
```

## Uso

Clique com botão direito em um arquivo `.exe` ou `.msi` e selecione **"🔍 Verificar com CompatFlow"**.

### Comandos

```bash
compatflow                      # Abrir interface
compatflow --update             # Atualizar banco de dados
compatflow --check-update        # Verificar atualizações
compatflow --upgrade            # Baixar atualização
```

## Gerenciadores suportados

- KDE Dolphin
- GNOME Nautilus  
- XFCE Thunar
- Files (Nemo/Caja)
- PCManFM

## Requisitos

- Python 3
- PySide6
- requests
- curl
