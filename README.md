# Sistema de Educação e Certificação em Engenharia de Software — Calculadora Python (Clean Code & TDD)

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Windows EXE](https://img.shields.io/badge/Windows-Execut%C3%A1veis%20.EXE%20Nativos-0078D6?logo=windows&logoColor=white)
![Metodologia](https://img.shields.io/badge/Did%C3%A1tica-Carrasco%20%28Rocketseat%20Style%29-8B5CF6)
![Arquitetura](https://img.shields.io/badge/Clean%20Code-Uncle%20Bob-2EA043)
![Testes](https://img.shields.io/badge/Testes%20Automatizados-142%20Aprovados-2EA043)
![Cobertura](https://img.shields.io/badge/Cobertura%20%28Linhas%20%26%20Branches%29-100%25-2EA043)
![Criptografia](https://img.shields.io/badge/Certifica%C3%A7%C3%A3o-SHA--256%20%26%20Proctoring-F59E0B)

## Propósito do Curso e Filosofia Pedagógica ("Modo Carrasco")

Este projeto vai muito além de uma simples calculadora em Python: trata-se de um **Sistema Completo de Educação, Avaliação Automatizada, Supervisão de Exame (*Proctoring*), Certificação Criptográfica (SHA-256) e Distribuição Nativa para Windows (`.exe`)** projetado sob inspiração direta das práticas de **Robert C. Martin (*Uncle Bob*)** e da didática imersiva *hands-on* (*Rocketseat Style*).

Aqui o aluno **não é aprovado apenas porque "o código rodou"**. O foco absoluto é forçar o **aprendizado profundo**, a separação rigorosa de responsabilidades, o domínio das armadilhas internas da linguagem Python e a construção de testes capazes de sobreviver a mutações sintáticas:
- Se o código acoplar regras de negócio com `Tkinter` $\rightarrow$ **Reprovado**.
- Se `0.1 + 0.2` retornar `0.30000000000000004` por desconhecimento da norma IEEE 754 e `decimal.Decimal` $\rightarrow$ **Reprovado**.
- Se `somar(True, 5)` retornar `6` por não saber que `bool` herda de `int` em Python $\rightarrow$ **Reprovado**.
- Se houver mutantes sobreviventes ou pontuação $\text{CRAP} > 12$ $\rightarrow$ **Reprovado**.
- Se o motor de *Proctoring* detectar fraude durante o exame $\rightarrow$ **Certificado Bloqueado**.

---

## A Parceria de Engenharia: Gemini & Antigravity

Este ecossistema educacional e técnico foi construído através da sinergia direta entre duas inteligências artificiais especializadas:

| Agente | Papel na Arquitetura e Execução |
|---|---|
| **Gemini** *(Concepção, Arquitetura Pedagógica e Prompt Engineering)* | Idealização da metodologia didática "Carrasco", definição das diretrizes de segurança e autonomia, estruturação dos requisitos de *Proctoring* simulado, modelagem da certificação via SHA-256 e engenharia do plano mestre de execução. |
| **Antigravity** *(Execução Técnica Autônoma, Código, QA, Empacotamento Windows e DevOps)* | Implementação 100% autônoma em Python do motor matemático (`Decimal`), interfaces gráficas (`main.py` e `app_educacao.py`), subsistema de *Proctoring* com *Hardware Mocks*, motor criptográfico `SHA-256`, validador `verify_certificate.py`, compilação dos executáveis Windows (`Sistema Educacao Calculadora.exe` e `Calculadora Python.exe`), instalador nativo (`instalar_sistema_windows.py`), bateria de 142 testes (`unittest`, `pytest`, `pytest-bdd`), motor AST de Testes de Mutação, métricas `Radon`/`CRAP` e publicação automatizada no GitHub. |

---

## Estrutura Arquitetural do Projeto (`/src`, `/tests`, `/docs` e Executáveis Windows)

```text
sistema-educacao-calculadora-python/
├── Sistema Educacao Calculadora.exe                       # Executável Windows Nativo da Plataforma de Educação & SHA-256
├── Calculadora Python.exe                                 # Executável Windows Nativo da Calculadora Gráfica
├── app_educacao.py                                        # Interface Gráfica (Tkinter) da Plataforma de Educação e Proctoring
├── main.py                                                # Interface Gráfica (Tkinter) da Calculadora (Tema Roxo e Lavanda)
├── calculadora.py                                         # Módulo de Domínio Matemático (100% Cobertura, 0 Mutantes Vivos)
├── instalar_sistema_windows.py                            # Instalador Nativo Windows (Menu Iniciar, Desktop e Registro HKCU)
├── verify_certificate.py                                  # CLI e Validador Criptográfico Independente de Certificados SHA-256
├── verificar_qualidade.py                                 # Esteira Unificada de Automação de Qualidade (Testes + Radon + CRAP + Mutação)
├── Abrir Sistema de Educacao.bat                          # Inicializador rápido por duplo clique da Plataforma de Educação
├── Abrir Calculadora.bat                                  # Inicializador rápido por duplo clique da Calculadora
├── Calculadora.pyw                                        # Script sem console para abertura direta no Windows
├── calculadora.ico                                        # Ícone ARGB de 32 bits personalizado do sistema
├── docs/                                                  # Material Didático Aprofundado (6 Módulos Carrasco)
│   ├── MODULO_01_CLEAN_CODE_E_ARQUITETURA.md              # SRP, Dispatch Tables, IEEE 754 vs Decimal
│   ├── MODULO_02_TRATAMENTO_DE_EXCECOES_BLINDADO.md       # Hierarquia de exceções, bool/int, NaN/inf
│   ├── MODULO_03_TDD_PYTEST_E_MUTACAO.md                  # Ciclo Red-Green-Refactor, Branch Coverage, Mutação e CRAP
│   ├── MODULO_04_PROCTORING_E_INTEGRIDADE_DE_EXAME.md     # Arquitetura de Hardware Mocks e Regras de Infração
│   ├── MODULO_05_CRIPTOGRAFIA_SHA256_E_CERTIFICACAO.md    # Hash SHA-256, Payload Canônico e Auditoria Antifraude
│   └── MODULO_06_BUILD_EXECUTAVEL_E_DEPLOY_WINDOWS.md     # Empacotamento PyInstaller (.exe), sys._MEIPASS e Deploy Windows
├── src/                                                   # Código-Fonte do Motor de Educação e Certificação
│   ├── __init__.py
│   ├── proctoring.py                                      # Motor de Proctoring Simulado (Webcam, Áudio e Janela Mocks)
│   ├── certificador_sha256.py                             # Motor Criptográfico SHA-256 e Assinatura Salgada
│   └── avaliador_carrasco.py                              # Avaliador Técnico Automatizado da Calculadora
├── tests/                                                 # Suíte Completa de Testes (142 Testes Automatizados)
│   ├── test_calculadora.py                                # 95 testes unitários e parametrizados da calculadora
│   ├── test_interface.py                                  # 15 testes de integração Tkinter + Mocks
│   ├── test_bdd_calculadora.py                            # 11 cenários executáveis BDD (pytest-bdd)
│   ├── test_sistema_educacao.py                           # 21 testes do Proctoring, Avaliador, GUI Educacional e SHA-256
│   ├── features/
│   │   └── calculadora.feature                            # Especificação Gherkin em Português
│   ├── qa/
│   │   └── roteiro_manual.md                              # Checklist de inspeção visual e UX
│   └── roteiro_testes.md                                  # Casos de teste funcionais CT01-CT10
├── GUIA_COMPLETO_E_GLOSSARIO_TECNICO.md                   # Dicionário de Termos Técnicos e Código Integral Comentado
├── RELATORIO_QUALIDADE.md                                 # Relatório Técnico de Engenharia de Qualidade
└── requirements.txt                                       # Dependências de Teste e Qualidade
```

---

## Trilha de Aprendizado (Os 6 Módulos em `/docs`)

1. **[Módulo 01 — Clean Code e Arquitetura Limpa](docs/MODULO_01_CLEAN_CODE_E_ARQUITETURA.md):** Como desacoplar a regra matemática da interface gráfica, eliminar cascatas de `if/elif` com *Dispatch Tables* e resolver a imprecisão binária do `float` (IEEE 754) usando `decimal.Decimal`.
2. **[Módulo 02 — Engenharia Defensiva e `try/except` Blindado](docs/MODULO_02_TRATAMENTO_DE_EXCECOES_BLINDADO.md):** Como evitar o crime do `except:` vazio e neutralizar as 3 armadilhas do Python (`isinstance(True, int) == True`, `float("nan")` e `float("inf")`).
3. **[Módulo 03 — TDD Implacável, `pytest` e Testes de Mutação](docs/MODULO_03_TDD_PYTEST_E_MUTACAO.md):** As 3 Leis do TDD de Uncle Bob, parametrização massiva, *Branch Coverage*, eliminação de mutantes via AST e cálculo da métrica **CRAP**.
4. **[Módulo 04 — Motor de Proctoring Simulado](docs/MODULO_04_PROCTORING_E_INTEGRIDADE_DE_EXAME.md):** Supervisão automatizada de exames usando *Mocks* de hardware (`SensorWebcamMock`, `SensorAudioMock`, `SensorJanelaMock`) e máquina de estados de penalidades.
5. **[Módulo 05 — Criptografia SHA-256 e Certificação](docs/MODULO_05_CRIPTOGRAFIA_SHA256_E_CERTIFICACAO.md):** Serialização JSON canônica, efeito avalanche, assinatura `SHA-256` e verificação em tempo constante (`hmac.compare_digest`).
6. **[Módulo 06 — Build de Executáveis Windows (`.exe`) e Deploy Nativo](docs/MODULO_06_BUILD_EXECUTAVEL_E_DEPLOY_WINDOWS.md):** Como compilar aplicações gráficas Python com `PyInstaller --onefile --windowed`, embutir recursos com `sys._MEIPASS` e instalar atalhos no Menu Iniciar, Desktop e Registro do Windows (`HKCU`).

---

## Como Executar no Windows (Executável Nativo ou Código-Fonte)

### Opção A — Executáveis Nativos do Windows (`.exe` — Sem precisar de terminal)
- Dê dois cliques em **`Sistema Educacao Calculadora.exe`** (ou abra **Sistema Educacao Calculadora Python** pelo **Menu Iniciar** / **Área de Trabalho**) para abrir a plataforma gráfica com os 6 módulos do curso, simulador interativo de Proctoring e emissor de certificados SHA-256.
- Dê dois cliques em **`Calculadora Python.exe`** (ou abra **Calculadora Python** pelo **Menu Iniciar** / **Área de Trabalho**) para abrir diretamente a calculadora gráfica.
- Para reinstalar os atalhos no Menu Iniciar e Desktop em qualquer computador Windows:
  ```bash
  python instalar_sistema_windows.py
  ```

### Opção B — Execução via Python e Automação de Qualidade
```bash
# Abrir a Plataforma Gráfica de Educação e Certificação
python app_educacao.py

# Abrir a Calculadora Gráfica
python main.py

# Emitir e auditar certificado criptográfico SHA-256 via CLI
python verify_certificate.py

# Executar todos os 142 testes automatizados e a esteira completa de qualidade
python verificar_qualidade.py
```
