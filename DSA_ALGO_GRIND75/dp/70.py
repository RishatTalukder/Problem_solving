from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        @cache
        def steps(n):
            nonlocal count
            if n == 0:
                count += 1
                return
            if n < 0:
                return
            steps(n - 1)
            steps(n - 2)

        return count
    

sol = Solution()

print(sol.climbStairs(2))  # 2
print(sol.climbStairs(3))  # 3