# 👣 Two Pointer Technique — Note

The **Two Pointer** technique is a common algorithmic strategy used to solve problems involving **linear data structures** like arrays and strings.

### 🧠 Core Idea:

Use **two variables (pointers)** to scan or process the data — either from:

- **Both ends** (left & right), or
- **One end** moving at **different speeds or conditions**

### 🔧 Common Usages:

1. **Sorted Array Problems**

   - Find pair with a given sum
   - Remove duplicates

2. **Sliding Window Problems**

   - Longest/shortest subarray with a condition
   - Maximum sum/minimum length

3. **String Problems**

   - Palindrome checking
   - Compressing characters or comparing substrings

### 🔁 Types of Two Pointer Patterns:

- **Opposite Ends**
  `left = 0, right = n - 1`
  → Useful when shrinking or scanning inward

- **Same Direction**
  `start = 0, end = 0`
  → Used for dynamic window or fast-slow pointer logic

### ✅ Example:

To find if an array has two numbers that sum to a target:

```python
nums = [1, 2, 3, 4, 6]
target = 7
left, right = 0, len(nums) - 1

while left < right:
    s = nums[left] + nums[right]
    if s == target:
        return True
    elif s < target:
        left += 1
    else:
        right -= 1
```

### 📌 Tips:

- Works best on **sorted data**.
- Helps reduce **time complexity** from `O(n²)` to `O(n)`.
- Often paired with **greedy**, **binary search**, or **sliding window**.

---

Let me know if you want me to tailor this for a specific type of problem (like strings or linked lists)!
