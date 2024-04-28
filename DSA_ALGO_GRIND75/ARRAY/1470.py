class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = [0]*len(nums)

        x = nums[:n]
        y = nums[n:]
        i = 0
        for xi,yi in zip(x,y):
            final[i],final[i+1] = xi, yi
            i += 2

        return final
