## 🧠 Solving LeetCode Until I Become Top 1% — Day `37`

### 🔹 Problem: [3307 Find the K-th Character in String Game II](https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/?envType=daily-question&envId=2025-07-04)

**Difficulty:** #Hard
**Tags:** #BitManipulation, #BinaryTree, #Simulation, #Math

---

### 📝 Problem Summary

You're given a list of binary operations and an integer `k`. The operations describe a string-building process where:

- `0` → Duplicate the current string.
- `1` → Duplicate and rotate all characters (i.e., `'a'` → `'b'`, `'z'` → `'a'`).

Starting from the character `'a'`, the string grows exponentially. You must return the character at the **k-th position** (1-indexed) in the final string. Since the string size can grow beyond `2^60`, directly building the string is impossible.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  My first dumb-dumb instinct was to actually simulate the whole string. After thinking for two seconds and glancing at `k <= 10^14`, I immediately panicked. 🫠
  Clearly, building the string is impossible. So I guessed maybe I should reverse simulate or use some kind of tree trick.

- **Optimized Strategy:**
  I saw someone mention using bit manipulation and tree traversal. That made me realize the string growth follows a **binary tree-like structure** where each operation is a node:

  - Each operation level doubles the string length.
  - If the op is `1`, you also rotate characters.

  So instead of building the string forward, you trace **backwards** from `k` to find how many `+1` (rotations) were applied to `'a'`. This only requires `O(log k)` steps.

  The idea is to walk back the path to the first `'a'`, tracking how many times a rotation occurred on the path to position `k`.

- **Algorithm Used:**
  `Bit Manipulation` + `Reverse Simulation`

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        ans = 0
        while k != 1:
            t = k.bit_length() - 1
            if (1 << t) == k:
                t -= 1
            k -= 1 << t
            if operations[t]:
                ans += 1
        return chr(ord("a") + (ans % 26))
```

---

### ⏱️ Time & Space Complexity

- **Time:** `O(log k)` → each step reduces `k` significantly
- **Space:** `O(1)` → only a few variables

---

### 🧩 Key Takeaways

- ✅ Learned how exponential string-building problems can be reversed via bit tricks.
- 💡 The use of `bit_length()` to identify subtree levels is brilliant and elegant.
- 💭 These problems scare me because of the size of the numbers involved, but breaking them down reveals a simple, elegant path.

---

### 🔁 Reflection (Self-Check)

- [ ] Could I solve this without help?
      ❌ I had the general reverse idea but couldn’t optimize it down. I panicked and opened discussion 😅

- [ ] Did I write code from scratch?
      ❌ No, I followed a solution after understanding it deeply.

- [x] Did I understand why it works?
      ✅ Yes, and honestly I feel proud now that I can explain it.

- [x] Will I be able to recall this in a week?
      ✅ I think so, now that I understand the binary tree traversal pattern.

---

### 📚 Related Problems

- [[848. Shifting Letters]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `36`  |
| Total Problems Solved | `371` |
| Confidence Today      | 😐    |
