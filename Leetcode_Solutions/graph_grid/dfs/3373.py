from collections import defaultdict
from typing import List

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        def color_tree(n: int, edges: List[List[int]]) -> List[int]:
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u)

            color = [-1] * n  # -1 means unvisited

            def dfs(u: int, c: int):
                color[u] = c
                for v in graph[u]:
                    if color[v] == -1:
                        dfs(v, c ^ 1)  # Alternate color (0 <-> 1)

            dfs(0, 0)  # Start from node 0 with color 0
            return color

        # Color both trees
        n = len(edges1) + 1
        m = len(edges2) + 1
        color1 = color_tree(n, edges1)
        color2 = color_tree(m, edges2)

        # Count number of color 0 and 1 in both trees
        count1 = [0, 0]
        for c in color1:
            count1[c] += 1
        count2 = [0, 0]
        for c in color2:
            count2[c] += 1

        # For each node in tree1, try connecting to tree2 color 0 or color 1
        result = []
        for i in range(n):
            my_color = color1[i]
            # If I connect to same color node, parity preserved -> target nodes = same color count in both trees
            option1 = count1[my_color] + count2[my_color]
            # If I connect to different color node, parity flips -> target nodes = same color count in tree1, opposite in tree2
            option2 = count1[my_color] + count2[1 - my_color]
            result.append(max(option1, option2))

        return result
