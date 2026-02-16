import sys
U32_MAX = 0xFFFFFFFF

def gray_code(n: int) -> int:
    """The complexity of this function is O(1)"""
    return n ^ (n >> 1)


def main():
    if len(sys.argv) != 2:
        print("Usage: python ex02_gray_code.py <u32_number>")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("Error: input must be an integer")
        sys.exit(1)
    if n < 0 or n > U32_MAX:
        print("Error: input must be a u32 (0 <= n <= 2^32 - 1)")
        sys.exit(1)
    result = gray_code(n)
    print(result)


if __name__ == '__main__':
    main()