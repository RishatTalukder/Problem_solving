
## 🧠 Solving LeetCode Until I Become Top 1% — Day `60`

### 🔹 Problem: [Power of Four](https://leetcode.com/problems/power-of-four/)

**Difficulty:** #Easy
**Tags:** #Math #BitManipulation

---

### 📝 Problem Summary

We are given an integer `n`.
We must check whether `n` is a **power of four** (i.e., can be written as `4^k` for some integer `k ≥ 0`).
Return `True` if it is, else `False`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Keep multiplying `4` until the value exceeds `n`, checking if it ever equals `n`.

* **Optimized Strategy:**

  * Since powers of 4 are always positive, discard `n ≤ 0` immediately.
  * Repeatedly divide `n` by `4` while it's divisible.
  * If we eventually reach `1`, then `n` is a power of four.
  * Avoid floating-point math (`log`) for precision safety.

* **Algorithm Used:**
  **Iterative Division** (a loop dividing by 4).

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n != 1:
            if (n % 4 != 0) or n == 0:
                return False
            n //= 4
        return True
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(log₄ n) — each step divides `n` by 4.
* **Space:** O(1) — constant memory.

---

### 🧩 Key Takeaways

* ✅ Powers of 4 are also powers of 2, but with even exponents in base-2 representation.
* 💡 Could also solve using **bit tricks**:

  * Check if `n` is power of two (`n & (n-1) == 0`)
  * AND `(n-1) % 3 == 0` to confirm it’s power of 4.
* 💭 This type of problem is common with "power of X" variations.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [Power of Two](https://leetcode.com/problems/power-of-two/)
* [Power of Three](https://leetcode.com/problems/power-of-three/)

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `60`    |
| Total Problems Solved | `416`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
