from PIL import Image
import random
import os
import argparse


def generate_example_nonogram_solution(
    image_path="example_nonogram_solution.png", width=20, height=20, color=False
):
    """Helper script to generate a random nonogram solution image, where each pixel represents a cell in the nonogram.
    Args:
        image_path (str): Path to save the generated image.
        width (int): Width of the nonogram.
        height (int): Height of the nonogram.
        color (bool): If True, use random colors for filled cells, otherwise use black and white.
    Returns:
        str: Path to the saved image.
    """
    grid = [[random.randint(0, 1) for _ in range(width)] for _ in range(height)]

    if color:
        # Random color for filled cells, white for empty
        def random_color():
            return tuple(random.randint(0, 255) for _ in range(3))

        pixels = [
            [random_color() if cell == 1 else (255, 255, 255) for cell in row]
            for row in grid
        ]
    else:
        # Black for filled, white for empty
        pixels = [
            [(0, 0, 0) if cell == 1 else (255, 255, 255) for cell in row]
            for row in grid
        ]

    # Create and save the image
    img = Image.new("RGB", (width, height))
    for y, row in enumerate(pixels):
        for x, pixel in enumerate(row):
            img.putpixel((x, y), pixel)

    img.save(image_path)
    return os.path.abspath(image_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate a random nonogram solution image."
    )
    parser.add_argument(
        "--image_path",
        type=str,
        default="example_nonogram_solution.png",
        help="Path to save the generated image.",
    )
    parser.add_argument("--width", type=int, default=20, help="Width of the nonogram.")
    parser.add_argument(
        "--height", type=int, default=20, help="Height of the nonogram."
    )
    parser.add_argument(
        "--color", action="store_true", help="Use random colors for filled cells."
    )

    args = parser.parse_args()
    result_path = generate_example_nonogram_solution(
        image_path=args.image_path,
        width=args.width,
        height=args.height,
        color=args.color,
    )
    print(f"Nonogram solution image saved to: {result_path}")
