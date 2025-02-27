from collections import defaultdict


class Solution:
    def fill_bob_path(self, node, parent, path, graph):
        if node == 0:
            return True
        
        for nei in graph[node]:
            if nei != parent:
                path.append(nei)
                if self.fill_bob_path(nei, node, path, graph):
                    return True
                path.pop()

        return False
    
    def get_alice_max_score(self, node, parent, curr, bob_path, graph, timestamp, amount):
        if bob_path[node] == -1 or bob_path[node] > timestamp:
            curr += amount[node]
        elif bob_path[node] == timestamp:
            curr += amount[node] // 2

        if len(graph[node]) == 1 and node != 0:
            return curr
        
        max_score = float('-inf')
        for nei in graph[node]:
            if nei != parent:
                max_score = max(max_score, self.get_alice_max_score(nei, node, curr, bob_path, graph, timestamp, amount))

        return max_score


    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        path = []
        bob_path = [-1] * len(amount)
        self.fill_bob_path(bob, -1, path, graph)
        for i, node in enumerate(path):
            bob_path[node] = i

        return self.get_alice_max_score(0, -1, 0, bob_path, graph, len(path), amount)

        


    