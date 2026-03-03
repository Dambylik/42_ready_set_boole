import sys

def powerset(s):
    """Complexity : O(n * 2^n)"""
    elements = list(s)
    n = len(elements)
    result = []

    for mask in range(1 << n):
        subset = []
        for i in range(n):
            if (mask >> i) & 1:
                subset.append(elements[i])
        result.append(subset)

    return result


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex08_powerset.py 'expr'")
        sys.exit(1)
    expr= sys.argv[1]
    
    try:
        print(powerset([expr]));
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    main()