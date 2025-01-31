from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        def bfs(start: int) -> int:
            queue = deque([start])
            distances = [0] * n
            distances[start] = 1
            max_distance = 1
            root = start
            
            while queue:
                current = queue.popleft()
                root = min(root, current)
                
                for neighbor in graph[current]:
                    if distances[neighbor] == 0:
                        distances[neighbor] = distances[current] + 1
                        max_distance = max(max_distance, distances[neighbor])
                        queue.append(neighbor)
                    elif abs(distances[neighbor] - distances[current]) != 1:
                        return -1, root
            
            return max_distance, root
        
        # Create adjacency list for the graph
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
        
        # Dictionary to store the maximum distance for each root node
        max_distances = defaultdict(int)
        
        # Iterate through each node to perform BFS
        for i in range(n):
            max_distance, root = bfs(i)
            if max_distance == -1:
                return -1
            max_distances[root] = max(max_distances[root], max_distance)
        
        return sum(max_distances.values())