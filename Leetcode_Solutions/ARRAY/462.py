class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        median = nums[n // 2]
        res = 0

        for num in nums:
            res += abs(num - median)

        return res
        