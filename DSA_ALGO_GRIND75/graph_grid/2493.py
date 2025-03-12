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
    


from collections import defaultdict, deque
from typing import List

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))  # Union-Find parent array
        rank = [1] * n  # Rank array for Union-Find

        # Find function with path compression
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function with rank optimization
        def union(x: int, y: int):
            rootX, rootY = find(x), find(y)
            if rootX != rootY:
                if rank[rootX] > rank[rootY]:
                    parent[rootY] = rootX
                elif rank[rootX] < rank[rootY]:
                    parent[rootX] = rootY
                else:
                    parent[rootY] = rootX
                    rank[rootX] += 1

        # Build adjacency list and apply Union-Find
        graph = defaultdict(list)
        for a, b in edges:
            graph[a - 1].append(b - 1)
            graph[b - 1].append(a - 1)
            union(a - 1, b - 1)  # Merge the nodes in Union-Find

        # Group nodes by their connected components
        components = defaultdict(list)
        for node in range(n):
            root = find(node)
            components[root].append(node)

        # BFS function to check bipartiteness and find max depth
        def bfs(start: int) -> int:
            queue = deque([start])
            depth = {start: 1}
            max_depth = 1

            while queue:
                curr = queue.popleft()
                for neighbor in graph[curr]:
                    if neighbor not in depth:
                        depth[neighbor] = depth[curr] + 1
                        max_depth = max(max_depth, depth[neighbor])
                        queue.append(neighbor)
                    elif abs(depth[neighbor] - depth[curr]) != 1:
                        return -1  # Not a bipartite graph
            
            return max_depth

        # Find the sum of maximum depths of bipartite components
        total_groups = 0
        for component in components.values():
            max_depth = 0
            for node in component:
                result = bfs(node)
                if result == -1:
                    return -1
                max_depth = max(max_depth, result)
            total_groups += max_depth

        return total_groups
