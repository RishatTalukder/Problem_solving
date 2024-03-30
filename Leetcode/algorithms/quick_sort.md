# quick sort

This is a advanced sorting algorithm. the concept is easy but the implementation is a little bit tricky. It's a little faster than `bubble sort` because the time complexity of `quick sort` is `O(nlogn)` and the time complexity of `bubble sort` is `O(n^2)`.

**_Solution steps:_**

1. Create a `partition` function that takes `nums`, `low` and `high` as arguments.

2. Create a variable `pivot` and set it to the `item` in the `high` index.

3. Create a variable `i` and set it to `low-1`.

4. Loop through the `nums` list from `low` to `high`. 

5. Check if the `item` in the `index` is less than or equal to the `pivot` or not.

6. If the `item` in the `index` is less than or equal to the `pivot` then increase the `i` variable by `1` and swap the `item` in the `index` with the `item` in the `i` index.

7. After the loop ends swap the `item` in the `i+1` index with the `item` in the `high` index.

8. Return the `i+1` index.

9. Create a `quick_sort` function that takes `nums`, `low` and `high` as arguments.

10. Check if the `low` is less than the `high` or not.

11. If the `low` is less than the `high` then call the `partition` function with `nums`, `low` and `high` as arguments and store the `partition` index in a variable `pi`.

12. Call the `quick_sort` function with `nums`, `low` and `pi-1` as arguments.

13. Call the `quick_sort` function with `nums`, `pi+1` and `high` as arguments.

14. Return the `nums` list.

**_Solution in python:_**

I will just follow the steps I mentioned above.

```python

class Solution:
    def sortColors(self, nums):
        def partition(nums, low, high):
            pivot = nums[high]
            i = low-1

            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]

            nums[i+1], nums[high] = nums[high], nums[i+1]

            return i+1

        def quick_sort(nums, low, high):
            if low < high:
                pi = partition(nums, low, high)

                quick_sort(nums, low, pi-1)
                quick_sort(nums, pi+1, high)

        quick_sort(nums, 0, len(nums)-1)

        return nums

```

Solved problems using `quick sort`:

- [Sort Colors](https://leetcode.com/problems/sort-colors/)