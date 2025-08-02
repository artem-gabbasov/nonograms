# 🧩 Nonogram Division Service

## Overview
Splits a solved nonogram Image (1 pixel = 1 cell) into smaller, playable nonograms (tiles), each with its own clues.

## Input
- **Image file:** Each pixel is a cell (white = empty)
- **Mode:** `"binary"` (default) or `"color"`
- **Tile width:** e.g. 4
- **Tile height:** e.g. 5

## Output
List of tiles:
```python
{
    "position": (row, col),
    "grid": [[...]],
    "row_clues": [[...]],
    "col_clues": [[...]]
} 
```

## Main Steps
1. Load Image → RGB grid
2. Convert to binary/color grid
3. Pad grid if needed
4. Split into tiles
5. Generate clues for each tile

## Class Structure
```
NonogramProcessor
 ├─ load_image()
 ├─ convert_to_grid()
 ├─ pad_grid()
 ├─ split_into_tiles()
 ├─ generate_clues()
 ├─ process()
 ├─ export()
 └─ print_results()
```

## Example
```python
processor = NonogramProcessor("input_solution.png", tile_width=4, tile_height=5, mode="binary")
processor.process()
tiles = processor.export()
```
