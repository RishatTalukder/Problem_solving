class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = 0
        maxx = nums[0]

        for i in nums:
            total = max(total+i, i)
            maxx = max(total, maxx)

        return maxx