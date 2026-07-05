"""
LeetCode 977 - Squares of a Sorted Array

Difficulty: Easy
Topics: Array, Sorting

Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []

        for num in nums:
            new_nums.append(num * num)

        new_nums.sort()

        return new_nums
