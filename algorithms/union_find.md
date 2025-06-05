# 🧩 Union-Find (Disjoint Set Union) Algorithm

## 📌 Overview

**Union-Find**, also known as **Disjoint Set Union (DSU)**, is a data structure that keeps track of a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It supports two primary operations efficiently:

* **Find**: Determine which subset a particular element belongs to.
* **Union**: Merge two subsets into a single subset.

Union-Find is widely used in solving problems related to **connectivity** in graphs.

---

## 🔧 Use Cases

Union-Find is particularly useful in the following scenarios:

* **Connected components** in a graph
* **Cycle detection** in undirected graphs
* **Kruskal’s algorithm** for finding Minimum Spanning Tree
* **Equivalence problems** (e.g., Leetcode 1061, 399, 1202)
* **Dynamic connectivity** problems
* **Image segmentation**
* **Social network groups**

---

## 🧠 Core Concepts

### 1. **Find Operation**

The `find(x)` function returns the **representative (root)** of the set containing `x`. It helps identify whether two elements are in the same subset.

### 2. **Union Operation**

The `union(x, y)` function **merges** the subsets containing `x` and `y`.

### 3. **Path Compression (Optimization)**

While performing `find(x)`, we **flatten the structure** of the tree, making each node point directly to the root. This greatly improves performance.

### 4. **Union by Rank / Size (Optimization)**

When merging two trees, attach the smaller tree under the larger one to keep the overall structure shallow.

---

## 🛠️ Python Implementation

### Basic Version (with Path Compression):

```python
class UnionFind:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if self.parent.get(x, x) != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent.get(x, x)

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX  # Merge the sets
```

---

## ⏱️ Time Complexity

* **Amortized Time per Operation**: Nearly constant `O(α(n))`, where `α` is the inverse Ackermann function — grows extremely slowly.
* Very efficient in practice, even for large datasets (e.g., `10^5` or more elements).

---

## 📚 Example Problem

> **Leetcode 1061: Lexicographically Smallest Equivalent String**
> Given equivalency rules between characters, determine the smallest lexicographical string by replacing characters with their equivalent ones.

Union-Find helps group characters and efficiently determine the representative (smallest character in each set).

---

## ✅ Summary

* Union-Find is a powerful structure for managing dynamic sets.
* Optimizations like **path compression** and **union by rank** make it very efficient.
* Essential in graph algorithms, equivalence problems, and connected components.

