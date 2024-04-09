class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = Counter(s)
        t = Counter(t)

        for k in t:
            if s[k] != t[k]:
                return k