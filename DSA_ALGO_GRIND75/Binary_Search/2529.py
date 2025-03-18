import bisect
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n = len(nums)

        pos_ind = bisect.bisect_right(nums, 0)
        neg_ind = bisect.bisect_left(nums, 0)

        ans = max(neg_ind, n - pos_ind)
        return ans


sol = Solution()

print(sol.maximumCount([-3, -2, -4, -5, 0, 1,3, 4,5]))
 