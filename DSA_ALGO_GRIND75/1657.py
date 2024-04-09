from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:

        cnt1 = Counter(word1)
        cnt2 = Counter(word2)

        v1 = list(cnt1.values())
        v1.sort()
        v2 = list(cnt2.values())
        v2.sort()

        if v1 != v2:
            return False

        v1 = list(cnt1.keys())
        v1.sort()
        v2 = list(cnt2.keys())
        v2.sort()

        return  v1 == v2