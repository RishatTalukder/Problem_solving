from typing import List

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        res = [pref[0]]

        prev = pref[0]

        for i in range(1,len(pref)):
            xor = prev^pref[i]
            res.append(xor)
            prev =xor

        return res

sol = Solution()
print(sol.findArray([5,2,0,3,1])) # [1,3,0,4]