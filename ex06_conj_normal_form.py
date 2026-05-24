import sys
from print_ast_tree import build_ast, Node, build_treelib_ast
from ex03_boolean_evaluation import boolean_eval
from ex05_neg_normal_form import to_nnf, ast_to_rpn, get_truth_values, same_truth_table


def to_cnf(node: Node) -> Node:
    """Convert NNF AST to Conjunctive Normal Form."""
    if node.left is None and node.right is None:
        return node

    left = to_cnf(node.left) if node.left else None # Pauses to evaluate the left '!' branch
    right = to_cnf(node.right) if node.right else None # Pauses to evaluate the right '!' branch

    if node.value == '|': # use Distributive Law
        if left.value == '&':
            return to_cnf(Node('&', Node('|', left.left, right), Node('|', left.right, right)))
        if right.value == '&':
            return to_cnf(Node('&', Node('|', left, right.left), Node('|', left, right.right)))
        
        if left.value == '|':
            return to_cnf(Node('|', left.left, Node('|', left.right, right)))

    if node.value == '&':
        if left.value == '&':
            return to_cnf(Node('&', left.left, Node('&', left.right, right)))

    return Node(node.value, left, right)


def conjunctive_normal_form(formula: str) -> str:
    """Return the Conjunctive Normal Form of an RPN formula as RPN string.
    """
    root = build_ast(formula)
    # binarytree_root = build_treelib_ast(root)
    # print("AST tree:")
    # binarytree_root.pprint()
    nnf_root = to_nnf(root) #Convert to NNF first: leaving you with a tree containing only variables, !, &, and |.
    # binarytree_root = build_treelib_ast(nnf_root)
    # print("AST NNF tree:")
    # binarytree_root.pprint()
    cnf_root = to_cnf(nnf_root)
    # binarytree_root = build_treelib_ast(cnf_root)
    # print("AST CNF tree:")
    # binarytree_root.pprint()
    return ast_to_rpn(cnf_root)


def test_06():
    formulas = [
        'AB&!',
        'AB|!',
        'AB>',
        'AB=',
        'AB|C&!',
        'A',
        'A!',
        'AB&',
        'AB|',

        'A',
        'A!',
        'AB&',
        'AB|',

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
            cnf = conjunctive_normal_form(f)
            print('CNF:', cnf)
        except Exception as e:
            print('  Error converting to CNF:', e)
            all_ok = False
        equiv = same_truth_table(f, conjunctive_normal_form)
        print(f"Truth tables equivalent: {equiv}")
        print()
    return all_ok
    

def main():
    allowed_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ!&|^>=')
    
    # Process single formula from command line:
    if len(sys.argv) != 2:
        print("Usage: python ex06_conj_normal_form.py 'formula'")
        sys.exit(1)

    formula = sys.argv[1]
    try:
        for char in formula:
            if char not in allowed_chars:
                raise ValueError("character is not allowed")
        result = conjunctive_normal_form(formula)
        print(f"Formula: {formula}")
        print(f"CNF: {result}")
        equiv = same_truth_table(formula, conjunctive_normal_form)
        print(f"Truth tables equivalent: {equiv}")
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    # test_06()
    main()