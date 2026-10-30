# Count Days Spent Together

## Intuition

The days Alice and Bob spend together are simply the days when their vacation periods overlap.

Instead of checking every single day, we can find the intersection of their two date ranges:

- The overlap starts at the **later** of the two arrival dates.
- The overlap ends at the **earlier** of the two leaving dates.

If the calculated start date is after the end date, there is no overlap, so we return `0`.

Otherwise, we just need to calculate the number of days between those two dates, including both the starting and ending days.

## Approach

Since all dates are in the same non-leap year and use the `MM-DD` format, we can compare them lexicographically as strings. This works because the month and day are always zero-padded.

First, calculate the overlapping range:

- `start = max(aa, ab)`
- `end = min(la, lb)`

If `start > end`, the vacation periods do not overlap.

To calculate the number of days between two dates, convert each date into its corresponding day number within the year.

For example, to convert `03-05`:
- Add the total number of days in January and February.
- Add the 5 days in March.

We can do this using a cumulative sum of the days in the preceding months, then subtract the day numbers of the two dates.

Finally, add `1` because both the starting and ending dates are included in the overlap.

## Complexity

- **Time complexity:** \(O(1)\) — Each date has a fixed-length format, and the month lookup involves at most 12 months.
- **Space complexity:** \(O(1)\) — The days array has a fixed size of 12, regardless of the input.

## Code

```python
class Solution:
    def countDaysTogether(self, aa: str, la: str, ab: str, lb: str) -> int:
        start = max(aa, ab)
        end = min(la, lb)

        if start > end:
            return 0

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def to_days(date):
            month, day = map(int, date.split('-'))

            return sum(days[:month-1]) + day

        return to_days(end) - to_days(start) + 1
```