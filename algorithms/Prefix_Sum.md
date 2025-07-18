# 🧠 Prefix Sum (Cumulative Sum)

### 🔹 What Is It?

**Prefix Sum** is a simple and powerful technique to quickly calculate the **sum of elements in a subarray**.

It converts a brute-force O(n) subarray sum into **O(1)** using precomputed values.

---

### 📦 Basic Idea

Given an array `arr = [a₀, a₁, a₂, ..., aₙ]`, we create a new array `prefix` such that:

```
prefix[i] = a₀ + a₁ + ... + aᵢ
```

Once this is built, we can compute any subarray sum `arr[l..r]` as:

```
prefix[r] - prefix[l - 1]
```

If `l = 0`, then it's simply `prefix[r]`.

---

### 🔧 When to Use It?

Use Prefix Sum when:

- You're repeatedly querying the sum of elements in a range.
- You're dealing with frequency counts or histogram analysis.
- You want to optimize time from O(n) to O(1) per query.

Common in:

- Range sum queries
- Sliding window problems
- Binary search with cumulative constraints
- Subarrays satisfying certain conditions

---

### ⚙️ Python Template

```python
def build_prefix_sum(arr):
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]

    for i in range(1, n):
        prefix[i] = prefix[i - 1] + arr[i]

    return prefix

def range_sum(prefix, l, r):
    return prefix[r] if l == 0 else prefix[r] - prefix[l - 1]
```

---

### 📌 Example

```python
arr = [2, 4, 6, 1, 3]
prefix = [2, 6, 12, 13, 16]

To get sum of arr[1..3] → 4 + 6 + 1 = 11
=> prefix[3] - prefix[0] = 13 - 2 = 11
```

---

### ⏱️ Time & Space Complexity

| Operation     | Time | Space |
| ------------- | ---- | ----- |
| Build Prefix  | O(n) | O(n)  |
| Query (range) | O(1) | -     |

---

### 🧩 Variations

- **2D Prefix Sum** (for matrix subregions)
- **Prefix XOR**, **Prefix Max/Min**
- **Difference Array** (reverse of prefix sum; used for range updates)

---

### 🧠 Intuition Tip

If you keep asking “What’s the total between two points?” and you’re recalculating it every time,

> **Prefix Sum is your go-to optimization.**
