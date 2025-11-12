class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        t = s[:]
        pos = 0

        while pos < len(s) and s[pos] == '9':
            pos += 1

        s = s if pos == len(s) else s.replace(s[pos],'9')

        pos = 1
        if t[0] != '1':
            t = t.replace(t[0], '1')

        else:
            while pos < len(t) and t[pos] in ['0', '1']:
                pos += 1


            t = t if pos==len(t) else t.replace(t[pos],'0')


        return abs(int(s)-int(t))
