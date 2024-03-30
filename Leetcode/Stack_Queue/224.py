class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: current env's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0')) # ord() returns an integer representing the Unicode character
            elif c == '(':
                stack.append(sign)  # Push current sign to stack
            elif c == ')':
                stack.pop()  # Pop the last sign from stack
            elif c == '+' or c == '-':
                ans += sign * num  # Add the previous number to the answer
                sign = (1 if c == '+' else -1) * stack[-1]  # Update the sign based on the current character and the last sign in stack
                num = 0  # Reset the number

        return ans + sign * num  # Add the last number to the answer
