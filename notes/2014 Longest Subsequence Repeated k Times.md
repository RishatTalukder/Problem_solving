## 🧠 Solving LeetCode Until I Become Top 1% — Day `32`

### 🔹 Problem: [2014. Longest Subsequence Repeated k Times](https://leetcode.com/problems/longest-subsequence-repeated-k-times/)

**Difficulty:** #Hard
**Tags:** #String, #Greedy, #BFS, #Hashing

---

### 📝 Problem Summary

> We are given a string `s` and an integer `k`. Our task is to find the **longest subsequence** (not substring) such that when this subsequence is repeated `k` times (i.e., `sub * k`), the resulting string is still a subsequence of `s`.
>
> If multiple valid solutions exist, return the **lexicographically largest** one. If no such subsequence exists, return an empty string.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - There was no waaaay, I could have come up with a brute force solution for this problem. The constraints are too large, and generating all subsequences would be infeasible.

- **Optimized Strategy:**

  - Any valid character in the final answer must appear **at least `k` times** in `s`.
  - Generate candidate subsequences using only these frequent characters.
  - Use **BFS** to build subsequences of increasing length.
  - For each candidate `sub`, check if `sub * k` is a subsequence of `s` using a greedy check via iterator traversal (`all(ch in iter(s) for ch in sub * k)`).
  - Use **reverse lexicographical BFS order** to ensure lexicographically largest answer is found first.

- **Algorithm Used:**

  - [[BFS]]
  - [[greedy]]
  - [[counter]]

---

### ⚙️ Code Implementation (Python)

```python
from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        candidate = sorted(
            [c for c, w in Counter(s).items() if w >= k], reverse=True
        )
        q = deque(candidate)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for ch in candidate:
                nxt = curr + ch
                it = iter(s)
                if all(c in it for c in nxt * k):
                    q.append(nxt)
        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** Worst-case exponential in terms of candidate growth, but pruned effectively using frequency filtering and subsequence validation.
- **Space:** O(N) — mainly for queue and frequency dictionary.

---

### 🧩 Key Takeaways

- ✅ Learned how **greedy + BFS** can solve what feels like a DP string problem.
- 💡 The trick of checking `sub * k` as a subsequence using `iter()` is powerful.
- 💭 Problems involving “repeated k times” often benefit from thinking in **multiples and frequency-based pruning**.

---

### 🔁 Reflection (Self-Check)

- [ ] Could I solve this without help? → ❌ Not fully. I understood the statement and explored ideas, but couldn't implement the working solution.
- [ ] Did I write code from scratch? → ❌ No, I referred to the editorial solution.
- [x] Did I understand why it works? → ✅ Yes, after explanation.
- [x] Will I be able to recall this in a week? → ✅ Yes, due to clear BFS structure and pruning trick.

---

### 📚 Related Problems

- [[395 Longest Substring with At Least K Repeating Characters]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `32`  |
| Total Problems Solved | `365`   |
| Confidence Today      | 😐    |
