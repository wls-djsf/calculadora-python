# Roteiro de QA e Validação Manual — Calculadora Python

## 1. Objetivo
Este documento descreve os procedimentos de Garantia de Qualidade (QA) para validação em uso real da **Calculadora Python**, estabelecendo uma distinção clara entre o que é verificado por **testes automatizados** e o que exige **inspeção visual e interação humana** na interface gráfica (Tkinter).

---

## 2. Separação de Responsabilidades: Testes Automatizados vs. Testes Manuais

| Categoria | Escopo | Ferramenta / Responsável |
|---|---|---|
| **Testes Unitários (Automatizados)** | Precisão matemática, operações básicas (`+`, `-`, `*`, `/`), porcentagem contextual, inversão de sinal, validação de tipos, divisão por zero e operações encadeadas. | `pytest` / `unittest` (`tests/test_calculadora.py`) |
| **Testes de Integração (Automatizados)** | Comunicação entre `main.py` e `calculadora.py`, sincronização de estado da interface, envio de operandos/operadores, atualização de visor e recuperação de erro. | `pytest` / `unittest` (`tests/test_interface.py`) |
| **Testes de Aceitação BDD (Automatizados)** | Cenários observáveis em Gherkin (inicialização, operações, limpeza `C`, retrocesso `⌫`, teclado, divisão por zero, continuidade pós-resultado). | `pytest-bdd` (`tests/features/calculadora.feature` e `tests/test_bdd_calculadora.py`) |
| **Testes de QA Manual (Interação Humana)** | Percepção visual da paleta roxa/lavanda, contraste real em tela, ergonomia de clique, fluidez de redimensionamento, alinhamento tipográfico e experiência de uso (UX). | Analista de QA / Responsável pelo Projeto (este roteiro) |

---

## 3. Pré-condições para Execução Manual
1. Ambiente Python 3.10+ com biblioteca gráfica `tkinter` habilitada.
2. No terminal, na raiz do projeto, executar:
   ```bash
   python main.py
   ```
3. Confirmar que a janela da calculadora abre centralizada na tela, sem erros no console.

---

## 4. Procedimentos de Verificação Manual (Interação Humana)

### 4.1. Aparência Visual e Identidade (Tema Roxo e Lavanda)
- **Passos:**
  1. Observar a janela principal recém-aberta.
  2. Inspecionar as cores de fundo da janela, do visor superior (histórico), do visor principal e das quatro categorias de botões (numéricos, operadores, controle e botão de igual `=`).
- **Critério de Aceitação:**
  - A paleta segue tons harmônicos de roxo escuro (`#1E152A` / `#2A1E3F`), lavanda suave para textos e botões numéricos (`#3B2C54` / `#F3EFFE`), roxo médio para controles/operadores (`#523A78`) e destaque vibrante para o botão `=` (`#8B5CF6`).
  - Não há bordas serrilhadas ou desalinhadas.

### 4.2. Legibilidade e Tipografia
- **Passos:**
  1. Digitar um número longo (ex.: `123456789.01`).
  2. Observar o visor principal e o visor de histórico superior durante uma operação (ex.: `12345 +`).
- **Critério de Aceitação:**
  - Os números no visor principal são exibidos em fonte grande, em negrito, alinhados à direita e sem cortes verticais.
  - O histórico superior apresenta a expressão pendente em fonte menor, claramente diferenciada do valor principal.

### 4.3. Contraste de Cores (Acessibilidade Visual)
- **Passos:**
  1. Verificar a leitura dos rótulos de todos os 20 botões da grade sob iluminação normal.
  2. Verificar o contraste entre o texto claro (`#F3EFFE` / `#FFFFFF`) e os fundos roxos dos botões e do visor.
- **Critério de Aceitação:**
  - Todos os símbolos (`%`, `CE`, `C`, `⌫`, `÷`, `×`, `-`, `+`, `±`, `.`, `=`) e dígitos (`0`–`9`) são imediatamente distinguíveis, sem fadiga visual (relação de contraste compatível com WCAG AA >= 4.5:1).

### 4.4. Posicionamento dos Botões e Layout em Grade
- **Passos:**
  1. Verificar a disposição física das 5 linhas por 4 colunas de botões:
     - Linha 1: `%`, `CE`, `C`, `⌫`
     - Linha 2: `7`, `8`, `9`, `÷`
     - Linha 3: `4`, `5`, `6`, `×`
     - Linha 4: `1`, `2`, `3`, `-`
     - Linha 5: `±`, `0`, `.`, `+`
     - Linha 6 (ou coluna/barra de ação): `=` ocupando destaque claro e acessível.
- **Critério de Aceitação:**
  - Espaçamento uniforme (`padx`/`pady`) entre todos os botões.
  - Layout intuitivo inspirado na calculadora padrão do Windows.

### 4.5. Facilidade de Utilização e Resposta aos Cliques
- **Passos:**
  1. Clicar sequencialmente nos botões para calcular `25 + 75 =`.
  2. Observar o efeito visual de *hover* / clique ativo nos botões.
  3. Testar cliques rápidos consecutivos em dígitos (`1`, `2`, `3`, `4`).
- **Critério de Aceitação:**
  - Resposta imediata (< 50 ms) a cada clique, sem perda de dígitos e com feedback visual de botão pressionado.

### 4.6. Comportamento do Teclado Físico
- **Passos:**
  1. Com a janela em foco, digitar números pelo teclado principal e pelo teclado numérico (*Numpad*).
  2. Utilizar as teclas `+`, `-`, `*`, `/` para operações.
  3. Pressionar `Enter` (ou `=`) para calcular o resultado.
  4. Pressionar `Backspace` para apagar o último dígito.
  5. Pressionar `Escape` para limpar tudo (`C`) e `Delete` para limpar a entrada atual (`CE`).
  6. Testar vírgula (`,`) e ponto (`.`) como separador decimal.
- **Critério de Aceitação:**
  - O aplicativo responde identicamente ao uso por clique e por teclado, sem necessidade de clicar em nenhum campo de texto antes de digitar.

### 4.7. Redimensionamento da Janela
- **Passos:**
  1. Arrastar as bordas da janela para aumentá-la até o dobro do tamanho inicial e maximizá-la.
  2. Reduzir a janela até o limite mínimo permitido.
- **Critério de Aceitação:**
  - Todos os botões e o visor expandem e contraem proporcionalmente (`grid_rowconfigure` / `grid_columnconfigure` com `weight`), mantendo o alinhamento.
  - A janela respeita o tamanho mínimo configurado (`minsize`), impedindo que os botões fiquem ocultos ou sobrepostos.

### 4.8. Mensagens de Erro e Recuperação
- **Passos:**
  1. Executar `10 ÷ 0 =`.
  2. Observar a mensagem apresentada no visor principal.
  3. Sem fechar o aplicativo, digitar `8 + 2 =` ou pressionar `C`.
- **Critério de Aceitação:**
  - O visor exibe a mensagem amigável `Erro: Divisão por zero` (sem travar ou exibir *traceback* técnico).
  - Ao digitar um novo número ou pressionar `C`/`CE`, a calculadora se recupera limpa e imediatamente para novas operações.

---

## 5. Checklist de Aprovação Manual (Para Preenchimento pelo Responsável)

| Item | Verificação | Resultado (`[ ] Aprovado` / `[ ] Reprovado`) | Observações |
|---|---|---|---|
| QM-01 | Aparência visual e paleta roxa/lavanda | `[ ] Aprovado  [ ] Reprovado` | |
| QM-02 | Legibilidade do visor principal e histórico | `[ ] Aprovado  [ ] Reprovado` | |
| QM-03 | Contraste de cores dos botões e textos | `[ ] Aprovado  [ ] Reprovado` | |
| QM-04 | Posicionamento e alinhamento em grade | `[ ] Aprovado  [ ] Reprovado` | |
| QM-05 | Fluidez e resposta aos cliques do mouse | `[ ] Aprovado  [ ] Reprovado` | |
| QM-06 | Atalhos e digitação pelo teclado físico | `[ ] Aprovado  [ ] Reprovado` | |
| QM-07 | Comportamento no redimensionamento | `[ ] Aprovado  [ ] Reprovado` | |
| QM-08 | Clareza da mensagem de erro e recuperação | `[ ] Aprovado  [ ] Reprovado` | |
