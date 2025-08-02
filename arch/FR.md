# Functional Requirements

1. Image2Nonogram Service

    1.1. Image Conversion to Nonogram:

        1.1.1. The system shall convert a user-provided image into a nonogram puzzle.

        1.1.2. The nonogram puzzle shall be based on a user-specified target size (width and height).

    1.2. Preview Feature:

        1.2.1. The system shall allow the user to preview the nonogram puzzle result before proceeding with full processing.

        1.2.2. The preview shall show the image representing the puzzle solution, without triggering all the workflow.

    1.3. Future Enhancements:

        1.3.1. The system shall support the generation of color puzzles in the future.

        1.3.2. The system shall allow the use of various image interpolation algorithms for better representations of the original image, preserving more detail and features.

2. Nonogram Division Service

    2.1. Image Segmentation:

        2.1.1. The system shall accept an image of a nonogram puzzle solution and divide it into several smaller, non-overlapping 2-dimensional segments.

        2.1.2. The segmentation process shall be configurable with user-defined parameters, in particular:

            2.1.2.1. The system shall request from the user a value that limits the allowed number of both rows and columns of each resultant segment.

            2.1.2.2. The system shall divide the entire puzzle into the minimal possible number of segments allowed by the limit provided by the user.

            2.1.2.3. The dimensions of the resultant segments shall be distributed as evenly as possible. For example, if one of the dimensions (width or height) is equal to 39 and the user limit is equal to 20, then it shall be divided into 2 segments along this dimension: of 20 and 19 cells, in any order. If the user limit is equal to 14, it shall be divided into 3 equal segments of 13 cells along this dimension.
   
            2.1.2.4. In the future the segmentation might be based on more sophisticated methods of complexity estimation than just division by dimensions. This means that the requirement of even distribution of segment dimensions might be reconsidered.

        2.1.3. The output shall provide enough information to reconstruct the order (or anyway the position) of each segment inside the original image.

    2.2. Puzzle Conversion:

        2.2.1. The system shall annotate each segment with appropriate number labels (row and column clues) to allow its unambiguous conversion into an individual nonogram puzzle.

3. Pagination Service

    3.1. Image Transformation:

        3.1.1. The system shall transform the puzzle segments together with their labels (clues) into images.

    3.2. Page Arrangement:

        3.2.1. The system shall arrange the resulting puzzle images into pages, minimizing the total number of pages required.

        3.2.2. The arrangement shall be based on factors such as puzzle size and page dimensions.

    3.3. Labeling:

        3.3.1. The system shall label each puzzle with a number to facilitate the reconstruction of the original image after printing.

        3.3.2. The label can be added either in the empty top-left corner of the puzzle or beyond its right and bottom borders (or in all the listed places).

4. PDF Generation Service

    4.1. PDF Creation:

        4.1.1. The system shall generate a PDF file containing the arranged pages of the nonogram puzzles.

        4.1.2. The generated PDF shall be downloadable or shareable by the user.

5. System-wide Requirements

    5.1. Error Handling

        5.1.1. The system shall validate all user inputs (e.g., wrong file type, invalid file size) and notify the user of any errors. In particular:

            5.1.1.1. At least the JPEG file type shall be supported. In case of an unsupported file type, the list of supported ones shall be provided to the user.

            5.1.1.2. Only input images of a reasonable size shall be accepted. For this, the size shall be limited by 10 megabytes.

            5.1.1.3. The requested nonograms shall have reasonable dimensions. For this, the nonogram dimensions (both height and width) shall be limited by 150 cells.

            5.1.1.4. The divided nonogram parts shall have reasonable dimensions. For this, the nonogram part dimensions (both height and width) shall be at least 10 cells.

        5.1.2. The system shall handle failures by providing clear error messages and guidance for resolution.
