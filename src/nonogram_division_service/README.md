# 🧩 Nonogram Division Service

## Overview
Splits a solved nonogram Image (1 pixel = 1 cell) into smaller, playable nonograms (segments), each with its own clues.

## Input
- **Image file:** Each pixel is a cell (white = empty)
- **Segment width:** e.g. 4
- **Segment height:** e.g. 5

## Output
List of segments:
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
3. Split into segments
4. Generate clues for each segment

## Class Structure
```
NonogramProcessor
 ├─ load_image()
 ├─ convert_to_grid()
 ├─ split_into_segments()
 ├─ generate_clues()
 ├─ process()
 └─ print_results()
```

## Example
```python
processor = NonogramProcessor("input_solution.png", segment_width=4, segment_height=5)
segments = processor.process()
```
