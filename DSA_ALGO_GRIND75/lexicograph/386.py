class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        start = 1

        for i in range(n):
            arr.append(start)
            if start*10 <= n:
                start = start*10
            
            else:
                while start%10==9 or start >=n:
                    start = start // 10    
                start += 1

        return arr
    

#same problem but using recursion

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        arr = []
        def dfs(start):
            if start > n:
                return
            arr.append(start)
            for i in range(10):
                if 10*start+i <= n:
                    dfs(10*start+i)
        for i in range(1,10):
            dfs(i)
        return arr
    
#same problem but using trie
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = {}
        for i in range(1,n+1):
            node = trie
            for c in str(i):
                if c not in node:
                    node[c] = {}
                node = node[c]
        res = []
        def dfs(node):
            for key in node:
                res.append(int(key))
                dfs(node[key])
        dfs(trie)
        return res