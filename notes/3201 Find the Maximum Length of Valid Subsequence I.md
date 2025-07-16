## 🧠 Solving LeetCode Until I Become Top 1% — Day `45`

### 🔹 Problem: [3201. Find the Maximum Length of Valid Subsequence I](https://leetcode.com/problems/find-the-maximum-length-of-valid-subsequence-i/)

**Difficulty:** #Medium
**Tags:** #Array, #Greedy

---

### 📝 Problem Summary

You are given an array `nums`.
A subsequence is **valid** if all adjacent elements satisfy:
`(a + b) % 2 == constant` — i.e., all adjacent *pairwise sums* are either always even or always odd.
Return the length of the **longest valid subsequence**.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Try generating all possible subsequences and check if they meet the condition — obviously way too slow for `n <= 2*10^5`.

* **Optimized Strategy:**
  The condition `(a + b) % 2 == constant` means the subsequence must either:

  * Always have *same parity* (odd+odd or even+even)
  * Or alternate between even and odd (odd+even or even+odd)

  This means there are only **4 patterns** to check:

  * `[even, even, ...]`
  * `[odd, odd, ...]`
  * `[even, odd, even, ...]`
  * `[odd, even, odd, ...]`

  So, for each pattern, greedily scan the array and pick numbers that match the expected parity at that position.


---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        res = 0
        for pattern in [[0, 0], [0, 1], [1, 0], [1, 1]]:
            cnt = 0
            for num in nums:
                if num % 2 == pattern[cnt % 2]:
                    cnt += 1
            res = max(res, cnt)
        return res
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(4 \* n) → O(n)
* **Space:** O(1)

---

### 🧩 Key Takeaways

* ✅ Identifying the **parity pattern** reduces the problem from an unclear DP to a greedy solution.
* 💡 Only 4 valid parity sequences exist — just simulate them all.
* 💭 Sometimes, thinking in terms of **mod 2** simplifies problems more than trying to force DP.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? (almost!)
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[300 Longest Increasing Subsequence]]
* [[2915 Length of the Longest Subsequence That Sums to Target]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `45`    |
| Total Problems Solved | `386`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
