class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort(key=lambda x:x[1])
        prev = intervals[0][1]
        for interval in intervals[1:]:
            if interval[0] < prev:
                res += 1
            else:
                prev = interval[1]

        return res