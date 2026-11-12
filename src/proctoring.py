# ============================================================
# MÓDULO: PROCTORING SIMULADO (SUPERVISÃO DE EXAME E MOCKS DE HARDWARE)
# RESPONSABILIDADE: MONITORAR SENSORES SIMULADOS E APLICAR REGRAS DE INFRAÇÃO
# ============================================================

from dataclasses import dataclass, asdict
from datetime import datetime, timezone


@dataclass
class SensorWebcamMock:
    """Mock de hardware de vídeo (webcam) para simulação determinística de supervisão."""
    rostos_detectados: int = 1
    olhar_na_tela: bool = True
    celular_detectado: bool = False


@dataclass
class SensorAudioMock:
    """Mock de hardware de áudio (microfone) com medição em decibéis (dB) e detecção de voz."""
    nivel_db: float = 35.0
    fala_humana_detectada: bool = False


@dataclass
class SensorJanelaMock:
    """Mock de telemetria do sistema operacional (foco de janela, monitores e área de transferência)."""
    foco_ativo: bool = True
    quantidade_monitores: int = 1
    tentativa_colar_externo: bool = False


@dataclass(frozen=True)
class RegistroInfracao:
    """Estrutura imutável que representa uma infração detectada durante o exame."""
    codigo: str
    descricao: str
    gravidade: str
    pontos: int
    timestamp_utc: str


class SessaoProctoring:
    """
    Motor de supervisão de exame (Proctoring) que avalia os sensores de hardware simulados,
    acumula penalidades e bloqueia candidatos que violem as regras de integridade.
    """

    LIMIAR_ELIMINACAO_PONTOS = 100
    LIMIAR_ELIMINACAO_QUANTIDADE = 3
    LIMIAR_DECIBEIS_MAXIMO = 65.0

    def __init__(self, candidato: str, webcam=None, audio=None, janela=None):
        if not isinstance(candidato, str) or not candidato.strip():
            raise ValueError("O nome do candidato deve ser uma string não vazia.")
        self.candidato = candidato.strip()
        self.webcam = webcam if webcam is not None else SensorWebcamMock()
        self.audio = audio if audio is not None else SensorAudioMock()
        self.janela = janela if janela is not None else SensorJanelaMock()
        self.infracoes: list[RegistroInfracao] = []
        self.pontuacao_penalidade: int = 0
        self.status: str = "INTEGRO"

    def registrar_infracao(self, codigo: str, descricao: str, gravidade: str, pontos: int):
        """Registra uma infração, soma os pontos de penalidade e recalcula o status da sessão."""
        agora = datetime.now(timezone.utc).isoformat()
        infracao = RegistroInfracao(
            codigo=codigo,
            descricao=descricao,
            gravidade=gravidade,
            pontos=pontos,
            timestamp_utc=agora,
        )
        self.infracoes.append(infracao)
        self.pontuacao_penalidade += pontos
        self._atualizar_status()
        return infracao

    def _atualizar_status(self):
        """Atualiza o estado da sessão conforme os limites de tolerância."""
        if (
            self.pontuacao_penalidade >= self.LIMIAR_ELIMINACAO_PONTOS
            or len(self.infracoes) >= self.LIMIAR_ELIMINACAO_QUANTIDADE
        ):
            self.status = "ELIMINADO_POR_FRAUDE"
        else:
            self.status = "ADVERTIDO"

    def inspecionar_ambiente(self):
        """Lê os três mocks de hardware (webcam, áudio e janela) e aplica as regras de infração."""
        novas_infracoes = []
        regras = [
            (
                self.webcam.rostos_detectados == 0,
                "AUSENCIA_ROSTO",
                "Nenhum rosto detectado no enquadramento da webcam.",
                "MEDIA",
                35,
            ),
            (
                self.webcam.rostos_detectados > 1,
                "MULTIPLOS_ROSTOS",
                "Mais de uma pessoa detectada no ambiente de prova.",
                "CRITICA",
                60,
            ),
            (
                self.webcam.celular_detectado,
                "CELULAR_DETECTADO",
                "Dispositivo móvel não autorizado detectado pela câmera.",
                "ELIMINATORIA",
                100,
            ),
            (
                not self.webcam.olhar_na_tela,
                "DESVIO_OLHAR",
                "Candidato desviou o olhar da tela de avaliação.",
                "LEVE",
                20,
            ),
            (
                self.audio.nivel_db > self.LIMIAR_DECIBEIS_MAXIMO or self.audio.fala_humana_detectada,
                "AUDIO_SUSPEITO",
                "Ruído acima de 65 dB ou conversação detectada no microfone.",
                "MEDIA",
                40,
            ),
            (
                not self.janela.foco_ativo,
                "PERDA_FOCO_JANELA",
                "Troca de janela ou perda de foco da aplicação de exame (Alt+Tab).",
                "ALTA",
                50,
            ),
            (
                self.janela.quantidade_monitores > 1,
                "MULTIPLOS_MONITORES",
                "Múltiplos monitores conectados durante a avaliação.",
                "ALTA",
                50,
            ),
            (
                self.janela.tentativa_colar_externo,
                "COLA_EXTERNA",
                "Tentativa de colar conteúdo externo na área de avaliação.",
                "CRITICA",
                70,
            ),
        ]

        for condicao_violada, codigo, descricao, gravidade, pontos in regras:
            if condicao_violada:
                novas_infracoes.append(self.registrar_infracao(codigo, descricao, gravidade, pontos))

        return novas_infracoes

    def esta_elegivel_para_certificacao(self) -> bool:
        """Retorna True somente se o candidato não tiver sido eliminado por fraude."""
        return self.status != "ELIMINADO_POR_FRAUDE"

    def gerar_relatorio_auditoria(self) -> dict:
        """Gera um dicionário auditável com o resumo completo da sessão de Proctoring."""
        return {
            "candidato": self.candidato,
            "status": self.status,
            "elegivel_certificacao": self.esta_elegivel_para_certificacao(),
            "pontuacao_penalidade": self.pontuacao_penalidade,
            "quantidade_infracoes": len(self.infracoes),
            "infracoes": [asdict(item) for item in self.infracoes],
        }
