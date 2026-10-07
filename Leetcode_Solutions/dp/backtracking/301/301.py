class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        res = set()
        maxlen = 0

        def solve(s, index, curr, count):
            nonlocal maxlen

            if count < 0:
                return

            if index == n:
                if count == 0:
                    if len(curr) > maxlen:
                        maxlen = len(curr)
                        res.clear()
                        res.add(''.join(curr))

                    elif len(curr) == maxlen:
                        res.add(''.join(curr))

                return

            if s[index] != ')' and s[index] != '(':
                curr.append(s[index])
                solve(s, index + 1, curr, count)
                curr.pop()
                return

            curr.append(s[index])

            solve(
                s,
                index + 1,
                curr,
                count + (1 if s[index] == '(' else -1)
            )

            curr.pop()

            solve(
                s,
                index + 1,
                curr,
                count
            )

        solve(s, 0, [], 0)

        return list(res)