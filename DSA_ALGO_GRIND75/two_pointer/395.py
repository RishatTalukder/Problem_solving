from collections import Counter

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        """
        This function finds the length of the longest substring of a given string `s` 
        where each character in the substring appears at least `k` times.

        Approach:
        1. If the length of the string `s` is less than `k`, return 0 because it's 
           impossible to have any substring where each character appears at least `k` times.
        2. Iterate through each unique character in the string `s`.
        3. If the count of the current character in the string is less than `k`, split 
           the string by this character. This means that any valid substring cannot 
           contain this character.
        4. Recursively call the function on each split part and store the lengths of 
           the valid substrings.
        5. Return the maximum length from the valid substrings.
        6. If all characters in the string appear at least `k` times, return the length 
           of the entire string `s`.

        :param s: Input string
        :param k: Minimum frequency of each character in the substring
        :return: Length of the longest substring where each character appears at least `k` times
        """
        if len(s) < k:
            return 0

        for char in set(s):
            if s.count(char) < k:
                split_reletive_to_char = s.split(char)
                maxx_lens = []
                for strng in split_reletive_to_char:
                    maxx_lens.append(self.longestSubstring(strng, k))

                return max(maxx_lens)
        
        return len(s)
    

s = "ababab"
k = 3

print(Solution().longestSubstring(s, k))