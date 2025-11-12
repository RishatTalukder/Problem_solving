class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c = 0

        for i in range(2, len(nums)):
            if nums[i-2] == 0:
                c += 1
                nums[i-2] = nums[i-2] ^ 1
                nums[i-1] = nums[i-1] ^ 1
                nums[i] = nums[i] ^ 1

        if sum(nums) == len(nums):
            return c
        
        return -1