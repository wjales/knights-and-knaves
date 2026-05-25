from z3 import *

def solve_puzzle(speaker, target):

    S = Bool(speaker)
    T = Bool(target)

    solver = Solver()

    statement = (T == False)

    solver.add(S == statement)

    if solver.check() == sat:

        m = solver.model()

        return {
            speaker: m.evaluate(S),
            target: m.evaluate(T)
        }

    return None