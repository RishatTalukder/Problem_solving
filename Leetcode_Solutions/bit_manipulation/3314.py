class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            val = -1
            for j in range(1, i):
                if (j | j+1) == i:
                    val = j
                    break

            ans.append(val)

        return ans
