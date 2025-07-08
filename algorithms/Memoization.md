# 🧠 Note: Memoization in Dynamic Programming

### 🔍 What is Memoization?

**Memoization** is a technique used to **optimize recursive algorithms** by storing the results of expensive function calls and **reusing them when the same inputs occur again**.

Think of it as:

> “If I’ve already solved this subproblem once, why do it again?”

---

### 🧪 When to Use It

Use memoization when:

* Your problem has **overlapping subproblems**.
* You are using **recursion**.
* You want to avoid **redundant calculations**.

---

### ⚙️ How Memoization Works

1. Write the **recursive solution** for the problem.
2. Use a **cache** (dictionary or `@lru_cache`) to store results of subproblems.
3. Before solving a subproblem, **check the cache** first.
4. If the result exists, return it. Otherwise, **compute and save** it.

---

### 🧩 Classic Example: Fibonacci with Memoization

```python
# Manual dictionary-based memoization
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

Or, using Python’s built-in decorator:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

---

### 🟢 Benefits

* **Drastically reduces time complexity** by avoiding repeated work.
* Makes **recursive solutions feasible** for large input sizes.
* Often the **quickest way to convert brute-force to optimal**.

---

### 🔴 Cautions

* Can hit **recursion depth limits** on deep recursion (use `sys.setrecursionlimit()` or convert to bottom-up).
* Takes **extra memory** to store intermediate results.
* Only works when there are **repeated subproblems** — not all recursive problems benefit.

---

### 🧠 Real-World Problems Using Memoization

* Fibonacci numbers
* 0/1 Knapsack
* Longest Common Subsequence
* Edit Distance
* Partitioning problems

---

### 💡 Tips

* If your state depends on multiple variables, use a **tuple as a key** in your cache.
* If the number of unique states is small, memoization is often **faster to implement and easier to read** than bottom-up DP.
* Combine with **binary search**, **backtracking**, or **DFS** when needed — it’s very flexible.
