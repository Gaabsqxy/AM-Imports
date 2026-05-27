import builtins
import os
import sys
import time

ORIGINAL_PRINT = builtins.print
ORIGINAL_INPUT = builtins.input
TYPING_DELAY = 0.003
VISUAL_MODE_ENABLED = False


def slow_write(text, delay=None):
    if delay is None:
        delay = TYPING_DELAY
    if os.getenv("AM_FAST_MODE") == "1":
        sys.stdout.write(str(text))
        sys.stdout.flush()
        return
    for char in str(text):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)


def slow_print(*values, sep=" ", end="\n", file=None, flush=False):
    if file not in (None, sys.stdout):
        ORIGINAL_PRINT(*values, sep=sep, end=end, file=file, flush=flush)
        return
    text = sep.join(str(value) for value in values) + end
    slow_write(text)
    if flush:
        sys.stdout.flush()


def slow_input(message=""):
    if message:
        slow_write(message)
    return ORIGINAL_INPUT("")


def enable_visual_mode(delay=0.003):
    global TYPING_DELAY, VISUAL_MODE_ENABLED
    TYPING_DELAY = delay
    if not VISUAL_MODE_ENABLED:
        builtins.print = slow_print
        builtins.input = slow_input
        VISUAL_MODE_ENABLED = True


def disable_visual_mode():
    global VISUAL_MODE_ENABLED
    builtins.print = ORIGINAL_PRINT
    builtins.input = ORIGINAL_INPUT
    VISUAL_MODE_ENABLED = False


def clear_screen():
    if os.name != "nt" and not os.getenv("TERM"):
        ORIGINAL_PRINT("\n" * 40)
        return
    os.system("cls" if os.name == "nt" else "clear")


def money(value):
    formatted = f"R$ {value:,.2f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def divider(size=64):
    print("═" * size)


def title(text):
    divider()
    print(text.center(64))
    divider()


def subtitle(text):
    print()
    print(text.center(64))
    print("─" * 64)


def pause():
    input("\nPressione Enter para continuar...")


def read_int(message, min_value=None, max_value=None):
    while True:
        try:
            value = int(input(message))
            if min_value is not None and value < min_value:
                print(f"Digite um número maior ou igual a {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Digite um número menor ou igual a {max_value}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


def read_float(message, min_value=None):
    while True:
        try:
            value = float(input(message).replace(",", "."))
            if min_value is not None and value < min_value:
                print(f"Digite um valor maior ou igual a {min_value}.")
                continue
            return value
        except ValueError:
            print("Entrada inválida. Digite um valor numérico.")


def ask_non_empty(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        print("Este campo não pode ficar vazio.")
