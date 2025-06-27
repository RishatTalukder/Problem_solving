# 📘 Recursion

---

### 🔍 What Is It?

**Recursion** is a programming technique where a function calls **itself** directly or indirectly to solve a smaller instance of the same problem.

> A recursive function continues to call itself with **simpler inputs** until it reaches a **base case**.

---

### 🧠 Core Concepts

1. **Base Case**:
   The condition where the recursion stops. Without it, you get infinite recursion → stack overflow.

2. **Recursive Case**:
   The function calls itself with a modified input to gradually approach the base case.

---

### 🛠 Example

**Factorial (n!)**

```python
def factorial(n):
    if n == 0:        # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call
```

---

### 📌 Real-Life Analogy

Imagine a row of people where each one passes a message to the person in front until it reaches the front of the line — then the answer propagates back. This is **call → base → return**.

---

### 📦 Applications

| Domain              | Example Problems                             |
| ------------------- | -------------------------------------------- |
| Mathematics         | Factorial, Fibonacci, GCD, Power             |
| Data Structures     | Tree Traversals, Graph Traversals (DFS)      |
| Backtracking        | Sudoku, N-Queens, Permutations, Combinations |
| Divide & Conquer    | Merge Sort, Quick Sort, Binary Search        |
| Dynamic Programming | Memoization-based DP problems                |

---

### 📊 Time & Space Complexity

- **Time**: Depends on the number of function calls and work per call.
- **Space**: Uses **call stack**. Depth of recursion = stack space used.

> Use **memoization** or **DP** to avoid recalculating overlapping subproblems.

---

### ⚠️ Common Mistakes

- Forgetting the base case → infinite recursion.
- Using mutable values (like lists or dicts) incorrectly in recursive calls.
- Assuming each recursive call runs in parallel (they don’t unless using async/threading).
- Exceeding Python’s default recursion limit (`sys.setrecursionlimit()` can change it, but be cautious).

---

### 💡 When to Use Recursion

- When a problem can be **divided into similar smaller subproblems**.
- Natural fit for **tree**, **graph**, or **backtracking** problems.
- When the problem’s recurrence is obvious or inherently recursive.

---

### ✅ Summary

| Pros                                   | Cons                                    |
| -------------------------------------- | --------------------------------------- |
| Clean, elegant code for some problems  | Can be inefficient (repetitive work)    |
| Matches natural problem structure      | Risk of stack overflow                  |
| Essential for DFS, Trees, Backtracking | Hard to debug if not carefully designed |

---

### 📝 Quick Tip

> Always write the **base case first**, then figure out how to move toward it recursively.
