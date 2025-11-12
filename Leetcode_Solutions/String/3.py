class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 #declaring a left pointer
        right = 0 #declaring a right pointer
        result = 0 #declaring a variable to store the result
        characters = set() #declaring a set to store the characters of the string

        #looping through the string using the right pointer
        while right < len(s):
            #if the character is already in the set
            if s[right] in characters:
                characters.remove(s[left]) #removing the character from the set
                left += 1 #increasing the left pointer by 1
            #if the character is not in the set
            else:
                characters.add(s[right]) #adding the character to the set
                right += 1 #increasing the right pointer by 1

            #checking if the length of the set is greater than the result
            if len(characters) > result:
                result = len(characters) #updating the result

        return result #returning the result