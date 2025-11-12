class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = { 'a': 0, 'b': 0, 'c': 0 }  # Dictionary to track occurrences
        left = 0  # Left pointer
        result = 0  # Store the count of valid substrings
        
        for right in range(len(s)):  # Expand right pointer
            count[s[right]] += 1  # Add current character to window
            
            # Check if window contains all 'a', 'b', 'c'
            while count['a'] > 0 and count['b'] > 0 and count['c'] > 0:
                result += len(s) - right  # All substrings from [left, right] to end are valid
                count[s[left]] -= 1  # Shrink window from left
                left += 1  # Move left pointer forward
        
        return result
