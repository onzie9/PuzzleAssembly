# This file creates a histogram for the puzzle.  Specifically, it puts together 4000 puzzles (or whatever number) and
# records the number of pieces it took to find the first matching piece, then the second, then the third, etc.
# The histogram describes these data.

import random
from pieces import Pieces
from pieces import UsedPieces
from functions import transfer

import os

directory = os.getcwd()
fob = directory + "/" + "histogramdata.txt"
histdata = open(fob, "w+")


temp = Pieces.copy()
tempused = UsedPieces.copy()
a = random.choice(tuple(temp))
transfer(a, temp, tempused)

steps = []
i = 2
step = 0
for j in range(4000):
    while len(temp) > 0:
        b = random.choice(tuple(temp))
        for piece in tempused:
            if abs(b[0]-piece[0]) == 1 and b[1] - piece[1] == 0:
                transfer(b, temp, tempused)
                i += 1
                break
            elif abs(b[1]-piece[1]) == 1 and b[0] - piece[0] == 0:
                transfer(b, temp, tempused)
                i += 1
                break
        step += 1
    temp = Pieces.copy()
    tempused = UsedPieces.copy()
    a = random.choice(tuple(temp))
    transfer(a, temp, tempused)
    steps.append(step + i)
    step = 0
    i = 2
histdata.write(str(steps))
