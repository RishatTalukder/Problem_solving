## 🧠 Kadane's Algorithm — Note

### 📌 What is it?

Kadane’s Algorithm is a famous **dynamic programming** technique used to find the **maximum sum subarray** in a **1D array of integers** (can include negatives). It runs in **O(n)** time and is one of the most efficient ways to solve this classic problem.

---

### 🧩 Problem It Solves

> “Given an array `arr` of integers (positive, negative, or zero), find the **contiguous subarray** with the **maximum sum**.”

Example:
Input → `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`
Output → `6` from subarray `[4, -1, 2, 1]`

---

### ⚙️ Core Idea

* As you iterate through the array, at each position you ask:

  🧠 *“Is it better to **extend** the previous subarray or **start fresh** from this index?”*

* Maintain two variables:

  * `current_sum` → max subarray sum **ending at current index**
  * `max_sum` → max subarray sum **found so far**

---

### 🪜 Step-by-Step

1. Initialize `current_sum` = `arr[0]`, `max_sum` = `arr[0]`
2. For each element from index 1 to end:

   * Update `current_sum` = `max(arr[i], current_sum + arr[i])`

     * (Start new subarray or extend the old one)
   * Update `max_sum` = `max(max_sum, current_sum)`
3. Return `max_sum`

---

### ⏱️ Time and Space Complexity

* **Time:** O(n) — single pass through array
* **Space:** O(1) — only two variables needed

---

### 💡 When to Use

* Find maximum profit/loss in a stock price difference array
* Longest sum of positive mood swings in psychology data 😅
* Subarrays with the most positive impact, or least damage
* As a base logic in 2D maximum submatrix sum problems

---

### 🔁 Variants

* **Min subarray sum** → Flip signs and apply Kadane
* **Max product subarray** → More complex, but a similar concept
* **Maximum circular subarray sum** → Combine normal and inverted Kadane

---

### 🧠 Memory Tip

> “Kadane keeps track of the past, but only if it’s helpful — otherwise, it starts fresh.”

---

Let me know if you’d like a visual diagram or a code example!
