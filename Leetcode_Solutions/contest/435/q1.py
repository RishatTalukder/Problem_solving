from collections import Counter

class Solution:
    def maxDifference(self, s: str) -> int:
        s_counter = Counter(s)
        odd = float('-inf')
        even = float('inf')

        for k,v in s_counter.items():
            if v%2 == 0:
                even = min(even, v)
            else:
                odd = max(odd, v)

        return odd - even

sol = Solution()
print(sol.maxDifference("abcabcab")) # 1