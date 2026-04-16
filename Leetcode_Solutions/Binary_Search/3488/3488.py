from collections import defaultdict
import bisect

class Solution:
    def solveQueries(self, nums, queries):
        pos = defaultdict(list)

        # build positions
        for i, v in enumerate(nums):
            pos[v].append(i)

        n = len(nums)
        ans = []

        for i in queries:
            arr = pos[nums[i]]

            if len(arr) == 1:
                ans.append(-1)
                continue

            idx = bisect.bisect_left(arr, i)

            # neighbors in circular manner
            left = arr[idx - 1] if idx > 0 else arr[-1]
            right = arr[idx + 1] if idx < len(arr) - 1 else arr[0]

            # compute circular distances
            d1 = abs(i - left)
            d2 = abs(i - right)

            d1 = min(d1, n - d1)
            d2 = min(d2, n - d2)

            ans.append(min(d1, d2))

        return ans