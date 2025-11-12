class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        from collections import Counter
        n = len(nums)
        freq = Counter(nums)
        dom, count = 0, 0

        for num, c in freq.items():
            if c > n//2:
                dom, count = num, c
                break

        left_count = 0

        for i in range(n-1):
            if nums[i] == dom:
                left_count += 1

            left_size = i + 1
            right_size = n - left_size
            right_count = count - left_count

            if left_count * 2 > left_size and right_count * 2 > right_size:
                return i
            
        return -1