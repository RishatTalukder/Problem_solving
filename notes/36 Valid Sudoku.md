## 🧠 Solving LeetCode Until I Become Top 1% — Day `71`

### 🔹 Problem: [36 Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

**Difficulty:** #Medium
**Tags:** #Array, #HashTable, #Matrix

---

### 📝 Problem Summary

> You are given a partially filled `9 x 9` Sudoku board. Each row, column, and `3x3` sub-box must not contain duplicate digits (from `1` to `9`).
> Return **true** if the board is valid according to Sudoku rules, otherwise return **false**.

> Note: The board does **not** need to be solved, only validated.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  For every cell, scan the entire row, column, and subgrid to check for duplicates. This would be inefficient since it repeatedly checks the same values.

- **Optimized Strategy:**
  Use **3 hash sets per row, per column, and per subgrid** to track existing values:

  - One set for each row
  - One set for each column
  - One set for each 3x3 box
  - While iterating, if a number already exists in the corresponding row, column, or box → invalid Sudoku.

---

### ⚙️ Code Implementation (Python)

```python
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == '.':
                    continue

                box_ind = (i // 3) * 3 + (j // 3)

                if (
                    val in rows[i] or
                    val in cols[j] or
                    val in boxes[box_ind]
                ):
                    return False

                rows[i].add(val)
                cols[j].add(val)
                boxes[box_ind].add(val)

        return True
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(81) → O(1) (since the board size is fixed 9x9).
- **Space:** O(81) → O(1) (at most 9×3 sets storing digits 1–9).

---

### 🧩 Key Takeaways

- ✅ Learned how to validate Sudoku using **3 parallel data structures (row, col, box)**.
- 💡 The trick was mapping `(i, j)` to a `3x3` box index using `(i//3)*3 + (j//3)`.
- 💭 Any problem involving checking constraints in multiple dimensions can often be solved with **parallel hash sets**.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week? (Need to reinforce the box index formula).

---

### 📚 Related Problems

- [[37 Sudoku Solver]]
- [[2133 Check if Every Row and Column Contains All Numbers]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `71`   |
| Total Problems Solved | `432`  |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
