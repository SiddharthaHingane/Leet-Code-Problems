class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        from functools import lru_cache

        suffix_len = len(suffix)
        suffix_num = int(suffix)

        def count_valid(number_str):
            n = len(number_str)

            @lru_cache(None)
            def dp(pos, tight):
                if pos == n:
                    return 1
                res = 0
                if pos >= n - suffix_len:
                    digit = int(suffix[pos - (n - suffix_len)])
                    if tight and digit > int(number_str[pos]):
                        return 0
                    if digit <= limit:
                        res += dp(pos + 1, tight and digit == int(number_str[pos]))
                else:
                    upper = int(number_str[pos]) if tight else limit
                    for d in range(0, upper + 1):
                        if d <= limit:
                            res += dp(pos + 1, tight and d == int(number_str[pos]))
                return res

            return dp(0, True)

        def calc(u):
            if u < suffix_num:
                return 0
            return count_valid(str(u))

        return calc(finish) - calc(start - 1)
