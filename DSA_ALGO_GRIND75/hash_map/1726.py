class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        product = {}
        res = 0
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                p = nums[i] * nums[j]
                product[p] = product.get(p, 0) + 1

        for p in product:
            res += product[p] * (product[p] - 1) // 2

        return res * 8