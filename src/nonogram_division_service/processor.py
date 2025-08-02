from PIL import Image
import numpy as np
import argparse
from itertools import groupby

WHITE_PIXEL = (255, 255, 255)


class NonogramProcessor:
    """Processes an image into nonogram segments with clues.
    Each pixel represents a cell in the nonogram.
    Args:
        path (str): Path to the input image file.
        segment_width (int): Width of each nonogram segment.
        segment_height (int): Height of each nonogram segment.
    Returns:
        sub_nonograms (list): List of sub-nonograms, each with its own clues
    """

    def __init__(self, path, segment_width=5, segment_height=5):
        self.path = path
        self.segment_width = segment_width
        self.segment_height = segment_height

    def load_image(self):
        assert self.path, "Image path must be provided"
        assert self.path.endswith(".png"), "Unsupported image format. Use PNG."
        img = Image.open(self.path).convert("RGB")
        return np.array(img)

    def convert_to_grid(self, pixels: np.ndarray):
        grid = [[tuple(p) for p in row] for row in pixels]
        return grid

    def pad_grid(self, grid):
        rows, cols = len(grid), len(grid[0])
        pad_r = (-rows) % self.segment_height
        pad_c = (-cols) % self.segment_width
        if isinstance(grid[0][0], int):
            pad_val = 0
        else:
            pad_val = WHITE_PIXEL

        for row in grid:
            row.extend([pad_val] * pad_c)
        for _ in range(pad_r):
            grid.append([pad_val] * len(grid[0]))
        return grid

    def split_into_segments(self, grid):
        """Split the grid into segments of specified size.
        Each segment is a sub-nonogram with its own clues.
        """
        padded = self.pad_grid(grid)
        sub_nonograms = []
        for r in range(0, len(padded), self.segment_height):
            for c in range(0, len(padded[0]), self.segment_width):
                segment = [
                    row[c : c + self.segment_width]
                    for row in padded[r : r + self.segment_height]
                ]
                sub_nonograms.append(
                    {
                        "position": (r // self.segment_height, c // self.segment_width),
                        "grid": segment,
                    }
                )
        return sub_nonograms

    def generate_clues(self, grid):
        def row_col_clues(lines):
            return [
                [(v, len(list(g))) for v, g in groupby(line) if v != WHITE_PIXEL]
                or [(WHITE_PIXEL, 0)]
                for line in lines
            ]

        rows = row_col_clues(grid)
        cols = row_col_clues(list(zip(*grid)))  # Transpose
        return rows, cols

    def process(self):
        pixels = self.load_image()
        grid = self.convert_to_grid(pixels)
        sub_nonograms = self.split_into_segments(grid)

        for segment in sub_nonograms:
            row_clues, col_clues = self.generate_clues(segment["grid"])
            segment["row_clues"] = row_clues
            segment["col_clues"] = col_clues

        return sub_nonograms

    def print_results(self, sub_nonograms):
        for segment in sub_nonograms:
            print(f"Tile at {segment['position']}:")
            print("Grid:")
            for row in segment["grid"]:
                print(row)
            print("Row clues:", segment["row_clues"])
            print("Column clues:", segment["col_clues"])
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process an image into nonogram segments."
    )
    parser.add_argument(
        "--image-path", help="Path to the input image file", required=True
    )
    parser.add_argument(
        "--segment-width",
        type=int,
        default=5,
        help="Width of each nonogram segment (default: 5)",
    )
    parser.add_argument(
        "--segment-height",
        type=int,
        default=5,
        help="Height of each nonogram segment (default: 5)",
    )

    args = parser.parse_args()
    processor = NonogramProcessor(
        args.image_path, args.segment_width, args.segment_height
    )
    sub_nonograms = processor.process()
    processor.print_results(sub_nonograms)
