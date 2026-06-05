"""
puzzles/generator.py

Responsável pela geração dos puzzles.

A nova versão suporta múltiplas premissas.

Exemplo:

Alice says:
"Bob is a knave."

Bob says:
"Carol is a knight."

Carol says:
"Alice and I are different."
"""

import random

from config import (
    NUMBER_OF_PREMISES,
    NUMBER_OF_CHARACTERS
)

from puzzles.templates import (
    AVAILABLE_TEMPLATES
)


# ==========================================================
# LISTA DE PERSONAGENS
# ==========================================================

ALL_CHARACTERS = [

    "Alice",

    "Bob",

    "Carol",

    "Dave",

    "Eve",

    "Frank",

    "Grace",

    "Henry"

]


def choose_characters():
    """
    Seleciona os personagens
    que participarão do puzzle.

    A quantidade é definida
    no arquivo config.py.
    """

    return random.sample(

        ALL_CHARACTERS,

        NUMBER_OF_CHARACTERS

    )


def choose_template():
    """
    Escolhe um template
    aleatoriamente.
    """

    return random.choice(

        AVAILABLE_TEMPLATES

    )


def choose_speaker_target(
    characters
):
    """
    Escolhe dois personagens distintos.

    Um será o speaker.

    Outro será o target.
    """

    return random.sample(

        characters,

        2

    )


def build_statement_text(
    speaker,
    target,
    template
):
    """
    Constrói o texto
    correspondente à premissa.
    """

    template_id = template["id"]

    if template_id == "simple_knave":

        return (

            f'{speaker} says:\n'

            f'"{target} is a knave."'

        )

    elif template_id == "simple_knight":

        return (

            f'{speaker} says:\n'

            f'"{target} is a knight."'

        )

    elif template_id == "same_role":

        return (

            f'{speaker} says:\n'

            f'"{target} and I are the same."'

        )

    elif template_id == "different_role":

        return (

            f'{speaker} says:\n'

            f'"{target} and I are different."'

        )

    raise Exception(

        "Template desconhecido."

    )


def generate_statement(
    characters
):
    """
    Gera uma única premissa.
    """

    speaker, target = (

        choose_speaker_target(

            characters

        )

    )

    template = (

        choose_template()

    )

    return {

        "speaker": speaker,

        "target": target,

        "template": template["id"]

    }


def build_puzzle_text(
    statements
):
    """
    Junta todas as premissas
    em um único texto.
    """

    lines = []

    for statement in statements:

        template = {

            "id":
            statement["template"]

        }

        line = build_statement_text(

            statement["speaker"],

            statement["target"],

            template

        )

        lines.append(

            line

        )

    return "\n\n".join(

        lines

    )


def generate_puzzle(
    number_of_premises=
    NUMBER_OF_PREMISES
):
    """
    Função principal do módulo.

    Retorna uma estrutura completa
    do puzzle.

    Exemplo:

    {

        "characters": [...],

        "statements": [...],

        "text": "..."

    }
    """

    characters = (

        choose_characters()

    )

    statements = []

    for _ in range(

        number_of_premises

    ):

        statements.append(

            generate_statement(

                characters

            )

        )

    puzzle_text = (

        build_puzzle_text(

            statements

        )

    )

    return {

        "characters":

            characters,

        "statements":

            statements,

        "text":

            puzzle_text

    }