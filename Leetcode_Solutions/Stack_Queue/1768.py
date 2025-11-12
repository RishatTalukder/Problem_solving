from collections import deque

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ans = ''

        for i in range(max(len(word1), len(word2))):
            if i < len(word1) and i < len(word2):
                ans += word1[i] + word2[i]

            elif i >= len(word1):
                ans += word2[i:]
                break
            elif i >= len(word2):
                ans += word1[i:]
                break
        return ans
    
sol = Solution()

print(sol.mergeAlternately("abc", "pqrst")) # apbqcr