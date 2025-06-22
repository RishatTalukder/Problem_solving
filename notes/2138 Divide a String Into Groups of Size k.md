## 🧠 Solving LeetCode Until I Become Top 1% — Day `27`

### 🔹 Problem: [2138 Divide a String Into Groups of Size k](https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/?envType=daily-question&envId=2025-06-22)

**Difficulty:** #Easy
**Tags:** #String, #Greedy

---

### 📝 Problem Summary

> Given a string `s`, divide it into groups of size `k`. If the final group is smaller than `k`, fill it with the given `fill` character until it reaches length `k`.

Return a list of strings, each representing a group of size `k`.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - Start taking substrings of length `k` in a loop and append them to a result list.
  - If the final group is smaller than `k`, pad it manually.

- **Optimized Strategy:**

  - First, check if `s` is divisible by `k`. If not, **append the appropriate number of `fill` characters** to make its length divisible by `k`.
  - Then, iterate over the updated string with a **step of size `k`** and slice out chunks.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        n = len(s)

        s = s + (fill*(k-n%k) if n%k else '')

        start = 0

        while start < len(s):
            res.append(s[start:start+k])
            start += k

        return res

```

### ⏱️ Time & Space Complexity

- **Time:** O(N)
  Traverses the string once to pad (if needed), and once to slice.
- **Space:** O(N)
  Output list stores all the k-sized chunks.

---

### 🧩 Key Takeaways

- ✅ Learned how to chunk a string cleanly using **modulo logic** and **list comprehensions**.
- 💡 Edge cases like "what if the string isn't divisible by k?" must be handled **before chunking**.
- 💭 This pattern is helpful for problems involving **grouping, formatting**, or **padding** strings to meet constraints.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[68 Text Justification]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `27`  |
| Total Problems Solved | `360` |
| Confidence Today      | 😃    |
