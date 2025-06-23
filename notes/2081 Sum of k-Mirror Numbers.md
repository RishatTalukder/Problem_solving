## 🧠 Solving LeetCode Until I Become Top 1% — Day `28`

### 🔹 Problem: [2081 K Mirror Numbers](https://leetcode.com/problems/k-mirror-numbers/)

**Difficulty:** Hard
**Tags:** #Palindrome, #BaseConversion, #Math, #BruteForce

---

### 📝 Problem Summary 

> Given two integers `k` and `n`, you are to find the sum of the first `n` positive integers that are palindromes in **both base 10 and base k**.
> A number is considered **k-mirror** if:
>
> * It's a palindrome in **base 10** (normal decimal), and
> * It's a palindrome in **base k**.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * Check every number starting from 1,
  * See if it's a palindrome in both base 10 and base k.
  * Keep going until I find `n` such numbers.
  * This idea is simple, but **extremely slow** and will TLE for large `n`.

* **What I Figured Out:**

  * I realized that we should generate **palindromes only** in base 10 and check if they’re also palindromes in base `k`.
  * This eliminates checking non-palindromic candidates, which saves a lot of time.
  * I also figured that we can build palindromes from half of the number (like how we do with 121, 12321 etc.).
  * But implementing this properly and avoiding edge case chaos (like odd vs even length, and prefix logic) overwhelmed me.
  * So yeah... **I chickened out and looked up the solution.**

---

### ✅ Optimal Solution (Palindrome Generator + Base Conversion)

#### 🪄 Core Idea:

Only generate numbers that are palindromes **in base 10**, and for each of them, check if they’re also palindromes in base `k`.

#### 💡 Steps:

1. **Generate palindromes in base 10 efficiently**:

   * Use a helper function `createPalindrome(num, odd)` that mirrors the digits of `num` to make a full palindrome.

     * If `odd=True`, make odd-length palindromes (like 121, 12321).
     * If `odd=False`, make even-length palindromes (like 1221, 123321).
2. **For each palindrome**, check if it’s also a palindrome in base `k`:

   * Convert to base `k` digit-wise and check if the list of digits is symmetric.
3. Keep doing this until you’ve found `n` such numbers. Sum them up and return.

#### ✨ Why this works:

* Palindromes are symmetric, and generating only base-10 palindromes **prunes the search space massively**.
* Instead of checking all integers, we explore just the ones that could possibly work.
* The generation is done in increasing order, so the smallest `n` k-mirror numbers are found.


**Algorithm Used:**
  [[palindrome_generator]] [[palindrome_checker]] [[base_conversion]]

---



### ⚙️ Code Implementation (Python)

```python
class Solution:
    def createPalindrome(self, num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    def isPalindrome(self, num: int, base: int) -> bool:
        digits = []
        while num > 0:
            digits.append(num % base)
            num //= base
        return digits == digits[::-1]

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            # Try all odd-length palindromes
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            # Try all even-length palindromes
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                if self.isPalindrome(p, k):
                    total += p
                    n -= 1
            length *= 10
        return total
```

---

### ⏱️ Time & Space Complexity

* **Time:** Depends on `n` and the base `k`. Practically efficient because we generate palindromes and not all integers. Still exponential in worst case.
* **Space:** O(log n) for digit storage during base conversion.

---

### 🧩 Key Takeaways

* ✅ Generating only valid candidates first (here: palindromes) **significantly improves performance**.
* 💡 A great example of **base conversion + symmetry checks**.
* 💭 Sometimes it's best to **invert the problem**: generate what you want instead of filtering from the whole space.

---

### 🔁 Reflection (Self-Check)

* [ ] Could I solve this without help? → Almost. Knew the direction, but not the implementation.
* [x] Did I write code from scratch? → With help from the official logic.
* [x] Did I understand why it works? → Yes
* [x] Will I be able to recall this in a week? → Yes, now that I know the palindrome generation trick.

---

### 📚 Related Problems

* [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
* [564. Find the Closest Palindrome](https://leetcode.com/problems/find-the-closest-palindrome/)
* [233. Number of Digit One](https://leetcode.com/problems/number-of-digit-one/)

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `X`   |
| Total Problems Solved | `Y`   |
| Confidence Today      | 😐    |

---

Let me know if you’d like a visual flowchart of how palindrome generation works or a Markdown export!
