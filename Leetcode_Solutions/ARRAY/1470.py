class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        final = []

        x = nums[:n]
        y = nums[n:]

        for i in range(n):
            final.append(x[i])
            final.append(y[i])

        return final
