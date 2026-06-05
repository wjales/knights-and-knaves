"""
puzzles/formatter.py

Responsável por converter a estrutura interna
do puzzle em texto legível para humanos.

Este módulo NÃO resolve lógica.
Ele apenas transforma os objetos
em frases.
"""


def format_statement(statement):
    """
    Converte uma premissa para texto.

    Entrada:

    {
        "speaker": "Alice",
        "target": "Bob",
        "template": "simple_knave"
    }
    """

    speaker = statement["speaker"]
    target = statement["target"]
    template = statement["template"]

    if template == "simple_knave":

        return (
            f'{speaker} says:\n'
            f'"{target} is a knave."'
        )

    elif template == "simple_knight":

        return (
            f'{speaker} says:\n'
            f'"{target} is a knight."'
        )

    elif template == "same_role":

        return (
            f'{speaker} says:\n'
            f'"{target} and I are the same."'
        )

    elif template == "different_role":

        return (
            f'{speaker} says:\n'
            f'"{target} and I are different."'
        )

    raise Exception(
        f"Template desconhecido: {template}"
    )


def format_puzzle(puzzle):
    """
    Converte um puzzle inteiro para texto.

    Entrada:

    {
        "characters": [...],
        "statements": [...]
    }

    Saída:

    Alice says:
    "Bob is a knave."

    Bob says:
    "Carol is a knight."
    """

    lines = []

    for statement in puzzle["statements"]:

        lines.append(
            format_statement(
                statement
            )
        )

    return "\n\n".join(
        lines
    )