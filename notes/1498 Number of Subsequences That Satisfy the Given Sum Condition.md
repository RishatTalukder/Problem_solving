## 🧠 Solving LeetCode Until I Become Top 1% — Day `34`

### 🔹 Problem: [1498. Number of Subsequences That Satisfy the Given Sum Condition](https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/)

**Difficulty:** #Medium
**Tags:** #TwoPointers, #Greedy, #Sorting, #BinarySearch, #Combinatorics

---

### 📝 Problem Summary

> Given a list of integers `nums` and an integer `target`, count the number of **non-empty subsequences** such that the **sum of the minimum and maximum elements** in the subsequence is less than or equal to the target.

Subsequences can be in any order and we care about the count, not the actual lists. Return the count modulo `10^9 + 7`.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  I could _technically_ generate all subsequences using backtracking or DFS, check their min + max, and count the valid ones. But, let's not... O(2^n) is a death sentence for even moderately-sized inputs.

- **Optimized Strategy:**
  This is where the fun began — I knew sorting would help (yay!), and I vaguely remembered something about using two pointers when dealing with subsequences and boundaries.

  The idea is:

  - Sort the array so that min/max pairs are easier to manage.
  - Fix the smallest element using a left pointer.
  - Then, use a right pointer to find the furthest index where `nums[left] + nums[right] <= target`.
  - The number of valid subsequences in that range is `2^(right - left)` (include/exclude middle elements).

  Now, **did I know this formula off the top of my head?**
  Of course not.
  **Did I panic and look it up?**
  Absolutely.
  **Combinatorics still haunts me in my dreams.**

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def numSubseq(self, nums, target):
        mod = 10**9 + 7
        nums.sort()
        n = len(nums)

        power = [1] * n
        for i in range(1, n):
            power[i] = (power[i - 1] * 2) % mod

        left, right = 0, n - 1
        result = 0

        while left <= right:
            if nums[left] + nums[right] <= target:
                result = (result + power[right - left]) % mod
                left += 1
            else:
                right -= 1

        return result
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) — Sorting dominates. The two-pointer scan is O(n).
- **Space:** O(n) — For the `power` table storing `2^i mod MOD`.

---

### 🧩 Key Takeaways

- ✅ When you see “count subsequences that satisfy a boundary condition”, you might not need to generate them all — just **count them** using math.
- 💡 Use sorting + two pointers when min/max or range comparisons are involved.
- 💭 Precomputing `2^i` is a **common trick** when you want to count subsets.

---

### 🔁 Reflection (Self-Check)

- [❌] Could I solve this without help?
  Haha. No. I had the right direction and then immediately crashed into a wall of fear and bitmask trauma.

- [❌] Did I write code from scratch?
  I modified and adapted what I found after shamelessly googling it.

- [✅] Did I understand why it works?
  After several hours of emotional support and revisiting middle school combinatorics? Yes.

- [✅] Will I be able to recall this in a week?
  Only if I tattoo `2^(right - left)` onto my forearm.

---

### 📚 Related Problems

- [[2835 Minimum Operations to Form Subsequence With Target Sum]]

- [[3098 Find the Sum of Subsequence Powers]]

- [[3082 Find the Sum of the Power of All Subsequences]]


---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `34`   |
| Total Problems Solved | `367`   |
| Confidence Today      | 😣    |
