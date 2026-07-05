"""
LeetCode 1480 - Running Sum of 1d Array

Difficulty: Easy
Topics: Array, Prefix Sum

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        result = []

        for i in range(len(nums)):
            running_sum += nums[i]
            result.append(running_sum)

        return result
