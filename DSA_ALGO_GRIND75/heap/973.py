from typing import List
import heapq

class Solution:
    def distance(self, x,y):
        return (x**2 + y**2)**0.5

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.heap = []
        for point in points:
            x,y = point
            dist = self.distance(x,y)
            heapq.heappush(self.heap, (dist, x, y),)
        
        print(self.heap)
        res = []
        for i in range(k):
            dist, x, y = heapq.heappop(self.heap)
            res.append([x,y])


        return res  
    

points = [[1,3],[-2,2]]
k = 1
sol = Solution()
print(sol.kClosest(points, k)) # [[-2,2]]
  