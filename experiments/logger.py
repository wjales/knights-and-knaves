"""
experiments/logger.py

Responsável por salvar o histórico
dos benchmarks executados.

Cada execução gera um registro
que é armazenado no arquivo:

results/benchmark_history.json

Se o arquivo não existir,
ele será criado automaticamente.
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

import json
import os
from datetime import datetime

from config import (
    BENCHMARK_HISTORY_FILE
)


# ==========================================================
# CARREGA O HISTÓRICO EXISTENTE
# ==========================================================

def load_history():
    """
    Carrega o arquivo contendo
    os benchmarks anteriores.

    Caso ele não exista,
    retorna uma lista vazia.
    """

    if not os.path.exists(

        BENCHMARK_HISTORY_FILE

    ):

        return []

    try:

        with open(

            BENCHMARK_HISTORY_FILE,

            "r",

            encoding="utf-8"

        ) as file:

            return json.load(

                file

            )

    except Exception:

        return []


# ==========================================================
# SALVA O HISTÓRICO
# ==========================================================

def save_history(
    history
):
    """
    Salva a lista completa
    de benchmarks.
    """

    # Garante que a pasta exista.

    os.makedirs(

        os.path.dirname(

            BENCHMARK_HISTORY_FILE

        ),

        exist_ok=True

    )

    with open(

        BENCHMARK_HISTORY_FILE,

        "w",

        encoding="utf-8"

    ) as file:

        json.dump(

            history,

            file,

            indent=4,

            ensure_ascii=False

        )


# ==========================================================
# CRIA UM REGISTRO
# ==========================================================

def create_log_entry(

    statistics

):
    """
    Constrói um registro
    padronizado do benchmark.
    """

    return {

        # Data e hora da execução.

        "timestamp":

            datetime.now().strftime(

                "%d/%m/%Y %H:%M:%S"

            ),

        # Modelo utilizado.

        "llm_provider":

            statistics[
                "llm_provider"
            ],

        # Número de premissas.

        "number_of_premises":

            statistics[
                "number_of_premises"
            ],

        # Quantidade de testes.

        "total_tests":

            statistics[
                "total_tests"
            ],

        # Acertos.

        "correct_answers":

            statistics[
                "correct_answers"
            ],

        # Erros.

        "wrong_answers":

            statistics[
                "wrong_answers"
            ],

        # Taxa de acerto.

        "accuracy":

            round(

                statistics[
                    "accuracy"
                ],

                2

            )

    }


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def log_benchmark(

    statistics,

    number_of_premises=None

):
    """
    Salva um benchmark
    no histórico.
    """

    # ----------------------------------
    # Compatibilidade.
    # ----------------------------------

    if (

        number_of_premises

        is not None

    ):

        statistics[

            "number_of_premises"

        ] = number_of_premises

    # ----------------------------------
    # Carrega histórico.
    # ----------------------------------

    history = load_history()

    # ----------------------------------
    # Cria novo registro.
    # ----------------------------------

    entry = create_log_entry(

        statistics

    )

    # ----------------------------------
    # Adiciona ao histórico.
    # ----------------------------------

    history.append(

        entry

    )

    # ----------------------------------
    # Salva.
    # ----------------------------------

    save_history(

        history

    )

    # ----------------------------------
    # Exibe confirmação.
    # ----------------------------------

    print()

    print("=" * 60)
    print("BENCHMARK SALVO")
    print("=" * 60)

    print()

    print(

        "Arquivo: "

        +

        BENCHMARK_HISTORY_FILE

    )

    print()

    print(

        f"LLM: "

        f"{entry['llm_provider']}"

    )

    print(

        f"Premissas: "

        f"{entry['number_of_premises']}"

    )

    print(

        f"Testes: "

        f"{entry['total_tests']}"

    )

    print(

        f"Acertos: "

        f"{entry['correct_answers']}"

    )

    print(

        f"Erros: "

        f"{entry['wrong_answers']}"

    )

    print(

        f"Acurácia: "

        f"{entry['accuracy']:.2f}%"

    )

    print()


# ==========================================================
# VISUALIZA O HISTÓRICO
# ==========================================================

def show_history():
    """
    Exibe todos os benchmarks
    armazenados.
    """

    history = load_history()

    print()

    print("=" * 60)
    print("HISTÓRICO DE BENCHMARKS")
    print("=" * 60)

    print()

    if len(history) == 0:

        print(

            "Nenhum benchmark "

            "foi executado."

        )

        print()

        return

    for index, item in enumerate(

        history,

        start=1

    ):

        print(

            f"Execução {index}"

        )

        print(

            f"Data: "

            f"{item['timestamp']}"

        )

        print(

            f"LLM: "

            f"{item['llm_provider']}"

        )

        print(

            f"Premissas: "

            f"{item['number_of_premises']}"

        )

        print(

            f"Testes: "

            f"{item['total_tests']}"

        )

        print(

            f"Acertos: "

            f"{item['correct_answers']}"

        )

        print(

            f"Erros: "

            f"{item['wrong_answers']}"

        )

        print(

            f"Acurácia: "

            f"{item['accuracy']:.2f}%"

        )

        print()

        print("-" * 60)

        print()