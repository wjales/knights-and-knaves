import random

NAMES = ["Alice", "Bob", "Carol", "Dave"]

def generate_puzzle():

    a, b = random.sample(NAMES, 2)

    text = f"{a} says: '{b} is a knave.'"

    return {
        "speaker": a,
        "target": b,
        "text": text
    }