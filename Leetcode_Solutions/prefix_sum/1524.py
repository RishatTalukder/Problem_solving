class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        sums = 0
        odd = 0

        for i in range(n):
            sums += arr[i]
            if sums % 2:
                odd += 1

        odd += (n - odd)*odd
        return odd % MOD



class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7

        even = 1
        odd = 0

        ans = 0
        pre = 0

        for i in arr:
            pre += i

            if pre%2:
                ans += even
                odd += 1

            else:
                ans += odd
                even += 1


        return ans%MOD
