class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        ans = count = 0
        dp = [0] * 26
        for i in range(len(s)):
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or ord(s[i - 1]) - ord(s[i]) == 25):
                count += 1
            else:
                count = 1
            dp[ord(s[i]) - ord('a')] = max(dp[ord(s[i]) - ord('a')], count)
        return sum(dp)
    

sol = Solution()
print(sol.findSubstringInWraproundString("zab"))