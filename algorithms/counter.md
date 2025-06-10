# 🧮 Counter Algorithms in Python

## 🔍 What is a Counter?

A **Counter** is a special type of dictionary from Python's `collections` module that is used to **count the frequency of elements** in a list, string, or any iterable.

It helps solve many common algorithm problems like:

* Finding the most common element
* Counting characters or words
* Checking if two strings are anagrams
* Frequency-based filtering or sorting

---

## 🧱 Syntax

```python
from collections import Counter

# Example with a list
nums = [1, 2, 2, 3, 1, 4, 2]
count = Counter(nums)
print(count)
# Output: Counter({2: 3, 1: 2, 3: 1, 4: 1})
```

---

## 🧠 Why is it Useful?

Counter-based algorithms are used to:

* Count **how many times** each element appears
* Access the **most common elements**
* Perform **set operations** (like intersection or subtraction of frequencies)

---

## 🎯 Real Problem Examples

### 1. **Find the Most Frequent Element**

```python
nums = [1, 3, 2, 1, 4, 3, 1]
count = Counter(nums)
most_common = count.most_common(1)[0][0]
print(most_common)  # Output: 1
```

### 2. **Check if Two Strings are Anagrams**

```python
def is_anagram(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_anagram("listen", "silent"))  # Output: True
```

### 3. **Filter Elements That Appear More Than Once**

```python
nums = [4, 4, 5, 6, 4, 5]
count = Counter(nums)
duplicates = [num for num, freq in count.items() if freq > 1]
print(duplicates)  # Output: [4, 5]
```

---

## 🧩 Bonus Tricks

* `count.elements()` returns an iterator over the original elements
* `count.subtract(other_counter)` subtracts counts
* `count + other_counter` adds frequencies from both

---

## 💡 Common Interview Tasks

* Frequency sort problems
* Majority element problems
* Group anagrams
* Character frequency in strings

---

## ✅ Summary

| Operation                    | Code Example             |
| ---------------------------- | ------------------------ |
| Count elements               | `Counter(data)`          |
| Get frequency of element `x` | `count[x]`               |
| Most common                  | `count.most_common(n)`   |
| Convert back to list         | `list(count.elements())` |