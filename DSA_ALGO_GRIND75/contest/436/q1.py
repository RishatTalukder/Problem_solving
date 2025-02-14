from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        
        row_diagonals = []
        col_diagonals = []

        for k in range(n):
            row_diagonal = [grid[i+k][i] for i in range(n-k)]
            row_diagonals.append(sorted(row_diagonal, reverse=True))
        
        for k in range(1, n):
            col_diagonal = [grid[i][i+k] for i in range(n-k)]
            col_diagonals.append(sorted(col_diagonal))

        matrix = [[None] * n for _ in range(n)]

        for k, diag in enumerate(row_diagonals):
            for i, val in enumerate(diag):
                matrix[i+k][i] = val

        for k, diag in enumerate(col_diagonals, start=1):
            for i, val in enumerate(diag):
                matrix[i][i+k] = val

        return matrix
    

sol = Solution()
print(sol.sortMatrix([[1]]))