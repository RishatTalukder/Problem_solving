class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # diagonals
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, d, can_turn, target):
            nx, ny = x + DIRS[d][0], y + DIRS[d][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            best = dfs(nx, ny, d, can_turn, 3 - target)  # continue straight
            if can_turn:
                best = max(best, dfs(nx, ny, (d + 1) % 4, False, 3 - target))  # turn
            return best + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # must start from 1
                    for d in range(4):
                        res = max(res, dfs(i, j, d, True, 2) + 1)
        return res