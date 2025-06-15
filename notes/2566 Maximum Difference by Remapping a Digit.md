## 🧠 Solving LeetCode Until I Become Top 1% — Day `19`

### 🔹 Problem: [2566 Maximum Difference by Remapping a Digit](https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/?envType=daily-question&envId=2025-06-14)

**Difficulty:** #Easy
**Tags:** #Greedy

---

### 📝 Problem Summary _(in your own words)_

> Given a non-negative integer `num`, the task is to find the maximum difference between two numbers formed by remapping the digits of `num`. The remapping allows you to replace any digit with any other digit, but you must ensure that the leading digit of the new number is not zero.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  \_Maybe this problem was my biggest fumble yet. got overconfident and tried to use over engineered solution. I was in the right track to solve the the problem as I was thinking of replacing the digits with the largest and smallest possible digits and I was actually right but my big brain said "why not use a stack?" and I ended up with no solution. This problem is actually brute force and not that hard.

- **Optimized Strategy:**
  _To me, the only edge case was getting the maximum number with the largest digit and what if the first digit is 9, So, we cannot just replace the first digit with 9 and get the largest number. We need to see if the first digit is 9, then we have to move to the next digit and replace it with 9. And for the minimum number, we can just replace the first digit with 0._

  - **Step 1:** Convert the number to a string to easily access each digit.
  - **Step 2:** Create a mapping for the largest digit (9) and the smallest digit (0).
  - **Step 3:** Iterate through the digits:
    - For the maximum number, replace the first non-9 digit with 9 and all other digits with 9.
    - For the minimum number, replace the first digit with 0 and all other digits with 0.
  - **Step 4:** Calculate the difference between the maximum and minimum numbers formed.

- **Algorithm Used:**
  [[greedy]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)

        t = num[:]
        pos = 0
        while pos < len(num) and num[pos] == '9':
            pos += 1

        if pos < len(num):
            num = num.replace(num[pos], '9')

        t = t.replace(t[0], '0')

        return int(num) - int(t)
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We iterate through the digits of the number once to form the maximum and minimum numbers.
- **Space:** O(1)
  - We use a constant amount of space for the string manipulations and do not use any additional data structures that scale with input size.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The importance of carefully considering edge cases, especially with leading digits.
- 💡 What made this problem tricky?
  - The initial overcomplication with using a stack instead of directly manipulating the string representation of the number.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems involving digit manipulation and consider the implications of leading digits.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?


---

### 📚 Related Problems

- [[1432 Max Difference You Can Get From Changing an Integer]]
---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `19`  |
| Total Problems Solved | `351` |
| Confidence Today      | 😐    |
