## 🧠 Solving LeetCode Until I Become Top 1% — Day `21`

### 🔹 Problem: [2016. Maximum Difference Between Increasing Elements](https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/?envType=daily-question&envId=2025-06-16)

**Difficulty:** #Easy
**Tags:** #PrefixSum #KadanesAlgorithm

---

### 📝 Problem Summary _(in your own words)_

> Given an array of integers, find the maximum difference between two elements such that the larger element comes after the smaller one in the array.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _We can use a nested loop to check every pair of elements, but this will be inefficient because the time complexity will be O(n^2)._

- **Optimized Strategy:**
  **Although the O(n^2) approach works, there is a more efficient way to solve this problem using a single pass through the array. Keep this pattern in mind if you encounter a problem where you need to din the maximum or minimum of a sequence of elements you can use [[Prefix_Sum]] algorithm. But there is a catch prefix sum is a modified version of another [[dp]] algorithm called [[kadane's_algorithm]].**

  _"Kadene's algorithm keeps track of the past, only if it's valueable"_

  - **Key Insight:**
    - Maintain a variable to track the minimum value seen so far as you iterate through the array.
    - For each element, calculate the difference between the current element and the minimum value.
    - Update the maximum difference if this new difference is larger.

- **Algorithm Used:**
  [[kadane's_algorithm]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        res = -1
        mn = nums[0]


        for i in nums[1:]:
            if i > mn:
                res = max(res, i-mn)

            else:
                mn = i


        return res
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) — single pass through the array
- **Space:** O(1) — only a few variables used

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - **Kadane's Algorithm** can be adapted to find maximum differences in sequences.
- 💡 What made this problem tricky?
  - Recognizing that the problem can be solved in linear time rather than quadratic.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems that involve finding a result based on the relationship between elements in a sequence, especially keeping track of the previous minimum or maximum values.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[121 Best Time to Buy and Sell Stock]]
- [[2078 Two Furthest Houses With Different Colors]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `21`  |
| Total Problems Solved | `353` |
| Confidence Today      | 😃    |
