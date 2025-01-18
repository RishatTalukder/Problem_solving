
from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s) #counting the characters of the string
        result = 0 #declaring a variable to store the result
        odd = 0 #declaring a variable to store the odd characters
        
        values = counter.values() #getting the values of the counter

        #looping through the values
        for value in values:
            #if the value is even
            if value % 2 == 0:
                result += value #adding the value to the result
            #if the value is odd
            else:
                result += value - 1 #adding the value - 1 to the result
                odd += 1 #adding 1 to the odd variable

        #if there are more than 0 odd characters left
        if odd > 0:
            result += 1 #adding 1 to the result

        return result #returning the result
    


class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_count = Counter(s)

        odds = 0
        result = 0

        for i in s_count.values();
            if i%2 == 0:
                result+=i
            
            else:
                result+=i-1
                odds+= 1


        if odds:
            result += 1


        return result