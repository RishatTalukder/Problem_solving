class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding Window Algorithm

        Steps:
        1. Initialize an empty dictionary to store the characters and their indices.
        2. Initialize two pointers, start and end, both pointing to the beginning of the string.
        3. Initialize a variable max_len to store the maximum length of the substring.
        4. Iterate through the string using the end pointer:
            - If the current character is already in the dictionary, update the start pointer to the next index of the duplicate character.
            - Update the max_len if the current substring length is greater than max_len.
            - Add the current character and its index to the dictionary.
            - Move the end pointer to the next index.
        5. Return the max_len as the length of the longest substring without repeating characters.
        """
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        dict = {}
        start = 0
        end = 0
        max_len = 0
        while end < len(s):
            if s[end] in dict:
                start = max(start, dict[s[end]] + 1)
            max_len = max(max_len, end - start + 1)
            dict[s[end]] = end
            end += 1
        return max_len
