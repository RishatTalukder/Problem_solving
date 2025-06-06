# ⚡ Greedy Algorithm – A Quick Note

### 🔍 What is a Greedy Algorithm?

A **Greedy Algorithm** is a problem-solving technique that makes the **locally optimal choice** at each step with the hope that these choices will lead to a **globally optimal solution**.

In simpler terms:

> **"Pick the best-looking option right now and hope it works out."**

---

### 🧠 Key Characteristics

* **Greedy Choice Property**: A global optimal solution can be arrived at by choosing local optima.
* **No Backtracking**: Once a decision is made, it is never reversed.
* **No DP Table**: Greedy doesn’t use memoization or previous computations.
* **Efficient**: Often faster than dynamic programming due to less overhead.

---

### 🧩 Common Use Cases

| Problem Type                         | Example Problems                            |
| ------------------------------------ | ------------------------------------------- |
| **Activity/Interval Scheduling**     | Job Scheduling, Meeting Rooms               |
| **Minimum Spanning Tree**            | Kruskal's and Prim’s Algorithm              |
| **Shortest Path in Graph**           | Dijkstra’s Algorithm                        |
| **Huffman Encoding**                 | Greedy Tree Construction                    |
| **Change-making**                    | Minimum coins needed (with specific limits) |
| **Greedy Stack/String Construction** | Lexicographically smallest string problems  |
| **Greedy Sorting**                   | Pancake Sorting, Candy Distribution         |

---

### 🧪 Classic Example: Coin Change (Greedy)

Given coin denominations `[1, 5, 10]` and amount = `17`,
Greedy picks the largest possible coin each time:

* Pick 10 → remaining = 7
* Pick 5 → remaining = 2
* Pick 1 × 2 → remaining = 0
  Total = 4 coins.

⚠️ **Note**: This greedy method only works if the coin system is **canonical** (like in most currencies). For arbitrary denominations, DP may be needed.

---

### ✅ When Does Greedy Work?

Greedy works if:

1. **Greedy-choice property** holds (local optimum leads to global).
2. **Optimal substructure** exists (problem can be broken into subproblems).

Otherwise, you may need **Dynamic Programming** instead.

---

### 🧠 Tips to Design Greedy Solutions

* Try to **sort** based on a greedy parameter.
* Always ask: *If I pick the best now, will it affect future decisions?*
* Simulate small examples and check if greedy always gives correct results.
* Compare with brute-force/DP for correctness.

---

### 🔧 Basic Greedy Template (if using sorted data):

```python
arr.sort()  # Optional
result = 0

for item in arr:
    if <greedy condition>:
        result += <value or count>
    else:
        break

return result
```

---
