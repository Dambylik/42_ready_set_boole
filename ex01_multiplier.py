from ex00_adder import adder
import sys
U32_MAX = 2**32 - 1


def multiplier(a: int, b: int) -> int:
    """
    Multiplies 2 u32-bit integers using only bitwise operations.
    
    Algorithm: Binary multiplication via iterative bit shifting
    - Check the least significant bit (LSB) of b: if it is 1, add a to result
    - Left shift a (double it) and right shift b (halve it)
    - Repeat until b becomes 0
    - This works because multiplying by binary digits is equivalent to shifting
    
    Complexity for fixed-width u32:
    - Time: O(1) — loop runs at most 32 times fixed-width
    - Space: O(1) — only uses constant variables
    """
    result = 0
    while b != 0:
        if (b & 1) == 1:  # check the least significant bit (LSB) of b: if it is 1, add a to result
            result = adder(result, a)
        a = a << 1  # Left shift a (double it)
        b = b >> 1  # Right shift b (halve it)
    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python ex01_multiplier.py <number> <number>")
        sys.exit(1)
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
    except ValueError:
        print("Error: input must be an integer")
        sys.exit(1)
    if not (0 <= a <= U32_MAX and 0 <= b <= U32_MAX):
        print("Error: inputs must be u32")
        sys.exit(1)

    result = multiplier(a, b)
    print(result)


def test_1():
    assert multiplier(0, 0) == 0
    assert multiplier(1, 0) == 0
    assert multiplier(0, 1) == 0
    assert multiplier(1, 1) == 1
    assert multiplier(1, 2) == 2
    assert multiplier(2, 2) == 4

if __name__ == '__main__':
    # test_1()
    main()