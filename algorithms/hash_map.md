# 🔑 HashMap (aka Hash Table / Dictionary)

### 🧠 What Is a HashMap?

A **HashMap** is a data structure that stores **key-value pairs** and allows for **fast lookups, insertions, and deletions** — typically in **O(1)** time on average.

> 💡 Think of it like a super-fast phonebook where you can instantly find a contact by name (the key).

---

### 🔹 Why Use a HashMap?

* 🔍 **Fast Access:** O(1) average time for `get`, `put`, and `delete`.
* 🏷️ **Associate data:** Useful for mapping relationships (e.g. frequency of characters, mapping user IDs to profiles).
* 🧩 **Essential in many problems:** Sliding window, prefix sums, frequency counting, etc.

---

### 🧱 Common Operations

| Operation      | Description                             |
| -------------- | --------------------------------------- |
| `put(k, v)`    | Insert or update key `k` with value `v` |
| `get(k)`       | Retrieve value associated with key `k`  |
| `delete(k)`    | Remove key `k` from the map             |
| `in k`         | Check if key `k` exists (`k in map`)    |
| `len(map)`     | Get number of key-value pairs           |
| `map.keys()`   | Get all keys                            |
| `map.values()` | Get all values                          |

---

### 🧪 Example (Python)

```python
freq = {}

# Counting character frequency
for char in "hello":
    freq[char] = freq.get(char, 0) + 1

# freq = {'h': 1, 'e': 1, 'l': 2, 'o': 1}
```

---

### 🧠 How It Works

* Keys are passed through a **hash function** to generate an **index** in an internal array.
* Handles **collisions** using techniques like:

  * **Chaining** (linked lists at each index)
  * **Open addressing** (probing for next free slot)

---

### ⚠️ Things to Watch Out For

* Worst-case time complexity is **O(n)** if there are too many collisions.
* HashMaps do **not maintain order** (use `OrderedDict` or `dict` in Python 3.7+ if needed).
* Keys must be **hashable** (immutable types like `int`, `str`, `tuple` are fine; `list`, `dict` are not).

---

### 🧩 Common Use Cases

* Frequency maps (`Counter`)
* Caching (memoization)
* Duplicate detection
* Grouping data (like anagrams)
* Two-sum & other hash-based problems

---

### 🛠️ Time & Space Complexity

| Operation  | Time (Avg) | Time (Worst) | Space |
| ---------- | ---------- | ------------ | ----- |
| `put()`    | O(1)       | O(n)         | O(n)  |
| `get()`    | O(1)       | O(n)         | O(n)  |
| `delete()` | O(1)       | O(n)         | O(n)  |

---

### 💡 Handy Built-ins (Python)

```python
from collections import defaultdict, Counter

d = defaultdict(int)   # auto initializes missing keys
c = Counter("banana")  # {'b':1, 'a':3, 'n':2}
```

---

### ✅ Takeaways

* One of the most powerful tools in your coding arsenal.
* Ideal for counting, mapping, and tracking data efficiently.
* Frequently used in **Sliding Window**, **Prefix Sum**, **Graph**, and **Greedy** problems.