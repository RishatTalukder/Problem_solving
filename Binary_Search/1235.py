import bisect
#import zip



class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        intervals = sorted(zip(startTime, endTime, profit),)
        memo = {}
        
        def dfs(i):
            if i == len(intervals):
                return 0
            
            if i in memo:
                return memo[i]
            
            res = dfs(i+1)

            j = bisect.bisect_left(intervals, (intervals[i][1], -1, -1),)

            memo[i] = res = max(res, intervals[i][2] + dfs(j))

            return res
        
        return dfs(0)