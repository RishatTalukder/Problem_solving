## 🧠 Solving LeetCode Until I Become Top 1% — Day `68`

### 🔹 Problem: [3459. Length of Longest V-Shaped Diagonal Segment](https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/description/?envType=daily-question&envId=2025-08-27)

**Difficulty:** Hard
**Tags:** #DynamicProgramming #Grid #DFS

---

### 📝 Problem Summary

> You are given a binary grid (`0`s and `1`s).
> A *V-shaped diagonal segment* is defined as a path that:
>
> * Starts at a cell with value `1`.
> * Moves diagonally in one of the four directions (↘, ↙, ↖, ↗).
> * At some point, **turns exactly once** clockwise (90°).
> * Alternates values along the path (`1 → 2 → 1 → 2 …`).
>
> The task is to find the **maximum length** of such a segment.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * From every `1` cell, try walking diagonally in all directions.
  * Keep track of visited cells and attempt to form a V-shape.
  * This would be exponential because at each step, you can choose to continue straight or turn → **too slow**.

* **Optimized Strategy:**

  * Notice that the segment is **strictly alternating** (`1-2-1-2…`).
  * We only need to know:

    * Current position `(x, y)`.
    * Current direction (which diagonal we’re going).
    * Whether we’ve already turned (boolean).
    * What value we expect next (`1` or `2`).
  * This screams **DFS + Memoization (cache)**.

* **Key Insight:**

  * If we move straight → continue the same direction.
  * If we haven’t turned yet → try turning clockwise and continue.
  * Use `@cache` so we don’t recompute states.

---

### ⚙️ Algorithm (Step-by-Step)

1. Define 4 diagonal directions:

   * `↘ (1,1)`, `↙ (1,-1)`, `↖ (-1,-1)`, `↗ (-1,1)`.

2. Write a recursive DFS function with memoization:

   * Input: `(x, y, direction, can_turn, expected_value)`.
   * Compute next `(nx, ny)` in the same direction.
   * If out of bounds or value ≠ expected → stop.
   * Otherwise:

     * Continue straight in same direction.
     * If `can_turn = True`, try turning clockwise and recurse.

3. Add `+1` at each successful step.

4. From every `1` in the grid, try all 4 directions with initial `can_turn=True`, expecting `2` next.

5. Keep global maximum.

---

### ⚙️ Code Implementation (Python)

```python
from functools import cache
from typing import List

class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]  # diagonals
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(x, y, d, can_turn, target):
            nx, ny = x + DIRS[d][0], y + DIRS[d][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            best = dfs(nx, ny, d, can_turn, 3 - target)  # continue straight
            if can_turn:
                best = max(best, dfs(nx, ny, (d + 1) % 4, False, 3 - target))  # turn
            return best + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # must start from 1
                    for d in range(4):
                        res = max(res, dfs(i, j, d, True, 2) + 1)
        return res
```

---

### ⏱️ Time & Space Complexity

* **Time:**
  Each state `(x, y, direction, can_turn, target)` is computed once →
  **O(m × n × 4 × 2 × 2) ≈ O(mn)**.

* **Space:**

  * Memoization cache → `O(mn)` states.
  * DFS recursion stack depth at most `O(m+n)`.

---

### 🧩 Key Takeaways

* ✅ Converted brute force into **stateful DFS + memoization**.
* 💡 Trick: No need to calculate actual diagonals → just use `(dx,dy)` pairs.
* 💭 Similar problems will involve **grid + path + direction + turn state** → DP over state space.

---

### 🔁 Reflection (Self-Check)

* [ ] Could I solve this without help? -> This problem had a lot of moving parts for me to handle alone. 
* [x] Did I understand why memoization was necessary?
* [x] Did I capture the turning logic correctly?
* [ ] Can I implement this again tomorrow without notes?

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `68`    |
| Total Problems Solved | `430`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |