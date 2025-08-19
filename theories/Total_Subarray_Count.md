# Counting Total Non-Empty Subarrays

Let's say we have a list of integers `arr = [1, 2, 3, 4,5]`. The total number of non-empty subarrays can be calculated using the formula:

\[\text{Total Subarrays} = \frac{n(n + 1)}{2}\]

This is derived from the fact that for each element in the array, we can choose to start a subarray at that element and end it at any subsequent element, including itself.

If subarrays length = 1:

We have `n` choices (each element can be a subarray).

If subarrays length = 2:

We have `n-1` choices (each pair of adjacent elements can form a subarray).

If subarrays length = 3:
We have `n-2` choices (each triplet of adjacent elements can form a subarray).

and so on...

Finally, if subarrays length = n:
We have `1` choice (the entire array itself).

So, the series of choices can be summed up as:
\[n + (n - 1) + (n - 2) + ... + 1 = \frac{n(n + 1)}{2}\]

This formula gives us the total number of non-empty subarrays in an array of size `n`.