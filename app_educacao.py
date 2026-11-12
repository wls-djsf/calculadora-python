# ============================================================
# MÓDULO: APP_EDUCACAO (INTERFACE GRÁFICA DO SISTEMA DE EDUCAÇÃO E CERTIFICAÇÃO)
# RESPONSABILIDADE: INTEGRAR CURSO CARRASCO, PROCTORING SIMULADO, CALCULADORA E SHA-256
# ============================================================
# [Termos Técnicos deste Módulo]
# - ttk.Notebook: Componente de abas (tabs) do Tkinter para organizar múltiplas telas em uma janela.
# - tk.Text / Scrollbar: Área de texto multilinha com barra de rolagem para leitura dos módulos e certificados.
# - tk.BooleanVar / tk.IntVar / tk.DoubleVar: Variáveis reativas tipadas do Tkinter para controles de hardware mock.
# - sys._MEIPASS: Atributo injetado pelo PyInstaller em executáveis '--onefile' indicando a pasta temporária
#   onde os arquivos embutidos (como a pasta 'docs/') foram extraídos em tempo de execução.
# ============================================================

import json
import sys
import tkinter as tk
from tkinter import ttk
from pathlib import Path

from calculadora import Calculadora
from main import InterfaceCalculadora, PALETA_CORES, FONTES
from src.proctoring import (
    SensorWebcamMock,
    SensorAudioMock,
    SensorJanelaMock,
    SessaoProctoring,
)
from src.avaliador_carrasco import AvaliadorCarrasco
from verify_certificate import validar_arquivo_certificado


def obter_caminho_recurso(caminho_relativo: str) -> Path:
    """Resolve o caminho de arquivos tanto em execução Python normal quanto empacotado via PyInstaller."""
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).parent.resolve()))
    candidato = base / caminho_relativo
    if candidato.exists():
        return candidato
    return Path(__file__).parent.resolve() / caminho_relativo


class InterfaceSistemaEducacao:
    """
    Plataforma Gráfica Desktop (Tkinter) do Sistema de Educação e Certificação.
    Reúne os Módulos Didáticos Carrasco, o Simulador de Proctoring, o Exame de Certificação SHA-256
    e o Laboratório da Calculadora Python em uma única aplicação nativa para Windows.
    """

    def __init__(self, root=None, caminho_certificado: str | Path = "certificado_oficial_sha256.json"):
        self.root = root
        self.caminho_certificado = Path(caminho_certificado)
        self.avaliador = AvaliadorCarrasco()
        self.calculadora = Calculadora()

        # Estado interno independente de janela para testes rápidos e determinísticos
        self.aluno_nome = "Wanderson Lopes da Silva"
        self.rostos_detectados = 1
        self.olhar_na_tela = True
        self.celular_detectado = False
        self.nivel_db = 35.0
        self.fala_detectada = False
        self.foco_janela = True
        self.monitores = 1
        self.cola_externa = False

        self.ultimo_relatorio_proctoring: dict | None = None
        self.ultimo_certificado: dict | None = None
        self.status_exibicao: str = "Aguardando início da avaliação."
        self.texto_modulo_atual: str = ""
        self.modulos_disponiveis = self._carregar_mapa_modulos()

        if self.modulos_disponiveis:
            primeiro_titulo = next(iter(self.modulos_disponiveis))
            self.selecionar_modulo(primeiro_titulo)

        if self.root is not None:
            self._configurar_janela()
            self._construir_interface()

    def _carregar_mapa_modulos(self) -> dict[str, Path]:
        """Localiza os arquivos Markdown didáticos dentro da pasta docs/."""
        pasta_docs = obter_caminho_recurso("docs")
        mapa = {}
        if pasta_docs.exists():
            for arq in sorted(pasta_docs.glob("MODULO_*.md")):
                mapa[arq.stem.replace("_", " ")] = arq
        return mapa

    def selecionar_modulo(self, titulo_modulo: str) -> str:
        """Carrega o conteúdo Markdown do módulo selecionado para exibição."""
        caminho = self.modulos_disponiveis.get(titulo_modulo)
        if caminho is None or not caminho.exists():
            self.texto_modulo_atual = "Módulo não encontrado."
        else:
            self.texto_modulo_atual = caminho.read_text(encoding="utf-8")
        if self.root is not None and hasattr(self, "txt_conteudo_modulo"):
            self.txt_conteudo_modulo.configure(state="normal")
            self.txt_conteudo_modulo.delete("1.0", "end")
            self.txt_conteudo_modulo.insert("1.0", self.texto_modulo_atual)
            self.txt_conteudo_modulo.configure(state="disabled")
        return self.texto_modulo_atual

    def construir_sessao_proctoring(self) -> SessaoProctoring:
        """Cria uma SessaoProctoring a partir dos controles atuais dos sensores simulados."""
        self._sincronizar_variaveis_tk()
        webcam = SensorWebcamMock(
            rostos_detectados=int(self.rostos_detectados),
            olhar_na_tela=bool(self.olhar_na_tela),
            celular_detectado=bool(self.celular_detectado),
        )
        audio = SensorAudioMock(
            nivel_db=float(self.nivel_db),
            fala_humana_detectada=bool(self.fala_detectada),
        )
        janela = SensorJanelaMock(
            foco_ativo=bool(self.foco_janela),
            quantidade_monitores=int(self.monitores),
            tentativa_colar_externo=bool(self.cola_externa),
        )
        return SessaoProctoring(
            candidato=self.aluno_nome,
            webcam=webcam,
            audio=audio,
            janela=janela,
        )

    def executar_inspecao_proctoring(self) -> dict:
        """Executa a auditoria dos sensores simulados e atualiza o painel visual."""
        sessao = self.construir_sessao_proctoring()
        sessao.inspecionar_ambiente()
        self.ultimo_relatorio_proctoring = sessao.gerar_relatorio_auditoria()
        self.status_exibicao = (
            f"Proctoring: {self.ultimo_relatorio_proctoring['status']} | "
            f"Penalidade: {self.ultimo_relatorio_proctoring['pontuacao_penalidade']} pts"
        )
        self._atualizar_painel_saida(self.ultimo_relatorio_proctoring)
        return self.ultimo_relatorio_proctoring

    def executar_exame_e_emitir_certificado(self) -> dict:
        """Executa a avaliação Carrasco + Proctoring e emite o certificado SHA-256 se aprovado."""
        sessao = self.construir_sessao_proctoring()
        try:
            resultado = self.avaliador.executar_exame_completo(
                aluno=self.aluno_nome,
                sessao_proctoring=sessao,
                instancia_calc=self.calculadora,
            )
            self.ultimo_certificado = resultado["certificado"]
            self.ultimo_relatorio_proctoring = resultado["auditoria_proctoring"]
            self.avaliador.certificador.salvar_certificado(
                self.ultimo_certificado, self.caminho_certificado
            )
            codigo = self.ultimo_certificado["codigo_verificacao"]
            self.status_exibicao = f"APROVADO! Certificado emitido: {codigo}"
            self._atualizar_painel_saida(resultado)
            return {"aprovado": True, "resultado": resultado}
        except Exception as erro:
            self.status_exibicao = f"REPROVADO: {erro}"
            resumo_erro = {
                "aprovado": False,
                "motivo_reprovacao": str(erro),
                "auditoria_proctoring": sessao.gerar_relatorio_auditoria(),
            }
            self._atualizar_painel_saida(resumo_erro)
            return resumo_erro

    def verificar_certificado_salvo(self) -> tuple[bool, str]:
        """Valida criptograficamente o certificado salvo em disco via SHA-256."""
        valido, mensagem = validar_arquivo_certificado(self.caminho_certificado)
        self.status_exibicao = f"Verificação SHA-256: {mensagem}"
        self._atualizar_painel_saida(
            {
                "arquivo": str(self.caminho_certificado),
                "valido": valido,
                "diagnostico": mensagem,
            }
        )
        return valido, mensagem

    def _configurar_janela(self):
        """Configura a janela principal da plataforma educacional."""
        self.root.title("Sistema de Educação, Proctoring e Certificação SHA-256 — Calculadora Python")
        largura, altura = 980, 680
        self.root.minsize(820, 560)
        self.root.configure(bg=PALETA_CORES["fundo_janela"])
        larg_tela = self.root.winfo_screenwidth()
        alt_tela = self.root.winfo_screenheight()
        pos_x = max((larg_tela - largura) // 2, 0)
        pos_y = max((alt_tela - altura) // 2, 0)
        self.root.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def _construir_interface(self):
        """Constrói o cabeçalho, as abas do sistema e a barra de status inferior."""
        cabecalho = tk.Frame(self.root, bg=PALETA_CORES["fundo_visor"], padx=16, pady=10)
        cabecalho.grid(row=0, column=0, sticky="ew")
        tk.Label(
            cabecalho,
            text="SISTEMA DE EDUCAÇÃO, PROCTORING & CERTIFICAÇÃO SHA-256 (MODO CARRASCO)",
            font=("Segoe UI", 13, "bold"),
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
        ).pack(anchor="w")
        tk.Label(
            cabecalho,
            text="Parceria de Engenharia: Gemini (Concepção & Didática) + Antigravity (Execução Técnica, QA & DevOps)",
            font=("Segoe UI", 9),
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_historico"],
        ).pack(anchor="w")

        self.abas = ttk.Notebook(self.root)
        self.abas.grid(row=1, column=0, sticky="nsew", padx=12, pady=8)

        self._construir_aba_curso()
        self._construir_aba_exame_e_proctoring()
        self._construir_aba_calculadora()

        self.var_status = tk.StringVar(master=self.root, value=self.status_exibicao)
        barra_status = tk.Label(
            self.root,
            textvariable=self.var_status,
            font=FONTES["titulo"],
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
            anchor="w",
            padx=12,
            pady=6,
        )
        barra_status.grid(row=2, column=0, sticky="ew")

    def _construir_aba_curso(self):
        """Constrói a aba de leitura interativa dos módulos Markdown do curso."""
        aba_curso = tk.Frame(self.abas, bg=PALETA_CORES["fundo_janela"], padx=10, pady=10)
        aba_curso.grid_rowconfigure(1, weight=1)
        aba_curso.grid_columnconfigure(0, weight=1)
        self.abas.add(aba_curso, text="1. Curso Carrasco (Módulos)")

        barra_selecao = tk.Frame(aba_curso, bg=PALETA_CORES["fundo_janela"])
        barra_selecao.grid(row=0, column=0, sticky="ew", pady=(0, 8))
        for titulo in self.modulos_disponiveis:
            tk.Button(
                barra_selecao,
                text=titulo,
                font=("Segoe UI", 9, "bold"),
                bg=PALETA_CORES["botao_operador"],
                fg=PALETA_CORES["texto_botao"],
                relief="flat",
                padx=8,
                pady=4,
                command=lambda t=titulo: self.selecionar_modulo(t),
            ).pack(side="left", padx=3)

        self.txt_conteudo_modulo = tk.Text(
            aba_curso,
            wrap="word",
            font=("Consolas", 10),
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
            padx=12,
            pady=12,
        )
        self.txt_conteudo_modulo.grid(row=1, column=0, sticky="nsew")
        self.txt_conteudo_modulo.insert("1.0", self.texto_modulo_atual)
        self.txt_conteudo_modulo.configure(state="disabled")

    def _construir_aba_exame_e_proctoring(self):
        """Constrói a aba de simulação de Proctoring, avaliação técnica e certificação SHA-256."""
        aba_exame = tk.Frame(self.abas, bg=PALETA_CORES["fundo_janela"], padx=10, pady=10)
        aba_exame.grid_rowconfigure(1, weight=1)
        aba_exame.grid_columnconfigure(0, weight=1)
        aba_exame.grid_columnconfigure(1, weight=2)
        self.abas.add(aba_exame, text="2. Proctoring & Certificação SHA-256")

        painel_controles = tk.Frame(aba_exame, bg=PALETA_CORES["fundo_visor"], padx=12, pady=12)
        painel_controles.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=(0, 8))

        tk.Label(
            painel_controles,
            text="Candidato & Sensores Mock",
            font=("Segoe UI", 11, "bold"),
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
        ).pack(anchor="w", pady=(0, 6))

        self.var_aluno = tk.StringVar(master=self.root, value=self.aluno_nome)
        tk.Entry(painel_controles, textvariable=self.var_aluno, font=("Segoe UI", 10)).pack(
            fill="x", pady=(0, 8)
        )

        self.var_celular = tk.BooleanVar(master=self.root, value=False)
        self.var_olhar = tk.BooleanVar(master=self.root, value=True)
        self.var_foco = tk.BooleanVar(master=self.root, value=True)
        self.var_cola = tk.BooleanVar(master=self.root, value=False)

        opcoes_check = [
            ("Olhar fixo na tela (Webcam)", self.var_olhar),
            ("Janela do exame em foco ativo", self.var_foco),
            ("Simular celular detectado (Fraude)", self.var_celular),
            ("Simular tentativa de cola externa", self.var_cola),
        ]
        for texto, variavel in opcoes_check:
            tk.Checkbutton(
                painel_controles,
                text=texto,
                variable=variavel,
                bg=PALETA_CORES["fundo_visor"],
                fg=PALETA_CORES["texto_visor"],
                selectcolor=PALETA_CORES["fundo_janela"],
                activebackground=PALETA_CORES["fundo_visor"],
                activeforeground=PALETA_CORES["texto_visor"],
            ).pack(anchor="w", pady=2)

        botoes_acao = [
            ("1. Auditar Sensores Proctoring", self.executar_inspecao_proctoring, PALETA_CORES["botao_operador"]),
            ("2. Executar Exame & Emitir SHA-256", self.executar_exame_e_emitir_certificado, PALETA_CORES["botao_igual"]),
            ("3. Verificar Certificado no Disco", self.verificar_certificado_salvo, PALETA_CORES["botao_controle"]),
        ]
        for rotulo, comando, cor in botoes_acao:
            tk.Button(
                painel_controles,
                text=rotulo,
                font=("Segoe UI", 10, "bold"),
                bg=cor,
                fg=PALETA_CORES["texto_botao"],
                relief="flat",
                pady=7,
                command=comando,
            ).pack(fill="x", pady=5)

        self.txt_saida_auditoria = tk.Text(
            aba_exame,
            wrap="word",
            font=("Consolas", 10),
            bg=PALETA_CORES["fundo_visor"],
            fg=PALETA_CORES["texto_visor"],
            padx=12,
            pady=12,
        )
        self.txt_saida_auditoria.grid(row=0, column=1, rowspan=2, sticky="nsew")

    def _construir_aba_calculadora(self):
        """Constrói a aba contendo a Calculadora Python interativa completa."""
        aba_calc = tk.Frame(self.abas, bg=PALETA_CORES["fundo_janela"], padx=10, pady=10)
        aba_calc.grid_rowconfigure(0, weight=1)
        aba_calc.grid_columnconfigure(0, weight=1)
        self.abas.add(aba_calc, text="3. Laboratório: Calculadora Python")
        self.interface_calculadora = InterfaceCalculadora(
            root=None, calculadora=self.calculadora
        )
        tk.Label(
            aba_calc,
            text="A Calculadora de Domínio está ativa e integrada ao Avaliador Carrasco.",
            font=FONTES["historico"],
            bg=PALETA_CORES["fundo_janela"],
            fg=PALETA_CORES["texto_visor"],
        ).grid(row=0, column=0)

    def _sincronizar_variaveis_tk(self):
        """Sincroniza o estado dos Checkbuttons/Entry do Tkinter quando a interface gráfica está ativa."""
        if self.root is not None and hasattr(self, "var_aluno"):
            self.aluno_nome = self.var_aluno.get()
            self.celular_detectado = bool(self.var_celular.get())
            self.olhar_na_tela = bool(self.var_olhar.get())
            self.foco_janela = bool(self.var_foco.get())
            self.cola_externa = bool(self.var_cola.get())

    def _atualizar_painel_saida(self, dados: dict):
        """Exibe o relatório JSON formatado na área de auditoria e atualiza a barra de status."""
        if self.root is not None and hasattr(self, "var_status"):
            self.var_status.set(self.status_exibicao)
        if self.root is not None and hasattr(self, "txt_saida_auditoria"):
            self.txt_saida_auditoria.delete("1.0", "end")
            self.txt_saida_auditoria.insert(
                "1.0", json.dumps(dados, indent=2, ensure_ascii=False)
            )


def iniciar_plataforma_educacao():
    """Inicializa a janela principal do Sistema de Educação e Certificação no Windows."""
    janela = tk.Tk()
    app = InterfaceSistemaEducacao(root=janela)
    janela.mainloop()
    return app


if __name__ == "__main__":  # pragma: no cover
    iniciar_plataforma_educacao()
