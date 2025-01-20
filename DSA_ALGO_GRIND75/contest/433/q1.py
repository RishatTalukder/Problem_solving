class Solution:
    def subarraySum(self, nums) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            start = max(0, i - nums[i])
            res += sum(nums[start:i + 1])
        return res
    

