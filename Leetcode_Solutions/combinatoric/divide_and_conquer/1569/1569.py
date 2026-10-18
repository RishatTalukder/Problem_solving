class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        MOD = 10**9 + 7

        def dfs(nums):
            m = len(nums)

            if m < 3:
                return 1

            left = [a for a in nums if a < nums[0]]
            right = [a for a in nums if a > nums[0]]

            return dfs(left)*dfs(right)*comb(m-1, len(left))%MOD

        return (dfs(nums)-1)%MOD