# Make a solver that reduces grid problem #1 from:
# https://udallas.brightspace.com/d2l/le/content/47383/viewContent/504108/View


def parse_tuple(string_form):
    tuple_form = string_form.replace(",", "")
    tuple_form = tuple_form.replace("(", "")
    tuple_form = tuple_form.replace(")", "")
    print(tuple_form)
    tuple_form = tuple(map(int, tuple_form.strip().split()))
    return tuple_form
# Problem Description:

# Given a rectangular grid with some of the squares blocked off, is 
# it possible to cover the unblocked squares with non-overlapping L trominos? 
# For example, for Figure A the answer would be "No." For Figure C, the answer 
# is "Yes," as shown in Figure D.
# The input format is the same as for Problem 1.


def squares_of(v, W, H, i):
    i, j, d = v
    answer = []
    if d == 'u':
        answer = [(i, j), (i+1, j), (i, j + 1)]
    if d == 'l':
        answer = [(i,j),(i -1, j - 1),(i, j + 1)]
    if d == 'r':
        answer = [(i,j),(i-1,j-1),(i,j-1)]
    if d == 'd':
        answer = [(i,j),(i+1,j),(i,j - 1)]
    return (i, [(s[0], s[1]) for s in answer if s[0] >= 0 and s[0] < H and s[1] >= 0 and s[1] < W])

def generate_variables(W, H, K, L):
    variables = {}
    directions = ['u', 'l', 'r', 'd' ]
    for x in range(1,W+1):
        for y in range(1, H+1):
            for dir in directions:
                for i in range(L):
                    placement = squares_of((x,y,dir), W, H, i)
                    # Check if the placement does not go off the board
                    if len(placement[1]) == 3:
                        variables[(x,y,i)] = placement[1]
    return variables

def generate_COVER_clause(variables, W, H, K, L, blockages):
    COVER = []
    return COVER

def generate_ONCE_clause(variables, W, H, K, L, blockages):
    ONCE = []
    return ONCE

def generage_BLOCKAGE_clause(variables, W, H, K, L, blockages):
    BLOCKAGE = []
    return BLOCKAGE

def print_instance(COVER, ONCE, BLOCKAGE):
    combined_clauses = COVER + ONCE + BLOCKAGE
    for clause in combined_clauses:
        print(clause)

if __name__ == "__main__":
    W, H, K, L = map(int, input().split())
    blockages = []
    for i in range(K):
        blockages.append(parse_tuple(input()))
    print(blockages)
    print(W, H, K, L)

    # Creates a Variable for each L and Each Rotation of L
    variables = generate_variables(W, H, K, L, blockages)
    # Every Square is Covered By an L
    COVER = generate_COVER_clause(variables, W, H, K, L, blockages)
    # Every Square is Covered Only Once
    ONCE = generate_ONCE_clause(variables, W, H, K, L, blockages)
    # No Blockage is Covered
    BLOCKAGE = generage_BLOCKAGE_clause(variables, W, H, K, L, blockages)
    print_instance(COVER, ONCE, BLOCKAGE)



