# 📍 1647. Minimum Deletions to Make Character Frequencies Unique

* 💡 Difficulty: Medium
* 🧩 Tags: #Greedy #HashTable #Sorting
* 🔄 Pattern: Greedy Adjustment
* 🔍 Link: [LeetCode Link](https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/)

---

## 🧠 Problem Summary

You’re given a string `s`. The goal is to delete the **minimum number of characters** so that **no two characters in the string have the same frequency**. You must return the **minimum number of deletions** required.

---

## 🚫 Brute Force Approach

Try deleting every possible combination of characters and check if the resulting frequencies are unique. This is computationally infeasible as it grows exponentially (`O(2^N)`), making it unusable for longer strings.

---

## ✅ Optimal Solution

### 🧠 Greedy Strategy (Core Insight):

To avoid duplicate frequencies, we want to make sure each frequency is **strictly less** than the next one when sorted in descending order.

### 🔢 Steps:

1. Count the frequency of each character.
2. Sort the frequency list in **ascending order**.
3. Iterate **backwards** through the list (from high to low frequencies):

   * If `freq[i] >= freq[i+1]`, reduce `freq[i]` until it's `< freq[i+1]` or 0.
   * Track how many deletions this took.
4. Return the total deletions.

This works because we only reduce frequencies when they’re not unique, and we always reduce just enough — a perfect greedy fit.

---

## 📦 Code (Python)

```python
from typing import List

class Solution:
    def minDeletions(self, s: str) -> int:
        freq = [0] * 26  # Frequency for 'a' to 'z'

        for c in s:
            freq[ord(c) - ord('a')] += 1

        freq.sort()
        deletions = 0

        for i in range(24, -1, -1):
            if freq[i] == 0:
                break

            if freq[i] >= freq[i + 1]:
                prev = freq[i]
                freq[i] = max(0, freq[i + 1] - 1)
                deletions += prev - freq[i]

        return deletions
```

---

## 📊 Complexity

* **Time:** `O(N + K log K)`

  * Counting takes `O(N)`
  * Sorting 26 characters takes `O(K log K)` (constant time)
* **Space:** `O(1)` — Only 26 fixed-size array for frequency

---

## 📝 Notes

* 🔥 The greedy reduction step is the key. If a frequency collides with the next, reduce it just enough to be smaller.
* 🔁 Going **backwards** ensures the higher frequencies don’t get blocked by smaller ones.
* 🧠 I got stuck trying to "balance" frequencies before thinking of strict reduction. Once I realized this is about *ordering*, not value optimization, it clicked.

---

Let me know if you'd like this exported in Markdown or turned into a `daily.dev` post!
