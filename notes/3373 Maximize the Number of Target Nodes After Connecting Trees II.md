## 🧠 Solving LeetCode Until I Become Top 1% — Day `2`

### 🔹 Problem: [3373. Maximize the Number of Target Nodes After Connecting Trees II](https://leetcode.com/problems/maximize-the-number-of-target-nodes-after-connecting-trees-ii/description/?envType=daily-question&envId=2025-05-29)

**Difficulty:** #Hard
**Tags:** #Graph #DFS #Tree #TreeBipartition

---

### 📝 Problem Summary

> 2 undirected trees are given, `tree1` and `tree2`, each with `n` and `m` nodes respectively. Goal is to find the maximum number of nodes in `tree2` that can be connected to each node in `tree1` such that the length of the path from any node in `tree1` to its connected node in `tree2` is even.
> almost same as [[3372]].

---

### 🧠 My Thought Process

- **Whats the difference between this problem and its predecessor?**
  _The only difference is that in [[3372]] the path length was given as `target` or `k`, but in this problem the path length is even, which means that the path length can be `2, 4, 6, ...` and so on. and also it's a hard problem so I think the greedy approach wont work here_

- **Brute Force Idea:**
  _I have no idea how to solve this problem, nada, zero, nothing, but i have the best brute force idea ever! can you guess what it is?_

  _DING! Yes, you guessed it right, it's the good old brute force GPT approach!_

- **Optimized Strategy:**
  _After much research and thinking(with the help of GPT), I realized that the strategy is not that hard actually, but hard to get to. The key is to use Depth-First Search (DFS) to count how many nodes have a parity of `even`, so, what we can do is somewhat find a way to mark the nodes in `tree1` and `tree2` as even or odd, and then use DFS to count to see how many nodes connect to each node in `tree1` with an even path length._

🧠 **Core Idea**

- A node `u` is _target_ to node `v` if the number of **edges on the path from `u` to `v` is even**.
- This is equivalent to saying: `u` and `v` are at the **same parity level** (e.g., both at even or both at odd depths in a tree).

1. **2-Coloring with DFS**:

   - Trees are bipartite, meaning we can color each node either `0` or `1` based on depth parity (even/odd depth).
   - This helps us group nodes that are reachable via **even-length** paths.

2. **Count Parities**:

   - Count how many nodes in each tree have color `0` and color `1`.

3. **Maximize Target Nodes for Each Node in Tree1**:

   - For each node in Tree1 (color `c1`), we have two options:

     - **Same-color connection**: Connect to a Tree2 node of color `c1` → target nodes = all nodes in Tree1 with color `c1` + Tree2 with color `c1`.
     - **Opposite-color connection**: Connect to a Tree2 node of color `1 - c1` → flips parity → target nodes = Tree1 with color `c1` + Tree2 with color `1 - c1`.

4. **Choose the Maximum**:

   - For each node in Tree1, choose the connection that gives more target nodes.

---

- **Algorithm Used:**
  - Depth-First Search (DFS) for tree traversal and counting reachable nodes.

---

### ⚙️ Code Implementation (Python)

```python{.line-numbers}
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

```

---

### ⏱️ Time & Space Complexity

- **Time:** O(N + M)

Where `N` is the number of nodes in `tree1` and `M` is the number of nodes in `tree2`. The DFS traversal runs in linear time relative to the number of edges.

- **Space:** O(N + M)

Where `N` is the number of nodes in `tree1` and `M` is the number of nodes in `tree2`.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - **Tree Bipartition with DFS:** I learned how to use DFS to color trees and count nodes based on parity, which is crucial for solving problems involving even-length paths in trees.
- 💡 What made this problem tricky?
  - **Understanding Parity in Trees:** The challenge was recognizing that the problem could be reduced to counting nodes based on their parity (even/odd) and leveraging the bipartite nature of trees.
- 💭 How will I recognize a similar problem in the future?
  - **Look for Parity Conditions:** If a problem involves paths with specific lengths (like even or odd), consider whether tree bipartition or parity coloring can simplify the solution.

---

### 🔁 Reflection (Self-Check)

- [❌] Could I solve this without help?
- [❌] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[3203 Find Minimum Diameter after Merging Trees]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `3`    |
| Total Problems Solved | `336`  |
| Confidence Today      | 😐     |
| Current Rank          | 40.25% |
