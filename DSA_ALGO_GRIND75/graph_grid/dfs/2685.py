from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        count = 0

        def dfs(node,component):
            component.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,component)

        for node in range(n):
            if node not in visited:
                component = set()
                dfs(node,component)
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    count += 1


        return count