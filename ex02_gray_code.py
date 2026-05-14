import sys
U32_MAX = 2**32 - 1

def gray_code(n: int) -> int:
    """Formula : gray = n XOR (n >> 1)"""
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
        print("Error: input must be a u32")
        sys.exit(1)
    result = gray_code(n)
    print(result)


def test_2():
    assert gray_code(0) == 0
    assert gray_code(1) == 1
    assert gray_code(2) == 3
    assert gray_code(3) == 2
    assert gray_code(4) == 6
    assert gray_code(5) == 7
    assert gray_code(6) == 5
    assert gray_code(7) == 4
    assert gray_code(8) == 12


if __name__ == '__main__':
    # test_2()
    main()
