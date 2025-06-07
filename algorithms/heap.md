# 🥇 Heap / Priority Queue – Notes

### 📌 What is a Heap?

A **heap** is a specialized tree-based data structure that satisfies the **heap property**:

- In a **min-heap**, the parent is always **less than or equal** to its children.
- In a **max-heap**, the parent is always **greater than or equal** to its children.

Heaps are commonly implemented as arrays and support efficient **insertion** and **deletion of the minimum or maximum** element.

---

### 🧮 Priority Queue

A **priority queue** is an abstract data type where each element has a **priority**, and elements are served based on their priority (not just insertion order).

Under the hood, **heaps** are often used to implement priority queues efficiently.

---

### 🔧 Common Operations (Min-Heap)

| Operation                   | Description                                   | Time Complexity |
| --------------------------- | --------------------------------------------- | --------------- |
| `heapq.heappush(h, val)`    | Push `val` into heap `h`                      | O(log n)        |
| `heapq.heappop(h)`          | Pop and return the **smallest** element       | O(log n)        |
| `heapq.heapify(arr)`        | Convert list `arr` into a heap in-place       | O(n)            |
| `heapq.heappushpop(h, val)` | Push then pop (more efficient than two calls) | O(log n)        |
| `heapq.nlargest(k, h)`      | Get `k` largest elements (max-heap behavior)  | O(k log n)      |
| `heapq.nsmallest(k, h)`     | Get `k` smallest elements                     | O(k log n)      |

In Python, `heapq` implements a **min-heap** by default.

---

### 🌀 Max-Heap in Python?

Python's `heapq` doesn't have a built-in max-heap, but you can simulate one by **pushing negative values**:

```python
import heapq
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
print(-heapq.heappop(max_heap))  # 5
```

---

### 🧠 Use Cases

- Dijkstra’s shortest path algorithm
- A\* search
- Huffman coding
- Top-k problems (e.g., top k frequent elements)
- Task scheduling by priority
- Real-time simulations (like event queues)

---

### 💡 Key Tips

- Use `heapq` when you frequently need the **smallest/largest** item in a dynamic list.
- For custom objects or more control, use `tuple(priority, item)` to sort by priority.
- Don't forget: `heapq` works on **lists** (it's not a class-based interface).
