class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n,N = 3,9
        rows = [[0]*(N+1) for _ in range(N)]
        cols = [[0]*(N+1) for _ in range(N)]
        boxes = [[0]*(N+1) for _ in range(N)]
        solved = False

        def couldPlace(val, row,col):
            idx = (row//3)*3 + col//3

            return rows[row][val] + cols[col][val] + boxes[idx][val] == 0

        def placeNumber(val,row,col):
            idx = (row//3)*3 + col//3
            rows[row][val] += 1
            cols[col][val] += 1 
            boxes[idx][val] += 1
            board[row][col] = str(val)

        
        def removeNumber(val,row,col):
            idx = (row//3)*3 + col//3
            rows[row][val] -= 1
            cols[col][val] -= 1 
            boxes[idx][val] -= 1
            board[row][col] = '.'


        def placeNext(row,col):
            nonlocal solved
            if row == N-1 and col == N-1:
                solved = True

            elif col == N-1:
                backtrack(row+1, 0)

            
            else:
                backtrack(row, col+1)


        def backtrack(row,col):
            nonlocal solved

            if board[row][col] == '.':
                for val in range(1,10):
                    if couldPlace(val,row,col):
                        placeNumber(val, row, col)
                        placeNext(row,col)
                        if not solved:
                            removeNumber(val,row,col)

            else:
                placeNext(row,col)


        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)


        backtrack(0,0)
            