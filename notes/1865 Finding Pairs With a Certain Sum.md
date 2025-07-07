## 🧠 Solving LeetCode Until I Become Top 1% — Day `39`

### 🔹 Problem: [1865. Finding Pairs With a Certain Sum](https://leetcode.com/problems/finding-pairs-with-a-certain-sum/)

**Difficulty:** Medium
**Tags:** #HashMap, #Simulation, #TwoSum

---

### 📝 Problem Summary

We are given two arrays `nums1` and `nums2`. `nums1` is static (unchanging), but `nums2` can be modified using `.add(index, val)`, which adds `val` to the value at `nums2[index]`.
We then need to support `.count(tot)` queries that return the number of pairs `(i, j)` such that:

```
nums1[i] + nums2[j] == tot
```

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Iterate through all pairs in `nums1` and `nums2` for every `count()` call — but this would be way too slow (up to 1e8 operations).

* **Optimized Strategy:**
  Since `nums1` is fixed, we can keep a running `Counter` for `nums2`.
  For every `count(tot)` query, loop over each value `a` in `nums1` and look for `tot - a` in the `Counter` of `nums2`.
  This reduces query time to O(n1), and updates to O(1) per `.add()`.

* **Algorithm Used:**
  Hash Map (Counter) + Simulation

---

### ⚙️ Code Implementation (Python)

```python
from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old_val = self.nums2[index]
        new_val = old_val + val

        self.count2[old_val] -= 1
        if self.count2[old_val] == 0:
            del self.count2[old_val]

        self.count2[new_val] += 1
        self.nums2[index] = new_val

    def count(self, tot: int) -> int:
        result = 0
        for num in self.nums1:
            complement = tot - num
            result += self.count2.get(complement, 0)
        return result
```

---

### ⏱️ Time & Space Complexity

* **Time:**

  * `.add()` → O(1)
  * `.count()` → O(len(nums1)) = up to 1000
* **Space:** O(len(nums2)) for the frequency map

---

### 🧩 Key Takeaways

* ✅ Learned how to handle **mutable state** with a `Counter`.
* 💡 The trick is to **not brute-force pairs**, but instead count complements using a hash map.
* 💭 If a problem is about `counting pairs`, always think in terms of **frequency mapping**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? *(Yes, once the problem was clearer.)*
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [1. Two Sum](https://leetcode.com/problems/two-sum/)
* [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `36`  |
| Total Problems Solved | `368` |
| Confidence Today      | 😃    |
