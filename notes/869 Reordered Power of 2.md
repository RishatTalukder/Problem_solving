## 🧠 Solving LeetCode Until I Become Top 1% — Day `56`

### 🔹 Problem: [869 Reordered Power of 2](https://leetcode.com/problems/reordered-power-of-2/)

**Difficulty:** #Medium
**Tags:** #Math #Sorting #Permutations

---

### 📝 Problem Summary

We are given an integer `n`.
We can reorder its digits in any way (no leading zeros) to form a new number.
The task is to determine if **any** such rearrangement is a power of two.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Generate all permutations of the digits in `n` and check if any forms a power of two.

  - Problem: This is factorial time complexity, way too slow for large numbers (up to 10 digits).

- **Optimized Strategy:**

  - Powers of two are rare: in 32-bit signed integers, only 31 possibilities (`1 << 0` to `1 << 30`).
  - Instead of permuting `n`, just compare its **digit frequency** to the digit frequency of each power of two.
  - Trick: Sorting the string representation of the number acts as a compact “signature” for its digits.
    Example:

    ```
    128  -> "128"  -> "128"
    821  -> "821"  -> "128" ✅ matches
    ```

- **Algorithm Used:**
  Precompute digit signatures for all powers of two and check for a match.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        def count_digits(x):
            # Returns the sorted string of digits as a "signature"
            return ''.join(sorted(str(x)))

        target = count_digits(n)

        # Compare target with all powers of 2 up to 2^30 (fits in 32-bit int)
        for i in range(31):
            if count_digits(1 << i) == target:
                return True
        return False
```

---

### ⏱️ Time & Space Complexity

- **Time:**

  - Sorting digits: O(d log d), where d ≤ 10 (constant).
  - Checking 31 powers of two → O(31 × d log d) ≈ O(1) constant time.

- **Space:** O(1) extra space (only temporary strings).

---

### 🧩 Key Takeaways

- ✅ Using **sorted digit signatures** is a powerful trick to check for “digit rearrangement” equality.
- 💡 Powers of two are so sparse that brute-forcing permutations isn’t necessary.
- 💭 Recognize that when a problem says "rearrange digits" but the range is small, you can precompute possibilities.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help?
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `55`   |
| Total Problems Solved | `411`  |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
