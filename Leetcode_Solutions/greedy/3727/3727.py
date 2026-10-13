class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]**2

        nums.sort(key=lambda x : abs(x))

        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]

        ans = 0
        for i in range(len(left)):
            ans += right[i]**2 -left[i]**2


        return ans + (right[i+1]**2 if i+1 < len(right) else 0)
    
