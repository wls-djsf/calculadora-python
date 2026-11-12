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
