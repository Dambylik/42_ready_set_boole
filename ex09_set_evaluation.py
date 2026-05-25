import sys


def eval_set(formula: str, sets: list[list[int]]) -> list[int]:
    """Evaluate a formula on sets using RPN notation.
    
    Supports operators:
    - '!' (complement): NOT
    - '&' (intersection): AND
    - '|' (union): OR
    - '^' (symmetric difference): XOR
    - '>' (implication): (NOT A) OR B
    - '=' (equivalence): (A AND B) OR ((NOT A) AND (NOT B))
    
    Returns: sorted list of elements in the result set.
    """
    real_sets = [set(s) for s in sets] #A becomes {0, 1, 2}, B becomes {0, 3, 4}
    universe = set()
    for s in real_sets:
        universe |= s #union operator (|=): universe becomes {0, 1, 2, 3, 4} after processing A and B in the example

    stack = []

    for token in formula: #Processing Token 'A' | Processing Token 'B'
        if token.isupper():
            index = ord(token) - ord('A') #Index Calculation: ord('A') - ord('A') = 65 - 65 = 0 | Index Calculation: ord('B') - ord('A') = 66 - 65 = 1
            if index >= len(real_sets):
                raise ValueError("Undefined variable")
            stack.append(real_sets[index]) #It grabs real_sets (Set A, then set B) and pushes it onto the stack.
            #Stack State: [ {0, 1, 2}, {0, 3, 4} ]
        elif token == '!':
            if not stack:
                raise ValueError("Invalid formula")
            a = stack.pop()
            stack.append(universe - a)

        elif token in "&|>^=":
            if len(stack) < 2:
                raise ValueError("Invalid formula")
            b = stack.pop()
            a = stack.pop()

            if token == '&': #intersection: elements common to both a and b
                stack.append(a & b) #{0, 1, 2} & {0, 3, 4} = {0}

            elif token == '|':
                stack.append(a | b)

            elif token == '>':
                stack.append((universe - a) | b)

            elif token == '^':
                # XOR: elements in either a or b, but not both
                stack.append((a - b) | (b - a))

            elif token == '=':
                stack.append((a & b) | ((universe - a) & (universe - b)))

        else:
            raise ValueError("Invalid character")

    if len(stack) != 1:
        raise ValueError("Invalid formula")

    return sorted(stack[0])


def test_09():
    test_cases = [
        ("AB&", [[0, 1, 2], [0, 3, 4]], [0]),
        ("AB|", [[0, 1, 2], [3, 4, 5]], [0, 1, 2, 3, 4, 5]),
        ("A!", [[0, 1, 2]], []),
        
        ("A", [[]], []),
        ("A!", [[]], []),
        ("A", [[42]], [42]),
        ("A!", [[42]], []),
        ("A!B&", [[1, 2, 3], [2, 3, 4]], [4]),
        ("AB|", [[0, 1, 2], []], [0, 1, 2]),
        ("AB&", [[0, 1, 2], []], []),
        ("AB&", [[0, 1, 2], [0]], [0]),
        ("AB&", [[0, 1, 2], [42]], []),
        ("AB^", [[0, 1, 2], [0]], [1, 2]),
        ("AB>", [[0], [1, 2]], [1, 2]),
        ("AB>", [[0], [0, 1, 2]], [0, 1, 2]),
        
        ("ABC||", [[], [], []], []),
        ("ABC||", [[0], [1], [2]], [0, 1, 2]),
        ("ABC||", [[0], [0], [0]], [0]),
        ("ABC&&", [[0], [0], []], []),
        ("ABC&&", [[0], [0], [0]], [0]),
        ("ABC^^", [[0], [0], [0]], [0]),
        ("ABC>>", [[0], [0], [0]], [0]),
    ]
    
    for formula, sets, expected in test_cases:
        result = eval_set(formula, sets)
        assert result == expected, f"eval_set('{formula}', {sets}) expected {expected}, got {result}"
        print(f"{formula:10} with {str(sets):50} -> {result}")
    
    return True


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
    # test_09()
    main()
