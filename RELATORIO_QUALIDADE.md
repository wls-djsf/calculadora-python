# Relatório de Desenvolvimento e Engenharia de Qualidade — Calculadora Python & Sistema de Educação e Certificação (SHA-256)

## 1. Análise Inicial e Plano de Execução

### 1.1. Inspeção Inicial do Diretório
Na inspeção inicial do workspace (`c:\Users\HORUS\Documents\Calculadora Python`), constatou-se a presença exclusiva do documento de especificação [PLANO CALCULADORA.docx](file:///c:/Users/HORUS/Documents/Calculadora%20Python/PLANO%20CALCULADORA.docx), a partir do qual foram construídos tanto a **Calculadora Python** quanto o **Sistema Completo de Educação, Proctoring Simulado e Certificação Criptográfica (SHA-256)** e seus respectivos **Executáveis Nativos para Windows (`.exe`)**.

### 1.2. Extração da Arquitetura e dos Módulos do Projeto
1. **`calculadora.py`** (`TODO 01` a `TODO 10`): Estruturação da classe `Calculadora`, adição, subtração, multiplicação, divisão (com proteção contra divisão por zero), porcentagem contextual, inversão de sinal, validação de dados (`ErroEntradaInvalida`), tratamento de precisão decimal (`Decimal`) e revisão de responsabilidades (sem dependência do Tkinter).
2. **`main.py`** (`TODO 01` a `TODO 13`): Configuração da janela principal Tkinter, identidade visual em paleta roxa e lavanda (`PALETA_CORES`), estrutura em grade, visor duplo (histórico e principal), botões numéricos, botões de operação, botões de controle (`C`, `CE`, `⌫`, `±`), integração com `Calculadora`, eventos de teclado físico, máquina de estados da interface e recuperação automática de erros.
3. **Subsistema de Educação, Proctoring e Certificação (`src/` e `verify_certificate.py`)**:
   - `src/proctoring.py`: Sensores simulados (`SensorWebcamMock`, `SensorAudioMock`, `SensorJanelaMock`) e motor `SessaoProctoring` com pontuação de risco e regras de infração.
   - `src/certificador_sha256.py`: Emissor e verificador criptográfico `CertificadorSHA256` com JSON canônico, `SHA-256`, `HMAC-SHA256` e `hmac.compare_digest`.
   - `src/avaliador_carrasco.py`: Motor `AvaliadorCarrasco` que submete `Calculadora` a 5 baterias de testes reais e integra o resultado ao `SessaoProctoring` e `CertificadorSHA256`.
   - `verify_certificate.py`: Utilitário CLI de auditoria pública para validar certificados `.json` e detectar adulterações.
4. **Aplicação Gráfica e Executáveis Nativos Windows (`app_educacao.py` e `instalar_sistema_windows.py`)**:
   - `app_educacao.py`: Plataforma Desktop Tkinter (`InterfaceSistemaEducacao`) com 3 abas interativas (Curso Carrasco com os 6 módulos em Markdown, Simulador de Proctoring + Exame Carrasco + Certificador SHA-256, e Laboratório Prático com a Calculadora integrada) e suporte a empacotamento `PyInstaller` (`sys._MEIPASS`).
   - `Sistema Educacao Calculadora.exe` e `Calculadora Python.exe`: Executáveis nativos Windows (`--onefile --windowed`).
   - `instalar_sistema_windows.py`: Instalador nativo para Windows que copia os executáveis para `%LOCALAPPDATA%\Programs\CalculadoraPython`, cria atalhos `.lnk` no Menu Iniciar e na Área de Trabalho e registra os aplicativos em `HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall`.
5. **Material Didático Modo Carrasco (`docs/`)**:
   - `docs/MODULO_01_CLEAN_CODE_E_ARQUITETURA.md`
   - `docs/MODULO_02_TRATAMENTO_DE_EXCECOES_BLINDADO.md`
   - `docs/MODULO_03_TDD_PYTEST_E_MUTACAO.md`
   - `docs/MODULO_04_PROCTORING_E_INTEGRIDADE_DE_EXAME.md`
   - `docs/MODULO_05_CRIPTOGRAFIA_SHA256_E_CERTIFICACAO.md`
   - `docs/MODULO_06_BUILD_EXECUTAVEL_E_DEPLOY_WINDOWS.md`

---

## 2. Arquivos Criados / Modificados e Funcionalidades Implementadas

| Arquivo | Papel Arquitetural | Funcionalidades Implementadas |
|---|---|---|
| `calculadora.py` | Lógica de Negócio | Classe `Calculadora` e exceção `ErroEntradaInvalida`; métodos `validar_numero`, `_formatar_resultado`, `somar`, `subtrair`, `multiplicar`, `dividir`, `porcentagem` (contextual), `inverter_sinal`, `calcular` e `calcular_encadeado`. Todos os `TODO 01`–`10` preservados. |
| `main.py` | Interface Gráfica da Calculadora | Classe `InterfaceCalculadora`, `PALETA_CORES` (tema roxo/lavanda), `FONTES` e `iniciar_aplicacao`. Visor duplo, grade responsiva de 20 botões, atalhos de teclado e controles `C`, `CE`, `⌫`, `±`. Todos os `TODO 01`–`13` preservados. |
| `app_educacao.py` | Plataforma Gráfica do Sistema de Educação | Classe `InterfaceSistemaEducacao`, `obter_caminho_recurso` (`sys._MEIPASS`) e `iniciar_plataforma_educacao`. Integra leitor dos 6 módulos do curso, simulador de Proctoring, exame Carrasco + certificado SHA-256 e laboratório da Calculadora. |
| `src/proctoring.py` | Motor de Proctoring Simulado | `SensorWebcamMock`, `SensorAudioMock`, `SensorJanelaMock`, `RegistroInfracao` e `SessaoProctoring` com auditoria determinística de integridade de exame. |
| `src/certificador_sha256.py` | Motor Criptográfico SHA-256 | `CertificadorSHA256` e `ErroCertificacaoReprovada` com hash `SHA-256`, assinatura `HMAC-SHA256` e comparação em tempo constante (`hmac.compare_digest`). |
| `src/avaliador_carrasco.py` | Avaliador Técnico Automatizado | `AvaliadorCarrasco` validando precisão `Decimal`, blindagem de tipos, divisão por zero, porcentagem contextual e encadeamento antes de autorizar o certificado. |
| `verify_certificate.py` | Validador CLI de Certificados | Script de linha de comando e API (`validar_arquivo_certificado`, `gerar_e_verificar_demonstracao`) para verificação pública de certificados JSON. |
| `instalar_sistema_windows.py` | Instalador Nativo Windows | Instala `Calculadora Python.exe` e `Sistema Educacao Calculadora.exe` em `%LOCALAPPDATA%\Programs\CalculadoraPython`, cria atalhos `.lnk` no Menu Iniciar e Área de Trabalho e registra no Registro do Windows (`winreg`). |
| `tests/test_calculadora.py` | Testes Unitários | 26 métodos `unittest.TestCase` + 69 execuções parametrizadas `@pytest.mark.parametrize` (total de 95 itens de teste unitário). |
| `tests/test_interface.py` | Testes de Integração | 15 testes de integração verificando widgets Tkinter reais, sincronização de visor/histórico, teclado, recuperação de erros e `MagicMock`. |
| `tests/features/calculadora.feature` | Especificação BDD (Gherkin) | 11 cenários de aceitação em linguagem natural (`# language: pt`). |
| `tests/test_bdd_calculadora.py` | Conector Executável BDD | Definições de passos (`@given`, `@when`, `@then`) conectando `calculadora.feature` à `InterfaceCalculadora` e `Calculadora`. |
| `tests/test_sistema_educacao.py` | Testes do Sistema de Educação | 21 testes cobrindo Proctoring Simulado, Certificador SHA-256, Avaliador Carrasco, CLI `verify_certificate.py` e a GUI `InterfaceSistemaEducacao` (`app_educacao.py`). |
| `verificar_qualidade.py` | Automação da Qualidade | Executor unificado de testes unitários, BDD, integração, sistema de educação, cobertura HTML/JSON/texto, métricas Radon, cálculo de CRAP e motor AST de Testes de Mutação. |

---

## 3. Resultados da Execução de Testes

Todos os comandos foram executados no ambiente real (`Python 3.12.10` em Windows):

| Suíte de Testes | Ferramenta | Quantidade Executada | Aprovados | Reprovados | Tempo |
|---|---|---:|---:|---:|---:|
| Testes Unitários Clássicos | `unittest` | 26 | 26 | 0 | 0.002s |
| Testes Unitários + Parametrizados (`test_calculadora.py`) | `pytest` | 95 | 95 | 0 | 0.28s |
| Testes de Aceitação BDD (`test_bdd_calculadora.py`) | `pytest-bdd` | 11 | 11 | 0 | 0.12s |
| Testes de Integração (`test_interface.py`) | `pytest` / `unittest` | 15 | 15 | 0 | 0.82s |
| Testes do Sistema de Educação, Proctoring, SHA-256 e GUI (`test_sistema_educacao.py`) | `pytest` / `unittest` | 21 | 21 | 0 | 0.41s |
| **Total Consolidado (`pytest`)** | `pytest` | **142** | **142** | **0** | **1.37s** |

---

## 4. Cobertura de Código e Ramificações (`coverage.py`)

Medição executada com `python -m coverage run --branch --source=calculadora,main,src,verify_certificate,app_educacao -m pytest`:

| Módulo | Declarações (`Stmts`) | Não Executadas (`Miss`) | Ramificações (`Branch`) | Ramificações Parciais (`BrPart`) | Cobertura Total (`Cover`) | Linhas Faltantes |
|---|---:|---:|---:|---:|---:|---|
| `calculadora.py` | 54 | 0 | 16 | 0 | **100%** | Nenhuma |
| `main.py` | 233 | 0 | 62 | 0 | **100%** | Nenhuma |
| `src/__init__.py` | 0 | 0 | 0 | 0 | **100%** | Nenhuma |
| `src/avaliador_carrasco.py` | 43 | 0 | 2 | 0 | **100%** | Nenhuma |
| `src/certificador_sha256.py` | 72 | 0 | 22 | 0 | **100%** | Nenhuma |
| `src/proctoring.py` | 59 | 0 | 8 | 0 | **100%** | Nenhuma |
| `verify_certificate.py` | 47 | 0 | 4 | 0 | **100%** | Nenhuma |
| `app_educacao.py` | 180 | 0 | 26 | 6 | **97%** (100% linhas) | Nenhuma linha faltante (`0 Miss`) |
| **TOTAL** | **688** | **0** | **140** | **6** | **99% (100% Stmts)** | **Nenhuma (`0 Miss`)** |

- **Relatório HTML gerado em:** `htmlcov/index.html`
- **Relatório JSON gerado em:** `coverage.json`

---

## 5. Resultado dos Testes de Mutação

### 5.1. Nota Técnica sobre o CLI `mutmut` no Windows
Ao executar `python -m mutmut` diretamente no Windows, a ferramenta encerra com a mensagem oficial:
> `To run mutmut on Windows, please use the WSL. Native windows support is tracked in issue https://github.com/boxed/mutmut/issues/397`

Isso ocorre porque o `mutmut 3.x` depende da chamada de sistema `os.fork()` exclusiva de sistemas Unix/POSIX.

### 5.2. Execução Real de Mutação via AST (`verificar_qualidade.py`)
Para garantir a verificação real de mutações no ambiente Windows sem depender de WSL, foi implementado em `verificar_qualidade.py` um motor determinístico de mutação em árvore sintática (`gerar_mutantes_ast` / `executar_testes_mutacao`) que aplica mutações individuais sobre `calculadora.py` nas 5 categorias exigidas e executa a suíte `pytest tests/test_calculadora.py` contra cada mutante:

- **Total de Mutações Geradas e Testadas:** **30**
- **Mutações Eliminadas (`KILLED`):** **30 (100.00%)**
- **Mutações Sobreviventes (`SURVIVED`):** **0 (0.00%)**
- **Mutações Equivalentes:** **0**

---

## 6. Métricas de Complexidade (`Radon`) e Pontuação CRAP

### 6.1. Resumo Estrutural e Índice de Manutenibilidade
- **Complexidade Ciclomática Média:** **2.49 (Nota A)** em 89 blocos analisados.
- **Índice de Manutenibilidade (`radon mi`):**
  - `calculadora.py`: **61.25 — Nota A**
  - `main.py`: **47.92 — Nota A**
  - `src/proctoring.py`: **52.61 — Nota A**
  - `src/certificador_sha256.py`: **53.08 — Nota A**
  - `src/avaliador_carrasco.py`: **64.94 — Nota A**
  - `verify_certificate.py`: **71.64 — Nota A**
  - `app_educacao.py`: **40.98 — Nota A**
- **Tamanho Total do Código Analisado (`radon raw`):** `1628 LOC` (`1122 SLOC`, `830 LLOC`).

### 6.2. Tabela Completa de Pontuação CRAP (Referência: $\text{CRAP} \le 12$)
Fórmula aplicada:
$$\text{CRAP}(m) = \text{comp}(m)^2 \times \left(1 - \frac{\text{cov}(m)}{100}\right)^3 + \text{comp}(m)$$

Todas as **69 funções e métodos** do projeto possuem **100.0% de cobertura de linhas** e pontuação **$\text{CRAP} \le 10.00$** (abaixo do limite máximo de `12.00`):

| Arquivo | Função / Método | Complexidade (`CC`) | Cobertura | Pontuação `CRAP` | Status ($\le 12$) |
|---|---|---:|---:|---:|---|
| `calculadora.py` | `Calculadora.validar_numero` | 4 | 100.0% | **4.00** | OK (<=12) |
| `calculadora.py` | `Calculadora._formatar_resultado` | 2 | 100.0% | **2.00** | OK (<=12) |
| `calculadora.py` | `Calculadora.somar` / `subtrair` / `multiplicar` / `inverter_sinal` | 1 | 100.0% | **1.00** | OK (<=12) |
| `calculadora.py` | `Calculadora.dividir` / `calcular` / `calcular_encadeado` | 2 | 100.0% | **2.00** | OK (<=12) |
| `calculadora.py` | `Calculadora.porcentagem` | 4 | 100.0% | **4.00** | OK (<=12) |
| `main.py` | `InterfaceCalculadora` (todos os 22 métodos + `iniciar_aplicacao`) | 1 a 5 | 100.0% | **1.00 a 5.00** | OK (<=12) |
| `src/proctoring.py` | `SessaoProctoring.__init__` | 6 | 100.0% | **6.00** | OK (<=12) |
| `src/proctoring.py` | `SessaoProctoring.inspecionar_ambiente` | 4 | 100.0% | **4.00** | OK (<=12) |
| `src/proctoring.py` | Demais métodos de `SessaoProctoring` | 1 a 3 | 100.0% | **1.00 a 3.00** | OK (<=12) |
| `src/certificador_sha256.py` | `CertificadorSHA256.verificar_certificado` | 10 | 100.0% | **10.00** | OK (<=12) |
| `src/certificador_sha256.py` | `CertificadorSHA256._validar_requisitos_aprovacao` | 6 | 100.0% | **6.00** | OK (<=12) |
| `src/certificador_sha256.py` | Demais métodos de `CertificadorSHA256` | 1 a 4 | 100.0% | **1.00 a 4.00** | OK (<=12) |
| `src/avaliador_carrasco.py` | `AvaliadorCarrasco` (todos os 8 métodos) | 1 a 5 | 100.0% | **1.00 a 5.00** | OK (<=12) |
| `verify_certificate.py` | `validar_arquivo_certificado` / `gerar_e_verificar_demonstracao` / `main` | 1 a 6 | 100.0% | **1.00 a 6.00** | OK (<=12) |
| `app_educacao.py` | `InterfaceSistemaEducacao` (todos os 14 métodos + 2 funções) | 1 a 5 | 100.0% | **1.00 a 5.00** | OK (<=12) |

---

## 7. Executáveis Windows e Instalação Local

Foram gerados e instalados dois executáveis nativos independentes (`.exe`) via `PyInstaller`:
1. **`Calculadora Python.exe`**: Aplicação gráfica da Calculadora Python.
2. **`Sistema Educacao Calculadora.exe`**: Plataforma gráfica completa contendo os 6 módulos do curso Carrasco embutidos (`--add-data "docs;docs"`), Simulador Interativo de Proctoring, Exame Carrasco + Emissor/Verificador de Certificados SHA-256 e Laboratório Prático da Calculadora.

Ambos encontram-se instalados em:
- Diretório do Projeto: `c:\Users\HORUS\Documents\Calculadora Python\`
- Diretório Oficial de Programas do Usuário: `C:\Users\HORUS\AppData\Local\Programs\CalculadoraPython\`
- Atalhos no Menu Iniciar: `C:\Users\HORUS\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\`
- Atalhos na Área de Trabalho: `C:\Users\HORUS\Desktop\`
