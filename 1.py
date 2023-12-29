class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for ind, num in enumerate(nums):
            if num in dic:  # If the complement of the current number is already in the dictionary
                return [dic[num], ind]  # Return the indices of the two numbers
            else:
                dic[target - num] = ind  # Store the complement and its index in the dictionary
