class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)

        t = num[:]
        pos = 0
        while pos < len(num) and num[pos] == '9':
            pos += 1

        if pos < len(num):
            num = num.replace(num[pos], '9')

        t = t.replace(t[0], '0')

        return int(num) - int(t)