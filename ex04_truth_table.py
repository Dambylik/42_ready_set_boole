import sys
from ex03_boolean_evaluation import boolean_eval


def print_truth_table(formula: str):
    letters = sorted(set(char for char in formula if char.isupper()))
    n = len(letters)

    print('| ' + ' | '.join(letters) + ' | = |')
    print('|---'*n + '---|')

    for i in range(2**n):
        validation_dict = {}
        for j, letter in enumerate(letters):
            bit = (i >> (n - 1 - j)) & 1
            validation_dict[letter] = str(bit)

        expr_eval = ''.join(validation_dict.get(c, c) for c in formula)
        result = boolean_eval(expr_eval)
        row = [validation_dict[l] for l in letters]
        print('| ' + ' | '.join(row) + ' | ' + str(int(result)) + ' |')


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
        sys.exit(1)


if __name__ == '__main__':
    main()

