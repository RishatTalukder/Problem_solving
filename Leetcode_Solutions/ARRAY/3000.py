class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mdiag = -1
        marea = -1

        for l, w in dimensions:
            diag = l**2 + w**2
            area = l*w

            if diag > mdiag or (mdiag == diag and area>marea):
                mdiag = diag
                marea = area

        return marea
