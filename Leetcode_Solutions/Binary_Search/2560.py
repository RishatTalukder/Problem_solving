class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        min_reward = 1
        max_reward = max(nums)
        total_houses = len(nums)

        while min_reward < max_reward:
            mid = (min_reward + max_reward) // 2
            possible_thefts = 0
            ind = 0

            while ind < total_houses:
                if nums[ind] <= mid:
                    possible_thefts += 1
                    ind += 2

                else:
                    ind += 1

            if possible_thefts >= k:
                max_reward = mid

            else:
                min_reward = mid + 1

        return min_reward