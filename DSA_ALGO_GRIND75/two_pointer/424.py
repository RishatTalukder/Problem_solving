from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        j = 0
        maxx = 0
        for i in range(len(s)):
            frequency[s[i]] += 1
            maxx_len = max(frequency.values())

            curr_len = i - j + 1

            if curr_len - maxx_len > k:
                frequency[s[j]] -= 1
                j += 1

            maxx = max(maxx, i - j + 1)

        return maxx