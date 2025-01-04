from collections import defaultdict
from random import choice
class Solution:

    def __init__(self, nums: List[int]):
        self.index_map = defaultdict(list)

        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.index_map[target])


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)