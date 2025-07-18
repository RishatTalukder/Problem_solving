# 📍238. Product of Array Except Self

* 💡 Difficulty: #Medium
* 🧩 Tags: #Array #PrefixProduct #SpaceOptimization
* 🔄 Pattern: Prefix + Suffix Products
* 🔍 Link: [LeetCode Link](https://leetcode.com/problems/product-of-array-except-self)

---

## 🧠 Problem Summary

You are given an integer array `nums` of length `n`.
Return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

**Constraints:**

* Do **not** use division.
* Solve it in `O(n)` time.
* The solution should use **O(1)** extra space (excluding the output array).

---

## 🚫 Brute Force Approach

We can iterate over each index `i` and compute the product of all elements except `i` using nested loops.

```python
# Brute force approach
res = []
for i in range(len(nums)):
    prod = 1
    for j in range(len(nums)):
        if i != j:
            prod *= nums[j]
    res.append(prod)
```

### ❌ Time: O(n²)

### ❌ Space: O(n)

**Why it's bad:** Too slow for large arrays due to nested loops.

---

## ✅ Optimal Solution

### 💡 Idea:

We calculate **prefix** and **suffix** products in two passes:

* First pass (left to right): Store product of elements *before* index `i` in `res[i]`
* Second pass (right to left): Multiply existing `res[i]` with product of elements *after* index `i`

This avoids using division and respects the space/time constraints.

---

## 📦 Code (Python)

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = post = 1
        n = len(nums)
        res = [0] * n

        # First pass: prefix products
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        # Second pass: suffix products
        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]

        return res
```

---

## 📊 Complexity

* **Time:** O(n) — Two linear passes.
* **Space:** O(1) — Output array `res` doesn't count as extra space.

---

## 📝 Notes

* ⚠️ Division is disallowed, so we compute products without it using prefix/suffix trick.
* ✅ Very common and elegant space optimization technique used in many array problems.
* 💡 Key Insight: `res[i] = product of all elements before i * product of all elements after i`.
