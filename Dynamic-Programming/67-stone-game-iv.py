from math import isqrt


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [False] * (n + 1)

        for stones in range(1, n + 1):
            for x in range(1, isqrt(stones) + 1):
                square = x * x

                if not dp[stones - square]:
                    dp[stones] = True
                    break

        return dp[n]
