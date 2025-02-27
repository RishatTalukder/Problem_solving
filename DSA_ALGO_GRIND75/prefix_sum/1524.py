class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        sums = 0
        oddCount = 0

        for i in range(n):
            sums += arr[i]
            if sums % 2:
                oddCount += 1

        oddCount += (n - oddCount)*oddCount
        return oddCount % MOD