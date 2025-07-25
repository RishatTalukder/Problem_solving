## 🧠 Solving LeetCode Until I Become Top 1% — Day `54`

### 🔹 Problem: [2322. Minimum Score After Removals on a Tree](https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/)

**Difficulty:** #Hard
**Tags:** #Tree, #DFS, #BitManipulation, #Graph, #Math, #BruteForce

---

### 📝 Problem Summary

> You’re given a tree (yes, that means no cycles and it’s connected) with `n` nodes, and each node has a value. The task? Pick **two edges** to cut. After cutting, you’ll get three separate trees.
> Then calculate the XOR value of each component’s nodes.
> Your goal is to **minimize** the **difference between the max and min** of those three XOR values.

Sounds simple, right? WRONG.
It’s a delightful mix of:

* Trees,
* XORs (bit ops),
* Edge removals,
* And a sprinkle of "wait, what exactly am I cutting?"

---

### 🧠 My Thought Process

#### 🚫 Brute Force Idea:

Sure, let's try **cutting all possible pairs of edges**, recompute the trees, XOR values, and score every time.
Oh, wait. That’s **O(n²)** cuts and **O(n)** work per cut? So about **O(n³)**?
Yeah, great way to set your laptop on fire.

#### ✅ Optimized Strategy:

So I took the noble route: **asked ChatGPT for help** because... yeah, no way I was cooking this up alone.

Here’s what we (and by that I mean mostly ChatGPT) did:

1. Build the tree using adjacency list.
2. Do a **DFS from the root** (node `0`) to:

   * Compute **subtree XOR** for every node.
   * Track **which nodes belong to the subtree** of each node.
3. Now iterate over **every pair of nodes** `i, j`, representing two edges we’ll cut (the edge from `i` to its parent and from `j` to its parent).
4. Three cases:

   * **Case 1:** `j` is inside `i`'s subtree (nested).
   * **Case 2:** `i` is inside `j`'s subtree (also nested).
   * **Case 3:** Independent branches.
5. For each case, compute the three XOR parts and evaluate the **score**:
   `score = max(x1, x2, x3) - min(x1, x2, x3)`
6. Return the **minimum score** found.

---

### ⚙️ Code Implementation (Python)

```python
import collections

class Solution:
    def minimumScore(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)
        graph = collections.defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subtree_xor = [0] * n
        descendants = [set() for _ in range(n)]

        def dfs(node, parent):
            subtree_xor[node] = nums[node]
            descendants[node].add(node)
            for neighbor in graph[node]:
                if neighbor != parent:
                    dfs(neighbor, node)
                    subtree_xor[node] ^= subtree_xor[neighbor]
                    descendants[node].update(descendants[neighbor])

        dfs(0, -1)
        total_xor = subtree_xor[0]
        min_score = float('inf')

        for i in range(1, n):
            for j in range(i + 1, n):
                xor_i = subtree_xor[i]
                xor_j = subtree_xor[j]

                if j in descendants[i]:  # j inside i
                    val1 = xor_j
                    val2 = xor_i ^ xor_j
                    val3 = total_xor ^ xor_i
                elif i in descendants[j]:  # i inside j
                    val1 = xor_i
                    val2 = xor_j ^ xor_i
                    val3 = total_xor ^ xor_j
                else:  # separate
                    val1 = xor_i
                    val2 = xor_j
                    val3 = total_xor ^ xor_i ^ xor_j

                score = max(val1, val2, val3) - min(val1, val2, val3)
                min_score = min(min_score, score)

        return min_score
```

---

### ⏱️ Time & Space Complexity

* **Time:** `O(n²)` — Two nested loops for pairs of cuts.
* **Space:** `O(n²)` — Sets storing subtree descendants make this non-trivial.

---

### 🧩 Key Takeaways

* ✅ XOR is cool and annoying. It’s its own inverse: `a ^ b ^ b = a`.
* ✅ Tree DP strikes again. This time, in disguise.
* ❌ Thought it was just about cutting edges and subtracting stuff.
  Turns out... no, we’re doing **set inclusion** and **bit-level subtree aggregation**. Fun!

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
  *lol no*
* [x] Did I write code from scratch?
  *If "copy-paste with pride" counts, then yes.*
* [x] Did I understand why it works?
  *Eventually, after a small existential crisis.*
* [x] Will I be able to recall this in a week?
  *If not, I’ll cry and come back here.*

---

### 🚀 Progress Tracker

| Metric                | Value              |
| --------------------- | ------------------ |
| Day                   | `54`                |
| Total Problems Solved | `395`                |
| Confidence Today      | 😣 (crying in XOR) |
| Leetcode Rating       | `1572`             |
