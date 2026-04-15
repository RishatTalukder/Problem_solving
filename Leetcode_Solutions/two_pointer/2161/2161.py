class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l,m,r = [],[],[]

        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                m.append(num)
            else:
                r.append(num)

        return l + m + r