## 🧠 Solving LeetCode Until I Become Top 1% — Day `64`

### 🔹 Problem: [3195. Find the Minimum Area to Cover All Ones I](https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/description/?envType=daily-question&envId=2025-08-22)

**Difficulty:** #Medium
**Tags:** #Array, #Matrix

---

### 📝 Problem Summary

> Finding the smallest area rectangle that can cover all `1`s in a binary matrix. The rectangle must be axis-aligned and can only contain `1`s.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _My solution is kinda brute force, because I will iterate through the entire matrix to find the minimum and maximum row and column indices that contain `1`s. This gives us the bounds of the rectangle that covers all `1`s._

- **Optimized Strategy:**
  _Instead of checking every possible rectangle, I directly find the minimum and maximum indices of rows and columns that contain `1`s. This reduces the problem to a simple calculation of area based on these indices. It's pretty efficient since we only traverse the matrix once._

---

### ⚙️ Code Implementation (Python)

```python
# Brief comment about the approach
from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0]) if grid else 0
        min_row, max_row = rows, -1
        min_col, max_col = cols, -1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)

        if max_row == -1:
            return 0
        return (max_row - min_row + 1) * (max_col - min_col + 1)

```

---

### ⏱️ Time & Space Complexity

- **Time:** O(rows \* cols) - We traverse the entire matrix once.
- **Space:** O(1) - We use a constant amount of space for variables.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  _Nothing new, just a straightforward application of finding bounds in a matrix._
- 💡 What made this problem tricky?
  _The tricky part was ensuring that I correctly identified the bounds of the rectangle and handled edge cases where there are no `1`s._
- 💭 How will I recognize a similar problem in the future?
  _Look for problems that require finding bounds or areas in a grid or matrix, especially when dealing with binary values._

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value     |
| --------------------- | --------- |
| Day                   | `64`      |
| Total Problems Solved | `425`     |
| Confidence Today      | 😃        |
| Leetcode Rating       | `1530` 👀 |
