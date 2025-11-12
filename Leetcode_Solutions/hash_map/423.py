from collections import Counter


class Solution:
    def originalDigits(self, s: str) -> str:
        count = Counter(s)
        result = [0] * 10

        result[0] = count['z']
        result[2] = count['w']
        result[4] = count['u']
        result[6] = count['x']
        result[8] = count['g']

        result[3] = count['h'] - result[8]
        result[5] = count['f'] - result[4]
        result[7] = count['s'] - result[6]

        result[1] = count['o'] - result[0] - result[2] - result[4]
        result[9] = count['i'] - result[5] - result[6] - result[8]

        return ''.join([str(i) * result[i] for i in range(10)])