# Calculadora Python

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Interface](https://img.shields.io/badge/Interface-Tkinter%20%28Tema%20Roxo%29-8B5CF6)
![Testes](https://img.shields.io/badge/Testes-121%20Aprovados-2EA043)
![Cobertura](https://img.shields.io/badge/Cobertura%20%28Linhas%20e%20Branches%29-100%25-2EA043)
![Mutação](https://img.shields.io/badge/Mutantes%20Eliminados-30%2F30%20%28100%25%29-2EA043)
![Complexidade](https://img.shields.io/badge/Radon%20CC%20%26%20MI-Nota%20A%20%28CRAP%20%E2%89%A4%205%29-2EA043)

## Descrição
Calculadora gráfica desenvolvida em Python com arquitetura modular, separação rigorosa de responsabilidades (Lógica de Negócio vs. Interface Gráfica) e uma esteira completa de **Engenharia de Qualidade** inspirada nas práticas de Robert C. Martin (*Uncle Bob*): **TDD (Red → Green → Refactor)**, **BDD com Gherkin**, **Cobertura de Linhas e Ramificações**, **Testes de Mutação via AST** e **Métricas Estáticas (Radon / CRAP)**.

## Objetivo
Desenvolver uma calculadora básica com interface inspirada na calculadora do Windows e tema visual roxo/lavanda, acompanhada de mecanismos independentes e automatizados de verificação de qualidade.

## Tecnologias
- **Python 3** (`decimal.Decimal` para precisão exata sem erros de ponto flutuante IEEE 754)
- **Tkinter / ttk** (Interface gráfica responsiva em grade)
- **unittest** & **pytest** (Testes unitários, integração, parametrização e *mocks*)
- **pytest-bdd** (Testes de aceitação executáveis em Gherkin em português)
- **coverage.py** (Cobertura de declarações e ramificações)
- **Radon** (Complexidade Ciclomática, Índice de Manutenibilidade, métricas de tamanho e pontuação **CRAP**)
- **AST Mutation Engine / mutmut** (Testes de mutação automatizados)

## Funcionalidades
- Adição (`+`), Subtração (`-`), Multiplicação (`*` / `×`) e Divisão (`/` / `÷`)
- Tratamento seguro de divisão por zero (`Erro: Divisão por zero`) com recuperação automática
- Porcentagem contextual (`%`) no padrão da calculadora do Windows
- Inversão de sinal (`±`)
- Limpeza completa (`C`), limpeza da entrada atual (`CE`) e retrocesso de dígito (`⌫`)
- Operações encadeadas e continuidade imediata após resultados
- Controle completo pelo mouse e pelo teclado físico/numérico (`0–9`, `+`, `-`, `*`, `/`, `%`, `.`, `,`, `Enter`, `Backspace`, `Esc`, `Delete`, `F9`)

## Estrutura
```text
Calculadora Python/
├── main.py                                 # Inicialização e interface gráfica (Tkinter)
├── calculadora.py                          # Regras de negócio e operações matemáticas
├── verificar_qualidade.py                  # Script único de validação de qualidade, mutação e CRAP
├── Calculadora.pyw                         # Atalho sem console para abertura direta no Windows
├── Abrir Calculadora.bat                   # Inicializador rápido por duplo clique no Windows
├── calculadora.ico                         # Ícone personalizado do aplicativo
├── requirements.txt                        # Dependências de testes e métricas de qualidade
├── .gitignore                              # Regras de exclusão de arquivos temporários para o Git
├── README.md                               # Documentação principal do projeto
├── RELATORIO_QUALIDADE.md                  # Relatório técnico completo de testes e métricas
├── GUIA_COMPLETO_E_GLOSSARIO_TECNICO.md    # Glossário de termos técnicos e código comentado
└── tests/
    ├── test_calculadora.py                 # Testes unitários e parametrizados da lógica matemática
    ├── test_interface.py                   # Testes de integração (main.py <-> calculadora.py e mocks)
    ├── test_bdd_calculadora.py             # Passos executáveis dos cenários Gherkin (pytest-bdd)
    ├── roteiro_testes.md                   # Roteiro de testes funcionais e critérios de aprovação
    ├── features/
    │   └── calculadora.feature             # Especificação de aceitação em Gherkin (# language: pt)
    └── qa/
        └── roteiro_manual.md               # Procedimentos e checklist de QA manual (UI/UX)
```

## Execução

### 1. Executar a Calculadora (Apenas Python padrão, sem dependências externas)
```bash
python main.py
```
*(No Windows, você também pode dar dois cliques em `Abrir Calculadora.bat` ou `Calculadora.pyw`).*

### 2. Instalar Dependências de Teste e Qualidade
```bash
pip install -r requirements.txt
```

## Testes e Automação da Qualidade

Para executar toda a esteira de qualidade em sequência (Testes Unitários + BDD + Integração + Cobertura + Radon + CRAP + Testes de Mutação):
```bash
python verificar_qualidade.py
```

Ou execute cada etapa individualmente:
- **Testes unitários (`unittest` e `pytest`):**
  ```bash
  python -m unittest tests/test_calculadora.py -v
  python -m pytest tests/test_calculadora.py -v
  ```
- **Testes de aceitação (BDD / Gherkin):**
  ```bash
  python -m pytest tests/test_bdd_calculadora.py -v
  ```
- **Testes de integração:**
  ```bash
  python -m pytest tests/test_interface.py -v
  ```
- **Cobertura de código e ramificações (`coverage.py`):**
  ```bash
  python -m coverage run --branch --source=calculadora,main -m pytest
  python -m coverage report -m
  python -m coverage html
  ```
- **Análise de complexidade e manutenibilidade (`radon`):**
  ```bash
  python -m radon cc calculadora.py main.py -s -a
  python -m radon mi calculadora.py main.py -s
  ```

## Resumo das Métricas Alcançadas

| Métrica de Qualidade | Resultado Obtido | Referência / Meta |
|---|---|---|
| **Testes Automatizados (`pytest`)** | **121 / 121 aprovados (100%)** | 0 falhas |
| **Cenários BDD Gherkin** | **11 / 11 aprovados (100%)** | 11 cenários conectados |
| **Cobertura de Linhas e Ramificações** | **100% (`calculadora.py` e `main.py`)** | $\ge 90\%$ (100% na lógica) |
| **Testes de Mutação (`calculadora.py`)** | **30 / 30 mutantes eliminados (100%)** | 0 sobreviventes |
| **Complexidade Ciclomática (`Radon CC`)** | **Nota A em 100% dos blocos (média 2.31)** | Nota A ou B |
| **Índice de Manutenibilidade (`Radon MI`)** | **Nota A (`69.15` e `43.55`)** | Nota A ($> 20$) |
| **Pontuação `CRAP` Máxima** | **4.00 (`calculadora.py`) / 5.00 (`main.py`)** | $\text{CRAP} \le 12.0$ |

## Interface
Tema visual roxo e lavanda (`#1E152A` / `#2A1E3F` / `#8B5CF6`) com alto contraste (padrão WCAG AA), botões responsivos em grade e visor duplo (histórico da expressão superior + valor principal).
