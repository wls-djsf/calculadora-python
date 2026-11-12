# ============================================================
# MÓDULO: AVALIADOR CARRASCO (EXAME TÉCNICO AUTOMATIZADO)
# RESPONSABILIDADE: AUDITAR A CALCULADORA DO ALUNO, EXECUTAR PROCTORING E EMITIR CERTIFICADO
# ============================================================

from calculadora import Calculadora
from src.proctoring import SessaoProctoring
from src.certificador_sha256 import CertificadorSHA256


class AvaliadorCarrasco:
    """
    Executa a bateria eliminatória de desafios práticos sobre a classe Calculadora,
    integra o resultado com a sessão de Proctoring e solicita a emissão do certificado SHA-256.
    Cada critério é isolado em seu próprio método (Single Responsibility Principle / CC <= 4).
    """

    def __init__(self, certificador: CertificadorSHA256 | None = None):
        self.certificador = certificador if certificador is not None else CertificadorSHA256()

    @staticmethod
    def _verificar_precisao_decimal(calc: Calculadora) -> bool:
        """Critério 1: Precisão Decimal exata (IEEE 754 vs Decimal) e normalização de tipo."""
        return (
            calc.somar(0.1, 0.2) == 0.3
            and calc.subtrair(0.3, 0.1) == 0.2
            and isinstance(calc.somar(2.5, 2.5), int)
        )

    @staticmethod
    def _verificar_blindagem_tipos(calc: Calculadora) -> bool:
        """Critério 2: Blindagem contra bool, None, strings, NaN e Infinito."""
        entradas_maliciosas = (True, False, None, "10", float("nan"), float("inf"), float("-inf"))
        for entrada in entradas_maliciosas:
            try:
                calc.somar(entrada, 1)
                return False
            except (ValueError, TypeError):
                pass
        return True

    @staticmethod
    def _verificar_divisao_zero(calc: Calculadora) -> bool:
        """Critério 3: Tratamento estrito de Divisão por Zero com ZeroDivisionError."""
        try:
            calc.dividir(10, 0)
            return False
        except ZeroDivisionError:
            return True

    @staticmethod
    def _verificar_porcentagem_contextual(calc: Calculadora) -> bool:
        """Critério 4: Porcentagem Contextual no padrão da calculadora do Windows."""
        return (
            calc.porcentagem(50) == 0.5
            and calc.porcentagem(10, 200, "+") == 20
            and calc.porcentagem(10, 200, "*") == 0.1
        )

    @staticmethod
    def _verificar_encadeamento_e_sinal(calc: Calculadora) -> bool:
        """Critério 5: Operações Encadeadas e Inversão de Sinal."""
        return (
            calc.calcular_encadeado(10, [("+", 5), ("*", 2), ("-", 6), ("/", 4)]) == 6
            and calc.inverter_sinal(5) == -5
            and calc.inverter_sinal(-5) == 5
            and str(calc.inverter_sinal(0)) == "0"
        )

    def avaliar_implementacao_calculadora(self, instancia_calc: Calculadora | None = None) -> dict:
        """
        Submete a instância de Calculadora aos 5 desafios técnicos dos módulos do curso.
        Retorna nota (0 a 100) e detalhamento por critério.
        """
        calc = instancia_calc if instancia_calc is not None else Calculadora()
        verificacoes = [
            ("Precisão Decimal e Normalização de Tipo", self._verificar_precisao_decimal),
            ("Blindagem contra Tipos Inválidos (bool/NaN/inf)", self._verificar_blindagem_tipos),
            ("Proteção de Divisão por Zero (ZeroDivisionError)", self._verificar_divisao_zero),
            ("Porcentagem Contextual (+, -, *, /)", self._verificar_porcentagem_contextual),
            ("Operações Encadeadas e Inversão de Sinal", self._verificar_encadeamento_e_sinal),
        ]

        detalhes = [
            {"criterio": nome, "pontos": 20.0 if funcao(calc) else 0.0}
            for nome, funcao in verificacoes
        ]
        nota_total = sum(item["pontos"] for item in detalhes)
        return {
            "nota_final": nota_total,
            "aprovado_tecnico": nota_total >= 80.0,
            "criterios": detalhes,
        }

    def executar_exame_completo(
        self,
        aluno: str,
        sessao_proctoring: SessaoProctoring,
        instancia_calc: Calculadora | None = None,
        cobertura_pct: float = 100.0,
        taxa_mutacao_pct: float = 100.0,
        crap_maximo: float = 5.0,
    ) -> dict:
        """
        Inspeciona o ambiente de Proctoring, avalia a implementação da calculadora e,
        se aprovado em tudo, emite o certificado criptografado SHA-256.
        """
        sessao_proctoring.inspecionar_ambiente()
        resultado_tecnico = self.avaliar_implementacao_calculadora(instancia_calc)

        certificado = self.certificador.emitir_certificado(
            aluno=aluno,
            nota_final=resultado_tecnico["nota_final"],
            cobertura_pct=cobertura_pct,
            taxa_mutacao_pct=taxa_mutacao_pct,
            crap_maximo=crap_maximo,
            sessao_proctoring=sessao_proctoring,
        )
        return {
            "avaliacao_tecnica": resultado_tecnico,
            "auditoria_proctoring": sessao_proctoring.gerar_relatorio_auditoria(),
            "certificado": certificado,
        }
