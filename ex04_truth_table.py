import sys
from ex03_boolean_evaluation import boolean_eval


def print_truth_table(formula: str):
    """Print the full truth table for an RPN formula.

        Complexity:
        - Time: O(n * 2^n), where n is the number of distinct variables.
            The 2^n term comes from enumerating every possible assignment,
            and each row requires building and evaluating the formula.
    """
    variables = sorted(set(char for char in formula if char.isupper()))
    n = len(variables)

    print('| ' + ' | '.join(variables) + ' | = |')
    print('|' + '---|' * (n + 1))

    for mask in range(1 << n):
        assignment = {}
        for i, var in enumerate(variables):
            assignment[var] = str((mask >> i) & 1)

        expr_eval = ''.join(assignment.get(c, c) for c in formula)
        result = boolean_eval(expr_eval)
        row = [assignment[l] for l in variables]
        
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
        sys.exit(1)


if __name__ == '__main__':
    # test_04()
    main()
