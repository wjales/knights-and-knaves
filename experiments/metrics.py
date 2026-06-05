"""
experiments/metrics.py

Responsável pelo cálculo das métricas do projeto.

Funções:

- Comparar resposta da LLM com o Z3.
- Calcular accuracy.
- Calcular taxas de ambiguidades.
- Calcular tempo médio.
- Gerar relatório estatístico.

Autor: Projeto Knights and Knaves
"""

# ==========================================================
# NORMALIZAÇÃO DE TEXTO
# ==========================================================

def normalize_text(text):
    """
    Converte texto para minúsculas e remove
    espaços extras.

    Isso facilita comparações entre respostas.
    """

    return text.lower().strip()


# ==========================================================
# VERIFICA SE UMA SOLUÇÃO ESTÁ PRESENTE
# ==========================================================

def solution_matches(solution, llm_response):
    """
    Verifica se uma solução encontrada
    pelo Z3 aparece na resposta da LLM.

    Exemplo:

    solução:

    {
        "Alice": True,
        "Bob": False
    }

    resposta:

    "Alice is a Knight and Bob is a Knave"

    retorna True.
    """

    response = normalize_text(
        llm_response
    )

    for person, value in solution.items():

        expected = (
            "knight"
            if value
            else "knave"
        )

        if person.lower() not in response:

            return False

        if expected not in response:

            return False

    return True


# ==========================================================
# COMPARAÇÃO ENTRE LLM E Z3
# ==========================================================

def compare_results(
    z3_result,
    llm_response
):
    """
    Verifica se a resposta da LLM
    coincide com pelo menos
    uma solução válida.
    """

    for solution in z3_result[
        "solutions"
    ]:

        if solution_matches(

            solution,

            llm_response

        ):

            return True

    return False


# ==========================================================
# ACCURACY
# ==========================================================

def calculate_accuracy(
    correct,
    total
):

    if total == 0:

        return 0

    return correct / total


# ==========================================================
# TAXA DE AMBIGUIDADE
# ==========================================================

def calculate_ambiguity_rate(
    ambiguous,
    total
):

    if total == 0:

        return 0

    return ambiguous / total


# ==========================================================
# TAXA DE SOLUÇÕES ÚNICAS
# ==========================================================

def calculate_unique_rate(
    unique,
    total
):

    if total == 0:

        return 0

    return unique / total


# ==========================================================
# TAXA DE UNSAT
# ==========================================================

def calculate_unsat_rate(
    unsat,
    total
):

    if total == 0:

        return 0

    return unsat / total


# ==========================================================
# TEMPO MÉDIO
# ==========================================================

def calculate_average_time(
    execution_times
):

    if len(
        execution_times
    ) == 0:

        return 0

    return (

        sum(
            execution_times
        )

        /

        len(
            execution_times
        )

    )


# ==========================================================
# MÉDIA DE SOLUÇÕES ENCONTRADAS
# ==========================================================

def calculate_average_solutions(
    solutions_per_puzzle
):

    if len(
        solutions_per_puzzle
    ) == 0:

        return 0

    return (

        sum(
            solutions_per_puzzle
        )

        /

        len(
            solutions_per_puzzle
        )

    )


# ==========================================================
# CRIA RELATÓRIO FINAL
# ==========================================================

def create_statistics(

    total,

    correct,

    ambiguous,

    unique,

    unsat,

    execution_times,

    solutions_per_puzzle

):

    return {

        "total_tests":

            total,

        "correct":

            correct,

        "accuracy":

            calculate_accuracy(

                correct,

                total

            ),

        "ambiguous":

            ambiguous,

        "ambiguity_rate":

            calculate_ambiguity_rate(

                ambiguous,

                total

            ),

        "unique":

            unique,

        "unique_rate":

            calculate_unique_rate(

                unique,

                total

            ),

        "unsat":

            unsat,

        "unsat_rate":

            calculate_unsat_rate(

                unsat,

                total

            ),

        "average_time":

            calculate_average_time(

                execution_times

            ),

        "average_solutions":

            calculate_average_solutions(

                solutions_per_puzzle

            )

    }