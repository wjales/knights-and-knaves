from puzzles.generator import generate_puzzle
from solver.z3_solver import solve_puzzle
from llm.router import ask_llm
from experiments.metrics import compare_results

def main():

    print("\n=== KNIGHTS & KNAVES BENCHMARK ===\n")

    puzzle = generate_puzzle()

    print("PUZZLE:\n", puzzle["text"])

    print("\n--- Z3 SOLVER ---\n")

    z3_result = solve_puzzle(
        puzzle["speaker"],
        puzzle["target"]
    )

    print(z3_result)

    print("\n--- LLM SOLVER ---\n")

    llm_result = ask_llm(puzzle["text"])

    print(llm_result)

    print("\n--- COMPARISON ---\n")

    compare_results(z3_result, llm_result)


if __name__ == "__main__":
    main()