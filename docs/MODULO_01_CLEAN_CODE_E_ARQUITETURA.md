# Módulo 01 — Clean Code e Arquitetura Limpa na Prática (Padrão Carrasco)

> *"O único modo de andar rápido é andar bem. Cada vez que você cede à tentação de escrever código sujo para 'ganhar tempo', você atrasa todo o projeto."* — **Robert C. Martin (Uncle Bob)**

Bem-vindo ao **Módulo 01** do Sistema de Educação e Certificação em Engenharia de Software com Python. Aqui não aceitamos código que "apenas funciona". Se o seu código calcula `2 + 2 = 4`, mas mistura interface gráfica com regra de negócio, possui funções com complexidade ciclomática alta ou sofre de imprecisão de ponto flutuante em `0.1 + 0.2`, **você está reprovado**.

---

## 1. O Pecado Capital do Iniciante: Acoplamento entre UI e Domínio

O erro mais comum ao construir uma calculadora gráfica em Python é colocar a matemática dentro dos botões do `Tkinter`:

```python
# ❌ CÓDIGO REPROVADO (Acoplado, Intestável e Frágil)
def clicar_igual():
    expressao = entrada_tk.get()
    resultado = eval(expressao)  # Falha grave de segurança + acoplamento com Tkinter + float impreciso!
    entrada_tk.delete(0, "end")
    entrada_tk.insert(0, str(resultado))
```

### Por que esse código é inaceitável?
1. **Impossível de testar sem abrir janelas:** A regra matemática está presa a `entrada_tk.get()`.
2. **Uso de `eval()`:** Permite execução arbitrária de código (*Code Injection*) e não permite controlar regras de negócio contextuais (como a porcentagem estilo Windows).
3. **Violação do SRP (*Single Responsibility Principle*):** A mesma função lê da tela, calcula a matemática e formata a saída visual.

### A Solução Arquitetural: Isolamento Total de Camadas
No nosso projeto de referência:
- **`calculadora.py` (Camada de Domínio / Regras de Negócio):** Não sabe que o `Tkinter` existe. Não importa bibliotecas visuais. Recebe números, valida tipos, executa aritmética exata com `Decimal` e retorna números ou lança exceções semânticas.
- **`main.py` (Camada de Apresentação e Estado de UI):** Gerencia eventos de clique, atalhos de teclado e `StringVar`, delegando 100% da matemática para a instância de `Calculadora`.

---

## 2. O Problema Oculto do `float` Binário (Norma IEEE 754)

Abra um terminal Python agora e digite:

```python
>>> 0.1 + 0.2 == 0.3
False
>>> 0.1 + 0.2
0.30000000000000004
```

### Por que isso acontece?
Os processadores representam números `float` em **base 2 (binária)** seguindo a norma **IEEE 754**. Assim como a fração $\frac{1}{3}$ em base 10 gera uma dízima periódica infinita ($0,33333...$), a fração $\frac{1}{10}$ ($0,1$) em base 2 é uma dízima periódica binária infinita ($0,0001100110011..._2$). Ao truncar em 53 bits de mantissa, surge um resíduo binário inevitável.

### Como um Engenheiro Sênior Resolve
Utilizamos o módulo nativo `decimal.Decimal`, que opera em **base 10 exata**, convertendo o número validado a partir de sua representação textual (`Decimal(str(valor))`):

```python
from decimal import Decimal

class Calculadora:
    def _formatar_resultado(self, valor_decimal: Decimal) -> int | float:
        """Retorna int quando o resultado é inteiro exato e float quando possui fração."""
        if valor_decimal == valor_decimal.to_integral_value():
            return int(valor_decimal)
        return float(valor_decimal)

    def somar(self, a: int | float, b: int | float) -> int | float:
        dec_a = self.validar_numero(a)
        dec_b = self.validar_numero(b)
        return self._formatar_resultado(dec_a + dec_b)
```

Observe a elegância de `_formatar_resultado`:
- `somar(0.1, 0.2)` calcula `Decimal('0.1') + Decimal('0.2') = Decimal('0.3')`, cujo `float(Decimal('0.3'))` é exatamente `0.3`.
- `somar(2.5, 2.5)` calcula `Decimal('5.0')`, detecta que é igual a `to_integral_value()` (`Decimal('5')`) e devolve o `int` `5` (evitando exibir `5.0` no visor).

---

## 3. Eliminando `if/elif` em Cascata com *Dispatch Tables* (Tabelas de Despacho)

Compare as duas implementações abaixo para despachar uma operação matemática:

```python
# ❌ COMPLEXIDADE CICLOMÁTICA ALTA (Cresce a cada novo operador)
def calcular_ruim(self, a, operador, b):
    if operador == "+":
        return self.somar(a, b)
    elif operador == "-":
        return self.subtrair(a, b)
    elif operador == "*":
        return self.multiplicar(a, b)
    elif operador == "/":
        return self.dividir(a, b)
    else:
        raise ValueError(f"Operador inválido: {operador}")
```

```python
# ✅ CLEAN CODE COM TABELA DE DESPACHO (Complexidade Ciclomática = 2, Nota A no Radon)
def calcular(self, a, operador, b):
    operacoes = {
        "+": self.somar,
        "-": self.subtrair,
        "*": self.multiplicar,
        "/": self.dividir,
    }
    if operador not in operacoes:
        raise ValueError(f"Operador inválido: {operador}")
    return operacoes[operador](a, b)
```

Com um dicionário de funções de primeira classe (`operacoes`), a **Complexidade Ciclomática (CC)** cai para apenas **2** (um único `if`), mantendo o código aberto para extensão e simples de testar.

---

## 4. Critérios "Carrasco" de Aprovação deste Módulo

Para avançar ao Módulo 02 no exame prático, seu código será submetido ao avaliador automatizado e **reprovará imediatamente** se:
1. Houver qualquer `import tkinter` dentro do módulo de domínio matemático;
2. Qualquer método tiver Complexidade Ciclomática $\text{CC} > 5$ (Nota inferior a `A` no `radon cc`);
3. `somar(0.1, 0.2) == 0.3` retornar `False`;
4. `somar(2.5, 2.5)` retornar texto ou `float` com `.0` residual quando deveria normalizar inteiros exatos.
