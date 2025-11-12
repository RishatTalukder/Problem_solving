from collections import deque 
from typing import List
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid), len(grid[0])
        queue = deque()
        fresh_c = 0
        minutes = 0

        for r in range(rows):
            for c in range(cols): 
                if grid[r][c] == 2:
                    queue.append((r,c))
                
                elif grid[r][c] == 1:
                    fresh_c += 1
        
        if fresh_c == 0:
            return 0
        
        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while queue:

            for i in range(len(queue)):
                r,c = queue.popleft()
                for dx,dy in directions:
                    nr,nc = r+dx, c+dy

                    if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]==1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_c -= 1

            if queue:
                minutes += 1

        return minutes if fresh_c == 0 else -1
    

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh_count = 0
        minute = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i,j))

                else:
                    fresh_count += 1
        
        if fresh_count == 0:
            return 0

        directions = [(0,1),(0,-1), (1,0), (-1,0)]

        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()

                for dx,dy in directions:
                    nr,nc = r+dx, c+dy

                    if 0<=nr<rows and 0<=nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        fresh_count -= 1

                
            if queue:
                minute += 1

        
        return minute if fresh_count == 0 else -1
    

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])) #4