"""
puzzles/templates.py

Este arquivo contém todos os templates
que podem ser utilizados pelo gerador.

Cada template possui:

- id
- descrição

O solver utilizará o campo "id"
para decidir qual fórmula lógica
deverá ser criada.
"""

# ==========================================================
# TEMPLATE:
# TARGET É KNAVE
# ==========================================================

SIMPLE_KNAVE = {

    "id": "simple_knave",

    "description":
        "Speaker afirma que o alvo é Knave."

}


# ==========================================================
# TEMPLATE:
# TARGET É KNIGHT
# ==========================================================

SIMPLE_KNIGHT = {

    "id": "simple_knight",

    "description":
        "Speaker afirma que o alvo é Knight."

}


# ==========================================================
# TEMPLATE:
# MESMO PAPEL
# ==========================================================

SAME_ROLE = {

    "id": "same_role",

    "description":
        "Speaker afirma que possui o mesmo papel do alvo."

}


# ==========================================================
# TEMPLATE:
# PAPÉIS DIFERENTES
# ==========================================================

DIFFERENT_ROLE = {

    "id": "different_role",

    "description":
        "Speaker afirma que possui papel diferente do alvo."

}


# ==========================================================
# LISTA DE TEMPLATES DISPONÍVEIS
# ==========================================================

AVAILABLE_TEMPLATES = [

    SIMPLE_KNAVE,

    SIMPLE_KNIGHT,

    SAME_ROLE,

    DIFFERENT_ROLE

]