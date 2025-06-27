# 📘 Divide and Conquer

---

### 🔍 What Is It?

**Divide and Conquer** is a problem-solving technique that breaks a problem down into **smaller subproblems**, solves each recursively, and then **combines** their results to form a solution to the original problem.

---

### 🧠 Core Steps

1. **Divide**: Break the original problem into smaller subproblems.
2. **Conquer**: Recursively solve each subproblem.
3. **Combine**: Merge the results of the subproblems into the solution of the original.

> You keep splitting until you hit a **base case** that can be solved directly.

---

### 📌 Classic Examples

| Problem                         | Divide Part                                 | Combine Part                            |
| ------------------------------- | ------------------------------------------- | --------------------------------------- |
| Merge Sort                      | Split array in half                         | Merge sorted halves                     |
| Quick Sort                      | Partition array around pivot                | Combine left + pivot + right            |
| Binary Search                   | Check mid, search left or right half        | Base case returns result                |
| Karatsuba Multiplication        | Split numbers into parts                    | Combine using recursive multiplications |
| Maximum Subarray (Kadane's alt) | Divide by midpoint, max on left/right/cross | Take max of the three                   |

---

### 🧠 Why Use It?

- Solves complex problems by **breaking them down**.
- Naturally leads to **recursive** solutions.
- Enables **parallelism** in some cases.
- Very efficient when combined with **memoization** or **pruning**.

---

### 💡 When to Use It?

Use Divide and Conquer when:

- The problem can be **naturally split** into subproblems.
- Subproblems are **similar** to the original.
- The **solution can be built** by combining sub-results.
- You want to **optimize a brute-force** approach (e.g., avoid recalculating overlapping parts).

---

### ⚠️ Common Pitfalls

- Not handling base cases properly.
- Not combining sub-results correctly.
- Redundant recomputation → may require **memoization** or **DP**.
- Overusing it when iterative or greedy approaches are simpler.

---

### 📦 Time Complexity

If each problem of size `n` is divided into `a` subproblems of size `n/b` and combining takes `O(n^d)`, the total time is:

```
T(n) = a * T(n/b) + O(n^d)
```

Use the **Master Theorem** to solve such recurrences.

---

### ✅ Summary

| Pros                         | Cons                                |
| ---------------------------- | ----------------------------------- |
| Clean recursive logic        | Can be heavy on stack (deep calls)  |
| Can reduce time complexity   | Needs correct combine logic         |
| Makes brute force manageable | May not be optimal for all problems |

---

### 📝 Quick Tip

> **Always ask:** Can I split this problem into smaller parts of the same kind?

If yes, it's a great candidate for divide and conquer.
