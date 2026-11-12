# ============================================================
# MÓDULO: VERIFY_CERTIFICATE
# RESPONSABILIDADE: VALIDAÇÃO CRIPTOGRÁFICA INDEPENDENTE DE CERTIFICADOS SHA-256
# ============================================================

import json
import sys
from pathlib import Path
from src.certificador_sha256 import CertificadorSHA256, CHAVE_EMISSOR_PADRAO
from src.proctoring import SessaoProctoring
from src.avaliador_carrasco import AvaliadorCarrasco


def validar_arquivo_certificado(
    caminho_arquivo: str | Path, segredo_emissor: str = CHAVE_EMISSOR_PADRAO
) -> tuple[bool, str]:
    """Lê um arquivo JSON de certificado do disco e valida sua autenticidade SHA-256."""
    caminho = Path(caminho_arquivo)
    if not caminho.exists():
        return False, f"Arquivo de certificado não encontrado: {caminho}"
    try:
        dados = json.loads(caminho.read_text(encoding="utf-8"))
    except json.JSONDecodeError as erro:
        return False, f"Arquivo JSON corrompido ou malformado: {erro}"

    certificador = CertificadorSHA256(segredo_emissor=segredo_emissor)
    return certificador.verificar_certificado(dados)


def gerar_e_verificar_demonstracao(caminho_saida: str | Path = "certificado_oficial_sha256.json") -> dict:
    """
    Executa uma demonstração completa de ponta a ponta:
    1. Simula a sessão de Proctoring íntegra;
    2. Executa o Avaliador Carrasco sobre a Calculadora;
    3. Emite e salva o certificado assinado com SHA-256;
    4. Valida criptograficamente o arquivo salvo.
    """
    sessao = SessaoProctoring(candidato="Wanderson Lopes da Silva")
    avaliador = AvaliadorCarrasco()
    resultado_exame = avaliador.executar_exame_completo(
        aluno="Wanderson Lopes da Silva",
        sessao_proctoring=sessao,
        cobertura_pct=100.0,
        taxa_mutacao_pct=100.0,
        crap_maximo=5.0,
    )
    caminho_salvo = avaliador.certificador.salvar_certificado(
        resultado_exame["certificado"], caminho_saida
    )
    valido, mensagem = validar_arquivo_certificado(caminho_salvo)
    return {
        "caminho_certificado": str(caminho_salvo),
        "valido": valido,
        "mensagem_verificacao": mensagem,
        "certificado": resultado_exame["certificado"],
    }


def main(argv: list[str] | None = None) -> int:
    argumentos = argv if argv is not None else sys.argv[1:]
    if argumentos:
        caminho = argumentos[0]
        valido, mensagem = validar_arquivo_certificado(caminho)
        print(f"[VERIFICAÇÃO SHA-256] Arquivo: {caminho}")
        print(f"[STATUS] {'APROVADO' if valido else 'REJEITADO'} — {mensagem}")
        return 0 if valido else 1

    resumo = gerar_e_verificar_demonstracao()
    cert = resumo["certificado"]
    print("=" * 72)
    print("VERIFICADOR DE CERTIFICADOS CRIPTOGRÁFICOS SHA-256 (GEMINI & ANTIGRAVITY)")
    print("=" * 72)
    print(f"Aluno Certificado : {cert['payload']['aluno']}")
    print(f"Curso             : {cert['payload']['curso']}")
    print(f"ID do Certificado : {cert['payload']['id_certificado']}")
    print(f"Nota Final        : {cert['payload']['nota_final']} / 100.0")
    print(f"Status Proctoring : {cert['payload']['status_proctoring']} (Penalidade: {cert['payload']['penalidade_proctoring']})")
    print(f"Hash Payload      : {cert['hash_payload_sha256']}")
    print(f"Assinatura SHA-256: {cert['assinatura_sha256']}")
    print(f"Código Público    : {cert['codigo_verificacao']}")
    print(f"Veredito Auditoria: {resumo['mensagem_verificacao']}")
    print("=" * 72)
    return 0 if resumo["valido"] else 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
