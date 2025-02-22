from typing import List
from math import comb


class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        quantity = 1
        total_sums = 0

        for i in range(n):
            total_sums += quantity*(nums[i]+nums[-i-1])
            quantity = 2*quantity - comb(i,k-1,exact=True)

        return total_sums%(10**9+7)