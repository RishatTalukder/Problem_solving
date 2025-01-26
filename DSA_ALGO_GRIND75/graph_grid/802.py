from collections import defaultdict

class Solution:
    def eventualSafeNodes(self, graph):
        res = []

        ternimal_nodes = []
        
        in_degree = defaultdict(list)
        for i, nodes in enumerate(graph):
            if not nodes:
                ternimal_nodes.append(i)

        for i, nodes in enumerate(graph):
            for node in nodes:
                in_degree[node].append(i)

        stack = ternimal_nodes.copy()

        while stack:
            node = stack.pop()
            res.append(node)
            for parent in in_degree[node]:
                graph[parent].remove(node)
                if not graph[parent]:
                    stack.append(parent)

        return sorted(res)
    

sol = Solution()

print(sol.eventualSafeNodes([[1,2],[2,3],[5],[0],[5],[],[]])) # [2,4,5,6]