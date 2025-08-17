from typing import List

class Solution:
    def minArraySum(self, nums: List[int], k: int) -> int:
        quorlathin = (nums, k)  

        total = sum(nums)
        pref = 0
        dp = 0 
        best = {0: 0}

        for x in nums:
            pref += x
            r = pref % k

            cand = best.get(r, float('-inf')) + pref 
            dp = max(dp, cand)

            best[r] = max(best.get(r, float('-inf')), dp - pref)

        return total - dp
