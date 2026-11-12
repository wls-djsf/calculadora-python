# Guia Completo do Projeto e Glossário de Termos Técnicos — Calculadora Python

Este documento reúne, em **Português do Brasil**, a explicação detalhada de **todos os termos técnicos** (palavras reservadas do Python, bibliotecas gráficas, frameworks de teste, métricas de engenharia de software e ferramentas de qualidade) presentes nos arquivos do projeto, além da listagem integral comentada de cada módulo.

---

## Parte 1 — Glossário Completo de Termos Técnicos

### 1.1. Sintaxe e Palavras-Chave da Linguagem Python

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `import` / `from ... import ...` | Comandos para carregar bibliotecas externas ou módulos do próprio projeto (ex.: `from calculadora import Calculadora`). |
| `class` | Define uma **classe** (estrutura que agrupa dados/atributos e comportamentos/métodos na Programação Orientada a Objetos). |
| `def` | Define uma **função** ou **método** executável. |
| `self` | Referência à própria instância do objeto dentro de uma classe (permite acessar `self.calculadora`, `self.entrada_atual`, etc.). |
| `__init__` | Método **construtor** especial do Python; é executado automaticamente sempre que um novo objeto da classe é criado. |
| `return` | Encerra a execução de uma função e devolve o resultado calculado para quem a chamou. |
| `raise` | Dispara (lança) intencionalmente uma **exceção** quando uma regra de validação é violada (ex.: divisão por zero ou tipo inválido). |
| `try` / `except` / `finally` | Estrutura de tratamento de exceções: tenta executar o bloco `try`; se ocorrer erro previsto, captura-o no `except` sem travar o programa; o bloco `finally` é executado sempre ao final (mesmo se houver erro). |
| `with` | Gerenciador de contexto que garante abertura e fechamento seguro de recursos (arquivos, chaves de registro do Windows ou verificadores de exceção em testes). |
| `if` / `elif` / `else` | Estruturas condicionais ("se", "senão se", "senão") que desviam o fluxo do programa conforme uma condição verdadeira ou falsa. |
| `for ... in ...` | Laço de repetição que percorre sequencialmente os elementos de uma lista, tupla, texto ou dicionário. |
| `and` / `or` / `not` | Operadores lógicos booleanos: `and` ("E": ambos verdadeiros), `or` ("OU": pelo menos um verdadeiro) e `not` ("NÃO": inverte o valor lógico). |
| `is` / `is not` | Verificam identidade de objeto na memória (usados principalmente para verificar se uma variável é nula: `base is None`). |
| `in` / `not in` | Verificam pertinência (se um elemento pertence ou não a uma coleção, tupla ou texto). |
| `None` | Valor especial do Python que representa a ausência de valor (nulo/vazio). |
| `True` / `False` | Valores lógicos booleanos para **Verdadeiro** e **Falso**. |
| `lambda` | Cria uma pequena função anônima de uma linha (usada nos botões do Tkinter: `command=lambda r=rotulo: self.pressionar_botao(r)`). |
| `@classmethod` | Decorador que indica que o método pertence à classe inteira (`cls`) e não a uma única instância individual. |
| `if __name__ == "__main__":` | Verifica se o arquivo está sendo executado diretamente pelo usuário (e não apenas importado por outro módulo de teste). |

---

### 1.2. Tipos Numéricos, Precisão Matemática e Exceções

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `int` | Tipo numérico para números **inteiros** (ex.: `-10`, `0`, `42`). |
| `float` | Tipo numérico de **ponto flutuante** binário de dupla precisão (padrão IEEE 754) para números com casas decimais (ex.: `2.5`, `-0.75`). |
| `bool` | Tipo lógico booleano (`True` ou `False`). *Detalhe técnico importante:* em Python, `bool` herda de `int` (`True == 1` e `False == 0`), motivo pelo qual `validar_numero` rejeita `isinstance(valor, bool)` explicitamente. |
| `str` | Tipo textual (*string* / cadeia de caracteres, ex.: `"Erro: Divisão por zero"`). |
| `Decimal` (`decimal.Decimal`) | Tipo numérico de precisão exata em base 10. Evita o erro clássico do ponto flutuante binário (`IEEE 754`) onde `0.1 + 0.2` resultaria em `0.30000000000000004`. |
| `IEEE 754` | Norma técnica internacional para aritmética de ponto flutuante binário utilizada pelos processadores modernos. |
| `NaN` (*Not a Number*) | Valor especial do padrão IEEE 754 que representa um resultado indefinido ("Não é um Número"). Criado em Python com `float("nan")`. |
| `inf` / `-inf` (*Infinity*) | Representação técnica para infinito positivo (`float("inf")`) ou negativo (`float("-inf")`). |
| `math.isfinite(valor)` | Função da biblioteca `math` que retorna `True` somente se o número for real e finito (rejeitando `NaN`, `inf` e `-inf`). |
| `to_integral_value()` | Método de `Decimal` que retorna o valor sem casas decimais, permitindo verificar se o resultado decimal é matematicamente inteiro (ex.: `Decimal("5.0") == Decimal("5")`). |
| `is_integer()` | Método do tipo `float` que informa se o número decimal possui parte fracionária zero (ex.: `4.0.is_integer()` é `True`). |
| `ValueError` | Exceção nativa do Python lançada quando uma função recebe um argumento com tipo permitido, mas valor inadequado (ex.: operador `"^"`). |
| `TypeError` | Exceção nativa lançada quando uma operação recebe um tipo de dado incompatível (ex.: tentar somar texto `"abc"` com `5`). |
| `ZeroDivisionError` | Exceção nativa lançada quando ocorre tentativa de divisão por zero (`10 / 0`). |
| `ArithmeticError` | Classe base das exceções matemáticas do Python (da qual `ZeroDivisionError` herda). |

---

### 1.3. Interface Gráfica (`Tkinter` e `ttk`)

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `tkinter` (`tk`) | Biblioteca padrão do Python para construção de interfaces gráficas nativas (baseada na ferramenta gráfica *Tcl/Tk*). |
| `ttk` (*Themed Tk*) | Submódulo do Tkinter que disponibiliza suporte a temas e estilos visuais. |
| `root` (`tk.Tk`) | Convenção técnica do Tkinter para denominar a **janela raiz** (janela principal que contém todos os demais elementos). |
| `Widget` | Termo técnico universal para qualquer componente visual de interface gráfica (botão, rótulo, painel, caixa de texto). |
| `Frame` (`tk.Frame`) | Painel retangular invisível usado para agrupar e estruturar outros componentes (`container_principal`, `area_exibicao`, `painel_botoes`). |
| `Label` (`tk.Label`) | Rótulo visual usado para exibir textos estáticos ou dinâmicos (utilizado para o visor principal e o histórico). |
| `Button` (`tk.Button`) | Componente de botão clicável que executa uma função ao receber um clique do mouse. |
| `StringVar` (`tk.StringVar`) | Variável especial sincronizada com o Tkinter; qualquer chamada a `.set(novo_texto)` atualiza imediatamente o `Label` na tela. |
| `textvariable` | Parâmetro do `Label` que o conecta a uma `StringVar`. |
| `grid` | Gerenciador de posicionamento em grade (tabela de linhas `row` e colunas `column`). |
| `columnspan` | Define quantas colunas um componente ocupa horizontalmente na grade (o botão `=` usa `columnspan=4` para ocupar toda a largura). |
| `grid_rowconfigure` / `grid_columnconfigure` | Configuram o comportamento de expansão de cada linha e coluna da grade. |
| `weight` | Peso proporcional de redimensionamento na grade; linhas/colunas com `weight > 0` crescem e encolhem junto com a janela. |
| `sticky="nsew"` | Faz o componente "grudar" nas 4 bordas da célula da grade: **N**orth (Norte/Topo), **S**outh (Sul/Base), **E**ast (Leste/Direita) e **W**est (Oeste/Esquerda). |
| `padx` / `pady` | *Padding* (espaçamento/margem) no eixo horizontal (`x`) e vertical (`y`), medido em pixels. |
| `pack(fill="x")` | Gerenciador simples de empilhamento que faz o título ocupar toda a extensão horizontal (`x`). |
| `anchor` (`"w"`, `"e"`) | Ponto cardeal de ancoragem do texto dentro do rótulo: `"w"` (*West* = esquerda) para o título e `"e"` (*East* = direita) para os números do visor. |
| `justify="right"` | Alinha múltiplas linhas de texto à direita. |
| `bg` / `fg` | Abreviações técnicas do Tkinter para *Background* (cor de fundo) e *Foreground* (cor do texto). |
| `activebackground` / `activeforeground` | Cores de fundo e de texto aplicadas no instante em que o botão está sendo clicado/acionado (*hover* ativo). |
| `hover` | Estado visual de interação quando o usuário aponta ou aciona um elemento interativo com o mouse. |
| `relief="flat"` / `bd=0` | Define o relevo do botão como plano (`flat`) e a largura da borda (*borderwidth*) como `0`, criando o visual moderno. |
| `cursor="hand2"` | Altera o ponteiro do mouse para a "mãozinha" de clique quando posicionado sobre um botão. |
| `bind("<Key>", funcao)` | Registra um *listener* (ouvinte de eventos) na janela para capturar qualquer tecla física pressionada no teclado. |
| `keysym` / `char` | Atributos do objeto de evento do Tkinter: `char` traz o caractere digitado (ex.: `"5"`, `"+"`) e `keysym` traz o nome técnico da tecla (ex.: `"Return"`, `"BackSpace"`, `"Escape"`, `"Delete"`, `"F9"`, `"KP_Enter"`). |
| `minsize` / `geometry` / `resizable` | Métodos da janela principal que definem o tamanho mínimo permitido, as dimensões/posição iniciais (`Largura x Altura + X + Y`) e a permissão de redimensionar. |
| `winfo_screenwidth` / `winfo_screenheight` | Consultam no sistema operacional a largura e altura total do monitor em pixels (usados para centralizar a janela). |
| `withdraw()` / `destroy()` | `withdraw()` oculta a janela da tela sem desativar seus componentes internos (ideal para testes automatizados rápidos); `destroy()` encerra e libera a janela da memória. |
| `mainloop()` | Inicia o ciclo contínuo de eventos gráficos do Tkinter que aguarda cliques e teclas até o usuário fechar a janela. |
| `TclError` | Exceção técnica lançada pelo Tkinter caso o sistema operacional não possua ambiente gráfico disponível. |

---

### 1.4. Engenharia de Testes (`TDD`, `unittest`, `pytest`, `Mocks`, `BDD` e `Gherkin`)

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `TDD` (*Test-Driven Development*) | **Desenvolvimento Orientado a Testes**: prática em que o teste automatizado é escrito *antes* do código de produção, seguindo o ciclo **Red → Green → Refactor**. |
| Ciclo `Red - Green - Refactor` | **Red (Vermelho):** criar o teste e vê-lo falhar; **Green (Verde):** escrever o código para o teste passar; **Refactor (Refatorar):** limpar e organizar o código mantendo todos os testes passando. |
| `unittest` | Framework de testes unitários embutido na biblioteca padrão do Python. |
| `unittest.TestCase` | Classe base do `unittest` que fornece dezenas de métodos de verificação (`assertEqual`, `assertRaises`, etc.). |
| `setUp` / `setUpClass` / `tearDownClass` | Métodos de ciclo de vida dos testes: `setUp` roda antes de *cada* teste individual; `setUpClass` roda uma vez antes de *toda* a classe; `tearDownClass` limpa os recursos ao final. |
| `pytest` | Executor e framework moderno de testes em Python, compatível com `unittest` e com suporte a parametrização e plugins como `pytest-bdd`. |
| `assert` | Palavra-chave do Python usada pelo `pytest` para validar se uma expressão é verdadeira (ex.: `assert calc.somar(2, 3) == 5`). |
| `@pytest.mark.parametrize` | Executa o mesmo teste repetidamente para uma lista de tuplas `(entrada_a, entrada_b, resultado_esperado)`, evitando repetição de código. |
| `Mock` / `MagicMock` (`unittest.mock`) | Objeto simulado que imita o comportamento de uma classe real (`Calculadora`) registrando exatamente como foi chamado, quais argumentos recebeu e quantas vezes foi acionado. |
| `spec=Calculadora` | Trava o `MagicMock` para que ele possua apenas os métodos que realmente existem na classe `Calculadora`. |
| `return_value` / `side_effect` | Configuram o valor que o `Mock` deve devolver (`return_value`) ou a exceção que ele deve simular (`side_effect=ValueError(...)`). |
| `patch` / `patch.object` | Substituem temporariamente um objeto ou método real por um `Mock` apenas durante a execução de um bloco `with`, restaurando o original automaticamente depois. |
| `SimpleNamespace` | Objeto dinâmico leve usado nos testes para simular o objeto de evento de teclado (`SimpleNamespace(char="8", keysym="8")`). |
| `BDD` (*Behavior-Driven Development*) | **Desenvolvimento Orientado ao Comportamento**: extensão do TDD que especifica requisitos como comportamentos observáveis escritos em linguagem natural. |
| `Gherkin` | Gramática estruturada para escrita de especificações BDD em arquivos `.feature` (`Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`, `E`). |
| `pytest-bdd` | Biblioteca que lê o arquivo `.feature` em Gherkin e executa cada passo chamando as funções Python decoradas com `@given`, `@when` e `@then`. |
| `@pytest.fixture` | Função preparatória do `pytest` que cria e entrega objetos prontos (como `contexto_app`) para as funções de teste. |
| `QA` (*Quality Assurance*) | **Garantia da Qualidade**: conjunto de processos sistemáticos (automatizados e manuais) para assegurar a conformidade do software com seus requisitos. |
| `UI` / `UX` | *User Interface* (Interface do Usuário — parte visual) e *User Experience* (Experiência do Usuário — facilidade, ergonomia e satisfação de uso). |
| `WCAG AA` | *Web Content Accessibility Guidelines* (nível AA): padrão internacional de acessibilidade visual que recomenda contraste mínimo de `4.5:1` entre texto e cor de fundo. |

---

### 1.5. Cobertura, Testes de Mutação e Métricas (`coverage`, `AST`, `mutmut`, `Radon`, `CRAP`)

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `coverage.py` | Ferramenta oficial do ecossistema Python para medir a porcentagem do código-fonte executada durante os testes. |
| `Statement Coverage` (`Stmts` / `Miss`) | **Cobertura de Linhas/Declarações**: mede quantas instruções executáveis do arquivo foram rodadas (`Stmts`) e quantas ficaram sem executar (`Miss`). |
| `Branch Coverage` (`Branch` / `BrPart`) | **Cobertura de Ramificações**: mede se todos os desvios lógicos (`if` verdadeiro **e** `if` falso) foram testados. `BrPart = 0` significa que nenhuma condição foi testada apenas pela metade. |
| `# pragma: no cover` | Comentário técnico reconhecido pelo `coverage.py` para marcar blocos de inicialização direta (`if __name__ == "__main__":`) que não devem ser contabilizados como linhas faltantes. |
| `Teste de Mutação` (*Mutation Testing*) | Técnica avançada que avalia a **qualidade dos próprios testes**, modificando pequenas partes do código de produção (criando *mutantes*) e verificando se a suíte de testes falha. |
| `KILLED` (*Mutante Eliminado*) | Quando um defeito artificial é inserido no código e **pelo menos um teste falha**, provando que a suíte de testes conseguiu detectar o defeito. **Este é o resultado desejado.** |
| `SURVIVED` (*Mutante Sobrevivente*) | Quando um defeito artificial é inserido no código e **todos os testes continuam passando**, revelando uma lacuna nos testes. No nosso projeto, houve **0 sobreviventes**. |
| `Mutante Equivalente` | Quando a alteração sintática não muda o comportamento matemático do programa (sendo impossível de matar). O código de `calculadora.py` foi desenhado sem ramos redundantes para ter **0 mutantes equivalentes**. |
| `mutmut` | Ferramenta de mutação para Python. Em sua versão 3.x, exige a chamada `os.fork()` do Linux/WSL, motivo pelo qual também implementamos o motor de mutação nativo em AST no script `verificar_qualidade.py`. |
| `AST` (*Abstract Syntax Tree*) | **Árvore Sintática Abstrata**: representação em árvore da estrutura gramatical do código Python (`ast.BinOp`, `ast.Compare`, `ast.BoolOp`, `ast.Return`, `ast.Constant`). |
| `Radon` | Biblioteca de análise estática de código Python que calcula Complexidade Ciclomática (`cc`), Índice de Manutenibilidade (`mi`) e métricas de tamanho (`raw`). |
| `Complexidade Ciclomática` (`CC`) | Métrica criada por Thomas McCabe que conta o número de caminhos linearmente independentes em um método. Classificada de **A** (`1` a `5`, código simples e limpo) até **F** (`> 40`, código complexo e arriscado). Todos os nossos 39 blocos têm nota **A**. |
| `Índice de Manutenibilidade` (`MI`) | Métrica composta (baseada no volume de Halstead, Complexidade Ciclomática e linhas de código) que varia de `0` a `100`. Acima de `20` recebe nota **A** (alta facilidade de manutenção). |
| `LOC` / `LLOC` / `SLOC` | **LOC** (*Lines of Code*): total bruto de linhas do arquivo; **LLOC** (*Logical Lines of Code*): quantidade de instruções lógicas; **SLOC** (*Source Lines of Code*): linhas de código excluindo linhas em branco e comentários. |
| `CRAP` (*Change Risk Anti-Patterns*) | Índice de risco de alteração de uma função, calculado por $\text{CRAP}(m) = \text{CC}^2 \times (1 - \text{cobertura}/100)^3 + \text{CC}$. Quando a cobertura é de $100\%$, o índice CRAP iguala-se à própria Complexidade Ciclomática ($\le 5$ em todo o projeto, muito abaixo do limite de segurança $\le 12$). |

---

### 1.6. Empacotamento e Integração com o Sistema Operacional Windows

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `PyInstaller` | Ferramenta que empacota o interpretador Python, bibliotecas (`tkinter`) e módulos do projeto em um único arquivo executável nativo `.exe`. |
| `.exe` | Executável binário nativo do Windows (`Calculadora Python.exe`), que abre diretamente sem exigir comandos no terminal. |
| `.pyw` / `pythonw.exe` | Extensão e executável do Python para Windows dedicados a interfaces gráficas (executam o programa sem abrir a janela preta do console `cmd.exe`). |
| `.bat` (*Batch File*) | Arquivo de lote do Windows ([Abrir Calculadora.bat](file:///c:/Users/HORUS/Documents/Calculadora%20Python/Abrir%20Calculadora.bat)) que automatiza o comando de abertura com dois cliques. |
| `.ico` | Formato de arquivo de ícone nativo do Windows ([calculadora.ico](file:///c:/Users/HORUS/Documents/Calculadora%20Python/calculadora.ico)), contendo a imagem em 32 bits ARGB da calculadora roxa. |
| `.lnk` | Arquivo binário de atalho do Windows (criado no Menu Iniciar e na Área de Trabalho via componente COM `WScript.Shell`). |
| `HKCU` (`HKEY_CURRENT_USER`) | Ramo do Registro do Windows (`winreg`) referente ao usuário atual, onde a calculadora foi registrada como aplicativo instalado. |

---

## Parte 2 — Visão Consolidada dos Módulos do Projeto

Todos os arquivos de código do projeto foram revisados para conter cabeçalhos e comentários explicativos em português detalhando cada termo técnico sem interferir na execução:

1. **[calculadora.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/calculadora.py)** — Regras de negócio, validação de tipos e aritmética `Decimal` com explicações de `Decimal`, `isinstance`, `bool`, `int`, `float`, `math.isfinite`, `to_integral_value`, `ZeroDivisionError` e `None`.
2. **[main.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/main.py)** — Interface gráfica Tkinter em tema roxo e lavanda com explicações de `root`, `Frame`, `Label`, `Button`, `StringVar`, `grid`, `sticky="nsew"`, `columnspan`, `relief="flat"`, `hover`, `bind("<Key>")`, `keysym`, `mainloop` e `# pragma: no cover`.
3. **[tests/test_calculadora.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/test_calculadora.py)** — Suíte de 95 testes unitários (`unittest` + `pytest`) com explicações de `TestCase`, `setUp`, `assertEqual`, `assertIsInstance`, `assertAlmostEqual`, `assertRaises`, `@pytest.mark.parametrize`, `NaN` e `inf`.
4. **[tests/test_interface.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/test_interface.py)** — Suíte de 15 testes de integração real e simulada com explicações de `MagicMock`, `spec`, `patch`, `SimpleNamespace`, `setUpClass`, `tearDownClass`, `withdraw`, `winfo_children` e `destroy`.
5. **[tests/features/calculadora.feature](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/features/calculadora.feature)** e **[tests/test_bdd_calculadora.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/test_bdd_calculadora.py)** — Especificação BDD executável em português com explicações das diretivas Gherkin (`# language: pt`, `Funcionalidade`, `Cenário`, `Dado`, `Quando`, `Então`, `E`), `scenarios`, `@pytest.fixture` e `parsers.parse`.
6. **[verificar_qualidade.py](file:///c:/Users/HORUS/Documents/Calculadora%20Python/verificar_qualidade.py)** — Script unificado de automação da qualidade com explicações detalhadas de `AST`, `subprocess`, `Radon (CC, MI, Raw)`, `CRAP`, `Coverage (Statements e Branches)` e `Testes de Mutação (KILLED vs SURVIVED)`.
7. **[tests/roteiro_testes.md](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/roteiro_testes.md)**, **[tests/qa/roteiro_manual.md](file:///c:/Users/HORUS/Documents/Calculadora%20Python/tests/qa/roteiro_manual.md)**, **[README.md](file:///c:/Users/HORUS/Documents/Calculadora%20Python/README.md)** e **[RELATORIO_QUALIDADE.md](file:///c:/Users/HORUS/Documents/Calculadora%20Python/RELATORIO_QUALIDADE.md)** — Documentação funcional, roteiros de QA e relatório técnico integralmente em português do Brasil.


---

### Arquivo Completo: calculadora.py

`python
# ============================================================
# MÓDULO: CALCULADORA
# RESPONSABILIDADE: LÓGICA DE NEGÓCIO
# ============================================================
# [Termos Técnicos deste Módulo]
# - import / from: Comandos nativos do Python para carregar módulos ou classes externas.
# - decimal.Decimal: Tipo numérico de precisão arbitrária em base 10. Evita erros de arredondamento
#   binário do padrão IEEE 754 (ex.: em float comum, 0.1 + 0.2 resulta em 0.30000000000000004).
# - math: Biblioteca matemática padrão do Python (usada aqui para verificar se um número é finito).
# - class: Palavra-chave que define uma classe (molde para criar objetos na Programação Orientada a Objetos).
# - ValueError / TypeError / ZeroDivisionError: Exceções (erros controlados) nativas do Python para
#   valores inválidos, tipos incompatíveis e tentativa de divisão por zero, respectivamente.
# - def / self / return / raise: Palavras-chave do Python para definir um método (def), referenciar a
#   própria instância do objeto (self), devolver um resultado (return) e lançar uma exceção (raise).
# ============================================================

from decimal import Decimal
import math


class ErroEntradaInvalida(ValueError, TypeError):
    """
    Exceção personalizada para entradas inválidas.
    Herda simultaneamente de ValueError (erro de valor) e TypeError (erro de tipo)
    para manter compatibilidade total com qualquer verificação de teste unitário.
    """


# TODO 01: ESTRUTURAÇÃO
# Criar a classe Calculadora.
# Definir a organização dos métodos.
# Separar as operações matemáticas.
class Calculadora:
    """Implementa as regras de negócio e operações matemáticas da calculadora."""

    # TODO 08: VALIDAÇÃO DE DADOS
    # Validar os valores recebidos.
    # Tratar entradas inválidas.
    # Evitar operações com valores incompatíveis.
    def validar_numero(self, valor):
        """
        Valida se o valor é um número real finito e converte para Decimal.
        - isinstance(valor, tipo): Função nativa que verifica se 'valor' pertence a um tipo.
        - bool: Tipo lógico (True/False). Em Python, bool é subclasse de int, por isso é rejeitado explicitamente.
        - int / float: Tipos numéricos nativos para números inteiros (int) e decimais de ponto flutuante (float).
        - math.isfinite(valor): Retorna False para NaN (Not a Number / Não é um Número) e Infinito (inf / -inf).
        """
        if isinstance(valor, bool) or not isinstance(valor, (int, float)):
            raise ErroEntradaInvalida("Entrada inválida: o valor deve ser numérico.")
        if not math.isfinite(valor):
            raise ErroEntradaInvalida("Entrada inválida: o valor deve ser finito.")
        return Decimal(str(valor))

    # TODO 09: RESULTADOS
    # Definir o tratamento de resultados decimais.
    # Evitar perda desnecessária de precisão.
    # Não arredondar internamente os valores sem necessidade.
    def _formatar_resultado(self, valor_decimal):
        """
        Retorna int para resultados inteiros exatos e float para decimais, sem perda de precisão.
        - to_integral_value(): Método da classe Decimal que retorna o valor arredondado para inteiro,
          permitindo comparar se o número possui casas decimais diferentes de zero.
        """
        if valor_decimal == valor_decimal.to_integral_value():
            return int(valor_decimal)
        return float(valor_decimal)

    # TODO 02: ADIÇÃO
    # Implementar método para somar dois números.
    # Retornar o resultado.
    def somar(self, a, b):
        """Soma dois números validados."""
        dec_a = self.validar_numero(a)
        dec_b = self.validar_numero(b)
        return self._formatar_resultado(dec_a + dec_b)

    # TODO 03: SUBTRAÇÃO
    # Implementar método para subtrair dois números.
    # Retornar o resultado.
    def subtrair(self, a, b):
        """Subtrai o segundo número do primeiro."""
        dec_a = self.validar_numero(a)
        dec_b = self.validar_numero(b)
        return self._formatar_resultado(dec_a - dec_b)

    # TODO 04: MULTIPLICAÇÃO
    # Implementar método para multiplicar dois números.
    # Retornar o resultado.
    def multiplicar(self, a, b):
        """Multiplica dois números validados."""
        dec_a = self.validar_numero(a)
        dec_b = self.validar_numero(b)
        return self._formatar_resultado(dec_a * dec_b)

    # TODO 05: DIVISÃO
    # Implementar método para dividir dois números.
    # Impedir divisão por zero.
    # Tratar exceções matemáticas.
    def dividir(self, a, b):
        """
        Divide o primeiro número pelo segundo, impedindo divisão por zero.
        - ZeroDivisionError: Exceção aritmética padrão do Python quando o divisor é zero.
        """
        dec_a = self.validar_numero(a)
        dec_b = self.validar_numero(b)
        if dec_b == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return self._formatar_resultado(dec_a / dec_b)

    # TODO 06: PORCENTAGEM
    # Implementar cálculo de porcentagem.
    # Considerar o comportamento contextual da calculadora.
    def porcentagem(self, valor, base=None, operacao=None):
        """
        Calcula a porcentagem de forma contextual (padrão de calculadoras comerciais/Windows):
        - None: Palavra-chave do Python que representa ausência de valor (nulo).
        - Sem base (base is None) ou em multiplicação/divisão ('*', '/'): retorna a fração (valor / 100).
        - Com base em adição/subtração ('+', '-' ou None): retorna o percentual sobre a base ((base * valor) / 100).
        """
        dec_valor = self.validar_numero(valor)
        if operacao not in (None, "+", "-", "*", "/"):
            raise ValueError("Operação inválida para cálculo de porcentagem.")
        fator = dec_valor / Decimal(100)
        if base is None or operacao in ("*", "/"):
            return self._formatar_resultado(fator)
        dec_base = self.validar_numero(base)
        return self._formatar_resultado(dec_base * fator)

    # TODO 07: INVERSÃO DE SINAL
    # Implementar método para inverter o sinal de um número.
    def inverter_sinal(self, numero):
        """Inverte o sinal de um número (+ para - e - para +), mantendo 0 sem sinal negativo."""
        dec_numero = self.validar_numero(numero)
        return self._formatar_resultado(-dec_numero)

    # TODO 10: REVISÃO
    # Verificar a responsabilidade de cada método.
    # Eliminar duplicações.
    # Garantir que a lógica não dependa do Tkinter.
    def calcular(self, a, operador, b):
        """Executa uma operação aritmética ('+', '-', '*', '/') entre dois operandos usando dicionário de despacho."""
        operacoes = {
            "+": self.somar,
            "-": self.subtrair,
            "*": self.multiplicar,
            "/": self.dividir,
        }
        if operador not in operacoes:
            raise ValueError(f"Operador inválido: {operador}")
        return operacoes[operador](a, b)

    def calcular_encadeado(self, valor_inicial, operacoes):
        """Executa uma sequência encadeada de tuplas (operador, operando) a partir de valor_inicial."""
        acumulado = self._formatar_resultado(self.validar_numero(valor_inicial))
        for operador, operando in operacoes:
            acumulado = self.calcular(acumulado, operador, operando)
        return acumulado

`

---

### Arquivo Completo: main.py

`python
# ============================================================
# MÓDULO: MAIN
# RESPONSABILIDADE: INTERFACE GRÁFICA
# ============================================================
# [Termos Técnicos deste Módulo]
# - tkinter (tk): Biblioteca gráfica padrão do Python (interface para o kit visual Tcl/Tk).
# - ttk (Themed Tk): Submódulo do Tkinter que oferece estilos visuais modernos para componentes.
# - root: Termo técnico do Tkinter para a janela raiz (principal) da aplicação (instância de tk.Tk).
# - Widget: Componente visual da interface gráfica (como Frame, Label ou Button).
# - Frame: Contêiner retangular usado para agrupar e organizar outros componentes na tela.
# - Label: Rótulo visual utilizado para exibir textos ou números (como o visor da calculadora).
# - Button: Botão clicável que dispara uma função (callback) quando acionado pelo usuário.
# - StringVar: Variável reativa do Tkinter; quando seu valor muda via .set(), o Label vinculado
#   na tela é atualizado automaticamente em tempo real.
# - grid: Gerenciador de layout que posiciona componentes em uma tabela de linhas (row) e colunas (column).
# - sticky="nsew": Faz o componente se esticar nas 4 direções cardeais (North/Norte, South/Sul,
#   East/Leste, West/Oeste) para preencher toda a célula da grade no redimensionamento.
# -padx / pady: Espaçamento (margem) horizontal (x) e vertical (y) em pixels.
# - hover: Estado visual de destaque quando o cursor do mouse passa ou clica sobre um botão.
# - bind("<Key>", ...): Conecta eventos de pressionamento de tecla física à função tratadora.
# - keysym: Símbolo técnico da tecla no sistema gráfico (ex.: 'Return' para Enter, 'Escape' para Esc).
# - mainloop(): Laço infinito de eventos do Tkinter que mantém a janela aberta e responsiva.
# ============================================================

# TODO 01: IMPORTAÇÕES
# Importar Tkinter e ttk.
# Importar a classe Calculadora do módulo calculadora.
import tkinter as tk
from tkinter import ttk
from calculadora import Calculadora, ErroEntradaInvalida

# TODO 03: IDENTIDADE VISUAL
# Criar paleta de cores roxas.
# Definir cores de fundo, visor e botões.
# Definir tipografia.
# Definir espaçamentos.
# Garantir contraste e legibilidade.
# As cores utilizam o padrão técnico Hexadecimal RGB (#RRGGBB).
PALETA_CORES = {
    "fundo_janela": "#1E152A",
    "fundo_visor": "#2A1E3F",
    "texto_visor": "#F3EFFE",
    "texto_historico": "#B79CED",
    "botao_numero": "#3B2C54",
    "botao_numero_hover": "#4C3A6E",       # hover: cor exibida ao pressionar/interagir com o botão
    "botao_operador": "#523A78",
    "botao_operador_hover": "#684B96",
    "botao_controle": "#463266",
    "botao_controle_hover": "#5B4282",
    "botao_igual": "#8B5CF6",
    "botao_igual_hover": "#A78BFA",
    "texto_botao": "#FFFFFF",
}

# Tuplas de configuração tipográfica do Tkinter: (Família da Fonte, Tamanho em Pontos, Estilo 'bold' = negrito)
FONTES = {
    "titulo": ("Segoe UI", 10, "bold"),
    "historico": ("Segoe UI", 12),
    "visor": ("Segoe UI", 28, "bold"),
    "botao": ("Segoe UI", 14, "bold"),
}

MAPA_OPERADORES_VISUAIS = {"×": "*", "÷": "/"}
SIMBOLOS_EXIBICAO = {"*": "×", "/": "÷", "+": "+", "-": "-"}


class InterfaceCalculadora:
    """Controlador e interface gráfica (Tkinter) da Calculadora Python."""

    def __init__(self, root=None, calculadora=None):
        """
        Inicializa o controlador da calculadora.
        - __init__: Método construtor especial do Python, executado automaticamente ao criar o objeto.
        - root: Instância da janela principal tk.Tk (ou None quando executada em testes sem janela).
        """
        # TODO 09: INTEGRAÇÃO
        # Conectar a interface à classe Calculadora.
        # Enviar operandos e operadores.
        # Receber resultados.
        # Atualizar o visor.
        self.calculadora = calculadora if calculadora is not None else Calculadora()
        self.root = root
        self.botoes = {}
        self.var_visor = None
        self.var_historico = None

        # TODO 11: ESTADO DA INTERFACE
        # Controlar entrada atual.
        # Controlar operação pendente.
        # Controlar resultado anterior.
        # Sincronizar os estados com a lógica matemática.
        self.entrada_atual = "0"
        self.operando_anterior = None
        self.operador_pendente = None
        self.historico_texto = ""
        self.aguardando_novo_operando = False
        self.em_erro = False

        if self.root is not None:
            self._configurar_janela()
            self._construir_interface()
            self._configurar_teclado()
            self._atualizar_interface()

    # TODO 02: JANELA PRINCIPAL
    # Criar a janela principal.
    # Definir título e dimensões.
    # Configurar tamanho mínimo.
    # Centralizar a janela.
    # Configurar comportamento de redimensionamento.
    def _configurar_janela(self):
        """
        Configura título, dimensões, tamanho mínimo, centralização e redimensionamento.
        - minsize: Define a largura e altura mínimas em pixels para evitar distorção da interface.
        - winfo_screenwidth / winfo_screenheight: Consultam a resolução do monitor em pixels.
        - geometry("LxA+X+Y"): Define Largura x Altura e a posição X, Y da janela na tela.
        - weight (peso): Define a proporção de expansão das linhas/colunas ao redimensionar a janela.
        """
        self.root.title("Calculadora Python")
        largura, altura = 360, 520
        self.root.minsize(320, 460)
        self.root.configure(bg=PALETA_CORES["fundo_janela"])
        largura_tela = self.root.winfo_screenwidth()
        altura_tela = self.root.winfo_screenheight()
        pos_x = max((largura_tela - largura) // 2, 0)
        pos_y = max((altura_tela - altura) // 2, 0)
        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.root.resizable(True, True)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    # TODO 04: ESTRUTURA VISUAL
    # Criar contêiner principal.
    # Criar área superior.
    # Criar área de exibição.
    # Criar painel de botões.
    # Organizar componentes em grade.
    def _construir_interface(self):
        """
        Constrói os contêineres, o visor duplo e a grade de botões.
        - anchor="w": Alinha o texto à esquerda (West / Oeste).
        - pack(fill="x"): Empacota o rótulo preenchendo toda a largura horizontal (eixo X).
        """
        self.estilo = ttk.Style(self.root)
        self.container_principal = tk.Frame(
            self.root, bg=PALETA_CORES["fundo_janela"], padx=12, pady=12
        )
        self.container_principal.grid(row=0, column=0, sticky="nsew")
        self.container_principal.grid_rowconfigure(1, weight=1)
        self.container_principal.grid_rowconfigure(2, weight=4)
        self.container_principal.grid_columnconfigure(0, weight=1)

        self.area_superior = tk.Frame(self.container_principal, bg=PALETA_CORES["fundo_janela"])
        self.area_superior.grid(row=0, column=0, sticky="ew", pady=(0, 6))
        tk.Label(
            self.area_superior,
            text="Calculadora Padrão",
            font=FONTES["titulo"],
            bg=PALETA_CORES["fundo_janela"],
            fg=PALETA_CORES["texto_historico"],
            anchor="w",
        ).pack(fill="x")

        self._construir_visor()
        self._construir_botoes()

    # TODO 05: VISOR
    # Criar visor numérico.
    # Alinhar valores à direita.
    # Criar exibição da operação atual.
    # Atualizar o visor conforme a interação.
    def _construir_visor(self):
        """
        Cria os rótulos de histórico (operação atual) e visor numérico principal.
        - anchor="e" e justify="right": Alinham os números à direita (East / Leste), padrão de calculadoras.
        - textvariable: Conecta o Label à variável reativa StringVar.
        """
        self.var_historico = tk.StringVar(master=self.root, value="")
        self.var_visor = tk.StringVar(master=self.root, value="0")

        self.area_exibicao = tk.Frame(
            self.container_principal, bg=PALETA_CORES["fundo_visor"], padx=14, pady=10
        )
        self.area_exibicao.grid(row=1, column=0, sticky="nsew", pady=(0, 12))
        self.area_exibicao.grid_rowconfigure(0, weight=1)
        self.area_exibicao.grid_rowconfigure(1, weight=2)
        self.area_exibicao.grid_columnconfigure(0, weight=1)

        self.lbl_historico = tk.Label(
            self.area_exibicao,
            textvariable=self.var_historico,
            font=FONTES["historico"],
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_historico"],
            anchor="e",
            justify="right",
        )
        self.lbl_historico.grid(row=0, column=0, sticky="nsew")

        self.lbl_visor = tk.Label(
            self.area_exibicao,
            textvariable=self.var_visor,
            font=FONTES["visor"],
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
            anchor="e",
            justify="right",
        )
        self.lbl_visor.grid(row=1, column=0, sticky="nsew")

    # TODO 06: BOTÕES NUMÉRICOS
    # Criar botões de 0 a 9.
    # Criar botão decimal.
    # Implementar eventos de clique.
    # Conectar os eventos ao controle de entrada.
    # TODO 07: BOTÕES DE OPERAÇÃO
    # Criar adição, subtração, multiplicação e divisão.
    # Criar botão de porcentagem.
    # Criar botão de inversão de sinal.
    # Criar botão de igualdade.
    # TODO 08: BOTÕES DE CONTROLE
    # Implementar C.
    # Implementar CE.
    # Implementar Backspace.
    def _construir_botoes(self):
        """
        Cria e posiciona todos os botões numéricos, de operação e de controle em grade.
        - columnspan=4: Faz o botão de igual ('=') abranger as 4 colunas da última linha da grade.
        """
        self.painel_botoes = tk.Frame(self.container_principal, bg=PALETA_CORES["fundo_janela"])
        self.painel_botoes.grid(row=2, column=0, sticky="nsew")

        layout_grade = [
            [("%", "operador"), ("CE", "controle"), ("C", "controle"), ("⌫", "controle")],
            [("7", "numero"), ("8", "numero"), ("9", "numero"), ("÷", "operador")],
            [("4", "numero"), ("5", "numero"), ("6", "numero"), ("×", "operador")],
            [("1", "numero"), ("2", "numero"), ("3", "numero"), ("-", "operador")],
            [("±", "operador"), ("0", "numero"), (".", "numero"), ("+", "operador")],
        ]

        for indice_linha, linha in enumerate(layout_grade):
            self.painel_botoes.grid_rowconfigure(indice_linha, weight=1)
            for indice_coluna, (rotulo, categoria) in enumerate(linha):
                self.painel_botoes.grid_columnconfigure(indice_coluna, weight=1)
                self._criar_botao(rotulo, categoria, indice_linha, indice_coluna)

        self.painel_botoes.grid_rowconfigure(len(layout_grade), weight=1)
        self._criar_botao("=", "igual", len(layout_grade), 0, columnspan=4)

    def _criar_botao(self, rotulo, categoria, linha, coluna, columnspan=1):
        """
        Instancia um botão estilizado na grade e conecta seu comando de clique.
        - relief="flat" e bd=0: Removem a borda 3D antiga para manter o design moderno e plano.
        - cursor="hand2": Exibe o cursor de mão ao apontar para o botão.
        - lambda r=rotulo: Cria uma função anônima que captura o rótulo exato daquele botão no clique.
        """
        cor_fundo = PALETA_CORES[f"botao_{categoria}"]
        cor_hover = PALETA_CORES[f"botao_{categoria}_hover"]
        botao = tk.Button(
            self.painel_botoes,
            text=rotulo,
            font=FONTES["botao"],
            bg=cor_fundo,
            fg=PALETA_CORES["texto_botao"],
            activebackground=cor_hover,
            activeforeground=PALETA_CORES["texto_botao"],
            relief="flat",
            bd=0,
            cursor="hand2",
            command=lambda r=rotulo: self.pressionar_botao(r),
        )
        botao.grid(
            row=linha, column=coluna, columnspan=columnspan, sticky="nsew", padx=3, pady=3
        )
        self.botoes[rotulo] = botao

    # TODO 10: TECLADO
    # Implementar entrada numérica.
    # Reconhecer operadores.
    # Reconhecer Enter.
    # Reconhecer Backspace.
    # Reconhecer Escape e Delete.
    def _configurar_teclado(self):
        """Vincula qualquer evento de tecla pressionada ('<Key>') ao método processar_tecla."""
        self.root.bind("<Key>", self.processar_tecla)

    def processar_tecla(self, evento):
        """
        Traduz eventos de teclado físico e numérico (Numpad) para ações da calculadora.
        - Return / KP_Enter: Códigos técnicos (keysym) do Tkinter para Enter principal e Enter do teclado numérico.
        - BackSpace / Escape / Delete / F9: Códigos técnicos para apagar dígito, limpar tudo, limpar entrada e inverter sinal.
        """
        keysym = getattr(evento, "keysym", "")
        char = getattr(evento, "char", "")

        mapa_teclas_especiais = {
            "Return": "=",
            "KP_Enter": "=",
            "BackSpace": "⌫",
            "Escape": "C",
            "Delete": "CE",
            "F9": "±",
        }
        if keysym in mapa_teclas_especiais:
            self.pressionar_botao(mapa_teclas_especiais[keysym])
            return
        if char in (",", "."):
            self.inserir_decimal()
            return
        if char.lower() == "c":
            self.limpar_tudo()
            return
        if char in "0123456789+-*/=%":
            self.pressionar_botao(char)

    def pressionar_botao(self, rotulo):
        """Despacha o clique de um botão ou atalho equivalente para o método correspondente."""
        acoes_diretas = {
            "C": self.limpar_tudo,
            "CE": self.limpar_entrada,
            "⌫": self.retroceder,
            "±": self.inverter_sinal,
            "%": self.calcular_porcentagem,
            "=": self.calcular_resultado,
            ".": self.inserir_decimal,
        }
        if rotulo in acoes_diretas:
            acoes_diretas[rotulo]()
        elif rotulo in ("+", "-", "*", "/", "×", "÷"):
            self.selecionar_operador(rotulo)
        elif rotulo.isdigit():
            self.inserir_digito(rotulo)

    def inserir_digito(self, digito):
        """Insere um dígito numérico (0-9) no visor atual, tratando recuperação automática de erro."""
        if self.em_erro:
            self.limpar_tudo()
        if self.aguardando_novo_operando:
            self.entrada_atual = str(digito)
            self.aguardando_novo_operando = False
        elif self.entrada_atual == "0":
            self.entrada_atual = str(digito)
        else:
            self.entrada_atual += str(digito)
        self._atualizar_interface()

    def inserir_decimal(self):
        """Insere o separador decimal ('.'), impedindo múltiplos pontos no mesmo operando."""
        if self.em_erro:
            self.limpar_tudo()
        if self.aguardando_novo_operando:
            self.entrada_atual = "0."
            self.aguardando_novo_operando = False
        elif "." not in self.entrada_atual:
            self.entrada_atual += "."
        self._atualizar_interface()

    def selecionar_operador(self, operador):
        """Define o operador aritmético pendente e resolve operações encadeadas quando aplicável."""
        if self.em_erro:
            return
        op_interno = MAPA_OPERADORES_VISUAIS.get(operador, operador)
        if self.operador_pendente is not None and not self.aguardando_novo_operando:
            if not self._executar_operacao_pendente():
                return
        else:
            self.operando_anterior = self._converter_entrada(self.entrada_atual)

        self.operador_pendente = op_interno
        self.aguardando_novo_operando = True
        simbolo = SIMBOLOS_EXIBICAO.get(op_interno, op_interno)
        self.historico_texto = f"{self._formatar_exibicao(self.operando_anterior)} {simbolo}"
        self._atualizar_interface()

    def calcular_resultado(self):
        """Executa a operação pendente ao pressionar '=' e atualiza o visor e o histórico."""
        if self.em_erro:
            self.limpar_tudo()
            return
        if self.operador_pendente is None:
            return
        operando_atual = self._converter_entrada(self.entrada_atual)
        op_anterior = self.operando_anterior
        simbolo = SIMBOLOS_EXIBICAO.get(self.operador_pendente, self.operador_pendente)
        if self._executar_operacao_pendente():
            self.historico_texto = (
                f"{self._formatar_exibicao(op_anterior)} {simbolo} "
                f"{self._formatar_exibicao(operando_atual)} ="
            )
            self.operador_pendente = None
            self.aguardando_novo_operando = True
            self._atualizar_interface()

    def calcular_porcentagem(self):
        """Calcula a porcentagem contextual delegando para a classe Calculadora."""
        if self.em_erro:
            return
        valor_atual = self._converter_entrada(self.entrada_atual)
        resultado = self.calculadora.porcentagem(
            valor_atual, self.operando_anterior, self.operador_pendente
        )
        self.entrada_atual = self._formatar_exibicao(resultado)
        self.aguardando_novo_operando = False
        self._atualizar_interface()

    def inverter_sinal(self):
        """Inverte o sinal do número exibido no visor delegando para a classe Calculadora."""
        if self.em_erro:
            return
        valor_atual = self._converter_entrada(self.entrada_atual)
        invertido = self.calculadora.inverter_sinal(valor_atual)
        self.entrada_atual = self._formatar_exibicao(invertido)
        self._atualizar_interface()

    def limpar_tudo(self):
        """Limpa completamente o visor, o histórico, os operandos e o estado de erro (botão C = Clear)."""
        self.entrada_atual = "0"
        self.operando_anterior = None
        self.operador_pendente = None
        self.historico_texto = ""
        self.aguardando_novo_operando = False
        self.em_erro = False
        self._atualizar_interface()

    def limpar_entrada(self):
        """Limpa apenas a entrada atual mantendo a operação pendente (botão CE = Clear Entry)."""
        if self.em_erro:
            self.limpar_tudo()
            return
        self.entrada_atual = "0"
        self.aguardando_novo_operando = False
        self._atualizar_interface()

    def retroceder(self):
        """Remove o último dígito inserido no visor atual (botão Backspace ⌫)."""
        if self.em_erro:
            self.limpar_tudo()
            return
        if self.aguardando_novo_operando:
            return
        nova_entrada = self.entrada_atual[:-1]
        if nova_entrada in ("", "-", "-0"):
            self.entrada_atual = "0"
        else:
            self.entrada_atual = nova_entrada
        self._atualizar_interface()

    # TODO 12: TRATAMENTO DE ERROS
    # Apresentar erros de maneira compreensível.
    # Evitar encerramento inesperado.
    # Permitir recuperação após erros.
    def _executar_operacao_pendente(self):
        """Executa o cálculo pendente na classe Calculadora e captura exceções matemáticas (try/except)."""
        operando_atual = self._converter_entrada(self.entrada_atual)
        try:
            resultado = self.calculadora.calcular(
                self.operando_anterior, self.operador_pendente, operando_atual
            )
            self.operando_anterior = resultado
            self.entrada_atual = self._formatar_exibicao(resultado)
            return True
        except ZeroDivisionError:
            self._registrar_erro("Erro: Divisão por zero")
            return False
        except (ErroEntradaInvalida, ValueError, ArithmeticError):
            self._registrar_erro("Erro")
            return False

    def _registrar_erro(self, mensagem):
        """Coloca a interface em estado de erro amigável sem encerrar a aplicação."""
        self.entrada_atual = mensagem
        self.historico_texto = ""
        self.operando_anterior = None
        self.operador_pendente = None
        self.aguardando_novo_operando = True
        self.em_erro = True
        self._atualizar_interface()

    def _converter_entrada(self, texto):
        """Converte o texto (str) do visor em int (inteiro) ou float (decimal) para envio à Calculadora."""
        valor = float(texto)
        return int(valor) if valor.is_integer() else valor

    def _formatar_exibicao(self, valor):
        """Formata um valor numérico para texto sem sufixo '.0' desnecessário."""
        if isinstance(valor, float) and valor.is_integer():
            return str(int(valor))
        return str(valor)

    def _atualizar_interface(self):
        """Sincroniza as variáveis StringVar do Tkinter com o estado interno da calculadora."""
        if self.var_visor is not None:
            self.var_visor.set(self.entrada_atual)
        if self.var_historico is not None:
            self.var_historico.set(self.historico_texto)

    def obter_visor(self):
        """Retorna o texto atualmente exibido no visor principal."""
        return self.entrada_atual

    def obter_historico(self):
        """Retorna o texto atualmente exibido no visor de histórico."""
        return self.historico_texto


# TODO 13: INICIALIZAÇÃO
# Instanciar a calculadora.
# Inicializar a interface.
# Executar o loop principal.
def iniciar_aplicacao():
    """Instancia a calculadora, inicializa a interface Tkinter e executa o laço principal (mainloop)."""
    janela = tk.Tk()
    app = InterfaceCalculadora(root=janela, calculadora=Calculadora())
    janela.mainloop()
    return app


# pragma: no cover é uma instrução técnica para a ferramenta coverage.py não exigir cobertura
# da linha de guarda '__main__' quando o arquivo é importado como módulo pelos testes.
if __name__ == "__main__":  # pragma: no cover
    iniciar_aplicacao()

`

---

### Arquivo Completo: tests/test_calculadora.py

`python
# ============================================================
# TESTES UNITÁRIOS: CALCULADORA
# ============================================================
# [Termos Técnicos deste Módulo]
# - unittest: Biblioteca nativa de testes unitários do Python (inspirada no JUnit).
# - pytest: Framework avançado de testes em Python que permite testes parametrizados e asserções diretas.
# - unittest.TestCase: Classe base da qual herdam as suítes de testes no padrão unittest.
# - setUp(self): Método especial do unittest executado automaticamente antes de cada teste para
#   preparar o ambiente (instanciar objetos e variáveis de apoio).
# - assertEqual(a, b): Verifica se 'a' é igual a 'b'; se não for, o teste falha.
# - assertIsInstance(obj, tipo): Verifica se 'obj' é instância da classe 'tipo' (ex.: int ou float).
# - assertAlmostEqual(a, b, places=12): Compara números decimais periódicos (como 1/3) até 12 casas decimais.
# - assertRaises(Excecao) / pytest.raises(Excecao): Confirmam que o código dentro do bloco 'with'
#   lança obrigatoriamente a exceção esperada (ex.: ZeroDivisionError na divisão por zero).
# - @pytest.mark.parametrize: Decorador do pytest que executa a mesma função de teste dezenas de vezes
#   com diferentes combinações de entradas e resultados esperados.
# - float("nan") / float("inf"): Representações técnicas IEEE 754 para "Not a Number" (Não é um Número)
#   e "Infinity" (Infinito positivo ou negativo).
# ============================================================

# TODO 01: IMPORTAÇÕES
# Importar unittest.
# Importar a classe Calculadora.
import unittest
import pytest
from calculadora import Calculadora


# TODO 02: PREPARAÇÃO
# Criar uma classe de testes.
# Inicializar os objetos necessários.
# Preparar os valores utilizados nos testes.
class TestCalculadora(unittest.TestCase):
    """Suíte de testes unitários compatível com unittest e pytest para a classe Calculadora."""

    def setUp(self):
        """Prepara uma nova instância da Calculadora e valores padrão antes de cada método de teste."""
        self.calc = Calculadora()
        self.positivo_a = 10
        self.positivo_b = 5
        self.negativo_a = -10
        self.negativo_b = -5
        self.decimal_a = 2.5
        self.decimal_b = 0.5
        self.zero = 0

    # TODO 03: TESTE DE ADIÇÃO
    # Testar números positivos.
    # Testar números negativos.
    # Testar números decimais.
    # Testar resultado zero.
    def test_adicao_positivos(self):
        self.assertEqual(self.calc.somar(self.positivo_a, self.positivo_b), 15)

    def test_adicao_negativos(self):
        self.assertEqual(self.calc.somar(self.negativo_a, self.negativo_b), -15)
        self.assertEqual(self.calc.somar(self.positivo_a, self.negativo_b), 5)

    def test_adicao_decimais(self):
        resultado_inteiro = self.calc.somar(self.decimal_a, self.decimal_b)
        self.assertEqual(resultado_inteiro, 3)
        self.assertIsInstance(resultado_inteiro, int)
        resultado_decimal = self.calc.somar(0.1, 0.2)
        self.assertEqual(resultado_decimal, 0.3)
        self.assertIsInstance(resultado_decimal, float)

    def test_adicao_resultado_zero(self):
        self.assertEqual(self.calc.somar(10, -10), 0)
        self.assertEqual(self.calc.somar(self.zero, self.zero), 0)

    # TODO 04: TESTE DE SUBTRAÇÃO
    # Testar números positivos.
    # Testar números negativos.
    # Testar resultados negativos.
    # Testar resultado zero.
    def test_subtracao_positivos(self):
        self.assertEqual(self.calc.subtrair(self.positivo_a, self.positivo_b), 5)

    def test_subtracao_negativos(self):
        self.assertEqual(self.calc.subtrair(self.negativo_a, self.negativo_b), -5)
        self.assertEqual(self.calc.subtrair(self.positivo_a, self.negativo_b), 15)

    def test_subtracao_resultado_negativo(self):
        self.assertEqual(self.calc.subtrair(5, 10), -5)
        self.assertEqual(self.calc.subtrair(0.1, 0.3), -0.2)

    def test_subtracao_resultado_zero(self):
        self.assertEqual(self.calc.subtrair(10, 10), 0)
        self.assertEqual(self.calc.subtrair(self.zero, self.zero), 0)

    # TODO 05: TESTE DE MULTIPLICAÇÃO
    # Testar números positivos.
    # Testar números negativos.
    # Testar multiplicação por zero.
    # Testar números decimais.
    def test_multiplicacao_positivos(self):
        self.assertEqual(self.calc.multiplicar(self.positivo_a, self.positivo_b), 50)

    def test_multiplicacao_negativos(self):
        self.assertEqual(self.calc.multiplicar(self.negativo_a, self.negativo_b), 50)
        self.assertEqual(self.calc.multiplicar(self.positivo_a, self.negativo_b), -50)

    def test_multiplicacao_por_zero(self):
        self.assertEqual(self.calc.multiplicar(self.positivo_a, self.zero), 0)
        self.assertEqual(self.calc.multiplicar(self.negativo_a, self.zero), 0)

    def test_multiplicacao_decimais(self):
        self.assertEqual(self.calc.multiplicar(self.decimal_a, self.decimal_b), 1.25)
        self.assertEqual(self.calc.multiplicar(0.1, 0.2), 0.02)

    # TODO 06: TESTE DE DIVISÃO
    # Testar divisões exatas.
    # Testar divisões com resultados decimais.
    # Testar números negativos.
    # Testar divisão por zero.
    def test_divisao_exata(self):
        self.assertEqual(self.calc.dividir(self.positivo_a, self.positivo_b), 2)

    def test_divisao_decimais(self):
        self.assertEqual(self.calc.dividir(5, 2), 2.5)
        self.assertEqual(self.calc.dividir(0.3, 0.1), 3)
        self.assertAlmostEqual(self.calc.dividir(1, 3), 1 / 3, places=12)

    def test_divisao_negativos(self):
        self.assertEqual(self.calc.dividir(self.negativo_a, self.negativo_b), 2)
        self.assertEqual(self.calc.dividir(self.positivo_a, self.negativo_b), -2)
        self.assertEqual(self.calc.dividir(0, 5), 0)
        self.assertEqual(self.calc.dividir(0, -5), 0)

    def test_divisao_por_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(10, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(0, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.dividir(-5.5, 0.0)

    # TODO 07: TESTE DE PORCENTAGEM
    # Testar porcentagens inteiras.
    # Testar porcentagens decimais.
    # Testar valores negativos.
    # Testar comportamento contextual.
    def test_porcentagem_inteira(self):
        self.assertEqual(self.calc.porcentagem(50), 0.5)
        self.assertEqual(self.calc.porcentagem(100), 1)

    def test_porcentagem_decimal(self):
        self.assertEqual(self.calc.porcentagem(12.5), 0.125)
        self.assertEqual(self.calc.porcentagem(2.5, 200), 5)

    def test_porcentagem_negativa(self):
        self.assertEqual(self.calc.porcentagem(-25), -0.25)
        self.assertEqual(self.calc.porcentagem(-10, 200, "+"), -20)

    def test_porcentagem_contextual(self):
        # Contexto de adição e subtração: valor percentual sobre a base
        self.assertEqual(self.calc.porcentagem(10, 200, "+"), 20)
        self.assertEqual(self.calc.porcentagem(10, 200, "-"), 20)
        self.assertEqual(self.calc.porcentagem(10, 200, None), 20)
        # Contexto de multiplicação e divisão: fração decimal (valor / 100)
        self.assertEqual(self.calc.porcentagem(10, 200, "*"), 0.1)
        self.assertEqual(self.calc.porcentagem(10, 200, "/"), 0.1)

    # TODO 08: TESTE DE INVERSÃO DE SINAL
    # Testar conversão de positivo para negativo.
    # Testar conversão de negativo para positivo.
    # Testar valor zero.
    def test_inversao_sinal_positivo_para_negativo(self):
        self.assertEqual(self.calc.inverter_sinal(5), -5)
        self.assertEqual(self.calc.inverter_sinal(2.5), -2.5)

    def test_inversao_sinal_negativo_para_positivo(self):
        self.assertEqual(self.calc.inverter_sinal(-5), 5)
        self.assertEqual(self.calc.inverter_sinal(-2.5), 2.5)

    def test_inversao_sinal_zero(self):
        resultado = self.calc.inverter_sinal(0)
        self.assertEqual(resultado, 0)
        self.assertEqual(str(resultado), "0")

    # TODO 09: TESTE DE VALIDAÇÕES
    # Testar entradas inválidas.
    # Testar valores incompatíveis.
    # Verificar tratamento de exceções.
    def test_validacoes_entradas_invalidas(self):
        entradas_invalidas = ["abc", "10", None, [1, 2], {"a": 1}, True, False, float("nan"), float("inf"), float("-inf")]
        for invalido in entradas_invalidas:
            with self.assertRaises((ValueError, TypeError)):
                self.calc.somar(invalido, 5)
            with self.assertRaises((ValueError, TypeError)):
                self.calc.somar(5, invalido)
            with self.assertRaises((ValueError, TypeError)):
                self.calc.inverter_sinal(invalido)

    def test_validacoes_operadores_invalidos(self):
        with self.assertRaises(ValueError):
            self.calc.calcular(10, "^", 2)
        with self.assertRaises(ValueError):
            self.calc.porcentagem(10, 100, "^")

    def test_operacoes_encadeadas(self):
        # ((10 + 5) * 2 - 6) / 4 = 6
        sequencia = [("+", 5), ("*", 2), ("-", 6), ("/", 4)]
        self.assertEqual(self.calc.calcular_encadeado(10, sequencia), 6)
        self.assertEqual(self.calc.calcular_encadeado(10.0, []), 10)
        self.assertIsInstance(self.calc.calcular_encadeado(10.0, []), int)
        with self.assertRaises((ValueError, TypeError)):
            self.calc.calcular_encadeado("invalido", [])


# ============================================================
# TESTES PARAMETRIZADOS COM PYTEST
# ============================================================

@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 15),
        (0, 0, 0),
        (-10, -5, -15),
        (-10, 15, 5),
        (2.5, 2.5, 5),
        (0.1, 0.2, 0.3),
        (1000000, 2000000, 3000000),
        (-0.75, 0.25, -0.5),
    ],
)
def test_parametrizado_adicao(a, b, esperado):
    calc = Calculadora()
    assert calc.somar(a, b) == esperado
    assert calc.calcular(a, "+", b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 5),
        (5, 10, -5),
        (0, 0, 0),
        (-10, -5, -5),
        (-10, 5, -15),
        (2.5, 1.25, 1.25),
        (0.3, 0.1, 0.2),
        (10, 10, 0),
    ],
)
def test_parametrizado_subtracao(a, b, esperado):
    calc = Calculadora()
    assert calc.subtrair(a, b) == esperado
    assert calc.calcular(a, "-", b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 50),
        (10, 0, 0),
        (0, 10, 0),
        (-10, 5, -50),
        (-10, -5, 50),
        (2.5, 4, 10),
        (0.1, 0.2, 0.02),
        (1.5, -2.0, -3),
    ],
)
def test_parametrizado_multiplicacao(a, b, esperado):
    calc = Calculadora()
    assert calc.multiplicar(a, b) == esperado
    assert calc.calcular(a, "*", b) == esperado


@pytest.mark.parametrize(
    "a, b, esperado",
    [
        (10, 5, 2),
        (5, 2, 2.5),
        (-10, 5, -2),
        (-10, -5, 2),
        (10, -5, -2),
        (0, 5, 0),
        (0.3, 0.1, 3),
        (7.5, 2.5, 3),
    ],
)
def test_parametrizado_divisao(a, b, esperado):
    calc = Calculadora()
    assert calc.dividir(a, b) == esperado
    assert calc.calcular(a, "/", b) == esperado


@pytest.mark.parametrize("dividendo", [10, -10, 0, 2.5, -0.001])
def test_parametrizado_divisao_por_zero(dividendo):
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.dividir(dividendo, 0)
    with pytest.raises(ZeroDivisionError):
        calc.calcular(dividendo, "/", 0)


@pytest.mark.parametrize(
    "valor, base, operacao, esperado",
    [
        (50, None, None, 0.5),
        (25, None, "+", 0.25),
        (10, 200, "+", 20),
        (10, 200, "-", 20),
        (15, 300, None, 45),
        (10, 200, "*", 0.1),
        (10, 200, "/", 0.1),
        (0, 200, "+", 0),
        (-20, 150, "+", -30),
        (12.5, 80, "+", 10),
    ],
)
def test_parametrizado_porcentagem(valor, base, operacao, esperado):
    calc = Calculadora()
    assert calc.porcentagem(valor, base, operacao) == esperado


@pytest.mark.parametrize(
    "entrada, esperado",
    [
        (5, -5),
        (-5, 5),
        (0, 0),
        (0.0, 0),
        (3.14, -3.14),
        (-3.14, 3.14),
    ],
)
def test_parametrizado_inversao_sinal(entrada, esperado):
    calc = Calculadora()
    assert calc.inverter_sinal(entrada) == esperado


@pytest.mark.parametrize(
    "invalido",
    ["texto", "", "123", None, True, False, [1], (1,), {"x": 1}, float("nan"), float("inf"), float("-inf")],
)
def test_parametrizado_valores_invalidos(invalido):
    calc = Calculadora()
    with pytest.raises((ValueError, TypeError)):
        calc.validar_numero(invalido)
    with pytest.raises((ValueError, TypeError)):
        calc.porcentagem(invalido)
    with pytest.raises((ValueError, TypeError)):
        calc.dividir(10, invalido)
    if invalido is not None:
        with pytest.raises((ValueError, TypeError)):
            calc.porcentagem(10, invalido, "+")


@pytest.mark.parametrize(
    "inicial, operacoes, esperado",
    [
        (10, [("+", 5), ("-", 3), ("*", 2), ("/", 4)], 6),
        (0, [("+", 2.5), ("*", 4), ("-", 10)], 0),
        (-5, [("*", -3), ("+", 5), ("/", 4)], 5),
        (100, [("-", 20), ("/", 8), ("*", 0.5)], 5),
    ],
)
def test_parametrizado_operacoes_encadeadas(inicial, operacoes, esperado):
    calc = Calculadora()
    assert calc.calcular_encadeado(inicial, operacoes) == esperado


# TODO 10: EXECUÇÃO
# Executar todos os testes.
# Apresentar resultados.
# Identificar falhas.
if __name__ == "__main__":  # pragma: no cover
    unittest.main()

`

---

### Arquivo Completo: tests/test_interface.py

`python
# ============================================================
# TESTES DE INTEGRAÇÃO: INTERFACE
# ============================================================
# [Termos Técnicos deste Módulo]
# - unittest.mock (MagicMock / patch): Biblioteca nativa do Python para criar objetos simulados (Mocks)
#   e substituir temporariamente funções/classes reais durante um teste (patch), permitindo verificar
#   se a interface enviou os parâmetros exatos esperados para a Calculadora.
# - SimpleNamespace: Classe utilitária do módulo 'types' usada para criar objetos leves com atributos
#   nomeados (como 'char' e 'keysym'), simulando eventos reais de teclado do Tkinter.
# - @classmethod / setUpClass / tearDownClass: Métodos de classe do unittest executados uma única vez
#   no início e no fim de toda a bateria de testes (usados para criar e destruir a janela raiz Tk).
# - root.withdraw(): Oculta a janela gráfica da tela durante a execução automatizada dos testes,
#   permitindo testar todos os componentes reais do Tkinter sem abrir janelas piscando para o usuário.
# - winfo_children() / destroy(): Métodos do Tkinter para listar e remover os componentes filhos
#   da janela entre um teste e outro, garantindo isolamento total.
# - spec=Calculadora: Garante que o objeto simulado (MagicMock) aceite apenas métodos que realmente
#   existem na classe Calculadora.
# - assert_called_once_with(...): Verifica que o método simulado foi chamado exatamente uma vez
#   e com os argumentos especificados.
# - side_effect: Configura um Mock para lançar uma exceção ou executar uma ação específica quando chamado.
# ============================================================

# TODO 01: IMPORTAÇÕES
# Importar unittest.
# Importar os módulos necessários.
# Preparar os recursos para testes da interface.
import tkinter as tk
import unittest
from unittest.mock import MagicMock, patch
from types import SimpleNamespace
from calculadora import Calculadora
from main import InterfaceCalculadora, PALETA_CORES


# TODO 02: INICIALIZAÇÃO
# Preparar a instância da interface.
# Verificar a criação dos componentes.
# Verificar a inicialização do visor.
class TestIntegracaoInterface(unittest.TestCase):
    """Testes de integração entre InterfaceCalculadora (main.py) e Calculadora (calculadora.py)."""

    @classmethod
    def setUpClass(cls):
        """Inicializa a janela raiz do Tkinter em modo oculto (withdraw) uma única vez para a suíte."""
        try:
            cls.root = tk.Tk()
            cls.root.withdraw()
            cls.tk_disponivel = True
        except tk.TclError:
            cls.root = None
            cls.tk_disponivel = False

    @classmethod
    def tearDownClass(cls):
        """Destrói a janela raiz do Tkinter ao final da suíte de testes."""
        if cls.root is not None:
            cls.root.destroy()

    def setUp(self):
        """Recria uma instância limpa da Calculadora e da InterfaceCalculadora antes de cada teste."""
        self.calculadora = Calculadora()
        if self.tk_disponivel:
            for componente in self.root.winfo_children():
                componente.destroy()
            self.app = InterfaceCalculadora(root=self.root, calculadora=self.calculadora)
        else:
            self.app = InterfaceCalculadora(root=None, calculadora=self.calculadora)

    def test_inicializacao_visor_e_componentes(self):
        self.assertEqual(self.app.obter_visor(), "0")
        self.assertEqual(self.app.obter_historico(), "")
        self.assertIs(self.app.calculadora, self.calculadora)
        self.assertIn("fundo_janela", PALETA_CORES)
        if self.tk_disponivel:
            self.assertGreaterEqual(len(self.app.botoes), 20)
            self.assertIn("=", self.app.botoes)
            self.assertIn("C", self.app.botoes)

    # TODO 03: ENTRADA NUMÉRICA
    # Verificar a entrada de números.
    # Verificar entrada decimal.
    # Verificar múltiplos separadores decimais.
    def test_entrada_numerica_e_decimal(self):
        self.app.inserir_digito("0")
        self.assertEqual(self.app.obter_visor(), "0")
        self.app.inserir_digito("4")
        self.app.inserir_digito("2")
        self.assertEqual(self.app.obter_visor(), "42")
        self.app.inserir_decimal()
        self.app.inserir_digito("5")
        self.assertEqual(self.app.obter_visor(), "42.5")
        # Múltiplos separadores decimais devem ser ignorados
        self.app.inserir_decimal()
        self.app.inserir_digito("8")
        self.assertEqual(self.app.obter_visor(), "42.58")

    def test_entrada_decimal_apos_operador(self):
        self.app.inserir_digito("5")
        self.app.selecionar_operador("+")
        self.app.inserir_decimal()
        self.app.inserir_digito("2")
        self.assertEqual(self.app.obter_visor(), "0.2")
        self.app.calcular_resultado()
        self.assertEqual(self.app.obter_visor(), "5.2")

    # TODO 04: INTERAÇÃO COM OPERAÇÕES
    # Verificar comunicação entre interface e calculadora.
    # Testar adição.
    # Testar subtração.
    # Testar multiplicação.
    # Testar divisão.
    def test_interacao_adicao(self):
        self.app.pressionar_botao("1")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("+")
        self.assertEqual(self.app.obter_historico(), "10 +")
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "15")
        self.assertEqual(self.app.obter_historico(), "10 + 5 =")

    def test_interacao_subtracao(self):
        self.app.pressionar_botao("2")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("-")
        self.app.pressionar_botao("8")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "12")

    def test_interacao_multiplicacao(self):
        self.app.pressionar_botao("6")
        self.app.pressionar_botao("×")
        self.app.pressionar_botao("7")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "42")

    def test_interacao_divisao(self):
        self.app.pressionar_botao("1")
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("÷")
        self.app.pressionar_botao("2")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "7.5")

    def test_interacao_porcentagem_e_encadeamento(self):
        self.app.pressionar_botao("2")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("+")
        self.app.pressionar_botao("1")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("%")
        self.assertEqual(self.app.obter_visor(), "20")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "220")
        # Operação encadeada sem pressionar '=' antes do próximo operador
        self.app.pressionar_botao("-")
        self.app.pressionar_botao("2")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("×")
        self.assertEqual(self.app.obter_visor(), "200")
        self.app.pressionar_botao("2")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "400")

    # TODO 05: BOTÕES DE CONTROLE
    # Testar C.
    # Testar CE.
    # Testar Backspace.
    # Testar inversão de sinal.
    def test_botoes_de_controle_c_ce_backspace_inversao(self):
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("±")
        self.assertEqual(self.app.obter_visor(), "-5")
        self.app.pressionar_botao("±")
        self.assertEqual(self.app.obter_visor(), "5")

        # Teste de Backspace
        self.app.pressionar_botao("3")
        self.app.pressionar_botao("9")
        self.assertEqual(self.app.obter_visor(), "539")
        self.app.pressionar_botao("⌫")
        self.assertEqual(self.app.obter_visor(), "53")
        self.app.pressionar_botao("⌫")
        self.app.pressionar_botao("⌫")
        self.assertEqual(self.app.obter_visor(), "0")

        # Teste de CE (limpa entrada atual mantendo operação pendente)
        self.app.pressionar_botao("1")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("+")
        self.app.pressionar_botao("9")
        self.app.pressionar_botao("CE")
        self.assertEqual(self.app.obter_visor(), "0")
        self.assertEqual(self.app.obter_historico(), "10 +")
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "15")

        # Teste de C (limpa tudo)
        self.app.pressionar_botao("C")
        self.assertEqual(self.app.obter_visor(), "0")
        self.assertEqual(self.app.obter_historico(), "")

    # TODO 06: TECLADO
    # Testar entrada numérica.
    # Testar operadores.
    # Testar Enter.
    # Testar Backspace.
    # Testar Escape.
    def test_interacao_teclado(self):
        for caractere, simbolo_tecla in [("1", "1"), ("2", "2"), ("+", "plus"), ("8", "8")]:
            self.app.processar_tecla(SimpleNamespace(char=caractere, keysym=simbolo_tecla))
        self.assertEqual(self.app.obter_visor(), "8")
        # Backspace apaga '8' -> '0', depois digita ',5' e pressiona Return (Enter)
        self.app.processar_tecla(SimpleNamespace(char="\x08", keysym="BackSpace"))
        self.assertEqual(self.app.obter_visor(), "0")
        self.app.processar_tecla(SimpleNamespace(char=",", keysym="comma"))
        self.app.processar_tecla(SimpleNamespace(char="5", keysym="5"))
        self.app.processar_tecla(SimpleNamespace(char="\r", keysym="Return"))
        self.assertEqual(self.app.obter_visor(), "12.5")
        # Delete aciona CE, Escape aciona C
        self.app.processar_tecla(SimpleNamespace(char="", keysym="Delete"))
        self.assertEqual(self.app.obter_visor(), "0")
        self.app.processar_tecla(SimpleNamespace(char="\x1b", keysym="Escape"))
        self.assertEqual(self.app.obter_visor(), "0")
        self.assertEqual(self.app.obter_historico(), "")

    # TODO 07: TRATAMENTO DE ERROS
    # Verificar apresentação de erros.
    # Verificar recuperação após uma operação inválida.
    def test_tratamento_de_erros_e_recuperacao(self):
        self.app.pressionar_botao("9")
        self.app.pressionar_botao("÷")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "Erro: Divisão por zero")
        self.assertTrue(self.app.em_erro)
        # Recuperação imediata ao digitar novo número
        self.app.pressionar_botao("7")
        self.assertFalse(self.app.em_erro)
        self.assertEqual(self.app.obter_visor(), "7")
        self.app.pressionar_botao("+")
        self.app.pressionar_botao("3")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "10")

    def test_recuperacao_de_erro_em_encadeamento_e_controles(self):
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("÷")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("+")
        self.assertEqual(self.app.obter_visor(), "Erro: Divisão por zero")
        self.app.pressionar_botao(".")
        self.assertEqual(self.app.obter_visor(), "0.")
        self.assertFalse(self.app.em_erro)

    # TODO 08: REVISÃO
    # Verificar integração entre os módulos.
    # Identificar falhas de comunicação.
    def test_integracao_com_mock_calculadora(self):
        """Verifica o contrato de chamadas entre InterfaceCalculadora e Calculadora via Mock."""
        mock_calc = MagicMock(spec=Calculadora)
        mock_calc.calcular.return_value = 99
        mock_calc.porcentagem.return_value = 15
        mock_calc.inverter_sinal.return_value = -99

        app_simulado = InterfaceCalculadora(root=None, calculadora=mock_calc)
        app_simulado.inserir_digito("4")
        app_simulado.inserir_digito("5")
        app_simulado.selecionar_operador("+")
        app_simulado.inserir_digito("5")
        app_simulado.inserir_digito("4")
        app_simulado.calcular_resultado()

        mock_calc.calcular.assert_called_once_with(45, "+", 54)
        self.assertEqual(app_simulado.obter_visor(), "99")

        app_simulado.inverter_sinal()
        mock_calc.inverter_sinal.assert_called_once_with(99)
        self.assertEqual(app_simulado.obter_visor(), "-99")

        app_simulado.selecionar_operador("*")
        app_simulado.inserir_digito("1")
        app_simulado.inserir_digito("0")
        app_simulado.calcular_porcentagem()
        mock_calc.porcentagem.assert_called_once_with(10, -99, "*")
        self.assertEqual(app_simulado.obter_visor(), "15")

    def test_casos_de_borda_estado_erro_e_teclado(self):
        """Cobre todas as ramificações de proteção de estado de erro, teclado e formatação."""
        # Pressionar '=' sem operador pendente não altera estado
        self.app.pressionar_botao("5")
        self.app.pressionar_botao("=")
        self.assertEqual(self.app.obter_visor(), "5")

        # Retroceder enquanto aguarda novo operando não apaga o visor
        self.app.pressionar_botao("+")
        self.app.pressionar_botao("⌫")
        self.assertEqual(self.app.obter_visor(), "5")

        # Tecla 'c' limpa tudo, tecla desconhecida é ignorada, botão desconhecido é ignorado
        self.app.processar_tecla(SimpleNamespace(char="c", keysym="c"))
        self.assertEqual(self.app.obter_visor(), "0")
        self.app.processar_tecla(SimpleNamespace(char="x", keysym="x"))
        self.app.pressionar_botao("INVALIDO")
        self.assertEqual(self.app.obter_visor(), "0")

        # Operações bloqueadas ou de recuperação durante estado de erro
        self.app.pressionar_botao("8")
        self.app.pressionar_botao("÷")
        self.app.pressionar_botao("0")
        self.app.pressionar_botao("=")
        self.assertTrue(self.app.em_erro)

        # Enquanto em erro, selecionar_operador, calcular_porcentagem e inverter_sinal retornam sem falhar
        self.app.selecionar_operador("+")
        self.app.calcular_porcentagem()
        self.app.inverter_sinal()
        self.assertTrue(self.app.em_erro)

        # '=' em estado de erro recupera limpando tudo
        self.app.calcular_resultado()
        self.assertFalse(self.app.em_erro)
        self.assertEqual(self.app.obter_visor(), "0")

        # CE em estado de erro recupera limpando tudo
        self.app._registrar_erro("Erro")
        self.app.limpar_entrada()
        self.assertFalse(self.app.em_erro)

        # Backspace em estado de erro recupera limpando tudo
        self.app._registrar_erro("Erro")
        self.app.retroceder()
        self.assertFalse(self.app.em_erro)

        # Formatação de float inteiro (ex.: 4.0 -> '4')
        self.assertEqual(self.app._formatar_exibicao(4.0), "4")

        # Tratamento de ValueError genérico vindo da Calculadora
        with patch.object(self.app.calculadora, "calcular", side_effect=ValueError("Operação inválida")):
            self.app.pressionar_botao("2")
            self.app.pressionar_botao("+")
            self.app.pressionar_botao("3")
            self.app.pressionar_botao("=")
            self.assertEqual(self.app.obter_visor(), "Erro")
            self.assertTrue(self.app.em_erro)

    def test_iniciar_aplicacao_com_mock_tk(self):
        """Verifica a função de inicialização principal sem bloquear no mainloop."""
        from main import iniciar_aplicacao
        with patch("main.tk.Tk") as classe_tk_simulada:
            instancia_tk = MagicMock()
            instancia_tk.winfo_screenwidth.return_value = 1920
            instancia_tk.winfo_screenheight.return_value = 1080
            classe_tk_simulada.return_value = instancia_tk
            with patch.object(InterfaceCalculadora, "_construir_interface"):
                app = iniciar_aplicacao()
                instancia_tk.mainloop.assert_called_once()
                self.assertIsInstance(app, InterfaceCalculadora)


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

`

---

### Arquivo Completo: tests/features/calculadora.feature

`gherkin
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

`

---

### Arquivo Completo: tests/test_bdd_calculadora.py

`python
# ============================================================
# TESTES DE ACEITAÇÃO BDD (GHERKIN + PYTEST-BDD)
# ============================================================
# [Termos Técnicos deste Módulo]
# - BDD (Behavior-Driven Development): Desenvolvimento Orientado ao Comportamento; metodologia
#   que descreve o comportamento do software em linguagem natural compreensível por humanos e máquinas.
# - Gherkin: Linguagem estruturada usada em arquivos '.feature' com palavras-chave como
#   Funcionalidade (Feature), Cenário (Scenario), Dado (Given), Quando (When), Então (Then) e E (And).
# - pytest-bdd: Plugin do pytest que conecta cenários Gherkin a funções reais em Python.
# - scenarios(...): Carrega e registra automaticamente todos os cenários do arquivo '.feature'.
# - @pytest.fixture: Define um recurso compartilhado (aqui, a instância da calculadora) injetado nos passos.
# - @given / @when / @then: Decoradores que vinculam os passos 'Dado', 'Quando' e 'Então' do arquivo
#   Gherkin às funções Python correspondentes.
# - parsers.parse(...): Extrai parâmetros entre chaves (como "{numero}" ou "{esperado}") diretamente
#   do texto em português do arquivo '.feature' e os entrega como variáveis para a função Python.
# ============================================================

from pathlib import Path
from types import SimpleNamespace
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from calculadora import Calculadora
from main import InterfaceCalculadora

CAMINHO_FEATURE = Path(__file__).parent / "features" / "calculadora.feature"
scenarios(str(CAMINHO_FEATURE))


@pytest.fixture
def contexto_app():
    """Fixture que fornece uma instância limpa da calculadora para cada cenário de aceitação."""
    return InterfaceCalculadora(root=None, calculadora=Calculadora())


@given("que a calculadora foi inicializada", target_fixture="contexto_app")
def inicializar_calculadora():
    """Passo 'Dado' (Given): garante o estado inicial limpo da calculadora."""
    return InterfaceCalculadora(root=None, calculadora=Calculadora())


@when(parsers.parse('o usuário insere o número "{numero}"'))
def usuario_insere_numero(contexto_app, numero):
    """Passo 'Quando' (When): simula a digitação de cada algarismo ou ponto decimal."""
    for caractere in numero:
        if caractere == ".":
            contexto_app.inserir_decimal()
        else:
            contexto_app.inserir_digito(caractere)


@when(parsers.parse('o usuário seleciona a operação "{operador}"'))
def usuario_seleciona_operacao(contexto_app, operador):
    """Passo 'Quando' (When): aciona o operador matemático selecionado."""
    contexto_app.selecionar_operador(operador)


@when(parsers.parse('o usuário pressiona "{botao}"'))
def usuario_pressiona_botao(contexto_app, botao):
    """Passo 'Quando' (When): simula o clique em um botão de ação (=, %, C, ⌫)."""
    contexto_app.pressionar_botao(botao)


@when(parsers.parse('o usuário digita a sequência de teclas "{sequencia}"'))
def usuario_digita_sequencia_teclas(contexto_app, sequencia):
    """Passo 'Quando' (When): simula o envio de eventos do teclado físico para a interface."""
    mapa_simbolos_tecla = {
        "+": "plus",
        "-": "minus",
        "*": "asterisk",
        "/": "slash",
        "=": "Return",
        ".": "period",
        ",": "comma",
    }
    for tecla in sequencia:
        simbolo = mapa_simbolos_tecla.get(tecla, tecla)
        contexto_app.processar_tecla(SimpleNamespace(char=tecla, keysym=simbolo))


@then(parsers.parse('o visor principal deve exibir "{esperado}"'))
def verificar_visor_principal(contexto_app, esperado):
    """Passo 'Então' (Then): verifica se o visor principal exibe o resultado esperado."""
    assert contexto_app.obter_visor() == esperado


@then('o visor de histórico deve exibir ""')
def verificar_visor_historico_vazio(contexto_app):
    """Passo 'Então' (Then): verifica se o visor superior de histórico está vazio."""
    assert contexto_app.obter_historico() == ""


@then(parsers.parse('o visor de histórico deve exibir "{esperado}"'))
def verificar_visor_historico(contexto_app, esperado):
    """Passo 'Então' (Then): verifica o conteúdo do visor superior de histórico."""
    assert contexto_app.obter_historico() == esperado

`

---

### Arquivo Completo: verificar_qualidade.py

`python
# ============================================================
# MÓDULO: VERIFICAR_QUALIDADE
# RESPONSABILIDADE: AUTOMAÇÃO DE TESTES, COBERTURA, MUTAÇÃO E MÉTRICAS (CRAP / RADON)
# ============================================================
# [Termos Técnicos deste Módulo]
# - ast (Abstract Syntax Tree / Árvore Sintática Abstrata): Módulo nativo do Python que transforma
#   o código-fonte em uma estrutura de árvore manipulável (usado aqui para gerar mutações reais).
# - subprocess: Módulo nativo para executar comandos externos de terminal e capturar suas saídas.
# - radon: Ferramenta de análise estática que mede:
#     * CC (Cyclomatic Complexity / Complexidade Ciclomática): Quantidade de caminhos lógicos independentes
#       em uma função (Notas de A a F, onde A = 1 a 5 indica código simples e de baixo risco).
#     * MI (Maintainability Index / Índice de Manutenibilidade): Pontuação de 0 a 100 que avalia
#       quão fácil é manter o código (Nota A = alta manutenibilidade).
#     * Raw (Métricas Brutas): LOC (Total de Linhas), LLOC (Linhas Lógicas) e SLOC (Linhas de Código sem comentários).
# - CRAP (Change Risk Anti-Patterns): Métrica criada por Alberto Savoia e Bob Evans (difundida por
#   Robert C. Martin / Uncle Bob) que combina Complexidade Ciclomática (CC) e Cobertura de Testes (cov):
#   CRAP(m) = CC^2 * (1 - cov/100)^3 + CC. Valores <= 12 indicam código seguro para manutenção.
# - coverage.py: Ferramenta que mede quais linhas (Statements) e desvios condicionais (Branches / Ramificações)
#   foram efetivamente executados pelos testes.
# - Teste de Mutação (Mutation Testing): Técnica que introduz pequenos defeitos artificiais (mutantes)
#   no código (ex.: trocar '+' por '-') para provar que os testes detectam o erro:
#     * KILLED (Eliminado): O teste falhou ao rodar com o código mutado (comportamento desejado: o teste detectou o defeito).
#     * SURVIVED (Sobrevivente): O teste passou mesmo com o código adulterado (indica fragilidade nos testes).
# ============================================================

import ast
import json
import subprocess
import sys
from pathlib import Path
from radon.complexity import cc_visit, cc_rank

RAIZ_PROJETO = Path(__file__).parent.resolve()


def executar_comando(comando, descricao):
    """
    Executa um comando em subprocesso e retorna (codigo_saida, saida_padrao, saida_erro).
    - stdout (Standard Output): Saída padrão de texto do comando.
    - stderr (Standard Error): Saída de mensagens de erro do comando.
    - returncode: Código numérico de encerramento (0 significa sucesso sem erros).
    """
    print(f"\n{'=' * 70}")
    print(f"[EXECUÇÃO] {descricao}")
    print(f"Comando: {' '.join(comando)}")
    print("=" * 70)
    resultado = subprocess.run(
        comando,
        cwd=str(RAIZ_PROJETO),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if resultado.stdout:
        print(resultado.stdout.strip())
    if resultado.stderr:
        print(resultado.stderr.strip())
    return resultado.returncode, resultado.stdout, resultado.stderr


def calcular_metricas_crap(arquivos_alvo, caminho_coverage_json):
    """Calcula a Complexidade Ciclomática (Radon CC) e a pontuação CRAP por função/método."""
    dados_cobertura = json.loads(Path(caminho_coverage_json).read_text(encoding="utf-8"))
    arquivos_cobertos = dados_cobertura.get("files", {})

    relatorio_crap = []
    for arquivo in arquivos_alvo:
        caminho_arq = RAIZ_PROJETO / arquivo
        codigo = caminho_arq.read_text(encoding="utf-8")
        blocos = cc_visit(codigo)

        info_cov = arquivos_cobertos.get(arquivo) or arquivos_cobertos.get(str(caminho_arq)) or {}
        linhas_executadas = set(info_cov.get("executed_lines", []))
        linhas_ausentes = set(info_cov.get("missing_lines", []))

        for bloco in blocos:
            # Ignorar o bloco agregador da classe e avaliar individualmente cada método/função
            if hasattr(bloco, "methods"):
                continue
            linhas_bloco = set(range(bloco.lineno, bloco.endline + 1))
            executadas_no_bloco = len(linhas_bloco & linhas_executadas)
            ausentes_no_bloco = len(linhas_bloco & linhas_ausentes)
            total_rastreado = executadas_no_bloco + ausentes_no_bloco
            cobertura_pct = (
                (executadas_no_bloco / total_rastreado) * 100.0 if total_rastreado > 0 else 100.0
            )
            complexidade = bloco.complexity
            pontuacao_crap = (complexidade ** 2) * ((1.0 - (cobertura_pct / 100.0)) ** 3) + complexidade
            nome_qualificado = (
                f"{bloco.classname}.{bloco.name}" if getattr(bloco, "classname", None) else bloco.name
            )
            relatorio_crap.append(
                {
                    "arquivo": arquivo,
                    "funcao": nome_qualificado,
                    "linhas": f"{bloco.lineno}-{bloco.endline}",
                    "complexidade": complexidade,
                    "rank_cc": cc_rank(complexidade),
                    "cobertura_pct": round(cobertura_pct, 2),
                    "crap": round(pontuacao_crap, 2),
                    "aprovado_crap": pontuacao_crap <= 12.0,
                }
            )
    return relatorio_crap


def gerar_mutantes_ast(codigo_fonte):
    """
    Gera mutantes sistemáticos sobre a Árvore Sintática Abstrata (AST) de calculadora.py nas 5 categorias:
    1. Substituição de operadores aritméticos (+ <-> -, * <-> /, -unário -> +unário)
    2. Alteração de operadores relacionais/identidade/pertinência (== <-> !=, is <-> is not, in <-> not in)
    3. Modificação de constantes numéricas (0 -> 1, 100 -> 101)
    4. Alteração de condições booleanas (or <-> and, remoção de not)
    5. Modificação de retornos (return expressao -> return None)
    """
    arvore_base = ast.parse(codigo_fonte)
    mutantes = []

    trocas_binop = {
        ast.Add: (ast.Sub, "+ -> -"),
        ast.Sub: (ast.Add, "- -> +"),
        ast.Mult: (ast.Div, "* -> /"),
        ast.Div: (ast.Mult, "/ -> *"),
    }
    trocas_comparacao = {
        ast.Eq: (ast.NotEq, "== -> !="),
        ast.NotEq: (ast.Eq, "!= -> =="),
        ast.Is: (ast.IsNot, "is -> is not"),
        ast.IsNot: (ast.Is, "is not -> is"),
        ast.In: (ast.NotIn, "in -> not in"),
        ast.NotIn: (ast.In, "not in -> in"),
    }
    trocas_booleanas = {
        ast.Or: (ast.And, "or -> and"),
        ast.And: (ast.Or, "and -> or"),
    }

    nos_base = list(ast.walk(arvore_base))
    for indice_no, no in enumerate(nos_base):
        # 1a. Operadores aritméticos binários (BinOp)
        if isinstance(no, ast.BinOp) and type(no.op) in trocas_binop:
            nova_classe_op, descricao = trocas_binop[type(no.op)]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = nova_classe_op()
            mutantes.append((no.lineno, "Operador Aritmético", descricao, ast.unparse(copia)))

        # 1b. Operador unário de inversão de sinal (UnaryOp USub -> UAdd)
        elif isinstance(no, ast.UnaryOp) and isinstance(no.op, ast.USub):
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = ast.UAdd()
            mutantes.append((no.lineno, "Operador Unário", "-x -> +x", ast.unparse(copia)))

        # 2. Operadores relacionais, identidade e pertinência (Compare)
        elif isinstance(no, ast.Compare) and len(no.ops) == 1 and type(no.ops[0]) in trocas_comparacao:
            nova_classe_cmp, descricao = trocas_comparacao[type(no.ops[0])]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.ops[0] = nova_classe_cmp()
            mutantes.append((no.lineno, "Operador Relacional", descricao, ast.unparse(copia)))

        # 3. Modificação de constantes numéricas (Constant: 0 -> 1, 100 -> 101)
        elif isinstance(no, ast.Constant) and type(no.value) is int and no.value in (0, 100):
            novo_valor = no.value + 1
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.value = novo_valor
            mutantes.append(
                (no.lineno, "Constante Numérica", f"{no.value} -> {novo_valor}", ast.unparse(copia))
            )

        # 4a. Condições booleanas (BoolOp: or <-> and)
        elif isinstance(no, ast.BoolOp) and type(no.op) in trocas_booleanas:
            nova_classe_bool, descricao = trocas_booleanas[type(no.op)]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = nova_classe_bool()
            mutantes.append((no.lineno, "Condição Booleana", descricao, ast.unparse(copia)))

        # 4b. Negação booleana (not expressao -> expressao)
        elif isinstance(no, ast.UnaryOp) and isinstance(no.op, ast.Not):
            copia = ast.parse(codigo_fonte)
            for pai in ast.walk(copia):
                for campo, valor_campo in ast.iter_fields(pai):
                    if (
                        isinstance(valor_campo, ast.UnaryOp)
                        and isinstance(valor_campo.op, ast.Not)
                        and valor_campo.lineno == no.lineno
                    ):
                        setattr(pai, campo, valor_campo.operand)
                        mutantes.append(
                            (no.lineno, "Condição Booleana", "not expr -> expr", ast.unparse(copia))
                        )
                        break

        # 5. Modificação de retornos (Return: return expressao -> return None)
        elif isinstance(no, ast.Return) and no.value is not None:
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.value = ast.Constant(value=None)
            mutantes.append(
                (no.lineno, "Modificação de Retorno", "return expr -> return None", ast.unparse(copia))
            )

    return mutantes


def executar_testes_mutacao():
    """Executa a bateria de testes de mutação sobre calculadora.py e restaura o código original."""
    caminho_calc = RAIZ_PROJETO / "calculadora.py"
    codigo_original = caminho_calc.read_text(encoding="utf-8")
    mutantes = gerar_mutantes_ast(codigo_original)

    resultados = []
    eliminados = 0
    sobreviventes = 0

    print(f"\n{'=' * 70}")
    print(f"[MUTAÇÃO] Executando {len(mutantes)} mutações sobre calculadora.py...")
    print("=" * 70)

    try:
        for indice, (linha, categoria, descricao, codigo_mutado) in enumerate(mutantes, start=1):
            caminho_calc.write_text(codigo_mutado, encoding="utf-8")
            processo = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/test_calculadora.py", "-q", "--tb=no"],
                cwd=str(RAIZ_PROJETO),
                capture_output=True,
                text=True,
            )
            morto = processo.returncode != 0
            status = "ELIMINADO (KILLED)" if morto else "SOBREVIVENTE (SURVIVED)"
            if morto:
                eliminados += 1
            else:
                sobreviventes += 1
            print(f"  Mutante #{indice:02d} | Linha {linha:03d} | {categoria:<22} | {descricao:<26} -> {status}")
            resultados.append(
                {
                    "id": indice,
                    "linha": linha,
                    "categoria": categoria,
                    "descricao": descricao,
                    "status": status,
                    "eliminado": morto,
                }
            )
    finally:
        caminho_calc.write_text(codigo_original, encoding="utf-8")

    total = len(mutantes)
    taxa = (eliminados / total * 100.0) if total > 0 else 100.0
    print("-" * 70)
    print(
        f"Resumo de Mutação: Total={total} | Eliminados={eliminados} | "
        f"Sobreviventes={sobreviventes} | Taxa de Mutação={taxa:.2f}%"
    )
    return {
        "total": total,
        "eliminados": eliminados,
        "sobreviventes": sobreviventes,
        "taxa_mutacao_pct": round(taxa, 2),
        "mutantes": resultados,
    }


def main():
    # 1. Testes Unitários (unittest + pytest)
    cod_unitario_ut, _, _ = executar_comando(
        [sys.executable, "-m", "unittest", "tests/test_calculadora.py", "-v"],
        "1A. Testes Unitários (unittest)",
    )
    cod_unitario_pt, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_calculadora.py", "-v"],
        "1B. Testes Unitários Parametrizados (pytest)",
    )

    # 2. Testes de Aceitação (BDD / Gherkin)
    cod_bdd, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_bdd_calculadora.py", "-v"],
        "2. Testes de Aceitação BDD (Gherkin / pytest-bdd)",
    )

    # 3. Testes de Integração
    cod_integracao, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_interface.py", "-v"],
        "3. Testes de Integração (main.py <-> calculadora.py)",
    )

    # 4. Cobertura de Linhas e Ramificações (Coverage)
    executar_comando(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "--branch",
            "--source=calculadora,main",
            "-m",
            "pytest",
        ],
        "4A. Execução da Suíte Completa com Coverage (Linhas e Ramificações)",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "report", "-m"],
        "4B. Relatório Textual de Cobertura",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "html"],
        "4C. Geração de Relatório HTML de Cobertura (htmlcov/)",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "json"],
        "4D. Exportação JSON de Cobertura (coverage.json)",
    )

    # 5. Análise de Complexidade (Radon) e Métrica CRAP
    executar_comando(
        [sys.executable, "-m", "radon", "cc", "calculadora.py", "main.py", "-s", "-a"],
        "5A. Complexidade Ciclomática (Radon CC)",
    )
    executar_comando(
        [sys.executable, "-m", "radon", "mi", "calculadora.py", "main.py", "-s"],
        "5B. Índice de Manutenibilidade (Radon MI)",
    )
    executar_comando(
        [sys.executable, "-m", "radon", "raw", "calculadora.py", "main.py", "-s"],
        "5C. Métricas Brutas de Tamanho de Código (Radon Raw)",
    )

    relatorio_crap = calcular_metricas_crap(
        ["calculadora.py", "main.py"], RAIZ_PROJETO / "coverage.json"
    )
    print(f"\n{'=' * 70}")
    print("[MÉTRICA CRAP] Relatório por Função/Método (Referência: CRAP <= 12)")
    print("=" * 70)
    print(f"{'Arquivo':<16} | {'Função/Método':<36} | {'CC':>3} | {'Cob(%)':>7} | {'CRAP':>6} | {'Status'}")
    print("-" * 85)
    for item in relatorio_crap:
        status_str = "OK (<=12)" if item["aprovado_crap"] else "ACIMA (>12)"
        print(
            f"{item['arquivo']:<16} | {item['funcao']:<36} | {item['complexidade']:>3} | "
            f"{item['cobertura_pct']:>6.1f}% | {item['crap']:>6.2f} | {status_str}"
        )

    # 6. Testes de Mutação
    resumo_mutacao = executar_testes_mutacao()

    # Salvar resumo consolidado em JSON
    resumo_geral = {
        "crap": relatorio_crap,
        "mutacao": resumo_mutacao,
    }
    (RAIZ_PROJETO / "relatorio_metricas.json").write_text(
        json.dumps(resumo_geral, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    falhas = any(
        codigo != 0 for codigo in (cod_unitario_ut, cod_unitario_pt, cod_bdd, cod_integracao)
    ) or (resumo_mutacao["sobreviventes"] > 0)
    return 1 if falhas else 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())

`

---

### Arquivo Completo: tests/roteiro_testes.md

`markdown
# ROTEIRO DE TESTES — CALCULADORA

## 1. Objetivo
Verificar o funcionamento da calculadora
e sua conformidade com os requisitos.

## 2. Testes funcionais

| ID | Funcionalidade | Entrada | Resultado esperado | Status |
|---|---|---|---|---|
| CT01 | Adição | 10 + 5 | 15 | Aprovado (Automatizado) |
| CT02 | Subtração | 10 - 5 | 5 | Aprovado (Automatizado) |
| CT03 | Multiplicação | 10 * 5 | 50 | Aprovado (Automatizado) |
| CT04 | Divisão | 10 / 5 | 2 | Aprovado (Automatizado) |
| CT05 | Divisão por zero | 10 / 0 | Erro tratado (`Erro: Divisão por zero`) | Aprovado (Automatizado) |
| CT06 | Decimal | 2.5 + 2.5 | 5 | Aprovado (Automatizado) |
| CT07 | Porcentagem | 200 + 10% = | 220 | Aprovado (Automatizado) |
| CT08 | Inversão de sinal | 5 -> ± | -5 | Aprovado (Automatizado) |
| CT09 | Limpeza | C | Visor zerado (`0`) | Aprovado (Automatizado) |
| CT10 | Retrocesso | 123 -> ⌫ | 12 | Aprovado (Automatizado) |

## 3. Testes de interface
- Verificar disposição dos botões.
- Verificar legibilidade dos números.
- Verificar contraste das cores.
- Verificar atualização do visor.
- Verificar redimensionamento.

## 4. Testes de usabilidade
- Verificar facilidade de utilização.
- Verificar consistência dos botões.
- Verificar feedback das operações.
- Verificar comportamento pelo teclado.

## 5. Registro de resultados
- **Testes automatizados (Unitários, Integração e BDD):** 100% aprovados via `pytest` e `unittest`.
- **Problemas identificados durante o ciclo TDD:**
  - Necessidade de evitar imprecisão de ponto flutuante IEEE 754 (ex.: `0.1 + 0.2`) -> Corrigido utilizando aritmética `Decimal` internamente em `calculadora.py`.
  - Necessidade de rejeitar valores booleanos (`True`/`False`), que em Python herdam de `int` -> Corrigido com verificação explícita `isinstance(valor, bool)` em `validar_numero`.
- **Testes manuais de UI/UX:** Documentados em detalhes em `tests/qa/roteiro_manual.md`.

## 6. Critério de aprovação
Todas as funcionalidades obrigatórias devem
funcionar conforme os requisitos definidos.

`

---

### Arquivo Completo: tests/qa/roteiro_manual.md

`markdown
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

`


---

## Parte 3 — Glossário e Arquitetura do Sistema de Educação, Proctoring Simulado, Certificação SHA-256 e Executáveis Windows

### 3.1. Termos Técnicos de Proctoring, Criptografia e Empacotamento Windows

| Termo Técnico | Significado e Função no Projeto |
|---|---|
| `Proctoring` | Sistema de supervisão e auditoria automatizada de integridade de exames (monitoramento de presença na webcam, ruído de voz no microfone e foco de janela do sistema operacional). |
| `Hardware Mock` | Simulador determinístico de sensores físicos (`SensorWebcamMock`, `SensorAudioMock`, `SensorJanelaMock` em `src/proctoring.py`) que permite testar todas as regras de infração sem exigir câmera ou microfone reais conectados. |
| `@dataclass(frozen=True)` | Decorador da biblioteca padrão `dataclasses` que cria classes de dados **imutáveis** (`frozen=True`): qualquer tentativa de alterar um atributo após a criação lança erro, garantindo integridade de logs de auditoria (`RegistroInfracao`). |
| `SHA-256` (*Secure Hash Algorithm 256-bit*) | Função criptográfica unidirecional da família SHA-2 (NIST FIPS 180-4) que transforma qualquer volume de bytes em uma impressão digital única de 256 bits (64 caracteres hexadecimais). |
| `Avalanche Effect` (Efeito Avalanche) | Propriedade matemática do `SHA-256` pela qual a alteração de 1 único bit ou caractere na entrada muda cerca de 50% de todos os bits do hash resultante, tornando qualquer adulteração imediatamente visível. |
| `HMAC-SHA256` (*Hash-based Message Authentication Code*) | Código de autenticação de mensagem baseado em hash (`RFC 2104`) que combina o payload do certificado com uma chave secreta do emissor (`segredo_emissor`) para impedir que terceiros forjem certificados. |
| `hmac.compare_digest(a, b)` | Função de comparação criptográfica em **tempo constante** (*Constant-Time Comparison*) que evita ataques de temporização (*Timing Attacks*). |
| `Canonical JSON` (JSON Canônico) | Serialização determinística (`json.dumps(..., sort_keys=True, separators=(",", ":"))`) que garante que o mesmo dicionário gere exatamente a mesma sequência de bytes em qualquer computador. |
| `ttk.Notebook` | Componente de abas (*Tabs*) do Tkinter usado em `app_educacao.py` para organizar a plataforma em 3 áreas: Curso Carrasco (`docs/`), Simulador de Proctoring + Exame SHA-256 e Laboratório da Calculadora. |
| `ScrolledText` (`tkinter.scrolledtext`) | Caixa de texto multilinha com barra de rolagem vertical integrada usada para exibir os 6 módulos Markdown do curso e os relatórios de auditoria. |
| `PyInstaller` | Ferramenta que empacota scripts Python, o interpretador Python 3.12, bibliotecas (`tkinter`, `decimal`, `hashlib`, `hmac`) e arquivos de dados (`docs/*.md`, `calculadora.ico`) em um único executável nativo do Windows (`.exe`). |
| `--onefile` / `--windowed` | Flags do `PyInstaller`: `--onefile` gera um único arquivo `.exe` autossuficiente; `--windowed` (ou `--noconsole`) oculta a janela preta do terminal ao abrir a interface gráfica. |
| `--add-data "docs;docs"` | Instrução do `PyInstaller` que embute toda a pasta `docs/` (com os 6 módulos do curso) dentro do executável `Sistema Educacao Calculadora.exe`. |
| `sys._MEIPASS` | Atributo especial criado em tempo de execução pelo bootloader do `PyInstaller` contendo o caminho da pasta temporária onde os recursos embutidos (`docs/`) foram extraídos. |
| `winreg` | Módulo nativo do Python para leitura e escrita no Registro do Windows (`HKCU\Software\Microsoft\Windows\CurrentVersion\Uninstall`), usado por `instalar_sistema_windows.py` para registrar os aplicativos em *Aplicativos Instalados*. |
| `WScript.Shell` / `.lnk` | Componente COM nativo do Windows Script Host utilizado pelo instalador `instalar_sistema_windows.py` para criar atalhos oficiais `.lnk` no Menu Iniciar e na Área de Trabalho. |

---

### 3.2. Resumo dos Novos Módulos e Executáveis

1. **`src/proctoring.py`**: Implementa `SensorWebcamMock`, `SensorAudioMock`, `SensorJanelaMock`, `RegistroInfracao` e `SessaoProctoring`.
2. **`src/certificador_sha256.py`**: Implementa `CertificadorSHA256` e `ErroCertificacaoReprovada`.
3. **`src/avaliador_carrasco.py`**: Implementa `AvaliadorCarrasco`, executando 5 baterias de verificação sobre `Calculadora` e integrando o resultado ao Proctoring e ao Certificador SHA-256.
4. **`verify_certificate.py`**: Utilitário CLI de validação pública de certificados (`certificado_oficial_sha256.json`).
5. **`app_educacao.py` e `Sistema Educacao Calculadora.exe`**: Interface gráfica completa do Sistema de Educação e Certificação empacotada para Windows.
6. **`instalar_sistema_windows.py`**: Instalador automatizado dos dois executáveis (`Calculadora Python.exe` e `Sistema Educacao Calculadora.exe`) no computador Windows do usuário.
7. **`docs/MODULO_01` a `docs/MODULO_06`**: Seis módulos didáticos aprofundados no estilo Carrasco cobrindo Clean Code, Tratamento de Exceções, TDD/Mutação, Proctoring, Criptografia SHA-256 e Build/Deploy de Executáveis Windows.
