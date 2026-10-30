class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0


        start = nums.index(0)

        asc = True
        dsc = True

        for i in range(1, n):
            val = nums[(start+i)%n]

            if val != i:
                asc = False

            if val != n-i:
                dsc = False

            if asc == dsc == False:
                return -1


        if asc:
            return min(start, n-start + 2)

        return min(n-start, start + 2)