## 🧠 Solving LeetCode Until I Become Top 1% — Day `58`

### 🔹 Problem: [Power of Three](https://leetcode.com/problems/power-of-three/)

**Difficulty:** #Easy
**Tags:** #Math #Recursion

---

### 📝 Problem Summary

Check if a given integer `n` is a **power of three** — meaning it can be expressed as `3^k` for some non-negative integer `k`.
If yes, return `True`; otherwise, return `False`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Keep dividing `n` by 3 until we either:

  * reach exactly 1 → `True` (it’s a power of three), or
  * get a remainder (`n % 3 != 0`) → `False`.

* **Optimized Strategy:**
  This is already efficient because:

  * Each division by 3 reduces `n` by a factor of 3.
  * The number of steps is `O(log₃ n)`, which is tiny for any integer in range.
    Alternatively, I could check using **maximum power of three in int range** and modulus, but the loop is simpler.

* **Algorithm Used:**
  Iterative division + modulus check.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        while n != 1:
            if n % 3 != 0 or n == 0:
                return False
            n //= 3
        return True
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(log₃ n) — repeatedly dividing by 3.
* **Space:** O(1) — no extra storage.

---

### 🧩 Key Takeaways

* ✅ Using iterative division is a quick and intuitive way to check powers of a number.
* 💡 An alternative approach is using **math.log** or precomputing the largest power of three in integer range and checking divisibility.
* 💭 Problems like this also appear for powers of two, powers of four, etc., and the logic is nearly identical.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[231 Power of Two]]
* [[342 Power of Four]]
* [[1780 Check if Number is a Sum of Powers of Three]]
---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `58`    |
| Total Problems Solved | `414`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
