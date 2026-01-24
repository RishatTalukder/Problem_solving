class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        ans = float('-inf')

        while left < right:
            sm = nums[left] + nums[right]
            ans = max(sm, ans)
            left += 1
            right -= 1 

        return ans