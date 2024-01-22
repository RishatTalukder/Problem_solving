class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        resultLen = 0

        for i in range(len(s)):
            #checking for the odd palingdrome
            left = i
            right = i

            # expanding the string from the middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resultLen:
                    resultLen = right - left + 1
                    result = s[left:right+1]
                left -= 1
                right += 1

            #checking for the even palingdrome
            left = i
            right = i + 1

            # expanding the string from the middle
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > resultLen:
                    resultLen = right - left + 1
                    result = s[left:right+1]
                left -= 1
                right += 1

        return result