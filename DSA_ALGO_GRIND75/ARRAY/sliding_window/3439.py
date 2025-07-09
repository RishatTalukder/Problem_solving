class Solution:
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[:k+1])
        ans = window

        for i in range(k+1, len(gaps)):
            window += gaps[i] - gaps[i - (k+1)]
            ans = max(ans, window)

        return ans