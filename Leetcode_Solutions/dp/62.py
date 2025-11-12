class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            
            if i == 0 and j == 0:
                return 1
            
            if (i,j) in cache:
                return cache[(i,j)]
            
            cache[(i,j)] = dfs(i-1,j) + dfs(i,j-1)

            return cache[(i,j)]

        return dfs(m-1,n-1)
    

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1]*n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]


        return grid[m-1][n-1]