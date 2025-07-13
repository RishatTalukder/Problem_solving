## 🧠 Solving LeetCode Until I Become Top 1% — Day `29`

### 🔹 Problem: [2200. Find All K-Distant Indices in an Array](https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/)

**Difficulty:** Easy
**Tags:** #TwoPointers, #Simulation

---

### 📝 Problem Summary

> You're given an array `nums`, an integer `key`, and another integer `k`.
> Find all indices `i` such that there exists **at least one** index `j` where:
>
> - `nums[j] == key` and
> - `abs(i - j) <= k`
>
> Return the list of such indices in **increasing order**.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - For every index `i`, check every index `j` and see if `nums[j] == key` and `abs(i-j) <= k`.
  - Time Complexity: O(n²) — too slow for larger inputs. But you can submit this in leetcode.

- **Optimized Strategy:**

  - Iterate through the array and whenever we find `nums[i] == key`, we know that:

    - All indices from `i-k` to `i+k` are valid `k-distant indices`.
    - We use `max(right, i-k)` as the start so that we **don't add overlapping ranges twice**.
    - Update `right = min(n, i+k+1)` to track the farthest index added so far.

  - We directly `extend` the `ans` list with that range.

- **Algorithm Used:**

  [[Two_Pointer]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        n = len(nums)
        right = 0

        for i in range(n):
            if nums[i] == key:
                left = max(right, i-k)
                right = min(n, i+k+1)
                ans.extend(range(left, right))
        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n + m), where `n` is the length of `nums` and `m` is the number of indices added to `ans`
- **Space:** O(m), output list

---

### 🧩 Key Takeaways

- ✅ Learned how to **efficiently avoid overlap** when marking ranges.
- 💡 Using `right` as a moving pointer to prevent re-adding indices is a **smart greedy trick**.
- 💭 This type of range-based scanning is useful in **sliding window and interval problems**.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help? → Yes
- [x] Did I write code from scratch? → Yes
- [x] Did I understand why it works? → Yes
- [x] Will I be able to recall this in a week? → Definitely

---

### 📚 Related Problems

- [[1 Two Sum]]
- [[2817 Minimum Absolute Difference Between Elements With Constraint]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `29`  |
| Total Problems Solved | `362` |
| Confidence Today      | 😃    |
