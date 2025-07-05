## 🧠 Solving LeetCode Until I Become Top 1% — Day `15`

### 🔹 Problem: [3442. Maximum Difference Between Even and Odd Frequency I](https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-i/description/?envType=daily-question&envId=2025-06-10)

**Difficulty:** #Easy
**Tags:** #HashMap #Counting #MinMax

---

### 📝 Problem Summary _(in your own words)_

> Return the maximum difference between the odd and even frequencies of characters in a given string.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This problem is not hard at all and I think if you know some basic data structures like `HashMap` or `Counter` you can solve it in due time. The only issue is finding the maximum difference. Which I think was fairly easy to do. The maximum distance between even and odd frequencies can be found by finding maximum odd frequency and minimum even frequency Because we have to return `odd - even`. So, if we find the maximum odd frequency and minimum even frequency we can just return `max_odd - min_even`._

- **Optimized Strategy:**
  - **Step 1:** Count the frequency of each character in the string using a `Counter`.
  - **Step 2:** Initialize two variables, `max_odd` and `min_even`, to track the maximum odd frequency and minimum even frequency respectively.
  - **Step 3:** Iterate through the frequency counts:
    - If the frequency is odd, update `max_odd` if it's greater than the current value.
    - If the frequency is even, update `min_even` if it's less than the current value.
- **Step 4:** Finally, return the difference `max_odd - min_even`.

- **Algorithm Used:**
  [[Counter]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        max_odd = float('-inf')
        min_even = float('inf')


        for i in c:
            if c[i]%2==0:
                min_even = min(min_even, c[i])
            else:
                max_odd = max(max_odd, c[i])


        return max_odd - min_even
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We traverse the string once to count frequencies and then iterate through the frequency counts, which is at most 26 for lowercase letters.
- **Space:** O(1)
  - We use a constant amount of space for the frequency counts since there are only a limited number of characters (26 lowercase letters).

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - Nothing new, just a simple counting problem using `Counter`.
- 💡 What made this problem tricky?
  - The tricky part was ensuring that we correctly differentiate between odd and even frequencies and handle the edge cases where there might not be any even frequencies.
- 💭 How will I recognize a similar problem in the future?
  - Difference between Min and Max frequencies.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `347` |
| Total Problems Solved | `15`  |
| Confidence Today      | 😃    |
