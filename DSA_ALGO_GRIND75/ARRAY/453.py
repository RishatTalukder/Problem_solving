import random
from typing import List
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        moves = 0

        for i in range(n-1,-1,-1):
            moves += nums[i] - nums[0]

        return moves
    
sol = Solution()
random.seed(10)
print(sol.minMoves([random.randint(1, 100) for _ in range(10)])) # 45
print(sol.minMoves([1,2,3])) # 3