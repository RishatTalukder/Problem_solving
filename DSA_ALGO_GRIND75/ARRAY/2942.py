class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for ind, word in enumerate(words):
            if x in word:
                res.append(ind)


        return res
        