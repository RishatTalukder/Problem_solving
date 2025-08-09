## 🧠 Solving LeetCode Until I Become Top 1% — Day `54`

### 🔹 Problem: [Power of Two](https://leetcode.com/problems/power-of-two/)

**Difficulty:** #Easy
**Tags:** #Math #BitManipulation

---

### 📝 Problem Summary

Given an integer `n`, determine if it is a power of two. A number is a power of two if it can be written as `2^k` for some integer `k ≥ 0`.
Return `True` if `n` is a power of two, otherwise return `False`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * Keep dividing `n` by 2 while it’s even.
  * If we ever hit an odd number before `n` becomes 1, it’s not a power of two.
  * If we reach 1 exactly, it is a power of two.
  * This works because a power of two in binary has exactly one `1` bit.

* **Optimized Strategy:**

  * Use bitwise trick:
    `n > 0 and (n & (n - 1)) == 0`
    This works because powers of two have exactly one bit set, so subtracting `1` flips that bit and sets all bits after it to `1`. AND-ing them results in `0`.
  * But here, I implemented the **division approach**, which is still O(log n) and easy to understand.

* **Algorithm Used:**
  Simple iterative division check.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n != 1:
            if n % 2 == 1 or n == 0:
                return False
            n //= 2
        return True
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(log n) — Each step halves `n`.
* **Space:** O(1) — No extra memory used.

---

### 🧩 Key Takeaways

* ✅ Powers of two in binary have **only one bit set**.
* 💡 Division method is beginner-friendly, bitwise method is constant-time.
* 💭 If a problem involves checking for power of two, consider both math and bit tricks.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[326 Power of Three]]
* [[191 Number of 1 Bits]]
* [[342 Power of Four]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `54`    |
| Total Problems Solved | `410`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
