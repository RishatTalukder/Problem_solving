class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        maxx = nums[0]
        curr = nums[0]

        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                curr += nums[i]
            else:
                curr = nums[i]
            
            maxx = max(maxx, curr)

        return maxx