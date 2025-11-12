class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        start = 0

        maxx = start

        for i in gain:
            start += i
            maxx = max(maxx, start)

        return maxx