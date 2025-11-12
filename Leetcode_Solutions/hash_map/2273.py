from collections import Counter


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        n = len(words)

        for i in range(1, n):
            if Counter(words[i]) == Counter(words[i - 1]):
                continue
            res.append(words[i])

        return res