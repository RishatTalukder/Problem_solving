# 🧾 Note: Palindrome Checker (Base-agnostic)

### 🔍 What is a Palindrome?

A **palindrome** is a value (number or string) that reads the same forward and backward.

Examples:

* Palindromic numbers: `121`, `12321`, `7`
* Palindromic strings: `"madam"`, `"racecar"`

---

### 🧠 What Does a Palindrome Checker Do?

It checks whether a given number (or string) is a palindrome — **digit by digit** for numbers, or **character by character** for strings.

You can also check **numeric palindromes in different bases**, which is often useful in competitive programming and problems like k-mirror numbers.

---

### ⚙️ Code: Palindrome Checker in Base `k` (for numbers)

```python
def is_palindrome(num: int, base: int = 10) -> bool:
    """
    Check if a number is a palindrome in the given base.
    
    Args:
        num: The number to check
        base: The numeric base (e.g., base 10, base 2)
        
    Returns:
        True if the number is a palindrome in the given base
    """
    digits = []
    while num > 0:
        digits.append(num % base)
        num //= base
    return digits == digits[::-1]
```

---

### 🧪 Examples

```python
is_palindrome(121, 10)      # ➞ True (121 in base 10 is a palindrome)
is_palindrome(585, 2)       # ➞ True (585 in binary is 1001001001)
is_palindrome(123, 10)      # ➞ False
```

---

### ⚠️ Note on Edge Cases

* `0` is a palindrome in any base.
* Negative numbers are **not** considered palindromes.
* Leading zeroes don't affect the logic here, because digits are extracted mathematically.

---

### 🔁 Time Complexity

* `O(d)` where `d` is the number of digits in `num` (base-dependent).
* Memory: `O(d)` for storing digits.

---

### 💡 Use Cases

* Base-k palindrome checks (e.g., [Leetcode 2081 – K Mirror Numbers](https://leetcode.com/problems/k-mirror-numbers/))
* Binary palindrome problems
* Validating symmetry in numeric puzzles
