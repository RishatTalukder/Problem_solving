from typing import List
from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        ind_map = {}

        for i in range(len(nums)):
            if nums[i] not in ind_map:
                ind_map[nums[i]] = [i]
            else:
                ind_map[nums[i]].append(i)

        count = 0
        if k in ind_map:
            count += len(ind_map[k])

        maxx_freq = 0
        maxx_count = 0
        left = 0

        for ind in ind_map[k]:
            sub_count = Counter(nums[left:ind]).values()
            maxx_count = max(list(sub_count)) if sub_count else maxx_count
            maxx_freq = max(maxx_freq, maxx_count)
            left = ind + 1

        if nums[left:]:
            sub_count = Counter(nums[left:ind]).values()
            maxx_count = max(list(sub_count)) if sub_count else maxx_count
            maxx_freq = max(maxx_freq, maxx_count)
            left = ind + 1

        return maxx_freq
    

sol = Solution()

print(sol.maxFrequency([1,2,3,4,5,6], k = 1))