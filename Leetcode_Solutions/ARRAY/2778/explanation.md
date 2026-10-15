# Finding Special Indices and Summing Their Squares

## Intuition

The idea is to iterate through the array and check which elements satisfy the given condition.

An index `i` is considered special if the length of the array is divisible by `i + 1`. Since Python uses zero-based indexing, we use `i + 1` to represent the element's position in the array.

For every special index, we add the square of the corresponding element to our answer.

For example, consider:

`nums = [1, 2, 3, 4]`

The array length is `4`.

- Index `0`: \(4 \bmod 1 = 0\), so we add \(1^2 = 1\).
- Index `1`: \(4 \bmod 2 = 0\), so we add \(2^2 = 4\).
- Index `2`: \(4 \bmod 3 \neq 0\), so we skip it.
- Index `3`: \(4 \bmod 4 = 0\), so we add \(4^2 = 16\).

The final answer is \(1 + 4 + 16 = 21\).

## Approach

1. Initialize `ans = 0` to store the sum of squares of the special elements.

2. Iterate through every index in the array using `range(len(nums))`.

3. For each index `i`, check whether `len(nums) % (i + 1) == 0`. If the remainder is zero, the index is special.

4. If the condition is satisfied, add `nums[i] ** 2` to `ans`.

5. After checking every index, return `ans`.

This approach is straightforward because we only need one traversal of the array and do not need any additional data structures.

## Complexity

- **Time complexity:** \(O(n)\), where \(n\) is the length of the array. We visit every element exactly once, performing a constant-time divisibility check and, when appropriate, a squaring and addition.

- **Space complexity:** \(O(1)\), because we only use the variable `ans` and the loop index. No additional data structure grows with the input size.

## Code

```python3
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            if len(nums) % (i + 1) == 0:
                ans += nums[i] ** 2

        return ans
```