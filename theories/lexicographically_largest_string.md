## 🅰️ Lexicographically Largest String — Note

In string comparison, **lexicographical order** works just like a dictionary:

* `"z"` > `"y"` > `"x"` ... > `"b"` > `"a"`
* For two strings, compare characters from **left to right**:

  * As soon as you find a different character, the one with the **larger character** is considered larger.

### ✅ Examples:

* `"cat"` < `"dog"` (because `'c'` < `'d'`)
* `"abc"` < `"abcd"` (prefix is smaller)
* `"zebra"` > `"apple"`

### 🧠 Lexicographically Largest Substring:

If you're asked to find the **lexicographically largest substring** of a given string:

* You look for the substring which would come **last in dictionary order**.
* This is often solved by:

  * **Greedy**: Look for the largest starting character and compare substrings.
  * **Two Pointer / Sliding Window**: Slide a window of fixed size and track the max.

### 📌 Use Cases in Problems:

* Picking the **best possible string** from valid splits.
* Comparing **substrings** for ordering.
* Finding **maximum lexicographical order** in strings formed after transformations.

---

Let me know if you want a visual example or how this applies in a specific problem!
