from satispy import Variable, Cnf
from satispy.solver import Minisat

H = 8 # height of board
W = 8 # width of board
def squares_of(v):
    i, j, d = v
    answer = []
    if d == 'u':
        answer = [(i, j), (i, j-1), (i, j+1), (i-1, j)]
    if d == 'd':
        answer = [(i, j), (i, j-1), (i, j+1), (i+1, j)]
    if d == 'l':
        answer = [(i, j), (i, j-1), (i+1, j), (i-1, j)]
    if d == 'r':
        answer = [(i, j), (i-1, j), (i, j+1), (i+1, j)]
    return [(s[0], s[1]) for s in answer if s[0] >= 0 and s[0] < H and s[1] >= 0 and s[1] < W]

# Start by building a list of all Ts that lie inside the board
all_tets = []
for i in range(H):
    for j in range(W):
        for dir in ['u', 'd', 'l', 'r']:
            if len(squares_of((i, j, dir))) == 4:
                all_tets.append((i, j, dir))

# Build a variable for each tetromino
varz = {}
for t in all_tets:
    s = str(t) # string
    v = Variable(s) # variable
    varz[t] = v # tuple as key in varz dictionary

# Loop over the variables = tetrominos
# Map each tetromino to its squares, and
# Map each square to the list of tetrominos that cover it
tet_to_s = {}
s_to_tet = {}
for t in all_tets:
    tet_to_s[t] = squares_of(t)
    for s in tet_to_s[t]:
        if s not in s_to_tet:
            s_to_tet[s] = [t]
        else:
            s_to_tet[s].append(t)
    
# Build the COVER clause, which says that each square is covered
COVER = Cnf() # Empty clause, to get things started
for i in range(H):
    for j in range(W):
        c = Cnf()
        for t in s_to_tet[(i, j)]:
            c |= varz[t]
        COVER &= c

# Build the ONCE clause, that says no overlapping tetrominos are selected
ONCE = Cnf()
for i in range(H): # loop over the squares
    for j in range(W):
        tets = s_to_tet[(i, j)]
        for t1 in range(len(tets)): # loop over the pairs of Ts covering this square
            for t2 in range(t1+1, len(tets)):
                ONCE &= (-varz[tets[t1]] | - varz[tets[t2]]) # Not both Ts picked
# Build the full clause
exp = COVER & ONCE
solver = Minisat()
solution = solver.solve(exp)
