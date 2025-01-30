from collections import defaultdict


class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def longest_path(node):
            visited.add(node)
            max_len = 0
            for nei in adj[node]:
                if nei not in visited:
                    max_len = max(max_len, 1 + longest_path(nei))

            return max_len
        
        res = 1

        for i in range(n):
            if i not in visited:
                res = max(res, longest_path(i))

        return res