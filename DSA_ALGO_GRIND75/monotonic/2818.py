def countPrimeFactors(n):
    factor = 2
    prime_factors = set()
    while factor * factor <= n:
        while n % factor == 0:
            prime_factors.add(factor)
            n //= factor
        factor += 1
    if n > 1:
        prime_factors.add(n)
    return len(prime_factors)


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Precompute prime factor counts for each number in nums
        num_info = [(index, countPrimeFactors(value), value) for index, value in enumerate(nums)]

        # Arrays to store the nearest greater element indices on the left and right
        nearest_greater_left = [-1] * n
        nearest_greater_right = [n] * n

        # Compute nearest greater element indices on the left
        stack = []
        for index, prime_count, value in num_info:
            while stack and stack[-1][0] < prime_count:
                stack.pop()
            if stack:
                nearest_greater_left[index] = stack[-1][1]
            stack.append((prime_count, index))

        # Compute nearest greater element indices on the right
        stack = []
        for index, prime_count, value in reversed(num_info):
            while stack and stack[-1][0] <= prime_count:
                stack.pop()
            if stack:
                nearest_greater_right[index] = stack[-1][1]
            stack.append((prime_count, index))

        # Sort numbers by value in descending order
        num_info.sort(key=lambda x: -x[2])

        result = 1
        for index, prime_count, value in num_info:
            left_bound = nearest_greater_left[index]
            right_bound = nearest_greater_right[index]
            contribution_count = (index - left_bound) * (right_bound - index)

            if contribution_count <= k:
                result = result * pow(value, contribution_count, MOD) % MOD
                k -= contribution_count
            else:
                result = result * pow(value, k, MOD) % MOD
                break

        return result