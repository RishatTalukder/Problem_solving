from itertools import combinations


class Solution:
    def largestSquareArea(
        self, bottomLeft: List[List[int]], topRight: List[List[int]]
    ) -> int:
        max_size = 0

        for i, j in combinations(zip(bottomLeft, topRight), 2):

            (bottom_left_i, top_right_i) = i
            (bottom_left_j,top_right_j) = j
            w = min(top_right_i[0], top_right_j[0]) - max(
                bottom_left_i[0], bottom_left_j[0]
            )
            h = min(top_right_i[1], top_right_j[1]) - max(
                bottom_left_i[1], bottom_left_j[1]
            )

            max_size = max(max_size, min(w, h))

        return max_size * max_size 
    

class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        size = 0

        for i, j in combinations(zip(bottomLeft, topRight), 2):
            bli,tri = i
            blj,trj = j

            w = min(tri[0],trj[0]) - max(bli[0], blj[0])
            h = min(tri[1],trj[1]) - max(bli[1], blj[1])

            size = max(size, min(w,h))


        return size*size
            