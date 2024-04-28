from collections import Counter
from math import comb

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter = Counter(nums)
        comb_sum = 0
        for i in counter.values():
            if i > 1:
                comb_sum = comb_sum + comb(i, 2)

        return comb_sum
    


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # Custom function to calculate combinations
        def comb(n, r):
            return factorial(n) // (factorial(r) * factorial(n - r))

        # Custom function to calculate factorial
        def factorial(n):
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

        # Count occurrences of each number
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1

        # Calculate sum of combinations
        comb_sum = 0
        for count in counter.values():
            if count > 1:
                comb_sum += comb(count, 2)

        return comb_sum