"""
main.py

Arquivo principal do projeto.

Responsável por:

- Configuração inicial;
- Escolha do número de premissas;
- Escolha da LLM;
- Geração de puzzles;
- Execução do solver Z3;
- Execução do pipeline LLM + Z3;
- Execução do benchmark.
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from config import (

    NUMBER_OF_PREMISES,

    DEFAULT_BENCHMARK_SIZE,

    DEFAULT_LLM_PROVIDER

)

from puzzles.generator import (
    generate_puzzle
)

from puzzles.formatter import (
    format_puzzle
)

from solver.z3_solver import (
    solve_puzzle
)

from solver.explain_solver import (
    explain_solution
)

from solver.llm_assisted_solver import (
    solve_with_llm
)

from experiments.benchmark import (
    run_benchmark
)

from experiments.logger import (
    log_benchmark
)


# ==========================================================
# CABEÇALHO
# ==========================================================

def print_header():

    print()

    print("=" * 60)
    print("KNIGHTS AND KNAVES")
    print("=" * 60)

    print()


# ==========================================================
# CONFIGURAÇÃO DAS PREMISSAS
# ==========================================================

def configure_premises():

    valor = input(

        f"Número de premissas "
        f"[{NUMBER_OF_PREMISES}]: "

    )

    if valor.strip() == "":

        return NUMBER_OF_PREMISES

    return int(valor)


# ==========================================================
# CONFIGURAÇÃO DA LLM
# ==========================================================

def configure_llm():

    print()

    print("LLMs disponíveis:")

    print()

    print("1 - Gemini")
    print("2 - Ollama")
    print("3 - Fallback")

    print()

    escolha = input(

        f"Escolha "
        f"[{DEFAULT_LLM_PROVIDER}]: "

    )

    if escolha.strip() == "":

        return DEFAULT_LLM_PROVIDER

    if escolha == "1":

        return "gemini"

    if escolha == "2":

        return "ollama"

    return "fallback"


# ==========================================================
# EXIBE A CONFIGURAÇÃO ATUAL
# ==========================================================

def print_execution_configuration(

    premises,

    llm

):

    print()

    print("=" * 60)
    print("CONFIGURAÇÃO DA EXECUÇÃO")
    print("=" * 60)

    print()

    print(

        f"Quantidade de premissas: "

        f"{premises}"

    )

    print(

        f"LLM selecionada: "

        f"{llm.capitalize()}"

    )

    print()

    print(

        "Estas configurações serão "

        "utilizadas em todas as "

        "operações."

    )

    print()


# ==========================================================
# MENU
# ==========================================================

def print_menu():

    print()

    print("1 - Gerar e resolver puzzle")

    print("2 - Resolver usando LLM + Z3")

    print("3 - Executar benchmark")

    print("4 - Alterar configurações")

    print("5 - Sair")

    print()


# ==========================================================
# OPÇÃO 1
# ==========================================================

def run_single_puzzle(

    number_of_premises

):

    puzzle = generate_puzzle(

        number_of_premises

    )

    print()

    print("=" * 60)
    print("PUZZLE GERADO")
    print("=" * 60)

    print()

    print(

        format_puzzle(

            puzzle

        )

    )

    print()

    resultado = solve_puzzle(

        puzzle

    )

    explain_solution(

        puzzle,

        resultado

    )


# ==========================================================
# OPÇÃO 2
# ==========================================================

def run_llm_pipeline(

    number_of_premises,

    llm_provider

):

    puzzle = generate_puzzle(

        number_of_premises

    )

    solve_with_llm(

        puzzle,

        llm_provider

    )


# ==========================================================
# OPÇÃO 3
# ==========================================================

def run_full_benchmark(

    number_of_premises,

    llm_provider

):

    print()

    quantidade = input(

        f"Quantidade de testes "
        f"[{DEFAULT_BENCHMARK_SIZE}]: "

    )

    if quantidade.strip() == "":

        quantidade = (

            DEFAULT_BENCHMARK_SIZE

        )

    else:

        quantidade = int(

            quantidade

        )

    resultado = run_benchmark(

        total_tests=

            quantidade,

        number_of_premises=

            number_of_premises,

        llm_provider=

            llm_provider

    )

    log_benchmark(

        resultado,

        number_of_premises

    )


# ==========================================================
# LOOP PRINCIPAL
# ==========================================================

def main():

    print_header()

    # ----------------------------------
    # Configuração inicial
    # ----------------------------------

    current_premises = (

        configure_premises()

    )

    current_llm = (

        configure_llm()

    )

    print_execution_configuration(

        current_premises,

        current_llm

    )

    # ----------------------------------
    # Menu principal
    # ----------------------------------

    while True:

        print_menu()

        opcao = input(

            "Escolha uma opção: "

        )

        # ------------------------------

        if opcao == "1":

            run_single_puzzle(

                current_premises

            )

        # ------------------------------

        elif opcao == "2":

            run_llm_pipeline(

                current_premises,

                current_llm

            )

        # ------------------------------

        elif opcao == "3":

            run_full_benchmark(

                current_premises,

                current_llm

            )

        # ------------------------------

        elif opcao == "4":

            print()

            print(

                "Alterando configurações..."

            )

            print()

            current_premises = (

                configure_premises()

            )

            current_llm = (

                configure_llm()

            )

            print_execution_configuration(

                current_premises,

                current_llm

            )

        # ------------------------------

        elif opcao == "5":

            print()

            print(

                "Programa encerrado."

            )

            print()

            break

        # ------------------------------

        else:

            print()

            print(

                "Opção inválida."

            )

            print()


# ==========================================================
# PONTO DE ENTRADA
# ==========================================================

if __name__ == "__main__":

    main()