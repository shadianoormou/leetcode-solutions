from typing import List

class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        remove_from_front = right + 1
        remove_from_back = n - left
        remove_from_both = left + 1 + n - right

        return min(remove_from_front, remove_from_back, remove_from_both)
