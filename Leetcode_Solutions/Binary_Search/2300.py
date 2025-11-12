import bisect
import math
from typing import List


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        c_potion = len(potions)
        result = []

        for spell in spells:
            required = math.ceil(success / spell)

            if required > potions[-1]:
                result.append(0)
                continue

            ind = bisect.bisect_left(potions, required)
            result.append(c_potion - ind)

        return result