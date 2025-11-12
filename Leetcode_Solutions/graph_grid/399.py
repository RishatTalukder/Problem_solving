from collections import defaultdict, deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = defaultdict(list)

        for i, eqn in enumerate(equations):
            a,b = eqn

            adj_list[a].append([b,values[i]])
            adj_list[b].append([a,1/values[i]])
        

        def bfs(start,target):
            if start not in adj_list or target not in adj_list:
                return -1.0
            
            queue = deque()
            visited = set()
            queue.append((start,1.0))
            visited.add(start)

            while queue:
                node, weight = queue.popleft()

                if node == target:
                    return weight

                for nei, val in adj_list[node];
                    if nei not in visited:
                        queue.append((nei,weight*val))
                        visited.add(nei)

            return -1.0

        return [bfs(start,target) for start,target in queries]