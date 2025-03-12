class Solution:
    def applyOperations(self, nums):
        n = len(nums)
        index = 0  # Pointer to track the position for non-zero elements

        for i in range(n):
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2  # Double the current element
                nums[i + 1] = 0  # Set the next element to 0

            # Shift non-zero elements to the front
            if nums[i] != 0:
                nums[index] = nums[i]  # Place non-zero element at the current index
                if index != i:
                    nums[i] = 0  # Set the original position to 0 if it was moved
                index += 1  # Move the index forward

        # Fill the remaining positions with zeros
        while index < n:
            nums[index] = 0
            index += 1

        return nums
    

from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Apply operations on adjacent equal numbers
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        # Step 2: Shift nonzero elements to the front
        result = [num for num in nums if num != 0]  # Collect all non-zero elements
        result.extend([0] * (n - len(result)))  # Append necessary zeros

        return result
