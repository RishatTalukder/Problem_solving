## 🧠 Solving LeetCode Until I Become Top 1% — Day `33`

### 🔹 Problem: [2099. Find Subsequence of Length K With the Largest Sum](https://leetcode.com/problems/problem-slug/)

**Difficulty:** #Easy
**Tags:** #Greedy #Sorting

---

### 📝 Problem Summary

> Find the subset with the largest sum of length `k` from an array of integers.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _It wasn't that hard figure out. The trick is don't go for the `subsequence` and think that it is a `dfs/backtracking` problem. Instead, it is a `greedy` problem where you just need to find the `k` largest elements._

- **Optimized Strategy:**

  1. **Attach each number to its original index:**

  - For every element in the list `nums`, create a pair of `(index, value)`.
  - This helps us keep track of the original position of each number, which is important because the final answer needs to be in the same **relative order** as in the original list.

  Example:
  If `nums = [5, 3, 8, 2]`, it becomes:
  `[(0, 5), (1, 3), (2, 8), (3, 2)]`

  ***

  2. **Select the top `k` largest elements (by value):**

  - Sort the list of `(index, value)` pairs by the **value part in descending order**.
  - Take the first `k` elements from this sorted list. These are the `k` largest numbers from the original array.

  Example (with `k = 2`):
  `[(2, 8), (0, 5)]` ← top 2 highest values.

  ***

  3. **Restore the original order of selected elements:**

  - Sort the selected `k` elements again, **but this time by their original index**.
  - This ensures the final output respects the order in which these elements originally appeared in the array.

- **Alternative Approach:**

  - The above method is efficient, but can be slightly optimized by using a **max-heap** to directly extract the `k` largest elements without sorting the entire array.

- **Algorithm Used:**
  - **[[Greedy]]**
  - **[[Sorting]]**

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(ind, num) for ind, num in enumerate(nums)]

        nums = sorted(nums, key=lambda x: -x[1])[:k]

        nums = sorted(nums)

        return [num[1] for num in nums]
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) for sorting, where n is the length of `nums`.
- **Space:** O(n) for storing the pairs of indices and values.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The problem is not about subsequences in the traditional sense, but rather about selecting the largest elements while maintaining their original order.
- 💡 What made this problem tricky?
  - The challenge was recognizing that it could be solved with a greedy approach rather than a brute-force subsequence generation.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems that ask for the largest or smallest elements in a list, especially when order matters. This often indicates a greedy or sorting solution.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[215 Kth Largest Element in an Array]]
- [[1005 Maximize Sum Of Array After K Negations]]
- [[1356 Sort Integers by The Number of 1 Bits]]
- [[2163 Minimum Difference in Sums After Removal of Elements]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `33`  |
| Total Problems Solved | `366` |
| Confidence Today      | 😃    |
