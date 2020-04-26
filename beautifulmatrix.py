import math

def moves(matrix: dict):
    ymoves=0
    xmoves=0
    counter=0
    for key in matrix:
        counter= counter+1
        if 1 in matrix[key]:
            mid = math.ceil(len(matrix[key])/2)
            xmoves = abs(mid - (matrix[key].index(1)+1))
            ymoves= abs(mid- counter)
            print(xmoves, ymoves)
    return xmoves+ymoves

matrix={
    "a":[0 ,0, 0, 0, 0],
    "b":[0, 0, 0, 0, 0],
    "c":[0 ,0, 0, 0, 0],
    "d":[1 ,0, 0, 0, 0],
    "e":[0 ,0, 0, 0, 0]
}


print(moves(matrix))