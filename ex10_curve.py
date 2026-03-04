U16_MAX = 2**16 - 1
U32_MAX = 2**32 - 1

def map_coordinates(x: int, y: int) -> float:
    if not (0 <= x <= U32_MAX and 0 <= y <= U32_MAX):
        raise ValueError("x and y must be between 0 and 65535")
    
    morton_code = 0
    for i in range(16):
        morton_code |= ((x >> i) & 1) << (2 * i)
        morton_code |= ((y >> i) & 1) << (2 * i + 1)

    return morton_code / U32_MAX

def main():
    tests = [
        (0, 0),
        (1, 0),
        (0, 1),
        (10, 20),
        (123, 456),
        (65535, 65535),
    ]

    print("Testing f⁻¹(f(x, y)) = (x, y)")
    print("-" * 50)

    for x, y in tests:
        mapped = map_coordinates(x, y)

        print(f"Input: ({x:5}, {y:5}) "
              f"→ f: {mapped:.10f} ")

if __name__ == "__main__":
    main()