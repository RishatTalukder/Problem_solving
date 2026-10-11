class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        i = 0
        count = 0

        while i < len(s):
            if s[i] =='(':
                stack.append(s[i])
                i += 1

            else:
                if i+1 < len(s) and s[i+1] == ')' :
                    if stack:
                        stack.pop()

                    else:
                        count += 1

                    i += 2

                else:
                    count += 1
                    if stack:
                        stack.pop()

                    else:
                        count += 1 

                    i += 1


        return count + len(stack)*2