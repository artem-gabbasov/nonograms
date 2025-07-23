# Nonograms System Overview

This project consists of four core services that work together to provide a complete printable nonogram puzzle experience.

The project aims to solve the following problems:

- Conversion of arbitrary images into nonograms
- Division of large nonograms into smaller ones, allowing them to be solved individually and then assembled into the original large nonogram using scissors and tape
- Efficient distribution of smaller puzzles across pages and convenient print-ready PDF generation

Below is a brief description of each service and its expected functionality.

## Services

### 1. Image2Nonogram Service
- Converts images into nonogram puzzles based on the target size.
- Allows users to preview the result before proceeding with full processing (to be discussed).
- Future enhancements may include support for color puzzles and various image interpolation algorithms.

### 2. Nonogram Division Service
- Accepts an image representing a puzzle solution and divides it into several smaller images based on user-defined parameters.
- Converts each segment into a puzzle by adding numbers to the left and top.

### 3. Pagination Service
- Transforms the resulting puzzles into images.
- Arranges the images into pages to minimize the total number of pages required.
- Labels each puzzle with a number to facilitate reconstruction of the original image.

### 4. PDF Generation Service
- Produces a PDF file from the arranged pages.

## System Interaction

![System Interaction Diagram](arch/nonograms-toplevel.png)

*The diagram above illustrates how the four services interact to deliver the Nonograms experience.*
