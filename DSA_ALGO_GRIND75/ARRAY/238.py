
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
    


class Solution:
    def productExceptSelf(self, nums):
        """
        Calculates the product of all elements in the given list except self.

        Args:
            nums (List[int]): The input list of integers.

        Returns:
            List[int]: The list of products of all elements except self.

        Algorithm:
        1. Initialize mul_except_zero as 1 and zero_count as 0.
        2. Iterate through each element num in nums.
            a. If num is not equal to 0, multiply it with mul_except_zero.
            b. If num is equal to 0, increment zero_count by 1.
        3. If zero_count is greater than 1, return a list of zeros with the same length as nums.
        4. If zero_count is equal to 1, return a list where all elements are 0 except for the zeros in nums, which are replaced with mul_except_zero.
        5. If zero_count is 0, return a list where each element is the result of dividing mul_except_zero by the corresponding element in nums.
        """

        mul_except_zero = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                mul_except_zero *= num
            else:
                zero_count += 1

        if zero_count > 1:
            return [0] * len(nums)
        elif zero_count == 1:
            return [0 if num != 0 else mul_except_zero for num in nums]
        
        return [mul_except_zero // num for num in nums]