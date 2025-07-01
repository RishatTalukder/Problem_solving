## 🧠 Solving LeetCode Until I Become Top 1% — Day `36`

### 🔹 Problem: [3330. Find the Original Typed String I](https://leetcode.com/problems/find-the-original-typed-string-i/description/?envType=daily-question&envId=2025-07-01)

**Difficulty:** #Easy
**Tags:** #String

---

### 📝 Problem Summary

> Given a string `word`, count how many _possible strings_ you can form by changing **some characters** (but not necessarily all). In this context, the number of possible strings is increased each time **two consecutive characters are equal**. Return the total number of such possibilities.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Try to generate all possible string variations and count — this would be exponential (`O(2^n)`), totally overkill for this problem.

- **Optimized Strategy:**
  The pattern is much simpler: every time you encounter a **pair of consecutive equal characters**, it adds another possible way to modify the string.

  - Start with `ans = 1` (for the original string).
  - For each position `i` from `1` to `n-1`, if `word[i] == word[i-1]`, we can consider another possible string variation.
  - Just iterate once and count.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def possibleStringCount(self, word: str) -> int:
        n, ans = len(word), 1
        for i in range(1, n):
            if word[i - 1] == word[i]:
                ans += 1
        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) — One pass through the string
- **Space:** O(1) — No extra space used

---

### 🧩 Key Takeaways

- ✅ You don't always need to simulate everything. Look for _patterns_.
- 💡 When a question asks about _counting variations_, always check if greedy one-pass observation is enough.
- 💭 If I see a similar pattern with "consecutive matching characters", I'll think of this problem.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[500 Keyboard Row]]
- [[2810 Faulty Keyboard]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `36`  |
| Total Problems Solved | `369` |
| Confidence Today      | 😃    |
