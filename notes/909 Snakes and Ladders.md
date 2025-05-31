## 🧠 Solving LeetCode Until I Become Top 1% — Day `5`

### 🔹 Problem: [909 Snakes and Ladders](https://leetcode.com/problems/snakes-and-ladders/description/?envType=daily-question&envId=2025-05-31)

**Difficulty:** #Medium
**Tags:** #Matrix #BFS #Graph #BruteForce

---

### 📝 Problem Summary _(in your own words)_

> Find the minimum number of moves to reach the last square of a Snakes and Ladders board, where each move can be from 1 to 6 squares forward. The board has snakes that send you back and ladders that take you forward.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This problem is actually a brute force problem, But in top of that we can use BFS to find the shortest path._

- **Optimized Strategy:**
  _We can use a BFS approach to explore all possible moves from the current position. Each position on the board can be treated as a node in a graph, and the edges represent valid moves (1 to 6 squares forward). We also need to account for snakes and ladders by mapping them to their respective destinations._

  - We can use a `visited` set to keep track of the squares we have already visited to avoid cycles.
  - Everytime we reach a square, we check if it has a snake or ladder and move accordingly.
  - And keep track of how many moves we have made so far.

- **Algorithm Used:**
  [[Shortest Path in Unweighted Graph]]

---

### ⚙️ Code Implementation (Python)

```python
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_position(s):
            """Convert square number to (row, col) on board."""
            quot, rem = divmod(s - 1, n)
            row = n - 1 - quot
            col = rem if (quot % 2 == 0) else n - 1 - rem
            return row, col

        visited = set()
        queue = deque([(1, 0)])  # (square number, move count)

        while queue:
            curr, moves = queue.popleft()
            for i in range(1, 7):
                next_square = curr + i
                if next_square > n * n:
                    continue
                row, col = get_position(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                if next_square == n * n:
                    return moves + 1
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # If we can't reach the end

```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n^2)
  - Each square can be visited once, and for each square, we check up to 6 possible moves.
  - The BFS ensures we explore all reachable squares efficiently.
- **Space:** O(n^2)
  - The `visited` set can grow to the size of the board, and the queue can also hold all squares in the worst case.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  _I learned how to model a board game as a graph and use BFS to find the shortest path in an unweighted graph._
  _Finding the position on the board using a mathematical formula to convert from 1D to 2D coordinates was also a key insight._
- 💡 What made this problem tricky?
  _The tricky part was converting the board's 2D representation into a 1D representation for easier traversal and handling the snakes and ladders efficiently._
- 💭 How will I recognize a similar problem in the future?
  _Finding the shortest path in a grid or board game is a common pattern. If I see a problem involving movement on a grid with obstacles or special rules (like snakes and ladders), I will think of using BFS or DFS to explore all possible paths._

---

### 🔁 Reflection (Self-Check)

- [🙄] Could I solve this without help?
- [😬] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[notes/2467 Most Profitable Path in a Tree]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `5`   |
| Total Problems Solved | `338` |
| Confidence Today      | 😃    |
