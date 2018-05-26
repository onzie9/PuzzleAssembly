import random
from pieces import Pieces
from pieces import UsedPieces
from functions import transfer

import os
import re

# Open two files where the data will be stored.
directory = os.getcwd()
fob = directory + "/" + "OrderedEdges.txt"
fobnew = directory + "/" + "OrderedEdgesWithSteps.txt"
orderededges = open(fob, "w+")
orderededgeswithsteps = open(fobnew, "w+")

a = random.choice(tuple(Pieces))  # Picks out a first random piece from which to start.  It has nothing to connect to,
                                  # so it stays out.
transfer(a, Pieces, UsedPieces)

# Start randomly choosing pieces and see if they attach to a.
i = 2
a = str(a)
a = re.sub("\(", "{", a)
a = re.sub("\)", "}", a)
orderededges.write(("{1, " + a + "}, "))  # Records the first entry of "ordered edges" which is keeping track of how
                                          # long it took to find a piece that fit.
step = 0  # Starts the count to see how many choices needed to be made before a fitting piece was found.
while len(Pieces) > 0:
    b = random.choice(tuple(Pieces))
    for piece in UsedPieces:
        if abs(b[0]-piece[0]) == 1 and b[1] - piece[1] == 0:  # Checking to see if the new random piece is a match to
                                                              # to any existing pieces.
            transfer(b, Pieces, UsedPieces)  # If it matches, move it the used pieces box.
            b = str(b)
            b = re.sub("\(", "{", b)
            b = re.sub("\)", "}", b)
            orderededges.write("{" + str(i) + ", " + b + "}, ")  # Record the data point in a way that Mathematica
                                                                 # can read.
            orderededgeswithsteps.write(str(step) + ", ")
            i += 1
            step = 0
            break
        elif abs(b[1]-piece[1]) == 1 and b[0] - piece[0] == 0:  #  Checks the same stuff as before, but in the vertical
                                                                #  direction.
            transfer(b, Pieces, UsedPieces)
            b = str(b)
            b = re.sub("\(", "{", b)
            b = re.sub("\)", "}", b)
            orderededges.write("{" + str(i) + ", " + b + "}, ")
            orderededgeswithsteps.write(str(step) + ", ")
            i += 1
            step = 0
            break
    step += 1
print(step + i)
