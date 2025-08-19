## 🧠 Solving LeetCode Until I Become Top 1% — Day `62`

### 🔹 Problem: [2348. Number of Zero-Filled Subarrays](https://leetcode.com/problems/number-of-zero-filled-subarrays/description/?envType=daily-question&envId=2025-08-19)

**Difficulty:** #Medium
**Tags:** #Array, #Math, #SlidingWindow

---

### 📝 Problem Summary

> Find how many subarrays in a given array consist entirely of zeros.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _I didn't try a brute force solution, as it would be inefficient for larger arrays. It straightforwardly looks like a math problem where we can count the number of zero-filled subarrays._

- **Optimized Strategy:**
  _The strategy is pretty simple: iterate through the array, count consecutive zeros, and use the formula for the total number of subarrays to calculate the result._

  - If we have `k` consecutive zeros, the number of zero-filled subarrays is given by the formula:
    \[\text{Total Zero-Filled Subarrays} = \frac{k(k + 1)}{2}\]
  - This is derived from the fact that for each zero, we can form a subarray that starts at that zero and ends at any subsequent zero, including itself.

- **Algorithm Used:**
  [[Sliding_Window]] [[Total_Subarray_Count]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def total_subs(self,n):
        return (n * (n + 1)) // 2

    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for num in nums:
            if num == 0:
                count += 1
            else:
                total += self.total_subs(count)
                count = 0
        total += self.total_subs(count)

        return total
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) -> where `n` is the length of the input array `nums`. We traverse the array once.
- **Space:** O(...) -> O(1) since we are using a constant amount of space for variables `count` and `total`.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  _The formula for counting subarrays is very useful, especially in problems involving consecutive elements._
- 💡 What made this problem tricky?
  _Me, I made it tricky by overthinking it. The problem is straightforward once you realize it's about counting consecutive zeros._
- 💭 How will I recognize a similar problem in the future?
  _Look for patterns in the input, especially when dealing with arrays of zeros or ones. The counting technique can often be applied._

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[413 Arithmetic Slices]]
- [[2110 Number of Smooth Descent Periods of a Stock]]
- [[2414 Length of the Longest Alphabetical Continuous Substring]]
- [[2526 Find Consecutive Integers from a Data Stream]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `62`   |
| Total Problems Solved | `423`  |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
