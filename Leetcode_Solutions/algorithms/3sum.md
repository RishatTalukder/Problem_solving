**_ 3SUM Algorithm _**

## 3SUM Algorithm

### Description

Given an array of integers, find all unique triplets in the array which gives the sum of zero.

### Example

Given array `S = [-1, 0, 1, 2, -1, -4]`, a solution set is:

```
[
  [-1, 0, 1],
  [-1, -1, 2]
]
```

### Solution

```python

 def threeSum(self, nums):
        nums.sort()
        result = []

        for i in range(len(nums)):
            left = i+1
            right = len(nums)-1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == 0:
                    triplet = [nums[i], nums[left], nums[right]]
                    triplet.sort()

                    if triplet not in result:
                        result.append(triplet)

                    left += 1
                    right -= 1

                elif sum < 0:
                    left += 1

                else:
                    right -= 1

        return result
```
