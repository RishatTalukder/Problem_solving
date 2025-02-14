from collections import defaultdict
import heapq
class Solution:
    def digit_sum(self, num):
        res = 0
        while num:
            res += num%10
            num //= 10
        return res
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        num_map = defaultdict(list)

        for i in range(n):
            summ = self.digit_sum(nums[i])
            heapq.heappush(num_map[summ], -nums[i])

        res = -1
        
        for heap in num_map.values():
            if len(heap) < 2:
                continue

            res = max(res, -heapq.heappop(heap)-heapq.heappop(heap))

        return res