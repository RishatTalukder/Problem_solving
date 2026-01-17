class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        MOD = 10**9 + 7
        h = self.get_edges(hFences, m)
        v = self.get_edges(vFences, n)

        max_edge = max(h & v, default=0)
        return (max_edge*max_edge)%MOD if max_edge else -1
        

    def get_edges(self, fences, border):
        points = sorted([1]+fences + [border])
        sett = set()
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                sett.add(points[j] - points[i])

        return sett

    