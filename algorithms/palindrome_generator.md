# 🧾 Note: Creating Palindromes (Digit-wise Construction)

### 🔍 What is a Palindrome?

A **palindrome** is a number (or string) that reads the same forward and backward.

Examples:

* Palindromic numbers: `121`, `1221`, `7`
* Palindromic strings: `"racecar"`, `"abba"`

---

### 🧠 Why Create Palindromes Digit-by-Digit?

Instead of checking every number and testing if it's a palindrome (which is slow), we can **construct** palindromes directly. This is useful when:

* We want to generate all palindromes of a certain size.
* We're optimizing for problems involving symmetry or numerical constraints.
* We want to avoid TLE in brute-force palindrome checking.

---

### 🧩 Core Idea

1. Start with a number (e.g., `123`)
2. Reflect its digits in reverse to create:

   * **Odd-length palindrome** → `12321`
   * **Even-length palindrome** → `123321`
3. Append digits in reverse to the original (skip last digit for odd).

---

### ⚙️ Code: Palindrome Generator in Python

```python
def create_palindrome(num: int, odd: bool) -> int:
    """
    Generate a palindrome from the given number.
    
    Args:
        num: The base prefix (e.g., 123)
        odd: Whether to generate an odd-length palindrome
    
    Returns:
        A full palindromic integer
    """
    result = num
    x = num // 10 if odd else num

    while x > 0:
        result = result * 10 + x % 10
        x //= 10

    return result
```

---

### 🧪 Examples

```python
create_palindrome(123, True)   # ➞ 12321
create_palindrome(123, False)  # ➞ 123321
create_palindrome(7, True)     # ➞ 7
```

---

### 🔁 Time Complexity

* `O(d)` where `d` is the number of digits in `num`, because we process each digit once while mirroring.

---

### 💡 Use Cases

* Generate all palindromes of a given length
* LeetCode problems like:

  * [2081. K Mirror Numbers](https://leetcode.com/problems/k-mirror-numbers/)
  * [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
* Numerical puzzles, string symmetry analysis, palindromic prime problems
