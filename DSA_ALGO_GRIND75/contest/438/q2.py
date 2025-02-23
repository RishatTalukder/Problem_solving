import heapq

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        total =0

        for i in range(len(grid)):
            row = sorted(grid[i], reverse=True)

            for j in range(min(len(row), limits[i])):
                heapq.heappush(max_heap, row[j])
                
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        total = sum(max_heap)
        return total