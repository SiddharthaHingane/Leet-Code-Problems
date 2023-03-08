class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        l, r, N = matrix[0][0], matrix[-1][-1], len(matrix)

        def helper(m):
            cnt = 0
            for i in range(N):
                x = bisect_right(matrix[i], m)
                cnt += x
            return cnt

        while l < r:
            mid = (l + r) // 2
            if helper(mid) < k:
                l = mid + 1
            else:
                r = mid
        return l
