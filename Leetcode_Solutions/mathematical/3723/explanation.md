# Maximize Sum of Squares by Greedily Distributing Digits

# Intuition

To maximize the sum of squares of the digits, we want to make the digits as large as possible. Since every digit can be at most `9`, we should use as many `9`s as we can.

For example, if `num = 4` and `sum =  twenty`, we can construct `"9920"`. It uses two `9`s, followed by the remaining sum `2`, and fills the remaining position with `0`s.

The key idea is simple: **use as many `9`s as possible, then use the remaining sum as one digit, and fill the rest with zeros.**

If the required sum is greater than `9 * num`, it's impossible because `num` digits can contribute at most `9 * num`.

# Approach

1. If `sum > 9 * num`, return an empty string because no valid number can have the required digit sum.
2. Use `divmod(sum, 9)` to calculate:
   - `div`: the number of `9`s we can use.
   - `mod`: the remaining sum after using those `9`s.
3. Construct the answer using `div` copies of `'9'`.
4. If `mod` is nonzero, append it as another digit.
5. Append zeros until the string contains exactly `num` digits.

# Complexity

- Time complexity: \(O(num)\), because constructing the string requires up to `num` digits.
- Space complexity: \(O(num)\), for the resulting string.

# Code

```python3
class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9*num:
            return ''

        div, mod = divmod(sum, 9)

        ans = '9'*div

        if mod:
            ans += str(mod)

        ans += '0'*(num - len(ans))

        return ans
```