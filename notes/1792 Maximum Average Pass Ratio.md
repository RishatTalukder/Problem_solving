
## 🧠 Solving LeetCode Until I Become Top 1% — Day `73`

### 🔹 Problem: [1792 Maximum Average Pass Ratio](https://leetcode.com/problems/maximum-average-pass-ratio/)

**Difficulty:** #Medium
**Tags:** #Greedy, #Heap, #Math, #PriorityQueue

---

### 📝 Problem Summary

You are given `n` classes, each with `passed` students out of `total` students. You can add `extraStudents` students, one at a time, and for each added student you can choose which class they join. Each added student is guaranteed to **pass**.

Your goal: distribute the extra students to maximize the **average pass ratio** across all classes, i.e.

$$
\text{maximize } \frac{1}{n} \sum_{i=1}^n \frac{\text{passed}_i}{\text{total}_i}
$$

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Try distributing students in all possible ways and compute the final average. This is obviously infeasible because the number of ways grows exponentially (`n^extraStudents`).

* **Optimized Strategy:**
  Instead of brute force, notice that adding a student to different classes **doesn’t give equal benefit**. Adding a student to a class with a **low pass ratio** increases the average differently than adding to one with a **higher pass ratio**.

  The trick is: **at each step, add the student to the class where they will provide the maximum increase ("gain") in the overall average.**

* **Algorithm Used:**

  * Greedy + Max Heap
  * Precompute the **gain function** for each class.
  * Always pick the class with the maximum marginal gain using a heap.
  * After placing a student, update its new gain and push it back into the heap.

---

### 📐 Mathematics

The gain of adding one student to a class with `p` passes out of `t` total is:

$$
\text{gain}(p, t) = \frac{p+1}{t+1} - \frac{p}{t}
$$

Why?

* Before adding: pass ratio = `p/t`.
* After adding: pass ratio = `(p+1)/(t+1)`.
* The **difference** = `(p+1)/(t+1) - p/t`.

This gain tells us **exactly how much the class's ratio improves** if we assign the next student here.

Since we want to maximize the total average, we must always choose the class with the **largest gain** at each step → that’s why we use a **max heap**.
(We push negative values because Python’s `heapq` is a min-heap by default.)

---

### ⚙️ Code Implementation (Python)

```python
import heapq
from typing import List

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = []

        # Gain function = improvement in pass ratio by adding one student
        def gain(pas, total):
            return (pas + 1) / (total + 1) - pas / total

        # Build initial heap with all classes
        for pas, total in classes:
            g = gain(pas, total)
            heapq.heappush(heap, (-g, pas, total))  # store negative for max heap

        # Assign extra students greedily
        for _ in range(extraStudents):
            g, pas, total = heapq.heappop(heap)
            pas += 1
            total += 1
            g = gain(pas, total)
            heapq.heappush(heap, (-g, pas, total))

        # Compute final average
        total_avg = sum(pas / total for _, pas, total in heap)
        return total_avg / len(classes)
```

---

### ⏱️ Time & Space Complexity

* **Time:** O((n + extraStudents) log n)

  * Each heap push/pop costs log(n).
  * We do this for `n` initializations + `extraStudents` assignments.

* **Space:** O(n) for the heap.

---

### 🧩 Key Takeaways

* ✅ The **gain function** is the key insight — quantify the benefit of adding a student.
* 💡 Using a **max heap** makes greedy selection efficient.
* 💭 Many allocation/optimization problems reduce to "compute marginal gain → pick max → update."

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? (Partially — needed insight for gain function)
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week? (Yes, heap + marginal gain pattern is memorable)

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `73`    |
| Total Problems Solved | `434`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
