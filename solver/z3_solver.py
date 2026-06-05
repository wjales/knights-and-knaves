"""
solver/z3_solver.py

Responsável por resolver os puzzles
utilizando o SMT Solver Z3.

Fluxo:

1) Cria uma variável booleana para cada personagem.
2) Traduz cada premissa para lógica.
3) Adiciona todas as restrições ao solver.
4) Enumera TODAS as soluções possíveis.
5) Classifica o problema.

Classificações:

UNIQUE:
    Existe apenas uma solução.

AMBIGUOUS:
    Existem duas ou mais soluções.

UNSAT:
    Não existe solução.
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from z3 import *

from solver.logic_builder import (
    build_constraint
)


# ==========================================================
# CRIA VARIÁVEIS DOS PERSONAGENS
# ==========================================================

def create_variables(
    characters
):
    """
    Cria uma variável booleana
    para cada personagem.

    Exemplo:

    Alice -> Bool("Alice")
    Bob   -> Bool("Bob")

    Convenção:

    True  = Knight
    False = Knave
    """

    variables = {}

    for character in characters:

        variables[
            character
        ] = Bool(
            character
        )

    return variables


# ==========================================================
# ADICIONA TODAS AS PREMISSAS
# ==========================================================

def add_constraints(

    solver,

    variables,

    statements

):
    """
    Percorre todas as premissas
    do puzzle.

    Para cada uma delas:

    - cria a fórmula lógica;
    - adiciona ao solver.
    """

    for statement in statements:

        constraint = (

            build_constraint(

                variables,

                statement

            )

        )

        solver.add(

            constraint

        )


# ==========================================================
# CONVERTE MODELO DO Z3
# ==========================================================

def model_to_dictionary(

    model,

    variables

):
    """
    Converte um modelo Z3
    para um dicionário Python.

    Exemplo:

    {

        "Alice": True,

        "Bob": False

    }
    """

    result = {}

    for person in variables:

        value = model.evaluate(

            variables[
                person
            ],

            model_completion=True

        )

        result[
            person
        ] = bool(
            value
        )

    return result


# ==========================================================
# BLOQUEIA MODELO ATUAL
# ==========================================================

def block_current_solution(

    solver,

    model,

    variables

):
    """
    Impede que o solver
    encontre novamente
    o mesmo modelo.

    Técnica clássica
    de enumeração.
    """

    block = []

    for person in variables:

        block.append(

            variables[
                person
            ]

            !=

            model.evaluate(

                variables[
                    person
                ],

                model_completion=True

            )

        )

    solver.add(

        Or(
            block
        )

    )


# ==========================================================
# ENUMERA TODAS AS SOLUÇÕES
# ==========================================================

def enumerate_solutions(

    solver,

    variables

):
    """
    Procura todos os modelos
    possíveis.

    Retorna:

    [

        {
            ...
        },

        {
            ...
        }

    ]
    """

    solutions = []

    while solver.check() == sat:

        model = solver.model()

        solution = (

            model_to_dictionary(

                model,

                variables

            )

        )

        solutions.append(

            solution

        )

        block_current_solution(

            solver,

            model,

            variables

        )

    return solutions


# ==========================================================
# CLASSIFICA RESULTADO
# ==========================================================

def classify_result(
    solutions
):
    """
    Define o tipo do puzzle.
    """

    total = len(
        solutions
    )

    if total == 0:

        return "UNSAT"

    elif total == 1:

        return "UNIQUE"

    else:

        return "AMBIGUOUS"


# ==========================================================
# CALCULA FATOS NECESSÁRIOS
# ==========================================================

def calculate_forced_values(
    solutions
):
    """
    Descobre quais personagens
    possuem o mesmo valor
    em todas as soluções.

    Exemplo:

    Solução 1

    Alice=True
    Bob=False

    Solução 2

    Alice=True
    Bob=True

    Resultado:

    Alice -> True
    Bob -> Indefinido
    """

    if len(
        solutions
    ) == 0:

        return {}

    forced = {}

    first = solutions[0]

    for person in first:

        value = first[
            person
        ]

        same = True

        for solution in solutions:

            if (

                solution[
                    person
                ]

                !=

                value

            ):

                same = False

                break

        if same:

            forced[
                person
            ] = value

        else:

            forced[
                person
            ] = None

    return forced


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def solve_puzzle(
    puzzle
):
    """
    Resolve um puzzle completo.

    Entrada:

    {

        "characters": [...],

        "statements": [...]

    }

    Retorna:

    {

        "status":

            "UNIQUE",

        "solutions":

            [...],

        "forced_values":

            {...},

        "number_of_solutions":

            1

    }
    """

    solver = Solver()

    # ----------------------------------
    # Cria variáveis
    # ----------------------------------

    variables = (

        create_variables(

            puzzle[
                "characters"
            ]

        )

    )

    # ----------------------------------
    # Adiciona premissas
    # ----------------------------------

    add_constraints(

        solver,

        variables,

        puzzle[
            "statements"
        ]

    )

    # ----------------------------------
    # Procura todas as soluções
    # ----------------------------------

    solutions = (

        enumerate_solutions(

            solver,

            variables

        )

    )

    # ----------------------------------
    # Classificação
    # ----------------------------------

    status = (

        classify_result(

            solutions

        )

    )

    # ----------------------------------
    # Valores obrigatórios
    # ----------------------------------

    forced_values = (

        calculate_forced_values(

            solutions

        )

    )

    # ----------------------------------
    # Resultado final
    # ----------------------------------

    return {

        "status":

            status,

        "solutions":

            solutions,

        "forced_values":

            forced_values,

        "number_of_solutions":

            len(
                solutions
            )

    }