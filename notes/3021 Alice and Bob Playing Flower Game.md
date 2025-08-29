## 🧠 Solving LeetCode Until I Become Top 1% — Day `70`

### 🔹 Problem: [3021. Alice and Bob Playing Flower Game](https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-29)

**Difficulty:** #Medium
**Tags:** #Math, #Combinatorics

---

### 📝 Problem Summary

Alice and Bob play a game with `n` flowers and `m` flowers. Each chooses one flower. Alice wins **if the total number of petals is odd**.

You need to count the number of winning pairs `(x, y)` where `1 ≤ x ≤ n` and `1 ≤ y ≤ m`.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Loop through all pairs `(x, y)` and check if `x + y` is odd. That would be `O(n * m)`, which is too slow for large inputs.

- **Optimized Strategy:**

  - The solution was unexpectedly simple once I realized the parity logic:

  - Alice wins only when one number is **even** and the other is **odd**.
  - Count how many odds and evens are in `1..n` and `1..m`.

    - `odds_in_n = (n + 1) // 2`
    - `evens_in_n = n // 2`
    - `odds_in_m = (m + 1) // 2`
    - `evens_in_m = m // 2`

  - Winning pairs = `(odds_in_n * evens_in_m) + (evens_in_n * odds_in_m)`
  - Simplifies to `(n * m) // 2`.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n * m) // 2
```

---

### ⏱️ Time & Space Complexity

- **Time:** `O(1)`
- **Space:** `O(1)`

---

### 🧩 Key Takeaways

- ✅ Learned how to reduce brute-force counting to simple parity logic.
- 💡 The trick is noticing that **half of all pairs will have odd sums**.
- 💭 In future, whenever I see problems about sums being odd/even, I’ll try **counting odds and evens separately** instead of brute force.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week? → Let’s see 😅

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `70`   |
| Total Problems Solved | `431`  |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1530` |
