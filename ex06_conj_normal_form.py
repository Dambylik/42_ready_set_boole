import sys
from ex03_boolean_evaluation import Node, build_ast
from ex05_neg_normal_form import to_nnf, ast_to_rpn


def to_cnf(node: Node) -> Node:

    if node.left is None and node.right is None:
        return node

    left = to_cnf(node.left) if node.left else None
    right = to_cnf(node.right) if node.right else None

    # distribute OR over AND
    if node.value == '|':
        if left.value == '&':
            return Node('&',
                        to_cnf(Node('|', left.left, right)),
                        to_cnf(Node('|', left.right, right)))

        if right.value == '&':
            return Node('&',
                        to_cnf(Node('|', left, right.left)),
                        to_cnf(Node('|', left, right.right)))

    return Node(node.value, left, right)


def conjunctive_normal_form(expr: str) -> str:
    root = build_ast(expr)
    nnf_root = to_nnf(root)
    cnf_root = to_cnf(nnf_root)
    return ast_to_rpn(cnf_root)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex06_conj_normal_form.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]

    try:
        result = conjunctive_normal_form(formula)
        print(result)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()


#tests = ["AB&!", "AB|!", "AB|C&", "AB|C|D|", "AB&C&D&", "AB&!C!|", "AB|!C!&"]
#for t in tests:
#    print(f"{t} -> {conjunctive_normal_form_rpn(t)}")