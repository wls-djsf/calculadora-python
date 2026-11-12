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
