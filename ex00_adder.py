import sys
U32_MAX = 2**32 - 1


def adder(a: int, b: int) -> int:
   """ 
   Complexity:
   - Time: O(log n) — runs as many times as there are bits in the number
   - Space: O(log n) — memory stacks up in layers (one for each bit)
   """
   if b == 0:
      return a
   
   sum_without_carry = a ^ b
   bits_to_carry_forward = (a & b) << 1
   return adder(sum_without_carry, bits_to_carry_forward)


def main():
    if len(sys.argv) != 3:
        print("Usage: python ex00_adder.py <number> <number>")
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
    result = adder(a, b)
    print(result)
    

if __name__ == '__main__':
    main()


def test_0():
    assert adder(0, 0) == 0
    assert adder(1, 0) == 1
    assert adder(0, 1) == 1
    assert adder(1, 1) == 2
    assert adder(1, 2) == 3
    assert adder(2, 2) == 4