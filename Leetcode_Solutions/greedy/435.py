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
    
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[1])

        ans = 0
        prev = intervals[0]

        for curr in intervals[1:]:
            if curr[0] < prev[1]:
                ans += 1

            else:
                prev = curr

        return ans