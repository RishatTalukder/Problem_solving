# Sum of Squared Distinct Counts of All Subarrays

# Intuition

We need to consider every possible subarray and calculate the square of the number of distinct elements it contains.

Instead of generating each subarray separately, we can fix a starting index and expand the subarray one element at a time.

We maintain a `set` to keep track of distinct elements. Whenever we add a new element, the set automatically handles duplicates. We then add the square of the set's size to our answer.

# Approach

1. Initialize `ans = 0` to store the total sum.
2. Use an outer loop to choose each possible starting index `i`.
3. Create an empty set `sub` for tracking distinct elements in the current subarrays.
4. Use an inner loop to extend the subarray from `i` to every possible ending index `j`.
5. Add `nums[j]` to the set, then add `len(sub) ** 2` to `ans`.
6. Return `ans` after processing all subarrays.

# Complexity

- Time complexity: \(O(n^2)\) on average, where \(n\) is the length of `nums`. There are \(O(n^2)\) subarrays, and set insertion takes \(O(1)\) average time.
- Space complexity: \(O(n)\), because the set can contain up to \(n\) distinct elements.

# Code

```python3
class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            sub = set()

            for j in range(i, len(nums)):
                sub.add(nums[j])
                ans += len(sub)**2

        return ans
```