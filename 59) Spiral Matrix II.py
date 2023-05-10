class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        L, R, T, B = 0, n-1, 0, n-1
        mat = [[0] * n for _ in range(n)]
        val = 0

        while L <= R and T <= B:
            for c in range(L, R+1):
                val += 1
                mat[T][c] = val
            T += 1

            for r in range(T, B+1):
                val += 1
                mat[r][R] = val
            R -= 1

            if T <= B:
                for c in range(R, L-1, -1):
                    val += 1
                    mat[B][c] = val
                B -= 1
            
            if L <= R:
                for r in range(B, T-1, -1):
                    val += 1
                    mat[r][L] = val
                L += 1
        return mat
