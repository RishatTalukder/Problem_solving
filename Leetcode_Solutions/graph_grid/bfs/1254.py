class Solution:

    def bfs(self, i,j,m,n, grid, visited):
        q= deque([(i,j)])
        visited[i][j] = True

        is_closed = True

        dirx = [0,1,0,-1]
        diry = [1,0,-1, 0]

        while q:
            x, y = q.popleft()

            for i in range(4):
                r,c = x+dirx[i], y + diry[i]

                if r < 0 or r >=m or c < 0 or c >= n:
                    is_closed = False 

                elif grid[r][c] == 0 and not visited[r][c]:
                    q.append((r,c))
                    visited[r][c] = True

        return is_closed



    def closedIsland(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])        

        visited = [[False]*n for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j] and self.bfs(i,j,m,n, grid, visited):
                    count += 1

        return count 