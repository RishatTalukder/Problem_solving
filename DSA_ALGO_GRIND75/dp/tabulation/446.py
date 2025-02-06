from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_slices = 0

        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                difference = nums[i] - nums[j]

                if difference < -2**31 or difference > 2**31-1:
                    continue
                
                count = dp[j][difference] if difference in dp[j] else 0

                total_slices += count
                dp[i][difference] += count + 1

        return total_slices