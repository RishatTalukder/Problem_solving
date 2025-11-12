class Solution:
    def maxTargetNodes(
        self, edges1: List[List[int]], edges2: List[List[int]], k: int
    ) -> List[int]:

        def dfs(node: int, parent: int, adj: List[List[int]], depth: int) -> int:
            if depth < 0:
                return 0
            count = 1  # include current node
            for neighbor in adj[node]:
                if neighbor == parent:
                    continue
                count += dfs(neighbor, node, adj, depth - 1)
            return count

        def computeReachability(edges: List[List[int]], max_depth: int) -> List[int]:
            n = len(edges) + 1
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)

            reachable = [0] * n
            for node in range(n):
                reachable[node] = dfs(node, -1, adj, max_depth)
            return reachable

        # Compute reachability in both trees
        count1 = computeReachability(edges1, k)
        count2 = computeReachability(edges2, k - 1)

        # Use the best possible Tree2 node for each Tree1 node
        max_reach_from_tree2 = max(count2)
        return [count1[i] + max_reach_from_tree2 for i in range(len(count1))]
