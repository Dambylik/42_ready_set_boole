import sys
from print_ast_tree import build_ast, Node, build_treelib_ast
from ex03_boolean_evaluation import boolean_eval
from ex05_neg_normal_form import to_nnf, ast_to_rpn, get_truth_values, same_truth_table


def to_cnf(node: Node) -> Node:
    """Convert NNF AST to Conjunctive Normal Form."""
    if node.left is None and node.right is None:
        return node

    left = to_cnf(node.left) if node.left else None
    right = to_cnf(node.right) if node.right else None

    if node.value == '|': # use Distributive Law
        if left and left.value == '&':
            # (A & B) | C = (A | C) & (B | C)
            left_or = Node('|', left.left, right)
            right_or = Node('|', left.right, right)
            return Node('&', to_cnf(left_or), to_cnf(right_or))
        if right and right.value == '&':
            # C | (A & B) = (C | A) & (C | B)
            left_or = Node('|', left, right.left)
            right_or = Node('|', left, right.right)
            return Node('&', to_cnf(left_or), to_cnf(right_or))

    if node.value == '&':
        if left and left.value == '&':
            # ((A & B) & C) = (A & (B & C))  - already flattened by recursion
            pass

    return Node(node.value, left, right)


def flatten_to_right_associative(node: Node) -> Node:
    """Convert chains of same operators to right-associative form.
    E.g., (((A | B) | C) | D) becomes A | (B | (C | D))
    """
    if node.left is None and node.right is None:
        return node
    
    left = flatten_to_right_associative(node.left) if node.left else None
    right = flatten_to_right_associative(node.right) if node.right else None
    
    # Collect all operands in a chain of the same operator
    if node.value in ('|', '&'):
        operands = []
        
        def collect_operands(n):
            if n and n.value == node.value:
                collect_operands(n.left)
                collect_operands(n.right)
            elif n:
                operands.append(n)
        
        collect_operands(left)
        collect_operands(right)
        
        if len(operands) > 1:
            # Rebuild in right-associative form
            result = operands[-1]
            for i in range(len(operands) - 2, -1, -1):
                result = Node(node.value, operands[i], result)
            return result
    
    return Node(node.value, left, right)


def conjunctive_normal_form(formula: str) -> str:
    """Return the Conjunctive Normal Form of an RPN formula as RPN string.
    """
    root = build_ast(formula)
    nnf_root = to_nnf(root)
    cnf_root = to_cnf(nnf_root)
    cnf_root = flatten_to_right_associative(cnf_root)
    return ast_to_rpn(cnf_root)


def test_06():
    formulas = [
        'AB&!',
        'AB|!',
        'AB|C&',
        'AB|C|D|',
        'AB&C&D&',
        'AB&!C!|',
        'AB|!C!&',

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
    test_06()
    # main()