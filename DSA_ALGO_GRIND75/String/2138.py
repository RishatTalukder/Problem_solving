class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)

        s = s + (fill*(k-n%k) if n%k else '')

        start = 0

        while start < len(s):
            res.append(s[start:start+k])
            start += k


        return res

        