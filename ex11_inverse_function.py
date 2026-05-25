from ex10_curve import map_coordinates
U16_MAX = 2**16 - 1
U32_MAX = 2**32 - 1


def reverse_map(n: float) -> tuple[int, int]:
    """Inverse of map_coordinates: recover 2D coordinates from a normalized Morton code.
    
    Extracts the original x and y coordinates from a space-filling curve value
    by deinterleaving the bits of the Morton code back into separate coordinates.
    
    Returns: Tuple (x, y) where x and y are in range [0, 65535].
    """

    morton_code = int(round(n * U32_MAX))
    x = 0
    y = 0

    for i in range(16):
        x |= ((morton_code >> (2 * i)) & 1) << i
        y |= ((morton_code >> (2 * i + 1)) & 1) << i

    return x, y


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
    print("-" * 60)

    for x, y in tests:
        mapped = map_coordinates(x, y)
        x_back, y_back = reverse_map(mapped)

        ok = (x, y) == (x_back, y_back)

        print(
            f"Input: ({x:5}, {y:5}) "
            f"→ f: {mapped:.10f} "
            f"→ f⁻¹: ({x_back:5}, {y_back:5}) "
            f"| OK: {ok}"
        )


if __name__ == "__main__":
    main()