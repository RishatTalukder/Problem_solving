from bisect import bisect_right

def jobScheduling(startTime, endTime, profit):
    # Step 1: Zip tasks and sort them by end time
    jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
    n = len(jobs)
    dp = [0]*n
    endtimes = [job[1] for job in jobs]

    # Step 2: Iterate over the jobs
    for i in range(n):
        # Step 3: Find the latest job that ends before the start of the current job
        start, end, pft = jobs[i]
        # Step 4: Find the index of the latest job that ends before the start of the current job
        idx = bisect_right(endtimes, start)-1
        # Step 5: Update the dp table
        dp[i] = max(dp[i-1], pft+dp[idx] if idx >= 0 else pft)

    return dp[-1]

import bisect
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = sorted(zip(startTime,endTime, profit), key=lambda x: x[1])
        max_profit = [0]*len(jobs)
        end_time = sorted(endTime)

        for i in range(len(jobs)):
            start, end, pft = jobs[i]
            idx = bisect.bisect_right(end_time, start)-1
            max_profit[i] = max(max_profit[i-1], pft+max_profit[idx] if idx >= 0 else pft)

        return max_profit[-1]

























