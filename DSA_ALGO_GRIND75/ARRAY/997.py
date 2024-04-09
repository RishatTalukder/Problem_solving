class Solution:
    def findJudge(self, n: int, trust) -> int:
        if n == 1 or trust == []:
            return -1

        hashmap = {}

        for a,b in trust:
            if a not in hashmap:
                hashmap[a] = [b]

            else:
                hashmap[a].append(b)

        keys = hashmap.keys()

        if len(keys) == n:
            return -1

        n = list(range(1,n+1))

        for i in keys:
            if i in n:
                n.remove(i)


        return n[-1]


n = 3
trust = [[1,2],[2,3]]

sol = Solution()

print(sol.findJudge(n,trust))



        
