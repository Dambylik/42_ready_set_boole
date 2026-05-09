from ex00_adder import adder
import sys
U32_MAX = 2**32 - 1


def multiplier(a: int, b: int) -> int:
    """
    Multiply two integers recursively using bit operations and adder().
    
    How it works:
    - Look at the last bit of b: if it is 1, add a to the result
    - Shift a left (double it) and b right (halve it)
    - Repeat until b becomes 0
    
    Example: 2 * 3
    - 3 in binary: 11 (has two 1-bits)
    - So: 2*1 (first 1-bit) + 2*2 (second 1-bit) = 2 + 4 = 6
    
    Complexity:
    - Time: O((log n)²) — loop runs log₂(n) times, each adder() also runs log₂(n) times
    - Space: O((log n)²) — memory stacks up from both loops together
    """
    # Base case: if b is 0, multiplication is done
    if b == 0:
        return 0
    
    # Check if the last bit of b is 1
    last_bit_is_one = (b & 1) == 1
    
    # Prepare for next recursion: shift a left (×2) and b right (÷2)
    a_shifted_left = a << 1
    b_shifted_right = b >> 1
    
    if last_bit_is_one:
        # If last bit is 1: add `a` to result of next multiplication
        return adder(a, multiplier(a_shifted_left, b_shifted_right))
    else:
        # If last bit is 0: skip and continue to next recursion
        return multiplier(a_shifted_left, b_shifted_right)


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


if __name__ == '__main__':
    main()


def test_1():
    assert multiplier(0, 0) == 0
    assert multiplier(1, 0) == 0
    assert multiplier(0, 1) == 0
    assert multiplier(1, 1) == 1
    assert multiplier(1, 2) == 2
    assert multiplier(2, 2) == 4