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

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        prev = pref[0]

        for i in pref[1:]:
            val = prev^i
            ans.append(val)
            prev = i

        return ans

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        prev=pref[0]
        ans = [pref[0]]

        for i in pref[1:]:
            ans.append(prev^i)
            prev = i

        return ans