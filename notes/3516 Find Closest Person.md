## 🧠 Solving LeetCode Until I Become Top 1% — Day `74`

### 🔹 Problem: [3516 Find Closest Person](https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04)

**Difficulty:** #Easy
**Tags:** #Math, #Comparison

---

### 📝 Problem Summary

First of all, maybe the EASIEST PROBLEM IN LEETCODE HISTORY.

You are given three integers `x`, `y`, and `z`. The task is to determine which of `x` or `y` is **closer to `z`**.

* If both are equally close → return `0`.
* If `x` is closer → return `1`.
* If `y` is closer → return `2`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  I think you can solve this eeeasily with simple math.

* **Optimized Strategy:**
  The brute force is optimal here — no loops, no data structures, just math.

  * Compute `|x - z|` and `|y - z|`.
  * Compare the two distances.
  * Decide the answer based on which difference is smaller.

* **Algorithm Used:**
  Pure **mathematical comparison** using absolute difference.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        x_abs = abs(x - z)
        y_abs = abs(y - z)

        if x_abs == y_abs:
            return 0
        elif x_abs < y_abs:
            return 1
        else:
            return 2
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(1) → Only a few arithmetic operations.
* **Space:** O(1) → No extra memory used.

---

### 🧩 Key Takeaways

* ✅ Learned how simple absolute difference comparisons solve closest-number problems.
* 💡 The trick is recognizing that **absolute difference** directly measures closeness.
* 💭 This technique can be reused in problems like “find closest element to a target in an array” (but with loops/binary search).

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? (Yes, straightforward math)
* [x] Did I write code from scratch? (Yes)
* [x] Did I understand why it works? (Yes, absolute difference logic)
* [x] Will I be able to recall this in a week? (Yes, very simple pattern)

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `74`    |
| Total Problems Solved | `437`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
