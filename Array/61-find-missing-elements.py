from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        present = set(nums)
        smallest = min(nums)
        largest = max(nums)

        return [
            value
            for value in range(smallest, largest + 1)
            if value not in present
        ]
