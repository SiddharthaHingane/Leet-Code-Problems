class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                total +=1
            else:
                total = 0
            res += total
        return res
