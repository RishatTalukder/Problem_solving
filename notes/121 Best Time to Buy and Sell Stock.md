# 📍 121. Best Time to Buy and Sell Stock

* 💡 Difficulty: #Easy
* 🧩 Tags: #KadanesAlgorithm
* 🔄 Pattern: Sliding Window
* 🔍 Link: [LeetCode Link](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

---

## 🧠 Problem Summary

You're given an array `prices`, where `prices[i]` represents the price of a stock on day `i`.
Your goal is to **buy once and sell once later** to maximize profit.
You must return the maximum profit possible, or `0` if no profitable transaction exists.

---

## 🚫 Brute Force Approach

Try every possible pair of days `(i, j)` such that `j > i`, calculate `prices[j] - prices[i]`, and keep track of the max profit.

* **Inefficient** because it checks all pairs: O(n²) time.

---

## ✅ Optimal Solution

Use a **single pass** and track the **minimum price so far** as you iterate.

### Step-by-Step:

1. Initialize `min_price = ∞` and `max_profit = 0`
2. For each price:

   * If current price is less than `min_price`, update `min_price`
   * Else calculate profit = `price - min_price` and update `max_profit` if greater
3. Return `max_profit`

---

## 📦 Code (Python)

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)
        
        return max_profit
```

---

## 📊 Complexity

* **Time:** O(n) — single pass through the array
* **Space:** O(1) — only a few variables needed

---

## 📝 Notes

* ✅ Classic [[kadane's_algorithm]].
* 💡 Always think about tracking "best seen so far" — here it's `min_price`.
* 💭 This pattern shows up in more complex stock trading problems (like cooldown, k transactions, etc.).
* 🧠 Reminder: Can't sell before you buy!
