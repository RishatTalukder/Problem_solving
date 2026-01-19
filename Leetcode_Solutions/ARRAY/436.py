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
    
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)

        for i, interval in enumerate(intervals):
            hashmap[interval[0]] = i

        sortedStartTime = sorted(hashmap.keys())

        ans = []

        for i in intervals:
            ind = bisect_left(sortedStartTime, i[1])

            if ind == len(sortedStartTime):
                ans.append(-1)

            else:
                ans.append(hashmap[sortedStartTime[ind]])

        return ans