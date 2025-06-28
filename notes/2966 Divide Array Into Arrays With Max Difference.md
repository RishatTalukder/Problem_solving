## 🧠 Solving LeetCode Until I Become Top 1% — Day `23`

### 🔹 Problem: [2966. Divide Array Into Arrays With Max Difference](https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/?envType=daily-question&envId=2025-06-18)

**Difficulty:** #Medium
**Tags:** #Sorting, #Greedy

---

### 📝 Problem Summary

> Given an array of integers `nums`, divide it into arrays of size 3 such that the maximum difference between the the elements in each array is at most `k`. Return an array of these arrays, or an empty array if it's not possible to divide the array as required.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _The problem statement was a little confusing at first, but I realized it was about grouping numbers into sets of 3 with a maximum difference constraint._
- **Optimized Strategy:**
  Use **sorting + greedy**:

  1. Sort the array to group similar numbers together.

  2. Since groups of 3 are needed, scan in chunks of 3.

  3. For each triplet: if `max - min <= k`, it's valid.

  4. If any triplet violates the rule, return an empty list immediately.

- **Algorithm Used**:
  [[Sorting]] [[Greedy]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range(0,len(nums),3):
            if nums[i+2] -nums[i] <= k:
                res.append(nums[i:i+3])

            else:
                return []


        return res
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) for sorting, O(n) for the loop, so overall O(n log n).
- **Space:** O(n) for the result list, but O(1) additional space if we ignore the output.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  Sorting helps in grouping similar numbers, making it easier to check the max difference.
- 💡 What made this problem tricky?
  The initial confusion about the grouping and the maximum difference constraint.
- 💭 How will I recognize a similar problem in the future?
  Look for problems that require grouping or partitioning with constraints, especially those involving differences or ranges.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `23`  |
| Total Problems Solved | `344` |
| Confidence Today      | 😃    |
