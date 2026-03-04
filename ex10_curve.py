def map_coordinates(x: int, y: int) -> float:
    # 1. Range Check (as encouraged by the instructions)
    MAX_U16 = 2**16 - 1
    if not (0 <= x <= MAX_U16 and 0 <= y <= MAX_U16):
        print("Error: Input out of range (0 to 65535)")
        return 0.0

    # 2. Bit Interleaving (Z-Order Curve / Morton Code)
    # We create a 32-bit integer by placing bits of x and y in alternating order
    morton_code = 0
    for i in range(16):
        # Extract the i-th bit of x and shift it to position 2*i
        morton_code |= (x & (1 << i)) << i
        # Extract the i-th bit of y and shift it to position 2*i + 1
        morton_code |= (y & (1 << i)) << (i + 1)

    # 3. Normalize to [0, 1]
    # The maximum value for a 32-bit result is 2^32 - 1
    MAX_U32 = 2**32 - 1
    return morton_code / MAX_U32

def main():
    # Test Case 1: The start (0,0) should be 0.0
    print(f"Map(0, 0)     -> {map_coordinates(0, 0)}")

    # Test Case 2: The very end (max, max) should be 1.0
    max_val = 2**16 - 1
    print(f"Map(max, max) -> {map_coordinates(max_val, max_val)}")

    # Test Case 3: Middle point
    print(f"Map(10, 20)   -> {map_coordinates(10, 20)}")

    # Test Case 4: Out of range
    map_coordinates(70000, 0)

if __name__ == "__main__":
    main()