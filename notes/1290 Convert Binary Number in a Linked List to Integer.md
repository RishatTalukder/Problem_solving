## 🧠 Solving LeetCode Until I Become Top 1% — Day `43`

### 🔹 Problem: [1290. Convert Binary Number in a Linked List to Integer](https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/)

**Difficulty:** #Easy
**Tags:** #LinkedList, #Math, #BitManipulation

---

### 📝 Problem Summary

You’re given the head of a singly linked list where each node contains either a `0` or a `1`, and the entire linked list represents a **binary number** (most significant bit comes first).

Your task is to convert that binary number to its decimal (base 10) form and return it as an integer.

---

### 🧠 My Thought Process

- **Brute Force Idea:**

  - Traverse the linked list and append each bit to a string.
  - After the traversal, use Python's built-in `int(binary_string, 2)` to convert it.

- **Optimized Strategy:**

  - Although string-building is simple, we could optimize space by keeping a running integer.
  - For every bit `b`, left-shift the current result (`res = res * 2 + b`).

  But for now, the string approach is fast and clear, especially for small constraints.

- **Algorithm Used:**
  Basic linked list traversal and binary string conversion.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        s = ''
        while head:
            s += str(head.val)
            head = head.next
        return int(s, 2)
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n) — one traversal through the list
- **Space:** O(n) — string `s` stores n bits

> ⚠️ This could be optimized to O(1) space by using integer shifting instead of a string.

---

### 🧩 Key Takeaways

- ✅ I practiced converting binary to decimal using both string manipulation and bit math.
- 💡 It's okay to start with readable solutions first, then optimize if necessary.
- 💭 Bit manipulation and linked list problems often come together — be prepared for that combo.

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
| Day                   | `43`   |
| Total Problems Solved | `384`  |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
