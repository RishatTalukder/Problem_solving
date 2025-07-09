## 🧠 Solving LeetCode Until I Become Top 1% — Day `41`

### 🔹 Problem: [3439 Reschedule Meetings for Maximum Free Time I](https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/)

**Difficulty:** #Medium
**Tags:** #Greedy, #SlidingWindow, #Intervals

---

### 📝 Problem Summary

Given a timeline and a bunch of meetings that don’t overlap (how convenient), you're allowed to reschedule **up to k of them**. You can’t change their order or duration, only shift them around to create **as much free time as possible**. Return the length of the **longest uninterrupted block of free time** you can manufacture.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  I didn’t even reach this stage. My brain just threw a 503 error. Everything looked like a heap problem, or maybe a job scheduler from the future. I started thinking about binary search trees and forgot what I was solving. Fantastic start.

* **Optimized Strategy:**
  After reading the discussion (aka being rescued by the brave souls who solved it), I found out it’s actually a **sliding window over “gaps between meetings”**. If I merge `k+1` of these gaps, I can “simulate” shifting `k` meetings out of the way and combine the in-between free time.

  Okay... sure. That makes sense **now**.

* **Algorithm Used:**
  [[Sliding_Window]] disguised as a scheduling problem. The trick is to compute all the **gaps**, then apply a moving sum of `k+1` to simulate the best-case meeting reshuffles.

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def maxFreeTime(self, eventTime, k, startTime, endTime):
        n = len(startTime)
        gaps = [startTime[0]]
        for i in range(1, n):
            gaps.append(startTime[i] - endTime[i - 1])
        gaps.append(eventTime - endTime[-1])

        window = sum(gaps[:k+1])
        ans = window

        for i in range(k+1, len(gaps)):
            window += gaps[i] - gaps[i - (k+1)]
            ans = max(ans, window)

        return ans
```

---

### ⏱️ Time & Space Complexity

* **Time:** O(n)
* **Space:** O(n)

---

### 🧩 Key Takeaways

* ✅ Sliding window is versatile — even when your brain isn’t.
* 💡 When a problem says “maximize free time,” don’t overthink. Just try merging gaps.
* 💭 This is like **Merge Intervals** meets **Max Subarray Sum** meets **Why am I doing this at 2 AM**.

---

### 🔁 Reflection (Self-Check)

* [ ] Could I solve this without help?
  → *Absolutely not. It was like my brain called in sick for the day.*

* [ ] Did I write code from scratch?
  → *Eventually, yes... with the training wheels of LeetCode discussions on full display.*

* [x] Did I understand why it works?
  → *Now I do. Took me a hot minute, though.*

* [x] Will I be able to recall this in a week?
  → *If my ego survives this problem, sure.*


---

### 🚀 Progress Tracker

| Metric                | Value |
| --------------------- | ----- |
| Day                   | `41`  |
| Total Problems Solved | `379` |
| Confidence Today      | 😣    |

