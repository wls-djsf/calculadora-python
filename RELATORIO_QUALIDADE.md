# Relatório de Desenvolvimento e Engenharia de Qualidade — Calculadora Python

## 1. Análise Inicial e Plano de Execução

### 1.1. Inspeção Inicial do Diretório
Na inspeção inicial do workspace (`c:\Users\HORUS\Documents\Calculadora Python`), constatou-se a presença exclusiva do documento de especificação [PLANO CALCULADORA.docx](file:///c:/Users/HORUS/Documents/Calculadora%20Python/PLANO%20CALCULADORA.docx), sem arquivos `.py` previamente implementados.

### 1.2. Extração da Arquitetura e dos TODOs do Documento Base
A leitura integral de `PLANO CALCULADORA.docx` revelou a arquitetura modular planejada e todos os blocos `TODO` obrigatórios por arquivo:
- **`calculadora.py`** (`TODO 01` a `TODO 10`): Estruturação da classe `Calculadora`, adição, subtração, multiplicação, divisão (com proteção contra divisão por zero), porcentagem contextual, inversão de sinal, validação de dados, tratamento de precisão decimal e revisão de responsabilidades (sem dependência do Tkinter).
- **`main.py`** (`TODO 01` a `TODO 13`): Importações, configuração da janela principal Tkinter, identidade visual em paleta roxa e lavanda, estrutura em grade, visor duplo (histórico e principal), botões numéricos, botões de operação, botões de controle (`C`, `CE`, `⌫`), integração com `Calculadora`, eventos de teclado físico, máquina de estados da interface, tratamento amigável de erros e inicialização.
- **`tests/test_calculadora.py`** (`TODO 01` a `TODO 10`): Testes unitários isolados da lógica matemática.
- **`tests/test_interface.py`** (`TODO 01` a `TODO 08`): Testes de integração entre interface e lógica matemática.
- **`tests/roteiro_testes.md`** e **`tests/qa/roteiro_manual.md`**: Roteiros funcionais e procedimentos manuais de QA.
- **`README.md`**: Documentação técnica e comandos de execução.

### 1.3. Plano de Execução Aplicado
1. **Preparação do Ambiente:** Instalação de `pytest`, `pytest-bdd`, `coverage`, `radon` e `mutmut`.
2. **Ciclo TDD (Red → Green → Refactor) para `calculadora.py`:**
   - **RED:** Criação do esqueleto de `calculadora.py` com os comentários `TODO` originais e execução de `tests/test_calculadora.py` confirmando a falha esperada (`104 failed`).
   - **GREEN:** Implementação da classe `Calculadora` com aritmética `Decimal` exata e validação rigorosa de tipos.
   - **REFACTOR:** Isolamento da formatação e despacho de operadores, mantendo complexidade ciclomática mínima.
3. **Ciclo TDD (Red → Green → Refactor) para Integração e Aceitação (`main.py`, `test_interface.py`, `calculadora.feature`):**
   - **RED:** Escrita dos 11 cenários Gherkin em `tests/features/calculadora.feature`, passos em `tests/test_bdd_calculadora.py` e testes de integração em `tests/test_interface.py` antes da implementação de `main.py`, confirmando a falha inicial.
   - **GREEN:** Implementação completa de `InterfaceCalculadora` e `PALETA_CORES` em `main.py`.
   - **REFACTOR:** Uso de tabelas de despacho (`acoes_diretas` e `mapa_teclas_especiais`) para reduzir a complexidade ciclomática e alcançar 100% de cobertura de linhas e ramificações.
4. **Verificação Independente de Qualidade:** Execução de cobertura de código/ramificações (`coverage.py`), análise estática (`radon`), cálculo de pontuação **CRAP**, testes de mutação sobre `calculadora.py` e consolidação no script `verificar_qualidade.py`.

---

## 2. Arquivos Criados / Modificados e Funcionalidades Implementadas

| Arquivo | Papel Arquitetural | Funcionalidades Implementadas |
|---|---|---|
| `calculadora.py` | Lógica de Negócio | Classe `Calculadora` e exceção `ErroEntradaInvalida`; métodos `validar_numero`, `_formatar_resultado`, `somar`, `subtrair`, `multiplicar`, `dividir`, `porcentagem` (contextual), `inverter_sinal`, `calcular` e `calcular_encadeado`. Todos os `TODO 01`–`10` preservados. |
| `main.py` | Interface Gráfica e Estado | Classe `InterfaceCalculadora`, `PALETA_CORES` (tema roxo/lavanda), `FONTES` e `iniciar_aplicacao`. Visor duplo, grade responsiva de 20 botões, atalhos de teclado (`0-9`, `+`, `-`, `*`, `/`, `%`, `.`, `,`, `Enter`, `BackSpace`, `Escape`, `Delete`, `F9`, `c`), controles `C`, `CE`, `⌫`, `±` e recuperação automática de erros. Todos os `TODO 01`–`13` preservados. |
| `tests/test_calculadora.py` | Testes Unitários | 26 métodos `unittest.TestCase` + 69 execuções parametrizadas `@pytest.mark.parametrize` (total de 95 itens de teste unitário). Todos os `TODO 01`–`10` preservados. |
| `tests/test_interface.py` | Testes de Integração | 15 testes de integração verificando widgets Tkinter reais, sincronização de visor/histórico, teclado, recuperação de erros e verificação de contrato com `MagicMock`. Todos os `TODO 01`–`08` preservados. |
| `tests/features/calculadora.feature` | Especificação BDD (Gherkin) | 11 cenários de aceitação em linguagem natural (`# language: pt`) cobrindo inicialização, 4 operações, porcentagem, limpeza `C`, retrocesso `⌫`, teclado, divisão por zero e continuidade após resultados. |
| `tests/test_bdd_calculadora.py` | Conector Executável BDD | Definições de passos (`@given`, `@when`, `@then`) conectando `calculadora.feature` à `InterfaceCalculadora` e `Calculadora`. |
| `tests/roteiro_testes.md` | Roteiro Funcional QA | Casos de teste funcionais `CT01` a `CT10` e registro de resultados. |
| `tests/qa/roteiro_manual.md` | Procedimentos de QA Manual | Guia passo a passo separando testes automatizados de validações visuais/humanas (aparência, contraste, legibilidade, redimensionamento, clique e teclado). |
| `verificar_qualidade.py` | Automação da Qualidade | Executor unificado de testes unitários, BDD, integração, cobertura HTML/JSON/texto, métricas Radon, cálculo de CRAP e motor AST de Testes de Mutação. |
| `README.md` | Documentação | Documentação da arquitetura, instruções de uso e comandos padronizados de qualidade. |

---

## 3. Resultados da Execução de Testes

Todos os comandos foram executados no ambiente real (`Python 3.12.10` em Windows):

| Suíte de Testes | Ferramenta | Quantidade Executada | Aprovados | Reprovados | Tempo |
|---|---|---|---|---|---|
| Testes Unitários Clássicos | `unittest` | 26 | 26 | 0 | 0.001s |
| Testes Unitários + Parametrizados | `pytest` | 95 | 95 | 0 | 0.28s |
| Testes de Aceitação (Gherkin) | `pytest-bdd` | 11 | 11 | 0 | 0.12s |
| Testes de Integração (`main` ↔ `calculadora`) | `pytest` / `unittest` | 15 | 15 | 0 | 0.80s |
| **Total Consolidado (`pytest`)** | `pytest` | **121** | **121** | **0** | **1.07s** |

---

## 4. Cobertura de Código e Ramificações (`coverage.py`)

Medição executada com `python -m coverage run --branch --source=calculadora,main -m pytest`:

| Módulo | Declarações (`Stmts`) | Não Executadas (`Miss`) | Ramificações (`Branch`) | Ramificações Parciais (`BrPart`) | Cobertura Total (`Cover`) | Linhas Faltantes |
|---|---:|---:|---:|---:|---:|---|
| `calculadora.py` | 54 | 0 | 16 | 0 | **100%** | Nenhuma |
| `main.py` | 233 | 0 | 62 | 0 | **100%** | Nenhuma |
| **TOTAL** | **287** | **0** | **78** | **0** | **100%** | **Nenhuma** |

- **Relatório HTML gerado em:** `htmlcov/index.html`
- **Relatório JSON gerado em:** `coverage.json`
- *Nota de Engenharia:* Apenas o bloco `if __name__ == "__main__":` de `main.py` utiliza `# pragma: no cover` por ser o ponto de entrada de execução direta do script; toda a função `iniciar_aplicacao()` e todas as classes e métodos de negócio e interface foram integralmente testados sem exclusões artificiais.

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
- **Mutações Equivalentes:** **0** (o método `_formatar_resultado` foi projetado sem condições redundantes para evitar mutantes equivalentes).

| ID | Linha | Categoria | Mutação Aplicada | Resultado |
|---:|---:|---|---|---|
| #01 a #10, #14, #19 | 31..128 | Modificação de Retorno | `return expr -> return None` (todos os retornos) | **ELIMINADO (KILLED)** |
| #11 | 27 | Condição Booleana | `or -> and` em `validar_numero` | **ELIMINADO (KILLED)** |
| #12 | 29 | Condição Booleana | `not math.isfinite(valor) -> math.isfinite(valor)` | **ELIMINADO (KILLED)** |
| #13 | 39 | Operador Relacional | `== -> !=` em `_formatar_resultado` | **ELIMINADO (KILLED)** |
| #15 | 78 | Operador Relacional | `dec_b == 0 -> dec_b != 0` em `dividir` | **ELIMINADO (KILLED)** |
| #16 | 92 | Operador Relacional | `not in -> in` na validação de `porcentagem` | **ELIMINADO (KILLED)** |
| #17 | 94 | Operador Aritmético | `dec_valor / Decimal(100) -> *` em `porcentagem` | **ELIMINADO (KILLED)** |
| #18 | 95 | Condição Booleana | `base is None or operacao in ... -> and` | **ELIMINADO (KILLED)** |
| #20 | 119 | Operador Relacional | `operador not in operacoes -> in` em `calcular` | **ELIMINADO (KILLED)** |
| #21 | 50 | Operador Aritmético | `dec_a + dec_b -> dec_a - dec_b` em `somar` | **ELIMINADO (KILLED)** |
| #22 | 59 | Operador Aritmético | `dec_a - dec_b -> dec_a + dec_b` em `subtrair` | **ELIMINADO (KILLED)** |
| #23 | 68 | Operador Aritmético | `dec_a * dec_b -> dec_a / dec_b` em `multiplicar` | **ELIMINADO (KILLED)** |
| #24 | 78 | Constante Numérica | `0 -> 1` na verificação de divisão por zero | **ELIMINADO (KILLED)** |
| #25 | 80 | Operador Aritmético | `dec_a / dec_b -> dec_a * dec_b` em `dividir` | **ELIMINADO (KILLED)** |
| #26 | 95 | Operador Relacional | `base is None -> base is not None` | **ELIMINADO (KILLED)** |
| #27 | 95 | Operador Relacional | `operacao in ("*", "/") -> not in` | **ELIMINADO (KILLED)** |
| #28 | 98 | Operador Aritmético | `dec_base * fator -> dec_base / fator` | **ELIMINADO (KILLED)** |
| #29 | 105 | Operador Unário | `-dec_numero -> +dec_numero` em `inverter_sinal` | **ELIMINADO (KILLED)** |
| #30 | 94 | Constante Numérica | `Decimal(100) -> Decimal(101)` em `porcentagem` | **ELIMINADO (KILLED)** |

---

## 6. Métricas de Complexidade (`Radon`) e Pontuação CRAP

### 6.1. Resumo Estrutural e Índice de Manutenibilidade
- **Complexidade Ciclomática Média:** **2.31 (Nota A)** em 39 blocos analisados (100% dos blocos receberam Nota **A**).
- **Índice de Manutenibilidade (`radon mi`):**
  - `calculadora.py`: **69.15 — Nota A** (Alta manutenibilidade)
  - `main.py`: **43.55 — Nota A** (Alta manutenibilidade)
- **Tamanho do Código (`radon raw`):**
  - `calculadora.py`: `128 LOC` (`59 SLOC`, `67 LLOC`, `38` linhas de comentários)
  - `main.py`: `467 LOC` (`326 SLOC`, `272 LLOC`, `69` linhas de comentários)

### 6.2. Tabela Completa de Pontuação CRAP (Referência: $\text{CRAP} \le 12$)
Fórmula aplicada:
$$\text{CRAP}(m) = \text{comp}(m)^2 \times \left(1 - \frac{\text{cov}(m)}{100}\right)^3 + \text{comp}(m)$$

| Arquivo | Função / Método | Complexidade (`CC`) | Nota `CC` | Cobertura | Pontuação `CRAP` | Status ($\le 12$) |
|---|---|---:|:---:|---:|---:|---|
| `calculadora.py` | `Calculadora.validar_numero` | 4 | A | 100.0% | **4.00** | Aprovado |
| `calculadora.py` | `Calculadora._formatar_resultado` | 2 | A | 100.0% | **2.00** | Aprovado |
| `calculadora.py` | `Calculadora.somar` | 1 | A | 100.0% | **1.00** | Aprovado |
| `calculadora.py` | `Calculadora.subtrair` | 1 | A | 100.0% | **1.00** | Aprovado |
| `calculadora.py` | `Calculadora.multiplicar` | 1 | A | 100.0% | **1.00** | Aprovado |
| `calculadora.py` | `Calculadora.dividir` | 2 | A | 100.0% | **2.00** | Aprovado |
| `calculadora.py` | `Calculadora.porcentagem` | 4 | A | 100.0% | **4.00** | Aprovado |
| `calculadora.py` | `Calculadora.inverter_sinal` | 1 | A | 100.0% | **1.00** | Aprovado |
| `calculadora.py` | `Calculadora.calcular` | 2 | A | 100.0% | **2.00** | Aprovado |
| `calculadora.py` | `Calculadora.calcular_encadeado` | 2 | A | 100.0% | **2.00** | Aprovado |
| `main.py` | `iniciar_aplicacao` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.__init__` | 3 | A | 100.0% | **3.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._configurar_janela` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._construir_interface` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._construir_visor` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._construir_botoes` | 3 | A | 100.0% | **3.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._criar_botao` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._configurar_teclado` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.processar_tecla` | 5 | A | 100.0% | **5.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.pressionar_botao` | 4 | A | 100.0% | **4.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.inserir_digito` | 4 | A | 100.0% | **4.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.inserir_decimal` | 4 | A | 100.0% | **4.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.selecionar_operador` | 5 | A | 100.0% | **5.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.calcular_resultado` | 4 | A | 100.0% | **4.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.calcular_porcentagem` | 2 | A | 100.0% | **2.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.inverter_sinal` | 2 | A | 100.0% | **2.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.limpar_tudo` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.limpar_entrada` | 2 | A | 100.0% | **2.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.retroceder` | 4 | A | 100.0% | **4.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._executar_operacao_pendente` | 3 | A | 100.0% | **3.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._registrar_erro` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._converter_entrada` | 2 | A | 100.0% | **2.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._formatar_exibicao` | 3 | A | 100.0% | **3.00** | Aprovado |
| `main.py` | `InterfaceCalculadora._atualizar_interface` | 3 | A | 100.0% | **3.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.obter_visor` | 1 | A | 100.0% | **1.00** | Aprovado |
| `main.py` | `InterfaceCalculadora.obter_historico` | 1 | A | 100.0% | **1.00** | Aprovado |

---

## 7. Problemas Encontrados, Correções e Pendências Manuais

### 7.1. Problemas Encontrados e Corrigidos Durante o Desenvolvimento
1. **Imprecisão de Ponto Flutuante IEEE 754 (`0.1 + 0.2 != 0.3`):**
   - *Problema:* Operações diretas com `float` nativo geram resíduos binários (`0.30000000000000004`).
   - *Correção:* Conversão validada via `Decimal(str(valor))` em `calculadora.py`, retornando `int` quando o valor é inteiro exato e `float` de precisão preservada nos demais casos.
2. **Herança de `bool` a partir de `int` em Python (`isinstance(True, int) == True`):**
   - *Problema:* Em Python, `True` e `False` são instâncias de `int` e passariam por um filtro ingênuo `isinstance(valor, (int, float))`.
   - *Correção:* Adicionada guarda explícita `if isinstance(valor, bool) or not isinstance(valor, (int, float)): raise ErroEntradaInvalida(...)`.
3. **Semântica de `base=None` em `porcentagem(valor, base=None, operacao=None)`:**
   - *Problema:* Na primeira execução parametrizada de entradas inválidas, o teste verificava `calc.porcentagem(10, None, "+")` esperando erro, mas `base=None` é o parâmetro legítimo para cálculo de porcentagem sem base (`valor / 100`).
   - *Correção:* Refinamento do teste parametrizado para validar `calc.dividir(10, invalido)` para todos os valores inválidos (incluindo `None`) e `calc.porcentagem(10, invalido, "+")` para todos os valores inválidos não-`None`.
4. **Incompatibilidade do CLI `mutmut 3.8.1` com Windows Nativo (`os.fork`):**
   - *Problema:* O executável `mutmut` exige WSL no Windows.
   - *Correção:* Implementação do motor de mutação AST integrado em `verificar_qualidade.py`, garantindo a execução automatizada e auditável de 30 mutantes reais no Windows.

### 7.2. Pendências e Testes Manuais Necessários (Validação Humana)
Conforme o Princípio Fundamental do projeto, a aprovação final dos critérios de aceitação e da experiência visual cabe ao **responsável pelo projeto**:
1. Executar `python main.py` e preencher o checklist `QM-01` a `QM-08` em [tests/qa/roteiro_manual.md](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/qa/roteiro_manual.md) para validar subjetivamente:
   - Harmonia visual da paleta roxa/lavanda no monitor utilizado;
   - Legibilidade e alinhamento tipográfico (`Segoe UI`);
   - Fluidez de redimensionamento da janela com o mouse;
   - Sensação tátil de clique e resposta ao teclado físico.
2. Revisar e aprovar formalmente os 11 cenários Gherkin em [tests/features/calculadora.feature](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/features/calculadora.feature).
