from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        node_map = {}

        def dfs(curr):
            if curr in node_map:
                return node_map[curr]

            clone = Node(curr.val)
            node_map[curr] = clone

            for neighbor in curr.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        
        return dfs(node)