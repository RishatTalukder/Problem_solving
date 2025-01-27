import heapq


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights)-1):
            difference = heights[i+1]-heights[i]
            if difference < 0:
                continue

            bricks -= difference
            heapq.heappush(heap, -difference)

            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -= 1
                bricks += -heapq.heappop(heap)

        return len(heights)-1