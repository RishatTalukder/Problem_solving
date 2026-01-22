import heapq
from typing import List

class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        # Doubly linked list via arrays
        left = [i - 1 for i in range(n)]
        right = [i + 1 for i in range(n)]
        right[n - 1] = -1

        alive = [True] * n

        # Count how many decreasing adjacent pairs exist
        bad = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                bad += 1

        # Min heap of (sum, index)
        heap = []
        for i in range(n - 1):
            heapq.heappush(heap, (nums[i] + nums[i + 1], i))

        ans = 0

        while bad > 0:
            s, i = heapq.heappop(heap)

            # Skip invalid pairs
            if not alive[i] or right[i] == -1:
                continue

            j = right[i]
            if not alive[j] or nums[i] + nums[j] != s:
                continue

            # Remove old bad relations
            if left[i] != -1 and nums[left[i]] > nums[i]:
                bad -= 1
            if nums[i] > nums[j]:
                bad -= 1
            if right[j] != -1 and nums[j] > nums[right[j]]:
                bad -= 1

            # Merge i and j
            nums[i] += nums[j]
            alive[j] = False
            right[i] = right[j]
            if right[j] != -1:
                left[right[j]] = i

            # Add new bad relations
            if left[i] != -1 and nums[left[i]] > nums[i]:
                bad += 1
            if right[i] != -1 and nums[i] > nums[right[i]]:
                bad += 1

            # Push new adjacent sums
            if left[i] != -1:
                heapq.heappush(heap, (nums[left[i]] + nums[i], left[i]))
            if right[i] != -1:
                heapq.heappush(heap, (nums[i] + nums[right[i]], i))

            ans += 1

        return ans
