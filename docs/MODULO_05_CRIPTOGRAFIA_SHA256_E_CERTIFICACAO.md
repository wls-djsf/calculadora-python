# Módulo 05 — Criptografia SHA-256 e Validação Antifraude de Certificados

O encerramento do curso e do exame supervisionado culmina na emissão de um **Certificado Digital Criptografado** (`src/certificador_sha256.py`) auditável de forma independente pelo script de linha de comando `verify_certificate.py`.

---

## 1. Fundamentos do Algoritmo Criptográfico SHA-256

O **SHA-256** (*Secure Hash Algorithm — 256 bits*), integrante da família **SHA-2** padronizada pelo NIST (FIPS 180-4), transforma qualquer volume de bytes em uma impressão digital única de **256 bits** (representada por **64 caracteres hexadecimais**):

1. **Determinístico:** A mesma entrada produz sempre exatamente o mesmo *hash*.
2. **Unidirecional (Função de Mão Única):** É computacionalmente inviável reverter o *hash* para descobrir os dados originais.
3. **Efeito Avalanche:** A alteração de um único caractere ou bit no certificado (ex.: mudar a nota de `95.0` para `95.1` ou alterar uma letra do nome do aluno) muda radicalmente cerca de 50% de todos os bits do *hash* resultante.
4. **Resistência a Colisão:** É impraticável encontrar dois documentos diferentes que produzam o mesmo *hash* SHA-256 ($2^{256}$ combinações possíveis).

---

## 2. Arquitetura de Dupla Camada: Payload Canônico + Assinatura SHA-256

Para evitar que um usuário mal-intencionado edite o arquivo JSON do certificado e simplesmente recalcule um SHA-256 simples por conta própria, nosso motor `CertificadorSHA256` implementa:

1. **Serialização Canônica Determinística:**
   Os campos essenciais do certificado (`id_certificado`, `aluno`, `curso`, `nota_final`, `taxa_mutacao_pct`, `cobertura_pct`, `crap_maximo`, `status_proctoring`, `penalidade_proctoring`, `emitido_em_utc`) são ordenados alfabeticamente (`sort_keys=True`) e compactados sem espaços ambíguos.
2. **Hash de Integridade do Payload (`hash_payload_sha256`):**
   $$\text{H}_{\text{payload}} = \text{SHA256}(\text{JSON\_Canônico})$$
3. **Assinatura Criptográfica Salgada (`assinatura_sha256`):**
   Combina o *hash* do *payload* com o segredo/sal criptográfico do emissor (`CHAVE_EMISSOR_PADRAO`) via `hashlib.sha256` e `hmac.compare_digest` (comparação em tempo constante imune a *Timing Attacks*):
   $$\text{Assinatura} = \text{SHA256}(\text{H}_{\text{payload}} \parallel \text{"::"} \parallel \text{Segredo\_Emissor})$$

---

## 3. Regras de Emissão e Verificação (`verify_certificate.py`)

O motor **recusa** a emissão do certificado (`ErroCertificacaoReprovada`) se qualquer uma das condições abaixo falhar:
- Nota técnica no exame $< 80.0$;
- Cobertura de código $< 95.0\%$;
- Taxa de mutação $< 100.0\%$;
- Pontuação CRAP máxima $> 12.0$;
- Sessão de Proctoring com status `ELIMINADO_POR_FRAUDE` ou não íntegra.

O validador `verify_certificate.py` lê qualquer certificado JSON, recalcula o `hash_payload_sha256` e a `assinatura_sha256` usando `hmac.compare_digest`, verifica se todos os índices de qualidade atendem às exigências mínimas e retorna o veredito de autenticidade (`CERTIFICADO AUTÊNTICO E VÁLIDO` ou `ALERTA DE FALSIFICAÇÃO / ADULTERAÇÃO DETECTADA`).
