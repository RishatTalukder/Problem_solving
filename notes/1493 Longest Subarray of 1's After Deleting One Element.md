## 🧠 Solving LeetCode Until I Become Top 1% — Day `65`

### 🔹 Problem: [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=daily-question&envId=2025-08-24)

**Difficulty:** #Medium
**Tags:** #SlidingWindow

---

### 📝 Problem Summary

> Given a binary array `nums`, you should delete one element from it. Return the size of the longest non-empty subarray containing only `1`'s in the resulting array. Return `0` if there is no such subarray.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _We can iterate through the array and count the number of 1's, but this would be inefficient._

- **Optimized Strategy:**
  _What we can do is use a sliding window approach to keep track of the number of 0's in the current window. We can expand the window by moving the right pointer and if we encounter more than one 0, we can move the left pointer to shrink the window until we have at most one 0 in the window. We keep track of the maximum length of the window minus one (to account for the deleted element)._

- **Algorithm Used:**
  [[Sliding_Window]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        ans = 0
        c = 0
        while r < len(nums):
            if nums[r] == 0:
                c += 1

            if c > 1:
                if nums[l] == 0:
                    c-= 1

                l+= 1

            ans = max(ans, r-l)

            r+= 1

        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
- **Space:** O(1)

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
    I solved this problem before, so it was a nice refresher on the sliding window technique.
- 💡 What made this problem tricky?
    Keeping track of the count of 0's in the window and ensuring we only have at most one 0.
- 💭 How will I recognize a similar problem in the future?
    Look for problems that involve finding the longest or shortest subarray with certain constraints, especially when dealing with binary arrays.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[1004 Max Consecutive Ones III]]

---

### 🚀 Progress Tracker

| Metric                | Value        |
| --------------------- | ------------ |
| Day                   | `65`         |
| Total Problems Solved | `427`        |
| Confidence Today      | 😃 / 😐 / 😣 |
| Leetcode Rating       | `1530`       |
