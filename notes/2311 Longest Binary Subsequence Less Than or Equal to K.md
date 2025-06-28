## 🧠 Solving LeetCode Until I Become Top 1% — Day `31`

### 🔹 Problem: [2311. Longest Binary Subsequence Less Than or Equal to K](https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/description/?envType=daily-question&envId=2025-06-26)

**Difficulty:** #Medium
**Tags:** #Greedy, #BitManipulation

---

### 📝 Problem Summary

You're given a **binary string `s`** and an integer `k`.
You need to **select a subsequence** (characters in order, skipping allowed) such that:

- That subsequence (as a binary number) is **less than or equal to `k`**.
- The **length** of this subsequence is **maximized**.

Return the **maximum possible length** of such a valid subsequence.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  This porblem is all the `avengers` of subsequences! Caught me off guard with the constraints. First of all it's a subsequence problem, so I I thoguht it has to be a [[dp]] problem. The it also is a binary string, so I it's a dynamic bit manipulation problem. Then it hit me that it's a medium problem, so it can't be that hard. So, I thought [[Greedy]] would be the way to go. But couldn't figure out how to do it. I was thinking of generating all subsequences and checking their values, but that would be too slow (O(2^n)). So, as i did for many of my previous problems, I decided to **look up the solution**.

- **Greedy Observations:**
  I noticed that `'0'`s **don’t contribute to the binary value**, so you can safely include them all.
  For `'1'`s, their **position in the binary string matters** (left = more value), so we must be selective.

  A key idea clicked when I realized we should **iterate from the right (LSB side)** so we can **build up the smallest possible binary value**, and greedily decide whether to include a `'1'`.

- **Bit Boundaries:**
  We can't include too many `'1'`s from the left, because `k` may only have `X` bits — any subsequence with more than `X` bits is guaranteed to be greater than `k`.

---

### ✅ Optimal Solution

**Greedy Approach, scanning from the end (LSB):**

1. Start from the **rightmost bit** of the binary string.
2. Always include `'0'`s — they don't affect value.
3. For each `'1'` at index `i` from the right:

   - Check if adding `2^i` (the value it would contribute in binary) **keeps total ≤ `k`**.
   - Only include it if the resulting value remains valid.

4. Use `k.bit_length()` to determine how many bits we can safely use.

This way, we maximize the count of characters (mostly `'0'`s and safe `'1'`s).

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        sm = 0                # running binary value of selected subsequence
        cnt = 0               # number of selected characters
        bits = k.bit_length() # how many bits max we can use to stay ≤ k

        for i, ch in enumerate(reversed(s)):
            if ch == "1":
                if i < bits and sm + (1 << i) <= k:
                    sm += 1 << i
                    cnt += 1
            else:
                cnt += 1  # always include '0'
        return cnt
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) — We iterate over each character once.
- **Space:** O(1) — Only a few variables for counting.

---

### 🧩 Key Takeaways

- ✅ Learned how `k.bit_length()` helps bound the maximum size of binary values.
- 💡 Trickiest part was realizing that `'0'` can always be included and that **value contribution depends on position**.
- 💭 In future problems, I’ll be on the lookout for **bit-based greedy constraints** — especially in problems involving subsequences and max values.

---

### 🔁 Reflection (Self-Check)

- [ ] Could I solve this without help? → ❌ Not entirely. I needed guidance to grasp the greedy logic fully.
- [ ] Did I write code from scratch? → ❌ No, but I understand every line now.
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[1702 Maximum Binary String After Change]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `31`  |
| Total Problems Solved | `364` |
| Confidence Today      | 😐    |
