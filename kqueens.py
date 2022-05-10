import itertools


# Builds a SAT instance, in DIMACS cnf format, for the k queens problem

# Instance: A rectangular chess board with some number of pawns, and a number K
# Question: Is it possible to place K queens so that all pawns are attacked?

# For simplicity, we simply print the cnf to standard output


# Helper function to print a clause in DIMACS cnf format
# input is a list of variables, positive or negative. 
# We simply print them with a "0" at the end
def print_clause(c):
    print(" ".join(map(str, c+[0])))


W, H = 8, 8
K = 2
#pawns = [(1, 1), (2, 1), (4, 1)]
pawns = [(2, 1), (3, 1), (4, 1), (8, 2), (1, 3), (1, 4), (8, 4), (8, 7), (4, 8), (5, 8), (6, 8)] # (x, y) coords
num_pawns = len(pawns)
non_pawns = [(x, y) for x in range(1, W+1) for y in range(1, H+1) if (x, y) not in pawns] # open squares
print(non_pawns)

"""
The variables

We have a variable (x, y, i) saying that the ith queen is in square (x, y), 1 <= i <= K
"""
variables = [] # list of variables/tuples
varmap = {}    # map each tuple to its variable number for the cnf format
count = 1
for x, y in non_pawns:
    for i in range(1, K+1):
        variables.append((x, y, i))
        varmap[(x, y, i)] = count
        count += 1
print(varmap)
        
"""
The Clauses
"""
clauses = [] # list of variables/tuples

# First we build K clauses to say that each queen is on the board
print("c Each queen is on the board")
for i in range(1, K+1): # for each queen
    this_clause = []
    for x, y in non_pawns:
        this_clause.append(varmap[(x, y, i)])
    print_clause(this_clause)

# Now we build clauses to say that no queen is on the board twice
print("c No queen is on the board twice")
for i in range(1, K+1):
    for s1, s2 in itertools.combinations(non_pawns, 2):
        x1, y1 = s1
        x2, y2 = s2
        this_clause = [-varmap[(x1, y1, i)], -varmap[(x2, y2, i)]] # These squares are not both Queen i
        print_clause(this_clause)

# Now we build a clause for each pawn saying that some queen attacks it
print("c Each pawn is attacked")
for p in pawns:
    this_clause = []
    for dx, dy in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]: # The eight directions
        x, y = p[0] + dx, p[1] + dy
        while (x, y) not in pawns and x >= 1 and x <= W and y >= 1 and y <= H:
            for i in range(1, K+1): # for each queen
                this_clause.append(varmap[(x, y, i)])
            x, y = x+dx, y+dy

    print_clause(this_clause)
print("", flush=True)




from sys import stdin
def show_solution():
    vars = []
    while True:
        line = stdin.readline().strip().split(" ")
        for var in line:
            if var == "v" or var == "": continue
            if var == "0": break
            vars.append(int(var))
        if var == "0": break
    print("+---" * W + "+")
    for y in range(1, H+1):
        print("|", end="")
        for x in range(1, W+1):
            if (x, y) in pawns:
                print(" P |", end = "")
            elif len([(x, y, i) for i in range(1, K+1) if varmap[(x, y, i)] in vars]) > 0:
                print(" Q |", end = "")
            else:
                print("   |", end = "")
        print("")
        print("+---" * W + "+")

show_solution()