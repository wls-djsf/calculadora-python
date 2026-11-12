# language: pt
# ============================================================
# ESPECIFICAÇÃO DE ACEITAÇÃO EM GHERKIN (BDD)
# ============================================================
# [Termos Técnicos deste Arquivo]
# - # language: pt -> Diretiva técnica obrigatória na linha 1 para instruir o interpretador
#   Gherkin a reconhecer palavras-chave em português.
# - Funcionalidade (Feature): Descreve o requisito de alto nível e o valor para o usuário.
# - Cenário (Scenario): Exemplo concreto e executável de comportamento do sistema.
# - Dado (Given): Pré-condição ou estado inicial antes da ação.
# - Quando (When): Ação realizada pelo usuário na calculadora.
# - Então (Then): Resultado observável esperado no visor.
# - E (And): Conector lógico que dá continuidade ao passo anterior (Dado, Quando ou Então).
# ============================================================
Funcionalidade: Calculadora Gráfica em Python
  Como um usuário da Calculadora Python
  Quero realizar operações matemáticas básicas e avançadas pela interface e pelo teclado
  Para obter resultados precisos com feedback claro no visor

  Cenário: Inicialização da calculadora
    Dado que a calculadora foi inicializada
    Então o visor principal deve exibir "0"
    E o visor de histórico deve exibir ""

  Cenário: Adição de dois números
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "+"
    E o usuário insere o número "5"
    E o usuário pressiona "="
    Então o visor principal deve exibir "15"

  Cenário: Subtração de dois números
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "-"
    E o usuário insere o número "5"
    E o usuário pressiona "="
    Então o visor principal deve exibir "5"

  Cenário: Multiplicação de dois números
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "*"
    E o usuário insere o número "5"
    E o usuário pressiona "="
    Então o visor principal deve exibir "50"

  Cenário: Divisão de dois números
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "/"
    E o usuário insere o número "5"
    E o usuário pressiona "="
    Então o visor principal deve exibir "2"

  Cenário: Cálculo de porcentagem contextual na adição
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "200"
    E o usuário seleciona a operação "+"
    E o usuário insere o número "10"
    E o usuário pressiona "%"
    E o usuário pressiona "="
    Então o visor principal deve exibir "220"

  Cenário: Limpeza completa do visor e estado com C
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "123"
    E o usuário seleciona a operação "+"
    E o usuário insere o número "45"
    E o usuário pressiona "C"
    Então o visor principal deve exibir "0"
    E o visor de histórico deve exibir ""

  Cenário: Retrocesso de dígitos com Backspace
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "123"
    E o usuário pressiona "⌫"
    Então o visor principal deve exibir "12"

  Cenário: Entrada de operações pelo teclado
    Dado que a calculadora foi inicializada
    Quando o usuário digita a sequência de teclas "8*7="
    Então o visor principal deve exibir "56"

  Cenário: Tratamento de divisão por zero
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "/"
    E o usuário insere o número "0"
    E o usuário pressiona "="
    Então o visor principal deve exibir "Erro: Divisão por zero"

  Cenário: Continuidade das operações após resultados
    Dado que a calculadora foi inicializada
    Quando o usuário insere o número "10"
    E o usuário seleciona a operação "+"
    E o usuário insere o número "5"
    E o usuário pressiona "="
    E o usuário seleciona a operação "*"
    E o usuário insere o número "3"
    E o usuário pressiona "="
    Então o visor principal deve exibir "45"
