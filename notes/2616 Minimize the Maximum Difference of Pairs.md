## 🧠 Solving LeetCode Until I Become Top 1% — Day `X`

### 🔹 Problem: [2616. Minimize the Maximum Difference of Pairs](https://leetcode.com/problems/minimize-the-maximum-difference-of-pairs/description/?envType=daily-question&envId=2025-06-13)

**Difficulty:** #Medium
**Tags:** #BinarySearch #Greedy #Sorting

---

### 📝 Problem Summary _(in your own words)_

> Given an array of integers `nums` and an integer `p`, the task is to find the minimum possible maximum difference between pairs of elements in `nums` after forming `p` pairs. Each pair consists of two elements, and the difference is calculated as the absolute difference between the two elements in the pair. The goal is to minimize the maximum difference across all pairs.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _It wasn't clear at first, but I thought of sorting the array and then trying to form pairs with the smallest difference. However, this approach would not guarantee the minimum maximum difference, This approach has too many edge cases like what if the array is the size of 6 and the number of pairs is 3, then we can form pairs with the smallest difference but the maximum difference will be larger than if we formed pairs with the largest difference. After some thought it felt like a greedy problem and after some more thought I realised It could be solved using binary search on the maximum difference but I'll be honest, I didn't know how to implement it at first._

- **Optimized Strategy:**
  _To solve this problem we can use the greedy binary search approach. It's a common technique for problems that involve minimizing or maximizing a value under certain constraints._

  - **Steps to Solve:**

  1. **Sort the Array:** Start by sorting the input array `nums`. This allows us to easily find pairs with minimal differences.
  2. **Maximum Difference can be** the difference between the largest and smallest elements in the array.
  3. **Minimum Difference will be** 0, which is the case when all elements are the same.
  4. We take two pointers, one is `high(max_diff)` and the other is `low(min_diff)`, and we will use binary search to find the minimum maximum difference.
  5. **Binary Search:**
     - While `low` is less than or equal to `high`, calculate the mid-point as `(low + high) // 2`.
     - Check if it is possible to form `p` pairs with a maximum difference of `mid`.
     - If it is possible, update `result` to `mid` and move `high` to `mid - 1`.
     - If it is not possible, move `low` to `mid + 1`.
  6. **Check Feasibility of Pairs:**
     - To check if we can form `p` pairs with a maximum difference of `mid`, iterate through the sorted array and count how many pairs can be formed.
     - If the difference between the current element and the next element is less than or equal to `mid`, form a pair and skip the next element.
     - Continue until either all elements are processed or `p` pairs are formed.

- **Algorithm Used:**
  [[Binary_Search]] [[Sorting]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        result = high

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip the next element as it's paired
                else:
                    i += 1  # Move to the next element
            return count >= p

        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n)
  - Sorting the array takes O(n log n).
  - The binary search runs in O(log(max_diff)), where max_diff is the difference between the largest and smallest elements.
  - The feasibility check runs in O(n) for each binary search iteration, leading to an overall complexity of O(n log n).
- **Space:** O(1)
  - The algorithm uses a constant amount of space for variables and does not require additional data structures that scale with input size.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The `greedy binary search` is a powerful algorithmic pattern for problems involving minimizing or maximizing a value under constraints.
- 💡 What made this problem tricky?
  - The challenge was to efficiently determine if `p` pairs could be formed with a given maximum difference, which required careful handling of the sorted array and the binary search logic.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems that involve minimizing or maximizing a value under constraints.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [❌] Did I write code from scratch?
- [😊] Did I understand why it works?
- [🫠] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[1200 minimum Absolute Difference]]
- [[1509 Minimum Difference Between Largest and Smallest Value in Three Moves]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `18`  |
| Total Problems Solved | `350` |
| Confidence Today      | 😃    |
