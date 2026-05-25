from llm.llm_gemini import ask_gemini
from llm.llm_ollama import ask_ollama
from llm.llm_fallback import ask_fallback
from config import GEMINI_API_KEY

def ask_llm(prompt):

    # tenta Gemini
    try:
        if GEMINI_API_KEY:
            return ask_gemini(prompt)
    except:
        pass

    # tenta Ollama
    try:
        return ask_ollama(prompt)
    except:
        pass

    # fallback final
    return ask_fallback(prompt)