from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        arrow = points[0][1]

        res = 1

        for i in range(1,len(points)):
            if points[i][0] > arrow:
                res += 1
                arrow = points[i][1]

        return res
    

sol = Solution()
print(sol.findMinArrowShots([[10,16],[2,8],[1,10],[7,12]])) # 2