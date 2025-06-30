## 🧠 Solving LeetCode Until I Become Top 1% — Day `35`

### 🔹 Problem: [594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/description/?envType=daily-question&envId=2025-06-30)

**Difficulty:** #Easy
**Tags:** #SlidingWindow, #Sorting

---

### 📝 Problem Summary

> Given an array of integers `nums`, return the **length** of the longest **harmonious subsequence**, where the **difference between the maximum and minimum element is exactly 1**.

> A subsequence is a sequence that can be derived from the array without changing the order of elements, and it doesn't have to be contiguous.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Loop through each element, and for each one, count how many elements exist with a value either equal to it or just one greater. This works but takes **O(n²)** — not optimal.

- **Optimized Strategy:**
  I figured out that sorting simplifies the problem. After sorting:

  - Use a **sliding window** (`j` and `i`) to keep track of the current window of elements.
  - If the difference between `nums[i]` and `nums[j]` is greater than 1, move `j` forward until the condition is satisfied.
  - If the difference is exactly 1, check the length of the current subarray and update the maximum length.

  At first, I used an `if` condition to adjust `j`, but it failed for cases where multiple elements needed to be skipped. The fix? Replace the `if` with a `while` loop — and boom, it worked.

### 📝 Algorithms Used

[[Sliding_Window]] [[Sorting]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def findLHS(self, nums):
        nums.sort()
        j = 0
        maxLength = 0

        for i in range(len(nums)):
            while nums[i] - nums[j] > 1:
                j += 1
            if nums[i] - nums[j] == 1:
                maxLength = max(maxLength, i - j + 1)
        return maxLength
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) — Sorting dominates
- **Space:** O(1) — No extra space besides a few variables

---

### 🧩 Key Takeaways

- ✅ Sliding window works best when dealing with **ranges or intervals** after sorting.
- 💡 The tricky part was updating the left pointer properly — an `if` wasn’t enough. `while` is your best friend in sliding window problems.
- 💭 I’ll recognize similar problems whenever a sorted array is involved and I need to track windowed properties like differences or frequencies.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help? → _Yes!_
- [x] Did I write code from scratch? → _Yup, just needed to tweak a loop._
- [x] Did I understand why it works? → _100%._
- [x] Will I be able to recall this in a week? → _Absolutely._

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `35`  |
| Total Problems Solved | `367` |
| Confidence Today      | 😃    |
