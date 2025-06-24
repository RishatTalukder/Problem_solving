# 📍 1. Two Sum

* 💡 Difficulty: Easy
* 🧩 Tags: #HashMap #Array #OnePass
* 🔄 Pattern: Hashing for Complements
* 🔍 Link: [LeetCode Link](https://leetcode.com/problems/two-sum/)

---

## 🧠 Problem Summary

You are given an array of integers `nums` and an integer `target`.
Return the indices of the two numbers in `nums` such that they **add up to `target`**.
You may assume each input has **exactly one solution**, and you **may not use the same element twice**.

---

## 🚫 Brute Force Approach

* Try all pairs of elements `(i, j)` and check if `nums[i] + nums[j] == target`.
* Time complexity: O(n²) — too slow for large inputs.
* Space complexity: O(1)

---

## ✅ Optimal Solution

### Strategy:

Use a **hash map** to store the complement of each number (i.e., `target - num`) while iterating.
If we ever see a number that already exists in the map, we found our answer.

### Steps:

1. Initialize an empty hash map (`hash`).
2. Loop through the array with `enumerate` to get index `i` and value `n`.
3. If `n` exists in the hash map, it means `target - n` was already seen — return `[i, hash[n]]`.
4. Otherwise, store `target - n` as a key and the index `i` as its value.

---

## 📦 Code (Python)

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i, n in enumerate(nums):
            if n in hash:
                return [i, hash[n]]
            else:
                hash[target - n] = i
```

---

## 📊 Complexity

* **Time:** O(n) — We visit each element once.
* **Space:** O(n) — In the worst case, we store all elements in the hash map.

---

## 📝 Notes

* ✅ This is a classic **complement pattern** using a hash map.
* ⚠️ Don’t confuse which value to store in the hash — store the **complement**, not the current number.
* 💭 Very common in interviews — memorize this technique and recognize similar problems involving pairs.
