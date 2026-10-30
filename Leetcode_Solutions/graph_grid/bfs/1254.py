from collections import deque


class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        
        def bfs(i, j, m, n, grid, visited):
            q = deque([(i,j)])

            visited[i][j] = True

            dir = [-1, 0, 1, 0, -1]

            close = True

            while q:
                x, y = q.popleft()

                for i in range(4):
                    r,c = x+dir[i], y+dir[i+1]

                    if r < 0 or r >= m or c < 0 or c >= n:
                        close = False
                        
                    elif grid[r][c] == 0 and not visited[r][c]:
                        q.append((r,c))
                        visited[r][c] = True

            return close

        m = len(grid)
        n= len(grid[0])

        visited = [[False]*n for _ in range(m)]

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j] and bfs(i, j, m , n, grid, visited):
                    count += 1


        return count


# my version

class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        def bfs(x, y, m,n, grid, visited):
            q = deque([(x,y)])
            visited.add((x,y))
            
            dir = [-1,0,1,0,-1]

            close = True

            while q:
                i,j = q.popleft()

                for k in range(4):
                    r,c = i+dir[k], j+dir[k+1]

                    if r<0 or r >= m or c < 0 or c >= n:
                        close = False

                    elif grid[r][c] == 0 and (r, c) not in visited:
                        q.append((r,c))
                        visited.add((r,c))


            return close


        m = len(grid)
        n = len(grid[0])

        visited = set()

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and (i, j) not in visited and bfs(i, j, m, n, grid, visited):
                    count += 1

        return count
