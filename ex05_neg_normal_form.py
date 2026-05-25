import sys
from print_ast_tree import build_ast, Node, build_treelib_ast
from ex03_boolean_evaluation import boolean_eval


def to_nnf(node: Node) -> Node:
    """Convert AST to Negation Normal Form.
    Ensures that negations only apply to variables by pushing
    `!` inward using De Morgan's laws and eliminating
    implications/equivalences/xor.
    """

    if node.left is None and node.right is None: #for 'AB&!' It's not a leaf node (it has children A and B).
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

    left = to_nnf(node.left) if node.left else None # Evaluates 'A' -> returns node 'A'
    right = to_nnf(node.right) if node.right else None # Evaluates 'B' -> returns node 'B'

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

    return Node(node.value, left, right) #It returns a clean & node with A and B attached.


def ast_to_rpn(node: Node) -> str:
    """Convert AST (NNF) back to Reverse Polish Notation."""
    if node is None:
        return ""
    left = ast_to_rpn(node.left)
    right = ast_to_rpn(node.right)

    return left + right + node.value


def negation_normal_form(formula: str) -> str:
    """Return the Negation Normal Form of an RPN formula as RPN string.
    """
    root = build_ast(formula)
    # binarytree_root = build_treelib_ast(root)
    # print("AST tree:")
    # binarytree_root.pprint()
    nnf_root = to_nnf(root)
    # binarytree_root = build_treelib_ast(nnf_root)
    # print("AST NNF tree:")
    # binarytree_root.pprint()
    return ast_to_rpn(nnf_root)


def get_truth_values(formula: str):
    """Extract truth values for a formula.
    Returns (letters, results) where results[i] is the Boolean result for assignment i.
    """
    variables = sorted(set(char for char in formula if char.isupper()))
    n = len(variables)
    results = []

    for mask in range(1 << n):
        assignment = {}
        for i, var in enumerate(variables):
            assignment[var] = str((mask >> i) & 1)

        expr_eval = ''.join(assignment.get(c, c) for c in formula)
        result = boolean_eval(expr_eval)
        results.append(result)

    return variables, results


def same_truth_table(formula: str, convert_func=None) -> bool:
    """Compare truth tables for `formula` and its converted form.
    Args:
        formula: The input formula
        convert_func: The conversion function to apply (default: negation_normal_form)
    Returns True if they are identical, False otherwise.
    """
    if convert_func is None:
        convert_func = negation_normal_form
    converted = convert_func(formula)
    _, orig_results = get_truth_values(formula)
    _, converted_results = get_truth_values(converted)
    return orig_results == converted_results


def test_05():
    formulas = [
        'AB&!',
        'AB|!',
        'AB>',
        'AB=',
        'AB|C&!',

        'A',
        'A!',
        'AB&!',
        'AB|!',
        'AB>!',
        'AB=!',

        'ABC||',
        'ABC||!',
        'ABC|&',
        'ABC&|',
        'ABC&|!',
        'ABC^^',
        'ABC>>'
    ]
    all_ok = True
    for f in formulas:
        print(f'Formula: {f}')
        try:
            nnf = negation_normal_form(f)
            print('NNF:', nnf)
        except Exception as e:
            print('  Error converting to NNF:', e)
            all_ok = False
        equiv = same_truth_table(f)
        print(f"Truth tables equivalent: {equiv}")
        print()
    return all_ok


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex05_neg_normal_form.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>=')
    try:
        for char in formula:
            if char not in allowed_chars:
                raise ValueError("character is not allowed")
        result = negation_normal_form(formula)
        print(f"Formula: {formula}")
        print(f"NNF: {result}")
        equiv = same_truth_table(formula)
        print(f"Truth tables equivalent: {equiv}")
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    test_05()
    # main()
