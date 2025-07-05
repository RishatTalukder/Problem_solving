## 🧠 Solving LeetCode Until I Become Top 1% — Day `25`

### 🔹 Problem: [3443 Maximum Distance After K Operations](https://leetcode.com/problems/maximum-distance-after-k-operations/)

**Difficulty:** #Medium
**Tags:** #Greedy, #PrefixSum, #Simulation

---

### 📝 Problem Summary

> You're given a string of directions like `'NSEW'`. You can change up to `k` of them into another direction. After walking according to this possibly modified path, what's the **maximum Manhattan distance** you can end up from the origin?

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  I knew I had to somehow simulate all the directions and check how far they took me. I thought of trying every combination of up to `k` changes to see what gave the farthest point, but that's exponential.

- **Optimized Strategy:**
  I figured I could **count occurrences** of `N`, `S`, `E`, `W`, then try to convert `S` into `N` (or vice versa), and similarly for `E`/`W`, to **maximize directional imbalance**. I even understood that converting `S → N` boosts distance by `+2`...
  But I wasn't 100% confident with how to distribute the `k` changes between axes, so I looked up the solution.

- **Algorithm Used:**
  [[Greedy]] [[Counter]] [[manhatten_distance]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0

        for it in s:
            if it == "N": north += 1
            elif it == "S": south += 1
            elif it == "E": east += 1
            elif it == "W": west += 1

            times1 = min(north, south, k)
            times2 = min(east, west, k - times1)

            ans = max(
                ans,
                self.count(north, south, times1) +
                self.count(east, west, times2)
            )

        return ans

    def count(self, d1: int, d2: int, ops: int) -> int:
        return abs(d1 - d2) + 2 * ops  # converting direction boosts distance by 2
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) — single pass through the string
- **Space:** O(1) — only counters used

---

### 🧩 Key Takeaways

- ✅ I learned that direction imbalance can be manipulated with a greedy strategy.
- 💡 Changing `S → N` increases the imbalance by 2, not 1.
- 💭 Next time I see a Manhattan distance with limited moves/modifications, I'll think in terms of balancing and maximizing axis difference.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help? → Almost, but needed validation.
- [x] Did I write code from scratch? → Yes, then compared.
- [x] Did I understand why it works? → Fully after exploring the `+2` gain.
- [x] Will I be able to recall this in a week? → Definitely.

---

### 📚 Related Problems

- [[1162 As Far from Land as Possible]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `25`  |
| Total Problems Solved | `356` |
| Confidence Today      | 😃    |
