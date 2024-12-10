class Solution:
    def climbStairs(self, n: int, cache = {}) -> int:
        if n == 0:
            return 1
        if n < 0:
            return 0
        
        if n not in cache:
            cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)

        return cache[n]