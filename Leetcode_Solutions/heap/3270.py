class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        heap = []
        hashmap = defaultdict(deque)
        keep = [True] * n
        for i in range(n):
            if s[i] == '*':
                smallest = heaheap.heappop(heap)
                idx = hashmap[smallest].pop()
                keep[i] = False
                keep[idx] = False
            else:
                heapq.heappush(heap, s[i])
                hashmap[s[i]].append(i)

        return ''.join(s[i] for i in range(n) if keep[i])