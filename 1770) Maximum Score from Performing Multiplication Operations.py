class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        n = len(nums)
        dp = [0] * (m + 1)  # [0,0,0,0]
        # nums=[1, 2, 3], multipliers=[3, 2, 1]
        for op in range(m - 1, -1, -1):
            print("")
            print("-----")
            print("")
            next_row = dp.copy()
            print('next_row', next_row)
            print('op', op)
            for left in range(op, -1, -1):
                print('left', left)
                print('multipliers[op]',multipliers[op])
                print('nums[left]',nums[left])
                dp[left] = max(multipliers[op] * nums[left] + next_row[left + 1],
                               multipliers[op] * nums[n - 1 - (op - left)] + next_row[left])
                print('dp', dp[left])
        return dp[0]
