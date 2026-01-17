from collections import defaultdict


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result_map = defaultdict(int)

        for num, score in nums1:
            result_map[num] += score

        for num, score in nums2:
            result_map[num] += score

        result_map = sorted(result_map.items())
        
        return result_map
    

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ans = defaultdict(int)

        for id, val in nums1:
            ans[id] += val

        for id, val in nums2:
            ans[id] += val

        
        ans = sorted(ans.items())

        return ans