## 🧠 Solving LeetCode Until I Become Top 1% — Day `75`

### 🔹 Problem: [2749 Minimum Operations to Make the Integer Zero](https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/?envType=daily-question&envId=2025-09-05)

**Difficulty:** #Medium
**Tags:** #Math, #BitManipulation, #Greedy

---

### 📝 Problem Summary

> You’re given two integers `num1` and `num2`. In one operation, you can subtract `num2 * k` from `num1`. The goal is to find the smallest integer `k` such that the result can be represented as the sum of exactly `k` powers of two (not necessarily distinct). If no such `k` exists, return -1.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Try all possible `k` values, compute `x = num1 - num2*k`, then check if `x` can be broken into exactly `k` powers of two.
  But checking this naively for large numbers would be too slow.

* **Optimized Strategy:**

  * After subtracting, we get `x = num1 - num2*k`.
  * For `x` to work:

    1. `x ≥ k` (since the smallest way to split is all ones, requiring at least `k`).
    2. `k ≥ popcount(x)` (since we need at least one summand for each set bit in binary).
  * The smallest valid `k` is the answer.

* **Algorithm Used:**
  Math + Bit Manipulation (`bit_count` to check popcount condition).

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:  # impossible since we can't split into k parts
                return -1
            if k >= x.bit_count():  # valid if k >= popcount(x)
                return k
            k += 1
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(num1 / num2) in worst case (looping k), but usually small because conditions fail quickly.
* **Space:** O(1).

---

### 🧩 Key Takeaways

* ✅ Learned that `popcount(x)` gives the *minimum* number of summands (powers of two) needed to form `x`.
* 💡 The tricky part was realizing you also need `x ≥ k` to bound the maximum possible summands.
* 💭 Similar problems often combine **math inequalities + binary representations**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? (No, needed some guidance)
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week? (Need to revisit binary condition intuition)

---

### 📚 Related Problems

* [[1658 Minimum Operations to Reduce X to Zero]]
* [[991 Broken Calculator]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `75`    |
| Total Problems Solved | `438`    |
| Confidence Today      | 😐     |
| Leetcode Rating       | `1530` |
