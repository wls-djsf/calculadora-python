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
