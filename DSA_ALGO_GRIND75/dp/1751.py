from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maxValue(self, events, k):
        # Sort events by start day
        events.sort()
        n = len(events)

        # Extract all start days into a separate list for binary search
        start_days = [e[0] for e in events]

        @lru_cache(None)
        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            
            # Option 1: Skip current event
            skip = dp(i + 1, remaining)

            # Option 2: Take current event
            # Find next event that starts AFTER current event ends
            next_index = bisect_right(start_days, events[i][1])
            take = events[i][2] + dp(next_index, remaining - 1)

            return max(skip, take)

        return dp(0, k)
