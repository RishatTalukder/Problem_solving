# 🧠 What is Iterative DFS?

**Iterative DFS** is a non-recursive version of Depth-First Search, typically implemented using an explicit **stack** instead of the call stack used in the recursive version.

It explores a tree or graph structure by going **deep before wide**, just like recursive DFS, but avoids stack overflow issues and offers more control over the traversal process.

---

## 🧾 When to Use Iterative DFS

* When recursion depth may exceed Python’s call stack limit (e.g., large trees or graphs).
* When you want to **mimic DFS manually** to have more control over the traversal process (e.g., tracking parents, paths, or backtracking logic).
* In environments where recursion is disallowed or dangerous (e.g., interview whiteboard setting, production code with unknown inputs).

---

## 📦 Typical Use Cases

* Tree or graph traversal
* Lexicographical traversal (as in \[LeetCode 386: Lexicographical Numbers])
* Backtracking simulations
* Generating permutations or combinations
* Maze or pathfinding algorithms

---

## 🧩 Code Template

### Tree/Graph Iterative DFS (Generic)

```python
def iterative_dfs(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # process(node) if needed
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
```

### Tree-Like Structure (e.g., Lexicographical Numbers)

```python
def lexicalOrder(n: int) -> List[int]:
    stack = [1]
    res = []
    while stack:
        curr = stack.pop()
        if curr <= n:
            res.append(curr)
            for i in range(9, -1, -1):
                next_num = curr * 10 + i
                if next_num <= n:
                    stack.append(next_num)
    return res
```

---

## ✅ Pros

* Avoids recursion limits
* Easier to debug (step-by-step control)
* Stack-based logic often matches how problems are described (e.g., backtracking)

---

## ⚠️ Cons

* Manual stack management can be less readable than recursion
* May require extra code to simulate recursion-like behavior (e.g., backtracking states)

---

## 📌 Summary

* **Iterative DFS** is DFS using an explicit stack instead of recursion.
* Preferred in systems with recursion limits or when more traversal control is needed.
* Especially useful in problems with large input size or lexicographic ordering needs.

