import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        def gain(pas,total):
            return (pas+1)/(total+1) - pas/total
        
        for pas, total in classes:
            g = gain(pas,total)
            heapq.heappush(heap, (-g, pas, total))

        for _ in range(extraStudents):
            g, pas, total = heapq.heappop(heap)
            pas += 1
            total += 1
            g = gain(pas,total)
            heapq.heappush(heap, (-g, pas, total))

        total_avg = sum(pas/total for _, pas, total in heap)

        return total_avg / len(classes)
