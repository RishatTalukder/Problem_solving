## 🧠 Solving LeetCode Until I Become Top 1% — Day `12`

### 🔹 Problem: [3170 Lexicographically Minimum String After Removing Stars](https://leetcode.com/problems/lexicographically-minimum-string-after-removing-stars/description/?envType=daily-question&envId=2025-06-07)

**Difficulty:** #Medium
**Tags:** #Greedy #Stack #HashMap #Heap

---

### 📝 Problem Summary _(in your own words)_

> Find the smallest lexicographical string after removing the smallest character in leftmost position for each `*` in the string. The `*` can be thought of as a wildcard that removes the character to its left.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _Well It wasn't that hard to figure out the whole solution for me, because this problem is pretty similar to [[1061 Lexicographically Smallest Equivalent String]]. We can use the same approach to solve this prblem too._

- **Optimized Strategy:**
  _We can keep track of the charaters using a hashmap and a stack. We can iterate through the string and for each character, we check if it is a `*`. If it is, we pop the smallest character from the stack. This means we have to sort the stack the array but if we update the stack while iterating through the string we might just increase the time complexity to O(n^2). So, it's a very common approach to use a `heap` or a `priority queue` to keep track of the smallest character in the stack. On the other hand, there can be multiple characters with the same value, So, instead of counting we can just store the indeces of the characters in the hashmap and then pop the smallest index from the stack when we encounter a `*`._

  1. **Initialize Structures:**

  - `heap`: A **min-heap** to always get the smallest character seen so far.
  - `hashmap`: A **defaultdict of deques** to track the **indices** of each character.
  - `keep`: A boolean list of length `n` initialized to `True` (keep everything initially).

  2. **Traverse the String (`s`):**
     For each index `i` in `s`:

  - **If the character is `'*'`:**

    1. Pop the **smallest character** from the min-heap.
    2. Get the **last occurrence index** of that character from `hashmap[char]`.
    3. Set `keep[i] = False` → remove the `'*'`.
    4. Set `keep[idx] = False` → remove the corresponding smallest character.

  - **If the character is a letter:**

    1. Push it into the **min-heap**.
    2. Append its index to `hashmap[char]`.

  3. **Build Final Result:**

  - Iterate over all indices.
  - For every index where `keep[i]` is `True`, include `s[i]` in the result.

  4. **Return the final string.**

- **Algorithm Used:**
  [[Greedy]] [[heap]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        heap = []
        hashmap = defaultdict(deque)
        keep = [True] * n
        for i in range(n):
            if s[i] == '*':
                smallest = heaheap.heappop(heap)
                idx = hashmap[smallest].pop()
                keep[i] = False
                keep[idx] = False
            else:
                heapq.heappush(heap, s[i])
                hashmap[s[i]].append(i)

        return ''.join(s[i] for i in range(n) if keep[i])
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n log n)
  - We iterate through the string once, and each character insertion/removal from the heap takes O(log n).
- **Space:** O(n)
  - We store the indices of characters in the hashmap and the heap.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - Well I learned new techniques called `boolean masking/flag array` to keep track array after operations like removing elements, also why should understand where to count and where to just keep track of indices.
- 💡 What made this problem tricky?
  - Nothing really, it was pretty easy.
- 💭 How will I recognize a similar problem in the future?
  - If I have to remove elements from an array based on some condition, I can use this greedy priority queue approach.

---

### 🔁 Reflection (Self-Check)

- [😊] Could I solve this without help?
- [🤔] Did I write code from scratch?
- [🫰] Did I understand why it works?
- [🫰] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `12`  |
| Total Problems Solved | `347` |
| Confidence Today      | 😃    |
