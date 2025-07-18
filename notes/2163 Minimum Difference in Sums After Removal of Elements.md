## 🧠 Solving LeetCode Until I Become Top 1% — Day `47`

### 🔹 Problem: [Minimum Difference in Sums After Removal of Elements](https://leetcode.com/problems/minimum-difference-in-sums-after-removal-of-elements)

**Difficulty:**#Hard
**Tags:** #Heap, #PrefixSum, #Greedy, #SlidingWindow, #PriorityQueue

---

### 📝 Problem Summary

We are given an array `nums` of length `3n`.
We need to **remove a subsequence of exactly `n` elements**, leaving `2n` elements. Then divide these `2n` into:

- First part of length `n` → `sumfirst`
- Second part of length `n` → `sumsecond`

We must return the **minimum value** of `sumfirst - sumsecond` we can get.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Try every combination of removing `n` elements and then splitting the remaining `2n` into two halves. Calculate the difference.
  ⛔️ This is `O(comb(3n, n))` — **completely intractable** for `n` up to `1e5`.

- **Optimized Strategy:**
  The idea is:

  1. **Fix the first n elements**: Use a **max heap** to maintain the **smallest prefix sum** of size `n` from the **left 2n elements**.
  2. **Fix the last n elements**: Use a **min heap** to maintain the **largest suffix sum** of size `n` from the **right 2n elements**.
  3. Traverse the middle `n` elements and at each point:

     - Maintain `part1[i]`: the minimum possible sum from left side of `n` elements (using max heap).
     - Maintain the max suffix sum from the right (using min heap).
     - For each split, compute `part1[i] - part2[i]` and update the minimum.

- **Algorithm Used:**
  ✅ [[Prefix_Sum]]
  ✅ [[Heap]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3, n = len(nums), len(nums) // 3

        # Step 1: Min prefix sum of n elements using max heap
        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        ql = [-x for x in nums[:n]]
        heapq.heapify(ql)
        part1[0] = total

        for i in range(n, 2 * n):
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total

        # Step 2: Max suffix sum of n elements using min heap
        part2_sum = sum(nums[2 * n:])
        qr = nums[2 * n:]
        heapq.heapify(qr)
        ans = part1[n] - part2_sum

        for i in range(2 * n - 1, n - 1, -1):
            part2_sum += nums[i]
            heapq.heappush(qr, nums[i])
            part2_sum -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2_sum)

        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** `O(n log n)`
- **Space:** `O(n)` for the heaps and prefix arrays

---

### 🧩 Key Takeaways

- ✅ Maintaining a fixed-size max/min set using heaps can help simulate optimal greedy choices.
- ✅ Breaking a problem into “left”, “middle”, and “right” sections often allows efficient precomputation.
- 💡 The use of **prefix heap building** and **suffix heap building** is extremely powerful.
- 💭 If a problem involves `k` removals or partitions and is performance-critical, try **monotonic data structures**, **heaps**, or **multisets**.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
      → The idea was in my head but I struggled with the implementation.

- [ ] Did I write code from scratch?
      → I could eventually write it after understanding the heap transitions.

- [x] Did I understand why it works?
      → Yes, but it required stepping through slowly.

- [x] Will I be able to recall this in a week?
      → I will if I practice prefix/suffix heap techniques again.

---

### 📚 Related Problems

- [[238 Product of Array Except Self]]
- [[2099 Find Subsequence of Length K With the Largest Sum]]
- [[notes/3469 Find Minimum Cost to Remove Array Elements]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `47`    |
| Total Problems Solved | `388`    |
| Confidence Today      | 😐     |
| Leetcode Rating       | `1572` |
