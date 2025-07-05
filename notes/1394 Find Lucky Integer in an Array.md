
## 🧠 Solving LeetCode Until I Become Top 1% — Day `38`

### 🔹 Problem: [1394 Find Lucky Integer in an Array](https://leetcode.com/problems/find-lucky-integer-in-an-array)

**Difficulty:** #Easy
**Tags:** #Array, #HashTable, #Counter

---

### 📝 Problem Summary

> You’re given an array of integers. A **lucky integer** is an integer whose **value is equal to its frequency** in the array.
> You need to find the **largest lucky integer**, or return -1 if none exist.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - Count frequency of each element manually using nested loops.
  - Check if the element’s value equals its frequency.
  - Time complexity would be horrible — O(n²). Clearly not great.

- **Optimized Strategy:**

  - Use a `Counter` from `collections` to get frequency in O(n).
  - Then, iterate over the frequency map in **descending order** of the key.
  - Return the **first value** where the key matches its frequency.
  - Why descending order? Because we need the **largest** such lucky integer.

- **Algorithm Used:**
  [[Counter]]

---

### ⚙️ Code Implementation (Python)

```python
from collections import Counter

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        c = Counter(arr)
        for k in sorted(c.keys(), reverse=True):
            if k == c[k]:
                return k
        return -1
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) — for sorting the keys
- **Space:** O(n) — to store frequencies in the counter

---

### 🧩 Key Takeaways

- ✅ Learned that combining `Counter` with sorted key traversal solves many frequency-based problems efficiently.
- 💡 Sorting in reverse helped instantly grab the **maximum** valid lucky number.
- 💭 This is a great pattern: _frequency check + reverse sort_ for max/min valid value extraction.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

Honestly, this was one of those satisfying ones where everything just _clicked_.

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `38`  |
| Total Problems Solved | `374` |
| Confidence Today      | 😃    |
