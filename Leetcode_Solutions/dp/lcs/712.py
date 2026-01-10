class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m,n = len(s1), len(s2)

        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i+1][j+1]=dp[i][j]+ord(s1[i])

                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

        total = sum((ord(c) for c in s1)) + sum((ord(c) for c in s2))

        return total - 2*dp[m][n]