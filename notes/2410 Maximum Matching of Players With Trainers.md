## 🧠 Solving LeetCode Until I Become Top 1% — Day `42`

### 🔹 Problem: [2410. Maximum Matching of Players With Trainers](https://leetcode.com/problems/maximum-matching-of-players-with-trainers/)

**Difficulty:** #Medium
**Tags:** #Greedy, #TwoPointers, #Sorting

---

### 📝 Problem Summary

We are given two arrays:

* `players[i]` denotes the strength requirement of the ith player.
* `trainers[j]` denotes the strength capability of the jth trainer.

A player can be matched with a trainer if the trainer's strength is **greater than or equal** to the player's requirement.

Each player and trainer can only be used once.

We need to **maximize** the number of such valid matches.

---

### 🧠 My Thought Process

* **Brute Force Idea:**

  * Try all pairs of players and trainers using a nested loop and mark used ones.
  * Time complexity would be **O(n²)** — too slow for large inputs.

* **Optimized Strategy:**

  * Sort both arrays.
  * Use **two pointers** — one for players and one for trainers.
  * Try to greedily match the weakest player with the smallest trainer who can support them.
  * If a match is possible, move both pointers.
  * Otherwise, move only the trainer pointer.

  This way, we avoid unnecessary comparisons and always match as early and efficiently as possible.

* **Algorithm Used:**
  `Greedy` + `Two Pointers` + `Sorting`

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        player_index = 0
        trainer_index = 0
        matches = 0
        
        while player_index < len(players) and trainer_index < len(trainers):
            if players[player_index] <= trainers[trainer_index]:
                matches += 1
                player_index += 1
                trainer_index += 1
            else:
                trainer_index += 1
        
        return matches
```

---

### ⏱️ Time & Space Complexity

* **Time:** `O(n log n + m log m)`
  (sorting players and trainers)
* **Space:** `O(1)`
  (in-place, no extra data structures)

---

### 🧩 Key Takeaways

* ✅ Sorting both arrays lets you make **greedy optimal decisions** in linear time afterward.
* 💡 Two pointers are often useful when dealing with **sorted arrays** and pairing problems.
* 💭 This is a classic matching problem — much like **assigning tasks to workers** or **pairing jobs with deadlines**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[826 Most Profit Assigning Work]]
* [[925 Long Pressed Name]]
* [[986 Interval List Intersections]]
* [[1754 Largest Merge Of Two Strings]]
* [[2071 Maximum Number of Tasks You Can Assign]]
* [[2300 Successful Pairs of Spells and Potions]]
* [[2332 The Latest Time to Catch a Bus]]
* [[2592 Maximize Greatness of an Array]]


---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `42`   |
| Total Problems Solved | `383`   |
| Confidence Today      | 😃    |
