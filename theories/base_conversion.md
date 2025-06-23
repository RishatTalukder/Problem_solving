# 🧾 Note: Base Conversion in Python

### 🔍 What is Base Conversion?

**Base conversion** is the process of changing a number from one base (radix) to another.

Common bases include:

* **Base 10** (Decimal) – what we usually use
* **Base 2** (Binary)
* **Base 8** (Octal)
* **Base 16** (Hexadecimal)

---

### 🔁 Why Use Base Conversion?

* Problems like [**k-mirror numbers**](https://leetcode.com/problems/k-mirror-numbers/)
* Checking **binary palindromes**
* Encoding/decoding numbers
* Understanding bit-level operations

---

### 🧠 Python Functions for Base Conversion

#### 🔹 1. Convert Decimal to Base `k` (as a list of digits)

```python
def to_base_k(n: int, k: int) -> list[int]:
    """Convert a decimal number to base-k and return list of digits."""
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % k)
        n //= k
    return digits[::-1]  # Reversed for most-significant-digit first
```

**Example:**

```python
to_base_k(31, 2)  # ➞ [1, 1, 1, 1, 1]
to_base_k(255, 16)  # ➞ [15, 15]
```

---

#### 🔹 2. Convert Base `k` to Decimal

```python
def from_base_k(digits: list[int], k: int) -> int:
    """Convert a list of base-k digits to a decimal number."""
    num = 0
    for digit in digits:
        num = num * k + digit
    return num
```

**Example:**

```python
from_base_k([1, 0, 1, 1], 2)  # ➞ 11
from_base_k([15, 15], 16)    # ➞ 255
```

---

### 🧩 Built-in Functions

Python also provides some quick tools for common bases:

```python
bin(10)     # '0b1010'      → Binary
oct(10)     # '0o12'        → Octal
hex(10)     # '0xa'         → Hexadecimal

int('1010', 2)  # 10        → Parse binary to int
int('a', 16)    # 10        → Parse hex to int
```

---

### 💡 Tips

* Always check for **leading zeros** when dealing with strings.
* Use `int(str, base)` to parse numbers from other bases.
* Be careful with digit representation beyond 9 (`10 → 'a'` in hex).

---

### 🧠 Complexity

* Conversion takes **O(logₖ n)** time (based on the number of digits).
* Space is also **O(logₖ n)** if storing digits.

---

### ✅ Use Cases in LeetCode

* `K-Mirror Numbers`
* `Palindrome in Base`
* `Base-7`, `Base-2`, `Base-16` conversion questions
