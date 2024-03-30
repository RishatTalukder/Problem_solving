class Solution:
    def evalRPN(self, tokens) -> int:
        stack = []

        while tokens:
            op = tokens.pop(0)
            if op == "+" or op == "-" or op == "/" or op == "*":
                b = stack.pop()
                a = stack.pop()
                if op == "+":
                    stack.append(a + b)
                elif op == "-":
                    stack.append(a - b)
                elif op == "*":
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))

            else:
                stack.append(int(op))

        return stack.pop()
    

if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(["2", "1", "+", "3", "*"]))
    print(s.evalRPN(["4", "13", "5", "/", "+"]))
    print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))