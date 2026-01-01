class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int("".join(map(str, digits)))

        num += 1

        return list(map(int, str(num)))
    

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1

        while digits[i] == 9 and i >= -len(digits):
            digits[i] = 0
            i -= 1

        if i == -len(digits)-1:
            digits.insert(0, 1)
        else:
            digits[i] += 1

        return digits