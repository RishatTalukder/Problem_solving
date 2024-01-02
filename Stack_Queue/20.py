class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            "(" : ")",  # Opening bracket "(" maps to closing bracket ")"
            "{" : "}",  # Opening bracket "{" maps to closing bracket "}"
            "[" : "]"   # Opening bracket "[" maps to closing bracket "]"
        }

        stack = []  # Initialize an empty stack

        for bracket in s:
            if bracket in pairs:  # If the bracket is an opening bracket
                stack.append(bracket)  # Push it onto the stack

            elif len(stack)==0 or bracket != pairs[stack.pop()]:  # If the bracket is a closing bracket
                return False  # Return False if the stack is empty or the closing bracket doesn't match the top of the stack

        return len(stack)==0  # Return True if the stack is empty, otherwise return False
