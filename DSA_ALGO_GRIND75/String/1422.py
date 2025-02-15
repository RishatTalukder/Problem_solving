class Solution:
    def maxScore(self, s: str) -> int:
        left = 1 if s[0] == "0" else 0
        right = s[1:].count("1")
        max_score = left + right
        for i in range(1,len(s)-1):
            if s[i] == "0":
                left += 1
            else:
                right -= 1
            max_score = max(max_score, left+right)

        return max_score