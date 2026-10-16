# Greedy Bit Distribution to Maximize the Sum of Squares

## Intuition

The main idea is that **we want to distribute the available set bits among `k` numbers so that the sum of their squares is as large as possible.**

Why does this work?

Squaring a number rewards larger values disproportionately. For example:

\[
5^2 + 1^2 = 26
\]

But if we distribute the bits more evenly:

\[
3^2 + 3^2 = 18
\]

In this example, concentrating the value into the larger number produces a greater sum of squares.

However, we cannot arbitrarily move bits around. We can only use bits that actually exist in the input numbers, and each occurrence of a bit can be used only once.

So, instead of thinking about the original numbers, let's think about their individual bits.

Suppose the input contains these numbers:

`nums = [2, 1, 3]`

Their binary representations are:

```text
2 = 010
1 = 001
3 = 011
```

We have two occurrences of bit `1` and two occurrences of bit `0`.

Since the same bit can appear in multiple input numbers, we can distribute those occurrences among our `k` constructed numbers. For `k = 2`, we can construct:

```text
Number 1: 011 = 3
Number 2: 011 = 3
```

Each constructed number uses one occurrence of each available bit. The resulting sum is:

\[
3^2 + 3^2 = 18
\]

The important observation is that **every available bit should be used in as many constructed numbers as possible, starting with the highest bits**. A higher bit contributes more to a number's value, so we prioritize it when building each number.

## Approach

### 1. Count how many times each bit appears

We create a `count` array of size `30`, where `count[i]` stores the number of input elements whose \(i\)-th bit is set.

For every number, we inspect each bit using:

```python
if num & (1 << i):
    count[i] += 1
```

The expression `1 << i` creates a number with only bit `i` set. Using bitwise AND tells us whether that bit is present in `num`.

After processing all numbers, we know how many copies of every bit are available to distribute.

### 2. Greedily construct `k` numbers

We repeat the construction process `k` times.

For each number, we start with `cur = 0` and inspect the bits from highest to lowest.

Whenever `count[i] > 0`, we include that bit in the current number:

```python
cur |= (1 << i)
count[i] -= 1
```

The first statement sets the bit in `cur`. The second consumes one available occurrence so that the same occurrence cannot be reused in another constructed number.

We continue until all bit positions have been checked.

**Why do we build each number using the highest available bits first?**

A high bit contributes more to the number than a low bit. By placing every available high bit into a constructed number before moving to lower bits, we make each number as large as the remaining bit counts allow.

Repeating this process distributes the available bits across the `k` numbers in a way that maximizes their sum of squares.

### 3. Add the square of each constructed number

Once a number is complete, we add its square to the result:

```python
res = (res + cur**2) % (10**9 + 7)
```

We take the modulo after each addition to keep the result within the required range.

After constructing all `k` numbers, we return `res`.

## Complexity

- **Time complexity:** \(O(nB + kB)\), where \(n\) is the length of `nums` and \(B = 30\) is the fixed number of bit positions. Since \(B\) is constant, this simplifies to \(O(n + k)\).

- **Space complexity:** \(O(B) = O(1)\), because the `count` array always contains 30 entries, regardless of the input size.

## Code

```python3
class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        count = [0] * 30

        for num in nums:
            for i in range(30):
                if num & (1 << i):
                    count[i] += 1

        res = 0

        for _ in range(k):
            cur = 0

            for i in range(29, -1, -1):
                if count[i] > 0:
                    cur |= (1 << i)
                    count[i] -= 1

            res = (res + cur**2) % (10**9 + 7)

        return res
```