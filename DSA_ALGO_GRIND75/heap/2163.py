class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n3, n = len(nums), len(nums) // 3

        # step 1: min prefix sum of n elements using max heap
        part1 = [0] * (n + 1)
        total = sum(nums[:n])
        ql = [-x for x in nums[:n]]  # simulate max heap
        heapq.heapify(ql)
        part1[0] = total

        for i in range(n, 2 * n):
            total += nums[i]
            heapq.heappush(ql, -nums[i])
            total -= -heapq.heappop(ql)
            part1[i - (n - 1)] = total

        # step 2: max suffix sum of n elements using min heap
        part2_sum = sum(nums[2 * n:])
        qr = nums[2 * n:]
        heapq.heapify(qr)
        ans = part1[n] - part2_sum

        for i in range(2 * n - 1, n - 1, -1):
            part2_sum += nums[i]
            heapq.heappush(qr, nums[i])
            part2_sum -= heapq.heappop(qr)
            ans = min(ans, part1[i - n] - part2_sum)

        return ans
