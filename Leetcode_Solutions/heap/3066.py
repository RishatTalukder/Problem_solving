from typing import List

import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        count = 0
        while len(nums) > 1 and nums[0] < k:
            count += 1
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, (2*x)+y)

        return count
    

sol = Solution()
print(sol.minOperations([1,1,2,4,9], k = 20))  # 3