class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        count = 0

        i = 0

        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1

            else:
                if i < len(s)-1 and s[i+1] == ')':
                    if not stack:
                        count += 1

                    else:
                        stack.pop()

                    i += 2

                else: 
                    count += 1
                    if not stack:
                        count += 1
                    else:
                        stack.pop()

                    i += 1


        return count + (len(stack)*2)