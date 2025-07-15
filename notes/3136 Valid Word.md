
## 🧠 Solving LeetCode Until I Become Top 1% — Day `44`

### 🔹 Problem: [3136 Valid Word](https://leetcode.com/problems/valid-word/)

**Difficulty:** #Easy
**Tags:** #String, #Validation, #Implementation

---

### 📝 Problem Summary

> Given a string, check if it's a valid "word" based on several conditions:
>
> * It must be at least 3 characters long.
> * It can only contain English letters (a-z, A-Z) and digits (0-9).
> * It must contain **at least one vowel**.
> * It must contain **at least one consonant**.

---

### 🧠 My Thought Process

* **Initial Thoughts:**
  I jumped into it assuming the conditions were just "contains a vowel, consonant, and maybe digit" — and wrote code based on that.
  Spoiler: I didn’t read the question properly.

* **Bug Discovered:**
  My solution failed on `"aya"` — which should be valid, but I thought it wasn’t because I misunderstood the rules.

* **Realization:**
  After carefully re-reading the prompt, I realized I missed **3 critical conditions**:

  * Word length must be ≥ 3
  * Only alphanumeric characters allowed
  * Must contain both vowel & consonant

* **Final Approach:**
  Just iterate over the string, check character types one by one, and track flags for:

  * Is there a vowel?
  * Is there a consonant?
  * Is every character valid?

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = set('aeiouAEIOU')
        has_vowel = False
        has_consonant = False

        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) — single pass through the word
* **Space:** O(1) — only a few flags

---

### 🧩 Key Takeaways

* ✅ Don't assume what the problem is asking — **read every line**.
* 💡 Even an easy string problem can go wrong if you skip rules.
* 💭 In future string validation problems, **always extract rules first** before touching code.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? *(Eventually, after reading properly)*
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week? *(Yes, but I’ll also double check the prompt from now on.)*

---

### 📚 Related Problems

* [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)
* [Strong Password Checker](https://leetcode.com/problems/strong-password-checker/)

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `44`    |
| Total Problems Solved | `385`    |
| Confidence Today      | 😐     |
| Leetcode Rating       | `1572` |
