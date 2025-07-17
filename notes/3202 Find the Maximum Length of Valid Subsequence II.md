## 🧠 Solving LeetCode Until I Become Top 1% — Day `46`

### 🔹 Problem: [Maximum Length of a Subsequence With Modular Sum Zero](https://leetcode.com/problems/maximum-length-of-a-subsequence-with-modular-sum-zero)

**Difficulty:** #Medium
**Tags:** #DP, #Array, #Greedy, #Math

---

### 📝 Problem Summary

> Given an array `nums` and an integer `k`, you need to find the length of the **longest subsequence** where **every pair of adjacent elements** `(a, b)` satisfies:
> `(a + b) % k == 0`.

---

### 🧠 My Thought Process

- **Naive Brainstorming (a.k.a "The idea was there... kinda"):**

  - I figured it had something to do with remainders because of `% k`.
  - I was thinking in terms of pairing mods somehow — so the **core idea** managed to show up to class.
  - But when it came time to actually write working code?
    🙃 Hello darkness, my old friend — tabulation DP strikes again.

- **Why I Couldn't Implement It:**

  - Because it's tabulation and my brain just refuses to store 2D DP tables in memory like a normal human.
  - Every time I try to update a `dp[i][j]` I end up wondering if I’m accidentally simulating the collapse of spacetime.

- **What Actually Works:**

  - Create a 2D DP table `dp[prev][curr]`, where each cell stores the max length of a subsequence ending with modulo pair `(prev, curr)`.
  - Update by flipping:
    If current number is `num % k`, then for each `prev` in `[0, k-1]`,
    `dp[prev][num] = dp[num][prev] + 1`
    Because `(a + b) % k == 0` ⇨ `a % k == (-b) % k`.

---

### ⚙️ Code Implementation (Python)

```python
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]  # dp[prev_mod][curr_mod]
        res = 0
        for num in nums:
            num %= k
            for prev in range(k):
                dp[prev][num] = dp[num][prev] + 1
                res = max(res, dp[prev][num])
        return res
```

> 💥 This solution works because it leverages the modular symmetry. You basically abuse the 2D array to remember the last good match, and mutate it like a boss.

---

### ⏱️ Time & Space Complexity

- **Time:** `O(n * k)`
  We iterate over all `n` elements and try pairing each with `k` mod classes.

- **Space:** `O(k^2)`
  The 2D DP table holds best subsequence lengths for each modulo pair.

---

### 🧩 Key Takeaways

- ✅ Even if your tabulation brain is weak, recognizing a problem as **modular + pair-based** is already half the battle.
- 🧠 When `% k` is involved, think in terms of remainders, not actual numbers.
- 🙃 Don't be ashamed of struggling with DP tables. They’re evil, and you’re brave for trying.

---

### 🔁 Reflection (Self-Check)

- [ ] Could I implement this myself without crying?
- [x] Did I at least think in the right direction?
- [x] Do I now understand the logic?
- [x] Will I revisit this later with a new appreciation for `dp[i][j]`?

---

### 📚 Related Problems

- [[300 Longest Increasing Subsequence]]
- [[2915 Length of the Longest Subsequence That Sums to Target]]

---

### 🚀 Progress Tracker

| Metric                | Value                    |
| --------------------- | ------------------------ |
| Day                   | `46`                     |
| Total Problems Solved | `387`                    |
| Confidence Today      | 😐 (DP strikes again...) |
| Leetcode Rating       | `1572`                   |
