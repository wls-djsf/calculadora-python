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
