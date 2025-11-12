class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        count = [(s.count("0"), s.count("1")) for s in strs]

        memo = {}

        def dp(i, m, n):
            if i == len(strs):
                return 0

            if (i, m, n) in memo:
                return memo[(i, m, n)]

            if m >= count[i][0] and n >= count[i][1]:
                memo[(i, m, n)] = max(1 + dp(i + 1, m - count[i][0], n - count[i][1]), dp(i + 1, m, n))
            else:
                memo[(i, m, n)] = dp(i + 1, m, n)

            return memo[(i, m, n)]
        
        return dp(0, m, n)