***KADANE's ALGORITHM***

**Problem Statement:** Given an array of integers, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**
```
Input: [-2,1,-3,4,-1,2,1,-5,4],

Output: 6

Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Solution steps:**

1. Initialize:
    - `max_so_far` = `max_ending_here` = 0

2. Loop for each element of the array
    - `max_ending_here` = `max_ending_here` + `a[i]`
    - if(`max_so_far` < `max_ending_here`)
        - `max_so_far` = `max_ending_here`

3. return `max_so_far`

**Solution:**
```python

def maxSubArray(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_so_far = max_ending_here = 0
    for i in nums:
        max_ending_here += i
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
    return max_so_far
```

