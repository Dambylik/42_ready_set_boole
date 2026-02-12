from ex00_adder import adder
import sys

def multiplier(a: int, b: int) -> int:
    result = 0
    while b!= 0:
        if (b & 1) == 1:
            result = adder(result, a)
        a = a << 1
        b = b >> 1
    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python ex01_multiplier.py <number> <number>")
        print("Example: python ex01_multiplier.py 42 42")
        sys.exit(1)
    else:
        result = multiplier(int(sys.argv[1]), int(sys.argv[2]))
        print(result)
    return 0


if __name__ == '__main__':
    main()