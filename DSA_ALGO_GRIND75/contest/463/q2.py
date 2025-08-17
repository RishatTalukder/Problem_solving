from typing import List

class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        MOD = 10**9 + 7
        x = queries  

        for li, ri, ki, vi in x:
            idx = li
            while idx <= ri:
                nums[idx] = (nums[idx] * vi) % MOD
                idx += ki

        result = 0
        for num in nums:
            result ^= num
        return result 