"""
config.py

Arquivo central de configurações do projeto.

Todas as opções gerais do sistema
devem ser alteradas aqui.

Módulos que utilizam este arquivo:

- main.py
- llm/router.py
- llm/llm_gemini.py
- llm/llm_ollama.py
- solver/llm_assisted_solver.py
- experiments/benchmark.py
- experiments/logger.py
- puzzles/generator.py
- solver/z3_solver.py
"""

# ==========================================================
# IMPORTAÇÕES
# ==========================================================

import os


# ==========================================================
# CONFIGURAÇÕES DOS PUZZLES
# ==========================================================

"""
Quantidade padrão de premissas.

Caso o usuário apenas pressione ENTER,
esse valor será utilizado.
"""

NUMBER_OF_PREMISES = 3


"""
Quantidade máxima de personagens
que podem existir em um puzzle.
"""

NUMBER_OF_CHARACTERS = 8


"""
Permite que um personagem
apareça falando mais de uma vez.
"""

ALLOW_REPEATED_SPEAKERS = True


# ==========================================================
# CONFIGURAÇÕES DO SOLVER
# ==========================================================

"""
Número máximo de soluções
que o Z3 irá enumerar.

Evita explosões combinatórias.
"""

MAX_SOLUTIONS = 1000


"""
Exibir todas as soluções encontradas.

True:
    Exibe todas.

False:
    Exibe apenas os fatos obrigatórios.
"""

SHOW_ALL_SOLUTIONS = True


# ==========================================================
# CONFIGURAÇÕES DO BENCHMARK
# ==========================================================

"""
Quantidade padrão de testes
executados no benchmark.
"""

DEFAULT_BENCHMARK_SIZE = 100


"""
Salvar automaticamente
os resultados do benchmark.
"""

SAVE_LOGS = True


"""
Salvar estatísticas gerais.
"""

SAVE_STATISTICS = True


# ==========================================================
# CONFIGURAÇÕES DAS LLMs
# ==========================================================

"""
Provider padrão.

Opções:

gemini
ollama
fallback
"""

DEFAULT_LLM_PROVIDER = "gemini"


"""
Provider atualmente utilizado.

Inicialmente assume o padrão,
mas poderá ser alterado
pelo main.py.
"""

LLM_PROVIDER = DEFAULT_LLM_PROVIDER


# ==========================================================
# MODELOS UTILIZADOS
# ==========================================================

"""
Modelo utilizado pela API Gemini.
"""

GEMINI_MODEL = "gemini-2.0-flash"


"""
Modelo local do Ollama.

Deve existir na saída de:

ollama list
"""

OLLAMA_MODEL = "llama3"


"""
Modelo atualmente configurado.

Mantido por compatibilidade
com módulos antigos.
"""

LLM_MODEL = GEMINI_MODEL


# ==========================================================
# CHAVES DAS APIS
# ==========================================================

"""
Chave da API Gemini.

Pode ser definida no ambiente:

GEMINI_API_KEY=xxxx
"""

GEMINI_API_KEY = os.getenv(

    "GEMINI_API_KEY",

    ""

)


"""
Chave da OpenAI.

Mantida para futuras expansões.
"""

OPENAI_API_KEY = os.getenv(

    "OPENAI_API_KEY",

    ""

)


# ==========================================================
# PARÂMETROS DAS LLMs
# ==========================================================

"""
Temperatura da geração.

0.0:
    Respostas determinísticas.

1.0:
    Mais criatividade.
"""

TEMPERATURE = 0.0


"""
Quantidade máxima de tokens.
"""

MAX_TOKENS = 2048


# ==========================================================
# ARQUIVOS DE SAÍDA
# ==========================================================

"""
Histórico dos benchmarks.
"""

BENCHMARK_HISTORY_FILE = (

    "results/"
    "benchmark_history.json"

)


"""
Arquivo de estatísticas.
"""

STATISTICS_FILE = (

    "results/"
    "statistics.json"

)


# ==========================================================
# IDENTIFICAÇÃO DO PROJETO
# ==========================================================

PROGRAM_NAME = (

    "Knights and Knaves"

)


PROGRAM_VERSION = (

    "2.0"

)


AUTHOR = (

    "Projeto de Pesquisa "
    "LLM + Z3"

)


# ==========================================================
# MENSAGENS PADRÃO
# ==========================================================

WELCOME_MESSAGE = (

    "Comparação entre "
    "Large Language Models "
    "e o Z3 Solver"

)


EXIT_MESSAGE = (

    "Programa encerrado."

)