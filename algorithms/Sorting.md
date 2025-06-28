# 📝 Note: Sorting

### 🔹 What is Sorting?

**Sorting** is the process of rearranging a collection of items (typically elements in an array or list) **in a specific order** — most commonly ascending or descending.

---

### 🔹 Why is Sorting Important?

Sorting is foundational in programming and algorithm design. It helps in:

* **Searching faster** (e.g., binary search)
* **Data normalization** for comparisons
* **Problem simplification** (greedy, two-pointers, sliding window)
* **Efficient grouping or partitioning**

---

### 🔹 Common Sorting Orders

* **Ascending**: smallest → largest (`1, 3, 5, 7`)
* **Descending**: largest → smallest (`9, 6, 4, 2`)
* **Custom**: e.g., based on string length, frequency, etc.

---

### 🔹 Built-in Sort (Python)

```python
arr = [4, 2, 9, 1]

# Ascending
arr.sort()

# Descending
arr.sort(reverse=True)

# Custom: Sort by string length
words.sort(key=len)
```

---

### 🔹 Common Sorting Algorithms

| Algorithm      | Time Complexity | Stable | In-place | Use-case                              |
| -------------- | --------------- | ------ | -------- | ------------------------------------- |
| Bubble Sort    | O(n²)           | ✅      | ✅        | Educational purposes                  |
| Selection Sort | O(n²)           | ❌      | ✅        | Simple but inefficient                |
| Insertion Sort | O(n²)           | ✅      | ✅        | Small datasets or nearly sorted data  |
| Merge Sort     | O(n log n)      | ✅      | ❌        | Stable sort for large datasets        |
| Quick Sort     | O(n log n) avg  | ❌      | ✅        | Fast and widely used                  |
| Heap Sort      | O(n log n)      | ❌      | ✅        | When constant memory is needed        |
| TimSort        | O(n log n)      | ✅      | ✅        | Python’s built-in `.sort()` uses this |
| Counting Sort  | O(n + k)        | ✅      | ❌        | When input range is small             |
| Radix Sort     | O(nk)           | ✅      | ❌        | Large integers with bounded digits    |
| Bucket Sort    | O(n + k)        | ✅      | ❌        | Uniformly distributed data            |

---

### 🔹 When to Use What?

* Use **built-in sort** (`sort()` or `sorted()`) in most cases.
* Use **custom sort with key** for non-standard ordering.
* Use **Counting/Radix sort** for large arrays of small integers.
* Use **Merge Sort** when stability matters and recursion is acceptable.
* Use **Quick Sort** for fast in-place sorting (often best average-case performance).

---

### 🔹 Interview Tips

* Understand **stable vs unstable sorting**.
* Know when **custom sorting** using `key` is helpful.
* Many problems combine **sorting + greedy**, **sorting + binary search**, or **sorting + two pointers**.

---

### 🧩 Problems that Use Sorting

* Merge Intervals
* Meeting Rooms
* Maximum Units on a Truck
* Minimum Platforms
* Relative Sort Array
* Sorting-based Greedy (e.g., Task Scheduler, Job Sequencing)