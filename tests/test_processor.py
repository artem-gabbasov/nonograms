import numpy as np
from PIL import Image
from pathlib import Path
import pytest
from ..src.nonogram_division_service.processor import NonogramProcessor


def test_binary_mode_simple_tile():
    # 5x5 black and white image (all black)
    img_path = Path("examples") / "input_5x5_bw.png"
    expected_grid = [
        [1, 1, 0, 0, 1],
        [0, 1, 1, 1, 0],
        [1, 0, 0, 1, 0],
        [1, 1, 0, 0, 1],
        [1, 1, 1, 0, 0],
    ]

    proc = NonogramProcessor(str(img_path), tile_width=5, tile_height=5, mode="binary")
    proc.process()
    tiles = proc.export()
    assert len(tiles) == 1
    tile = tiles[0]
    assert tile["position"] == (0, 0)
    assert tile["grid"] == expected_grid
    assert tile["row_clues"] == [[2, 1], [3], [1, 1], [2, 1], [3]]
    assert tile["col_clues"] == [[1, 3], [2, 2], [1, 1], [2], [1, 1]]


def test_color_mode_simple():
    img_path = Path("examples") / "input_5x5_color.png"
    expected_grid = [
        [
            (np.uint8(44), np.uint8(246), np.uint8(210)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(92), np.uint8(68), np.uint8(3)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
        ],
        [
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(144), np.uint8(183), np.uint8(213)),
            (np.uint8(89), np.uint8(244), np.uint8(106)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
        ],
        [
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(13), np.uint8(83), np.uint8(254)),
            (np.uint8(33), np.uint8(191), np.uint8(247)),
        ],
        [
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(100), np.uint8(162), np.uint8(76)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(72), np.uint8(156), np.uint8(201)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
        ],
        [
            (np.uint8(181), np.uint8(134), np.uint8(207)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(68), np.uint8(61), np.uint8(156)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
            (np.uint8(255), np.uint8(255), np.uint8(255)),
        ],
    ]
    expected_row_clues = [
        [
            ((np.uint8(44), np.uint8(246), np.uint8(210)), 1),
            ((np.uint8(92), np.uint8(68), np.uint8(3)), 1),
        ],
        [
            ((np.uint8(144), np.uint8(183), np.uint8(213)), 1),
            ((np.uint8(89), np.uint8(244), np.uint8(106)), 1),
        ],
        [
            ((np.uint8(13), np.uint8(83), np.uint8(254)), 1),
            ((np.uint8(33), np.uint8(191), np.uint8(247)), 1),
        ],
        [
            ((np.uint8(100), np.uint8(162), np.uint8(76)), 1),
            ((np.uint8(72), np.uint8(156), np.uint8(201)), 1),
        ],
        [
            ((np.uint8(181), np.uint8(134), np.uint8(207)), 1),
            ((np.uint8(68), np.uint8(61), np.uint8(156)), 1),
        ],
    ]
    expected_col_clues = [
        [
            ((np.uint8(44), np.uint8(246), np.uint8(210)), 1),
            ((np.uint8(181), np.uint8(134), np.uint8(207)), 1),
        ],
        [
            ((np.uint8(144), np.uint8(183), np.uint8(213)), 1),
            ((np.uint8(100), np.uint8(162), np.uint8(76)), 1),
        ],
        [
            ((np.uint8(89), np.uint8(244), np.uint8(106)), 1),
            ((np.uint8(68), np.uint8(61), np.uint8(156)), 1),
        ],
        [
            ((np.uint8(92), np.uint8(68), np.uint8(3)), 1),
            ((np.uint8(13), np.uint8(83), np.uint8(254)), 1),
            ((np.uint8(72), np.uint8(156), np.uint8(201)), 1),
        ],
        [((np.uint8(33), np.uint8(191), np.uint8(247)), 1)],
    ]
    proc = NonogramProcessor(str(img_path), tile_width=5, tile_height=5, mode="color")
    proc.process()
    tiles = proc.export()
    tile = tiles[0]
    assert len(tiles) == 1
    assert tile["position"] == (0, 0)
    assert tile["grid"] == expected_grid
    assert tile["row_clues"] == expected_row_clues
    assert tile["col_clues"] == expected_col_clues


def test_padding_and_split():
    # 9x10image with 5x5 tiles
    img_path = img_path = Path("examples") / "input_9x10_bw.png"
    grid_0_0 = [
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
    ]

    grid_0_1 = [
        [1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 0, 0],
    ]

    grid_1_0 = [
        [0, 1, 1, 0, 1],
        [0, 1, 1, 0, 0],
        [1, 0, 1, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1],
    ]

    grid_1_1 = [
        [1, 1, 0, 0, 0],
        [1, 0, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 0],
    ]
    proc = NonogramProcessor(str(img_path), tile_width=5, tile_height=5)
    proc.process()
    tiles = proc.export()
    assert len(tiles) == 4
    assert tiles[0]["position"] == (0, 0)
    assert tiles[0]["grid"] == grid_0_0
    assert tiles[1]["position"] == (0, 1)
    assert tiles[1]["grid"] == grid_0_1
    assert tiles[2]["position"] == (1, 0)
    assert tiles[2]["grid"] == grid_1_0
    assert tiles[3]["position"] == (1, 1)
    assert tiles[3]["grid"] == grid_1_1


def test_invalid_image_format():
    # Create a dummy image with an unsupported format
    with pytest.raises(
        AssertionError, match="Unsupported image format. Use PNG or JPEG."
    ):
        proc = NonogramProcessor("dummy.txt")
        proc.load_image()


def test_invalid_mode():
    img_path = "input_5x5_color.png"
    with pytest.raises(ValueError, match="Unsupported mode"):
        proc = NonogramProcessor(img_path, mode="unsupported")
        proc.convert_to_grid(np.zeros((5, 5, 3), dtype=np.uint8))


def test_image_does_not_exist():
    with pytest.raises(FileNotFoundError):
        proc = NonogramProcessor("non_existent_image.png")
        proc.load_image()
