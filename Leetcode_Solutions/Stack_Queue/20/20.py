class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }

        brackets = []

        for ch in s:
            if ch not in hashmap:
                if not brackets:  # noqa: SIM114
                    return False
                    
                elif ch != brackets.pop():
                    return False

            elif ch in hashmap:
                brackets.append(hashmap[ch])

        return bool(not brackets)


class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        stack = []

        for ch in s:
            if ch not in hashmap:
                if len(stack) == 0 or len(stack) > 0 and stack.pop() != ch:
                    return False

            elif ch in hashmap:
                stack.append(hashmap[ch])

        return len(stack) == 0

class Solution:
    def isValid(self, s: str) -> bool:
        hash = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        stack = []

        for ch in s:
            if ch not in hash:
                if len(stack) == 0 or stack.pop() != ch:
                    return False

            elif ch in hash:
                stack.append(hash[ch])
                

        return len(stack) == 0