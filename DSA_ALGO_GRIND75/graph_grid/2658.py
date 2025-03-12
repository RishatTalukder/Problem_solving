class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_fish = 0

        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            
            fish = grid[i][j]
            grid[i][j] = -1

            for dir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_i, new_j = i + dir[0], j + dir[1]
                if 0<=new_i<rows and 0<=new_j<cols and grid[new_i][new_j] > 0:
                    fish += dfs(new_i, new_j)

            return fish

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    max_fish = max(max_fish, dfs(i, j))

        return max_fish



        