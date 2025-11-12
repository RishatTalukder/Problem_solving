class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        res = float('-inf')
        for i in range(1,len(nums)):
            res = max(res, abs(nums[i]-nums[i-1]))


        return res
