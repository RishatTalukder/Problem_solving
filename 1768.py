class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
         p1, p2 = 0, 0         
         out = ''

         while p1 < len(word1) or p2 < len(word2):
            if p1 < len(word1):
                out += word1[p1]
            if p2 < len(word2):
                out += word2[p2]
            p1 += 1
            p2 += 1

         return out