## 🧠 Solving LeetCode Until I Become Top 1% — Day `52`

### 🔹 Problem: [Maximum Score From Removing Substrings](https://leetcode.com/problems/maximum-score-from-removing-substrings/)

**Difficulty:** #Medium
**Tags:** #Greedy, #String, #Stack

---

### 📝 Problem Summary

You're given a string `s` made up of lowercase letters, and two integers `x` and `y`:

* You can remove **one occurrence** of the substring `"ab"` and earn `x` points.
* You can remove **one occurrence** of the substring `"ba"` and earn `y` points.

You can perform these operations **as many times as you like, in any order**.
Your goal is to **maximize the total score**.

---

### 🧠 My Thought Process

#### ❓ What's the challenge?

Order **matters**. For example, suppose:

* `s = "abba"`
* `x = 5` (value of "ab")
* `y = 10` (value of "ba")

Now depending on which pair you remove first, the remaining characters can change:

* If you remove `"ab"` first, you're left with `"ba"`, giving total `5 + 10 = 15`.
* If you remove `"ba"` first, you're left with `"ab"`, also `10 + 5 = 15`.

But it’s not always equal. Some strings block optimal operations if you do them in the wrong order.

---

#### 🔍 Greedy Observation:

We must **remove the higher scoring substring first**, otherwise we might "waste" the opportunity to gain more points.

✅ So the plan is:

* Always remove the more **valuable** pair first.
* Then remove the remaining possible pairs of the other type.

---

#### ✂️ Trick for Simplifying:

Since we're dealing with **"ab"** and **"ba"**, both pairs involve just `'a'` and `'b'`.
We’ll simulate removal using a greedy pass through the string.

Let’s say:

* `"ab"` has **higher value**, so we process left to right and greedily remove all `"ab"` we can.
* Then process the leftovers and greedily remove `"ba"`.

But instead of writing **two passes**, we flip the string if `"ba"` is more valuable than `"ab"`, and always remove `"ab"` in one pass.

---

### 🪄 Why This Works:

We use two counters: `a_count` and `b_count` to keep track of how many unmatched `'a'` or `'b'` characters are waiting to form a valid pair.

When we hit a character:

* If it matches the **second character** of a potential pair, and we have a matching **first character** stored, we remove the pair and add the score.
* If not, we just increase the counter.

Whenever we hit a character **other than 'a' or 'b'**, it acts as a **barrier** (`c`, `d`, etc.), so we finalize any remaining opposite pairs from `a_count` and `b_count` into `"ba"`.

---

### ⚙️ Final Code (Python)

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Always remove higher-value pair ("ab" or "ba") first
        if x < y:
            x, y = y, x
            s = s[::-1]  # Flip string so we can still remove "ab" first

        a_count = 0  # number of 'a's waiting for 'b'
        b_count = 0  # number of 'b's waiting for 'a'
        result = 0

        for char in s:
            if char == 'a':
                a_count += 1
            elif char == 'b':
                if a_count > 0:
                    a_count -= 1
                    result += x  # remove "ab" pair
                else:
                    b_count += 1
            else:
                # If we hit any non a/b character, try to clean up "ba" pairs
                result += min(a_count, b_count) * y
                a_count = 0
                b_count = 0

        # Clean up remaining unmatched pairs at the end
        result += min(a_count, b_count) * y
        return result
```

---

### ⏱️ Time & Space Complexity

* **Time Complexity:** `O(n)`
  We loop through the string only once.

* **Space Complexity:** `O(1)`
  No extra memory besides a few counters.

---

### 🧩 Key Takeaways

* ✅ **Greedy first** if order matters and values differ.
* 💡 Reversing the string can **unify logic** instead of duplicating code.
* 🔄 Remember to **reset state** when encountering "barrier" characters.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[2135 Count Words Obtained After Adding a Letter]]

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `52`    |
| Total Problems Solved | `393`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
