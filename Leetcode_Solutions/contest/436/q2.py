from typing import List

class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        res = []
        element_map = {}

        for group in groups:
            if group in element_map:
                res.append(element_map[group])
                continue

            element_ind = -1
            for i, element in enumerate(elements):
                if group % element == 0:
                    element_ind = i
                    break

            element_map[group] = element_ind
            res.append(element_ind)

        return res
