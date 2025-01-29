from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomera = 0

        for a,b in points:
            d = {}
            for x,y in points:
                dist = (a-x)**2 + (b-y)**2
                if dist in d:
                    boomera += 2 * d[dist]
                    d[dist] += 1
                else:
                    d[dist] = 1


        return boomera
    
sol = Solution()
print(sol.numberOfBoomerangs([[0,0],[1,0],[2,0],[3,0]])) # 2