class Solution:
    """
    A class used to decode a given encoded string.
    Methods
    -------
    decodeString(s: str) -> str
        Decodes the encoded string `s` and returns the decoded string.
    decodeString(s: str) -> str:
        Decodes the encoded string `s` using a stack-based approach.
        Parameters:
        s (str): The encoded string containing digits, letters, and square brackets.
        Returns:
        str: The decoded string.
        Approach:
        - Initialize an empty string `curr` to store the current decoded substring.
        - Initialize an empty deque `stack` to store tuples of (previous decoded substring, repeat count).
        - Initialize an integer `num` to store the current number being processed.
        - Iterate through each character in the string `s`:
            - If the character is a digit, update `num` to form the complete number.
            - If the character is '[', push the current `curr` and `num` onto the stack, and reset `curr` and `num`.
            - If the character is ']', pop from the stack to get the previous substring and repeat count, and update `curr` by repeating the current substring `count` times and appending it to the previous substring.
            - If the character is a letter, append it to `curr`.
        - Return the final decoded string `curr`.
    """
    def decodeString(self, s: str) -> str:
        curr = ""
        stack = deque()
        num = 0

        for char in s:
            if char.isdigit():
                num = num*10 + int(char)

            elif char == "[":
                stack.append((curr, num))
                curr = ""
                num = 0

            elif char=="]":
                prev, count = stack.pop()
                curr = prev+curr*count
            
            else:
                curr += char
            
        return curr