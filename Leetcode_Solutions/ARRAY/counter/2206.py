from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c = Counter(nums)

        for num in c:
            if c[num] % 2 != 0:
                return False
            
        return True