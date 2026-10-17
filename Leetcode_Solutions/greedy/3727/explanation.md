# Intuition

The key idea is to **sort the numbers by their absolute values and place the smaller ones where they will be subtracted, while placing the larger ones where they will be added.**

Since we're working with squares, the sign of a number doesn't matter. For example, \((-5)^2 = 5^2 = 25\). So, we can focus entirely on the absolute values.

To maximize the alternating sum, we want the largest squares to contribute positively and the smallest squares to contribute negatively. Sorting by absolute value lets us split the array into two halves to achieve this.

# Approach

1. Sort `nums` by absolute value in ascending order.
2. Split the sorted array into two halves:
   - `left` contains the smaller absolute values, whose squares will be subtracted.
   - `right` contains the larger absolute values, whose squares will be added.
3. Pair each element in `left` with the corresponding element in `right` and add the difference between their squares to `ans`.
4. If `right` contains one extra element, add its square separately.
5. If there's only one element, return its square directly.

# Complexity

- Time complexity: \(O(n\log n)\), due to sorting the array.
- Space complexity: \(O(n)\), because slicing creates new lists for `left` and `right`.

# Code

```python3
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]**2

        nums.sort(key=lambda x: abs(x))

        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]

        ans = 0

        for i in range(len(left)):
            ans += right[i]**2 - left[i]**2

        return ans + (right[i+1]**2 if i+1 < len(right) else 0)
```