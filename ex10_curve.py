U16_MAX = 2**16 - 1
U32_MAX = 2**32 - 1

def map_coordinates(x: int, y: int) -> float:
    """Map 2D coordinates to a 1D value using Morton code (Z-order curve).
    
    Returns: Normalized Morton code as float in range [0, 1).
    """
    if not (0 <= x <= U16_MAX and 0 <= y <= U16_MAX):
        raise ValueError("x and y must be between 0 and 65535")
    
    morton_code = 0
    for i in range(16): #interleaving the binary digits (bits) of $x$ and $y$ like shuffling a deck of cards.
        morton_code |= ((x >> i) & 1) << (2 * i) #Shifts that bit to an even position
        morton_code |= ((y >> i) & 1) << (2 * i + 1) #Shifts that bit to an odd position
        #{morton_code} = [y_{15}][x_{15}][y_{14}][x_{14}] ... [y_1][x_1][y_0][x_0]
    return morton_code / U32_MAX #When you interleave two 16-bit integers ($x$ and $y$), the resulting morton_code is a 32-bit integer.

def main():
    tests = [
        (0, 0),
        (1, 0),
        (0, 1),
        (10, 20),
        (123, 456),
        (65535, 65535)
    ]

    print("Testing f⁻¹(f(x, y)) = (x, y)")
    print("-" * 50)

    for x, y in tests:
        mapped = map_coordinates(x, y)

        print(f"Input: ({x:5}, {y:5}) "
              f"→ f: {mapped:.10f} ")

if __name__ == "__main__":
    main()