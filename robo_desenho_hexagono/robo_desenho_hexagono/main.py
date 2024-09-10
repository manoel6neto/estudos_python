# coding: utf-8

import pyautogui
from time import sleep

# Constantes
PYAUTOGUI_PAUSE_PADRAO = 1
SLEEP_PADRAO = 2


def inicializando_pyautogui() -> None:
    """
    Função que inicializa os parâmetros importantes do pyautogui.
    :return: None
    """
    try:
        pyautogui.PAUSE = PYAUTOGUI_PAUSE_PADRAO
        pyautogui.FAILSAFE = True
    except Exception as ex:
        print(f"Erro ao inicializar o pyautogui: {ex}")


def principal() -> None:
    """
    Função principal que controla o fluxo do programa.
    :return: None
    """
    try:
        print("Iniciando o processamento...")

        # Inicializando o pyautogui
        inicializando_pyautogui()

        # Abrindo o menu iniciar para executar o paint
        pyautogui.hotkey("winleft")

        # Aguardando o Paint abrir
        sleep(SLEEP_PADRAO)

        # Buscando pelo Paint
        pyautogui.write("Paint")

        # Aguardando o Paint abrir
        sleep(SLEEP_PADRAO)

        # Abrindo o Paint
        pyautogui.press("enter")

        # Aguardando o Paint abrir
        sleep(SLEEP_PADRAO)

        # Fechando o Paint
        pyautogui.hotkey("alt", "f4")

        # Aguardando o Paint fechar
        sleep(SLEEP_PADRAO)

        print("Finalizado o processamento!!!")
    except Exception as ex:
        print(f"Erro ao executar o programa: {ex}")


if __name__ == '__main__':
    try:
        print("Iniciando o programa!!!")
        principal()
    except Exception as ex:
        print(f"Erro na inicialização do programa: {ex}")
    finally:
        print("Finalizando o programa!!!")
