## 🧠 Solving LeetCode Until I Become Top 1% — Day `X`

### 🔹 Problem: [1432. Max Difference You Can Get From Changing an Integer](https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/?envType=daily-question&envId=2025-06-15)

**Difficulty:** #Medium
**Tags:** #Greedy

---

### 📝 Problem Summary _(in your own words)_

> Given a non-negative integer `num`, the task is to find the maximum difference between two numbers formed by changing the digits of `num`. You can change any digit to any other digit, but you must ensure that the leading digit of the new number is not zero.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _Almost Exactly like the [[2566 Maximum Difference by Remapping a Digit]] problem. But the only difference is that there can be no leading zero in the new number. So, I implemented(copy \* pasted) the previous solution and changed the checking for leading zero to 1. Guess what? It didn't work! The thing is only edge case is that there can be no leading zero but there can be zero after the first digit. So, we need to check for the position of the first digit and also check where there is no zero after the first digit._

- **Optimized Strategy:**
  Sure! Here's the **step-by-step algorithm** written in plain English (no code), focusing entirely on the logical process behind the solution to **Leetcode 1432: Max Difference You Can Get From Changing an Integer**.

---

### 🧠 **Algorithm: Step-by-Step Explanation**

#### ✅ Objective:

From a given integer `num`, create two new integers `a` and `b` by replacing **all occurrences** of **one digit** with **another digit** (twice, separately), such that the **difference between `a` and `b` is maximized**.

- No number can have a **leading zero**
- Result must be a **valid non-zero integer**

---

### ✏️ Step-by-Step Process:

#### 🔹 Step 1: Convert the number to a string

- This allows you to work with individual digits easily.

---

### 🔺 Part A: Create the **maximum number (`a`)**

#### Step 2: Look for the **first digit** from the left that is **not 9**

- If all digits are already 9, there’s no need to change anything — it’s already the largest it can be.

#### Step 3: Replace **all occurrences** of that digit with `9`

- This ensures the resulting number is as large as possible, while changing only one digit value globally.

---

### 🔻 Part B: Create the **minimum number (`b`)**

#### Step 4: Check the **first digit**

- If the first digit is **not 1**, change **all occurrences** of that digit to **1**

  - This makes the number smaller while preserving a valid leading digit (no zero).

#### Step 5: If the first digit **is already 1**:

- Starting from the **second digit**, look for the **first digit** that is **greater than 1**
- Replace **all occurrences** of that digit with **0**

  - This reduces the number further, but avoids putting a 0 at the start (which would be invalid).

---

### ✅ Final Step:

- Convert both modified numbers (`a` and `b`) back to integers.
- Return the **absolute difference** between them.

---

### 🧠 Why This Works:

- It ensures **only one digit** is replaced globally in each transformation (per the rules).
- Maximizes and minimizes using smart digit targeting (`9` and `1` or `0`) without violating **leading zero** constraints.
- Efficient and [[Greedy]] — finds the best possible digits to manipulate.

* **Algorithm Used:**
  [[Greedy]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        t = s[:]
        pos = 0

        while pos < len(s) and s[pos] == '9':
            pos += 1

        s = s if pos == len(s) else s.replace(s[pos],'9')

        pos = 1
        if t[0] != '1':
            t = t.replace(t[0], '1')

        else:
            while pos < len(t) and t[pos] in ['0', '1']:
                pos += 1


            t = t if pos==len(t) else t.replace(t[pos],'0')


        return abs(int(s)-int(t))

```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n), where n is the number of digits in `num`.
  - We traverse the string representation of `num` a few times, but each traversal is linear in terms of the number of digits.
- **Space:** O(n), for storing the string representations of `num`, `s`, and `t`.
  - The space used is proportional to the number of digits in `num`.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The importance of handling leading zeros when transforming digits in a number.
- 💡 What made this problem tricky?
  - Ensuring that the first digit remains valid (not zero) while maximizing or minimizing the number.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems involving digit manipulation, especially those that require maximizing or minimizing values while adhering to constraints like leading zeros.

---

### 🔁 Reflection (Self-Check)

- [✅] Could I solve this without help?
- [✅] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[2566 Maximum Difference by Remapping a Digit]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `20`  |
| Total Problems Solved | `352` |
| Confidence Today      | 😃    |
