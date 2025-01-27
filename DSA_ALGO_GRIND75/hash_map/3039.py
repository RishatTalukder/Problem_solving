from collections import OrderedDict, Counter
from typing import List

class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        count = Counter(s)
        maxx_count = max(count.values())
        final_chars = {k for k,v in count.items() if v == maxx_count}
        ans = ""
        for i in s[::-1]:
            if i in final_chars:
                ans = i + ans
                final_chars.remove(i)

        return ans


s = "abcd"
sol = Solution()
print(sol.lastNonEmptyString(s)) # "ab"