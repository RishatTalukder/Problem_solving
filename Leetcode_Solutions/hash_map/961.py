class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        n = len(nums)//2

        for num in count:
            if count[num] == n:
                return num

            