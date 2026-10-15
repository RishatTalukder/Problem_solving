class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        count = [0]*30

        for num in nums:
            for i in range(30):
                if num & (1<<i):
                    count[i] += 1

        res = 0

        for _ in range(k):
            cur = 0

            for i in range(29,-1,-1):
                if count[i] > 0:
                    cur |= (1 << i)
                    count[i] -= 1

            res = (res + cur**2)%MOD


        return res