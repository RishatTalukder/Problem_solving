import heapq
import random

random.seed(32)

arr = [-random.randint(1,25) for _ in range(15)]

print(arr)  

heapq.heapify(arr)

print(arr)

heapq.heappush(arr, -14)

print(arr) 

sortes_heap = []

while arr:

    sortes_heap.append(-heapq.heappop(arr))

print(sortes_heap)