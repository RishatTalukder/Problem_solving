from collections import deque
from typing import List

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # List to store groups of numbers
        groups = []
        # Dictionary to map each number to its group index
        num_to_group_index = {}

        # Sort the numbers to process them in ascending order
        for num in sorted(nums):
            # If there are no groups or the difference between the current number
            # and the last number in the last group is greater than the limit,
            # create a new group
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            
            # Add the current number to the last group
            groups[-1].append(num)
            # Map the current number to its group index
            num_to_group_index[num] = len(groups) - 1

        # List to store the result
        result = []

        # Iterate through the original list of numbers
        for num in nums:
            # Get the group of the current number
            group = groups[num_to_group_index[num]]
            # Append the leftmost element of the group to the result
            result.append(group.popleft())

        return result