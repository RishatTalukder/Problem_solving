# 📘 Note: Top-Down Dynamic Programming (Memoization)

### 🔍 What is Top-Down DP?

Top-Down DP (also called **Memoization**) is a recursive problem-solving technique where you solve the **big problem by recursively solving subproblems** and **store their results** to avoid recomputation.

Think of it like this:

> "Ask the function what the answer is. If it already knows it, great. If not, break the problem down and ask again — but remember what you learned."

---

### 🛠️ How it works:

1. **Define the recursive state**
   Identify the function signature, i.e., what parameters define your subproblem.
   Example: `dp(i, k)` = max value from index `i` with `k` choices left.

2. **Base cases**
   Clearly define when recursion should stop.
   E.g., if `k == 0` or `i == n`, return 0.

3. **Recursive logic**
   Make the choice(s): either pick something or skip it (classic 0/1 Knapsack style).
   Compute both results, take the best one.

4. **Memoize**
   Store the result of each state in a dictionary or with `@lru_cache` so it's only computed once.

---

### ✅ Pros

* Intuitive to write (just think recursively).
* Easy to debug.
* Good when only a few states are visited among many.

---

### ❌ Cons

* May lead to recursion depth issues for large inputs.
* Slightly slower than bottom-up in tight constraints due to call stack overhead.

---

### 📦 Python Example: Fibonacci (Classic)

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Or with manual memoization:

```python
memo = {}
def fib(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
```

---

### 🧠 Tips

* **Use tuples** as dictionary keys if multiple parameters define a state.
* Use `@lru_cache(None)` for fast prototyping.
* If getting TLEs, try switching to **Bottom-Up DP**.

---

### 🪄 When to Use Top-Down

* Problem breaks down into overlapping subproblems.
* You're comfortable with recursion.
* You want clean and readable logic for complex state spaces.
