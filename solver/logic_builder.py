"""
solver/logic_builder.py

Traduz cada template para uma
restrição lógica do Z3.

Este módulo evita que o
z3_solver.py fique cheio
de blocos if/else.
"""

from z3 import *


def build_constraint(
    variables,
    statement
):
    """
    Recebe:

    variables:

    {
        "Alice": Bool("Alice"),
        "Bob": Bool("Bob")
    }

    statement:

    {
        "speaker": "Alice",
        "target": "Bob",
        "template": "simple_knave"
    }

    Retorna uma expressão Z3.
    """

    speaker = variables[
        statement["speaker"]
    ]

    target = variables[
        statement["target"]
    ]

    template = statement[
        "template"
    ]

    # -----------------------------
    # Target é Knave
    # -----------------------------

    if template == "simple_knave":

        return (

            speaker

            ==

            (target == False)

        )

    # -----------------------------
    # Target é Knight
    # -----------------------------

    elif template == "simple_knight":

        return (

            speaker

            ==

            (target == True)

        )

    # -----------------------------
    # Mesmo papel
    # -----------------------------

    elif template == "same_role":

        return (

            speaker

            ==

            (speaker == target)

        )

    # -----------------------------
    # Papéis diferentes
    # -----------------------------

    elif template == "different_role":

        return (

            speaker

            ==

            (speaker != target)

        )

    raise Exception(
        f"Template desconhecido: {template}"
    )