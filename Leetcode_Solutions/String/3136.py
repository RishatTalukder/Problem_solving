class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        has_vowel = False
        has_consonant = False

        for c in word:
            if not (c.isalpha() or c.isdigit()):
                return False  # invalid character

            if c.isalpha():
                if c.lower() in vowel_set:
                    has_vowel = True
                else:
                    has_consonant = True

        return has_vowel and has_consonant
