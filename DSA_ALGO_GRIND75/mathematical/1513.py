class Solution:
    def numSub(self, s: str) -> int:
        const = 10**9 + 7
        total = 0
        c = 0

        for i in s:
            if i == '0':
                total += c*(c+1)//2
                c = 0

            else:
                c += 1


        total += c*(c+1)//2
        total %= const

        return total