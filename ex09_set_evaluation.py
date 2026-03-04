import sys

def eval_set(formula: str, sets: list[list[int]]) -> list[int]:
    # Convert input to real sets
    real_sets = [set(s) for s in sets]

    # Universe = union of all sets
    universe = set()
    for s in real_sets:
        universe |= s

    stack = []

    for token in formula:
        if token.isupper():
            index = ord(token) - ord('A')
            if index >= len(real_sets):
                raise ValueError("Undefined variable")
            stack.append(real_sets[index])

        elif token == '!':
            if not stack:
                raise ValueError("Invalid formula")
            a = stack.pop()
            stack.append(universe - a)

        elif token in "&|>=":
            if len(stack) < 2:
                raise ValueError("Invalid formula")
            b = stack.pop()
            a = stack.pop()

            if token == '&':
                stack.append(a & b)

            elif token == '|':
                stack.append(a | b)

            elif token == '>':
                stack.append((universe - a) | b)

            elif token == '=':
                stack.append((a & b) | ((universe - a) & (universe - b)))

        else:
            raise ValueError("Invalid character")

    if len(stack) != 1:
        raise ValueError("Invalid formula")

    return sorted(stack[0])


def main():
    if len(sys.argv) < 3:
        print("Usage: python ex09_set_evaluation.py 'AB&' '0,1,2' '0,3,4'")
        sys.exit(1)

    formula = sys.argv[1]

    try:
        sets = []
        for arg in sys.argv[2:]:
            if arg.strip() == "":
                sets.append([])
            else:
                sets.append([int(x) for x in arg.split(",")])

        result = eval_set(formula, sets)
        print(result)

    except ValueError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()

# ================= TESTS =================
"""
tests = [
    # (formula, sets)
    ("AB&", [[0,1,2], [0,3,4]]),
    ("AB|", [[0,1,2], [3,4,5]]),
    ("A!",  [[0,1,2]], []),
]

for formula, sets in tests:
    result = eval_set(formula, sets)
    print(f"{formula} with {sets}") 
    print(f"Result:      {result}")
"""