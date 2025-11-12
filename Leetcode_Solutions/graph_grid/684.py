from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        for u, v in edges:
            root_u, root_v = find(u), find(v)

            if root_u == root_v:
                return [u, v]

            parent[root_v] = root_u


sol = Solution()
print(sol.findRedundantConnection([[1,2],[1,3],[2,3]])) # [2,3]