def queen_attack_pos(i,j):
    for k in range(0,N):   # row and column check
        if board[i][k]=='Q' or board[k][j]=='Q':
            return True

    for k in range(0,N):        # diagonal check
        for l in range(0,N):
            if(k+l==i+j)or(k-l==i-j):
                if board[k][l]=='Q':
                    return True
    return False
def N_queens(n):
    if(n==0):    #solution
        return True
    for i in range(0,N):
        for j in range(0,N):
            if(not(queen_attack_pos(i,j))) and (board[i][j]!='Q'):
                board[i][j]='Q'
                if N_queens(n-1)==True:
                    return True
                board[i][j]='_'

    return False

N=int(input("Enter number of Queens: "))
board=[['_']*N for _ in range(N)]

N_queens(N)
print("Solution of ",N," Queens Problem ")
for i in board:
    print(i)

