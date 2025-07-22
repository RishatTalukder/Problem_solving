# 📍3. Longest Substring Without Repeating Characters

* 💡 Difficulty: Medium
* 🧩 Tags: #TwoPointers #SlidingWindow #HashSet
* 🔄 Pattern: Sliding Window
* 🔍 Link: [LeetCode Link](https://leetcode.com/problems/longest-substring-without-repeating-characters)

---

## 🧠 Problem Summary

Given a string `s`, find the length of the **longest substring** without repeating characters.

---

## 🚫 Brute Force Approach

Try all substrings and check if they contain duplicate characters. This takes **O(n³)** because:

* Generating all substrings takes O(n²)
* Checking each for uniqueness takes O(n)

Too slow for large inputs.

---

## ✅ Optimal Solution (Sliding Window)

* Maintain a sliding window `[left, right)` with unique characters.
* Use a set to track characters inside the current window.
* Expand `right` as long as no duplicates.
* If a duplicate appears, shrink `left` until it's removed.
* At every step, update the maximum length as `right - left`.

---

## 📦 Code (Python)

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        dup = set()
        left = 0
        right = 0

        while right < len(s):
            if s[right] not in dup:
                dup.add(s[right])
                right += 1
            else:
                dup.remove(s[left])
                left += 1
            res = max(res, right - left)

        return res
```

---

## 📊 Complexity

* **Time:** O(n) — each character is visited at most twice.
* **Space:** O(min(n, m)) — where `m` is the size of the character set (e.g., 26 for lowercase letters, 128 for ASCII).

---

## 📝 Notes

* ✅ Learned how to maintain a window of unique characters using a set.
* 💡 The trick is to **only remove one char at a time** from the left when you hit a duplicate.
* 💭 Very similar to problems involving longest subarray with unique properties — this is a base pattern to memorize.
