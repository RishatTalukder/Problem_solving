
## 🧠 Solving LeetCode Until I Become Top 1% — Day `61`

### 🔹 Problem: [1323. Maximum 69 Number](https://leetcode.com/problems/maximum-69-number/)

**Difficulty:** #Easy
**Tags:** #Greedy, #Math

---

### 📝 Problem Summary

> You’re given a positive integer made up of only digits `6` and `9`. You are allowed to change **at most one digit** (`6 → 9` or `9 → 6`).
> The goal is to maximize the resulting number.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Replace each `6` with `9` one by one, compute all possible numbers, and pick the maximum. This works, but it’s wasteful.

* **Optimized Strategy (Greedy):**

  * To maximize, we only need to flip the **leftmost `6`** into `9`.
  * Why? Because digits on the left have higher weight in decimal representation.
  * No need to check further, just do a single replacement.

* **Algorithm Used:**
  **Greedy + String Manipulation**

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maximum69Number (self, num: int) -> int:
        # Convert number to string for easy manipulation
        num = str(num)

        # Replace only the first '6' with '9'
        num = num.replace('6', '9', 1)

        # Convert back to int and return
        return int(num)
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n), where n = number of digits (string scan + replacement).
* **Space:** O(n) due to string conversion.

---

### 🧩 Key Takeaways

* ✅ Greedy worked because we only need to maximize once at the **highest place value**.
* 💡 Learned that string manipulation can often simplify digit-based problems.
* 💭 Similar problems often involve changing **the most significant digit first**.

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
| Day                   | `61`    |
| Total Problems Solved | `417`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |

