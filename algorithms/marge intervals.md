`Marge Interval` is a problem that given a collection of intervals, merge all overlapping intervals.

For example,

Given `[1,3],[2,6],[8,10],[15,18]`,

return `[1,6],[8,10],[15,18]`.

Explanation:

Since intervals `[1,3]` and `[2,6]` overlaps because `2 < 3`, we merged them into `[1,6]`.

and there is no other intervals that overlaps with each other.

SOLUTION:
```python
def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    if not intervals:
        return []
    # sort the intervals by their start value
    intervals.sort(key=lambda x: x.start)

    stack = [intervals[0]]

    # for each interval, if it overlaps with the previous one, combine them together
    for i in intervals[1:]:
        # if overlap
        if stack[-1][0] <= i[0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1], i[1])
        else:
            stack.append(i)
    
    
    return stack

```