# PuzzleAssembly
Various results based on assembling a blank 1500 piece puzzle

All the work in this project is based on the following puzzle-assembly agorithm:
1. Open the box, and put the empty box top to the side.
2. Choose one piece at random from the full box.
3. Draw another piece at random from the box.  If it does not fit with the first piece, then put it in the empty box top. If it does fit, then put it in place.
4. Repeat the process until you find a piece that fits.
5. Empty the box top back into the original box.
6. Repeat steps 3-5 until all the pieces are in the puzzle.

There are several images associated with this project.  In no particular order, the descriptions are as follows:
1. The animated gifs represent three actual implementations of the algorithm.  There is no effort to make the frame rates of the gifs meaningful.
2. The histogram is of 4000 implementations of the algorithm.  The datum depicted is the total number of piece-handlings during the assembly.  That is, on average, one would have to reach into the box around 20,000 times to take a piece out.  Most of the time, the piece that is removed will fail to fit into the current status of the puzzle, so it is placed in the box top and tried again later.
3. The dot plot is the average number of pieces that had to be chosen before a piece that fits is found at each step.  The plot is taken over 40 implementations of the algorithm.
