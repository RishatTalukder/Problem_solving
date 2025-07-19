## 🧠 Solving LeetCode Until I Become Top 1% — Day `48`

### 🔹 Problem: [1233. Remove Sub-Folders from the Filesystem](https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/)

**Difficulty:** #Medium
**Tags:**  #String, #Sorting 

---

### 📝 Problem Summary

You’re given a list of folder paths (e.g., `["/a","/a/b","/c/d","/c/d/e","/c/f"]`).
The task is to remove **all sub-folders**, keeping only the **top-level parent folders**.

> A folder `f1` is a sub-folder of `f2` if `f1` starts with `f2 + "/"`.

Return a list of folders excluding all sub-folders.

---

### 🧠 My Thought Process

* **Brute Force Idea:**
  For each folder, check if it's a subfolder of any other folder in the list. That would be `O(n²)` comparisons. Not scalable.

* **Optimized Strategy:**
  Sort the folders lexicographically. That way, any subfolder will immediately follow its parent.

  * Initialize the result list with the first folder.
  * For every folder from index `1` onward:

    * If it doesn’t start with the last added folder + `'/'`, it's a top-level folder → add it to result.

* **Algorithm Used:**
  Sorting + Prefix Check

---

### ⚙️ Code Implementation (Python)

```python
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()  # Lexicographically sort paths
        res = [folder[0]]  # First one is always a root

        for f in folder[1:]:
            prev = res[-1]
            # Check if `f` is NOT a subfolder of the last added root
            if not (f.startswith(prev) and len(f) > len(prev) and f[len(prev)] == "/"):
                res.append(f)

        return res
```

---

### ⏱️ Time & Space Complexity

* **Time:** `O(n log n)` — Sorting takes `n log n`, rest is linear scan
* **Space:** `O(n)` — Result list

---

### 🧩 Key Takeaways

* ✅ Learned how **lexicographic sorting** simplifies hierarchical string problems.
* 💡 Tricky part was making sure we don't falsely match `/a/bc` as subfolder of `/a`.
* 💭 Will look out for prefix-matching problems where sorted input helps reduce complexity.

---

### 🔁 Reflection (Self-Check)

* [x] Could I solve this without help?
* [x] Did I write code from scratch?
* [x] Did I understand why it works?
* [x] Will I be able to recall this in a week?

---

### 🚀 Progress Tracker

| Metric                | Value  |
| --------------------- | ------ |
| Day                   | `48`    |
| Total Problems Solved | `389`    |
| Confidence Today      | 😃     |
| Leetcode Rating       | `1572` |
