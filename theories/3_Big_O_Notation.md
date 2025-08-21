# Big_O_Notation

This is a part of theoretical complexity analysis, focusing on Big O notation, which describes the upper bound of an algorithm's time complexity in terms of input size.

Let's say you have a algorithm time funciton given below:

```python
def example_algorithm(n):
    # A simple example algorithm that runs in O(n^2)
    total = 0
    for i in range(n):
        for j in range(n):
            total += i + j
    return total
```

So, `T(n) = c + n^2`, where `c` is a constant factor. The Big O notation simplifies this to `O(n^2)`.

The rule of simplification is that we ignore constant factors and lower order terms, focusing on the term that grows the fastest as `n` increases.

This just mean the execution time of the algorithm will be less than or equal to `Kn^2` for some constant `K` and sufficiently large `n`.

This means that as `n` grows, the time complexity of the algorithm will be dominated by the `n^2` term, and the constant factor `K` does not affect the growth rate.

There can be many types of Big O notations, such as:
- `O(1)` - Constant time
- `O(log n)` - Logarithmic time
- `O(n)` - Linear time
- `O(n log n)` - Linearithmic time
- `O(n^2)` - Quadratic time
- `O(n^3)` - Cubic time
- `O(2^n)` - Exponential time

If we seriealize the above example, we will surely get the following:

> O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n)

So, we can see that o(n^2) is worse than O(n log n) and O(n), but better than O(2^n).

![image](./image.png)

This chart shows the growth of different Big O notations as `n` increases. The y-axis represents the time complexity, while the x-axis represents the input size `n`. As `n` grows, the differences in growth rates become more pronounced, illustrating why we use Big O notation to describe algorithm efficiency.