# class Solution:
#     def missingNumber(self, nums: List[int]) -> int:
#         nums.sort()

#         for i in range(len(nums)+1):
#             if i < len(nums) and nums[i] != i :
#                 return i

#         return i


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(i for i in range(len(nums)+1))

        for i in nums:
            if i in nums_set:
                nums_set.remove(i)

        return nums_set.pop()


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for i in range(len(nums)+1):
            if i not in nums_set:
                return i
