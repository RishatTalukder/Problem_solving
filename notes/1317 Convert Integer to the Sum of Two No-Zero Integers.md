
## 🧠 Solving LeetCode Until I Become Top 1% — Day `77`

### 🔹 Problem: [1317 Convert Integer to the Sum of Two No-Zero Integers](https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/?envType=daily-question&envId=2025-09-08)

**Difficulty:** #Easy
**Tags:** #Math, #BruteForce

---

### 📝 Problem Summary

We are given an integer `n`. We need to split it into two positive integers `A` and `B` such that:

1. `A + B = n`
2. Neither `A` nor `B` contains the digit `0`.

Return any valid pair `[A, B]`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Iterate over all possible values of `A` from `1` to `n-1`. For each `A`, compute `B = n - A`.
  Check if both numbers do **not contain the digit 0**.

* **Optimized Strategy:**
  Since the range is only `1` to `n-1`, the brute force is actually fine. The constraint is small enough that this simple approach passes.

* **Algorithm Used:**
  Simple **brute force search** with string conversion to detect `0`.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for A in range(1, n):
            B = n - A
            if "0" not in str(A) + str(B):
                return [A, B]
        return []
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n \* log(n))
  (We loop up to `n`, and string conversion/checking costs about `O(log n)` per number.)

* **Space:** O(1)
  (Only a few integers are stored at a time.)

---

### 🧩 Key Takeaways

* ✅ Checking digits via string conversion is often the simplest and fast enough for small constraints.
* 💡 Sometimes brute force is the *intended* solution when constraints are low.
* 💭 Always confirm input size before over-optimizing.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `77`    |
| Total Problems Solved | `441`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
