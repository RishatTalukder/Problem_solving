class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowel_set and s[right] in vowel_set:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowel_set:
                left += 1
            if s[right] not in vowel_set:
                right -= 1

        return ''.join(s)