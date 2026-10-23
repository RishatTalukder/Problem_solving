# Find Target Indices After Sorting

## Intuition

After sorting the array, all occurrences of `target` will be next to each other. So instead of checking every index, we can use **binary search to find the first occurrence** of `target`, then collect consecutive indices until the values are no longer equal to it.

If the target doesn't exist in the array, the result will simply be an empty list.

## Approach

1. Sort `nums` in ascending order.
2. Use `bisect_left()` to find the first index where `target` could be inserted without breaking the sorted order. This gives the first occurrence of `target`, if it exists.
3. Starting from that index, keep appending indices to `ans` while the current element equals `target`.
4. Return `ans`.

## Complexity

- **Time complexity:** \(O(n\log n)\), because sorting dominates the runtime. The binary search takes \(O(\log n)\), and collecting the matching indices takes at most \(O(n)\).
- **Space complexity:** \(O(n)\) for the resulting list in the worst case. Sorting may also require additional space depending on the implementation.

## Code

```python3
class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()

        ind = bisect_left(nums, target)
        ans = []

        while ind < len(nums) and nums[ind] == target:
            ans.append(ind)
            ind += 1

        return ans
```