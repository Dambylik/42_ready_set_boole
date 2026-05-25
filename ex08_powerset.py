import sys


def powerset(set_: list[int]) -> list[list[int]]:
    """Generate all subsets of the given set.
    Space Complexity: O(2^n) - must store all 2^n subsets in the result list.
    """
    elements = sorted(set(set_))
    n = len(elements)
    result = []

    for mask in range(1 << n):
        subset = []
        for i, element in enumerate(elements):
            if (mask >> i) & 1:
                subset.append(element)
        result.append(subset)

    return result


def test_08():
    test_cases = [
        ([], [[]]),
        ([0], [[], [0]]),
        ([0, 1], [[], [0], [1], [0, 1]]),
        ([0, 1, 2], [[], [0], [1], [0, 1], [2], [0, 2], [1, 2], [0, 1, 2]]),

        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([1], [[], [1]]),
        ([3, 1, 2], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ]
    
    for input_set, expected in test_cases:
        result = powerset(input_set)
        assert result == expected, f"powerset({input_set}) expected {expected}, got {result}"
        print(f"powerset({input_set}): {len(result)} subsets -> {result}")
    
    return True


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
    # test_08()
    main()