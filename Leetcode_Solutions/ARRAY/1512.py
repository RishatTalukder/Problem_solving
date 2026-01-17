from collections import Counter
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(comb(v, 2) for v in counter.values() if v > 1)
    
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = Counter(nums)

        ans = 0

        for k, v in c.items():
            if v > 1:
                ans += v*(v-1)//2

        return ans


