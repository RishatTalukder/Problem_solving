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

        return True if not brackets else False