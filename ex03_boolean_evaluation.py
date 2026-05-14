import sys
from print_ast_tree import build_ast, build_treelib_ast


def boolean_eval(expr: str) -> bool:
    """Evaluate an RPN propositional formula.

    Complexity:
    - Time: O(n) where n is len(expr)
    """
    stack = []
    for char in expr:
        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        elif char == '!':
            a = stack.pop()
            stack.append(not a)
        elif char == '&':
            b, a = stack.pop(), stack.pop()
            stack.append(a and b)
        elif char == '|':
            b, a = stack.pop(), stack.pop()
            stack.append(a or b)
        elif char == '^':
            b, a = stack.pop(), stack.pop()
            stack.append(a != b)
        elif char == '>':
            b, a = stack.pop(), stack.pop()
            stack.append(not a or b)
        elif char == '=':
            b, a = stack.pop(), stack.pop()
            stack.append(a == b)
    return stack[0]


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 ex03_boolean_evaluation.py <expression>")
        return
    
    expr = sys.argv[1]
    try:
        result = boolean_eval(expr)
        print(f"\nEvaluation result: {result}")
        ast_root = build_ast(expr)
        binarytree_root = build_treelib_ast(ast_root)
        print("AST tree:")
        binarytree_root.pprint()
    except Exception as e:
        print(f"Error: {e}")


def test_03():
    assert boolean_eval("0!") is True
    assert boolean_eval("1!") is False
    assert boolean_eval("00|") is False
    assert boolean_eval("10|") is True
    assert boolean_eval("01|") is True
    assert boolean_eval("11|") is True
    assert boolean_eval("10&") is False
    assert boolean_eval("11&") is True
    assert boolean_eval("11^") is False
    assert boolean_eval("10^") is True
    assert boolean_eval("00>") is True
    assert boolean_eval("01>") is True
    assert boolean_eval("10>") is False
    assert boolean_eval("11>") is True
    assert boolean_eval("00=") is True
    assert boolean_eval("11=") is True
    assert boolean_eval("10=") is False
    assert boolean_eval("01=") is False

    assert boolean_eval("11&0|") is True
    assert boolean_eval("10&1|") is True
    assert boolean_eval("11&1|") is True
    assert boolean_eval("11&1|1^") is False
    assert boolean_eval("01&1|1=") is True
    assert boolean_eval("01&1&1&") is False
    assert boolean_eval("0111&&&") is False


if __name__ == "__main__":
    test_03()
    main()
