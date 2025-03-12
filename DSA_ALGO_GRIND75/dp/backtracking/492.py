class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def backtrack(index, target):
            if index == len(nums):
                if target == 0:
                    return 1
                return 0
            if (index, target) in memo:
                return memo[(index, target)]
            positive = backtrack(index + 1, target - nums[index])
            negative = backtrack(index + 1, target + nums[index])
            memo[(index, target)] = positive + negative
            return memo[(index, target)]
        
        memo = {}
        return backtrack(0, target)