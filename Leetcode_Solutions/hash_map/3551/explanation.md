# Minimum Swaps to Sort by Digit Sum Using Cycle Decomposition

## Intuition

The tricky part of this problem is that **sorting the array is easy, but finding the minimum number of swaps needed to reach the sorted order is not as straightforward.**

First, we need to determine the correct sorted order. Each number is sorted by:
1. Its digit sum in ascending order.
2. Its actual value in ascending order when two numbers have the same digit sum.

Once we know the sorted order, we can think of the problem differently: instead of swapping numbers directly, let's figure out **where each element belongs in the final sorted array**.

Imagine an element at index `i` belongs at index `target[i]`. If we follow these destination indices, we eventually return to an index we've already visited. This forms a cycle.

For example, suppose the elements need to move like this:

`0 → 2 → 1 → 0`

These three positions form a cycle. We can fix this cycle using just **2 swaps**.

In general, a cycle containing $k$ elements requires $k-1$ swaps to put every element in its correct position.

So, if there are $n$ elements and $C$ independent cycles, the minimum number of swaps is:

$$
\boxed{n-C}
$$

Our goal is therefore to determine the destination of every element and count the cycles.

## Approach

### 1. Calculate the digit sum of every number

We iterate through `nums` and calculate each number's digit sum using `% 10` to extract the last digit and `// 10` to remove it.

For example, the digit sum of `321` is:

$$
3+2+1=6
$$

We store each digit sum in `digitSum`, keeping the same index as the original number.

### 2. Determine the sorted order

Instead of sorting the actual numbers, we sort their indices:

```python
indecies = list(range(n))
indecies.sort(key=lambda i: (digitSum[i], nums[i]))
```

Why sort indices instead of numbers?

Because we need to preserve the original positions of the elements to calculate how many swaps are required.

The sorting key `(digitSum[i], nums[i])` ensures that digit sum is the primary criterion and the actual number is the tie-breaker.

For example, consider:

```text
nums     = [21, 13, 12]
digitSum = [ 3,  4,  3]
```

The sorted order is:

```text
12, 21, 13
```

The corresponding original indices are:

```text
2, 0, 1
```

Therefore, `indecies = [2, 0, 1]`.

### 3. Build the destination mapping

We create `target`, where `target[i]` tells us the **destination index of the element originally at index `i`**.

```python
target = [0] * n

for pos, ind in enumerate(indecies):
    target[ind] = pos
```

For our example:

```text
Original index:  0   1   2
Original value: 21  13  12
Destination:     1   2   0
```

So:

```python
target = [1, 2, 0]
```

This means:
- The element at index `0` belongs at index `1`.
- The element at index `1` belongs at index `2`.
- The element at index `2` belongs at index `0`.

Following these destinations gives us the cycle:

$$
0 \rightarrow 1 \rightarrow 2 \rightarrow 0
$$

### 4. Count the cycles

We use `visited` to ensure that each cycle is counted only once.

```python
visited = [0] * n
cycle = 0

for i in range(n):
    if not visited[i]:
        cycle += 1
        j = i

        while not visited[j]:
            visited[j] = 1
            j = target[j]
```

Whenever we encounter an unvisited index, we have discovered a new cycle, so we increment `cycle`.

Then we follow `target` repeatedly until we reach an already visited index. Every index encountered along the way belongs to that cycle.

After processing all indices, `cycle` contains the total number of independent cycles.

### 5. Calculate the minimum swaps

Every cycle of length $k$ requires $k-1$ swaps. If there are $C$ cycles containing all $n$ elements, the total is:

$$
(k_1-1)+(k_2-1)+\cdots+(k_C-1)
$$

Since the sum of all cycle lengths is $n$, this simplifies to:

$$
\boxed{\text{Minimum swaps}=n-C}
$$

Therefore, we return:

```python
return n - cycle
```

## Complexity

Let $n$ be the number of elements and $D$ be the maximum number of digits in any number.

- **Time complexity:** $O(n\log n+nD)$. Calculating digit sums takes $O(nD)$, sorting the indices takes $O(n\log n)$, and counting cycles takes $O(n)$. If the numbers have a bounded number of digits, this simplifies to $O(n\log n)$.
- **Space complexity:** $O(n)$, for the digit sums, index ordering, destination mapping, and visited array.

## Code

```python3
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)

        digitSum = []

        for num in nums:
            summ = 0

            while num > 0:
                summ += num % 10
                num //= 10

            digitSum.append(summ)

        indecies = list(range(n))
        indecies.sort(key=lambda i: (
            digitSum[i], nums[i]
        ))

        target = [0] * n

        for pos, ind in enumerate(indecies):
            target[ind] = pos

        visited = [0] * n
        cycle = 0

        for i in range(n):
            if not visited[i]:
                cycle += 1
                j = i

                while not visited[j]:
                    visited[j] = 1
                    j = target[j]

        return n - cycle
```