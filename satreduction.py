from itertools import combinations

def parse_tuple(string_form):
    tuple_form = string_form.replace(",", "")
    tuple_form = tuple_form.replace("(", "")
    tuple_form = tuple_form.replace(")", "")
    # print(tuple_form)
    tuple_form = tuple(map(int, tuple_form.split()))
    return tuple_form

def squares_of(v):
    i, j, d = v
    answer = []
    if d == 'u':
        answer = [(i, j), (i-1, j), (i, j-1)]
    if d == 'l':
        answer = [(i,j), (i+1, j), (i, j-1)]
    if d == 'r':
        answer = [(i,j),(i+1,j),(i,j+1)]
    if d == 'd':
        answer = [(i,j),(i,j+1),(i-1,j)]
    return [(s[0], s[1]) for s in answer if s[0] >= 1 and s[0] <= W and s[1] >= 1 and s[1] <= H and (s[0], s[1]) not in blockages]

if __name__ == "__main__":
    global W, H, K, L 
    W, H, K, L = map(int, input().split())
    global blockages 
    blockages = [parse_tuple(input()) for k in range(K)]


    all_Ls = []
    for i in range(1, W+1):
        for j in range(1, H+1):
            for dir in ['u', 'd', 'l', 'r']:
                if len(squares_of((i, j, dir))) == 3:
                    all_Ls.append((i, j, dir))

    # Build a variable for each L moninmo
    var_map = {}
    for i, l in enumerate(all_Ls):
        var_map[l] = i + 1

    # Loop over the variables = tetrominos
    # Map each tetromino to its squares, and
    # Map each square to the list of tetrominos that cover it
    L_to_s = {}
    s_to_L = {}
    for l in all_Ls:
        L_to_s[l] = squares_of(l)
        for s in L_to_s[l]:
            if s not in s_to_L:
                s_to_L[s] = [l]
            else:
                s_to_L[s].append(l)


    # Build COVER Clause
    COVER = []
    for x in range(1,W+1):
        for y in range(1, H+1):
            clause = []
            # Don't check if a blocked square is covered
            if (x,y) in blockages:
                continue
            for L in s_to_L[(x,y)]: #Saying (1,1) not in s_to_L
                clause.append(var_map[L])
            COVER.append(" ".join(map(str, clause)))

    # Build a ONCE Clause
    ONCE = []
    for x in range(1,W+1):
        for y in range(1,H+1):
            if (x,y) in blockages:
                continue
            all_ls_for_square = [-var_map[l] for l in s_to_L[(x,y)]]
            for l1, l2 in combinations(all_ls_for_square, 2):
                ONCE.append(" ".join(map(str, [l1,l2])))

    # Print Clauses
    for clause in COVER: print(clause, 0)
    for clause in ONCE: print(clause, 0)








                            
                        
    
