class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        result = high

        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # Skip the next element as it's paired
                else:
                    i += 1  # Move to the next element
            return count >= p

        while low <= high:
            mid = (low + high) // 2
            if can_form_pairs(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result