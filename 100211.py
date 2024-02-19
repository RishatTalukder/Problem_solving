from collections import Counter
class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        s_count = Counter(s)
        max_count = max(s_count.values())
        final_chars = {k for k,v in s_count.items() if v == max_count}

        print(final_chars)

        res = ''
        for charecter in s[::-1]:
            if charecter in final_chars:
                res = charecter + res
                final_chars.discard(charecter)

        print(res)


        return res
                
sol = Solution()
 
sol.lastNonEmptyString("abcd") # 2