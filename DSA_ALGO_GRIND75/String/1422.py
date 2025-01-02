class Solution:
    def maxScore(self, s: str) -> int:
        s_count = Counter(s)
        left = 0
        ans = 0

        n = len(s)
        count = 0
        while left < n-1:
            if s[left] == "0":
                count += 1
                s_count["0"] -= 1
            
            ans = max(ans, count + (n-s_count["0"]-(left+1)))
            
            left += 1

        return ans