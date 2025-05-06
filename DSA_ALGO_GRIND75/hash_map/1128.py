class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        freq = defaultdict(int)
        for i in dominoes:
            a, b = i
            if a > b:
                a, b = b, a
            freq[(a, b)] += 1
        for i in freq.values():
            count += (i * (i - 1)) // 2
        return count