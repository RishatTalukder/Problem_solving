import bisect
import collections 

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        startTimeMap = collections.defaultdict(int)

        for i, interval in enumerate(intervals):
            startTimeMap[interval[0]] = i

        sortedStartTimes = sorted(startTimeMap.keys())

        result = []

        for interval in intervals:
            idx = bisect.bisect_left(sortedStartTimes, interval[1])

            if idx == len(sortedStartTimes):
                result.append(-1)
            else:
                result.append(startTimeMap[sortedStartTimes[idx]])




        return result                   