from collections import defaultdict,deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj_list = defaultdict(list)
        in_degree = [0]*n

        for f, t in edges:
            adj_list[f].append(t)
            adj_list[t].append(f)
            in_degree[f] += 1
            in_degree[t] += 1

        leaves = deque([i for i in range(n) if in_degree[i] == 1])

        remaining_nodes = n

        while remaining_nodes >2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for i in range(leaves_count):
                leaf = leaves.popleft()
                for nei in adj_list[leaf]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 1:
                        leaves.append(nei)

        
        return list(leaves)