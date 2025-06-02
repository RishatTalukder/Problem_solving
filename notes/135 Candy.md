## 🧠 Solving LeetCode Until I Become Top 1% — Day `7`

### 🔹 Problem: [https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2025-06-02](https://leetcode.com/problems/candy/description/?envType=daily-question&envId=2025-06-02)

**Difficulty:** #Hard
**Tags:** #Greedy #TwoPassGreedy

---

### 📝 Problem Summary

> Finding out the minimum number of candies to distribute to children based on their ratings, ensuring that each child with a higher rating than their neighbor gets more candies.

---

### 🧠 My Thought Process

- **Brute Force Idea:**
  _This problem is maybe the easiest `HARD` problem I have ever solved. I didnt realize first but the bruteforce idea I had was actually the optimal solution. I was always weak at greedy problems, but this one was straightforward._

- **Optimized Strategy:**
  _It's a two-pass greedy algorithm. As, the minimum candies a child could have is 1, we can start by giving each child 1 candy._

  - **First Pass:** We can now iterate from `left to right`, and if the current child's `rating` is greater than the previous child's rating, we give them one more candy than the previous child.
  - **Second Pass:** Then we iterate from `right to left`, and if the current child's `rating` is greater than the next child's rating, we ensure they have more candies than the next child. We take the `maximum` of the current candies and the required candies to ensure the condition is met.

- **Algorithm Used:**
  [[two_pass_greedy]]

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 0:
            return 0

        # Step 1: Initialize candies array with 1 candy for each child
        candies = [1] * n

        # Step 2: Left to right pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        # Step 3: Right to left pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        # Step 4: Return the total number of candies
        return sum(candies)
```

---

### ⏱️ Time & Space Complexity

- **Time:** O(n)
  - We traverse the ratings array twice, once from left to right and once from right to left.
- **Space:** O(n)
- The space complexity is O(n) due to the `candies` array used to store the number of candies for each child.

---

### 🧩 Key Takeaways

- ✅ What concept or trick did I learn?
  - The `two-pass greedy algorithm` is a powerful technique for problems where `local conditions` depend on both `previous and next elements`.
- 💡 What made this problem tricky?
  - Nothing really, it was straightforward once I realized the two-pass approach.
- 💭 How will I recognize a similar problem in the future?
  - Conditions that require comparing both previous and next elements often indicate a need for a two-pass greedy solution.

---

### 🔁 Reflection (Self-Check)

- [😊] Could I solve this without help?
- [😁] Did I write code from scratch?
- [🐵] Did I understand why it works?
- [🙄] Will I be able to recall this in a week?

---

### 📚 Related Problems

- [[3122 Minimum Number of Operations to Satisfy Conditions]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `7`   |
| Total Problems Solved | `342` |
| Confidence Today      | 😃    |
