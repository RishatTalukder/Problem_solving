board = []

cols_taken = set()

def set_diagonal(x,y, board):
    for i in range(8):
        for j in range(8):
            if board[i][j] >=0:
                if i - j == x-y:
                    board[i][j] += 1

                if i+j == x + y:
                    board[i][j] += 1

def reset_diagonal(x,y, board):
    for i in range(8):
        for j in range(8):
            if board[i][j] > 0:
                if i - j == x-y:
                    board[i][j] -= 1

                if i+j == x + y:
                    board[i][j] -= 1

ans = 0  

def place_queen(row, board):
    global ans
    if row == 8:
        ans += 1
        return
    
    for col in range(8):
        if board[row][col] == -1:
            continue

        if col in cols_taken:
            continue

        if board[row][col] > 0:
            continue

        cols_taken.add(col)
        set_diagonal(row, col, board)
        
        place_queen(row+1, board)
        
        cols_taken.remove(col)
        reset_diagonal(row, col, board)

def row_maper(x):
    if x == '.':
        return 0
    
    if x == '*':
        return -1

for i in range(8):
    row = list(map(row_maper, input()))
    board.append(row)

# print(*board, sep='\n')
# set_main_diagonal(4,2,board)
place_queen(0,board)
print(ans)