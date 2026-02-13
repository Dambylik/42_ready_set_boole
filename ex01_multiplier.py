from ex00_adder import adder
import sys
U32_MAX = 0xFFFFFFFF


def multiplier(a: int, b: int) -> int:
    """The complexity of this function is O(1)"""
    result = 0
    while b!= 0:
        if (b & 1) == 1:
            result = adder(result, a)
        a = (a << 1) & U32_MAX
        b = b >> 1
    return result & U32_MAX


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
        print("Error: inputs must be u32 (0 <= n <= 2^32 - 1)")
        sys.exit(1)

    result = multiplier(a, b)
    print(result)


if __name__ == '__main__':
    main()