# Minimum Operations to Make a String Sorted Using Character Extremes

## Intuition

The key observation is that we don't need to simulate the operations to determine the answer. Instead, we can figure out the minimum number of operations by looking at the **smallest and largest characters in the string and where they appear**.

The goal is to make the string sorted in non-decreasing order. If it is already sorted, we need zero operations.

Otherwise, we need to understand how the positions of the minimum and maximum characters affect our ability to sort the string.

### Case 1: The string has length two

If the string contains only two characters and is not sorted, it must look like this:

`"ba"`

There is no way to fix this using the allowed operations, so the answer is `-1`.

### Case 2: The first character is the minimum, or the last character is the maximum

Suppose the string looks like this:

`"acb"`

The smallest character, `'a'`, is already at the beginning. We only need to move the largest character, `'c'`, to the end.

More generally, if the first character is the minimum or the last character is the maximum, one operation is sufficient to put the string in sorted order.

### Case 3: The minimum or maximum character is somewhere in the middle

Consider:

`"bca"`

The string is not sorted, and neither the first character is the minimum nor the last character is the maximum.

However, the minimum character `'a'` is in the middle. We can use two operations to move the extreme characters into their correct positions and finish sorting the string.

The same reasoning applies if the maximum character appears in the middle.

### Case 4: Neither extreme character is in the middle

Consider:

`"cab"`

Here, the minimum character `'a'` is in the middle, so this example actually falls into Case 3. For the three-operation case, consider a longer string such as `"bdca"`.

The minimum character `'a'` is at the end, and the maximum character `'d'` is in the middle, so this example also falls into Case 3.

The important condition for needing three operations is that the string is not sorted, has length greater than two, the first character is not the minimum, the last character is not the maximum, and neither extreme character appears in the middle.

In that situation, we need three operations to move the extreme characters into their correct positions and sort the string.

**The overall idea is to classify the string based on whether it is already sorted and where its minimum and maximum characters occur.** This lets us determine the answer without actually performing the operations.

## Approach

1. Find the length of the string, along with its minimum and maximum characters.
2. Check whether the string is already sorted. If so, return `0`.
3. If the string has length two and is not sorted, return `-1`.
4. If the first character is the minimum or the last character is the maximum, return `1`.
5. Otherwise, check the interior characters. If any interior character is the minimum or maximum, return `2`.
6. If none of these conditions apply, return `3`.

## Complexity

- **Time complexity:** \(O(n)\), where \(n\) is the length of the string. Finding the minimum and maximum, checking whether the string is sorted, and scanning the interior all take linear time.
- **Space complexity:** \(O(1)\), because the algorithm uses only a constant number of variables, excluding the input string.

## Code

```python
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mx = max(s)
        mn = min(s)

        if all(a <= b for a, b in zip(s, s[1:])):
            return 0

        if len(s) == 2:
            return -1

        if s[0] == mn or s[-1] == mx:
            return 1

        for i in range(1, len(s)-1):
            if s[i] == mn or s[i] == mx:
                return 2

        return 3
```