class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        if x < y:
            x, y = y, x
            s = s[::-1]

        a_count = 0
        b_count = 0
        result = 0

        for char in s:
            if char == 'a':
                a_count += 1
            elif char == 'b':
                if a_count > 0:
                    a_count -= 1
                    result += x

                else:
                    b_count += 1
            else:
                res += min(a_count, b_count) * y
                a_count = 0
                b_count = 0

        result += min(a_count, b_count) * y
        return result