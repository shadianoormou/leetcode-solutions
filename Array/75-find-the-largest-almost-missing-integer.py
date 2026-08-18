from typing import List
from collections import Counter


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        freq = Counter(nums)

        # Every size-1 subarray contains only one element.
        # So any value occurring exactly once is almost missing.
        if k == 1:
            answer = -1

            for num in nums:
                if freq[num] == 1:
                    answer = max(answer, num)

            return answer

        # Whole array is the only subarray.
        if k == n:
            return max(nums)

        # For 1 < k < n, only values at the two ends
        # can appear in exactly one size-k subarray.
        answer = -1

        if freq[nums[0]] == 1:
            answer = max(answer, nums[0])

        if freq[nums[-1]] == 1:
            answer = max(answer, nums[-1])

        return answer
