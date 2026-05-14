import sys
U32_MAX = 2**32 - 1


def adder(a: int, b: int) -> int:
   """ 
   Adds 2 u32-bit integers using bitwise operations without +/- operators.
   
   Complexity :
   - Time: O(1) — loop runs at most 32 times fixed-width
   - Space: O(1) — only uses constant variables (no recursion)
   """
   while b!= 0:
      sum_ = a ^ b
      carry = (a & b) << 1
      a = sum_
      b = carry
   return a


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
    

def test_00():
    assert adder(0, 0) == 0
    assert adder(1, 0) == 1
    assert adder(0, 1) == 1
    assert adder(1, 1) == 2
    assert adder(1, 2) == 3
    assert adder(2, 2) == 4


if __name__ == '__main__':
    test_00()
    main()