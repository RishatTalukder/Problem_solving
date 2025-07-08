## 🧠 Solving LeetCode Until I Become Top 1% — Day `30`

### 🔹 Problem: [2040 Kth Smallest Product of Two Sorted Arrays](https://leetcode.com/problems/kth-smallest-product-of-two-sorted-arrays)

**Difficulty:** #Hard
**Tags:** #BinarySearch

---

### 📝 Problem Summary

> We're given two sorted arrays (`nums1` and `nums2`) and a number `k`.
> We need to find the `k`-th smallest product we can get by multiplying an element from `nums1` with one from `nums2`.
> Arrays can contain negative numbers and zeros.
> We're not asked to **generate** the products, but to **find** the value of the `k`-th smallest product.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - I initially thought about creating a full 2D grid of all possible products (`nums1[i] * nums2[j]`) and sorting them to get the `k`-th smallest.
  - But I quickly realized it would be too slow — 50,000 × 50,000 = 2.5 \* 10⁹ elements is impossible to handle in memory or time.

- **What I _thought_:**

  - I assumed it was a **DP problem** — something like `0/1 knapsack` where we pick combinations and track them.
  - It felt like I could "build a table" of size `len(nums1) × len(nums2)` and walk through it somehow\...
  - I got excited thinking I might solve a hard problem on my own for the first time 😅

- **Reality check:**

  - I was wrong. It wasn’t DP — it was a **binary search on the value space**, not on indices.
  - I didn’t manage to implement it on my own and had to look up the solution.
  - Once I saw the code, I realized the core idea (binary search + counting pairs) was something I had seen before, but the tricky part was correctly handling **negatives and zeros**.

---

### ✅ Optimal Solution (from discussion)

- The key insight is:

  > Instead of generating all products, binary search on the **value** of the k-th smallest product.

- To make that work, we need a helper function that, given a number `x`, counts how many products are ≤ `x`.
- This counting is done using:

  - `bisect_right` for positive numbers (upper bound)
  - `bisect_left` for negative numbers (lower bound)
  - Special handling for zero, since `0 * anything = 0`

- Then we binary search in a huge range (like -10¹⁰ to 10¹⁰) to find the smallest `x` such that `count_pairs(x) >= k`.

---

### Algorithms Used

[[Binary_Search]]

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_pairs(x: int) -> int:
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    target = x // a
                    if x % a != 0:
                        target += 1
                    count += len(nums2) - bisect.bisect_left(nums2, target)
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        low, high = -10**10, 10**10
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid
        return low
```

---

### ⏱️ Time & Space Complexity

- **Time:** `O(n * log m * log R)`

  - `R` is the range of possible products (binary search steps)

- **Space:** `O(1)`

---

### 🧩 Key Takeaways

- ✅ Learned how to **binary search over values**, not indices — a common pattern in “k-th smallest” problems involving virtual sorted arrays.
- 💡 The hardest part was handling **negative values**, **division rounding**, and **zero cases** correctly.
- 😖 I underestimated the complexity and misclassified it as a DP problem.
- 💭 Now I know: if a brute-force 2D matrix of values is implied, but too big, and the question asks for "k-th smallest", there's a good chance it's a binary search on value.

---

### 🔁 Reflection (Self-Check)

- [❌] Could I solve this without help?
- [❌] Did I write code from scratch?
- [✅] Did I understand why it works after reading?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[373 Find K Pairs with Smallest Sums]]
- [[532 K-diff Pairs in an Array]]
- [[2398 Maximum Number of Robots Within Budget]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `30`  |
| Total Problems Solved | `363` |
| Confidence Today      | 😐    |
