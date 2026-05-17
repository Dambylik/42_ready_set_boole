import sys


def boolean_eval(expr: str) -> bool:
    stack = []
    for char in expr:
        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        elif char == '!':
            a = stack.pop()
            stack.append(not a)
        elif char == '&':
            b, a = stack.pop(), stack.pop()
            stack.append(a and b)
        elif char == '|':
            b, a = stack.pop(), stack.pop()
            stack.append(a or b)
        elif char == '^':
            b, a = stack.pop(), stack.pop()
            stack.append(a != b)
        elif char == '>':
            b, a = stack.pop(), stack.pop()
            stack.append(not a or b)
        elif char == '=':
            b, a = stack.pop(), stack.pop()
            stack.append(a == b)
    return stack[0]


def print_truth_table(formula: str):
    """Print the full truth table for an RPN formula.

        Complexity:
        - Time: O(n * 2^n), where n is the number of distinct variables.
            The 2^n term comes from enumerating every possible assignment,
            and each row requires building and evaluating the formula.
    """
    letters = sorted(set(char for char in formula if char.isupper()))
    n = len(letters)

    print('| ' + ' | '.join(letters) + ' | = |')
    print('|' + '---|' * (n + 1))

    for i in range(2**n):
        validation_dict = {}
        for j, letter in enumerate(letters):
            bit = (i >> (n - 1 - j)) & 1
            validation_dict[letter] = str(bit)

        expr_eval = ''.join(validation_dict.get(c, c) for c in formula)
        result = boolean_eval(expr_eval)
        row = [validation_dict[l] for l in letters]
        
        print('| ' + ' | '.join(row) + ' | ' + str(int(result)) + ' |')


def test_04():
    formulas = (
        'AB&C|',
        'AB&C|D|',

        'A',
        'A!',
        'AB|',
        'AB&',
        'AB^',
        'AB>',
        'AB=',
        'AA=',
        'ABC==',
        'AB>C>',
        'AB>A>A>',
    )

    for formula in formulas:
        print(f'Formula: {formula}')
        print_truth_table(formula)
        print()
        

def main():
    if len(sys.argv) != 2:
        print("Usage: python ex04_truth_table.py 'expression'")
        sys.exit (1)
    
    formula = sys.argv[1]
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>=')
    try:
        for char in formula:
            if char not in allowed_chars:
                raise ValueError("character is not allowed")
        print_truth_table(formula)
    except ValueError as e:
        print("Error: ", e)
        # sys.exit(1)


if __name__ == '__main__':
    test_04()
    # main()
