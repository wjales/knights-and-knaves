"""
experiments/benchmark.py

Responsável por executar uma série de
testes automáticos para comparar a
resposta produzida pela LLM com a
solução encontrada pelo Z3.

Fluxo:

1) Gera um puzzle.
2) Envia para a LLM.
3) Resolve com o Z3.
4) Compara os resultados.
5) Atualiza as estatísticas.
6) Repete o processo N vezes.
7) Retorna um relatório completo.
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from puzzles.generator import (
    generate_puzzle
)

from solver.llm_assisted_solver import (
    solve_with_llm
)


# ==========================================================
# CRIA A ESTRUTURA DAS ESTATÍSTICAS
# ==========================================================

def create_statistics():
    """
    Cria o dicionário que armazenará
    todas as métricas do benchmark.
    """

    return {

        # Quantidade total de testes.
        "total_tests": 0,

        # Quantidade de respostas corretas.
        "correct_answers": 0,

        # Quantidade de respostas incorretas.
        "wrong_answers": 0,

        # Taxa de acerto.
        "accuracy": 0.0,

        # LLM utilizada.
        "llm_provider": "",

        # Número de premissas utilizadas.
        "number_of_premises": 0

    }


# ==========================================================
# ATUALIZA AS ESTATÍSTICAS
# ==========================================================

def update_statistics(

    statistics,

    report

):
    """
    Atualiza os contadores do benchmark.

    Parâmetros
    ----------
    statistics : dict

        Dicionário principal das métricas.

    report : dict

        Relatório retornado pelo
        solve_with_llm().
    """

    statistics[
        "total_tests"
    ] += 1

    if report[
        "matches_z3"
    ]:

        statistics[
            "correct_answers"
        ] += 1

    else:

        statistics[
            "wrong_answers"
        ] += 1


# ==========================================================
# CALCULA A ACURÁCIA
# ==========================================================

def calculate_accuracy(
    statistics
):
    """
    Calcula a taxa de acerto
    percentual do benchmark.
    """

    total = statistics[
        "total_tests"
    ]

    if total == 0:

        statistics[
            "accuracy"
        ] = 0.0

        return

    statistics[
        "accuracy"
    ] = (

        statistics[
            "correct_answers"
        ]

        /

        total

    ) * 100


# ==========================================================
# EXIBE O PROGRESSO
# ==========================================================

def print_progress(

    current,

    total

):
    """
    Exibe o andamento da execução.
    """

    print(

        f"Teste "

        f"{current}"

        f"/"

        f"{total}"

    )


# ==========================================================
# EXECUTA O BENCHMARK
# ==========================================================

def run_benchmark(

    total_tests,

    number_of_premises,

    llm_provider

):
    """
    Executa todos os testes.

    Parâmetros
    ----------
    total_tests : int

        Quantidade de puzzles.

    number_of_premises : int

        Quantidade de premissas.

    llm_provider : str

        LLM escolhida pelo usuário.
    """

    # ----------------------------------
    # Inicializa estatísticas.
    # ----------------------------------

    statistics = (

        create_statistics()

    )

    statistics[
        "llm_provider"
    ] = llm_provider

    statistics[
        "number_of_premises"
    ] = number_of_premises

    print()

    print("=" * 60)
    print("INICIANDO BENCHMARK")
    print("=" * 60)

    print()

    print(

        f"LLM utilizada: "

        f"{llm_provider}"

    )

    print(

        f"Premissas: "

        f"{number_of_premises}"

    )

    print(

        f"Quantidade de testes: "

        f"{total_tests}"

    )

    print()

    # ----------------------------------
    # Loop principal.
    # ----------------------------------

    for i in range(

        total_tests

    ):

        print_progress(

            i + 1,

            total_tests

        )

        # ------------------------------
        # Gera um novo puzzle.
        # ------------------------------

        puzzle = generate_puzzle(

            number_of_premises

        )

        # ------------------------------
        # Executa o pipeline completo.
        # ------------------------------

        report = solve_with_llm(

            puzzle,

            llm_provider

        )

        # ------------------------------
        # Atualiza as métricas.
        # ------------------------------

        update_statistics(

            statistics,

            report

        )

    # ----------------------------------
    # Calcula a acurácia final.
    # ----------------------------------

    calculate_accuracy(

        statistics

    )

    # ----------------------------------
    # Exibe o resumo.
    # ----------------------------------

    print()

    print("=" * 60)
    print("RESULTADO FINAL")
    print("=" * 60)

    print()

    print(

        f"LLM: "

        f"{statistics['llm_provider']}"

    )

    print(

        f"Premissas: "

        f"{statistics['number_of_premises']}"

    )

    print(

        f"Total de testes: "

        f"{statistics['total_tests']}"

    )

    print(

        f"Acertos: "

        f"{statistics['correct_answers']}"

    )

    print(

        f"Erros: "

        f"{statistics['wrong_answers']}"

    )

    print(

        f"Acurácia: "

        f"{statistics['accuracy']:.2f}%"

    )

    print()

    # ----------------------------------
    # Retorna o relatório completo.
    # ----------------------------------

    return statistics