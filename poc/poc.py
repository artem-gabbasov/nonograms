import sys

import numpy as np
from PIL import Image


def image_to_monochrome_matrix(image_path, width, height, threshold=128):
    # Open and convert image to grayscale
    with Image.open(image_path).convert("L") as img:
        # Resize image to desired dimensions
        img = img.resize((width, height))
        # Convert to numpy array
        arr = np.array(img)
    # Apply threshold to get 0 or 1
    matrix = (arr < threshold).astype(int)
    return matrix


if __name__ == "__main__":
    if not 4 <= len(sys.argv) <= 5:
        print(f"Usage: {sys.argv[0]} <image_path> <width> <height> [<threshold>]")
        sys.exit(1)
    image_path = sys.argv[1]
    width = int(sys.argv[2])
    height = int(sys.argv[3])
    if len(sys.argv) == 5:
        threshold = int(sys.argv[4])
        matrix = image_to_monochrome_matrix(image_path, width, height, threshold)
    else:
        matrix = image_to_monochrome_matrix(image_path, width, height)
    for row in matrix:
        print("".join(map(str, row)))
