## 🧠 Solving LeetCode Until I Become Top 1% — Day `17`

### 🔹 Problem: [3423 Maximum Difference Between Adjacent Elements in a Circular Array](https://leetcode.com/problems/maximum-difference-between-adjacent-elements-in-a-circular-array/description/?envType=daily-question&envId=2025-06-12)

**Difficulty:** #Easy
**Tags:** #Array

---

### 📝 Problem Summary _(in your own words)_

> Given a circular array, find the maximum absolute difference between adjacent elements. The array wraps around, meaning the last element is adjacent to the first.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _Well finally a problem that I can solve without looking at the solution and cofirming that I am on the right track. The problem has a word "circular" in it and don't get confused by it. You can think that it might be a linked list or something, but it's just a normal array. Just the first and last elements are adjacent to each other. So, we can just iterate through the array and find the maximum absolute difference between adjacent elements. You can either find the absolute difference between the first and last elements separately or just add it to the end of the array and iterate through it. I think both approaches are valid._

- **Optimized Strategy:**
  - **Step 1:** Add the first element to the end of the array to handle the circular nature.
  - **Step 2:** Initialize a variable `result` to store the maximum absolute difference.
  - **Step 3:** Iterate through the array and calculate the absolute difference between each adjacent pair of elements.
  - **Step 4:** Update `result` if the current absolute difference is greater than the previous maximum.
- **Step 5:** Return the `result` as the final answer.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        nums.append(nums[0])
        res = float('-inf')
        for i in range(1,len(nums)):
            res = max(res, abs(nums[i]-nums[i-1]))

        return res
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We iterate through the array once to calculate the maximum absolute difference.
- **Space:** O(1)
  - We use a constant amount of space for the `result` variable and do not use any additional data structures that scale with input size.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - Nothing new.
- 💡 What made this problem tricky?
  - For beginners the word "circular" might be confusing, but it's just a normal array with the first and last elements being adjacent.
- 💭 How will I recognize a similar problem in the future?
  - Look for the word "circular" in the problem statement.

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
| Day                   | `17`  |
| Total Problems Solved | `349` |
| Confidence Today      | 😃    |
