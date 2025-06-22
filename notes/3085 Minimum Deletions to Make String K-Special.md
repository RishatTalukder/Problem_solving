## 🧠 Solving LeetCode Until I Become Top 1% — Day `26`

### 🔹 Problem: [3085. Minimum Deletions to Make String K-Special](https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/?envType=daily-question&envId=2025-06-21)

**Difficulty:** #Medium
**Tags:** #Greedy, #Sorting, #FrequencyCounting

---

### 📝 Problem Summary

> You're given a string `word` and an integer `k`. You can delete any characters you want. Your goal is to **minimize the total deletions** such that the **maximum and minimum character frequencies in the final string differ by at most `k`**.
>
> In other words, if one character appears a lot and another very few times, you might need to delete some instances of characters to bring their frequencies closer together.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * Count frequency of each character.
  * Try deleting every possible combination of characters to make the frequencies valid.
  * Obviously, this is **super inefficient** because of the exponential number of possibilities.

* **What I Figured Out:**

  * I understood that I needed to **normalize the frequencies** somehow.
  * Realized I should **sort** the frequencies and try to bring all of them into a valid range by deletion.
  * But I couldn't figure out how to choose the optimal base frequency and how to trim only the oversized ones.

---

### ✅ Optimal Solution (Greedy + Sorting)

#### 🔍 Strategy:

1. Count how often each character appears.
2. Sort the frequencies in ascending order.
3. Try making **each frequency value** the “base frequency” that others should stay close to, within a range of `[base, base + k]`.

#### 💡 Greedy Insight:

For each possible base frequency:

* **Characters with smaller frequencies** than the base? Just **delete them all** — no way to "increase" frequency.
* **Characters with bigger frequencies** than `base + k`? **Trim them down** to `base + k` — only delete the excess.
* The greedy part here is realizing that it’s always better to:

  * **Remove entire characters** that are too small (less than base),
  * **Partially reduce** the ones that are too big (greater than base + k),
  * And skip those in the safe range.

#### 🧠 Why this works:

Trying every frequency as a "base" gives us a chance to test each possible tolerance window `[base, base + k]`. This is a classic **"fix a center and adjust the rest"** greedy pattern.

---

### ⚙️ Code Implementation (Python)

```python
from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        char_freq = Counter(word)
        freq_list = sorted(char_freq.values())
        total_chars = len(freq_list)
        min_deletions = float('inf')

        for i in range(total_chars):
            base_freq = freq_list[i]
            deletions = 0

            # Delete all characters with freq < base
            for j in range(i):
                deletions += freq_list[j]

            # Delete excess of characters with freq > base + k
            for j in range(i + 1, total_chars):
                if freq_list[j] > base_freq + k:
                    deletions += freq_list[j] - (base_freq + k)

            min_deletions = min(min_deletions, deletions)

        return min_deletions
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(N log N) for sorting frequency list, where N = number of unique characters (at most 26)
* **Space:** O(N) for frequency storage

---

### 🧩 Key Takeaways

* ✅ This is a perfect use-case of **greedy window fixing** where you pick a baseline and shrink everything else into place.
* 💡 Sorting helps anchor the base and simplifies the logic to loop through and decide who’s too small and who’s too big.
* 💭 If you see constraints involving "difference ≤ K" and need to minimize adjustments, always think: *"Can I sort and build a valid range window?"*

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? → Partially
* [🫠] Did I write code from scratch? → It was confusing af.
* [x] Did I understand why it works? → Yes
* [x] Will I be able to recall this in a week? → Definitely with the greedy pattern logic.

---

### 📚 Related Problems

* [[1647 Minimum Deletions to Make Character Frequencies Unique]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `26`   |
| Total Problems Solved | `357`   |
| Confidence Today      | 😐    |