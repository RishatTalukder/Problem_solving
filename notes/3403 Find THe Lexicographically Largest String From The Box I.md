## 🧠 Solving LeetCode Until I Become Top 1% — Day `9`

### 🔹 Problem: [3403 Find The Lexicographically Largest String From The Box I](https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/description/?envType=daily-question&envId=2025-06-04)

**Difficulty:** #Medium
**Tags:** #Greedy #TwoPointer

---

### 📝 Problem Summary _(in your own words)_

> I hate anything that has the word "lexicographically" in it. It alwasy makes me feel like I have no Idea what I'm doing. But here we are. The problem is asking us to find the [[theories/lexicographically_largest_string]] from a given string `s` if we split it into `numFriends` parts. Confused yet?

---

### 🧠 My Thought Process

- **Optimized Strategy:**
  _This problem has nothing to do with lexicography. We just need to find the largest possible substring with the largest `order` of characters. A charecter with a higher `order` is considered lexicographically larger. So, `b` is larger than `a`, `c` is larger than `b`, and so on._

  - This of it like this:
    - If we have a string with 6 charecters and we need to split it into 2 parts, The maximum possible substring length we can have is 5 and minimum is 1.
    - But here's is the catch, even if the smaller substring is smaller than the larger one, It can still be lexicographically larger if it has a higher order character.
    - So, we just need to find the largest character in the string and try to take the largest possible substring that starts with that character.

- **Algorithm Used:**
  [[Two_Pointer]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        r = n-numFriends+1
        max_char = max(word)
        ans = ''
        for l in range(n):
            if word[l] == max_char:
                sub = word[l:l+r]
                ans = max(ans, sub)
        return ans
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n^2)
  - We iterate through the string and for each character, we check the substring of length `r` starting from that character. But average case is O(n) because we only check the substring if the character is the maximum character in the string.
- **Space:** O(n)
  - The space complexity is O(n) because we store the maximum substring in the `ans` variable.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?

  - Greedy approach is not that bad after all.

- 💡 What made this problem tricky?
  - The word "lexicographically" made it sound more complex than it is. It's just about finding the largest substring starting with the largest character.
- 💭 How will I recognize a similar problem in the future?
  - Look for problems that wants me to split a string into parts and find the largest substring with constraints.

---

### 🔁 Reflection (Self-Check)

- [🫰] Could I solve this without help?
- [😐] Did I write code from scratch?
- [✅] Did I understand why it works?
- [😊] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[notes/1163 Last Substring in Lexicographical Order]]
- [[notes/1718 Construct the Lexicographically Largest Valid Sequence]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `9`   |
| Total Problems Solved | `344` |
| Confidence Today      | 😃    |
