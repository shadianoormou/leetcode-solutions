from typing import List


class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1

                for mid in range(left, right):
                    left_sum = prefix[mid + 1] - prefix[left]
                    right_sum = prefix[right + 1] - prefix[mid + 1]

                    if left_sum < right_sum:
                        dp[left][right] = max(
                            dp[left][right],
                            left_sum + dp[left][mid]
                        )

                    elif left_sum > right_sum:
                        dp[left][right] = max(
                            dp[left][right],
                            right_sum + dp[mid + 1][right]
                        )

                    else:
                        dp[left][right] = max(
                            dp[left][right],
                            left_sum + max(
                                dp[left][mid],
                                dp[mid + 1][right]
                            )
                        )

        return dp[0][n - 1]
