
import sys

def adder(a: int, b: int) -> int:
   while b!= 0:
      sum_ = a ^ b #XOR (without carry)
      carry = (a & b) << 1 #carry + shift in 1 bit
      a = sum_
      b = carry
   return a

def main():
   if len(sys.argv) != 3:
      print("Usage: python ex00_adder.py <number> <number>")
      print("Example: python ex00_adder.py 42 42")
      sys.exit(1)
   else:
      result = adder(int(sys.argv[1]), int(sys.argv[2]))
      print(result)


if __name__ == '__main__':
    main()