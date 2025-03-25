from heapq import heappop, heappush
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # Step 1: Build the adjacency list (graph)
        graph = {i: [] for i in range(n)}
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))

        # Step 2: Initialize Dijkstra's algorithm
        min_heap = [(0, 0)]  # (distance, node)
        dist = [float('inf')] * n
        ways = [0] * n  # Ways to reach each node using the shortest path
        dist[0] = 0
        ways[0] = 1

        while min_heap:
            curr_time, node = heappop(min_heap)

            # If the current distance is already larger, continue
            if curr_time > dist[node]:
                continue

            # Step 3: Process neighbors
            for neighbor, time in graph[node]:
                new_time = curr_time + time

                # Found a shorter path
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]  # Reset count
                    heappush(min_heap, (new_time, neighbor))

                # Found another shortest path
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD

        return ways[n - 1]
