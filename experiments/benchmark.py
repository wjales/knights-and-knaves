from puzzles.generator import generate_puzzle
from llm.router import ask_llm
from solver.z3_solver import solve_puzzle

def run_benchmark(n=20):

    correct = 0

    for i in range(n):

        p = generate_puzzle()

        z3 = solve_puzzle(p["speaker"], p["target"])
        llm = ask_llm(p["text"])

        print(f"\nTest {i+1}")

        print(z3)
        print(llm)

    print("\nBenchmark finished")