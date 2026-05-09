import sys

def powerset(set_: list[int]) -> list[list[int]]:
    """Complexity : O(n * 2^n)"""
    elements = sorted(set(set_))
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
        print("Usage: python ex08_powerset.py '1 2 3'")
        sys.exit(1)
        
    try:
        expr = sys.argv[1]
        numbers = [int(x) for x in expr.split()]
        for subset in powerset(numbers):
            print(subset)
    except ValueError as e:
        print("Error: ", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

# tests = [[1, 2, 3]]
# for t in tests:
#    print(f"{t} -> {powerset(t)}")