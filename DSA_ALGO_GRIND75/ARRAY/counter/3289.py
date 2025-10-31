class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        c = Counter(nums)

        ans = []

        for i in c:
            if c[i] == 2:
                ans.append(i)

        return ans