## 🧠 Solving LeetCode Until I Become Top 1% — Day `4`

### 🔹 Problem: [2359 Find Closest Node to Given Two Nodes](https://leetcode.com/problems/find-closest-node-to-given-two-nodes/description/?envType=daily-question&envId=2025-05-30)

**Difficulty:** Medium
**Tags:** #Graph #DFS

---

### 📝 Problem Summary _(in your own words)_

> Finding The commong node between two nodes in a directed graph.
> The maximum distance from the `common node` to the two nodes should be minimized.

---

### 🧠 My Thought Process

- **My Thoughts:**
  _At this problem isn't as confusing as the previous one. And the problem statement is clear, So It's didn't take me long to figure out how to solve this problem._

- **Strategy:**
  _We can use Depth-First Search (DFS) to traverse the graph and store the distance of each node from the two given nodes._

  - Take the new lists `dist1` and `dist2` to store the distance of each node from the two given nodes.
  - Use `DFS` to `traverse` the graph and update the distance of each node from the two given nodes.
  - Now we can `iterate` through both lists and find the maximum distanced node that has the minimum distance from both nodes.
  - the last thing is kinda confusing, but we can use the `max` function to find the maximum distance node that has the minimum distance from both nodes.

- **Algorithm Used:**
  `Depth-First Search (DFS)`

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def get_distances(start):
            n = len(edges)
            dist = [-1] * n
            steps = 0
            while start != -1 and dist[start] == -1:
                dist[start] = steps
                steps += 1
                start = edges[start]
            return dist

        dist1 = get_distances(node1)
        dist2 = get_distances(node2)

        min_dist = float('inf')
        result = -1

        for i in range(len(edges)):
            if dist1[i] != -1 and dist2[i] != -1:
                max_dist = max(dist1[i], dist2[i])
                if max_dist < min_dist:
                    min_dist = max_dist
                    result = i
        return result
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We traverse each node once to calculate distances from both nodes.
  - The overall complexity is linear with respect to the number of nodes.
- **Space:** O(...)
- **Space:** O(n)
  - We use two lists to store distances for each node, which requires O(n) space.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  _I learned how to use DFS to find the distance of each node from two given nodes in a directed graph._
- 💡 What made this problem tricky?
  _Me, I didn't userstand the problem statement at first so I thought I has to find the common node between the two nodes that has the maximum distance from node1 and minimum distance from node2.. So, I though it's going to be heap problem, but after reading the problem statement again I realized that it's not a heap problem, it's a straightforward DFS problem._
- 💭 How will I recognize a similar problem in the future?
  _Minimizing distances in a graph using DFS is a common pattern. If I see a problem involving distances in a directed graph, I will think of using DFS to calculate those distances._

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [❌] Did I write code from scratch?(had some bugs that I couldn't fix, so took some help from the discussion section)
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `4`   |
| Total Problems Solved | `337` |
| Confidence Today      | 😃    |
