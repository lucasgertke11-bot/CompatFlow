# CompatFlow - Guia de Desenvolvimento

## O que é o CompatFlow?

CompatFlow é um verificador de compatibilidade que:
- Detecta programas Windows (.exe)
- Verifica se existe versão nativa Linux
- Verifica se existe "port" (instalação via Lutris)
- Instala automaticamente usando o script correto

---

## Estrutura do Projeto

```
compatflow/
├── compatflow.py              # Aplicativo principal
├── install-compatflow.sh      # Script de instalação
├── uninstall-compatflow.sh    # Script de desinstalação
└── README_DEV.md        # Este arquivo
```

---

## Como Funciona

### 1. Detecção
```
Usuário clica em VioletSetup.exe
       ↓
CompatFlow extrai nome: "violet"
       ↓
Busca no cache local (~/.config/compatflow/ports.json)
       ↓
Encontra correspondência → mostra "Port via LUTRIS"
```

### 2. Instalação via Port
```
Clica em "Instalar Port"
       ↓
CompatFlow copia VioletSetup.exe → /tmp/compatflow_install/setup.exe
       ↓
Baixa script YML do GitHub
       ↓
Modifica YML: $SCRIPTDIR/setup.exe
       ↓
Executa: lutris -i /tmp/compatflow_install/installer.yml
       ↓
Lutris instala o jogo automaticamente
```

---

## Como Adicionar um Novo Jogo

### Passo 1: Criar o Script YML do Lutris

Crie um arquivo `nome_do_jogo.yml` com esta estrutura:

```yaml
name: Nome do Jogo
game_slug: nome-do-jogo
version: Nome do Servidor/Port
slug: nome-do-jogo-port
runner: wine

script:
  game:
    arch: win64
    exe: $GAMEDIR/drive_c/PastaDoJogo/Launcher.exe
    prefix: $GAMEDIR
  
  installer:
  - input_menu:
      description: 'Escolha o idioma:'
      id: LANG
      options:
      - PT: Português
      - EN: English
      preselect: PT
  
  - task:
      executable: $SCRIPTDIR/setup.exe
      name: wineexec
```

**Importante:**
- Use `$SCRIPTDIR/setup.exe` para installations automáticas
- `$GAMEDIR` é onde o Lutris vai instalar o jogo
- O `input_menu` é opcional (pode remover se não precisar)

### Passo 2: Hospedar o YML

Hospede o arquivo YML no repositório GitHub:
```
distroforge-database/data/ports/scripts/nome_do_jogo.yml
```

URL: `https://github.com/lucasgertke11-bot/distroforge-database/tree/main/data/ports/scripts`

### Passo 3: Adicionar ao ports.json

Edite o arquivo `data/ports/ports.json` no GitHub:

```json
{
  "nome_do_jogo": {
    "name": "Nome do Jogo (Servidor)",
    "type": "lutris",
    "keywords": ["nome", "keywords", "para", "detectar"],
    "description": "Descrição do jogo",
    "dependencies": {
      "arch": ["lutris", "wine"],
      "ubuntu": ["lutris", "wine"],
      "fedora": ["lutris", "wine"]
    },
    "install": {
      "type": "lutris",
      "script_url": "https://raw.githubusercontent.com/lucasgertke11-bot/distroforge-database/main/data/ports/scripts/nome_do_jogo.yml"
    }
  }
}
```

**Campos:**
- `name`: Nome exibição
- `type`: Sempre "lutris" por enquanto
- `keywords`: Palavras para detectar (case insensitive)
- `description`: Descrição breve
- `dependencies`: Pacotes necessários por distro
- `script_url`: URL RAW do YML no GitHub

### Passo 4: Testar

```bash
# Atualizar cache local
compatflow --update

# Testar detecção
compatflow --test /caminho/ate/jogo.exe
```

---

## Exemplo Completo: Grand Fantasia (Violet)

### YML (grand_fantasia.yml)
```yaml
name: Grand Fantasia (Violet)
game_slug: grand-fantasia
version: Violet
slug: grand-fantasia-violet
runner: wine

script:
  game:
    arch: win64
    exe: $GAMEDIR/drive_c/X-Legend/GrandFantasia$INPUT_LANG/Launcher.exe
    prefix: $GAMEDIR
  
  installer:
  - input_menu:
      description: 'Choose the game language:'
      id: LANG
      options:
      - PT: Portuguese
      - EN: English
      - FR: French
      - ES: Spanish
      preselect: pt
  
  - task:
      executable: $SCRIPTDIR/setup.exe
      name: wineexec
```

### Entrada no ports.json
```json
"violet": {
  "name": "Grand Fantasia (Violet)",
  "type": "lutris",
  "keywords": ["violet", "grandfantasia", "gfantasia", "gfa", "grand_fantasia"],
  "description": "MMORPG - Servidor Private Violet",
  "dependencies": {
    "arch": ["lutris", "wine"],
    "ubuntu": ["lutris", "wine"],
    "fedora": ["lutris", "wine"]
  },
  "install": {
    "type": "lutris",
    "script_url": "https://raw.githubusercontent.com/lucasgertke11-bot/distroforge-database/main/data/ports/scripts/grand_fantasia.yml"
  }
}
```

---

## Comandos Úteis

```bash
# Atualizar cache do CompatFlow
compatflow --update

# Testar detecção de arquivo
compatflow --test /caminho/até/arquivo.exe

# Verificar cache local
cat ~/.config/compatflow/ports.json

# Limpar cache
rm ~/.config/compatflow/ports.json
```

---

## Variáveis do YML (Lutris)

| Variável | Descrição |
|----------|-----------|
| `$GAMEDIR` | Pasta onde o jogo será instalado |
| `$SCRIPTDIR` | Pasta onde está o script YML |
| `$INPUT_LANG` | Valor selecionado no input_menu |
| `$CACHE` | Pasta temporária do Lutris |
| `$WINEBIN` | Caminho do Wine do Lutris |

---

## Tasks do Lutris (YML)

### wineexec - Executar .exe
```yaml
- task:
    name: wineexec
    executable: $SCRIPTDIR/setup.exe
```

### create_prefix - Criar prefixo Wine
```yaml
- task:
    name: create_prefix
    arch: win64
```

### winetricks - Instalar dependências
```yaml
- task:
    name: winetricks
    app: vcrun2019 dotnet48
```

---

## Referências

- [Documentação Lutris](https://github.com/lutris/lutris/blob/master/docs/installers.rst)
- [Site Lutris](https://lutris.net/)
- [Repositório CompatFlow](https://github.com/lucasgertke11-bot/distroforge-database)

---

## Fluxo Resumido

```
1. Você: Cria script YML do jogo
2. Você: Hospeda no GitHub
3. Você: Adiciona entrada no ports.json
4. CompatFlow: Usuário atualiza cache (--update)
5. CompatFlow: Detecta automaticamente
6. CompatFlow: Copia exe → modifica YML → executa Lutris
7. Lutris: Instala o jogo
```
