class Solution:
    def minTimeToType(self, word: str) -> int:
        curr = 'a'
        total = 0

        for ch in word:
            if curr == ch:
                continue

            diff = abs(ord(curr) - ord(ch))
            total += min(diff, 26 - diff)
            curr = ch

        return total + len(word)