import sys
U32_MAX = 0xFFFFFFFF

def adder(a: int, b: int) -> int:
   """The complexity of this function is O(1)"""
   while b!= 0:
      sum_ = a ^ b #XOR (without carry)
      carry = (a & b) << 1 #carry + shift in 1 bit
      a = sum_
      b = carry
   return a & U32_MAX


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
        print("Error: inputs must be u32 (0 <= n <= 2^32 - 1)")
        sys.exit(1)
    result = adder(a, b)
    print(result)
    

if __name__ == '__main__':
    main()