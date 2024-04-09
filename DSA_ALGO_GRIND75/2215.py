a = [1,2,3,3]
b = [1,1,2,2]

from collections import Counter

# a = Counter(a)
# b = Counter(b)

# list_a = list(a.keys())
# list_b = list(b.keys())

# for i in list_a:
#     if i in list_b:
#         del a[i]
#         del b[i]

# print(a,b)


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)

        list_num1 = list(nums1.keys())
        list_num2 = list(nums2.keys())

        for i in list_num1:
            if i in list_num2:
                del nums1[i]
                del nums2[i]

        return [list(nums1.keys()),list(nums2.keys())]
    


print(Solution().findDifference(a,b))