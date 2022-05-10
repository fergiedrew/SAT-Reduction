import itertools

# Make a solver that reduces grid problem #1 from:
# https://udallas.brightspace.com/d2l/le/content/47383/viewContent/504108/View


def parse_tuple(string_form):
    tuple_form = string_form.replace(",", "")
    tuple_form = tuple_form.replace("(", "")
    tuple_form = tuple_form.replace(")", "")
    # print(tuple_form)
    tuple_form = tuple(map(int, tuple_form.strip().split()))
    return tuple_form
# Problem Description:

# Given a rectangular grid with some of the squares blocked off, is 
# it possible to cover the unblocked squares with non-overlapping L trominos? 
# For example, for Figure A the answer would be "No." For Figure C, the answer 
# is "Yes," as shown in Figure D.
# The input format is the same as for Problem 1.

def all_Ls(H, W, blockages):
    directions = ['u', 'l', 'd', 'r']
    count = 1
    for y in range(H):
        for x in range(W):
            for dir in directions:
            
                if len(squares_of((x,y,dir), W, H, blockages)) == 3:
                    variables[(x,y)] = count
                    count += 1



                    


def squares_of(v, W, H, blockages):
    i, j, d = v
    answer = []
    if d == 'u':
        answer = [(i, j), (i-1, j), (i, j-1)]
    if d == 'l':
        answer = [(i,j), (i+1, j), (i, j-1)]
    if d == 'r':
        answer = [(i,j),(i+1,j),(i,j+1)]
    if d == 'd':
        answer = [(i,j),(i ,j-1),(i-1,j)]
    return [(s[0], s[1]) for s in answer if s[0] >= 1 and s[0] <= W and s[1] >= 1 and s[1] <= H and (s[0], s[1]) not in blockages]

def generate_variables(W, H, K, L, blockages):
    variables = {}
    directions = ['u', 'l', 'r', 'd']
    count = 1
    for x in range(1,W+1):
        for y in range(1, H+1):
            for dir in directions:
                for i in range(1,L+1):
                    placement = squares_of((x,y,dir), W, H, blockages)
                    # Check if the placement does not go off the board
                    print(f'{placement=} for {x} , {y}')
                    if len(placement) == 3:
                        for square in placement:
                            # Add all squares covered by placement to variables
                            variables[(square[0],square[1],i)] = count
                    count += 1
    print(variables)
    return variables

# Prints an array of variables as one string for one or statement
def print_clause(clause):
    full_clause = []
    for variable in clause:
        full_clause += str(variable) 
    print(" ".join(full_clause))

# COVER will be a large or statement such that every variable is accounted for.
def generate_COVER_clause(variables, W, H, K, L, blockages):
    COVER = []
    for y in range(1, H+1):
        for x in range(1, W+1):
            for l in range(1, L+1):
                if (x,y,l) in variables:
                    COVER.append(variables[(x,y,l)])

    return COVER

# ONCE will be a conjunction of or statements wach with 2 variables in them
def generate_ONCE_clause(variables, W, H, K, L, blockages):
    ONCE = []
    for y in range(1,H+1):
        for x in range(1,W+1):
            for l1, l2 in itertools.combinations(list(range(1,L+1)), 2):
                if (x,y) in blockages:
                    continue
                ONCE.append([-variables[(x,y,l1)], -variables[(x,y,l2)]])

    return ONCE

# BLOCKAGE will also be a large and clause
# For each blockage, check if any l covers it
def generate_BLOCKAGE_clause(variables, W, H, K, L, blockages):
    BLOCKAGE = []
    for blockage in blockages:
        x, y = blockage[0], blockage[1]
        for i in range(1, L+1):
            BLOCKAGE.append(-variables[(x,y,i)])
            

    return BLOCKAGE

def print_instance(COVER, ONCE, BLOCKAGE):
    combined_clauses = COVER + ONCE + BLOCKAGE
    for clause in combined_clauses:
        print_clause(clause)

if __name__ == "__main__":







    W, H, K, L = map(int, input().split())
    blockages = []
    for i in range(K):
        blockages.append(parse_tuple(input()))
    # print(blockages)
    # print(W, H, K, L)

    L_to_s = {}
    s_to_L = {}
    for l in all_Ls(H, W, blockages):
        L_to_s[l] = squares_of(l)
        for s in L_to_s[l]:
            if s not in s_to_L:
                s_to_L[s] = [l]
            else:
                s_to_L[s].append(l)
        

    # Creates a Variable for each L and Each Rotation of L
    variables = generate_variables(W, H, K, L, blockages)
    # Every Square is Covered By an L
    COVER = generate_COVER_clause(variables, W, H, K, L, blockages)
    # Every Square is Covered Only Once
    ONCE = generate_ONCE_clause(variables, W, H, K, L, blockages)
    # No Blockage is Covered
    BLOCKAGE = generate_BLOCKAGE_clause(variables, W, H, K, L, blockages)

    for clause in COVER:
        print(clause, 0)
    
    for clause in ONCE:
        print(clause[0], clause[1], 0)

    for clause in BLOCKAGE:
        print(clause, 0)


