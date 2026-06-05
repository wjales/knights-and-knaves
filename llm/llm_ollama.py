"""
llm/llm_ollama.py

Módulo responsável pela comunicação
com um servidor Ollama local.

Fluxo:

main.py
    ↓

router.py
    ↓

ask_ollama()
    ↓

Servidor Ollama
    ↓

Resposta textual
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

import ollama

from config import (

    OLLAMA_MODEL

)


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def ask_ollama(
    prompt
):
    """
    Envia um prompt para
    o modelo configurado
    no Ollama.

    Parâmetros
    ----------
    prompt : str

        Texto enviado ao modelo.

    Retorno
    --------
    str

        Resposta produzida
        pelo Ollama.
    """

    try:

        # ----------------------------------
        # Faz a requisição ao Ollama
        # ----------------------------------

        response = ollama.chat(

            model=

                OLLAMA_MODEL,

            messages=[

                {

                    "role":

                        "user",

                    "content":

                        prompt

                }

            ]

        )

        # ----------------------------------
        # Retorna apenas o texto
        # ----------------------------------

        return response[

            "message"

        ][

            "content"

        ]

    except Exception as e:

        return (

            "[OLLAMA ERROR]\n\n"

            +

            str(e)

        )