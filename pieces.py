
# Pieces creates a set of all the elements of the cartesian product range(50)Xrange(30). This also acts at the position
# of each piece.

Pieces = set()
for i in range(50):
    for j in range(30):
        Pieces.add((i, j))

UsedPieces = set()
TempPieces = set()
TempPieces2 = set()
