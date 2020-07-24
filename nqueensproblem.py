def isFeasable(board, row, col,n):
    #checking in the row
    for i in range(0,n):
        if board[row][i] == 1:
            return False
    #checking in the column
    for i in range(0,n):
        if board[i][col] == 1:
            return False
    
    #checking for right diagnol
    i = row
    j= col
    while (i>=0 and j < n):
        if board[i][j] == 1:
            return False
        i=i-1
        j=j+1

    #checking for left diagnol
    i = row
    j= col
    while (i>= 0 and j >= 0):
        if board[i][j] == 1:
            return False
        i=i-1
        j=j-1

    return True 

def nQueens(board,row,n):
    if row < n:
        for col in range(0,n):
            if isFeasable(board, row, col,n):
                board[row][col]=1
                nQueens(board,row+1,n)
                board[row][col] = "-"
    else:
        print("Solution is")
        for i in range(0, n):
            for j in range(0,n):
                print(board[i][j], end=" ")
            print("\n\n")


r=5
c=5
board = [["-" for x in range(r)] for y in range(c)]

nQueens(board,0,r)