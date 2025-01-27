class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even_arr = []
        odd = []

        for num in nums:
            if num >=0:
                even_arr.append(num)
            else:
                odd.append(num)

        res = []

        for i in range(len(even_arr)):
            res.append(even_arr[i])
            res.append(odd[i])

        return res
