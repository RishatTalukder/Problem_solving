from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        adj_list = defaultdict(list)

        for a,b in trust:
            adj_list[a].append(b)

        for i in range(1,n+1):
            if len(adj_list[i]) == 0:
                judge = i
                break
        else:
            return -1

        for i in range(1,n+1):
            if i == judge:
                continue
            if judge not in adj_list[i]:
                return -1
            
        return judge