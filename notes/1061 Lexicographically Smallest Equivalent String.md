## 🧠 Solving LeetCode Until I Become Top 1% — Day `10`

### 🔹 Problem: [1061 Lexicographically Smallest Equivalent String](https://leetcode.com/problems/lexicographically-smallest-equivalent-string/description/?envType=daily-question&envId=2025-06-05)

**Difficulty:** #Medium
**Tags:** #UnionFind

---

### 📝 Problem Summary _(in your own words)_

> We have to find the lexicographically smallest equivalent string for a given string `baseStr` using the equivalence relations defined in `pairs`. Each pair `(a, b)` means that `a` and `b` are equivalent. Also if `a` is equivalent to `b` and `b` is equivalent to `c`, then `a` is equivalent to `c`. The output should be the smallest string that can be formed by replacing characters in `baseStr` with their equivalents.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This problem was easier than expected because It has the `lexicographically` word in it and I thought there is no way i will be able to solve it. But the giva away was the if `a` is equivalent to `b` and `b` is equivalent to `c`, then `a` is equivalent to `c`. That's when I realised this should be a problem with linked components and we have two types of linked data structures: `trees` or `graphs`. I thought of trnsforming the pairs into a graph and store each charecter as a node and it's connected nodes in a heap. This way I can get the smallest character in O(log n) time. But I was a Little of and then I realised why not use [[union_find]] to solve this problem. And that awas the actual solution._

- **Optimized Strategy:**
  _We can use the Union-Find data structure to group equivalent characters together with a heirarchy. The idea is to union the characters in each pair and then find the smallest character in each group. You can find full union find algortihm explanation [in this video](https://www.youtube.com/watch?v=ayW5B2W9hfo)_

  - The only tricky(not tricky but a single logic) part was how to store the smallest character in each group. The way I did it was to use a `dictionary` where the key is the root of the group and the root should be the smallest character in the group.
  - after that we can iterate through the `baseStr` and for each character, we can find the root of the group it belongs to and replace it with the smallest character in that group.

- **Algorithm Used:**
  [[union_find]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = {}

        def find(x):
            if parent.get(x, x) != x:
                parent[x] = find(parent[x])
            return parent.get(x, x)

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[max(rootX, rootY)] = min(rootX, rootY)

        for a, b in zip(s1, s2):
            union(a, b)

        result = []
        for char in baseStr:
            result.append(find(char))

        return ''.join(result)
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n + m + k), where `n` is the length of `s1`, `m` is the length of `s2`, and `k` is the length of `baseStr`. The union-find operations are nearly constant time due to path compression.
- **Space:** O(n + m), where `n` is the number of unique characters in `s1` and `m` is the number of unique characters in `s2`. The space is used for the parent dictionary.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - It was actually a good practice for `Union-Find` and how to use it to solve problems with equivalence relations.
- 💡 What made this problem tricky?
  - The tricky part was understanding how to maintain the smallest character in each equivalence group while using union-find.
- 💭 How will I recognize a similar problem in the future?
  - If I see a problem with equivalence relations or connected components, I will think of using the Union-Find data structure to solve it.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [😊] Did I write code from scratch?
- [✅] Did I understand why it works?
- [😊] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[3474 Lexicographically Smallest Generated String]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `10`  |
| Total Problems Solved | `345` |
| Confidence Today      | 😃    |
