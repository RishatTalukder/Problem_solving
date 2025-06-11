## 🧠 Solving LeetCode Until I Become Top 1% — Day `16`

### 🔹 Problem: [3445 Maximum Difference Between Even and Odd Frequency II](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/)

**Difficulty:** 😩 #DAMN
**Tags:** #PrefixSum, #Bitmasking, #FenwickTree, #Dp, #Hashing

---

### 📝 Problem Summary

> You're given a string of digits (0-4) and a number `k`. Your job is to find a substring of length **at least k** where:
>
> - One character `a` has an **odd** frequency
> - Another character `b` has an **even** frequency
>   Then return the **maximum** value of `freq[a] - freq[b]` for all such substrings.

Yup. Sounds deceptively easy, like a classic sliding window problem, right? Right?? **WRONG.**

---

### 🧠 My Thought Process

#### 💭 Brute Force Idea:

- “Hmm… maybe we can just try all substrings of size ≥ k, count the frequencies, and if any `a` is odd and `b` is even, calculate `freq[a] - freq[b]`.”
- That would take about `O(n^3)` if you're unlucky enough to check all substrings and all digit pairs inside them. Beautiful time complexity for 2025, right?
- **Conclusion:** Totally impractical, _unless you're sending your computer to the next dimension to compute._

#### 🧠 Optimized Strategy:

- I honestly tried. I really thought this might be a **sliding window** problem. I _felt_ like it was sliding window. I imagined sliding through the array like a ninja.

- But then came the pain.

- I figured out that we needed to **track frequency differences and parity** across substrings, but I couldn’t figure out how to **efficiently compare earlier prefix frequencies** without redoing work.

- And then, came The Great Enlightenment™:

  > **Here is The great ChatGPT explaining the solution of [raj ghosh](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/6831422/all-language-solutions0msbeat-100all-in-0f88h/)** — the savior of lost problem solvers.

- The approach uses:

  - Prefix sums to compute frequency difference of digits `a` and `b`
  - Bitmask parity tracking to filter only odd/even freq substrings
  - And a **Fenwick Tree (Binary Indexed Tree)** to keep track of the _minimum prefix difference so far_ for matching parity groups

  Because apparently solving substring frequency problems requires _range minimum queries_ over _prefix-difference state-space_ and that’s just another Tuesday on LeetCode now.

### Algorithm Used:

[[fenwick_tree]] [[prefix_sum]] [[bitmasking]] [[dp]] [[hash_map]]

---

### ⚙️ Code Implementation (Python)

```python
class FenwickTree:
    INF = float('inf')

    def __init__(self, size):
        self.size = size
        self.tree = [self.INF] * (size + 1)

    # Update the tree at index i with the minimum of current and new value
    def update(self, i, value):
        i += 1  # 1-based indexing
        while i <= self.size:
            self.tree[i] = min(self.tree[i], value)
            i += i & -i

    # Query the minimum value in range [0, i]
    def query(self, i):
        i += 1  # 1-based indexing
        result = self.INF
        while i > 0:
            result = min(result, self.tree[i])
            i -= i & -i
        return result

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        # A helper class to implement Fenwick Tree (Binary Indexed Tree) for range minimum queries
        n = len(s)
        max_diff = float('-inf')  # To track the final answer

        # Try every pair of digits (a != b) from 0 to 4
        for a in range(5):
            for b in range(5):
                if a == b:
                    continue

                # Prefix arrays
                D = [0] * (n + 1)        # Net difference of count[a] - count[b]
                pa = [0] * (n + 1)       # Parity of count[a] (0: even, 1: odd)
                pb = [0] * (n + 1)       # Parity of count[b]
                countB = [0] * (n + 1)   # Total number of digit b up to index i

                # Build the prefix state arrays
                for i in range(1, n + 1):
                    digit = int(s[i - 1])
                    D[i] = D[i - 1] + (1 if digit == a else 0) - (1 if digit == b else 0)
                    pa[i] = (pa[i - 1] + (1 if digit == a else 0)) & 1  # Even/Odd parity
                    pb[i] = (pb[i - 1] + (1 if digit == b else 0)) & 1
                    countB[i] = countB[i - 1] + (1 if digit == b else 0)

                # 2x2 matrix of Fenwick Trees based on parity of a and b
                trees = [[FenwickTree(n + 1) for _ in range(2)] for _ in range(2)]

                for j in range(n + 1):
                    # Only update tree if the prefix ends at least k characters before current
                    if j >= k:
                        idx = j - k
                        trees[pa[idx]][pb[idx]].update(countB[idx], D[idx])

                    if j > 0:
                        need_pa = 1 - pa[j]  # We want a to be odd
                        need_pb = pb[j]      # We want b to be even

                        if countB[j] > 0:
                            # Query the best prefix value satisfying parity and b count
                            best_val = trees[need_pa][need_pb].query(countB[j] - 1)
                            if best_val != FenwickTree.INF:
                                max_diff = max(max_diff, D[j] - best_val)

        return max_diff if max_diff != float('-inf') else -1
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n) for each of 20 digit-pairs ⇒ **O(20 × n log n)**
- **Space:** O(n) for prefix arrays and BITs

---

### 🧩 Key Takeaways

- ✅ Learned how **prefix difference arrays** and **bit parity** can be used to encode substring properties
- 💡 The tricky part was realizing how to _track valid earlier substrings_ to maximize the result — you need to remember _states_, not just positions
- 💭 This pattern shows up in problems where you want to optimize some **delta between frequency/counts** under constraints like length, parity, etc.

---

### 🔁 Reflection (Self-Check)

- [❌] Could I solve this without help? — **Absolutely not.**
- [❌] Did I write code from scratch? — **Only after dissecting GPT and Raj’s work.**
- [✅] Did I understand why it works? — **I tried my best, but I’m still not sure if I’ll remember it next week.**
- [❌] Will I be able to recall this in a week? — **Nope, been there, done that.**

---

### 📚 Related Problems

- [[3005 Count Elements With Maximum Frequency]]
- [[1838 Frequency of the Most Frequent Element]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `16`   |
| Total Problems Solved | `348`  |
| Confidence Today      | 😩😩😩 |
