def reverse_map(n: float) -> (int, int):
    # 1. Range Check
    if not (0.0 <= n <= 1.0):
        print("Error: Input must be between 0.0 and 1.0")
        return (0, 0)

    # 2. Convert the float back to the 32-bit integer (Morton Code)
    MAX_U32 = 2**32 - 1
    # We round to the nearest integer to handle floating point precision issues
    morton_code = int(round(n * MAX_U32))

    x = 0
    y = 0

    # 3. Bit De-interleaving
    for i in range(16):
        # Extract the bit at position 2*i and move it to position i for x
        if morton_code & (1 << (2 * i)):
            x |= (1 << i)
        
        # Extract the bit at position 2*i + 1 and move it to position i for y
        if morton_code & (1 << (2 * i + 1)):
            y |= (1 << i)

    return (x, y)

# Including the original map function to test the (f⁻¹ ∘ f) property
def map_coordinates(x: int, y: int) -> float:
    morton_code = 0
    for i in range(16):
        morton_code |= (x & (1 << i)) << i
        morton_code |= (y & (1 << i)) << (i + 1)
    return morton_code / (2**32 - 1)

def main():
    # Test cases to prove (f⁻¹ ∘ f)(x,y) = (x,y)
    test_coords = [(0, 0), (65535, 65535), (10, 20), (123, 456)]

    print(f"{'Input (x, y)':<20} | {'Mapped Float':<15} | {'Reversed (x, y)':<20}")
    print("-" * 60)

    for x_in, y_in in test_coords:
        float_val = map_coordinates(x_in, y_in)
        x_out, y_out = reverse_map(float_val)
        print(f"({x_in:>5}, {y_in:>5})      | {float_val:.10f}    | ({x_out:>5}, {y_out:>5})")

if __name__ == "__main__":
    main()