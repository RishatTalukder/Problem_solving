from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        # if the heightMap is empty
        if not heightMap:
            return 0
        
        # get the dimensions of the heightMap
        m,n = len(heightMap), len(heightMap[0])

        # create a min heap to store the height of the cells
        heap = []

        # create a visited set to store the visited cells
        visited = set()

        # add the border cells to the heap and visited set
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m-1 or j == 0  or j ==n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i,j))

        
        # create a variable to store the result
        result = 0

        # create a variable to store the level of the water
        level = 0

        #apply bfs

        while heap:
            height, i, j = heapq.heappop(heap)
            level = max(level,height)

            for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=x<m and 0<=y<n and (x,y) not in visited:
                    visited.add((x,y))
                    result += max(0,level-heightMap[x][y])
                    heapq.heappush(heap, (heightMap[x][y], x, y))

        return result

    
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

        if not heightMap or len(heightMap) <3 or len(heightMap[0])<3:
            return 0
        rows = len(heightMap)
        cols = len(heightMap[0])
        visited = [[False]*cols for _ in range(rows)]
        heap = []
        for i in range(rows):
            for j in range(cols):
                if i ==0 or i == rows-1 or j == 0 or j == cols-1:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))

        result = 0

        while heap:
            height, i ,j = heapq.heappop(heap)

            for ni,nj in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0<=ni<rows and 0<=nj<cols and not visited[ni][nj]:
                    visited[ni][nj] = True
                    result += max(0, height - heightMap[ni][nj])
                    heapq.heappush(heap, (max(height, heightMap[ni][nj]), ni, nj))

        return result