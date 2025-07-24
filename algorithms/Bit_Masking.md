# 🧠 Bitmasking

### 🔹 What Is Bitmasking?

**Bitmasking** is a technique that uses the **binary representation of integers** (bits) to efficiently store and manipulate **subsets, states, or boolean flags** using bitwise operations.

Instead of using arrays or sets, we represent presence/absence with bits:

- `1` means **present/true**
- `0` means **absent/false**

---

### 📦 Where Is It Used?

- Representing **subsets** of a small set (usually ≤ 20 elements)
- **DP on subsets** (e.g. Traveling Salesman, Set Cover)
- Efficient **state compression**
- **Game state encoding**
- Checking **parity**, **on/off toggles**
- Solving **constraint satisfaction problems** (e.g. Sudoku, N-Queens)

---

### 🔧 Basic Bitwise Operations

| Operation              | Description                   | Python Expression        |        |              |
| ---------------------- | ----------------------------- | ------------------------ | ------ | ------------ |
| `x & (1 << i)`         | Check if the `i`-th bit is ON | `bool(mask & (1 << i))`  |        |              |
| \`mask                 | (1 << i)\`                    | Turn ON the `i`-th bit   | \`mask | = (1 << i)\` |
| `mask & ~(1 << i)`     | Turn OFF the `i`-th bit       | `mask &= ~(1 << i)`      |        |              |
| `mask ^ (1 << i)`      | Toggle the `i`-th bit         | `mask ^= (1 << i)`       |        |              |
| `bin(mask).count("1")` | Count number of ON bits       | (useful for subset size) |        |              |

---

### 🧩 Example: Subsets with Bitmask

```python
n = 3  # number of elements
for mask in range(1 << n):  # loop through all 2^n subsets
    subset = []
    for i in range(n):
        if mask & (1 << i):
            subset.append(i)
    print(f"Mask {bin(mask)} → Subset: {subset}")
```

---

### 🔐 Intuition Tip

Bitmask is just a clever way of saying:

> "I’ll use a single integer’s binary form to keep track of which things are on/off."

For example:

- `10101` → means positions 0, 2, and 4 are ON.

---

### 💡 Real World Analogy

Think of a **bitmask as a row of switches** (light switches or power toggles). You can flip, check, or set them using **bitwise tools** instead of many if-else conditions.

---

### ⏱️ Time & Space

Efficient if:

- Total states = `2^n` (where `n <= 20`)
- Bit operations are **O(1)** per use

---

### 🧠 Patterns & Problems

- Subset enumeration (`1 << n`)
- DP with `dp[mask]`
- Graphs with visited nodes as masks
- Minimum cost Hamiltonian paths
- Set cover, Scheduling, Puzzle games

---

### 🧪 Bonus: Check if One Bit is Set (Power of Two)

```python
def is_power_of_two(x):
    return x and (x & (x - 1)) == 0
```
