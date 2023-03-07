class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = zip(efficiency, speed)
        eng = sorted(eng, key=lambda x: x[0], reverse=True)
        sumSpeed, res = 0, 0
        speedHeap = []
        for e, s in eng:
            heapq.heappush(speedHeap, s)
            sumSpeed += s
            if len(speedHeap) > k:
                sumSpeed -= heapq.heappop(speedHeap)

            res = max(res, sumSpeed * e)
        return res % (10 ** 9 + 7)
