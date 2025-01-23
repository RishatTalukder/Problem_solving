class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        """
        Takes a string s and an integer k as inputs, and then
        returns the maximum number of vowels that appear in
        any substring of s with length k.
        """
        # do all the inclusion checks once at the start
        isVowel = [c in {'a','e','i','o','u'} for c in s]
        # get initial number (which is also initial max)
        maxVowels = nowVowels = sum(isVowel[:k])
        # highest possible is substring of all vowels
        if maxVowels == k: return k
        # iterate over remaining characters
        for i in range(k,len(s)):
            # check if character leaving substring is vowel
            if isVowel[i-k]: nowVowels -=1
            # check if character entering substring is vowel
            if isVowel[i]: nowVowels += 1
            # check if found a new maximum
            if nowVowels > maxVowels: maxVowels = nowVowels
            # check if reached highest possible
            if maxVowels == k: return k
        # if never reached highest possible, return max
        return maxVowels
    
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        is_vowel = [c in {'a', 'e', 'i', 'o', 'u'} for c in s]

        max_vowels = curr_vowels = sum(is_vowel[:k])

        if max_vowels == k:
            return k
        
        for i in range(k, len(s)):
            if is_vowel[i-k]:
                curr_vowels -= 1

            if is_vowel[i]:
                curr_vowels += 1

            if curr_vowels > max_vowels:
                max_vowels = curr_vowels

            if max_vowels == k:
                return k
            
        return max_vowels