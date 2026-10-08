class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        n = len(s)
        res = set()
        maxln = 0

        def solve(s, i, curr, count):
            nonlocal maxln

            if count < 0 :
                return


            if i == n:
                if count == 0:
                    if len(curr) > maxln:
                        maxln = len(curr)
                        res.clear()
                        res.add(''.join(curr))

                    elif len(curr) == maxln:
                        res.add(''.join(curr))


                return

            
            if s[i] not in '()':
                curr.append(s[i])
                solve(s, i+1, curr, count)
                curr.pop()
                return

            curr.append(s[i])

            solve(
                s,
                i+1,
                curr,
                count + (1 if s[i] == '(' else -1)
            )

            curr.pop()

            solve(
                s,
                i+1,
                curr, 
                count
            )

        solve(s, 0, [], 0)

        return list(res)