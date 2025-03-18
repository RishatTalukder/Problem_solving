from typing import List

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = 0
        used = 0
        mx = 0

        for right in range(len(nums)):
            while (used & nums[right]) != 0:
                used ^= nums[left]
                left += 1

            used |= nums[right]

            mx = max(mx, right - left + 1)

        return mx
    

sol = Solution()
print(sol.longestNiceSubarray([1,3,8,48,10])) 