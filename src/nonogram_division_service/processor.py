from PIL import Image
import numpy as np
import argparse
from itertools import groupby

WHITE_PIXEL = (255, 255, 255)


class NonogramProcessor:
    """Processes an image into nonogram tiles with clues.
    Each pixel represents a cell in the nonogram.
    Args:
        path (str): Path to the input image file.
        tile_width (int): Width of each nonogram tile.
        tile_height (int): Height of each nonogram tile.
        mode (str): Processing mode: 'binary' or 'color'.
    Returns:
        None
    Attributes:
        grid (list): 2D list representing the nonogram grid.
        sub_nonograms (list): List of sub-nonograms, each with its own clues
    """

    def __init__(self, path, tile_width=5, tile_height=5, mode="binary"):
        self.path = path
        self.tile_width = tile_width
        self.tile_height = tile_height
        self.mode = mode
        self.grid = []
        self.sub_nonograms = []

    def load_image(self):
        assert self.path, "Image path must be provided"
        assert self.path.endswith(
            (".png", ".jpg", ".jpeg")
        ), "Unsupported image format. Use PNG or JPEG."
        img = Image.open(self.path).convert("RGB")
        return np.array(img)

    def convert_to_grid(self, pixels: np.ndarray):
        if self.mode == "binary":
            binary = (pixels != [255, 255, 255]).any(axis=2).astype(int)
            self.grid = binary.tolist()
        elif self.mode == "color":
            self.grid = [[tuple(p) for p in row] for row in pixels]
        else:
            raise ValueError("Unsupported mode")

    def pad_grid(self, grid):
        rows, cols = len(grid), len(grid[0])
        pad_r = (-rows) % self.tile_height
        pad_c = (-cols) % self.tile_width
        if isinstance(grid[0][0], int):
            pad_val = 0
        else:
            pad_val = WHITE_PIXEL

        for row in grid:
            row.extend([pad_val] * pad_c)
        for _ in range(pad_r):
            grid.append([pad_val] * len(grid[0]))
        return grid

    def split_into_tiles(self):
        """Split the grid into tiles of specified size.
        Each tile is a sub-nonogram with its own clues.
        """
        padded = self.pad_grid(self.grid)
        self.sub_nonograms = []
        for r in range(0, len(padded), self.tile_height):
            for c in range(0, len(padded[0]), self.tile_width):
                tile = [
                    row[c : c + self.tile_width]
                    for row in padded[r : r + self.tile_height]
                ]
                self.sub_nonograms.append(
                    {
                        "position": (r // self.tile_height, c // self.tile_width),
                        "grid": tile,
                    }
                )

    def generate_clues(self, grid):
        def row_col_clues(lines):
            if isinstance(lines[0][0], int):  # binary mode
                return [
                    [len(list(g)) for v, g in groupby(line) if v == 1] or [0]
                    for line in lines
                ]
            else:  # color mode
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
        self.convert_to_grid(pixels)
        self.split_into_tiles()

        for tile in self.sub_nonograms:
            row_clues, col_clues = self.generate_clues(tile["grid"])
            tile["row_clues"] = row_clues
            tile["col_clues"] = col_clues

    def export(self):
        return self.sub_nonograms

    def print_results(self):
        for tile in self.sub_nonograms:
            print(f"Tile at {tile['position']}:")
            print("Grid:")
            for row in tile["grid"]:
                print(row)
            print("Row clues:", tile["row_clues"])
            print("Column clues:", tile["col_clues"])
            print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process an image into nonogram tiles."
    )
    parser.add_argument("image_path", help="Path to the input image file")
    parser.add_argument(
        "--tile_width",
        type=int,
        default=5,
        help="Width of each nonogram tile (default: 5)",
    )
    parser.add_argument(
        "--tile_height",
        type=int,
        default=5,
        help="Height of each nonogram tile (default: 5)",
    )
    parser.add_argument(
        "--mode",
        choices=["binary", "color"],
        default="binary",
        help="Processing mode: 'binary' or 'color' (default: 'binary')",
    )

    args = parser.parse_args()
    processor = NonogramProcessor(
        args.image_path, args.tile_width, args.tile_height, args.mode
    )
    processor.process()
    result = processor.export()
    processor.print_results()
