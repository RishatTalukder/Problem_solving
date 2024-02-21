# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()

#         for i in range(len(nums)+1):
#             if i < len(nums) and nums[i] != i :
#                 return i

#         return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for ind, val in enumerate(nums):
            if ind != val:
                return ind
            
        return len(nums)