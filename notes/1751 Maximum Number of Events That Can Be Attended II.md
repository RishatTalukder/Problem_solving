## 🧠 Solving LeetCode Until I Become Top 1% — Day `40`

### 🔹 Problem: [1751. Maximum Number of Events That Can Be Attended II](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/)

**Difficulty:** #Hard
**Tags:** #DP, #BinarySearch, #Greedy, #Sorting, #Memoization

---

### 📝 Problem Summary

You're given a list of events. Each event has a start day, end day, and value. You can attend at most `k` non-overlapping events. An event takes up the whole duration (you can't attend another that overlaps even by one day). Return the maximum value you can accumulate from attending events.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Try all combinations of `k` events and pick the one with the maximum total value — but this becomes computationally impossible for large inputs due to `O(2^n)` complexity.

- **Optimized Strategy:**

  - First, sort the events by start time.
  - For each event, you either:

    1. Skip it and move to the next.
    2. Attend it and jump to the next non-overlapping event using `bisect_right`.

  - Use DP to remember the best total value from each state `(i, remaining)`.
  - Either use `@lru_cache` or manual memoization with a dictionary.

- **Algorithm Used:**
  [[Top_Down_DP]] + [[Binary_Search]] + [[Memoization]]

---

### ⚙️ Code Implementation (Python)

```python
from bisect import bisect_right

class Solution:
    def maxValue(self, events, k):
        events.sort()
        start_days = [e[0] for e in events]
        n = len(events)
        memo = {}

        def dp(i, remaining):
            if i == n or remaining == 0:
                return 0
            if (i, remaining) in memo:
                return memo[(i, remaining)]

            skip = dp(i + 1, remaining)
            next_index = bisect_right(start_days, events[i][1])
            take = events[i][2] + dp(next_index, remaining - 1)

            memo[(i, remaining)] = max(skip, take)
            return memo[(i, remaining)]

        return dp(0, k)
```

---

### ⏱️ Time & Space Complexity

- **Time:** `O(n * k * log n)`

  - `n` is the number of events
  - `k` is the number of events you can attend
  - `log n` is from the binary search

- **Space:** `O(n * k)` for memoization

---

### 🧩 Key Takeaways

- ✅ Learned how to combine binary search with DP to skip over overlapping intervals efficiently.
- 💡 The trick was finding the next valid event after the current one using `bisect_right`.
- 💭 This is basically interval scheduling with a twist — instead of choosing max number of events, we choose max value with a cap `k`.

---

### 🔁 Reflection (Self-Check)

- [] Could I solve this without help? (Nope, the implementation might look simple, but the thought process was complex)
- [] Did I write code from scratch? (Nope again, but I adapted the logic)
- [x] Did I understand why it works? (Yes)
- [x] Will I be able to recall this in a week? (Yes, especially the `dp(i, remaining)` part)

---

### 📚 Related Problems

- [[1353 Maximum Number of Events That Can Be Attended]]

- [[2008 Maximum Earnings From Taxi]]

- [[2054 Two Best Non-Overlapping Events]]
- [[2402. Meeting Rooms III]]
---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `40`  |
| Total Problems Solved | `378` |
| Confidence Today      | 😐    |