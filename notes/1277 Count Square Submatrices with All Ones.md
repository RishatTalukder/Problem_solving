## 🧠 Solving LeetCode Until I Become Top 1% — Day `63`

### 🔹 Problem: [1277. Count Square Submatrices with All Ones](https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/?envType=daily-question&envId=2025-08-20)

**Difficulty:** #Medium
**Tags:** #Array, #Matrix #DynamicProgramming

---

### 📝 Problem Summary

> Dinsing the square matrix subarrays that consist entirely of 1s, return the number of square submatrices that have all their sides of equal length and contain only 1s.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This is kind of a brute force problem where we can iterate through all possible submatrices and check if they are square and consist of all 1s. However, this would be inefficient._

- **Optimized Strategy:**
  _This problem has a simple twist: we can use dynamic programming to keep track of the size of the largest square submatrix ending at each cell. The value at each cell will be the minimum of the values from the top, left, and top-left diagonal cells plus one if the current cell is 1._

    - It's kinda hard to explain, but the idea is that if we have a square submatrix ending at (i, j), then the size of that square is determined by the minimum of the squares ending at (i-1, j), (i, j-1), and (i-1, j-1).

- **Algorithm Used:**
  [[Matrix]] [[dp]] 

---

### ⚙️ Code Implementation (Python)

```python
# Brief comment about the approach
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        res = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and i > 0 and j > 0:
                    matrix[i][j] = min(
                        matrix[i-1][j],
                        matrix[i][j-1],
                        matrix[i-1][j-1]
                    ) + 1
                res += matrix[i][j]

        return res
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(m * n)
- **Space:** O(1) - In-place modification of the input matrix

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
    _Dynamic programming can be used to efficiently count square submatrices by building on previously computed values._
- 💡 What made this problem tricky?
    _Understanding how to use the minimum of neighboring cells to determine the size of the square submatrix was key._
- 💭 How will I recognize a similar problem in the future?
    _Look for problems involving counting or finding submatrices, especially those that can be solved with dynamic programming._

---

### 🔁 Reflection (Self-Check)

- [ ] Could I solve this without help?
- [ ] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[2087 Minimum Cost Homecoming of a Robot in a Grid]]
- [[2088. Count Fertile Pyramids in a Land]]

---

### 🚀 Progress Tracker

| Metric                | Value        |
| --------------------- | ------------ |
| Day                   | `63`          |
| Total Problems Solved | `424`          |
| Confidence Today      | 😃 / 😐 / 😣 |
| Leetcode Rating       | `1572`       |
