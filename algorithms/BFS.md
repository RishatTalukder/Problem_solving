# 📘 BFS (Breadth-First Search) — Algorithm Note

### 📌 What is BFS?

**BFS (Breadth-First Search)** is an algorithm for traversing or searching in data structures like trees or graphs. It explores **all the neighbor nodes at the current depth** before moving on to nodes at the next depth level.

It uses a **queue (FIFO)** to keep track of nodes to explore and ensures we explore in layers.

---

### 📦 When to Use BFS?

✅ When you need the **shortest path in an unweighted graph**

✅ When you need to **explore all nodes level-by-level**

✅ For **layered problems** (e.g., transformations, moves in a game)

✅ In **lexicographical search** when we want to explore solutions in increasing/decreasing order

✅ In **state-space traversal** (e.g., puzzles, subsequence generation)

---

### 🔍 Algorithm Steps

1. Start from a node (or state), push it to a **queue**.
2. While the queue is not empty:

   * Pop the current node.
   * For each valid **neighbor** (or next state):

     * If it's unvisited or satisfies the condition, enqueue it.
3. Optionally use a **visited set** or state pruning to avoid cycles or repeated work.

---

### 🧠 Example: BFS in a 2D Grid

```python
from collections import deque

def bfs_grid(grid, start):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    q = deque([start])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != '#' and (nr, nc) not in visited:
                q.append((nr, nc))
```

---

### 🧊 Example: BFS on Strings (State-Space Search)

```python
from collections import deque

def bfs_generate_subsequences(s):
    q = deque([''])
    results = []

    while q:
        sub = q.popleft()
        results.append(sub)
        for ch in 'abc':
            q.append(sub + ch)
    return results
```

---

### ⏱️ Time & Space Complexity

* **Time:** Depends on branching factor (B) and depth (D) → up to **O(B^D)**
* **Space:** O(B^D) — due to queue holding all nodes at a level

---

### ⚠️ Common Pitfalls

* Forgetting to mark states as visited → may cause infinite loops
* Using DFS when you need **shortest paths** → use BFS instead!
* Expanding too many unnecessary states → prune wisely!

---

### 🧩 Key Takeaways

* BFS is your go-to for **shortest path**, **level order**, and **layered exploration**
* Pair it with **sets** or **hashmaps** to track visited or processed nodes
* Often combined with other techniques: bitmasks, string ops, matrix traversal
