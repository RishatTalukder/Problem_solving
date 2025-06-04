## 🧠 Solving LeetCode Until I Become Top 1% — Day `8`

### 🔹 Problem: [1298. Maximum Candies You Can Get from Boxes](https://leetcode.com/problems/maximum-candies-you-can-get-from-boxes/description/?envType=daily-question&envId=2025-06-03)

**Difficulty:** #Hard
**Tags:** #Graph #BFS

---

### 📝 Problem Summary

> You are given `n` boxes, each containing a certain number of candies. You can open boxes in a specific order and collect candies from them. Theboces might have connections to other boxes, allowing you to open them in a specific sequence. The goal is to maximize the number of candies you can collect. I know Confusing af. feelings mututal brother.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This Problem is actually brtute force graph traversal problem. The only thing is to find Which traversal to use. I started with `DFS` but the implementation was getting too complex with recursion. Then I switched to `BFS` which was much cleaner and easier to manage._

- **Optimized Strategy:**

  - _Heres the key idea: Use a queue to manage the boxes you can open. We can add the initial box to the queue and then process each box in the queue, collecting candies and adding connected boxes to the queue._
    - **Step 1:** Initialize an empty queue and add the initial box to it.
    - **Step 2:** While the queue is not empty, pop a box from the front.
    - **Step 3:** Collect candies and chekc if we have already opened this box or if we don't have the key to open it.
    - **Step 4:** If we don't have the key, we can add the box to the queue and continue processing. Because we might get the key later.
    - **Step 5:** As we can open boxes and can get keys to other boxes, we can set the status of the box to opened and add its connected boxes to the queue.
    - **Step 6:** Also we will add the boxes to the queue only if we find new_boxes that we haven't opened yet.

- **Algorithm Used:**
  [[notes/algorithms/graph_bfs.md]]

---

### ⚙️ Code Implementation (Python)

```python
from collections import deque
from typing import List

class Solution:
    def maxCandies(
        self,
        status: List[int],
        candies: List[int],
        keys: List[List[int]],
        containedBoxes: List[List[int]],
        initialBoxes: List[int]
    ) -> int:

        n = len(status)
        visited = [False] * n
        have_box = [False] * n
        have_key = status[:]
        queue = deque()

        for box in initialBoxes:
            have_box[box] = True
            if have_key[box]:
                queue.append(box)

        total_candies = 0

        while queue:
            box = queue.popleft()

            if visited[box]:
                continue
            visited[box] = True
            total_candies += candies[box]

            # Gain new keys
            for key in keys[box]:
                if not have_key[key]:
                    have_key[key] = 1
                    if have_box[key] and not visited[key]:
                        queue.append(key)

            # Add new boxes
            for new_box in containedBoxes[box]:
                have_box[new_box] = True
                if have_key[new_box] and not visited[new_box]:
                    queue.append(new_box)

        return total_candies
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n + m), where n is the number of boxes and m is the total number of connections (keys and contained boxes).
- **Space:** O(n), for the queue and visited arrays.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - _Nothing new, just a good practice of using BFS for graph traversal problems._
- 💡 What made this problem tricky?
  - _The tricky part was managing the state of boxes (opened, keys available) and ensuring we only process boxes that can be opened._
- 💭 How will I recognize a similar problem in the future?
  - _Look for problems involving traversal of connected components, especially when keys or conditions affect accessibility._

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [😬] Did I write code from scratch?
- [😊] Did I understand why it works?
- [😊] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `8`   |
| Total Problems Solved | `343` |
| Confidence Today      | 😃    |
