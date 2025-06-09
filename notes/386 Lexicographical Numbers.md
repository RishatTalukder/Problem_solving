## 🧠 Solving LeetCode Until I Become Top 1% — Day `13`

### 🔹 Problem: [386 Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/description/?envType=daily-question&envId=2025-06-08)

**Difficulty:** #Medium
**Tags:** #Lexicographical #DFS

---

### 📝 Problem Summary

> Return a lexicographically sorted list of all integers from `1` to `n` in their string representation.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This problem is kinda a brute force problem. You can just generate all numbers from `1` to `n`, convert them to strings, and sort them. But that would be inefficient or you can think for iterating over the numbers and generating them in lexicographical order._

- **Optimized Strategy:**
  _I used the later bruteforce approach. Than I saw it's a iterative DFS solution (instead of recursion, I used a stack)._

  - Start iterating from `1` and append the current number to the result.
  - Now, check if the current number multiplied by `10` is less than or equal to `n`. If it is, set current number to `current * 10`.
  - If not, check if the current number plus `1` is less than or equal to `n`. If it is, increment the current number by `1`.
  - But there is a twist, if the current number plus `1` results in a number that has has a mode of `10` we can have same number again, so we need to backtrack before incrementing the current number.
  - So, check if the current number is divisible by `10` and if the mode is `9`. We will divide the current number by `10` to backtrack.

- **Algorithm Used:**
  [[iterative_dfs]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        curr = 1

        for i in range(n):
            res.append(curr)

            if curr*10 <= n:
                curr = curr*10

            else:
                while curr%10 == 9 or curr >= n:
                    curr = curr//10

                curr += 1

        return res
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We iterate through numbers from `1` to `n`, and each number is processed in constant time.
- **Space:** O(n)
  - The result list stores all numbers from `1` to `n`.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - _I learned how to generate numbers in lexicographical order using an iterative DFS approach._
- 💡 What made this problem tricky?
  - _The tricky part was figuring out the backtracking condition when the current number reaches a point where it can no longer be multiplied by `10`._
- 💭 How will I recognize a similar problem in the future?
  - _If I encounter a problem that requires generating numbers in a specific order, especially lexicographically, I can apply this iterative DFS approach._

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
| Day                   | `13`  |
| Total Problems Solved | `348` |
| Confidence Today      | 😃    |
