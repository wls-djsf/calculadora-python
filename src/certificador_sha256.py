# ============================================================
# MÓDULO: CERTIFICADOR CRIPTOGRÁFICO SHA-256
# RESPONSABILIDADE: EMISSÃO E VERIFICAÇÃO ANTIFRAUDE DE CERTIFICADOS DIGITAIS
# ============================================================

import hashlib
import hmac
import json
from datetime import datetime, timezone
from pathlib import Path
from src.proctoring import SessaoProctoring

CHAVE_EMISSOR_PADRAO = "ANTIGRAVITY-GEMINI-CARRASCO-CLEAN-CODE-2026-SHA256-SALT"
CURSO_PADRAO = "Engenharia de Software Sênior, TDD, Mutação e Clean Code com Python"


class ErroCertificacaoReprovada(ValueError):
    """Exceção lançada quando o candidato não atinge os critérios rigorosos de certificação."""


class CertificadorSHA256:
    """
    Motor criptográfico baseado em SHA-256 para emissão e validação de certificados técnicos.
    Utiliza serialização JSON canônica e comparação em tempo constante (hmac.compare_digest).
    """

    NOTA_MINIMA_APROVACAO = 80.0
    COBERTURA_MINIMA_PCT = 95.0
    TAXA_MUTACAO_MINIMA_PCT = 100.0
    CRAP_MAXIMO_PERMITIDO = 12.0

    def __init__(self, segredo_emissor: str = CHAVE_EMISSOR_PADRAO):
        if not isinstance(segredo_emissor, str) or len(segredo_emissor.strip()) < 8:
            raise ValueError("O segredo do emissor deve possuir no mínimo 8 caracteres.")
        self.segredo_emissor = segredo_emissor

    @staticmethod
    def gerar_hash_sha256(conteudo_textual: str) -> str:
        """Calcula o resumo criptográfico SHA-256 (64 caracteres hexadecimais) de uma string UTF-8."""
        return hashlib.sha256(conteudo_textual.encode("utf-8")).hexdigest()

    @staticmethod
    def serializar_payload_canonico(payload: dict) -> str:
        """Serializa o dicionário do payload em JSON determinístico (chaves ordenadas e sem espaços extras)."""
        return json.dumps(payload, sort_keys=True, ensure_ascii=False, separators=(",", ":"))

    def calcular_assinatura(self, hash_payload: str) -> str:
        """Gera a assinatura SHA-256 salgada combinando o hash do payload com o segredo do emissor."""
        material = f"{hash_payload}::{self.segredo_emissor}"
        return self.gerar_hash_sha256(material)

    def _validar_requisitos_aprovacao(
        self,
        nota_final: float,
        cobertura_pct: float,
        taxa_mutacao_pct: float,
        crap_maximo: float,
        sessao_proctoring: SessaoProctoring,
    ):
        """Aplica as regras 'Carrasco' de engenharia antes de autorizar a emissão do certificado."""
        if not sessao_proctoring.esta_elegivel_para_certificacao():
            raise ErroCertificacaoReprovada(
                f"Certificação bloqueada pelo Proctoring: status={sessao_proctoring.status} "
                f"(penalidade={sessao_proctoring.pontuacao_penalidade})."
            )
        if nota_final < self.NOTA_MINIMA_APROVACAO:
            raise ErroCertificacaoReprovada(
                f"Nota insuficiente ({nota_final:.1f} < {self.NOTA_MINIMA_APROVACAO:.1f})."
            )
        if cobertura_pct < self.COBERTURA_MINIMA_PCT:
            raise ErroCertificacaoReprovada(
                f"Cobertura de código insuficiente ({cobertura_pct:.1f}% < {self.COBERTURA_MINIMA_PCT:.1f}%)."
            )
        if taxa_mutacao_pct < self.TAXA_MUTACAO_MINIMA_PCT:
            raise ErroCertificacaoReprovada(
                f"Sobrevivência de mutantes detectada ({taxa_mutacao_pct:.1f}% < {self.TAXA_MUTACAO_MINIMA_PCT:.1f}%)."
            )
        if crap_maximo > self.CRAP_MAXIMO_PERMITIDO:
            raise ErroCertificacaoReprovada(
                f"Pontuação CRAP acima do limite seguro ({crap_maximo:.2f} > {self.CRAP_MAXIMO_PERMITIDO:.2f})."
            )

    def emitir_certificado(
        self,
        aluno: str,
        nota_final: float,
        cobertura_pct: float,
        taxa_mutacao_pct: float,
        crap_maximo: float,
        sessao_proctoring: SessaoProctoring,
        curso: str = CURSO_PADRAO,
        emitido_em_utc: str | None = None,
    ) -> dict:
        """Valida todos os requisitos e emite um certificado assinado com SHA-256."""
        if not isinstance(aluno, str) or not aluno.strip():
            raise ValueError("O nome do aluno deve ser uma string válida.")

        self._validar_requisitos_aprovacao(
            nota_final, cobertura_pct, taxa_mutacao_pct, crap_maximo, sessao_proctoring
        )

        instante = emitido_em_utc or datetime.now(timezone.utc).isoformat()
        semente_id = f"{aluno.strip()}|{curso.strip()}|{instante}"
        id_certificado = f"CERT-{self.gerar_hash_sha256(semente_id)[:12].upper()}"

        payload = {
            "id_certificado": id_certificado,
            "aluno": aluno.strip(),
            "curso": curso.strip(),
            "nota_final": round(float(nota_final), 2),
            "cobertura_pct": round(float(cobertura_pct), 2),
            "taxa_mutacao_pct": round(float(taxa_mutacao_pct), 2),
            "crap_maximo": round(float(crap_maximo), 2),
            "status_proctoring": sessao_proctoring.status,
            "penalidade_proctoring": sessao_proctoring.pontuacao_penalidade,
            "emitido_em_utc": instante,
        }

        json_canonico = self.serializar_payload_canonico(payload)
        hash_payload = self.gerar_hash_sha256(json_canonico)
        assinatura = self.calcular_assinatura(hash_payload)
        codigo_verificacao = f"SHA256-{assinatura[:8].upper()}-{assinatura[-8:].upper()}"

        return {
            "payload": payload,
            "hash_payload_sha256": hash_payload,
            "assinatura_sha256": assinatura,
            "codigo_verificacao": codigo_verificacao,
            "algoritmo": "SHA-256 (FIPS 180-4)",
            "emissor": "Parceria de Engenharia Gemini & Antigravity",
        }

    def salvar_certificado(self, certificado: dict, caminho_arquivo: str | Path) -> Path:
        """Salva o certificado assinado em formato JSON estruturado no disco."""
        destino = Path(caminho_arquivo)
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(
            json.dumps(certificado, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        return destino

    def verificar_certificado(self, certificado: dict) -> tuple[bool, str]:
        """
        Verifica a integridade criptográfica SHA-256 e a conformidade das métricas de um certificado.
        Retorna (valido: bool, mensagem_diagnostico: str).
        """
        if not isinstance(certificado, dict) or "payload" not in certificado:
            return False, "Estrutura de certificado inválida: campo 'payload' ausente."

        payload = certificado["payload"]
        hash_informado = str(certificado.get("hash_payload_sha256", ""))
        assinatura_informada = str(certificado.get("assinatura_sha256", ""))

        json_canonico = self.serializar_payload_canonico(payload)
        hash_recalculado = self.gerar_hash_sha256(json_canonico)

        if not hmac.compare_digest(hash_informado, hash_recalculado):
            return (
                False,
                "Adulteração detectada: o hash SHA-256 do payload não corresponde aos dados do certificado.",
            )

        assinatura_esperada = self.calcular_assinatura(hash_recalculado)
        if not hmac.compare_digest(assinatura_informada, assinatura_esperada):
            return (
                False,
                "Assinatura criptográfica SHA-256 inválida ou falsificada.",
            )

        # Verificar se os critérios mínimos continuam respeitados no payload
        if (
            payload.get("status_proctoring") == "ELIMINADO_POR_FRAUDE"
            or payload.get("nota_final", 0) < self.NOTA_MINIMA_APROVACAO
            or payload.get("cobertura_pct", 0) < self.COBERTURA_MINIMA_PCT
            or payload.get("taxa_mutacao_pct", 0) < self.TAXA_MUTACAO_MINIMA_PCT
            or payload.get("crap_maximo", 999) > self.CRAP_MAXIMO_PERMITIDO
        ):
            return False, "Os indicadores técnicos do payload violam as regras mínimas de aprovação."

        return (
            True,
            f"Certificado AUTÊNTICO e VÁLIDO ({certificado.get('codigo_verificacao')}).",
        )
