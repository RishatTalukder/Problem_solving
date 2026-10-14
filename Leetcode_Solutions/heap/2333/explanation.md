# Minimizing Square Differences Using Frequency Counting and Greedy Reduction

## Intuition

The goal is to minimize the sum of squared differences between corresponding elements of `nums1` and `nums2` by performing at most `k1 + k2` operations.

In each operation, we can increase or decrease an element in either array by `1`. This means we can reduce the absolute difference between a pair of corresponding elements by `1` per operation, as long as that difference is greater than zero.

Let's define the absolute difference at each index as:

\[
d_i = |nums1[i] - nums2[i]|
\]

Our goal is to minimize:

\[
\sum_{i=0}^{n-1} d_i^2
\]

The important observation is that **reducing a larger difference is generally more beneficial than reducing a smaller one**.

For example, reducing a difference from `5` to `4` decreases its squared contribution by:

\[
5^2 - 4^2 = 9
\]

But reducing a difference from `2` to `1` decreases its squared contribution by only:

\[
2^2 - 1^2 = 3
\]

Therefore, we should prioritize the largest differences and reduce them before spending operations on smaller ones.

A straightforward solution might sort all the differences and repeatedly reduce the largest one. However, we can do better by using **frequency counting**.

Instead of storing every difference separately, we count how many times each difference occurs. This allows us to process all differences of the same value together.

## Approach

### 1. Combine the available operations

We can modify either array, so both operation budgets contribute toward reducing the differences.

We combine them into a single budget:

```python
k = k1 + k2
```

This represents the total number of operations available.

### 2. Find the maximum difference

We iterate through both arrays and calculate the absolute difference at each index.

At the same time, we find the largest difference, `maxx`.

We need this value to determine the size of our frequency array.

For example, if the differences are:

`[3, 1, 3, 2]`

then `maxx = 3`.

### 3. Build the frequency array

We create an array initialized with zeros:

```python
freq = [0] * (maxx + 1)
```

Here, `freq[d]` represents the number of elements whose absolute difference is exactly `d`.

For the differences `[3, 1, 3, 2]`, the frequency array would be:

| Difference | Frequency |
|---:|---:|
| 0 | 0 |
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |

The advantage is that we can process every difference of the same value together instead of sorting and updating individual elements.

### 4. Reduce the largest differences first

We iterate from `maxx` down to `1`.

At each difference `i`, we check how many operations we can use to reduce it.

There are `freq[i]` differences currently equal to `i`. Each one needs one operation to become `i - 1`.

We calculate:

```python
minn = min(k, freq[i])
```

This gives us the number of differences we can reduce at this level:

- If `k` is smaller than `freq[i]`, we reduce only `k` of them and run out of operations.
- If `k` is at least `freq[i]`, we reduce all of them by one and continue to the next smaller difference.

We then update the operation budget:

```python
k -= minn
```

Next, we update the frequencies:

```python
freq[i] -= minn
freq[i - 1] += minn
```

The first line removes the reduced differences from level `i`. The second adds them to level `i - 1`.

For example, suppose we have three differences equal to `4` and only two operations remaining.

Initially:

`freq[4] = 3`

We can reduce two of those differences from `4` to `3`, resulting in:

- `freq[4] = 1`
- `freq[3] = 2`
- `k = 0`

Since no operations remain, we stop reducing the differences.

This greedy process prioritizes the differences with the greatest potential reduction in squared error.

### 5. Calculate the final sum

After using the available operations, we calculate the sum of the squared differences.

Each difference `i` contributes \(i^2\), and there are `freq[i]` such differences.

Therefore, the final answer is:

\[
\sum_{i=1}^{maxx} i^2 \cdot freq[i]
\]

We iterate through the frequency array and accumulate these contributions.

We start from `maxx` and go down to `1`. Differences equal to zero do not contribute anything, so we can safely ignore them.

## Complexity

Let \(n\) be the length of the input arrays and \(M\) be the maximum absolute difference.

- **Time complexity:** \(O(n + M)\). Finding the maximum difference and building the frequency array take \(O(n)\) time each. Processing the frequency array and calculating the final sum each take \(O(M)\) time.

- **Space complexity:** \(O(M)\). The frequency array contains \(M + 1\) entries. Apart from this array, we use only a constant amount of additional space.

This approach avoids sorting the individual differences, making it particularly effective when the maximum difference is reasonably small.

## Code

```python3
class Solution:
    def minSumSquareDiff(
        self,
        nums1: list[int],
        nums2: list[int],
        k1: int,
        k2: int
    ) -> int:
        k = k1 + k2

        maxx = 0

        for i in range(len(nums1)):
            maxx = max(
                maxx,
                abs(nums1[i] - nums2[i])
            )

        freq = [0] * (maxx + 1)

        for i in range(len(nums1)):
            freq[
                abs(nums1[i] - nums2[i])
            ] += 1

        for i in range(maxx, 0, -1):
            if k <= 0:
                break

            minn = min(k, freq[i])

            k -= minn
            freq[i] -= minn
            freq[i - 1] += minn

        ans = 0

        for i in range(maxx, 0, -1):
            ans += i * i * freq[i]

        return ans
```

