import sys
from ex03_boolean_evaluation import build_ast
from ex05_neg_normal_form import to_nnf
from ex06_conj_normal_form import to_cnf


def extract_clauses(node):
    """Return list of clauses (each clause = list of literals)"""

    if node.value == '&':
        return extract_clauses(node.left) + extract_clauses(node.right)

    return [extract_literals(node)]


def extract_literals(node):
    """Return list of literals inside a clause"""

    if node.value == '|':
        return extract_literals(node.left) + extract_literals(node.right)

    if node.value == '!':
        return [('!', node.right.value)]

    return [(None, node.value)]


def evaluate_clause(clause, assignment):
    """Clause is satisfied if at least one literal is True"""

    for neg, var in clause:
        value = assignment[var]
        if neg:
            value = not value
        if value:
            return True
    return False


def is_satisfiable(expr: str) -> bool:
    root = build_ast(expr)
    nnf_root = to_nnf(root)
    cnf_root = to_cnf(nnf_root)

    clauses = extract_clauses(cnf_root)

    variables = sorted({var for clause in clauses for _, var in clause})
    n = len(variables)

    for mask in range(1 << n):
        assignment = {}
        for i, var in enumerate(variables):
            assignment[var] = bool((mask >> i) & 1)

        if all(evaluate_clause(cl, assignment) for cl in clauses):
            return True

    return False


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex07_sat.py 'formula'")
        sys.exit(1)

    expr = sys.argv[1]

    try:
        print(is_satisfiable(expr))
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

#tests = ["AB|", "AB&", "AA!&", "AA^"]
#for t in tests:
#    print(f"{t} -> {evaluate_clause(t)}")