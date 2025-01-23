from collections import Counter
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        hash_map = Counter(nums)

        count = 0

        for num in nums:
            if num == k - num:
                count += hash_map[num] // 2
                hash_map[num] = 0
            elif k - num in hash_map and hash_map[num] > 0 and hash_map[k-num] > 0:
                count += 1
                hash_map[num] -= 1
                hash_map[k-num] -= 1

        return count
     

sol = Solution()

print(sol.maxOperations([3,1,3,4,3], 6))