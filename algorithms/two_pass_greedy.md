# Two-Pass Greedy Algorithm

**Two-pass greedy** is a pattern where we make **two directional passes** over the data (usually an array) to enforce certain conditions that can't be guaranteed in just one pass.

---

### 🔁 **Pattern:**

1. **Left-to-right pass**:
   Enforce a local condition (e.g., current > previous → do something).
2. **Right-to-left pass**:
   Enforce the symmetric condition in reverse (e.g., current > next → adjust accordingly).

---

### 🧠 **When to Use:**

* When constraints depend on **both previous and next elements**.
* When satisfying one direction may break conditions in the opposite direction.
* When **local optimum in one direction is not enough** for global correctness.

---

### 🧩 **Common Problems Using This:**

* [[135 Candy]]
* [[notes/Leetcode 122: Best Time to Buy and Sell Stock II (variant)]]
* Scheduling or resource allocation where neighbors affect outcomes

---

### ⚠️ **Key Insight:**

> Greedily handle one direction first, then fix violations from the other side without breaking the previous one (using `max()` or similar safeguards).
