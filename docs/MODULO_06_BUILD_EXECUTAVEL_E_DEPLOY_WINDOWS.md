# Módulo 06 — Geração de Executáveis Windows (`.exe`), Empacotamento de Recursos e Instalação Nativa

Um projeto de engenharia completo não deve exigir que o usuário final abra um terminal e digite comandos Python para utilizar o software. Neste módulo final, transformamos tanto a **Calculadora Gráfica** (`main.py`) quanto a **Plataforma Gráfica do Sistema de Educação, Proctoring e Certificação SHA-256** (`app_educacao.py`) em **executáveis nativos do Windows (`.exe`)**, instalados no sistema operacional com atalhos no Menu Iniciar e na Área de Trabalho.

---

## 1. Como o `PyInstaller` Empacota uma Aplicação Python em `.exe`

O **PyInstaller** analisa a árvore de importações do seu script principal, coleta o interpretador Python (`python312.dll`), a biblioteca gráfica (`Tcl/Tk`), os módulos do projeto (`calculadora.py`, `src/proctoring.py`, `src/certificador_sha256.py`, `src/avaliador_carrasco.py`) e os arquivos didáticos (`docs/*.md`), empacotando tudo em um único executável autônomo:

```bash
python -m PyInstaller --noconfirm --onefile --windowed --icon calculadora.ico --add-data "docs;docs" --name "Sistema Educacao Calculadora" app_educacao.py
```

### Explicação Técnica de Cada Flag
- `--onefile`: Empacota todos os binários e bibliotecas em um único arquivo `.exe` portátil.
- `--windowed` (ou `--noconsole`): Usa o *bootloader* gráfico do Windows (`runw.exe`), abrindo diretamente a janela do Tkinter sem exibir o prompt preto do `cmd.exe`.
- `--icon calculadora.ico`: Embute o ícone ARGB de 32 bits no cabeçalho PE (*Portable Executable*) do Windows.
- `--add-data "docs;docs"`: Inclui toda a pasta `docs/` (com os 6 módulos em Markdown) dentro do arquivo executável para leitura offline.

---

## 2. O Segredo do `sys._MEIPASS` em Executáveis `--onefile`

Quando um executável `--onefile` é aberto pelo usuário, o *bootloader* do PyInstaller extrai os arquivos embutidos em uma pasta temporária de alta velocidade no sistema operacional e define o caminho dessa pasta no atributo especial `sys._MEIPASS`.

Se o seu código tentar abrir `Path("docs/MODULO_01.md")` usando caminho relativo fixo, ele pode não encontrar os arquivos quando executado a partir de um atalho na Área de Trabalho. A função `obter_caminho_recurso` em `app_educacao.py` resolve isso de forma limpa:

```python
import sys
from pathlib import Path

def obter_caminho_recurso(caminho_relativo: str) -> Path:
    """Resolve o caminho tanto em execução Python normal quanto empacotado via PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent.resolve()))
    candidato = base / caminho_relativo
    if candidato.exists():
        return candidato
    return Path(__file__).parent.resolve() / caminho_relativo
```

---

## 3. Instalação Nativa no Windows (Menu Iniciar, Desktop e Registro `HKCU`)

O instalador automatizado do projeto realiza três integrações nativas com o Windows (sem modificar arquivos do sistema operacional):

1. **Diretório Padrão de Programas do Usuário (`%LOCALAPPDATA%\Programs\CalculadoraPython`):**
   Copia os executáveis `Calculadora Python.exe` e `Sistema Educacao Calculadora.exe` junto com o ícone `calculadora.ico` e os módulos didáticos.
2. **Atalhos `.lnk` no Menu Iniciar e na Área de Trabalho (`WScript.Shell`):**
   Cria os atalhos oficiais em `%APPDATA%\Microsoft\Windows\Start Menu\Programs\` e em `%USERPROFILE%\Desktop\`, permitindo abrir ambos os aplicativos pelo Menu Iniciar ou com dois cliques na Área de Trabalho.
3. **Registro nos Aplicativos Instalados do Windows (`winreg`):**
   Registra o software na chave do usuário `HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall\CalculadoraPython`, exibindo-o na listagem oficial de aplicativos instalados do Windows.
