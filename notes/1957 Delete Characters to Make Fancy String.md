
## 🧠 Solving LeetCode Until I Become Top 1% — Day `50`

### 🔹 Problem: [1957. Delete Characters to Make Fancy String](https://leetcode.com/problems/delete-characters-to-make-fancy-string/)

**Difficulty:** #Easy
**Tags:** #String

---

### 📝 Problem Summary

Given a string `s`, remove the **minimum** number of characters such that there are **no three consecutive characters** that are the same. Return the resulting string.
✅ The answer is guaranteed to be unique.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  I initially tried to simulate the string modification by scanning it and using `pop(i)` whenever I found three repeating characters. But... yeah, `pop()` on a list is **O(n)** if it's not at the end — and I was doing it potentially `n` times. So... it timed out.

* **Optimized Strategy:**
  I realized instead of deleting from the original string, I could **build a new one** from scratch:

  * Start with an empty result list.
  * Loop through each character.
  * Append the character **only if** the last two characters in the result are **not equal to the current character**.

  This way, I never have three in a row — and all operations are fast (`O(1)` per append/check).

* **Algorithm Used:**
  Simple **greedy + string construction** strategy.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def makeFancyString(self, s: str) -> str:
        res = []
        for c in s:
            if len(res) >= 2 and res[-1] == res[-2] == c:
                continue
            res.append(c)
        return ''.join(res)
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) — One pass through the string with constant time operations.
* **Space:** O(n) — To store the resulting string.

---

### 🧩 Key Takeaways

* ✅ Reversing your approach can turn a brute force into a greedy O(n) solution.
* 💡 Avoid modifying a list in-place with `pop(i)` inside a loop unless you're popping from the end.
* 💭 If a problem talks about **"consecutive" characters**, consider a **sliding window of size 2 or 3**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[3316 Find Maximum Removals From Source String]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `50`    |
| Total Problems Solved | `391`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
