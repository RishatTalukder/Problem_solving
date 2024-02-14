class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negetive = []
        final = [0]*len(nums)
        for i in nums:
            if i > 0:
                positive.append(i)

            else:
                negetive.append(i)

        for i in range(0,len(nums),2):
            final[i] = positive[i//2]
            final[i+1] = negetive[i//2]

        return final
