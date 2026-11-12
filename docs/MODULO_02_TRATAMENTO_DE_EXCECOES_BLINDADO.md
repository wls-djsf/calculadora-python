# Módulo 02 — Engenharia Defensiva e `try/except` de Nível Produção

> *"Tratamento de erros é importante, mas se ele obscurece a lógica do código, está errado."* — **Robert C. Martin (Clean Code, Capítulo 7)**

Neste módulo você aprenderá por que 90% dos estudantes usam `try/except` da forma errada em Python e como blindar sua calculadora contra as armadilhas mais traiçoeiras da linguagem.

---

## 1. As Três Armadilhas de Tipos em Python que Derrubam Sistemas

Se alguém pedir para você validar se uma entrada `valor` é um número em Python, sua primeira reação provavelmente será escrever:

```python
# ❌ VALIDAÇÃO INGÊNUA (Falha em 3 cenários críticos!)
def validar_ingenuo(valor):
    if not isinstance(valor, (int, float)):
        raise ValueError("Não é número!")
```

Por que essa função **reprova** nos nossos testes de qualidade?

### Armadilha #1: Em Python, `bool` é subclasse de `int`!
Por razões históricas (PEP 285), a classe `bool` herda diretamente de `int`:
```python
>>> isinstance(True, int)
True
>>> isinstance(False, (int, float))
True
>>> True + True
2
```
Com a validação ingênua acima, `calc.somar(True, 5)` retorna `6` em vez de lançar erro!

### Armadilha #2: `float("nan")` (Not a Number) é um `float`!
```python
>>> nan = float("nan")
>>> isinstance(nan, float)
True
>>> nan == nan
False
```
Se `float("nan")` passar pela validação, `Decimal(str(nan))` criará `Decimal('NaN')` e corromperá ou quebrará todas as comparações subsequentes.

### Armadilha #3: `float("inf")` e `float("-inf")` também são `float`!
Infinitos positivos e negativos passam em `isinstance(valor, float)`, mas não são números reais finitos operáveis em uma calculadora comercial.

---

## 2. A Validação Blindada (Padrão Sênior)

Veja como `validar_numero` em `calculadora.py` neutraliza todas as três armadilhas em apenas 4 linhas de lógica e Complexidade Ciclomática `4`:

```python
import math
from decimal import Decimal

class ErroEntradaInvalida(ValueError, TypeError):
    """Herda de ValueError e TypeError para compatibilidade total de contrato."""

def validar_numero(self, valor):
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErroEntradaInvalida("Entrada inválida: o valor deve ser numérico.")
    if not math.isfinite(valor):
        raise ErroEntradaInvalida("Entrada inválida: o valor deve ser finito.")
    return Decimal(str(valor))
```

### Por que `class ErroEntradaInvalida(ValueError, TypeError)`?
Em Python, algumas suítes de testes esperam `TypeError` quando um tipo errado (`"abc"`, `None`, `True`) é passado, enquanto outras esperam `ValueError` para valores inválidos (`float("nan")`). Ao criar uma exceção de domínio que herda de `(ValueError, TypeError)`, tanto `except ValueError:` quanto `except TypeError:` capturam o erro de forma limpa e polimórfica!

---

## 3. O Crime do `except:` Vazio (*Bare Except*) vs. Tratamento Semântico na UI

Nunca escreva `except:` genérico sem especificar as classes de exceção:
- Um `except:` vazio captura até `KeyboardInterrupt` (`Ctrl+C`) e `SystemExit`, impedindo o encerramento do processo e mascarando *bugs* de digitação (`NameError`, `AttributeError`).

Em `main.py`, a camada de interface trata exclusivamente as exceções matemáticas esperadas da camada de domínio e diferencia a mensagem exibida ao usuário:

```python
def _executar_operacao_pendente(self):
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
```

### Recuperação de Estado Pós-Erro
Uma calculadora profissional não pode obrigar o usuário a fechar e abrir o programa após dividir por zero (`10 / 0 =`). O método `_registrar_erro` ativa a *flag* `self.em_erro = True`, e no instante em que o usuário digita qualquer novo número (`inserir_digito`) ou pressiona `C`, `CE`, `⌫` ou `=`, o estado é limpo automaticamente e a calculadora volta a operar normalmente.

---

## 4. Desafio Carrasco #02 (Checklist de Sobrevivência)

1. Teste sua função de soma passando `True`, `False`, `None`, `"123"`, `[]`, `{}`, `float("nan")`, `float("inf")` e `float("-inf")` tanto no primeiro quanto no segundo argumento. Se **qualquer um** não lançar exceção, você reprova.
2. Teste `dividir(10, 0)`, `dividir(0, 0)` e `dividir(-5.5, 0.0)`: todos devem lançar especificamente `ZeroDivisionError`.
