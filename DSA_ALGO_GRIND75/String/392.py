class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)

        for i in t:
            if i in s and s[0] == i:
                s.remove(i)

        if s:
            return False
        else:
            return True