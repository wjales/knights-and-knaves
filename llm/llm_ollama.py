import ollama
from config import OLLAMA_MODEL

def ask_ollama(prompt):

    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"[OLLAMA ERROR] {e}"