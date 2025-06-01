## 🧠 Solving LeetCode Until I Become Top 1% — Day `6`

### 🔹 Problem: [2929. Distribute Candies Among Children II](https://leetcode.com/problems/distribute-candies-among-children-ii/description/?envType=daily-question&envId=2025-06-01)

**Difficulty:** #Medium
**Tags:** #Math #Combinatorics

---

### 📝 Problem Summary

> Finding The number of ways to distribute `n` candies among `3` children such that each child gets 0 or more candies, and the limit is given by `limit` candies for each child.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _It's a very straight forward combinatorial problem. I'm not that good at combinatorics, But I think if I try hard enough I can figure out `How to find the combinations of distributing candies among children`._

- **Optimized Strategy:**
  _Well, I learned something new today, and thare is a formula to find the combinations of non-negative integer solutions to the equation `x1 + x2 + x3 + ... + xk = n`, which is called [[stars and bars]] theorem. The formula is: `comb(n + k - 1, k - 1)`, where `n` is the total number of items to distribute, and `k` is the number of groups (children in this case)._

  **Core Idea**

  - _We can use this formula to find the number of ways to distribute `n` candies among `3` children, where each child can get `0` or more candies._
  - _But we also have a limit on the number of candies each child can get. So, what we can do is to find the number of ways to distribute `n` candies among `3` children without any limit, and then subtract the number of ways to distribute `n` candies among `3` children with the limit._

- **Solution Steps:**

  - These explanations are Taken from CHAT GPT because I'm not qualified enough to explain these problem steps in a help full way.

  🧠 Key Idea

  This is a **bounded integer partition** problem — we need to count how many ways we can split `n` candies into 3 non-negative integers `a + b + c = n` such that `a <= limit`, `b <= limit`, and `c <= limit`.

  ***

  💡 Total Unrestricted Ways

  First, count how many ways there are to distribute `n` candies to 3 children **without any restriction**. This is a classical "stars and bars" problem:

  - We treat the problem as placing 2 dividers between `n` candies.
  - The number of such distributions is:
    `C(n + 2, 2)`
    This means choosing 2 places from `n + 2` positions.

  ***

  ❌ Remove Invalid Distributions Using Inclusion-Exclusion

  Now subtract the number of **invalid** distributions — those where **at least one child gets more than `limit`**.

  **Step 1**: Subtract 1 Child Exceeding Limit

  - Pick one child to receive `limit + 1` candies.
  - Now distribute the remaining `n - (limit + 1)` candies among 3 children.
  - There are 3 ways to choose that child.
  - Count of such cases:
    `3 * C(n - (limit + 1) + 2, 2)`

  **Step 2**: Add Back 2 Children Exceeding Limit

  - Two children received `limit + 1` candies each.
  - Remaining candies: `n - 2 * (limit + 1)`
  - 3 ways to choose any 2 of the 3 children.
  - Count:
    `3 * C(n - 2 * (limit + 1) + 2, 2)`

  **Step 3**: Subtract 3 Children Exceeding Limit

  - All three children got `limit + 1` candies.
  - Remaining candies: `n - 3 * (limit + 1)`
  - Count:
    `C(n - 3 * (limit + 1) + 2, 2)`

  ***

  ✅ Final Answer

  Combine everything:

  ```
  C(n + 2, 2)
  - 3 * C(n - (limit + 1) + 2, 2)
  + 3 * C(n - 2 * (limit + 1) + 2, 2)
  - C(n - 3 * (limit + 1) + 2, 2)
  ```

  If any of the combinations have a negative top value (like `C(-1, 2)`), treat them as 0.

---

### 🚀 Why It Works

This is the classic **inclusion-exclusion principle**:

1. Subtract cases where at least one child breaks the rule.
2. Add back cases that were subtracted multiple times.
3. Subtract over-corrected overlaps.

### ⚙️ Code Implementation (Python)

```python
def cal(x):
    if x < 0:
        return 0
    return x * (x - 1) // 2


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        return (
            cal(n + 2)
            - 3 * cal(n - limit + 1)
            + 3 * cal(n - (limit + 1) * 2 + 2)
            - cal(n - 3 * (limit + 1) + 2)
        )
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(1)
- **Space:** O(1)

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The **stars and bars** theorem for counting combinations of distributing items.
- 💡 What made this problem tricky?
  - Understanding how to apply the inclusion-exclusion principle to bounded integer partitions.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems involving distributing items with constraints, especially when limits are involved.

---

### 🔁 Reflection (Self-Check)

- [😊] Could I solve this without help?
- [🫠] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [Similar Problem 1](#)
- [Similar Problem 2](#)

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `6`   |
| Total Problems Solved | `341` |
| Confidence Today      | 😃    |
