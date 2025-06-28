## 🧠 Solving LeetCode Until I Become Top 1% — Day `11`

### 🔹 Problem: [2434. Using a Robot to Print the Lexicographically Smallest String](https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/description/?envType=daily-question&envId=2025-06-06)

**Difficulty:** #Medium
**Tags:** #Greedy #Stack #HashMap

---

### 📝 Problem Summary

> Find the lexicographically smallest string that can be formed by using a robot that can do the following operations:

1. Add a character to a stack `t` from the front of a string `s`.
2. Remove the top character from the stack `t` and append it to the result string `res`.

---n

### 🧠 My Thought Process

- **Brute Force Idea:**
  _I was kinda close while thinking about the solution. And I actually thought of a greedy approach which is a little bit complex than the real solution. What can I say I'm still learning._

- **Optimized Strategy:**
  _The main trick is to keep track of the next smallest possible character that can be added to the stack `t` while ensuring that the characters in `t` are in lexicographical order._

  - Use a stack to build the result string.
  - Set the min character to 'a' initially.
  - Make a frequency map of characters in `s` to know how many characters are left to process.
  - Iterate through the string `s` and for each character and add it to the stack if and update the frequency map.
  - Now check if the prev min character count is Zero or not, if it is zero then we set the min character to the next smallest character in the alphabet.
  - Now we can check if the last character in the stack is lexicographically smaller than the current min character and if it is then we can pop the last character from the stack and append it to the result string.

- **Algorithm Used:**
  [[Greedy]]

---

### ⚙️ Code Implementation (Python)

```python
from collections import deque
from collections import Counter
class Solution:
    def robotWithString(self, s: str) -> str:
        s = deque(s)
        c = Counter(s)
        res = []
        stack = []
        min_char = 'a'


        for ch in s:
            stack.append(ch)
            c[ch] -= 1

            while c[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            while stack and stack[-1] <= min_char:
                res.append(stack.pop())

        return ''.join(res)
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n), where n is the length of the string `s`. Each character is processed once.
- **Space:** O(n), for the stack and the result string.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - Greedy decision-making in with stacks.
- 💡 What made this problem tricky?
  - The challenge was to maintain the lexicographical order while efficiently managing the stack and the frequency of characters.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems involving stacks and lexicographical order, especially those that require maintaining a sorted order while processing characters.

---

### 🔁 Reflection (Self-Check)

- [🫠] Could I solve this without help?
- [🫠] Did I write code from scratch?
- [✅] Did I understand why it works?
- [✅] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `11`  |
| Total Problems Solved | `346` |
| Confidence Today      | 😐    |
