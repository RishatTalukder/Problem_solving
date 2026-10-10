class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        maxln = 0
        res = set()
        
        def backtrack(s, i, cur, count):
            nonlocal maxln
            if count < 0:
                return

            if i == n:
                if count == 0:
                    if len(cur) > maxln:
                        maxln = len(cur)
                        res.clear()
                        res.add(''.join(cur))

                    if len(cur) == maxln:
                        res.add(''.join(cur))

                return

            if s[i] not in '()':
                cur.append(s[i])
                backtrack(s, i+1, cur, count)
                cur.pop()
                return

            cur.append(s[i])

            backtrack(
                s,
                i+1,
                cur,
                count + (1 if s[i] == '(' else -1)
            )

            cur.pop()

            backtrack(
                s,
                i+1,
                cur,
                count
            )

        
        backtrack(s, 0, [], 0)

        return list(res)