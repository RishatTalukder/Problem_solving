I used `prefix` and `postfix` to solve `product of array except self` problem. I think it is a good way to solve this kind of problem. I will use it in the future.

```python


class Solution:
    def productExceptSelf(self, nums):
        result = []

        for i in range(len(nums)):
            product = 1

            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]

            result.append(product)

        return result