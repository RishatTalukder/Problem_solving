# 📍395. Longest Substring with At Least K Repeating Characters

- 💡 Difficulty: Medium
- 🧩 Tags: #DivideAndConquer #Recursion #String
- 🔄 Pattern:[[Divide_and_Conquer]] [[Recursion]]
- 🔍 Link: [LeetCode Link](https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/)

---

## 🧠 Problem Summary

Given a string `s` and an integer `k`, we need to return the **length** of the **longest substring** where **every character appears at least `k` times**. If no such substring exists, return 0.

---

## 🚫 Brute Force Approach

The naive idea would be to **generate all substrings** and check the frequency of characters in each. But this takes **O(n³)** time:

- O(n²) for generating all substrings.
- O(n) for checking each one.

This would TLE for `s.length = 10⁴`.

---

## ✅ Optimal Solution

We use **divide and conquer with recursion**:

1. If the entire string is valid (all characters appear ≥ k times), return the length.
2. Otherwise, **find a character whose total frequency is less than `k`**.

   - This character cannot be in any valid substring.
   - So we **split the string at that character** (like a delimiter).

3. Recursively solve each split part, and take the **maximum length** of the valid substrings.

### Why This Works:

By always splitting at characters that disqualify the entire string, we reduce unnecessary checking and isolate potentially valid segments.

---

## 📦 Code (Python)

```python
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        for ch in set(s):
            if s.count(ch) < k:
                subs = s.split(ch)
                return max(self.longestSubstring(sub, k) for sub in subs)

        return len(s)
```

---

## 📊 Complexity

- **Time:** O(n²) in worst case (because of repeated splits and string operations)
- **Space:** O(n) for recursive call stack and substring splits

---

## 📝 Notes

- 🔥 Clever divide and conquer — we only split at “bad” characters that can’t be in the result.
- 💡 Base case is crucial: if `len(s) < k`, return 0 early to avoid unnecessary recursion.
- 🧠 String `.count()` and `.split()` are used well — but remember they can be expensive if not optimized.
