"""
solver/explain_solver.py

Responsável por apresentar ao usuário
uma explicação amigável do resultado
produzido pelo Z3.

Este módulo não resolve o problema.

Ele apenas recebe o resultado do solver
e organiza as informações de forma
mais compreensível.
"""


# ==========================================================
# CONVERTE BOOLEANO EM TEXTO
# ==========================================================

def role_name(value):
    """
    Converte o valor booleano
    para o papel correspondente.

    True  -> Knight
    False -> Knave
    """

    if value:

        return "Knight"

    return "Knave"


# ==========================================================
# EXIBE AS PREMISSAS
# ==========================================================

def print_statements(
    puzzle
):
    """
    Mostra todas as premissas
    utilizadas pelo solver.
    """

    print()

    print("=" * 60)
    print("PREMISSAS")
    print("=" * 60)

    print()

    print(
        puzzle["text"]
    )

    print()


# ==========================================================
# EXIBE UMA SOLUÇÃO
# ==========================================================

def print_solution(
    solution,
    number
):
    """
    Exibe uma solução individual.
    """

    print()

    print(
        f"SOLUÇÃO {number}"
    )

    print("-" * 30)

    for person in sorted(
        solution.keys()
    ):

        print(

            f"{person:<10}"

            f": "

            f"{role_name(solution[person])}"

        )

    print()


# ==========================================================
# EXIBE TODOS OS MODELOS
# ==========================================================

def print_all_solutions(
    result
):
    """
    Percorre todas as soluções
    encontradas pelo Z3.
    """

    for index, solution in enumerate(

        result[
            "solutions"
        ],

        start=1

    ):

        print_solution(

            solution,

            index

        )


# ==========================================================
# EXIBE VALORES OBRIGATÓRIOS
# ==========================================================

def print_forced_values(
    result
):
    """
    Exibe quais personagens
    possuem papel fixo
    em todas as soluções.
    """

    print()

    print("=" * 60)
    print("VALORES OBRIGATÓRIOS")
    print("=" * 60)

    print()

    forced = result[
        "forced_values"
    ]

    for person in sorted(

        forced.keys()

    ):

        value = forced[
            person
        ]

        if value is None:

            print(

                f"{person:<10}"

                f": "

                f"INDEFINIDO"

            )

        else:

            print(

                f"{person:<10}"

                f": "

                f"{role_name(value)}"

            )

    print()


# ==========================================================
# EXIBE CONCLUSÃO
# ==========================================================

def print_conclusion(
    result
):
    """
    Mostra a conclusão geral.
    """

    print()

    print("=" * 60)
    print("CONCLUSÃO")
    print("=" * 60)

    print()

    status = result[
        "status"
    ]

    if status == "UNIQUE":

        print(
            "Existe apenas uma solução possível."
        )

    elif status == "AMBIGUOUS":

        print(

            "Existem múltiplas soluções válidas."

        )

        print(

            f"Foram encontradas "

            f"{result['number_of_solutions']} "

            f"soluções."

        )

    else:

        print(

            "O conjunto de premissas é inconsistente."

        )

        print(

            "Nenhuma solução foi encontrada."

        )

    print()


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def explain_solution(

    puzzle,

    result

):
    """
    Exibe toda a explicação.
    """

    print_statements(

        puzzle

    )

    print()

    print("=" * 60)
    print("RESULTADO DO Z3")
    print("=" * 60)

    print()

    print(

        f"Status: "

        f"{result['status']}"

    )

    print(

        f"Quantidade de soluções: "

        f"{result['number_of_solutions']}"

    )

    print()

    if result[
        "number_of_solutions"
    ] > 0:

        print_all_solutions(

            result

        )

        print_forced_values(

            result

        )

    print_conclusion(

        result

    )