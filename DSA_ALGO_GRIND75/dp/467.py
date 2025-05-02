class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        # dp[i] stores the max length of valid substring ending with chr(i + ord('a'))
        max_len_ending_with = [0] * 26
        current_length = 0

        for i in range(len(s)):
            # Check if current character continues a wraparound sequence
            if i > 0 and (ord(s[i]) - ord(s[i - 1]) == 1 or (s[i - 1] == 'z' and s[i] == 'a')):
                current_length += 1
            else:
                current_length = 1

            index = ord(s[i]) - ord('a')
            max_len_ending_with[index] = max(max_len_ending_with[index], current_length)

        # The sum of all max lengths gives the count of unique substrings
        return sum(max_len_ending_with)
