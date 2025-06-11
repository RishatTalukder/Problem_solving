# 🧠 Fenwick Tree (Binary Indexed Tree)

### 🔹 What Is It?

A **Fenwick Tree**, also known as a **Binary Indexed Tree (BIT)**, is a data structure that provides efficient methods for:

* **Prefix sum queries** (`query`)
* **Element updates** (`update`)

All in **O(log n)** time, using only **O(n)** space.

---

### 🔧 When Do We Use It?

Use a Fenwick Tree when:

* You have an array of numbers,
* You need to **frequently update values** (e.g., add 5 to index 3),
* And you want to **query the sum of elements from 0 to i** many times.

Common use-cases:

* Range sum queries
* Inversion count problems
* Counting frequencies efficiently (especially in dynamic situations)

---

### 🧩 How It Works

Internally, Fenwick Tree stores **partial sums** in a smart way using bit manipulation (`x & -x`) to find the **least significant bit**.

It’s like a segment tree, but simpler and more space-efficient when only prefix queries are needed.

---

### ⚙️ Core Operations

#### 1. **Update (index, value)**

Add `value` to the element at `index`.

```python
def update(i, val):
    i += 1
    while i <= n:
        tree[i] += val
        i += i & -i  # Move to next responsible node
```

#### 2. **Query (index)**

Returns the sum from index `0` to `index`.

```python
def query(i):
    i += 1
    res = 0
    while i > 0:
        res += tree[i]
        i -= i & -i  # Move to parent node
    return res
```

---

### 📦 Python Class Template

```python
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (size + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.tree[i] += val
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= i & -i
        return res

    # Optional: range sum from l to r
    def range_query(self, l, r):
        return self.query(r) - self.query(l - 1)
```

---

### ⏱️ Time & Space Complexity

| Operation | Time     | Space |
| --------- | -------- | ----- |
| `update`  | O(log n) | O(n)  |
| `query`   | O(log n) | O(n)  |

---

### 🧠 Intuition Tip

If Segment Tree feels like a full database,

> **Fenwick Tree is like a super-fast index on that database — limited but blazing fast.**

You don’t track the full range at each node — just the right **chunks of prefix sums**.
