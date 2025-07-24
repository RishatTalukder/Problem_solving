## 🧠 Solving LeetCode Until I Become Top 1% — Day `53`

### 🔹 Problem: [2135 Count Words Obtained After Adding a Letter](https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/)

**Difficulty:** #Medium
**Tags:** #BitMsk, #Hashing, #Set, #Strings

---

### 📝 Problem Summary

You're given two lists of unique words: `startWords` and `targetWords`.

You can transform a word from `startWords` into a `targetWord` by:

- Adding **exactly one** letter anywhere in the word.
- Then rearranging the resulting word.

You need to return the number of `targetWords` that can be obtained this way from any `startWord`.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  Try all possible pairs between `startWords` and `targetWords`. For each, add one character to `startWord`, sort, and check if it matches a `targetWord`.
  → **Too slow**. Time complexity is O(N \* M \* log L).

- **Optimized Strategy:**
  Use **bitmasking** to represent character presence in each word:

  - Convert each `startWord` into a bitmask and store it in a set.
  - For each `targetWord`, remove each letter one at a time and check if the resulting bitmask exists in the set.

  Intuition: Instead of trying to go from `startWord` → `targetWord`, we reverse the process. We check if removing one letter from `targetWord` gives us a `startWord`.

- **Algorithm Used:**
  [[Bit_Masking]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def wordToMask(self, word: str) -> int:
        mask = 0
        for ch in word:
            mask |= 1 << (ord(ch) - ord('a'))
        return mask

    def wordCount(self, startWords, targetWords) -> int:
        start_set = set()

        # Step 1: Convert all startWords to bitmask and store
        for word in startWords:
            mask = self.wordToMask(word)
            start_set.add(mask)

        count = 0

        # Step 2: For each targetWord, remove each letter and check
        for word in targetWords:
            target_mask = self.wordToMask(word)
            for ch in word:
                bit = 1 << (ord(ch) - ord('a'))
                reduced_mask = target_mask ^ bit  # remove one bit
                if reduced_mask in start_set:
                    count += 1
                    break  # only count once per word

        return count
```

---

### ⏱️ Time & Space Complexity

- **Time:**

  - O(N \* L + M \* L) where:

    - N = len(startWords)
    - M = len(targetWords)
    - L = max length of words (<= 26)

- **Space:** O(N) — to store the bitmasks of `startWords` in a set

---

### 🧩 Key Takeaways

- ✅ Learned how to use **bitmasking** to represent character sets in a string.
- 💡 Reversing the process (removing a letter from the target) can sometimes simplify the problem.
- 🔍 XOR (`^`) is a clean and safe way to toggle bits — better than subtraction in bitmask logic.

---

### 🔁 Reflection (Self-Check)

- [x] Could I solve this without help? _(Eventually, yes)_
- [x] Did I write code from scratch?
- [x] Did I understand why it works?
- [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[1717 Maximum Score From Removing Substrings]]
- [[1638 Count Substrings That Differ by One Character]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `53`    |
| Total Problems Solved | `394`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |

