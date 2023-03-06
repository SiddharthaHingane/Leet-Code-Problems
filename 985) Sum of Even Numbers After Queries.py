class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evnesum = sum(i for i in nums if i % 2 == 0)
        for i in range(len(queries)):
            val, id = queries[i]
            if nums[id] % 2 == 0: evnesum -= nums[id]
            nums[id] += val
            if nums[id] % 2 == 0: evnesum += nums[id]
            queries[i] = evnesum
        return queries
