class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sm = 0
        mx = 0

        for num in nums:
            if num == 1:
                sm += num
            else:
                mx = max(mx,sm)
                sm = 0

        mx = max(mx,sm)

        return mx

            