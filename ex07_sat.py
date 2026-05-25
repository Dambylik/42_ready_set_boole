import sys
from print_ast_tree import build_ast, Node
from ex05_neg_normal_form import to_nnf, ast_to_rpn, get_truth_values, same_truth_table
from ex06_conj_normal_form import to_cnf


def extract_clauses(node: Node):
    """Return list of clauses (each clause = list of literals)."""
    if node.value == '&':
        return extract_clauses(node.left) + extract_clauses(node.right)

    return [extract_literals(node)]


def extract_literals(node: Node):
    """Return list of literals inside a clause."""
    if node.value == '|':
        return extract_literals(node.left) + extract_literals(node.right)

    if node.value == '!':
        return [('!', node.right.value)]

    return [(None, node.value)]


def evaluate_clause(clause, assignment):
    """Clause is satisfied if at least one literal is True."""
    for neg, var in clause:
        value = assignment[var]
        if neg:
            value = not value
        if value:
            return True
    return False


def is_satisfiable(formula: str) -> bool:
    """Check if a formula is satisfiable using brute-force CNF-SAT algorithm.
    Complexity: O(2^n) where n is the number of unique variables.    
    Returns: True if the formula is satisfiable, False otherwise.
    """
    root = build_ast(formula)
    nnf_root = to_nnf(root)
    cnf_root = to_cnf(nnf_root)
    clauses = extract_clauses(cnf_root)    
    variables = sorted({var for clause in clauses for _, var in clause})
    n = len(variables)

    for mask in range(1 << n):
        assignment = {}
        for i, var in enumerate(variables):
            assignment[var] = bool((mask >> i) & 1)
        for clause in clauses:
            if not evaluate_clause(clause, assignment): #If any clause is False, the code hits break
                break
        else:
            return True
        
    return False


def test_07():
    test_cases = [
        ('AB|', True),
        ('AB&', True),
        ('AA!&', False),
        ('AA^', False),

        ('A', True),
        ('A!', True),
        ('AA|', True),
        ('AA&', True),
        ('AA!&', False),
        ('AA^', False),
        ('AB^', True),
        ('AB=', True),
        ('AA>', True),
        ('AA!>', True),

        ('ABC||', True),
        ('AB&A!B!&&', False),
        ('ABCDE&&&&', True),
        ('AAA^^', True),
        ('ABCDE^^^^', True),
    ]
    
    for formula, expected in test_cases:
        result = is_satisfiable(formula)
        assert result == expected, f"Formula '{formula}' expected {expected}, got {result}"
        print(f"Formula '{formula}': {result}")
    
    return True


def main():
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>=')
    
    if len(sys.argv) != 2:
        print("Usage: python ex07_sat.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]
    try:
        for char in formula:
            if char not in allowed_chars:
                raise ValueError("character is not allowed")
        result = is_satisfiable(formula)
        print(f"Formula: {formula}")
        print(f"Satisfiable: {result}")
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    test_07()
    # main()