import warnings

warnings.filterwarnings(
    "ignore",
    message="pkg_resources is deprecated as an API.*",
    category=UserWarning,
)
from binarytree import Node as BinaryNode


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def build_ast(expr: str):
    """Parse a string and convert it into the Abstract Syntax Tree"""
    stack = []

    for char in expr:
        if char == '0' or char == '1' or char.isupper():
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


def build_treelib_ast(ast_node):
    """Build a binarytree Node from the AST"""
    binarytree_node = BinaryNode(ast_node.value)

    if ast_node.left is not None:
        binarytree_node.left = build_treelib_ast(ast_node.left)
    if ast_node.right is not None:
        binarytree_node.right = build_treelib_ast(ast_node.right)

    return binarytree_node


def print_ast_root(ast_node, indent=0, branch="root"):
    """Print the AST root in a readable recursive form"""
    if ast_node is None:
        return

    prefix = "  " * indent
    if branch == "root":
        print(f"{prefix}{ast_node.value}")
    else:
        print(f"{prefix}{branch}: {ast_node.value}")

    if ast_node.left is not None:
        print_ast_root(ast_node.left, indent + 1, "left")
    if ast_node.right is not None:
        print_ast_root(ast_node.right, indent + 1, "right")
