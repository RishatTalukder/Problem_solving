# 📘 Trie (Prefix Tree)

### 🌳 What is a Trie?

A **Trie** (pronounced “try”) is a **tree-like data structure** used to efficiently store and retrieve **keys in a dataset of strings**, especially when many of those strings share **common prefixes**.

> It is particularly useful for **dictionary-related problems** like autocomplete, spell checking, prefix matching, and word search.

---

### 🔠 Core Concept

Each **node** in a Trie represents a **character** in a word. The **path from the root to a node** represents a prefix or a complete word.

* The **root** is an empty node.
* **Edges** represent characters.
* A **boolean flag** is usually stored to indicate the **end of a valid word**.

---

### ✅ Key Features

| Feature               | Description                                                      |
| --------------------- | ---------------------------------------------------------------- |
| Prefix Search         | Efficiently checks if any word starts with a given prefix.       |
| Word Insertion/Search | Time complexity depends on word length, not the number of words. |
| Memory Efficient      | Shares common prefixes to reduce space.                          |

---

### 🧠 Time Complexity

Let `L` be the length of the word or prefix.

| Operation     | Time Complexity |
| ------------- | --------------- |
| Insert word   | O(L)            |
| Search word   | O(L)            |
| Search prefix | O(L)            |

> Much faster than searching each word in a list, especially when dealing with a large number of strings.

---

### 🔧 Trie Node Structure (Typical)

```python
class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end = False
```

### 🏗️ Basic Operations

* **Insert**: Traverse the tree character by character; create nodes as needed.
* **Search**: Traverse using each character; return true only if `is_end = True`.
* **StartsWith**: Same as search but doesn’t require `is_end = True`.

---

### 📚 Common Applications

* 🧩 Autocomplete engines
* 📝 Spell checkers
* 🕵️ Word search in 2D grids (e.g. Leetcode 212)
* 🔒 IP routing (longest prefix matching)
* 📖 Dictionary & Thesaurus systems
* 🧠 Solving problems with large datasets of strings (e.g. contact lists)

---

### 🧭 Summary

* A Trie is an **efficient, tree-based structure for strings**.
* Best used when dealing with **lots of words or prefixes**.
* Faster than hash maps for prefix-based queries.
* Can be enhanced with additional metadata (like frequency, indexes, etc.)

---

Let me know if you'd like a visual diagram of a Trie or want me to walk you through implementing it from scratch!
