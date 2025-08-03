# Pagination Service

## Overview

This service converts extracted nonogram segments into images and arranges them into pages to minimize the total number of pages required.

It consists of the following components:
- Instantiation of internal models representing the input segments
- Rasterization of the created models onto a canvas
- Optimal placement of the resulting images on page(s)

## Input

- **List of segments:**
    ```json
    {
        "position": (row, col),
        "grid": [[...]],
        "row_clues": [[...]],
        "col_clues": [[...]]
    }
    ```
- **Cell width in pixels:** e.g., 30
- **Cell height in pixels:** e.g., 30

## Output

- **List of pages:**
    ```json
    {
        "nonograms": [
            {
                "top": int,
                "left": int,
                "image": "<image data, format to be decided (e.g., base64-encoded PNG)>"
            }
        ]
    }
    ```

## Main Steps

1. Model instantiation (Segment → Internal model)
2. Model rasterization on canvas (Internal model → Image)
3. Image placement on pages (List of images → Page descriptors)
4. Output preparation (List of page descriptors → Output JSON)

## Packages

### model

Provides classes that translate clue lists into a convenient representation of complete information about a nonogram segment (or, in general, a nonogram).

Handles the distribution of clues among rows and columns (collectively called "lanes") and the proper labeling of the puzzle.

**Status:** Implemented (without labeling puzzles with identifiers), **not tested**.

### raster

Provides graphical methods to draw a puzzle represented by a model onto a canvas. Also provides the dimensions of the resulting image.

**Status:** Not implemented.

### placement

Provides optimal placement of images on pages to minimize the number of pages.

**Status:** Not implemented.
