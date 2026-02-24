import sys
from ex03_boolean_evaluation import boolean_eval


def print_truth_table(formula: str):
    letters = set()

    for char in formula:
        if char.isupper():
               letters.add(char)   
           
    print(sorted(letters))
    print("------")

    



def main():
    if len(sys.argv) != 2:
        print("Usage: python ex04_truth_table.py '(A∧B)vC'")
        sys.exit (1)
    try:
        result = print_truth_table(sys.argv[1])
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == '__main__':
    main()

