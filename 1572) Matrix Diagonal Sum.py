class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        R = len(mat)
        pD, sD = 0, 0
        for r in range(R):
            pD += mat[r][r]
            mat[r][r] = 0
        
        for r in range(R-1, -1, -1):
            sD += mat[R-r-1][r]

        return pD + sD
