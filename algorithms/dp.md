# 🧠 Dynamic Programming (DP)

### 🔹 What Is Dynamic Programming?

Dynamic Programming is an optimization technique used to **solve complex problems by breaking them down into simpler subproblems**, storing the results of subproblems to avoid redundant computation.

> 💡 **"Remember the past to avoid redoing it."**

---

### 🧩 When to Use DP

Ask yourself:

* Can the problem be **broken into subproblems**?
* Are the subproblems **overlapping**?
* Does the problem have **optimal substructure**?

If yes, it’s likely a DP problem.

---

### 🧱 Two Key Properties

1. **Overlapping Subproblems**

   * The same subproblem is solved multiple times (like Fibonacci).
2. **Optimal Substructure**

   * The solution to a problem can be constructed from solutions to subproblems.

---

### 🔧 Common DP Techniques

| Technique                  | Description                                                                          |
| -------------------------- | ------------------------------------------------------------------------------------ |
| **Memoization** (Top-Down) | Store results of recursive calls.                                                    |
| **Tabulation** (Bottom-Up) | Build the solution iteratively from base cases.                                      |
| **State Compression**      | Use less memory by compressing dimensions (often with bitmasking or rolling arrays). |

---

### 🛠️ Template Patterns

#### 1. **Top-Down (Memoization)**

```python
dp = {}

def f(i):
    if i in dp:
        return dp[i]
    if base_case:
        return result
    dp[i] = f(i-1) + f(i-2)  # Example logic
    return dp[i]
```

#### 2. **Bottom-Up (Tabulation)**

```python
dp = [0] * (n + 1)
dp[0] = base_0
dp[1] = base_1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i-2]  # Example logic
```

---

### 🔢 Classic DP Problems by Type

| Type               | Examples                                    |
| ------------------ | ------------------------------------------- |
| **1D DP**          | Fibonacci, Climbing Stairs                  |
| **2D DP**          | Knapsack, Edit Distance, Grid Paths         |
| **DP on Strings**  | LCS, Palindromic Substrings                 |
| **DP on Trees**    | Tree DP, House Robber III                   |
| **Bitmask DP**     | Traveling Salesman                          |
| **DP with States** | Stock Buy & Sell with K transactions        |
| **DP with Gap**    | Matrix Chain Multiplication, Burst Balloons |

---

### 🧠 Intuition Tip

Think of DP as **solving puzzles where smaller pieces can be reused.** You can’t afford to rebuild the same piece again and again — instead, save it and reuse it.

---

### ⚙️ Time & Space Complexity

| Approach  | Time Complexity                         | Space Complexity       |
| --------- | --------------------------------------- | ---------------------- |
| Top-Down  | Depends on number of unique subproblems | Stack + Memo Table     |
| Bottom-Up | Usually better for space, no recursion  | Table or Rolling Array |

---

### 🎯 How to Identify a DP Problem

* Are you asked to count or maximize/minimize something?
* Can you define the problem in terms of **choices and consequences**?
* Do brute force solutions repeat the same calculations?

---

### 🧩 Examples to Practice

* **Easy:** Climbing Stairs, Fibonacci, House Robber
* **Medium:** Coin Change, Unique Paths, Longest Palindromic Subsequence
* **Hard:** Edit Distance, Interleaving Strings, Burst Balloons

---

### 💡 Final Thoughts

* Start from **base cases** and build up.
* Clearly define the **state**, **transition**, and **goal**.
* Practice different dimensions (1D, 2D, DP with Strings, etc.).
* Try drawing the **state table or recursion tree**.
