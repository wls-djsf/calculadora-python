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
