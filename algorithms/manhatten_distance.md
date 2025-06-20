# 📏 Note: Manhattan Distance

### 📌 Definition

**Manhattan Distance** (a.k.a. **Taxicab Distance** or **L1 Distance**) between two points in a grid is the **sum of the absolute differences** of their corresponding coordinates.

If the two points are:

* `P1 = (x₁, y₁)`
* `P2 = (x₂, y₂)`

Then the Manhattan Distance is:

```
|x₁ - x₂| + |y₁ - y₂|
```

---

### 🧠 Intuition

Imagine you're walking in a city where you can only move along the grid (no diagonal shortcuts, like a taxi on streets).
The total number of blocks you'd walk to go from point A to point B is the **Manhattan Distance**.

Unlike **Euclidean Distance** (which measures straight-line distance), Manhattan only considers **horizontal + vertical steps**.

---

### ✅ Properties

* It **ignores diagonals**.
* Works well in grid-based movement (e.g., mazes, chessboard, robotics).
* Always **≥ 0**.
* If `P1 == P2`, the distance is `0`.
* Often used in problems involving **4-directional movement**.

---

### 📦 When to Use

* Problems with **grid navigation** using only up/down/left/right.
* **AI pathfinding** on grids (e.g., A\*, greedy BFS heuristics).
* **Distance heuristics** for approximations.
* Geometry problems where movement cost depends on axis-aligned travel.

---

### 💻 Code Snippet (Python)

```python
def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
```

---

### 🧩 Example

If you're at `(2, 3)` and your destination is `(5, 1)`,
then the Manhattan Distance is:

```
|2 - 5| + |3 - 1| = 3 + 2 = 5
```

You’ll walk 3 steps right and 2 steps down — total 5 moves.

---

### 📝 Tip for Competitive Programmers

* In **greedy/optimization** problems, Manhattan distance is often used to **maximize or minimize travel/coverage**.
* Watch for **"maximizing distance with limited moves"** — convert balanced steps into unbalanced steps to increase Manhattan distance.
* **Useful with BFS** in grids: often used to sort or prioritize points.