class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n//7
        start = 28
        end = 28 + 7*(weeks-1)
        summ = weeks*(start+end)//2

        last_monday = weeks+1
        last_week = 0

        for day in range(n%7):
            last_week += last_monday+day

        return summ+last_week