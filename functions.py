# The main purpose of file is to define the function "transfer" which moves unused pieces from the main box to the
# empty box. makeGraph and seeGraph didn't end up being used for this particular project.

import pygraphviz as pgv


def transfer(a, b, c):
    if a in b:
        b.remove(a)
    else:
        print(str(a) + " not in the set")
    c.add(a)


def makegraph(s):
    A = pgv.AGraph()
    for i in range(0, len(s)):
        for j in range(i, len(s)):
            if abs(s[i][0] - s[j][0]) == 1 and s[i][1] - s[j][1] == 0:
                A.add_edge(s[j], s[i])
            elif abs(s[i][1] - s[j][1]) == 1 and s[i][0] - s[j][0] == 0:
                A.add_edge(s[j], s[i])
    return(A)


def seegraph(g):
    A=makegraph(g)
    A.write('simple.dot')
    B = pgv.AGraph('simple.dot')
    B.layout()
    B.draw('simple.png')


nodes = []
for i in range(5):
    for j in range(5):
        nodes.append((i,j))
