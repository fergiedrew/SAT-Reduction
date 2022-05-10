# Make a solver that reduces grid problem #1 from:
# https://udallas.brightspace.com/d2l/le/content/47383/viewContent/504108/View


def parse_tuple(string_form):
    tuple_form = string_form.replace(",", "")
    tuple_form = tuple_form.replace("(", "")
    tuple_form = tuple_form.replace(")", "")
    tuple_form = map(int, tuple_form.split())
    tuple_form = tuple(tuple_form)
    return tuple_form
# Problem Description:

# Given a rectangular grid with some of the squares blocked off, is 
# it possible to cover the unblocked squares with non-overlapping L trominos? 
# For example, for Figure A the answer would be "No." For Figure C, the answer 
# is "Yes," as shown in Figure D.
# The input format is the same as for Problem 1.

def generate_variables(W, H, K, L, blockages):
    variables = []
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
    blockages = [] # Initialize list of blockages (in the form of tuples) not allowed to be covered
    for i in range(K):
        blockage = parse_tuple(input())
        blockages.append(blockage)
    # Creates a Variable for each L and Each Symmetry of L
    variables = generate_variables(W, H, K, L, blockages)
    # Every Square is Covered By an L
    COVER = generate_COVER_clause(variables, W, H, K, L, blockages)
    # Every Square is Covered Only Once
    ONCE = generate_ONCE_clause(variables, W, H, K, L, blockages)
    # No Blockage is Covered
    BLOCKAGE = generage_BLOCKAGE_clause(variables, W, H, K, L, blockages)
    print_instance(COVER, ONCE, BLOCKAGE)



