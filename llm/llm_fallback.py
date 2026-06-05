"""
llm/llm_fallback.py

Implementação de segurança.

Este módulo é utilizado quando
nenhuma LLM estiver disponível
ou quando ocorrer alguma falha
na comunicação.

Ele permite que o restante da
aplicação continue funcionando.
"""


def ask_fallback(prompt):
    """
    Resposta padrão.

    O parâmetro prompt é mantido
    apenas para manter a mesma
    interface dos demais módulos.
    """

    return (
        "[FALLBACK]\n\n"

        "Nenhuma LLM disponível.\n"

        "Verifique:\n"

        "- Chave da API;\n"
        "- Conexão com a internet;\n"
        "- Servidor Ollama;\n"
        "- Configuração do router."
    )