## 🧠 Solving LeetCode Until I Become Top 1% — Day `51`

### 🔹 Problem: [1695. Maximum Erasure Value](https://leetcode.com/problems/maximum-erasure-value/)

**Difficulty:** #Medium
**Tags:** #Array, #HashSet, #SlidingWindow

---

### 📝 Problem Summary

You're given an array of positive integers.
You need to select a subarray (contiguous elements) that contains only **unique** elements and has the **maximum possible sum**.

Return the maximum sum of such a subarray.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * Try all subarrays and calculate the sum if all elements are unique.
  * Time Complexity: O(n²) — definitely too slow for large inputs.

* **Optimized Strategy:**

  * Use a **sliding window** to keep track of a window with unique elements.
  * Use a set `dup` to quickly check for duplicates.
  * Maintain a running `total` of current window sum.
  * If a duplicate is found, shrink the window from the left until the duplicate is removed.

* **Algorithm Used:**
  ✅ [[Sliding_Window]]
  ✅ [[Hash_Set]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        left = 0
        dup = set()
        total = 0
        
        for right in range(len(nums)):
            while nums[right] in dup:
                total -= nums[left]
                dup.remove(nums[left])
                left += 1

            total += nums[right]
            dup.add(nums[right])
            res = max(res, total)

        return res
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) — each element is added and removed from the set at most once.
* **Space:** O(n) — in the worst case, the set could contain all `n` elements (if they're all unique).

---

### 🧩 Key Takeaways

* ✅ Learned how to use the sliding window technique to maintain a window of unique elements.
* 💡 The trick was realizing we could “slide” away duplicates by subtracting from the total sum dynamically.
* 💭 If I ever need to find the max/min of a property over a window with unique values — sliding window + set is a go-to.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[3 Longest Substring Without Repeating Characters]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `51`    |
| Total Problems Solved | `392`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
