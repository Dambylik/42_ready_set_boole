import sys
from ex03_boolean_evaluation import build_ast, Node, print_tree


def to_nnf(node: Node) -> Node:
    """Convert AST to Negation Normal Form"""

    if node.left is None and node.right is None:
        return node

    if node.value == '!':
        child = to_nnf(node.right)

        if child.value == '!':
            return to_nnf(child.right)

        if child.value == '&':
            return to_nnf(Node('|', Node('!', right=child.left), Node('!', right=child.right)))

        if child.value == '|':
            return to_nnf(Node('&', Node('!', right=child.left), Node('!', right=child.right)))
        return Node('!', right=child)

    left = to_nnf(node.left) if node.left else None
    right = to_nnf(node.right) if node.right else None

    if node.value == '>':
        return to_nnf(Node('|', Node('!', right=left), right))

    if node.value == '=':
        left_and = Node('&', left, right)
        right_and = Node('&', Node('!', right=left), Node('!', right=right))
        return to_nnf(Node('|', left_and, right_and))

    if node.value == '^':
        left_and = Node('&', left, Node('!', right=right))
        right_and = Node('&', Node('!', right=left), right)
        return to_nnf(Node('|', left_and, right_and))

    return Node(node.value, left, right)


def ast_to_rpn(node: Node) -> str:
    """Convert AST NNF back to Reverse Polish Notation"""
    if node is None:
        return ""
    left = ast_to_rpn(node.left)
    right = ast_to_rpn(node.right)

    return left + right + node.value


def negation_normal_form(formula: str) -> str:
    root = build_ast(formula)
    # print_tree(root)
    nnf_root = to_nnf(root)
    # print_tree(nnf_root)
    return ast_to_rpn(nnf_root)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex05_neg_normal_form.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]
    try:
        result = negation_normal_form(formula)
        print(result)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1) 

if __name__ == "__main__":
    main()


# tests = ["AB&!", "AB|!", "AB>", "AB=", "AB|C&!"]
# for t in tests:
#    print(f"{t} -> {negation_normal_form(t)}")       