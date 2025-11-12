from collections import deque

class Solution:
    """
    Class Solution that contains a method to solve the maximum rotate function problem.

    Methods
    -------
    maxRotateFunction(nums: List[int]) -> int
        Calculates the maximum value of the rotation function F for the given list of integers.

    Parameters
    ----------
    nums : List[int]
        A list of integers for which the maximum rotate function value is to be calculated.

    Returns
    -------
    int
        The maximum value of the rotation function F.

    Explanation
    -----------
    The rotation function F for a given list of integers nums is defined as:
    F(k) = 0 * nums[k] + 1 * nums[k+1] + 2 * nums[k+2] + ... + (n-1) * nums[k+n-1]
    where k is the index of rotation and n is the length of the list.

    The algorithm calculates the initial rotation function value F(0) and then iteratively computes the value for subsequent rotations using the relationship:
    F(k) = F(k-1) + sum(nums) - n * nums[n-k]
    This relationship is derived from the fact that rotating the array by one position to the right means that each element's contribution to the sum increases by the total sum of the array minus n times the element that was moved from the end to the start.

    The algorithm keeps track of the maximum value of F(k) encountered during the iterations and returns it as the result.
    """
    def maxRotateFunction(self,nums) -> int:
        n = len(nums)
        nums = deque(nums)

        max_sum = sum([i*num for i, num in enumerate(nums)])
        curr_sum = max_sum

        for i in range(n-1, 0, -1):
            curr_sum = curr_sum + sum(nums) - n*nums[i]
            max_sum = max(max_sum, curr_sum)

        return max_sum
    
nums = [4, 3, 2, 6]

s = Solution()

print(s.maxRotateFunction(nums)) # 26