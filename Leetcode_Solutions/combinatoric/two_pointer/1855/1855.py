class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = p2 = 0
        ans = 0

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2] and p1 <= p2:
                ans = max(ans, p2 - p1)
                p2 += 1
            else:
                p1 += 1
                if p2 < p1:
                    p2 = p1

        return ans