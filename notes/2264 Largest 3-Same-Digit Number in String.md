## 🧠 Solving LeetCode Until I Become Top 1% — Day `59`

### 🔹 Problem: [Largest 3-Same-Digit Number in String](https://leetcode.com/problems/largest-3-same-digit-number-in-string/)

**Difficulty:** Easy
**Tags:** #String #Greedy

---

### 📝 Problem Summary

We are given a numeric string `num`.
We need to find the **largest substring of length 3** where all digits are the same (like `"777"` or `"333"`).
If there’s no such substring, return an empty string `""`.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Check every substring of length 3, verify if all three characters are equal, and keep track of the largest. This would work but requires many slice operations.

* **Optimized Strategy:**

  * Traverse the string **once** while counting consecutive identical digits.
  * When we find exactly three consecutive same digits, compare with the current maximum digit found.
  * Store only the **best digit** (no need to store the whole substring).
  * Build the final answer at the end by repeating that digit 3 times.

* **Algorithm Used:**
  **Single-pass scan** + **max tracking**.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count = 0
        prev = 'X'   # sentinel value
        maxd = ' '   # store max digit found
        
        for c in num:
            if c == prev:
                count += 1
            else:
                count = 1
            if count == 3:
                maxd = max(c, maxd)
            prev = c
        
        return "" if maxd == ' ' else maxd * 3
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) — single scan over `num`.
* **Space:** O(1) — constant variables.

---

### 🧩 Key Takeaways

* ✅ Consecutive character counting is often more efficient than substring slicing.
* 💡 Using `max()` on characters works directly since `'9' > '8' > ... > '0'` in ASCII.
* 💭 This approach can be adapted for problems like finding the **longest consecutive character sequence**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[1903 Largest Odd Number in String]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `59`    |
| Total Problems Solved | `415`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
