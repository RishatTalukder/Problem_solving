from collections import OrderedDict, Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        nums_count = OrderedDict(sorted(nums_count.items(), key=lambda x: x[1], reverse=True))

        return list(nums_count.keys())[:k]


import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = Counter(nums)
        heap = [(-count, num) for num, count in nums_count.items()]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]