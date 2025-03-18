from typing import List

class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]], mid: int) -> bool:
        n = len(nums)
        modified_nums = nums[:]
        delta = [0] * (n + 1)

        for i in range(mid):
            left, right, value = queries[i]
            delta[left] -= value
            if right + 1 < n:
                delta[right + 1] += value

        current_decrement = 0
        for i in range(n):
            current_decrement += delta[i]
            modified_nums[i] += current_decrement
            if modified_nums[i] > 0:
                return False
        return True

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left, right, result = 0, len(queries), -1

        while left <= right:
            mid = (left + right) // 2
            if self.isZeroArray(nums, queries, mid):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        
        return result