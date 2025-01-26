from collections import deque


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        index_on_groups = {}

        for num in sorted(nums):
            if not groups or abs(num - groups[-1][-1]) > limit:
                groups.append(deque())
            
            groups[-1].append(num)
            index_on_groups[num] = len(groups) - 1

        res = []

        for num in nums:
            group = groups[index_on_groups[num]]
            res.append(group.popleft())


        return res