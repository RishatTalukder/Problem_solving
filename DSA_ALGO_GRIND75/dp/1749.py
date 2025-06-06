class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        mn = 0
        mx = 0
        total = 0

        for num in nums:
            total += num
            mn = min(mn,total)
            mx = max(mx,total)

        return mx-mn
    

from typing import List

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        min_sum = float('inf')
        curr_max = 0
        curr_min = 0

        for num in nums:
            curr_max = max(num, curr_max + num)
            curr_min = min(num, curr_min + num)

            max_sum = max(max_sum, curr_max)
            min_sum = min(min_sum, curr_min)

        return max(max_sum, -min_sum)
