class Solution:
    def hasSameDigits(self, s: str) -> bool:
        s = list(map(int, s))

        while len(s) > 2:
            s = [(s[i] + s[i + 1]) % 10 for i in range(len(s) - 1)]

        return s[0] == s[1]