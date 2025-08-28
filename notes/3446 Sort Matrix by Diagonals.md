## 🧠 Solving LeetCode Until I Become Top 1% — Day `69`

### 🔹 Problem: [3446 Sort Matrix by Diagonals](https://leetcode.com/problems/sort-matrix-by-diagonals/description/?envType=daily-question&envId=2025-08-28)

**Difficulty:** #Medium
**Tags:** #Matrix, #HashMap, #Sorting

---

### 📝 Problem Summary

> You are given a 2D grid. Each diagonal of the matrix (identified by the difference `row - col`) must be sorted independently.
>
> * Diagonals starting from the top-right should be sorted in **descending order**.
> * Diagonals starting from the top-left should be sorted in **ascending order**.
>   Return the modified matrix after sorting each diagonal.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Extract each diagonal separately into a list, sort it, and then put the sorted values back. But this requires a lot of manual tracking of diagonals.

* **Optimized Strategy:**
  Instead of treating diagonals manually, use the property that each diagonal is uniquely identified by `row - col`.

  * Store elements of each diagonal in a `hashmap` where `key = row - col`.
  * Sort diagonals:

    * If `key < 0` (upper diagonals), sort **descending**.
    * If `key >= 0` (lower diagonals), sort **ascending**.
  * Refill the matrix by popping elements back in the correct order.

* **Algorithm Used:**
  `HashMap for grouping + Sorting each diagonal independently`.

---

### ⚙️ Code Implementation (Python)

```python
from collections import defaultdict
from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(list)
        rows = len(grid)
        cols = len(grid[0])

        # Group elements by diagonal (key = row - col)
        for row in range(rows):
            for col in range(cols):
                key = row - col
                hashmap[key].append(grid[row][col])

        # Sort each diagonal
        for key in hashmap:
            if key < 0:
                hashmap[key].sort(reverse=True)
            else:
                hashmap[key].sort()

        # Refill the matrix with sorted diagonals
        for row in range(rows):
            for col in range(cols):
                key = row - col
                grid[row][col] = hashmap[key].pop()

        return grid
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(m × n × log(min(m, n))) — each diagonal is sorted individually.
* **Space:** O(m × n) — hashmap storage for all diagonals.

---

### 🧩 Key Takeaways

* ✅ Learned the trick that diagonals in a matrix can be grouped using `row - col`.
* 💡 The twist was handling different sort orders (ascending vs descending) depending on diagonal position.
* 💭 For future diagonal problems, always check if `row - col` or `row + col` can uniquely represent them.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week? 
---

### 📚 Related Problems

* [[1329 Sort the Matrix Diagonally]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `69`    |
| Total Problems Solved | `430`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
