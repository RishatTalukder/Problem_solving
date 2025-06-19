## 🧠 Solving LeetCode Until I Become Top 1% — Day `24`

### 🔹 Problem: [2294. Partition Array Such That Maximum Difference Is K](https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k)

**Difficulty:** #Medium
**Tags:** #Greedy, #Sorting

---

### 📝 Problem Summary

You are given an array `nums` and an integer `k`. Your goal is to partition the array into **the minimum number of subsequences**, such that:

- Each subsequence contains **contiguous elements** (not necessarily adjacent in the original array, but you pick them together after sorting),
- The **maximum difference** between the smallest and largest element in a subsequence is at most `k`.

Return the **minimum number of such subsequences** required to partition the array.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  I initially thought about trying all groupings using backtracking or recursion, keeping track of the max and min in each group. But it was obviously too slow for large inputs (`n ≤ 10⁵`), and clearly would TLE.

- **Optimized Strategy:**
  Sorting the array simplifies the problem. Once sorted, we can just **greedily group** elements until the difference between the current element and the starting element exceeds `k`. When it does, start a new group.

  ✅ This way, we guarantee we form groups with the minimum possible size and minimize total groups.

- **Algorithm Used:**
  [[greedy]] + [[sorting]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        left = 0
        right = 0

        while right < len(nums):
            if nums[right] - nums[left] <= k:
                right += 1
            else:
                res += 1
                left = right

        return res + 1
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) — due to sorting
- **Space:** O(1) — no extra space used (in-place logic after sorting)

---

### 🧩 Key Takeaways

- ✅ Sorting + Greedy is a powerful combo when you care about differences between values.
- 💡 Don’t overthink with complicated DP when a greedy grouping strategy can work.
- 💭 Problems that ask for minimizing the number of groups with a constraint often hint at **greedy or sliding window**.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help? → Yes
- [x] Did I write code from scratch? → Yes
- [x] Did I understand why it works? → Yes
- [x] Will I be able to recall this in a week? → Absolutely. Classic greedy stuff.

---

### 📚 Related Problems

- [[1438 Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit]]
- [[2779 Maximum Beauty of an Array After Applying Operation]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `24`  |
| Total Problems Solved | `356` |
| Confidence Today      | 😃    |
