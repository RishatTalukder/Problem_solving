## 🧠 Solving LeetCode Until I Become Top 1% — Day `14`

### 🔹 Problem: [440 K-th Smallest in Lexicographical Order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/?envType=daily-question&envId=2025-06-09)

**Difficulty:** #Hard
**Tags:** #BinarySearch #Lexicographical #Math #Trie

---

### 📝 Problem Summary

> Finding the k-th smallest number in lexicographical order from `1` to `n`. The numbers are treated as strings for comparison.

---n

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This is a problem that I had tp think a lot about, there are some interesting ways to solve it. I solved this a long time ago, But i still remember the horror of it. The statement told me to return the k-th smallest number in lexicographical order from `1` to `n` and instantly I thought of generating all numbers from `1` to `n` and sorting them in string order and return the `k-1` index. But I had a `memory limit exceeded` error. So I had to think of a better way to solve it but I didn't know there was a data structure called `Trie` that could solve this problem. So, i learned `Trie` and tried to implement it, but alas! I was too dumb to think I can solve a problem that is using a advanced data structure like `Trie`. So. I thought let's see the solution and I was like "What!! this is a search problem and we can get mathematical with it". What is happening I hate `lexicographical` problems(yes, this was my first lexicographical problem)._

- **Optimized Strategy:**
  _The problem can be solved Using the `trie` data structure, which is pretty straightforward. I will heavily recommand trying it yourself. But i will explain the mathematical way to solve it because we can skip the overhead of creating a `trie` and just use some mathematical properties of numbers._

  Absolutely! Let’s break down the **intuition** behind this solution to **LeetCode 440: K-th Smallest in Lexicographical Order**, without diving into code—just the **concept** as if you're **teaching it to someone in plain terms**.

  ### 🧭 Intuition

  Think of lexicographical numbers as a **prefix tree (trie)**:

  - The root of the tree starts from 1 to 9 (just like dictionary words start with 'a' to 'z').
  - From each number, you can **go deeper by adding digits**, like:

  - From 1 → 10 → 100 → 1000...
  - From 2 → 20 → 200 → 2000...
  - You can also **move sideways** to the next number: from 1 to 2, from 2 to 3, and so on.

  Now, what we want to do is simulate this **navigation of the tree** to reach the `k-th` number in lex order.

  ***

  ### 🔍 So, how do we do it?

  Let’s say you’re standing at the number `1`. Now you want to decide:

  > Should I go deeper into `1`, like `10`, `100`, etc. or skip to the next number, `2`?

  To make this decision, we calculate:

  **"How many numbers exist under this prefix?"**
  That is, how many numbers start with `1`?

  - If the count is **less than or equal to `k`**, then that means the k-th number is **not here**, so we **skip this whole subtree** and move to `2`, `3`, etc.
  - If the count is **greater than `k`**, then the number we want **must lie inside this subtree**, so we go **deeper into it**, e.g., from `1` to `10`.

  This way, we can **efficiently skip whole sections** of the lex order without generating them.

  ***

  ### 🔢 A Visual Analogy

  Imagine lexicographical order from 1 to 20:

  ```
  1
  10
  11
  12
  13
  14
  15
  16
  17
  18
  19
  2
  20
  3
  4
  ...
  ```

  If you’re at `1`, the numbers starting with `1` are: 1, 10–19 = 11 numbers.
  If `k = 13`, then:

  - You’ll skip the whole subtree of `1` (which has 11 numbers) if `k > 11`.
  - Otherwise, you go deeper into `1` → `10`, then `100`, etc.

  ***

  ### 📚 Summary

  - We treat the numbers like a **dictionary trie**.
  - We **count how many numbers** lie under each "prefix" like `1`, `2`, `10`, `11` using math, not actual generation.
  - If `k` is bigger than that count, **skip to next sibling**.
  - If `k` is smaller, **go deeper into children**.
  - Repeat until `k` steps are made.

- **Algorithm Used:**
  [[Binary_Search]] [[prefix_tree_trie]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        curr = 1
        k -= 1

        def get_steps(n, pre1, pre2):
            steps = 0

            while pre1 <=n:
                steps += min(n+1, pre2)-pre1
                pre1 *= 10
                pre2 *= 10

            return steps


        while k:
            steps = get_steps(n, curr, curr+1)

            if steps <= k:
                curr += 1
                k -= steps

            else:
                curr *= 10
                k-=1


        return curr
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(log n \* log n)
  - The logarithmic factor comes from the number of digits in `n` and the way we traverse the tree-like structure.
  - Each step involves counting numbers under a prefix, which is logarithmic in nature.
- **Space:** O(1)
  - We are using a constant amount of space for variables, not storing any large data structures.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - I learned how to navigate a lexicographical order using a mathematical approach rather than brute force, which is efficient and elegant.
- 💡 What made this problem tricky?
  - Implementing the logic of counting numbers under a prefix without generating them was challenging.
- 💭 How will I recognize a similar problem in the future?
  - Lexicographical problems.

---

### 🔁 Reflection (Self-Check)

- [🫠] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [😐] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[2376 Count Special Integers]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `14`  |
| Total Problems Solved | `347` |
| Confidence Today      | 😃    |
