from collections import Counter
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum(comb(v, 2) for v in counter.values() if v > 1)
    
