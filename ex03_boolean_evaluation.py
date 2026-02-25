import sys

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_ast(expr: str):
    stack = []

    for char in expr:
        if char == '0' or char == '1':
            stack.append(Node(char))

        elif char == '!':
            if len(stack) < 1:
                raise ValueError("Invalid expression")
            child = stack.pop()
            stack.append(Node('!', right=child))

        elif char in '&|^>=':
            if len(stack) < 2:
                raise ValueError("Invalid expression")
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(char, left, right))

        else:
            raise ValueError("Invalid character")

    if len(stack) != 1:
        raise ValueError("Invalid expression")

    return stack[0]


def print_tree(node, indent=0):
    if node is None:
        return
    print("  " * indent + str(node.value))
    print_tree(node.left, indent + 1)
    print_tree(node.right, indent + 1)


def boolean_eval(expr: str) -> bool:
    """ Time: O(n) One pass, constant work per symbol
        Space: O(n) (stack)"""
    stack = []

    for char in expr:
        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        
        elif char == '!':
            if len(stack) < 1:
                raise ValueError("To perform unary operation stack should have at least 1 value")
            a = stack.pop()
            stack.append(not a)
        
        elif char in '&|^>=':
            if len(stack) < 2:
                raise ValueError("To perform binary operation stack should have at least 2 values")
            b = stack.pop()
            a = stack.pop()
            
            if char == '&':
                stack.append(a and b)
            elif char == '|':
                stack.append(a or b)
            elif char == "^":
                stack.append(a ^ b)
            elif char == ">":
                stack.append((not a) or b)
            elif char == "=":
                stack.append(a == b)
        else:
            raise ValueError("Invalid character")
    
    if len(stack) != 1:
        raise ValueError("invalid RPN (two operands, no operator)")
    
    return stack[0]


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex03_boolean_evaluation.py 'expression'")
        sys.exit(1)
    
    allowed = set("01!&|^>=")
    try:
        for char in sys.argv[1]:
            if char not in allowed:
                raise ValueError("Invalid character")

        expr = sys.argv[1]
        result = boolean_eval(expr)
        print("RPN eval:", result)
        ast_tree = build_ast(expr)
        print("\nAST:")
        print_tree(ast_tree)

    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)



if __name__ == '__main__':
    main()