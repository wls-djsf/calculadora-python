# ============================================================
# TESTES DE ACEITAÇÃO BDD (GHERKIN + PYTEST-BDD)
# ============================================================
# [Termos Técnicos deste Módulo]
# - BDD (Behavior-Driven Development): Desenvolvimento Orientado ao Comportamento; metodologia
#   que descreve o comportamento do software em linguagem natural compreensível por humanos e máquinas.
# - Gherkin: Linguagem estruturada usada em arquivos '.feature' com palavras-chave como
#   Funcionalidade (Feature), Cenário (Scenario), Dado (Given), Quando (When), Então (Then) e E (And).
# - pytest-bdd: Plugin do pytest que conecta cenários Gherkin a funções reais em Python.
# - scenarios(...): Carrega e registra automaticamente todos os cenários do arquivo '.feature'.
# - @pytest.fixture: Define um recurso compartilhado (aqui, a instância da calculadora) injetado nos passos.
# - @given / @when / @then: Decoradores que vinculam os passos 'Dado', 'Quando' e 'Então' do arquivo
#   Gherkin às funções Python correspondentes.
# - parsers.parse(...): Extrai parâmetros entre chaves (como "{numero}" ou "{esperado}") diretamente
#   do texto em português do arquivo '.feature' e os entrega como variáveis para a função Python.
# ============================================================

from pathlib import Path
from types import SimpleNamespace
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from calculadora import Calculadora
from main import InterfaceCalculadora

CAMINHO_FEATURE = Path(__file__).parent / "features" / "calculadora.feature"
scenarios(str(CAMINHO_FEATURE))


@pytest.fixture
def contexto_app():
    """Fixture que fornece uma instância limpa da calculadora para cada cenário de aceitação."""
    return InterfaceCalculadora(root=None, calculadora=Calculadora())


@given("que a calculadora foi inicializada", target_fixture="contexto_app")
def inicializar_calculadora():
    """Passo 'Dado' (Given): garante o estado inicial limpo da calculadora."""
    return InterfaceCalculadora(root=None, calculadora=Calculadora())


@when(parsers.parse('o usuário insere o número "{numero}"'))
def usuario_insere_numero(contexto_app, numero):
    """Passo 'Quando' (When): simula a digitação de cada algarismo ou ponto decimal."""
    for caractere in numero:
        if caractere == ".":
            contexto_app.inserir_decimal()
        else:
            contexto_app.inserir_digito(caractere)


@when(parsers.parse('o usuário seleciona a operação "{operador}"'))
def usuario_seleciona_operacao(contexto_app, operador):
    """Passo 'Quando' (When): aciona o operador matemático selecionado."""
    contexto_app.selecionar_operador(operador)


@when(parsers.parse('o usuário pressiona "{botao}"'))
def usuario_pressiona_botao(contexto_app, botao):
    """Passo 'Quando' (When): simula o clique em um botão de ação (=, %, C, ⌫)."""
    contexto_app.pressionar_botao(botao)


@when(parsers.parse('o usuário digita a sequência de teclas "{sequencia}"'))
def usuario_digita_sequencia_teclas(contexto_app, sequencia):
    """Passo 'Quando' (When): simula o envio de eventos do teclado físico para a interface."""
    mapa_simbolos_tecla = {
        "+": "plus",
        "-": "minus",
        "*": "asterisk",
        "/": "slash",
        "=": "Return",
        ".": "period",
        ",": "comma",
    }
    for tecla in sequencia:
        simbolo = mapa_simbolos_tecla.get(tecla, tecla)
        contexto_app.processar_tecla(SimpleNamespace(char=tecla, keysym=simbolo))


@then(parsers.parse('o visor principal deve exibir "{esperado}"'))
def verificar_visor_principal(contexto_app, esperado):
    """Passo 'Então' (Then): verifica se o visor principal exibe o resultado esperado."""
    assert contexto_app.obter_visor() == esperado


@then('o visor de histórico deve exibir ""')
def verificar_visor_historico_vazio(contexto_app):
    """Passo 'Então' (Then): verifica se o visor superior de histórico está vazio."""
    assert contexto_app.obter_historico() == ""


@then(parsers.parse('o visor de histórico deve exibir "{esperado}"'))
def verificar_visor_historico(contexto_app, esperado):
    """Passo 'Então' (Then): verifica o conteúdo do visor superior de histórico."""
    assert contexto_app.obter_historico() == esperado
