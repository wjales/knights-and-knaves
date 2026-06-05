"""
solver/llm_assisted_solver.py

Pipeline híbrido:

Puzzle
   ↓
LLM
   ↓
Z3
   ↓
Comparação
   ↓
Relatório

Este módulo é utilizado
tanto pelo main.py
quanto pelo benchmark.
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from llm.router import (

    ask_llm

)

from solver.z3_solver import (

    solve_puzzle

)

from experiments.metrics import (

    compare_results

)


# ==========================================================
# CONSTRÓI O PROMPT
# ==========================================================

def build_prompt(
    puzzle
):
    """
    Monta o texto enviado
    para a LLM.
    """

    prompt = ""

    prompt += (

        "Solve the following "

        "Knights and Knaves puzzle.\n\n"

    )

    prompt += (

        "Rules:\n"

    )

    prompt += (

        "- Knights always tell the truth.\n"

    )

    prompt += (

        "- Knaves always lie.\n\n"

    )

    prompt += (

        "Puzzle:\n\n"

    )

    prompt += (

        puzzle["text"]

    )

    prompt += (

        "\n\n"

        "Return the role of "

        "every character."

    )

    return prompt


# ==========================================================
# CONSULTA À LLM
# ==========================================================

def query_llm(

    puzzle,

    provider

):
    """
    Envia o puzzle
    para a LLM escolhida.
    """

    prompt = build_prompt(

        puzzle

    )

    return ask_llm(

        prompt,

        provider

    )


# ==========================================================
# CONSULTA AO Z3
# ==========================================================

def query_z3(
    puzzle
):
    """
    Resolve o puzzle
    utilizando Z3.
    """

    return solve_puzzle(

        puzzle

    )


# ==========================================================
# COMPARAÇÃO
# ==========================================================

def compare_llm_and_z3(

    llm_response,

    z3_result

):
    """
    Verifica se a resposta
    produzida pela LLM
    corresponde a alguma
    solução válida.
    """

    return compare_results(

        z3_result,

        llm_response

    )


# ==========================================================
# RELATÓRIO
# ==========================================================

def build_report(

    puzzle,

    provider,

    llm_response,

    z3_result,

    success

):
    """
    Organiza todas as
    informações obtidas.
    """

    return {

        "provider":

            provider,

        "puzzle":

            puzzle,

        "prompt":

            build_prompt(

                puzzle

            ),

        "llm_response":

            llm_response,

        "z3_result":

            z3_result,

        "matches_z3":

            success

    }


# ==========================================================
# IMPRESSÃO
# ==========================================================

def print_report(
    report
):
    """
    Exibe o relatório.
    """

    print()

    print("=" * 60)
    print("RESULTADO LLM + Z3")
    print("=" * 60)

    print()

    print(

        f"LLM utilizada: "

        f"{report['provider']}"

    )

    print()

    print("=" * 60)
    print("PUZZLE")
    print("=" * 60)

    print()

    print(

        report[
            "puzzle"
        ][
            "text"
        ]

    )

    print()

    print("=" * 60)
    print("RESPOSTA DA LLM")
    print("=" * 60)

    print()

    print(

        report[
            "llm_response"
        ]

    )

    print()

    print("=" * 60)
    print("RESULTADO DO Z3")
    print("=" * 60)

    print()

    print(

        "Status: "

        +

        report[
            "z3_result"
        ][
            "status"
        ]

    )

    print()

    print(

        "Número de soluções: "

        +

        str(

            report[
                "z3_result"
            ][
                "number_of_solutions"
            ]

        )

    )

    print()

    if report[
        "matches_z3"
    ]:

        print(

            "✓ A resposta da LLM "

            "é compatível com "

            "o Z3."

        )

    else:

        print(

            "✗ A resposta da LLM "

            "não corresponde "

            "a nenhuma solução "

            "válida."

        )

    print()


# ==========================================================
# PIPELINE PRINCIPAL
# ==========================================================

def solve_with_llm(

    puzzle,

    provider

):
    """
    Executa todo o pipeline.

    1) Consulta a LLM.

    2) Resolve usando Z3.

    3) Compara.

    4) Gera relatório.

    5) Exibe.

    6) Retorna.
    """

    # ----------------------------------
    # Consulta à LLM
    # ----------------------------------

    llm_response = query_llm(

        puzzle,

        provider

    )

    # ----------------------------------
    # Consulta ao Z3
    # ----------------------------------

    z3_result = query_z3(

        puzzle

    )

    # ----------------------------------
    # Comparação
    # ----------------------------------

    success = compare_llm_and_z3(

        llm_response,

        z3_result

    )

    # ----------------------------------
    # Relatório
    # ----------------------------------

    report = build_report(

        puzzle,

        provider,

        llm_response,

        z3_result,

        success

    )

    # ----------------------------------
    # Exibição
    # ----------------------------------

    print_report(

        report

    )

    # ----------------------------------
    # Retorno
    # ----------------------------------

    return report