## 🧠 Solving LeetCode Until I Become Top 1% — Day `42`

### 🔹 Problem: [3405. Count the Number of Arrays with K Matching Adjacent Elements](https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements)

**Difficulty:** #Hard
**Tags:** #Combinatorics, #Math, #DP

---

### 📝 Problem Summary

> We are given three integers `n`, `m`, and `k`. We must count how many arrays of length `n` we can build such that:
>
> * Every element is from the range `[1, m]`.
> * Exactly `k` adjacent index pairs (i.e., `arr[i-1] == arr[i]`) must be equal.
>   No index can be part of more than one such pair, and the total result must be returned modulo 10⁹+7.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Honestly, my brute force was more like "brute cluelessness." 😵
  I thought: "Okay... just try all possible arrays and check if they satisfy the condition," but with constraints up to 10⁵, this is 100% dead on arrival.

* **Optimized Strategy:**
  Enter: 🧙‍♂️ The Great ChatGPT and his sacred scrolls of combinatorics!

  Here’s how the optimized solution works:

  1. **Choose `k` positions (out of `n-1` adjacent pairs) where elements will be the same.**
     This can be done in `C(n-1, k)` ways.

  2. **Choose the first element of the array** in `m` ways.

  3. **For the remaining `n - 1 - k` positions**, you must pick a different value than the previous — so for each of these, you have `m - 1` choices.

  Final formula:
  `ways = C(n - 1, k) * m * (m - 1)^(n - 1 - k)`

* **Algorithm Used:**
  `Modular Combinatorics`, `Fast Exponentiation`, `Math`

---

### ⚙️ Code Implementation (Python)

```python
MOD = 10**9 + 7
MAX = 10**5 + 10  # Safety margin for n up to 1e5

# Precompute factorials and inverse factorials
fact = [1] * MAX
inv_fact = [1] * MAX

for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD

# Inverse of factorial using Fermat's Little Theorem
inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, -1, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

def comb_mod(n, k):
    if k < 0 or k > n:
        return 0
    return fact[n] * inv_fact[k] % MOD * inv_fact[n - k] % MOD

class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        return comb_mod(n - 1, k) * m % MOD * pow(m - 1, n - 1 - k, MOD) % MOD

```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n) for precomputing factorials and inverse using built-ins
* **Space:** O(1) if using Python’s built-in factorials (else O(n) if you precompute them)

---

### 🧩 Key Takeaways

* ✅ Learned how to count combinations modulo a prime using `math.factorial` + modular inverse.
* 💡 The trickiest part was understanding the separation of adjacent equal-pair placements from distinct ones.
* 💭 If a problem says “exactly K adjacent matches,” chances are, it's asking for clever combinatorics, not brute force.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? — *Nope, needed help.*
* [ ] Did I write code from scratch? — *Partially, modified a solution I found.*
* [x] Did I understand why it works? — *Yes, after breaking it down.*
* [x] Will I be able to recall this in a week? — *Yes, especially with the pattern in mind.*

---

### 📚 Related Problems

* [[1922 Count Good Numbers]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `22`  |
| Total Problems Solved | `354`   |
| Confidence Today      | 😐    |
