## 🧠 Solving LeetCode Until I Become Top 1% — Day `76`

### 🔹 Problem: [1304 Find N Unique Integers Sum up to Zero](https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/?envType=daily-question&envId=2025-09-07)

**Difficulty:** #Easy
**Tags:** #Math, #Constructive

---

### 📝 Problem Summary

> Given an integer `n`, return an array of `n` **unique integers** such that they sum up to 0.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Generate random numbers and try to adjust until their sum is zero. This would be messy and inefficient.

* **Optimized Strategy:**

  * Pair positive and negative integers: `(1, -1), (2, -2), ...`
  * If `n` is even, the pairs are enough.
  * If `n` is odd, just add `0` to balance everything out.
  * This guarantees uniqueness and ensures the sum is always 0.

* **Algorithm Used:**
  Constructive Math (pairing positives and negatives).

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(1, n // 2 + 1):
            ans.append(i)
            ans.append(-i)
        if n % 2 == 1:
            ans.append(0)
        return ans
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) — we generate `n` elements.
* **Space:** O(n) — storing the result array.

---

### 🧩 Key Takeaways

* ✅ Learned how constructive math can directly give the answer without brute force.
* 💡 The “pairing” trick is a powerful way to balance sums.
* 💭 If a problem asks for sums = 0 (or balanced counts), think about symmetry.

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
| Day                   | `76`    |
| Total Problems Solved | `440`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
