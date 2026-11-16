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
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd_prefixes = 0
        even_prefixes = 1

        prefix_sum = 0
        result = 0

        for num in arr:
            prefix_sum += num

            if prefix_sum % 2:
                result += even_prefixes
                odd_prefixes += 1
            else:
                result += odd_prefixes
                even_prefixes += 1

        return result % MOD
