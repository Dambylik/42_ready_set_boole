import sys
from ex03_boolean_evaluation import Node, build_ast

def to_cnf(node: Node) -> Node:
    """Convert AST to Conjunctive Normal Form"""
    if node is None:
        return None

    # Переменная или константа
    if node.value.isupper() or node.value in '01':
        return Node(node.value)

    # NEGATION
    if node.value == '!':
        child = to_cnf(node.right)
        # DE MORGAN
        if child.value == '&':
            left = Node('!', right=child.left)
            right = Node('!', right=child.right)
            return Node('|', to_cnf(left), to_cnf(right))
        elif child.value == '|':
            left = Node('!', right=child.left)
            right = Node('!', right=child.right)
            return Node('&', to_cnf(left), to_cnf(right))
        elif child.value == '!':  # двойное отрицание
            return to_cnf(child.right)
        else:
            return Node('!', right=child)

    # Конъюнкция или дизъюнкция
    if node.value in '&|':
        left = to_cnf(node.left)
        right = to_cnf(node.right)

        if node.value == '|':
            # распределение OR над AND
            if left.value == '&':
                a = left.left
                b = left.right
                return Node('&', to_cnf(Node('|', a, right)), to_cnf(Node('|', b, right)))
            elif right.value == '&':
                a = right.left
                b = right.right
                return Node('&', to_cnf(Node('|', left, a)), to_cnf(Node('|', left, b)))
        return Node(node.value, left, right)

    return node


def cnf_to_rpn(node: Node) -> str:
    """Convert AST CNF back to Reverse Polish Notation"""
    if node is None:
        return ""
    if node.value in '!&|':
        if node.value == '!':
            return cnf_to_rpn(node.right) + '!'
        else:
            return cnf_to_rpn(node.left) + cnf_to_rpn(node.right) + node.value
    else:
        return node.value


def conjunctive_normal_form_rpn(expr: str) -> str:
    root = build_ast(expr)
    cnf_root = to_cnf(root)
    return cnf_to_rpn(cnf_root)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex06_conj_normal_form.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]
    try:
        result = conjunctive_normal_form_rpn(formula)
        print(result)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1) 

if __name__ == "__main__":
    main()


#tests = ["AB&!", "AB|!", "AB|C&", "AB|C|D|", "AB&C&D&", "AB&!C!|", "AB|!C!&"]
#for t in tests:
#    print(f"{t} -> {conjunctive_normal_form_rpn(t)}")