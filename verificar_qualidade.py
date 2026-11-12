# ============================================================
# MÓDULO: VERIFICAR_QUALIDADE
# RESPONSABILIDADE: AUTOMAÇÃO DE TESTES, COBERTURA, MUTAÇÃO E MÉTRICAS (CRAP / RADON)
# ============================================================
# [Termos Técnicos deste Módulo]
# - ast (Abstract Syntax Tree / Árvore Sintática Abstrata): Módulo nativo do Python que transforma
#   o código-fonte em uma estrutura de árvore manipulável (usado aqui para gerar mutações reais).
# - subprocess: Módulo nativo para executar comandos externos de terminal e capturar suas saídas.
# - radon: Ferramenta de análise estática que mede:
#     * CC (Cyclomatic Complexity / Complexidade Ciclomática): Quantidade de caminhos lógicos independentes
#       em uma função (Notas de A a F, onde A = 1 a 5 indica código simples e de baixo risco).
#     * MI (Maintainability Index / Índice de Manutenibilidade): Pontuação de 0 a 100 que avalia
#       quão fácil é manter o código (Nota A = alta manutenibilidade).
#     * Raw (Métricas Brutas): LOC (Total de Linhas), LLOC (Linhas Lógicas) e SLOC (Linhas de Código sem comentários).
# - CRAP (Change Risk Anti-Patterns): Métrica criada por Alberto Savoia e Bob Evans (difundida por
#   Robert C. Martin / Uncle Bob) que combina Complexidade Ciclomática (CC) e Cobertura de Testes (cov):
#   CRAP(m) = CC^2 * (1 - cov/100)^3 + CC. Valores <= 12 indicam código seguro para manutenção.
# - coverage.py: Ferramenta que mede quais linhas (Statements) e desvios condicionais (Branches / Ramificações)
#   foram efetivamente executados pelos testes.
# - Teste de Mutação (Mutation Testing): Técnica que introduz pequenos defeitos artificiais (mutantes)
#   no código (ex.: trocar '+' por '-') para provar que os testes detectam o erro:
#     * KILLED (Eliminado): O teste falhou ao rodar com o código mutado (comportamento desejado: o teste detectou o defeito).
#     * SURVIVED (Sobrevivente): O teste passou mesmo com o código adulterado (indica fragilidade nos testes).
# ============================================================

import ast
import json
import subprocess
import sys
from pathlib import Path
from radon.complexity import cc_visit, cc_rank

RAIZ_PROJETO = Path(__file__).parent.resolve()


def executar_comando(comando, descricao):
    """
    Executa um comando em subprocesso e retorna (codigo_saida, saida_padrao, saida_erro).
    - stdout (Standard Output): Saída padrão de texto do comando.
    - stderr (Standard Error): Saída de mensagens de erro do comando.
    - returncode: Código numérico de encerramento (0 significa sucesso sem erros).
    """
    print(f"\n{'=' * 70}")
    print(f"[EXECUÇÃO] {descricao}")
    print(f"Comando: {' '.join(comando)}")
    print("=" * 70)
    resultado = subprocess.run(
        comando,
        cwd=str(RAIZ_PROJETO),
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    if resultado.stdout:
        print(resultado.stdout.strip())
    if resultado.stderr:
        print(resultado.stderr.strip())
    return resultado.returncode, resultado.stdout, resultado.stderr


def calcular_metricas_crap(arquivos_alvo, caminho_coverage_json):
    """Calcula a Complexidade Ciclomática (Radon CC) e a pontuação CRAP por função/método."""
    dados_cobertura = json.loads(Path(caminho_coverage_json).read_text(encoding="utf-8"))
    arquivos_cobertos = dados_cobertura.get("files", {})

    relatorio_crap = []
    for arquivo in arquivos_alvo:
        caminho_arq = RAIZ_PROJETO / arquivo
        codigo = caminho_arq.read_text(encoding="utf-8")
        blocos = cc_visit(codigo)

        info_cov = arquivos_cobertos.get(arquivo) or arquivos_cobertos.get(str(caminho_arq)) or {}
        linhas_executadas = set(info_cov.get("executed_lines", []))
        linhas_ausentes = set(info_cov.get("missing_lines", []))

        for bloco in blocos:
            # Ignorar o bloco agregador da classe e avaliar individualmente cada método/função
            if hasattr(bloco, "methods"):
                continue
            linhas_bloco = set(range(bloco.lineno, bloco.endline + 1))
            executadas_no_bloco = len(linhas_bloco & linhas_executadas)
            ausentes_no_bloco = len(linhas_bloco & linhas_ausentes)
            total_rastreado = executadas_no_bloco + ausentes_no_bloco
            cobertura_pct = (
                (executadas_no_bloco / total_rastreado) * 100.0 if total_rastreado > 0 else 100.0
            )
            complexidade = bloco.complexity
            pontuacao_crap = (complexidade ** 2) * ((1.0 - (cobertura_pct / 100.0)) ** 3) + complexidade
            nome_qualificado = (
                f"{bloco.classname}.{bloco.name}" if getattr(bloco, "classname", None) else bloco.name
            )
            relatorio_crap.append(
                {
                    "arquivo": arquivo,
                    "funcao": nome_qualificado,
                    "linhas": f"{bloco.lineno}-{bloco.endline}",
                    "complexidade": complexidade,
                    "rank_cc": cc_rank(complexidade),
                    "cobertura_pct": round(cobertura_pct, 2),
                    "crap": round(pontuacao_crap, 2),
                    "aprovado_crap": pontuacao_crap <= 12.0,
                }
            )
    return relatorio_crap


def gerar_mutantes_ast(codigo_fonte):
    """
    Gera mutantes sistemáticos sobre a Árvore Sintática Abstrata (AST) de calculadora.py nas 5 categorias:
    1. Substituição de operadores aritméticos (+ <-> -, * <-> /, -unário -> +unário)
    2. Alteração de operadores relacionais/identidade/pertinência (== <-> !=, is <-> is not, in <-> not in)
    3. Modificação de constantes numéricas (0 -> 1, 100 -> 101)
    4. Alteração de condições booleanas (or <-> and, remoção de not)
    5. Modificação de retornos (return expressao -> return None)
    """
    arvore_base = ast.parse(codigo_fonte)
    mutantes = []

    trocas_binop = {
        ast.Add: (ast.Sub, "+ -> -"),
        ast.Sub: (ast.Add, "- -> +"),
        ast.Mult: (ast.Div, "* -> /"),
        ast.Div: (ast.Mult, "/ -> *"),
    }
    trocas_comparacao = {
        ast.Eq: (ast.NotEq, "== -> !="),
        ast.NotEq: (ast.Eq, "!= -> =="),
        ast.Is: (ast.IsNot, "is -> is not"),
        ast.IsNot: (ast.Is, "is not -> is"),
        ast.In: (ast.NotIn, "in -> not in"),
        ast.NotIn: (ast.In, "not in -> in"),
    }
    trocas_booleanas = {
        ast.Or: (ast.And, "or -> and"),
        ast.And: (ast.Or, "and -> or"),
    }

    nos_base = list(ast.walk(arvore_base))
    for indice_no, no in enumerate(nos_base):
        # 1a. Operadores aritméticos binários (BinOp)
        if isinstance(no, ast.BinOp) and type(no.op) in trocas_binop:
            nova_classe_op, descricao = trocas_binop[type(no.op)]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = nova_classe_op()
            mutantes.append((no.lineno, "Operador Aritmético", descricao, ast.unparse(copia)))

        # 1b. Operador unário de inversão de sinal (UnaryOp USub -> UAdd)
        elif isinstance(no, ast.UnaryOp) and isinstance(no.op, ast.USub):
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = ast.UAdd()
            mutantes.append((no.lineno, "Operador Unário", "-x -> +x", ast.unparse(copia)))

        # 2. Operadores relacionais, identidade e pertinência (Compare)
        elif isinstance(no, ast.Compare) and len(no.ops) == 1 and type(no.ops[0]) in trocas_comparacao:
            nova_classe_cmp, descricao = trocas_comparacao[type(no.ops[0])]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.ops[0] = nova_classe_cmp()
            mutantes.append((no.lineno, "Operador Relacional", descricao, ast.unparse(copia)))

        # 3. Modificação de constantes numéricas (Constant: 0 -> 1, 100 -> 101)
        elif isinstance(no, ast.Constant) and type(no.value) is int and no.value in (0, 100):
            novo_valor = no.value + 1
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.value = novo_valor
            mutantes.append(
                (no.lineno, "Constante Numérica", f"{no.value} -> {novo_valor}", ast.unparse(copia))
            )

        # 4a. Condições booleanas (BoolOp: or <-> and)
        elif isinstance(no, ast.BoolOp) and type(no.op) in trocas_booleanas:
            nova_classe_bool, descricao = trocas_booleanas[type(no.op)]
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.op = nova_classe_bool()
            mutantes.append((no.lineno, "Condição Booleana", descricao, ast.unparse(copia)))

        # 4b. Negação booleana (not expressao -> expressao)
        elif isinstance(no, ast.UnaryOp) and isinstance(no.op, ast.Not):
            copia = ast.parse(codigo_fonte)
            for pai in ast.walk(copia):
                for campo, valor_campo in ast.iter_fields(pai):
                    if (
                        isinstance(valor_campo, ast.UnaryOp)
                        and isinstance(valor_campo.op, ast.Not)
                        and valor_campo.lineno == no.lineno
                    ):
                        setattr(pai, campo, valor_campo.operand)
                        mutantes.append(
                            (no.lineno, "Condição Booleana", "not expr -> expr", ast.unparse(copia))
                        )
                        break

        # 5. Modificação de retornos (Return: return expressao -> return None)
        elif isinstance(no, ast.Return) and no.value is not None:
            copia = ast.parse(codigo_fonte)
            alvo = list(ast.walk(copia))[indice_no]
            alvo.value = ast.Constant(value=None)
            mutantes.append(
                (no.lineno, "Modificação de Retorno", "return expr -> return None", ast.unparse(copia))
            )

    return mutantes


def executar_testes_mutacao():
    """Executa a bateria de testes de mutação sobre calculadora.py e restaura o código original."""
    caminho_calc = RAIZ_PROJETO / "calculadora.py"
    codigo_original = caminho_calc.read_text(encoding="utf-8")
    mutantes = gerar_mutantes_ast(codigo_original)

    resultados = []
    eliminados = 0
    sobreviventes = 0

    print(f"\n{'=' * 70}")
    print(f"[MUTAÇÃO] Executando {len(mutantes)} mutações sobre calculadora.py...")
    print("=" * 70)

    try:
        for indice, (linha, categoria, descricao, codigo_mutado) in enumerate(mutantes, start=1):
            caminho_calc.write_text(codigo_mutado, encoding="utf-8")
            processo = subprocess.run(
                [sys.executable, "-m", "pytest", "tests/test_calculadora.py", "-q", "--tb=no"],
                cwd=str(RAIZ_PROJETO),
                capture_output=True,
                text=True,
            )
            morto = processo.returncode != 0
            status = "ELIMINADO (KILLED)" if morto else "SOBREVIVENTE (SURVIVED)"
            if morto:
                eliminados += 1
            else:
                sobreviventes += 1
            print(f"  Mutante #{indice:02d} | Linha {linha:03d} | {categoria:<22} | {descricao:<26} -> {status}")
            resultados.append(
                {
                    "id": indice,
                    "linha": linha,
                    "categoria": categoria,
                    "descricao": descricao,
                    "status": status,
                    "eliminado": morto,
                }
            )
    finally:
        caminho_calc.write_text(codigo_original, encoding="utf-8")

    total = len(mutantes)
    taxa = (eliminados / total * 100.0) if total > 0 else 100.0
    print("-" * 70)
    print(
        f"Resumo de Mutação: Total={total} | Eliminados={eliminados} | "
        f"Sobreviventes={sobreviventes} | Taxa de Mutação={taxa:.2f}%"
    )
    return {
        "total": total,
        "eliminados": eliminados,
        "sobreviventes": sobreviventes,
        "taxa_mutacao_pct": round(taxa, 2),
        "mutantes": resultados,
    }


def main():
    # 1. Testes Unitários (unittest + pytest)
    cod_unitario_ut, _, _ = executar_comando(
        [sys.executable, "-m", "unittest", "tests/test_calculadora.py", "-v"],
        "1A. Testes Unitários (unittest)",
    )
    cod_unitario_pt, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_calculadora.py", "-v"],
        "1B. Testes Unitários Parametrizados (pytest)",
    )

    # 2. Testes de Aceitação (BDD / Gherkin)
    cod_bdd, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_bdd_calculadora.py", "-v"],
        "2. Testes de Aceitação BDD (Gherkin / pytest-bdd)",
    )

    # 3. Testes de Integração
    cod_integracao, _, _ = executar_comando(
        [sys.executable, "-m", "pytest", "tests/test_interface.py", "-v"],
        "3. Testes de Integração (main.py <-> calculadora.py)",
    )

    # 4. Cobertura de Linhas e Ramificações (Coverage)
    executar_comando(
        [
            sys.executable,
            "-m",
            "coverage",
            "run",
            "--branch",
            "--source=calculadora,main",
            "-m",
            "pytest",
        ],
        "4A. Execução da Suíte Completa com Coverage (Linhas e Ramificações)",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "report", "-m"],
        "4B. Relatório Textual de Cobertura",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "html"],
        "4C. Geração de Relatório HTML de Cobertura (htmlcov/)",
    )
    executar_comando(
        [sys.executable, "-m", "coverage", "json"],
        "4D. Exportação JSON de Cobertura (coverage.json)",
    )

    # 5. Análise de Complexidade (Radon) e Métrica CRAP
    executar_comando(
        [sys.executable, "-m", "radon", "cc", "calculadora.py", "main.py", "-s", "-a"],
        "5A. Complexidade Ciclomática (Radon CC)",
    )
    executar_comando(
        [sys.executable, "-m", "radon", "mi", "calculadora.py", "main.py", "-s"],
        "5B. Índice de Manutenibilidade (Radon MI)",
    )
    executar_comando(
        [sys.executable, "-m", "radon", "raw", "calculadora.py", "main.py", "-s"],
        "5C. Métricas Brutas de Tamanho de Código (Radon Raw)",
    )

    relatorio_crap = calcular_metricas_crap(
        ["calculadora.py", "main.py"], RAIZ_PROJETO / "coverage.json"
    )
    print(f"\n{'=' * 70}")
    print("[MÉTRICA CRAP] Relatório por Função/Método (Referência: CRAP <= 12)")
    print("=" * 70)
    print(f"{'Arquivo':<16} | {'Função/Método':<36} | {'CC':>3} | {'Cob(%)':>7} | {'CRAP':>6} | {'Status'}")
    print("-" * 85)
    for item in relatorio_crap:
        status_str = "OK (<=12)" if item["aprovado_crap"] else "ACIMA (>12)"
        print(
            f"{item['arquivo']:<16} | {item['funcao']:<36} | {item['complexidade']:>3} | "
            f"{item['cobertura_pct']:>6.1f}% | {item['crap']:>6.2f} | {status_str}"
        )

    # 6. Testes de Mutação
    resumo_mutacao = executar_testes_mutacao()

    # Salvar resumo consolidado em JSON
    resumo_geral = {
        "crap": relatorio_crap,
        "mutacao": resumo_mutacao,
    }
    (RAIZ_PROJETO / "relatorio_metricas.json").write_text(
        json.dumps(resumo_geral, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    falhas = any(
        codigo != 0 for codigo in (cod_unitario_ut, cod_unitario_pt, cod_bdd, cod_integracao)
    ) or (resumo_mutacao["sobreviventes"] > 0)
    return 1 if falhas else 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
