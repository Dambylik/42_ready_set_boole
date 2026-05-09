from ex00_adder import adder
import sys
U32_MAX = 2**32 - 1


def multiplier(a: int, b: int) -> int:
    """
    time: O(log n) proportional to the number of bits

    Complexity:
    - Time: O(log n * k) where n is the value magnitude (number of bits)
      and k is cost of `adder` (which is O(log n)). For typical analysis,
      this gives O((log n)^2) in bit-operations. If `adder` is considered O(1)
      for fixed-size integers (e.g. u32) then this is O(log n) iterations.
    - Space: O(1) — uses a fixed number of variables.
    """
    result = 0
    while b!= 0:
        if (b & 1) == 1:
            result = adder(result, a)
        a = (a << 1)
        b = b >> 1
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


if __name__ == '__main__':
    main()


def test_1():
    assert multiplier(0, 0) == 0
    assert multiplier(1, 0) == 0
    assert multiplier(0, 1) == 0
    assert multiplier(1, 1) == 1
    assert multiplier(1, 2) == 2
    assert multiplier(2, 2) == 4