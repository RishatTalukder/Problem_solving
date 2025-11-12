from collections import deque

class Solution:
    def highestPeak(self, isWater):
        rows, cols = len(isWater), len(isWater[0])
        result = [[-1 for _ in range(cols)] for _ in range(rows)]

        queue = deque()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j] == 1:
                    result[i][j] = 0
                    queue.append((i,j))

        
        while queue:
            layer = len(queue)

            for _ in range(layer):
                i,j = queue.popleft()

                for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                    new_i, new_j = i+x, j+y
                    
                    if 0<=new_i<rows and 0<=new_j<cols and result[new_i][new_j] == -1:
                        result[new_i][new_j] = result[i][j] + 1
                        queue.append((new_i,new_j))

        return result
    

sol = Solution()
print(sol.highestPeak([[0,1],[0,0]])) # [[1,0],[2,1]]