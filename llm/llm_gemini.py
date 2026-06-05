"""
llm/llm_gemini.py

Módulo responsável pela comunicação
com a API do Google Gemini.

Fluxo:

main.py
    ↓

router.py
    ↓

ask_gemini()
    ↓

API Gemini
    ↓

Resposta textual
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

import google.generativeai as genai

from config import (

    GEMINI_API_KEY,

    GEMINI_MODEL

)


# ==========================================================
# CONFIGURA A API
# ==========================================================

# Configura a chave da API.
# Essa configuração é feita apenas
# uma vez quando o módulo é carregado.

genai.configure(

    api_key=GEMINI_API_KEY

)


# ==========================================================
# FUNÇÃO PRINCIPAL
# ==========================================================

def ask_gemini(
    prompt
):
    """
    Envia um prompt para o Gemini.

    Parâmetros
    ----------
    prompt : str

        Texto enviado ao modelo.

    Retorno
    --------
    str

        Resposta produzida
        pelo Gemini.
    """

    try:

        # ----------------------------------
        # Cria o modelo
        # ----------------------------------

        model = genai.GenerativeModel(

            GEMINI_MODEL

        )

        # ----------------------------------
        # Envia o prompt
        # ----------------------------------

        response = model.generate_content(

            prompt

        )

        # ----------------------------------
        # Retorna apenas o texto
        # ----------------------------------

        return response.text

    except Exception as e:

        return (

            "[GEMINI ERROR]\n\n"

            +

            str(e)

        )