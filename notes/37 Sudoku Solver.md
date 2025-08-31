## 🧠 Solving LeetCode Until I Become Top 1% — Day `72`

### 🔹 Problem: [37 Sudoku Solver](https://leetcode.com/problems/sudoku-solver/?envType=daily-question&envId=2025-08-31)

**Difficulty:** #Hard
**Tags:** #Backtracking, #Matrix, #Recursion

---

### 📝 Problem Summary

> We are given a partially filled 9×9 Sudoku board. The task is to fill the empty cells (`.`) such that the Sudoku rules are satisfied:
>
> * Each row contains digits `1–9` without repetition
> * Each column contains digits `1–9` without repetition
> * Each of the nine 3×3 sub-boxes contains digits `1–9` without repetition
>
> The solution must modify the board **in-place**.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Try all numbers `1–9` in every empty cell and check if the board remains valid. This would be extremely slow because there are many possibilities.

* **Optimized Strategy:**
  Use **backtracking with constraints tracking**:
  
  * Sudoku is already solved partially in programming, So, this problem is more like a algorithm memorization problem.
  * Maintain three data structures (`rows`, `cols`, `boxes`) to quickly check if a number can be placed.
  * Instead of recomputing validity each time, update these structures when placing/removing numbers.
  * Recursively try to fill the board cell by cell.
  * If a placement leads to a dead end, undo (backtrack) and try another number.

* **Algorithm Used:**
  **Backtracking with pruning** using helper functions:

  * `couldPlace(val, row, col)` → checks if we can place a number.
  * `placeNumber(val, row, col)` / `removeNumber(...)` → update board + tracking arrays.
  * `backtrack(row, col)` → recursive filling with backtracking.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Modify the board in-place using backtracking.
        """
        n, N = 3, 9
        rows = [[0] * (N+1) for _ in range(N)]
        cols = [[0] * (N+1) for _ in range(N)]
        boxes = [[0] * (N+1) for _ in range(N)]
        solved = False

        def couldPlace(val, row, col):
            idx = (row // 3) * 3 + col // 3
            return rows[row][val] + cols[col][val] + boxes[idx][val] == 0

        def placeNumber(val, row, col):
            idx = (row // 3) * 3 + col // 3
            rows[row][val] += 1
            cols[col][val] += 1
            boxes[idx][val] += 1
            board[row][col] = str(val)

        def removeNumber(val, row, col):
            idx = (row // 3) * 3 + col // 3
            rows[row][val] -= 1
            cols[col][val] -= 1
            boxes[idx][val] -= 1
            board[row][col] = '.'

        def placeNext(row, col):
            nonlocal solved
            if row == N-1 and col == N-1:
                solved = True
            elif col == N-1:
                backtrack(row+1, 0)
            else:
                backtrack(row, col+1)

        def backtrack(row, col):
            nonlocal solved
            if board[row][col] == '.':
                for val in range(1, 10):
                    if couldPlace(val, row, col):
                        placeNumber(val, row, col)
                        placeNext(row, col)
                        if not solved:
                            removeNumber(val, row, col)
            else:
                placeNext(row, col)

        # Initialize constraints from given board
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    placeNumber(int(board[i][j]), i, j)

        backtrack(0, 0)
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(9^m) worst case, where `m` is the number of empty cells. Pruning (checking validity with sets/arrays) makes it much faster in practice.
* **Space:** O(81) = O(1) (fixed-size board + tracking arrays).

---

### 🧩 Key Takeaways

* ✅ Backtracking is powerful for constraint satisfaction problems like Sudoku.
* 💡 The **row, col, box tracking arrays** significantly reduce redundant checks.
* 💭 When faced with recursive filling problems, always think: “Can I prune invalid paths early with some data structure?”

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? (with some practice)
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [ ] Will I be able to recall this in a week? (I haven't memorized the exact code yet)

---

### 📚 Related Problems

* [[notes/36 Valid Sudoku]]
* [[notes/980 Unique Paths III]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `72`    |
| Total Problems Solved | `433`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
