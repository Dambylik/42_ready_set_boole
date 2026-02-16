import sys

def boolean_eval(expr: str) -> bool:
    """ Time: O(n)
        Space: O(n) (stack)"""
    stack = []

    for char in expr:
        if char.isspace():
            continue

        if char == '0':
            stack.append(False)
        elif char == '1':
            stack.append(True)
        
        elif char == '!':
            if len(stack) < 1:
                raise ValueError("Invalid expression")
            a = stack.pop()
            stack.append(not a)
        
        elif char in '&|^>=':
            if len(stack) < 2:
                raise ValueError("Invalid expression")
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
        raise ValueError("Invalid expression")
    
    return stack[0]


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex03_boolean_evaluation.py <expression>")
        sys.exit(1)
    try:
        result = boolean_eval(sys.argv[1])
        print(result)
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == '__main__':
    main()