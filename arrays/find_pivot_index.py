"""
LeetCode 724 - Find Pivot Index

Difficulty: Easy
Topics: Array, Prefix Sum

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1
