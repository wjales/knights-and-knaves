"""
llm/router.py

Responsável por selecionar
qual modelo de linguagem (LLM)
será utilizado.

A escolha pode vir:

1) Do main.py (preferencial).
2) Do config.py (valor padrão).

Fluxo:

main.py
    ↓
solve_with_llm()
    ↓
ask_llm()
    ↓
Gemini / Ollama / Fallback
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

from config import (

    LLM_PROVIDER

)


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def ask_llm(

    prompt,

    provider=None

):
    """
    Envia um prompt para a LLM.

    Parâmetros:

    prompt:
        Texto enviado ao modelo.

    provider:
        Modelo escolhido pelo usuário.

    Se provider for None,
    utiliza o valor padrão
    definido no config.py.
    """

    # ----------------------------------
    # Define o provider
    # ----------------------------------

    provider = (

        provider

        or

        LLM_PROVIDER

    ).lower()

    # ----------------------------------
    # GEMINI
    # ----------------------------------

    if provider == "gemini":

        try:

            from llm.llm_gemini import (

                ask_gemini

            )

            return ask_gemini(

                prompt

            )

        except Exception as e:

            return (

                "[ROUTER ERROR]\n\n"

                "Falha ao utilizar "

                "Gemini.\n\n"

                +

                str(e)

            )

    # ----------------------------------
    # OLLAMA
    # ----------------------------------

    elif provider == "ollama":

        try:

            from llm.llm_ollama import (

                ask_ollama

            )

            return ask_ollama(

                prompt

            )

        except Exception as e:

            return (

                "[ROUTER ERROR]\n\n"

                "Falha ao utilizar "

                "Ollama.\n\n"

                +

                str(e)

            )

    # ----------------------------------
    # FALLBACK
    # ----------------------------------

    elif provider == "fallback":

        from llm.llm_fallback import (

            ask_fallback

        )

        return ask_fallback(

            prompt

        )

    # ----------------------------------
    # PROVIDER INVÁLIDO
    # ----------------------------------

    else:

        from llm.llm_fallback import (

            ask_fallback

        )

        return (

            "[ROUTER ERROR]\n\n"

            f"Provider inválido: "

            f"{provider}\n\n"

            +

            ask_fallback(

                prompt

            )

        )