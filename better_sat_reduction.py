from itertools import combinations
def parse_tuple(string_form):
    tuple_form = string_form.replace(",", "")
    tuple_form = tuple_form.replace("(", "")
    tuple_form = tuple_form.replace(")", "")
    # print(tuple_form)
    tuple_form = tuple(map(int, tuple_form.split()))
    return tuple_form

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
        answer = [(i,j),(i,j+1),(i-1,j)]
    return [(s[0], s[1]) for s in answer if s[0] >= 1 and s[0] <= W and s[1] >= 1 and s[1] <= H and (s[0], s[1]) not in blockages]

if __name__ == "__main__":
    W, H, K, L = map(int, input().split())
    blockages = []
    for i in range(K):
        blockages.append(parse_tuple(input()))

    count = 1
    L_to_squares = {}
    squares_to_L = {}
    for y in range(1,H+1):
        for x in range(1,W+1):
            for l in range(1,L+1):
                for dir in ['u', 'd', 'l', 'r']:
                    if len(squares_of((x,y,dir), W, H, blockages)) == 3:
                        if count in L_to_squares:
                            L_to_squares[count] += squares_to_L
                        else:
                            L_to_squares[count] = squares_to_L
                        for square in squares_to_L:
                            squares_to_L[square] = count

                        count += 1

    ONCE = []
    COVER = []
    for x in range(1,W+1):
        for y in range(1,H+1):
            if (x,y) in blockages:
                continue
            for l in range(1, L+1):
                if (x,y,l) in squares_to_L:
                    COVER.append(squares_to_L[(x,y)]

    for x in range(1,W+1):
        for y in range(1,H+1):
            if (x,y) in blockages:
                continue
            for l1, l2 in combinations(-L for L in squares_to_L[(x,y)]):
                clause = l1, l2
                ONCE.append(clause)

    for clause in COVER:
        print(clause)
    for clause in ONCE:
        string = " ".join(clause)








                            
                        
    
