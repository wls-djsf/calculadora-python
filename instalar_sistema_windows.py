# ============================================================
# MÓDULO: INSTALAR_SISTEMA_WINDOWS
# RESPONSABILIDADE: INSTALAR EXECUTÁVEIS (.EXE) NO WINDOWS, MENU INICIAR E DESKTOP
# ============================================================
# [Termos Técnicos deste Módulo]
# - LOCALAPPDATA / APPDATA / USERPROFILE: Variáveis de ambiente padrão do Windows que apontam
#   para as pastas de programas locais, Menu Iniciar e perfil do usuário atual.
# - WScript.Shell (CreateShortcut): Objeto COM nativo do Windows Script Host utilizado para
#   gerar arquivos binários de atalho (.lnk) com ícone personalizado.
# - winreg (HKEY_CURRENT_USER): Módulo nativo do Python para registrar o aplicativo na lista
#   de "Aplicativos Instalados" do Windows sem exigir privilégios de Administrador da máquina.
# ============================================================

import os
import shutil
import subprocess
import winreg
from pathlib import Path

RAIZ_PROJETO = Path(__file__).parent.resolve()
ICO_ORIGEM = RAIZ_PROJETO / "calculadora.ico"

PASTA_INSTALACAO = Path(os.environ.get("LOCALAPPDATA", str(RAIZ_PROJETO))) / "Programs" / "CalculadoraPython"
MENU_INICIAR_PROGRAMAS = (
    Path(os.environ.get("APPDATA", str(RAIZ_PROJETO)))
    / "Microsoft"
    / "Windows"
    / "Start Menu"
    / "Programs"
)
AREA_DE_TRABALHO = Path(os.environ.get("USERPROFILE", str(RAIZ_PROJETO))) / "Desktop"


def criar_atalho_windows(
    caminho_lnk: Path, destino_exe: Path, pasta_trabalho: Path, icone: Path, descricao: str
):
    """Cria um atalho nativo do Windows (.lnk) usando VBScript via cscript."""
    vbs_path = PASTA_INSTALACAO / "criar_atalho_temp.vbs"
    conteudo_vbs = (
        'Set oWS = WScript.CreateObject("WScript.Shell")\r\n'
        f'Set oLink = oWS.CreateShortcut("{caminho_lnk}")\r\n'
        f'oLink.TargetPath = "{destino_exe}"\r\n'
        f'oLink.WorkingDirectory = "{pasta_trabalho}"\r\n'
        f'oLink.IconLocation = "{icone}, 0"\r\n'
        f'oLink.Description = "{descricao}"\r\n'
        'oLink.Save\r\n'
    )
    vbs_path.write_text(conteudo_vbs, encoding="mbcs")
    try:
        subprocess.run(["cscript", "//NoLogo", str(vbs_path)], check=True)
    finally:
        if vbs_path.exists():
            vbs_path.unlink()


def registrar_no_windows(
    id_chave: str, nome_exibicao: str, exe_instalado: Path, ico_instalado: Path, atalho_iniciar: Path
):
    """Registra o executável na chave Uninstall do usuário atual (HKCU) do Windows."""
    chave_caminho = rf"Software\Microsoft\Windows\CurrentVersion\Uninstall\{id_chave}"
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, chave_caminho) as key:
        winreg.SetValueEx(key, "DisplayName", 0, winreg.REG_SZ, nome_exibicao)
        winreg.SetValueEx(key, "DisplayIcon", 0, winreg.REG_SZ, str(ico_instalado))
        winreg.SetValueEx(key, "InstallLocation", 0, winreg.REG_SZ, str(PASTA_INSTALACAO))
        winreg.SetValueEx(key, "Publisher", 0, winreg.REG_SZ, "Parceria Gemini & Antigravity")
        winreg.SetValueEx(key, "DisplayVersion", 0, winreg.REG_SZ, "2.0.0")
        winreg.SetValueEx(key, "NoModify", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(key, "NoRepair", 0, winreg.REG_DWORD, 1)
        cmd_uninstall = f'cmd.exe /c del /f /q "{exe_instalado}" & del /f /q "{atalho_iniciar}"'
        winreg.SetValueEx(key, "UninstallString", 0, winreg.REG_SZ, cmd_uninstall)


def instalar_aplicativos():
    """Instala a Calculadora Python e o Sistema de Educação no Windows, Menu Iniciar e Desktop."""
    PASTA_INSTALACAO.mkdir(parents=True, exist_ok=True)
    ico_instalado = PASTA_INSTALACAO / "calculadora.ico"
    if ICO_ORIGEM.exists():
        shutil.copy2(ICO_ORIGEM, ico_instalado)

    aplicativos = [
        (
            "Calculadora Python.exe",
            "Calculadora Python",
            "CalculadoraPython",
            "Calculadora Gráfica em Python (Tema Roxo e Lavanda)",
        ),
        (
            "Sistema Educacao Calculadora.exe",
            "Sistema Educacao Calculadora Python",
            "SistemaEducacaoCalculadoraPython",
            "Sistema de Educação, Proctoring Simulado e Certificação SHA-256",
        ),
    ]

    for nome_exe, nome_atalho, id_registro, descricao in aplicativos:
        exe_dist = RAIZ_PROJETO / "dist" / nome_exe
        exe_raiz = RAIZ_PROJETO / nome_exe
        origem = exe_dist if exe_dist.exists() else exe_raiz
        if not origem.exists():
            continue

        # Garantir cópia na raiz do projeto e na pasta de instalação do Windows
        if exe_dist.exists():
            shutil.copy2(exe_dist, exe_raiz)
        exe_instalado = PASTA_INSTALACAO / nome_exe
        shutil.copy2(origem, exe_instalado)

        atalho_menu = MENU_INICIAR_PROGRAMAS / f"{nome_atalho}.lnk"
        criar_atalho_windows(atalho_menu, exe_instalado, PASTA_INSTALACAO, ico_instalado, descricao)

        atalho_desktop = AREA_DE_TRABALHO / f"{nome_atalho}.lnk"
        if AREA_DE_TRABALHO.exists():
            criar_atalho_windows(
                atalho_desktop, exe_instalado, PASTA_INSTALACAO, ico_instalado, descricao
            )

        registrar_no_windows(id_registro, nome_atalho, exe_instalado, ico_instalado, atalho_menu)
        print(f"[OK] Instalado: {exe_instalado} (Existe: {exe_instalado.exists()})")
        print(f"[OK] Menu Iniciar: {atalho_menu} (Existe: {atalho_menu.exists()})")
        if atalho_desktop.exists():
            print(f"[OK] Desktop: {atalho_desktop} (Existe: {atalho_desktop.exists()})")


if __name__ == "__main__":  # pragma: no cover
    instalar_aplicativos()
