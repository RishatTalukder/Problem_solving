# 📘 Binary Tree — Concept & Overview

### 🌳 What is a Binary Tree?

A **Binary Tree** is a hierarchical data structure in which **each node has at most two children** — referred to as the **left child** and the **right child**.

It’s called “binary” because each node can have **0, 1, or 2 children**.

---

### 🔧 Key Terminologies

* **Root**: The topmost node of the tree.
* **Leaf Node**: A node with no children.
* **Parent / Child**: Relationships between nodes connected by edges.
* **Depth**: The level of a node from the root.
* **Height**: The longest path from a node to a leaf.
* **Subtree**: A smaller tree consisting of a node and its descendants.

---

### 🧠 Common Types of Binary Trees

| Type                         | Description                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------- |
| **Full Binary Tree**         | Every node has 0 or 2 children.                                                           |
| **Perfect Binary Tree**      | All internal nodes have 2 children, and all leaves are at the same depth.                 |
| **Complete Binary Tree**     | All levels are fully filled except possibly the last, which is filled from left to right. |
| **Balanced Binary Tree**     | The height difference between left and right subtrees is at most 1 for every node.        |
| **Binary Search Tree (BST)** | Left child < Parent < Right child (used for fast searching/sorting).                      |

---

### 📈 Time Complexities (on average)

| Operation     | Time                          |
| ------------- | ----------------------------- |
| Access/Search | O(log n) *(for balanced BST)* |
| Insertion     | O(log n)                      |
| Deletion      | O(log n)                      |

> ❗ Worst-case for unbalanced trees: **O(n)**

---

### 🔁 Tree Traversal Methods

Traversal = visiting all nodes in a specific order.

1. **Inorder (Left, Root, Right)** → Sorted order for BST.
2. **Preorder (Root, Left, Right)** → Used to copy the tree.
3. **Postorder (Left, Right, Root)** → Used to delete the tree.
4. **Level Order (Breadth-First Search)** → Using a queue.

---

### 📦 Applications of Binary Trees

* Expression parsing and evaluation (Expression Trees)
* Searching and sorting (Binary Search Tree, AVL Tree)
* Priority Queues (Heap is a binary tree)
* Huffman Encoding (used in data compression)
* File systems, XML/HTML parsers, etc.

---

### 🧩 Representation in Code

A binary tree node is usually defined like this:

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

---

### 🧭 Summary

* Binary Tree is a **core hierarchical structure** in computer science.
* Mastering traversal and recursive patterns is key.
* Specialized versions (BST, Heaps, AVL) offer powerful use cases.

---

Let me know if you want a visual diagram or a printable cheat sheet version of this!
