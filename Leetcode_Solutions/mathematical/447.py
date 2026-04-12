
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        boomer = 0 

        for a,b in points:
            dist = {}

            for x,y in points:
                d = (a-x)**2 + (b-y)**2
                
                if d in dist:
                    boomer += 2*dist[d]
                    dist[d] += 1

                else:
                    dist[d] = 1

        return boomer