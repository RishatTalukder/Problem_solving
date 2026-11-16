from collections import deque

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        q = deque(map(int, list(s)))
        
        while len(q) > k:
            summ = []
            
            while q:
                batch = []

                for i in range(k):
                    if q:
                        batch.append(q.popleft())
                    else:
                        break
                batch = list(map(int, str(sum(batch))))
                summ.extend(batch)

            q = deque(summ)

        return ''.join(map(str, list(q)))
