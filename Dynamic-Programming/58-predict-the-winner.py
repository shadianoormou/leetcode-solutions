from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for left in range(n - 2, -1, -1):
            for right in range(left + 1, n):
                take_left = nums[left] - dp[right]
                take_right = nums[right] - dp[right - 1]
                dp[right] = max(take_left, take_right)

        return dp[n - 1] >= 0
