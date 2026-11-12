# Módulo 03 — TDD Implacável, `pytest`, Cobertura de Branches e Testes de Mutação

> *"Se você não testa as mutações do seu código, quem garante quem está testando os seus testes?"*

Neste módulo saímos do básico de "escrever um teste que passa" para entrar na **Engenharia de Qualidade Avançada**: TDD estrito, parametrização com `pytest`, cobertura de ramificações (*Branch Coverage*), Testes de Mutação via AST e a métrica **CRAP**.

---

## 1. As Três Leis do TDD (Robert C. Martin)

1. **Primeira Lei:** Você não tem permissão para escrever código de produção a menos que seja para fazer um teste unitário que está falhando passar.
2. **Segunda Lei:** Você não tem permissão para escrever mais de um teste unitário do que o suficiente para falhar (e erros de compilação/importação contam como falha).
3. **Terceira Lei:** Você não tem permissão para escrever mais código de produção do que o suficiente para fazer o único teste que está falhando passar.

Isso gera o ciclo de segundos **Red → Green → Refactor**:
- **RED:** O teste é executado contra um *stub* e falha pelo motivo certo.
- **GREEN:** A regra de negócio é implementada até o teste ficar verde.
- **REFACTOR:** Duplicações são removidas e nomes são lapidados sem quebrar nenhum teste.

---

## 2. Parametrização Massiva com `@pytest.mark.parametrize`

Em vez de escrever 8 funções quase idênticas para testar soma de positivos, negativos, zeros e decimais, usamos `@pytest.mark.parametrize`:

```python
import pytest
from calculadora import Calculadora

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
```

Cada tupla gera um caso de teste independente no relatório do `pytest`, permitindo identificar instantaneamente qual combinação de valores falhou.

---

## 3. Cobertura de Linhas vs. Cobertura de Ramificações (*Branch Coverage*)

Medir apenas cobertura de linhas (`coverage run -m pytest`) é perigoso. Considere:
```python
if base is None or operacao in ("*", "/"):
    return self._formatar_resultado(fator)
```
Se você testar apenas com `base=None`, a linha foi executada (100% *Line Coverage*), mas a segunda metade da condição (`operacao in ("*", "/")` quando `base` não é `None`) **nunca foi exercitada**!
Por isso exigimos `coverage run --branch`, que verifica se todas as decisões lógicas assumiram tanto `True` quanto `False` (`0` *partial branches*).

---

## 4. Testes de Mutação: O Teste de Fogo dos Seus Testes

Mesmo com 100% de cobertura de linhas e *branches*, um teste sem `assert` adequado é inútil. O **Teste de Mutação** modifica a Árvore Sintática Abstrata (`AST`) do seu código criando **mutantes** (defeitos artificiais):

| Categoria de Mutação | Exemplo no Código Original | Mutante Gerado | O que deve acontecer? |
|---|---|---|---|
| **Operador Aritmético** | `dec_a + dec_b` | `dec_a - dec_b` | Teste falha → **ELIMINADO (`KILLED`)** |
| **Operador Relacional** | `if dec_b == 0:` | `if dec_b != 0:` | Teste falha → **ELIMINADO (`KILLED`)** |
| **Constante Numérica** | `Decimal(100)` | `Decimal(101)` | Teste falha → **ELIMINADO (`KILLED`)** |
| **Condição Booleana** | `if a or b:` | `if a and b:` | Teste falha → **ELIMINADO (`KILLED`)** |
| **Modificação de Retorno** | `return resultado` | `return None` | Teste falha → **ELIMINADO (`KILLED`)** |

Se você escolher valores ruins nos testes — por exemplo, testar multiplicação apenas com `calc.multiplicar(2, 2) == 4` ou `calc.somar(0, 0) == 0` — quando o mutante trocar `*` por `+` (`2 + 2 == 4`) ou `+` por `-` (`0 - 0 == 0`), **o mutante sobreviverá (`SURVIVED`)**!
Por isso escolhemos pares assimétricos como `(10, 5)`, onde:
- $10 + 5 = 15$
- $10 - 5 = 5$
- $10 \times 5 = 50$
- $10 \div 5 = 2$

---

## 5. A Métrica CRAP (*Change Risk Anti-Patterns*)

A pontuação **CRAP** combina a Complexidade Ciclomática $\text{comp}(m)$ de um método com sua cobertura de testes $\text{cov}(m)$:

$$\text{CRAP}(m) = \text{comp}(m)^2 \times \left(1 - \frac{\text{cov}(m)}{100}\right)^3 + \text{comp}(m)$$

- Se uma função tem $\text{comp}(m) = 10$ e $0\%$ de cobertura: $\text{CRAP} = 10^2 \times 1 + 10 = 110$ (**Altíssimo risco!**).
- Se uma função tem $\text{comp}(m) = 4$ e $100\%$ de cobertura: $\text{CRAP} = 4^2 \times 0 + 4 = 4.00$ (**Código limpo e seguro, $\le 12$**).
