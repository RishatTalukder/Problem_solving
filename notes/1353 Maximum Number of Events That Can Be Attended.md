## 🧠 Solving LeetCode Until I Become Top 1% — Day `37`

### 🔹 Problem: [1353. Maximum Number of Events That Can Be Attended](https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/)

**Difficulty:** Medium
**Tags:** #Greedy, #Heap, #Sorting

---

### 📝 Problem Summary

You’re given a list of events. Each event has a `startDay` and an `endDay`. You can attend **only one event per day**, and you can attend an event on **any day in its range**.

Return the **maximum number of events** you can attend.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  Try to greedily attend every event starting from the first day to the last. Check for each day if there's an event available. **Too slow.**

* **My Initial Thought:**
  This feels like an interval merge problem — sort the events by end time, and try to attend them one by one.

  But the twist here is:

  > You can choose *any* day in the event’s range, and events can overlap.

  So you can't just keep a `prev` variable like in merge intervals because **you can’t attend two events on the same day**, and **some events can have the same day ranges**.

* **Optimized Strategy (Greedy + Min Heap):**

  1. Sort events by their start day.
  2. Iterate day-by-day.
  3. For each day:

     * Add all events that start that day to a min heap (by end day).
     * Remove all events from the heap that ended before today.
     * If the heap isn’t empty, attend the event with the earliest end day (pop from heap), and increment your counter.

* Why this works: You always choose to attend the event that ends soonest, freeing up more future days.

---

### ⚙️ Code Implementation (Python)

```python
import heapq

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()  # Sort by start day
        heap = []
        day = 0
        i = 0
        res = 0
        n = len(events)

        while i < n or heap:
            if not heap:
                day = events[i][0]
            while i < n and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            while heap and heap[0] < day:
                heapq.heappop(heap)
            if heap:
                heapq.heappop(heap)
                res += 1
                day += 1
        return res
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n log n)
  (due to sorting + heap operations)
* **Space:** O(n) for the heap

---

### 🧩 Key Takeaways

* ✅ Learned how to use a **heap** for a greedy strategy where we prioritize the event that **ends the earliest**.
* 💡 Problem looks like an interval problem but **heap + day simulation** is needed because we must **attend only one event per day**.
* 💭 If the problem involves scheduling with a **choice of days**, consider **simulating each day**.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help? *(Almost — needed clarity on the simulation part.)*
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 📚 Related Problems

* [[1751 Maximum Number of Events That Can Be Attended II]]
* [[2008 Maximum Earnings From Taxi]]
* [[2402. Meeting Rooms III]]

---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `39`  |
| Total Problems Solved | `377` |
| Confidence Today      | 😃    |
