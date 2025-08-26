
## 🧠 Solving LeetCode Until I Become Top 1% — Day `66`

### 🔹 Problem: [3000. Maximum Area of Longest Diagonal Rectangle](http://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/description/?envType=daily-question&envId=2025-08-26)

**Difficulty:** #Easy
**Tags:** #Array #Math

---

### 📝 Problem Summary

> You are given a 2D integer array `dimensions` where `dimensions[i] = [li, wi]` indicates that the `iᵗʰ` rectangle has a length of `li` and a width of `wi`.

> Return the area of the rectangle with the largest area among all rectangles that have the longest diagonal. If there are multiple rectangles with the longest diagonal, return the largest area among them.
---

### 🧠 My Thought Process

- **Optimized Strategy:**
  _It's just a simple conditional maximization problem. We need to calculate the diagonal and area for each rectangle and keep track of the maximum diagonal and corresponding maximum area._

---

### ⚙️ Code Implementation (Python)

```python
# Brief comment about the approach
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mdiag = -1
        marea = -1

        for l, w in dimensions:
            diag = l**2 + w**2
            area = l*w

            if diag > mdiag or (mdiag == diag and area>marea):
                mdiag = diag
                marea = area

        return marea
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) where n is the number of rectangles in dimensions
- **Space:** O(1) constant space

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
    - Simple iteration with conditional checks to maintain maximum values.
- 💡 What made this problem tricky?
    - Ensuring to check both diagonal length and area correctly.
- 💭 How will I recognize a similar problem in the future?
    - Look for problems that require maximizing or minimizing values based on multiple criteria.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value        |
| --------------------- | ------------ |
| Day                   | `66`          |
| Total Problems Solved | `429`          |
| Confidence Today      | 😃 / 😐 / 😣 |
| Leetcode Rating       | `1530`       |
