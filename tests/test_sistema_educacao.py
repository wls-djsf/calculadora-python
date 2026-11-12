# ============================================================
# TESTES UNITÁRIOS E DE INTEGRAÇÃO: SISTEMA DE EDUCAÇÃO, PROCTORING E CERTIFICAÇÃO SHA-256
# ============================================================

import copy
import json
import unittest
import pytest
from src.proctoring import (
    SensorWebcamMock,
    SensorAudioMock,
    SensorJanelaMock,
    SessaoProctoring,
)
from src.certificador_sha256 import (
    CertificadorSHA256,
    ErroCertificacaoReprovada,
)
from src.avaliador_carrasco import AvaliadorCarrasco
from verify_certificate import (
    validar_arquivo_certificado,
    gerar_e_verificar_demonstracao,
    main as cli_verify_main,
)


class TestProctoringSimulado(unittest.TestCase):
    """Valida as regras de monitoramento de hardware simulado (webcam, áudio e janela)."""

    def test_sessao_integra_sem_infracoes(self):
        sessao = SessaoProctoring(candidato="Wanderson Lopes")
        infracoes = sessao.inspecionar_ambiente()
        self.assertEqual(len(infracoes), 0)
        self.assertEqual(sessao.pontuacao_penalidade, 0)
        self.assertEqual(sessao.status, "INTEGRO")
        self.assertTrue(sessao.esta_elegivel_para_certificacao())

    def test_candidato_invalido_dispara_erro(self):
        with self.assertRaises(ValueError):
            SessaoProctoring(candidato="   ")
        with self.assertRaises(ValueError):
            SessaoProctoring(candidato=None)

    def test_advertencia_leve_sem_eliminacao(self):
        webcam = SensorWebcamMock(rostos_detectados=1, olhar_na_tela=False, celular_detectado=False)
        sessao = SessaoProctoring(candidato="Aluno Teste", webcam=webcam)
        infracoes = sessao.inspecionar_ambiente()
        self.assertEqual(len(infracoes), 1)
        self.assertEqual(infracoes[0].codigo, "DESVIO_OLHAR")
        self.assertEqual(sessao.pontuacao_penalidade, 20)
        self.assertEqual(sessao.status, "ADVERTIDO")
        self.assertTrue(sessao.esta_elegivel_para_certificacao())

    def test_eliminacao_imediata_por_celular_detectado(self):
        webcam = SensorWebcamMock(rostos_detectados=1, olhar_na_tela=True, celular_detectado=True)
        sessao = SessaoProctoring(candidato="Aluno Fraude", webcam=webcam)
        sessao.inspecionar_ambiente()
        self.assertEqual(sessao.pontuacao_penalidade, 100)
        self.assertEqual(sessao.status, "ELIMINADO_POR_FRAUDE")
        self.assertFalse(sessao.esta_elegivel_para_certificacao())

    def test_eliminacao_por_acumulo_de_tres_infracoes(self):
        webcam = SensorWebcamMock(rostos_detectados=0, olhar_na_tela=False, celular_detectado=False)
        audio = SensorAudioMock(nivel_db=80.0, fala_humana_detectada=True)
        sessao = SessaoProctoring(candidato="Aluno Ruido", webcam=webcam, audio=audio)
        infracoes = sessao.inspecionar_ambiente()
        self.assertEqual(len(infracoes), 3)
        self.assertEqual(sessao.status, "ELIMINADO_POR_FRAUDE")
        self.assertFalse(sessao.esta_elegivel_para_certificacao())
        relatorio = sessao.gerar_relatorio_auditoria()
        self.assertEqual(relatorio["quantidade_infracoes"], 3)
        self.assertFalse(relatorio["elegivel_certificacao"])


@pytest.mark.parametrize(
    "webcam, audio, janela, codigo_esperado, pontos_esperados",
    [
        (SensorWebcamMock(rostos_detectados=0), SensorAudioMock(), SensorJanelaMock(), "AUSENCIA_ROSTO", 35),
        (SensorWebcamMock(rostos_detectados=2), SensorAudioMock(), SensorJanelaMock(), "MULTIPLOS_ROSTOS", 60),
        (SensorWebcamMock(celular_detectado=True), SensorAudioMock(), SensorJanelaMock(), "CELULAR_DETECTADO", 100),
        (SensorWebcamMock(olhar_na_tela=False), SensorAudioMock(), SensorJanelaMock(), "DESVIO_OLHAR", 20),
        (SensorWebcamMock(), SensorAudioMock(nivel_db=75.0), SensorJanelaMock(), "AUDIO_SUSPEITO", 40),
        (SensorWebcamMock(), SensorAudioMock(fala_humana_detectada=True), SensorJanelaMock(), "AUDIO_SUSPEITO", 40),
        (SensorWebcamMock(), SensorAudioMock(), SensorJanelaMock(foco_ativo=False), "PERDA_FOCO_JANELA", 50),
        (SensorWebcamMock(), SensorAudioMock(), SensorJanelaMock(quantidade_monitores=2), "MULTIPLOS_MONITORES", 50),
        (SensorWebcamMock(), SensorAudioMock(), SensorJanelaMock(tentativa_colar_externo=True), "COLA_EXTERNA", 70),
    ],
)
def test_parametrizado_regras_infracao_proctoring(webcam, audio, janela, codigo_esperado, pontos_esperados):
    sessao = SessaoProctoring("Candidato Parametrizado", webcam=webcam, audio=audio, janela=janela)
    infracoes = sessao.inspecionar_ambiente()
    assert len(infracoes) == 1
    assert infracoes[0].codigo == codigo_esperado
    assert sessao.pontuacao_penalidade == pontos_esperados


class TestCertificadorSHA256(unittest.TestCase):
    """Valida a emissão criptográfica SHA-256, regras de bloqueio e detecção de adulteração."""

    def setUp(self):
        self.certificador = CertificadorSHA256()
        self.sessao_limpa = SessaoProctoring("Wanderson Lopes da Silva")
        self.sessao_limpa.inspecionar_ambiente()

    def test_segredo_emissor_curto_invalido(self):
        with self.assertRaises(ValueError):
            CertificadorSHA256(segredo_emissor="curto")

    def test_emissao_e_verificacao_certificado_valido(self):
        cert = self.certificador.emitir_certificado(
            aluno="Wanderson Lopes da Silva",
            nota_final=100.0,
            cobertura_pct=100.0,
            taxa_mutacao_pct=100.0,
            crap_maximo=5.0,
            sessao_proctoring=self.sessao_limpa,
            emitido_em_utc="2026-11-11T22:00:00+00:00",
        )
        self.assertEqual(len(cert["hash_payload_sha256"]), 64)
        self.assertEqual(len(cert["assinatura_sha256"]), 64)
        self.assertTrue(cert["codigo_verificacao"].startswith("SHA256-"))
        valido, msg = self.certificador.verificar_certificado(cert)
        self.assertTrue(valido)
        self.assertIn("AUTÊNTICO", msg)

    def test_bloqueio_certificacao_por_criterios_carrasco(self):
        # 1. Aluno vazio
        with self.assertRaises(ValueError):
            self.certificador.emitir_certificado("", 100.0, 100.0, 100.0, 5.0, self.sessao_limpa)
        # 2. Nota < 80
        with self.assertRaises(ErroCertificacaoReprovada):
            self.certificador.emitir_certificado("Aluno", 79.9, 100.0, 100.0, 5.0, self.sessao_limpa)
        # 3. Cobertura < 95%
        with self.assertRaises(ErroCertificacaoReprovada):
            self.certificador.emitir_certificado("Aluno", 100.0, 94.0, 100.0, 5.0, self.sessao_limpa)
        # 4. Taxa de mutação < 100%
        with self.assertRaises(ErroCertificacaoReprovada):
            self.certificador.emitir_certificado("Aluno", 100.0, 100.0, 96.0, 5.0, self.sessao_limpa)
        # 5. CRAP > 12.0
        with self.assertRaises(ErroCertificacaoReprovada):
            self.certificador.emitir_certificado("Aluno", 100.0, 100.0, 100.0, 12.5, self.sessao_limpa)
        # 6. Eliminado no Proctoring
        sessao_fraude = SessaoProctoring(
            "Aluno", webcam=SensorWebcamMock(celular_detectado=True)
        )
        sessao_fraude.inspecionar_ambiente()
        with self.assertRaises(ErroCertificacaoReprovada):
            self.certificador.emitir_certificado("Aluno", 100.0, 100.0, 100.0, 5.0, sessao_fraude)

    def test_deteccao_de_adulteracao_no_payload_ou_assinatura(self):
        cert = self.certificador.emitir_certificado(
            aluno="Wanderson Lopes da Silva",
            nota_final=90.0,
            cobertura_pct=100.0,
            taxa_mutacao_pct=100.0,
            crap_maximo=4.0,
            sessao_proctoring=self.sessao_limpa,
        )
        # Adulterar nota no payload sem atualizar hash
        adulterado_payload = copy.deepcopy(cert)
        adulterado_payload["payload"]["nota_final"] = 100.0
        valido, msg = self.certificador.verificar_certificado(adulterado_payload)
        self.assertFalse(valido)
        self.assertIn("Adulteração detectada", msg)

        # Recalcular hash_payload mas sem conhecer o segredo do emissor
        adulterado_assinatura = copy.deepcopy(adulterado_payload)
        novo_json = self.certificador.serializar_payload_canonico(adulterado_assinatura["payload"])
        adulterado_assinatura["hash_payload_sha256"] = self.certificador.gerar_hash_sha256(novo_json)
        valido2, msg2 = self.certificador.verificar_certificado(adulterado_assinatura)
        self.assertFalse(valido2)
        self.assertIn("Assinatura criptográfica SHA-256 inválida", msg2)

        # Estrutura inválida
        valido3, _ = self.certificador.verificar_certificado({"invalido": True})
        self.assertFalse(valido3)

        # Forjar payload com nota reprovada mas assinado com a chave
        forjado = copy.deepcopy(cert)
        forjado["payload"]["nota_final"] = 50.0
        h_forjado = self.certificador.gerar_hash_sha256(
            self.certificador.serializar_payload_canonico(forjado["payload"])
        )
        forjado["hash_payload_sha256"] = h_forjado
        forjado["assinatura_sha256"] = self.certificador.calcular_assinatura(h_forjado)
        valido4, msg4 = self.certificador.verificar_certificado(forjado)
        self.assertFalse(valido4)
        self.assertIn("violam as regras mínimas", msg4)


def test_avaliador_carrasco_e_script_verify_certificate(tmp_path):
    """Testa o fluxo ponta a ponta do AvaliadorCarrasco e do módulo verify_certificate."""
    caminho_cert = tmp_path / "cert_teste.json"
    resumo = gerar_e_verificar_demonstracao(caminho_cert)
    assert resumo["valido"] is True
    assert caminho_cert.exists()

    # Testar CLI com caminho válido e em modo demonstração sem argumentos
    assert cli_verify_main([str(caminho_cert)]) == 0
    assert cli_verify_main([]) == 0

    # Testar CLI com arquivo inexistente
    assert cli_verify_main([str(tmp_path / "nao_existe.json")]) == 1

    # Testar arquivo JSON malformado
    arq_corrompido = tmp_path / "corrompido.json"
    arq_corrompido.write_text("{json_invalido", encoding="utf-8")
    valido, msg = validar_arquivo_certificado(arq_corrompido)
    assert valido is False
    assert "corrompido" in msg


def test_avaliador_carrasco_detecta_calculadora_defeituosa():
    """Verifica que uma calculadora que usa float impreciso e aceita bool perde pontos e reprova."""
    class CalculadoraIngênua:
        def somar(self, a, b):
            return a + b

        def subtrair(self, a, b):
            return a - b

        def dividir(self, a, b):
            return 0  # Não lança ZeroDivisionError!

        def porcentagem(self, v, base=None, op=None):
            return 0

        def calcular_encadeado(self, ini, ops):
            return 0

        def inverter_sinal(self, n):
            return n

    avaliador = AvaliadorCarrasco()
    resultado = avaliador.avaliar_implementacao_calculadora(CalculadoraIngênua())
    assert resultado["nota_final"] == 0.0
    assert resultado["aprovado_tecnico"] is False


def test_interface_sistema_educacao_gui_e_fluxo_completo(tmp_path):
    """Testa a aplicação gráfica InterfaceSistemaEducacao (app_educacao.py) com e sem janela Tk."""
    import tkinter as tk
    from unittest.mock import MagicMock, patch
    from app_educacao import (
        InterfaceSistemaEducacao,
        obter_caminho_recurso,
        iniciar_plataforma_educacao,
    )

    assert obter_caminho_recurso("docs").exists()
    assert not obter_caminho_recurso("caminho_inexistente_xyz").exists()

    caminho_cert = tmp_path / "cert_gui.json"
    try:
        janela = tk.Tk()
        janela.withdraw()
    except tk.TclError:
        janela = None

    try:
        app = InterfaceSistemaEducacao(root=janela, caminho_certificado=caminho_cert)
        assert len(app.modulos_disponiveis) >= 6
        primeiro_mod = next(iter(app.modulos_disponiveis))
        conteudo = app.selecionar_modulo(primeiro_mod)
        assert "Módulo" in conteudo
        assert app.selecionar_modulo("MODULO_INEXISTENTE") == "Módulo não encontrado."

        # 1. Inspeção de Proctoring íntegra
        rel_proc = app.executar_inspecao_proctoring()
        assert rel_proc["status"] == "INTEGRO"

        # 2. Exame completo aprovado + emissão de certificado SHA-256
        res_exame = app.executar_exame_e_emitir_certificado()
        assert res_exame["aprovado"] is True
        assert caminho_cert.exists()

        # 3. Verificação SHA-256 do certificado salvo
        valido, msg = app.verificar_certificado_salvo()
        assert valido is True
        assert "AUTÊNTICO" in msg

        # 4. Simular fraude (celular detectado) e confirmar bloqueio do certificado
        if janela is not None:
            app.var_celular.set(True)
        else:
            app.celular_detectado = True
        res_fraude = app.executar_exame_e_emitir_certificado()
        assert res_fraude["aprovado"] is False
        assert "bloqueada pelo Proctoring" in res_fraude["motivo_reprovacao"]
    finally:
        if janela is not None:
            janela.destroy()

    # Testar iniciar_plataforma_educacao com Mock de Tk para não bloquear em mainloop
    with patch("app_educacao.tk.Tk") as mock_tk:
        instancia_tk = MagicMock()
        instancia_tk.winfo_screenwidth.return_value = 1920
        instancia_tk.winfo_screenheight.return_value = 1080
        mock_tk.return_value = instancia_tk
        with patch.object(InterfaceSistemaEducacao, "_construir_interface"):
            app_iniciado = iniciar_plataforma_educacao()
            instancia_tk.mainloop.assert_called_once()
            assert isinstance(app_iniciado, InterfaceSistemaEducacao)
