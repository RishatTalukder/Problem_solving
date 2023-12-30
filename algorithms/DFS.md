***DEPTH FIRST SEARCH***

**Depth First Search** is a graph traversal algorithm that explores as far as possible along each branch before backtracking.

**Time Complexity:** O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.

**Space Complexity:** O(V) where V is number of vertices in the graph.

**Applications:**

- For an unweighted graph, DFS traversal of the graph produces the minimum spanning tree and all pair shortest path tree.

- Detecting cycle in a graph

- Path Finding

- Topological Sorting

- To test if a graph is bipartite

- Finding Strongly Connected Components of a graph

- Solving puzzles with only one solution, such as mazes.

Prolems solved using DFS:

- [Combination Sum](https://leetcode.com/problems/combination-sum/)

implementaion:
    
    ```python


class Solution:
    def combinationSum(self, candidates, target):
        # create a result list
        result = []

        # create a dfs function that takes index, current and total as arguments
        def dfs(index, current, total):
            # check if the total is equal to the target or not
            if total == target:
                result.append(current.copy())
                return
            # check if the total is greater than the target or not
            if total > target or index >= len(candidates):
                return
            
            current.append(candidates[index]) # append the current item to the current list

            dfs(index, current, total+candidates[index]) # call the dfs function with index, current and total+candidates[index] as arguments

            current.pop() # remove the last item from the current list

            dfs(index+1, current, total) # call the dfs function with index+1, current and total as arguments

        dfs(0, [], 0) # call the dfs function with 0, [], 0 as arguments

        return result

    ```
