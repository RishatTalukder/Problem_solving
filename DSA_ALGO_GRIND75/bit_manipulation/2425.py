from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1,len2 = len(nums1), len(nums2)
        count = {}

        for num in nums1:
            count[num] = count.get(num,0)+len2

        for num in nums2:
            count[num] = count.get(num,0)+len1

        ans = 0

        for num in count:
            if count[num]%2:
                ans^=num

        return ans
    
#another approach faster
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        len1 ,len2 = len(nums1), len(nums2)

        ans = 0

        if len2%2:
            for num in nums1:
                ans^=num

        if len1%2:
            for num in nums2:
                ans^=num

        return ans

            
    

sol = Solution()
print(sol.xorAllNums([2,1,3],[10,2,5,0])) # 13