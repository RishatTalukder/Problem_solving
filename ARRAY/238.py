
class Solution:
    def productExceptSelf(self, nums):
        result = [0] * len(nums)
        product = 1

        for i in range(len(nums)):
            result[i] = product
            product *= nums[i]

        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]

        return result