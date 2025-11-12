from collections import Counter
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = Counter()
        a = None
        b = None
        n = len(grid)
        
        for i in grid:
            c.update(i)

        for i in range(1, n*n+1):
            if c[i] == 2:
                a = i
            elif c[i] == 0:
                b = i

        return [a, b]
                
    

sol = Solution()
print(sol.findMissingAndRepeatedValues([[1,3],[2,2]])) # [2, 